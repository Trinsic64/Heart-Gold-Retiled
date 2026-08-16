import fs from "node:fs";
import path from "node:path";

function pad4(value) {
  return (value + 3) & ~3;
}

function sortedFiles(directory) {
  return fs.readdirSync(directory, { withFileTypes: true })
    .filter((entry) => entry.isFile())
    .map((entry) => path.join(directory, entry.name))
    .sort((left, right) => left.localeCompare(right, "en", { sensitivity: "base" }));
}

function buildNarc(files) {
  const elements = files.map((file) => fs.readFileSync(file));
  const btafSize = 12 + elements.length * 8;
  const btnfSize = 16;
  const dataSize = elements.reduce((position, element) => pad4(position) + element.length, 0);
  const paddedDataSize = pad4(dataSize);
  const gmifSize = 8 + paddedDataSize;
  const fileSize = 16 + btafSize + btnfSize + gmifSize;
  const output = Buffer.alloc(fileSize, 0xff);

  output.write("NARC", 0, "ascii");
  output.writeUInt32LE(0x0100fffe, 4);
  output.writeUInt32LE(fileSize, 8);
  output.writeUInt16LE(16, 12);
  output.writeUInt16LE(3, 14);

  let position = 16;
  output.write("BTAF", position, "ascii");
  output.writeUInt32LE(btafSize, position + 4);
  output.writeUInt32LE(elements.length, position + 8);
  let elementPosition = 0;
  for (let index = 0; index < elements.length; index += 1) {
    elementPosition = pad4(elementPosition);
    output.writeUInt32LE(elementPosition, position + 12 + index * 8);
    elementPosition += elements[index].length;
    output.writeUInt32LE(elementPosition, position + 16 + index * 8);
  }

  position += btafSize;
  output.write("BTNF", position, "ascii");
  output.writeUInt32LE(btnfSize, position + 4);
  output.writeUInt32LE(4, position + 8);
  output.writeUInt32LE(0x10000, position + 12);

  position += btnfSize;
  output.write("GMIF", position, "ascii");
  output.writeUInt32LE(gmifSize, position + 4);
  const dataStart = position + 8;
  elementPosition = 0;
  for (const element of elements) {
    elementPosition = pad4(elementPosition);
    element.copy(output, dataStart + elementPosition);
    elementPosition += element.length;
  }
  return output;
}

function readNarcElements(buffer) {
  if (buffer.toString("ascii", 0, 4) !== "NARC") throw new Error("Output does not have a NARC header.");
  if (buffer.readUInt32LE(8) !== buffer.length) throw new Error("NARC file-size header is invalid.");
  const btafOffset = 16;
  if (buffer.toString("ascii", btafOffset, btafOffset + 4) !== "BTAF") throw new Error("NARC has no BTAF section.");
  const count = buffer.readUInt32LE(btafOffset + 8);
  const btnfOffset = btafOffset + buffer.readUInt32LE(btafOffset + 4);
  if (buffer.toString("ascii", btnfOffset, btnfOffset + 4) !== "BTNF") throw new Error("NARC has no BTNF section.");
  const gmifOffset = btnfOffset + buffer.readUInt32LE(btnfOffset + 4);
  if (buffer.toString("ascii", gmifOffset, gmifOffset + 4) !== "GMIF") throw new Error("NARC has no GMIF section.");
  const dataStart = gmifOffset + 8;
  const elements = [];
  for (let index = 0; index < count; index += 1) {
    const start = buffer.readUInt32LE(btafOffset + 12 + index * 8);
    const end = buffer.readUInt32LE(btafOffset + 16 + index * 8);
    elements.push(buffer.subarray(dataStart + start, dataStart + end));
  }
  return elements;
}

const [inputDirectory, outputPath] = process.argv.slice(2);
if (!inputDirectory || !outputPath) {
  console.error("Usage: node tools/build-narc-from-folder.mjs <input folder> <output NARC>");
  process.exit(2);
}

const files = sortedFiles(inputDirectory);
if (!files.length) throw new Error(`No files found in ${inputDirectory}.`);
const output = buildNarc(files);
const unpacked = readNarcElements(output);
if (unpacked.length !== files.length) throw new Error(`Built NARC contains ${unpacked.length} elements instead of ${files.length}.`);
for (let index = 0; index < files.length; index += 1) {
  if (!unpacked[index].equals(fs.readFileSync(files[index]))) throw new Error(`NARC round-trip mismatch at member ${index}.`);
}
fs.mkdirSync(path.dirname(outputPath), { recursive: true });
fs.writeFileSync(outputPath, output);
console.log(JSON.stringify({
  inputDirectory: path.resolve(inputDirectory),
  outputPath: path.resolve(outputPath),
  members: files.length,
  bytes: output.length,
  roundTripVerified: true,
}, null, 2));
