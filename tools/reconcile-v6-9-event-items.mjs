import fs from "node:fs";
import path from "node:path";

const ITEM_OVERWORLD_TYPE = 3;
const RARE_MAX_EFFECTIVE_RATE = 5;

function parseCsv(text) {
  const records = [];
  let row = [];
  let cell = "";
  let quoted = false;
  for (let index = 0; index < text.length; index += 1) {
    const character = text[index];
    if (quoted) {
      if (character === '"' && text[index + 1] === '"') {
        cell += '"';
        index += 1;
      } else if (character === '"') quoted = false;
      else cell += character;
    } else if (character === '"') quoted = true;
    else if (character === ",") {
      row.push(cell);
      cell = "";
    } else if (character === "\n") {
      row.push(cell.replace(/\r$/, ""));
      if (row.some(Boolean)) records.push(row);
      row = [];
      cell = "";
    } else cell += character;
  }
  if (cell || row.length) {
    row.push(cell.replace(/\r$/, ""));
    if (row.some(Boolean)) records.push(row);
  }
  const [headers, ...rows] = records;
  return {
    headers,
    rows,
    objects: rows.map((values) => Object.fromEntries(headers.map((header, index) => [header, values[index] ?? ""]))),
  };
}

function csvCell(value) {
  const string = String(value ?? "");
  return /[",\r\n]/.test(string) ? `"${string.replaceAll('"', '""')}"` : string;
}

function writeCsv(filePath, rows, columns = Object.keys(rows[0] ?? {})) {
  const output = [columns.join(","), ...rows.map((row) => columns.map((column) => csvCell(row[column])).join(","))].join("\r\n") + "\r\n";
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, output);
}

function eventOverworldOffset(buffer, expectedIndex) {
  let position = 0;
  const spawnableCount = buffer.readUInt32LE(position);
  position += 4 + spawnableCount * 0x14;
  const overworldCount = buffer.readUInt32LE(position);
  position += 4;
  if (expectedIndex < 0 || expectedIndex >= overworldCount) {
    throw new Error(`Overworld index ${expectedIndex} is outside count ${overworldCount}.`);
  }
  return position + expectedIndex * 0x20;
}

function eventOverworldSection(buffer) {
  let position = 0;
  const spawnableCount = buffer.readUInt32LE(position);
  position += 4 + spawnableCount * 0x14;
  const countOffset = position;
  const count = buffer.readUInt32LE(countOffset);
  return { countOffset, count, recordsOffset: countOffset + 4 };
}

function objectIndicesWithFlag(buffer, flag) {
  const section = eventOverworldSection(buffer);
  const indices = [];
  for (let index = 0; index < section.count; index += 1) {
    if (buffer.readUInt16LE(section.recordsOffset + index * 0x20 + 8) === flag) indices.push(index);
  }
  return indices;
}

function insertOverworldRecord(buffer, index, record) {
  if (record.length !== 0x20) throw new Error(`Cannot insert an overworld record with length ${record.length}.`);
  const section = eventOverworldSection(buffer);
  if (index < 0 || index > section.count) throw new Error(`Cannot insert overworld index ${index} into count ${section.count}.`);
  const insertionOffset = section.recordsOffset + index * 0x20;
  const output = Buffer.concat([buffer.subarray(0, insertionOffset), record, buffer.subarray(insertionOffset)]);
  output.writeUInt32LE(section.count + 1, section.countOffset);
  return output;
}

function objectKey(eventFile, objectIndex) {
  return `${Number(eventFile)}:${Number(objectIndex)}`;
}

function normalizeSpecies(value) {
  return String(value ?? "")
    .replace(/^SPECIES_/, "")
    .replace(/\s+Lvl(?:\s+\d+(?:-\d+)?)?.*$/i, "")
    .toUpperCase()
    .replace(/[^A-Z0-9]/g, "");
}

