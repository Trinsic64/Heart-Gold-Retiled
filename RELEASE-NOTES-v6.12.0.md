# HeartGold Retiled Expansion v6.12.0

This feature release publishes the v8 xDelta build and makes later-generation evolution resources obtainable from the Goldenrod Department Store.

## Changes

- Reworked the Goldenrod Department Store inventory:
  - Upper 2F now sells the supported evolution stones, including the Ice Stone.
  - Lower 2F now sells held and consumable evolution items such as the Razor Claw, apples, pots, Galarica items, Linking Cord, Black Augurite, and Peat Block.
  - 3F now sells the Urshifu scrolls, Charcadet armors, Metal Alloy, Ability Capsule, Ability Patch, and Gold Bottle Cap.
  - 4F retains the six vitamin items and 5F retains the existing TM selection.
- Simplified six former Linking Cord evolutions:
  - Kadabra, Machoke, Graveler, and Haunter now evolve at level 36.
  - Boldore and Gurdurr now evolve at level 40.
  - Alolan Graveler remains the sole Linking Cord evolution.
- Included the corresponding HG-Engine mart and evolution source tables for release transparency.

## Download

- **Patch:** `HG-Retiled-Expansion-Patch-v8.xdelta`
- **Size:** 35.9 MiB (37,636,462 bytes)
- **SHA-256:** `5C885FF9C93DDC395C0A0B64184AE96D31273326228DCCA4BDD6E58ECE85A5C4`

Apply this patch by itself to a clean, legally obtained **Pokémon HeartGold (USA)** ROM matching the hashes in the repository README. Do not stack it with another Retiled patch.

## Validation

- The supplied v8 patch and canonical expansion patch are byte-identical.
- The patch begins with the expected VCDIFF/xDelta header.
- The Goldenrod mart lists terminate correctly and all referenced item constants exist in the release item catalogue.
- The six converted evolution tables each contain the expected level method and nine explicit table entries.
- A checksum-valid decode against the clean source ROM was not rerun because no source ROM or xDelta decoder is present in this workspace. Test the published patch end-to-end against the compatible clean ROM before distributing it broadly.

No ROM is included. This release contains only a binary difference patch, source configuration, documentation, and checksums.
