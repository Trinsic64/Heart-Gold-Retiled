# Pokémon Heartfelt Gold v1.0.4

Adds an optional **Level Cap NPC** to 24 Pokémon Centers across Johto and Kanto. Speak to the NPC to see the current cap, disable it by setting it to 100, restore the badge-based cap, or adjust it one level at a time. The menu can be cancelled, and adjustments stop at levels 1 and 100.

This release includes the Route 42 Hiker fix and the regional-form, battle sprite positioning, and Pokédex fixes from v1.0.3 and earlier.

## Updating and save compatibility

In-game saves from earlier Heartfelt Gold versions are expected to remain compatible; this update does not change the save layout. Back up your save, then import or copy it for the new ROM. Match its filename to the ROM where required by your emulator. Boot from the in-game save instead of restoring an emulator save state made with an older build.

Download `Heartfelt-Gold-v1.0.4-Patch.xdelta` and apply it directly to a clean Pokémon HeartGold (USA) ROM. Do not apply it over an older patched ROM. Transfer your save separately.

## Patch and source ROM

- Patch: `Heartfelt-Gold-v1.0.4-Patch.xdelta`
- Patch size: 39,723,007 bytes
- Patch SHA-256: `19ffd05cf2e2a11b0e75697ba91ae721ed55cbe3677a61d89889af3ac03d903b`
- Required source: clean Pokémon HeartGold (USA).
- Source MD5: `258cea3a62ac0d6eb04b5a0fd764d788`
- Source SHA-1: `4fcded0e2713dc03929845de631d0932ea2b5a37`
- Source SHA-256: `65f02a56842b75aa92d775d56d657a56fe3fa993550b04dc20704ab82d760105`
- Decoded ROM size: 209,652,192 bytes
- Decoded ROM SHA-256: `85095dff98cc5af3290a3d6f21fc9788ec657347a17a11d16040931d8555f480`

## Verification

The supplied xDelta decoded against the clean USA source and reproduced the v9 HG-Engine clean build byte for byte. The build audit passed: all 627 map headers, 1,139 script members, and 943 text members match the v9 Test input. All 24 Level Cap NPCs are bound to their Center scripts in the decoded ROM. The only named filesystem difference from the v9 Test input is bonus Chuck's trainer party, whose levels follow the current HG-Engine source (five at 36 and one at 38).

The NPC interactions have not yet been playtested in game. The player download is the `.xdelta` asset. The accompanying `checksums.sha256` file verifies downloads.