function speciesHeldItems(speciesSource, relevantItems) {
  const holdersByItem = new Map([...relevantItems].map((item) => [item, []]));
  let currentSpecies = "";
  for (const line of speciesSource.split(/\r?\n/)) {
    const speciesMatch = line.match(/^\s*\[(SPECIES_[A-Z0-9_]+)\]\s*=/);
    if (speciesMatch) currentSpecies = speciesMatch[1];
    const itemMatch = line.match(/^\s*\.(common|rare)\s*=\s*(ITEM_[A-Z0-9_]+)/);
    if (!itemMatch || !currentSpecies || !holdersByItem.has(itemMatch[2])) continue;
    holdersByItem.get(itemMatch[2]).push({ species: currentSpecies, heldSlot: itemMatch[1] });
  }
  return holdersByItem;
}

function encounterRarity(encounterCsv, holders) {
  const holderNames = new Set(holders.map((holder) => normalizeSpecies(holder.species)));
  const rateColumns = [];
  const conditionalColumns = [];
  for (let index = 0; index < encounterCsv.headers.length; index += 1) {
    const header = encounterCsv.headers[index];
    const rateMatch = header.match(/^(Wild|Surf|Old Rod|Good Rod|Super Rod|Rock Smash) (\d+)%$/);
    if (rateMatch) rateColumns.push({ index, method: rateMatch[1], rate: Number(rateMatch[2]) });
    else if (/^(Wild|Surf|Good Rod|Super Rod) Swarm$|^(Sinnoh|Hoenn) \d+$/.test(header)) conditionalColumns.push(index);
  }

  let maximumEffectiveRate = 0;
  let ordinaryMatches = 0;
  let conditionalMatches = 0;
  const locations = new Set();
  for (const values of encounterCsv.rows) {
    const ratesByMethod = new Map();
    for (const column of rateColumns) {
      if (!holderNames.has(normalizeSpecies(values[column.index]))) continue;
      ratesByMethod.set(column.method, (ratesByMethod.get(column.method) ?? 0) + column.rate);
      ordinaryMatches += 1;
      if (values[2]) locations.add(values[2]);
    }
    maximumEffectiveRate = Math.max(maximumEffectiveRate, ...ratesByMethod.values(), 0);
    for (const index of conditionalColumns) {
      if (!holderNames.has(normalizeSpecies(values[index]))) continue;
      conditionalMatches += 1;
      if (values[2]) locations.add(values[2]);
    }
  }
  return {
    maximumEffectiveRate,
    ordinaryMatches,
    conditionalMatches,
    locations: [...locations].sort(),
  };
}

function backupOnce(source, destination) {
  if (fs.existsSync(destination)) return;
  fs.mkdirSync(path.dirname(destination), { recursive: true });
  fs.copyFileSync(source, destination);
}

function validateHighIdExpandedScript(contentsDir, row) {
  if (row.pickup_strategy !== "local-high-id-item-ball") return;
  const scriptFile = String(Number(row.script_files)).padStart(4, "0");
  const expandedPath = path.join(contentsDir, "expanded", "scripts", `${scriptFile}.script`);
  const text = fs.readFileSync(expandedPath, "utf8");
  const scriptNumber = Number(row.local_script_number);
  const startMatch = new RegExp(`^Script ${scriptNumber}:\\s*$`, "m").exec(text);
  const scriptBlock = startMatch
    ? text.slice(startMatch.index, text.indexOf("\nScript ", startMatch.index + startMatch[0].length) < 0
      ? text.indexOf("//===== FUNCTIONS", startMatch.index + startMatch[0].length)
      : text.indexOf("\nScript ", startMatch.index + startMatch[0].length))
    : "";
  const itemPattern = new RegExp(`^\\s*SetVar 0x8004 (?:${row.new_item_constant}|${Number(row.new_item_id)})\\s*$`, "m");
  if (!scriptBlock || !itemPattern.test(scriptBlock)) {
    throw new Error(`${row.new_item_constant}: expanded script ${scriptFile} does not resolve local script ${row.local_script_number} to item ${row.new_item_id}.`);
  }
}

