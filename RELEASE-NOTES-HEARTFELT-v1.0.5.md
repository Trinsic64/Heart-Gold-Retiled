# Pokémon Heartfelt Gold v1.0.5

## Changes

- EXP All implemented.
- Expanded marts and department stores.
- Auspicious Armor unlocks in marts after Gym 5.
- Malicious Armor unlocks in marts after Gym 5.
- Scroll of Water and Scroll of Darkness unlock in marts after Gym 6.
- Cheaper mart items.
- Mega Stones, Evolution Stones, Nature Mints, and more added to department stores.
- Updated Trainer AI.

Use **Exp. Share** in the Bag to toggle EXP All on or off. With sharing enabled, participating Pokémon receive their full calculated EXP and healthy non-Egg non-participants receive half. The setting persists when you save. Existing level scaling and level caps still apply.

Includes the optional Level Cap NPC and fixes from v1.0.4 and earlier.

## Updating

Apply `Heartfelt-Gold-v1.0.5-Patch.xdelta` directly to a clean Pokémon HeartGold (USA) ROM. Apply one patch to the clean ROM; do not stack it over an earlier Heartfelt Gold release.

In-game saves from earlier Heartfelt Gold versions are expected to remain compatible. Back up your save, then import or copy it for the new ROM, matching filenames where required by your emulator. Load the in-game save instead of an emulator save state from an older build.

## Patch and source ROM

- Patch: `Heartfelt-Gold-v1.0.5-Patch.xdelta`
- Patch size: 34,552,621 bytes
- Patch SHA-256: `d814036e86628e9d0512701094dc7f9ac54a11d6b3aebc716a837f77ccf74506`
- Required source: clean Pokémon HeartGold (USA).
- Source MD5: `258cea3a62ac0d6eb04b5a0fd764d788`
- Source SHA-1: `4fcded0e2713dc03929845de631d0932ea2b5a37`
- Source SHA-256: `65f02a56842b75aa92d775d56d657a56fe3fa993550b04dc20704ab82d760105`
- Decoded ROM size: 209,654,240 bytes
- Decoded ROM SHA-256: `ecb1a9f716a12d8737c9697eaa693fc9fc88fff809852328c535aca902e0799b`

## Verification

The release patch decoded against the clean USA source and reproduced the completed v11-Test1 EXP All engine build byte for byte. The build audit passed: all 627 map headers, 1,139 script banks, and existing dialogue were preserved from v11-Test1, with two EXP All toggle messages appended to bag text bank 10. The engine-generated item attributes and trainer data are the other named filesystem differences from that input.

Tests of the actual EXP code passed for both flat and scaled formulas, including multiple participants, Eggs, fainted Pokémon, and compatibility with held Exp. Shares from older saves. Source review confirms the five-badge Armor unlocks and six-badge Scroll unlocks. In-game testing remains necessary; these automated checks do not certify battle or menu behavior on an emulator or hardware.

EXP All is adapted from [zebben's exp-share branch](https://github.com/zebben/hg-engine/tree/exp-share), with additional handling for Eggs and held Exp. Shares in existing saves.

The player download is the `.xdelta` asset. The accompanying `checksums.sha256` file verifies downloads.
