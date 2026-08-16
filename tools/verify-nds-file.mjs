import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";

function sha256(buffer) {
  return crypto.createHash("sha256").update(buffer).digest("hex").toUpperCase();
}

function readFileTable(rom) {
  const fntOffset = rom.readUInt32LE(0x40);
  const fntSize = rom.readUInt32LE(0x44);
  const fatOffset = rom.readUInt32LE(0x48);
  const fatSize = rom.readUInt32LE(0x4c);
  if (fntOffset + fntSize > rom.length || fatOffset + fatSize > rom.length) throw new Error("ROM FNT/FAT offsets are outside the file.");
  const rootDirectoryCount = rom.readUInt16LE(fntOffset + 6);
  const files = new Map();

  function visit(directoryId, prefix) {
    const directoryIndex = directoryId & 0x0fff;
    if (directoryIndex >= rootDirectoryCount) throw new Error(`Directory ID ${directoryId.toString(16)} is outside the FNT table.`);
    const entryOffset = fntOffset + directoryIndex * 8;
    let position = fntOffset + rom.readUInt32LE(entryOffset);
    let fileId = rom.readUInt16LE(entryOffset + 4);
    while (true) {
      const descriptor = rom[position++];
      if (descriptor === 0) break;
      const isDirectory = (descriptor & 0x80) !== 0;
      const nameLength = descriptor & 0x7f;
      const name = rom.toString("ascii", position, position + nameLength);
      position += nameLength;
      const currentPath = prefix ? `${prefix}/${name}` : name;
      if (isDirectory) {
        const childDirectoryId = rom.readUInt16LE(position);
        position += 2;
        visit(childDirectoryId, currentPath);
      } else {
        files.set(currentPath, fileId);
        fileId += 1;
      }
    }
  }

  visit(0xf000, "");
  return { files, fatOffset, fatEntries: fatSize / 8 };
}

const [romPath, internalPathArg, expectedPath] = process.argv.slice(2);
if (!expectedPath) {
  console.error("Usage: node tools/verify-nds-file.mjs <ROM.nds> <internal/path> <expected file>");
  process.exit(2);
}
const internalPath = internalPathArg.replaceAll("\\", "/").replace(/^\/+/, "");
const rom = fs.readFileSync(romPath);
const table = readFileTable(rom);
const fileId = table.files.get(internalPath);
if (fileId === undefined) throw new Error(`ROM does not contain ${internalPath}.`);
if (fileId >= table.fatEntries) throw new Error(`File ID ${fileId} is outside the FAT.`);
const start = rom.readUInt32LE(table.fatOffset + fileId * 8);
const end = rom.readUInt32LE(table.fatOffset + fileId * 8 + 4);
if (end < start || end > rom.length) throw new Error(`Invalid FAT range ${start}-${end} for ${internalPath}.`);
const actual = rom.subarray(start, end);
const expected = fs.readFileSync(expectedPath);
const matches = actual.equals(expected);
console.log(JSON.stringify({
  romPath: path.resolve(romPath),
  internalPath,
  fileId,
  bytes: actual.length,
  sha256: sha256(actual),
  expectedPath: path.resolve(expectedPath),
  expectedBytes: expected.length,
  expectedSha256: sha256(expected),
  matches,
}, null, 2));
if (!matches) process.exit(1);
