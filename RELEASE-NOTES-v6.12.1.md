# HeartGold Retiled Expansion v6.12.1

This balance and map-fix release publishes the v10 xDelta build.

## Changes

- Rebalanced Victory Road 2F's two high-level rare encounters:
  - Tyranitar is now level 48 instead of level 55.
  - Zweilous is now level 45 instead of level 50.
- Corrected several BDHC collision plates on Victory Road.
- Updated the tracked encounter source and player guide to reflect the new level range.

## Download

- **Patch:** `HG-Retiled-Expansion-Patch-v10.xdelta`
- **Size:** 35.7 MiB (37,396,262 bytes)
- **SHA-256:** `0B4328C30B1C41CBC9E22CBAC47A35B681F906063AC0F35B31C9A4A8487417F4`

Apply this patch by itself to a clean, legally obtained **Pokémon HeartGold (USA)** ROM matching the hashes in the repository README. Do not stack it with another Retiled patch.

## Validation

- The supplied v10 patch and canonical expansion patch are byte-identical.
- The patch begins with the expected VCDIFF/xDelta header.
- The tracked Victory Road 2F encounter table has a maximum level of 48 and the guide matches its rare-slot values.
- A checksum-valid decode against the clean source ROM was not rerun because no source ROM or xDelta decoder is present in this workspace. Test the published patch end-to-end against the compatible clean ROM before distributing it broadly.

No ROM is included. This release contains only a binary difference patch, source configuration, documentation, and checksums.
