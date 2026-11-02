# Pokémon Heartfelt Gold v1.0.3

Fixes the crash when interacting with the Hiker on **Route 42**. Includes all v1.0.2 regional-form, battle sprite positioning, and Pokédex fixes.

## Updating and save compatibility

**Compatible with in-game saves from previous Heartfelt Gold versions. No new game is required.** Back up your save, then import or copy it for the new ROM. Match its filename to the ROM where required by your emulator. Boot from the in-game save instead of restoring an emulator save state made with an older build.

Download `Heartfelt-Gold-v1.0.3-Patch.xdelta` and apply it directly to a clean Pokémon HeartGold (USA) ROM. Do not apply it over an older patched ROM. Transfer your save separately.

## Patch and source ROM

- Patch: `Heartfelt-Gold-v1.0.3-Patch.xdelta`
- Patch size: 39,712,167 bytes
- Patch SHA-256: `8b8bef11e6305adfd47ab42db5604a24cf20908b28284e035ae43f38c33d6575`
- Required source: clean Pokémon HeartGold (USA).
- Source MD5: `258cea3a62ac0d6eb04b5a0fd764d788`
- Source SHA-1: `4fcded0e2713dc03929845de631d0932ea2b5a37`
- Source SHA-256: `65f02a56842b75aa92d775d56d657a56fe3fa993550b04dc20704ab82d760105`
- Decoded ROM size: 209,627,616 bytes
- Decoded ROM SHA-256: `0907cbe60a314af3cc6bb2c6eed292430cb1fbc0fbc424eb0faa390085410143`

## Verification

The supplied xDelta decoded against the clean USA source and reproduced the hg-engine v8 build byte for byte. The hg-engine build and DSPRE archive audit passed, with all 384 named files matching the owner's corrected input ROM, including the changed archive. The Route 42 correction was supplied by the project owner.

The player download is the `.xdelta` asset. The accompanying `checksums.sha256` file verifies downloads.
