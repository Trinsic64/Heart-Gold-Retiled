.nds

MAP_MAHOGANY equ 87

// The a133 encounter-area archive uses overworld area ID 69 for Mahogany
// Town. In the original game that final table entry is a 0xFFFF sentinel,
// because Mahogany has no wild encounters. Keep the new archive entry and the
// Pokédex overlay's map lookup in sync.

.open "base/overlay/overlay_0018.bin", 0x021E5900

// sOverworldMapIDs[69]: 0xFFFF -> MAP_MAHOGANY (map header 87 / T28)
.org 0x021F99DE
    .halfword MAP_MAHOGANY

// Add Mahogany to the location-sort lookup. MAP_MOUNT_MOON is not a separate
// Pokédex area (Mt. Moon Square is the representative dungeon map), so its
// slot can be reused while retaining the correct alphabetical position.
// sMapIDs_Alphabetical[84]: MAP_MOUNT_MOON -> MAP_MAHOGANY
.org 0x021F9B30
    .word MAP_MAHOGANY

.close
