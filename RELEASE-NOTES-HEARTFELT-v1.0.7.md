# Pokémon Heartfelt Gold v1.0.7 — Major Update

New Ruins of Alph encounters, updated hg-engine sprites, new camera views, and fixes for Dragon's Den encounters, Gym level caps and Pokémon evolutions.

## What's changed

1. **Ruins of Alph encounters are set.**

   | Encounter table | Room |
   |---|---|
   | 10 | Small room — ladder down |
   | 11 | Bottom “ZigZag” room — ladder up |
   | 12 | Puzzle room |
   | 13 | Reward room — four Poké Ball rewards |

2. **Updated hg-engine sprites.** The release includes the newly ported sprite updates.
3. **Fixed Dragon's Den cave encounters.**
4. **New overworld camera:** zoomed in.
5. **New indoor camera:** 3D, zoomed out.
6. **Fixed Gyms automatically setting the level cap.**
7. **Fixed Pokémon evolutions, including Scyther.**

Includes the features from earlier Heartfelt Gold releases: EXP All toggled through Exp. Share, expanded marts and department stores, cheaper items, evolution-item unlocks, updated Trainer AI, the optional Level Cap NPC, and the increased Kanto legendary encounter levels from v1.0.6.

## Updating

Apply `Heartfelt-Gold-v1.0.7-Patch.xdelta` directly to a clean **Pokémon HeartGold (USA)** ROM matching the hashes below. Apply one patch to the clean ROM; do not stack it over v1.0.6 or another patched ROM.

In-game saves from earlier Heartfelt Gold versions are expected to remain compatible. Back up your save, then import or copy it for the new ROM, matching filenames where required by your emulator. Load the in-game save instead of an emulator save state from an older build. A known copied save was successfully loaded, saved and reloaded during this build's verification; this does not establish compatibility with every save or story state.

## Patch and source ROM

- Patch: `Heartfelt-Gold-v1.0.7-Patch.xdelta`
- Patch size: 39,293,966 bytes
- Patch SHA-256: `c37541b75a3efd0802a457ec9f36a53eed324b3cf7a49ac58888fd1d855470d0`
- Required source: clean Pokémon HeartGold (USA).
- Source MD5: `258cea3a62ac0d6eb04b5a0fd764d788`
- Source SHA-1: `4fcded0e2713dc03929845de631d0932ea2b5a37`
- Source SHA-256: `65f02a56842b75aa92d775d56d657a56fe3fa993550b04dc20704ab82d760105`
- Decoded ROM size: 207,710,176 bytes
- Decoded ROM SHA-256: `a6d5dd80112f08f2a7a1eca5fdd735d65e097fb9a86817e48a48042047893246`

## Verification and known limits

The supplied patch decoded against the documented clean USA source and reproduced the validated v18 feature build byte for byte. All 384 named filesystem files retain the v18 input's contents, including all 627 map headers, 1,139 script members, existing dialogue, and the v18 map and matrix changes. Two archive containers were repacked with identical members.

The preservation audit passed for project data, configuration, dynamic-header hooks and custom cameras. A headless copied-save test booted, continued, saved and reloaded in a fresh emulator process without modifying the original save. This release verification is not a full playthrough or a hardware test.

The project remains a work in progress, with some awkward or glitchy tiles and incomplete hg-engine battle/form features. Not every new form has complete front artwork. The prior engine validation also retains known upstream issues involving Disguise, Ice Face, Illusion with Neutralizing Gas, Wandering Spirit when the defender faints, Ripen/Fling and Substitute; these are not advertised as fixed in v1.0.7.

Please report problems through [GitHub Issues](https://github.com/Trinsic64/Heartfelt-Gold/issues), including the release version, location and steps to reproduce.

Engine updates are based on [hg-engine](https://github.com/BluRosie/hg-engine). EXP All is adapted from [zebben's exp-share branch](https://github.com/zebben/hg-engine/tree/exp-share), with additional handling for Eggs and held Exp. Shares in existing saves.

Download the `.xdelta` asset to play. The accompanying `checksums.sha256` file verifies downloads. No ROM or save is distributed.
