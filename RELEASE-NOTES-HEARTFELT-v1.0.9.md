# Pokémon Heartfelt Gold v1.0.9

Adds **999 Rare Candies above Professor Elm's Lab** in New Bark Town.

## What's changed

- Added a reward of **999 Rare Candies above Professor Elm's Lab**.
- Includes all features and fixes from v1.0.8, including scripted expanded-item pickups, Ruins of Alph encounter fixes, centered battle sprites, the original overworld camera and the new indoor camera settings.

## Updating

Apply `Heartfelt-Gold-v1.0.9-Patch.xdelta` directly to a clean **Pokémon HeartGold (USA)** ROM matching the hashes below. Apply one patch to the clean ROM; do not stack it over v1.0.8 or another patched ROM.

In-game saves from earlier Heartfelt Gold versions are expected to remain compatible. Back up your save, then import or copy it for the new ROM, matching filenames where required by your emulator. Load the in-game save instead of an emulator save state from an older build. Previously collected item rewards remain collected on existing saves.

## Patch and source ROM

- Patch: `Heartfelt-Gold-v1.0.9-Patch.xdelta`
- Patch size: 39,295,194 bytes
- Patch SHA-256: `55735dca98762490df6062113a9124bf906c5e4e63b265ce7c624713dcf65d56`
- Required source: clean Pokémon HeartGold (USA).
- Source MD5: `258cea3a62ac0d6eb04b5a0fd764d788`
- Source SHA-1: `4fcded0e2713dc03929845de631d0932ea2b5a37`
- Source SHA-256: `65f02a56842b75aa92d775d56d657a56fe3fa993550b04dc20704ab82d760105`
- Decoded ROM size: 207,710,176 bytes
- Decoded ROM SHA-256: `b1284f79671df317ca4b6c9e2db32195cd100efff60367832288eb9c25e67fd6`

## Verification and known limits

The supplied patch decoded successfully against the documented clean USA source and reproduced the v21 hg-engine output byte for byte. The build's preservation audit passed for protected project data, configuration, messages, scripts, items, dynamic headers and the input ROM's camera table.

The Rare Candy addition was supplied by the project author. Release packaging verification does not constitute a full playthrough or hardware test. No new save/reload test was performed for v1.0.9.

The project remains a work in progress, with some awkward or glitchy tiles and incomplete hg-engine battle/form features. Prior known engine issues are not advertised as resolved by this release.

Please report problems through [GitHub Issues](https://github.com/Trinsic64/Heartfelt-Gold/issues), including the release version, location and steps to reproduce.

Engine updates are based on [hg-engine](https://github.com/BluRosie/hg-engine). EXP All is adapted from [zebben's exp-share branch](https://github.com/zebben/hg-engine/tree/exp-share), with additional handling for Eggs and held Exp. Shares in existing saves.

Download the `.xdelta` asset to play. The accompanying `checksums.sha256` file verifies downloads. No ROM or save is distributed.
