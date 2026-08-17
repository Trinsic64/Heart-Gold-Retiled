# HeartGold Retiled Expansion v6.10.1

This patch-only release promotes the newly supplied v3 xDelta build while retaining the v6.10 trainer roster and synchronized player guides.

## Download

- **Patch:** `HG-Retiled-Expansion-Patch.xdelta`
- **Size:** 35.9 MiB (37,646,354 bytes)
- **SHA-256:** `D63287B23A87CF89AD443A1FF8B786E7141865022F37B57790469FE98D963F9A`

Apply this patch to a clean, legally obtained **Pokémon HeartGold (USA)** ROM matching the hashes in the repository README. Apply only this patch; do not stack it with another Retiled patch.

## Release update

- Replaces the v6.10.0 expansion download with the newly generated v3 xDelta build.
- Retains the edited 738-record HG-Engine trainer roster and its 2,843 party members.
- Retains the synchronized Trainer Guide and walkthrough boss checkpoints introduced in v6.10.0.
- Updates the canonical patch checksum and version references throughout the release documentation.

## Validation

- The promoted artifact is byte-identical to `HG-Retiled-Expansion-Patch-v3.xdelta`.
- The patch has a valid VCDIFF/xDelta header and the SHA-256 above was recomputed after promotion to the canonical download filename.
- Documentation and checksum files were checked for stale v6.10.0 patch references.
- A checksum-valid decode against the clean source ROM was not rerun in this workspace; test the published patch end-to-end against the compatible clean ROM before distributing it broadly.

## Work-in-progress warnings

- The project remains a work in progress and may contain map/tile issues or gameplay bugs.
- A full runtime playthrough has not been completed for this release.
- Keep rotating save backups while testing.
- Z-Moves, Dynamax/Gigantamax, Terastallization, discontinued online services, Pal Park replacement, and Pokéwalker replacement are not included.

No ROM is included. This release contains only a binary difference patch, HG-Engine trainer authoring source, and documentation.
