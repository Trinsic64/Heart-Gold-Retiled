# Pokémon Heartfelt Gold v1.0.8

A corrective update to v1.0.7, fixing item pickups, Ruins of Alph encounters, battle sprite placement and camera settings.

## What's changed

1. **Fixed hg-engine/DSPRE ground-item incompatibility.** Expanded items that could not be picked up through the event item numbering are now given through explicit scripts. Other ground rewards have been replaced with suitable items.
2. **Fixed Ruins of Alph encounters.** Includes the final encounter corrections following v1.0.7.
3. **Centered battle sprites.** Restored the intended placement of affected regional, Mega and Primal forms in the battle frame.
4. **Kept the original overworld camera.** The zoomed overworld camera advertised in v1.0.7 has been reverted.
5. **Included the new indoor camera settings.** The indoor camera changes are preserved in this build.

Includes the earlier Heartfelt Gold features and fixes, including updated hg-engine sprites, Dragon's Den encounters, Gym level-cap fixes and corrected Pokémon evolutions.

## Updating

Apply `Heartfelt-Gold-v1.0.8-Patch.xdelta` directly to a clean **Pokémon HeartGold (USA)** ROM matching the hashes below. Apply one patch to the clean ROM; do not stack it over v1.0.7 or another patched ROM.

In-game saves from earlier Heartfelt Gold versions are expected to remain compatible. Back up your save, then import or copy it for the new ROM, matching filenames where required by your emulator. Load the in-game save instead of an emulator save state from an older build. Previously collected item rewards remain collected on existing saves.

## Patch and source ROM

- Patch: `Heartfelt-Gold-v1.0.8-Patch.xdelta`
- Patch size: 39,295,592 bytes
- Patch SHA-256: `ab937cfb6e085684ae46e4dc6fbb1c1267788aee63800f43a0346951aef29c3a`
- Required source: clean Pokémon HeartGold (USA).
- Source MD5: `258cea3a62ac0d6eb04b5a0fd764d788`
- Source SHA-1: `4fcded0e2713dc03929845de631d0932ea2b5a37`
- Source SHA-256: `65f02a56842b75aa92d775d56d657a56fe3fa993550b04dc20704ab82d760105`
- Decoded ROM size: 207,710,688 bytes
- Decoded ROM SHA-256: `a342cf8fc32d81cb529e4be4d8ce7f0d89be06345f71d06ce4aa772d66cb4ca9`

## Verification and known limits

The supplied patch decoded successfully against the documented clean USA source and reproduced the v20 hg-engine output byte for byte. The build's preservation audit passed for protected project data, configuration, messages, scripts, items, dynamic headers and the input ROM's camera table.

The gameplay corrections above were supplied and tested by the project author. Release packaging verification does not constitute a full playthrough or hardware test. No new save/reload test was performed for v1.0.8.

The project remains a work in progress, with some awkward or glitchy tiles and incomplete hg-engine battle/form features. Prior known engine issues are not advertised as resolved by this release.

Please report problems through [GitHub Issues](https://github.com/Trinsic64/Heartfelt-Gold/issues), including the release version, location and steps to reproduce.

Engine updates are based on [hg-engine](https://github.com/BluRosie/hg-engine). EXP All is adapted from [zebben's exp-share branch](https://github.com/zebben/hg-engine/tree/exp-share), with additional handling for Eggs and held Exp. Shares in existing saves.

Download the `.xdelta` asset to play. The accompanying `checksums.sha256` file verifies downloads. No ROM or save is distributed.
