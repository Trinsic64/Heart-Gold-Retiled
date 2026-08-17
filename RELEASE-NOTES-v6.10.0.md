# HeartGold Retiled Expansion v6.10.0

This trainer-focused release updates the expansion patch to the newly authored HG-Engine roster and synchronizes the player-facing trainer documentation with the exact source used by the build.

## Download

- **Patch:** `HG-Retiled-Expansion-Patch.xdelta`
- **Size:** 35.9 MiB (37,646,242 bytes)
- **SHA-256:** `1C0D6FAF4CB402B67AF4D56DD17C232C23EF2BC836CDE304280249F5948E2197`

Apply this patch to a clean, legally obtained **Pokémon HeartGold (USA)** ROM matching the hashes in the repository README. Apply only this patch; do not stack it with another Retiled patch.

## Trainer roster update

- The release now includes the edited HG-Engine `Trainers.c` authoring source.
- All 738 trainer records and 2,843 party members parse successfully.
- The Trainer Guide has been regenerated from the new source, updating 233 trainer entries relative to the previous guide.
- Major-team tables now reflect the configured party order, held items, custom moves, and battle items.
- The walkthrough's Johto Gyms, first Pokémon League challenge, Kanto Gyms, Blue, and Red checkpoints now match the edited roster.
- Notable changes include expanded or rebuilt teams for Chuck, Pryce, Will, Koga, Karen, Brock, Misty, Lt. Surge, Erika, Janine, and Sabrina.

## Validation

- The patch has a valid VCDIFF/xDelta header and the SHA-256 above was recomputed after promoting the new patch to the canonical download filename.
- Trainer Forge parsed all 738 records and 2,843 party members, rejected all 48 numeric engine filler slots, validated every party species and structural field, confirmed item references, and completed lossless C export round-trip tests.
- The complete trainer index and walkthrough boss summaries were regenerated directly from `HG-Engine/data/Trainers.c`.
- A checksum-valid decode against the clean source ROM was not rerun in this workspace; test the published patch end-to-end against the compatible clean ROM before distributing it broadly.

## Work-in-progress warnings

- The project remains a work in progress and may contain map/tile issues or gameplay bugs.
- A full runtime playthrough has not been completed for this release.
- Keep rotating save backups while testing the new trainer balance.
- Z-Moves, Dynamax/Gigantamax, Terastallization, discontinued online services, Pal Park replacement, and Pokéwalker replacement are not included.

No ROM is included. This release contains only a binary difference patch, HG-Engine trainer authoring source, and documentation.
