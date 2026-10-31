# Pokémon Heartfelt Gold v1.0.0

This is the first major release under the **Pokémon Heartfelt Gold** name, succeeding HeartGold Retiled Expansion v6.12.1.

## Highlights

- Reworked regular wild encounters and trainer parties throughout Johto and Kanto.
- Added a broad set of scripted Legendary, Mythical, and other special encounters. The [Static Encounter Guide](Docs/Guides/Static-Encounter-Guide.md) records 87 named `WildBattle` commands from the supplied DSPRE script export, with species, level, and script bank.
- Changed the starter choices to Treecko, Torchic, and Mudkip, each holding its matching Mega Stone in the current hg-engine source.
- Configured National Dex access, reusable TMs, forgettable HMs, uncapped overworld and battle frame rate, a variable-driven level cap, and expanded mart inventories.
- Continued map and visual work. See the [player guide index](Docs/Guides/README.md) for encounter, trainer, evolution, and feature details.

## Patch

- File: `xDelta/Heartfelt-Gold-v1-Patch.xdelta`
- Size: 39,711,940 bytes
- SHA-256: `3a7799354f4cb11e0169b9ae3e8f73bfbc334ad83a1b0d58abb3d2260dec4443`

Apply this patch alone to a clean Pokémon HeartGold (USA) ROM matching the source hashes in the [README](README.md). Do not stack it with a Retiled Expansion patch.

## Verification scope

The patch has a VCDIFF/xDelta header and its SHA-256 was computed from the supplied file. It decoded successfully against a clean USA source ROM matching the README hash. The decoded output is byte-identical to the local `Heartfelt-Gold-v3-Release.nds` (209,627,104 bytes; SHA-256 `a1b8f23e65a324212271bbcbaaaa9890093927af24209a4e4b53c96b0c6bdd1b`). The `v1` patch filename denotes this Heartfelt Gold patch release; the matching local ROM build is named `v3-Release`.

The scripting framework scan found no parse or coverage errors in the supplied DSPRE export. The patch was not played through in this release workflow. The static encounter export was provided as identical to the patch's static scripts; locations marked unconfirmed in the guide need an in-game map check. The older `validate-encounters-trainers.mjs` policy check currently stops on an under-level Crobat in the Mt. Mortar Waterfall Room table; its expected evolution and balance rules predate this source update.