const [contentsDir, manifestPath, inventoryPath, heldPath, encountersPath, speciesPath, outputDir, mode = "--dry-run", backupDirArg = "", sourceEventDir = ""] = process.argv.slice(2);
if (!outputDir || !["--dry-run", "--apply"].includes(mode)) {
  console.error("Usage: node tools/reconcile-v6-9-event-items.mjs <DSPRE contents> <v6-6 manifest.csv> <original inventory.csv> <held registry.csv> <encounters.csv> <Species.c> <output dir> [--dry-run|--apply] [backup dir] [source event dir]");
  process.exit(2);
}

const manifest = parseCsv(fs.readFileSync(manifestPath, "utf8")).objects;
const inventory = parseCsv(fs.readFileSync(inventoryPath, "utf8")).objects;
const heldRows = parseCsv(fs.readFileSync(heldPath, "utf8")).objects;
const encounters = parseCsv(fs.readFileSync(encountersPath, "utf8"));
const heldByItem = new Map(heldRows.map((row) => [row.item_constant, row]));
const manifestByObject = new Map(manifest.map((row) => [objectKey(row.event_file, row.event_object_index), row]));
const inventoryByObject = new Map(inventory.map((row) => [objectKey(row.event_file, row.event_object_index), row]));
const relevantItems = new Set(manifest.map((row) => row.new_item_constant));
const holdersByItem = speciesHeldItems(fs.readFileSync(speciesPath, "utf8"), relevantItems);
const decisionsByItem = new Map();

for (const row of manifest) {
  const registry = heldByItem.get(row.new_item_constant);
  const holders = holdersByItem.get(row.new_item_constant) ?? [];
  if (!holders.length && registry?.assigned_species) {
    holders.push({ species: registry.assigned_species, heldSlot: registry.held_slot || "scripted" });
  }
  const rarity = encounterRarity(encounters, holders);
  let disposition;
  let reason;
  if (row.placement_status === "existing") {
    disposition = "keep-ground-mega";
    reason = "Pre-v6.6 ground Mega pickup; no earlier non-Mega item exists in the audited source inventory";
  } else if (!holders.length || registry?.status === "not-assigned") {
    disposition = "keep-ground-mega";
    reason = "No catchable family member has this Mega Stone as a held item";
  } else if (/static|primal/.test(registry?.status ?? "")) {
    disposition = "keep-ground-mega";
    reason = "Held source is a rare/static encounter";
  } else if (rarity.maximumEffectiveRate <= RARE_MAX_EFFECTIVE_RATE) {
    disposition = "keep-ground-mega";
    reason = rarity.maximumEffectiveRate > 0
      ? `Wild holder is rare (maximum effective ordinary encounter rate ${rarity.maximumEffectiveRate}%)`
      : "Wild holder is conditional-only or otherwise rare";
  } else {
    disposition = "restore-original-item";
    reason = `Wild family holder reaches ${rarity.maximumEffectiveRate}% effective encounter rate`;
  }
  decisionsByItem.set(row.new_item_constant, { registry, holders, rarity, disposition, reason });
}

const decisionRows = manifest.map((row) => {
  const decision = decisionsByItem.get(row.new_item_constant);
  return {
    event_file: Number(row.event_file),
    event_object_index: Number(row.event_object_index),
    location: row.location,
    mega_stone: row.new_item_constant,
    original_item: row.old_item_constant,
    placement_status: row.placement_status,
    held_species: decision.holders.map((holder) => holder.species).join(";"),
    held_slots: decision.holders.map((holder) => holder.heldSlot).join(";"),
    held_registry_status: decision.registry?.status ?? "missing",
    max_effective_encounter_rate_percent: decision.rarity.maximumEffectiveRate || "",
    ordinary_slot_matches: decision.rarity.ordinaryMatches,
    conditional_matches: decision.rarity.conditionalMatches,
    wild_locations: decision.rarity.locations.join(";"),
    disposition: decision.disposition,
    reason: decision.reason,
  };
});

const changes = [];
const auditRows = [];
const backupDir = backupDirArg || path.join(outputDir, "backups", "before-event-item-reconciliation");
for (const original of inventory) {
  const key = objectKey(original.event_file, original.event_object_index);
  const mega = manifestByObject.get(key);
  const decision = mega ? decisionsByItem.get(mega.new_item_constant) : null;
  let desiredScript = Number(original.script_number);
  let desiredItemId = Number(original.item_id);
  let desiredItemConstant = original.item_constant;
  let action = "classify-original-pickup";
  if (mega && decision.disposition === "keep-ground-mega") {
    desiredScript = Number(mega.event_script_number);
    desiredItemId = Number(mega.new_item_id);
    desiredItemConstant = mega.new_item_constant;
    action = "keep-ground-mega";
    validateHighIdExpandedScript(contentsDir, mega);
  } else if (mega) {
    action = "restore-original-item";
  }

  const eventFileName = String(Number(original.event_file)).padStart(4, "0");
  const eventPath = path.join(contentsDir, "unpacked", "eventFiles", eventFileName);
  let buffer = fs.readFileSync(eventPath);
  const targetFlag = Number(original.flag);
  let matchingIndices = objectIndicesWithFlag(buffer, targetFlag);
  let restoredMissingObject = false;
  if (!matchingIndices.length) {
    if (!sourceEventDir) throw new Error(`${key}: pickup flag ${targetFlag} is absent and no source event directory was supplied.`);
    const sourcePath = path.join(sourceEventDir, eventFileName);
    const sourceBuffer = fs.readFileSync(sourcePath);
    const sourceOffset = eventOverworldOffset(sourceBuffer, Number(original.event_object_index));
    const sourceRecord = sourceBuffer.subarray(sourceOffset, sourceOffset + 0x20);
    if (sourceRecord.readUInt16LE(8) !== targetFlag) {
      throw new Error(`${key}: source event record flag ${sourceRecord.readUInt16LE(8)} does not match audited flag ${targetFlag}.`);
    }
    buffer = insertOverworldRecord(buffer, Number(original.event_object_index), sourceRecord);
    matchingIndices = objectIndicesWithFlag(buffer, targetFlag);
    restoredMissingObject = true;
  }
  if (matchingIndices.length !== 1) throw new Error(`${key}: expected one overworld with pickup flag ${targetFlag}, found ${matchingIndices.length}.`);
  const actualObjectIndex = matchingIndices[0];
  const offset = eventOverworldOffset(buffer, actualObjectIndex);
  const beforeType = buffer.readUInt16LE(offset + 6);
  const beforeFlag = buffer.readUInt16LE(offset + 8);
  const beforeScript = buffer.readUInt16LE(offset + 10);
  if (!Number.isInteger(desiredItemId) || desiredItemId <= 0) throw new Error(`${key}: no valid item ID resolved.`);
  if (desiredScript >= 7000 && desiredScript < 8000 && desiredScript - 7000 !== desiredItemId) {
    throw new Error(`${key}: global item script ${desiredScript} does not resolve to item ID ${desiredItemId}.`);
  }
  const needsChange = restoredMissingObject || beforeType !== ITEM_OVERWORLD_TYPE || beforeScript !== desiredScript;
  if (needsChange) {
    changes.push({ key, eventPath, eventFileName, offset, beforeType, beforeScript, desiredScript, restoredMissingObject });
    if (mode === "--apply") {
      backupOnce(eventPath, path.join(backupDir, "unpacked", "eventFiles", eventFileName));
      buffer.writeUInt16LE(ITEM_OVERWORLD_TYPE, offset + 6);
      buffer.writeUInt16LE(desiredScript, offset + 10);
      fs.writeFileSync(eventPath, buffer);
    }
  }
  auditRows.push({
    event_file: Number(original.event_file),
    event_object_index: Number(original.event_object_index),
    actual_object_index: actualObjectIndex,
    location: original.locations,
    flag: Number(original.flag),
    before_type: beforeType,
    after_type: ITEM_OVERWORLD_TYPE,
    before_script: beforeScript,
    after_script: desiredScript,
    resolved_item_id: desiredItemId,
    resolved_item_constant: desiredItemConstant,
    action,
    restored_missing_object: restoredMissingObject ? "yes" : "no",
    changed: needsChange ? "yes" : "no",
  });
}

if (inventory.length !== 257) throw new Error(`Expected 257 audited pickup objects, found ${inventory.length}.`);
if (new Set(inventory.map((row) => objectKey(row.event_file, row.event_object_index))).size !== inventory.length) {
  throw new Error("Original pickup inventory contains duplicate event objects.");
}

if (mode === "--apply") {
  for (const row of auditRows) {
    const eventPath = path.join(contentsDir, "unpacked", "eventFiles", String(row.event_file).padStart(4, "0"));
    const buffer = fs.readFileSync(eventPath);
    const matchingIndices = objectIndicesWithFlag(buffer, row.flag);
    if (matchingIndices.length !== 1) throw new Error(`${objectKey(row.event_file, row.event_object_index)}: post-patch flag lookup failed.`);
    const offset = eventOverworldOffset(buffer, matchingIndices[0]);
    if (buffer.readUInt16LE(offset + 6) !== ITEM_OVERWORLD_TYPE) throw new Error(`${objectKey(row.event_file, row.event_object_index)}: post-patch item type validation failed.`);
    if (buffer.readUInt16LE(offset + 10) !== row.after_script) throw new Error(`${objectKey(row.event_file, row.event_object_index)}: post-patch item script validation failed.`);
  }
  fs.mkdirSync(outputDir, { recursive: true });
  writeCsv(path.join(outputDir, "mega-ground-pickup-decisions.csv"), decisionRows);
  writeCsv(path.join(outputDir, "event-item-audit.csv"), auditRows);
}

const summary = {
  mode,
  contentsDir: path.resolve(contentsDir),
  rarityRule: `keep ground Mega pickup when the holder's maximum effective ordinary encounter rate is <= ${RARE_MAX_EFFECTIVE_RATE}%, conditional/static, or unavailable`,
  pickupObjectsAudited: auditRows.length,
  pickupObjectsChanged: changes.length,
  noneTypesCorrected: changes.filter((change) => change.beforeType !== ITEM_OVERWORLD_TYPE).length,
  scriptsCorrected: changes.filter((change) => change.beforeScript !== change.desiredScript).length,
  missingPickupObjectsRestored: changes.filter((change) => change.restoredMissingObject).length,
  originalItemsRestored: decisionRows.filter((row) => row.disposition === "restore-original-item").length,
  groundMegaPickupsKept: decisionRows.filter((row) => row.disposition === "keep-ground-mega").length,
  keptRareOrStatic: decisionRows.filter((row) => row.disposition === "keep-ground-mega" && /rare|static|conditional/i.test(row.reason)).length,
  keptNoHeldSource: decisionRows.filter((row) => /No catchable/.test(row.reason)).length,
  keptPreExisting: decisionRows.filter((row) => /Pre-v6\.6/.test(row.reason)).length,
  restoredMegaStones: decisionRows
    .filter((row) => row.disposition === "restore-original-item")
    .map((row) => `${row.mega_stone} -> ${row.original_item} (${row.max_effective_encounter_rate_percent}%)`),
  keptRareWildMegaStones: decisionRows
    .filter((row) => row.disposition === "keep-ground-mega" && /maximum effective/.test(row.reason))
    .map((row) => `${row.mega_stone} (${row.max_effective_encounter_rate_percent}%)`),
  backupDir: mode === "--apply" ? path.resolve(backupDir) : null,
  outputDir: mode === "--apply" ? path.resolve(outputDir) : null,
};
if (mode === "--apply") fs.writeFileSync(path.join(outputDir, "summary.json"), `${JSON.stringify(summary, null, 2)}\n`);
console.log(JSON.stringify(summary, null, 2));
