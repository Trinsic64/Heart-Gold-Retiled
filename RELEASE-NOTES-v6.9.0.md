# HeartGold Retiled Expansion v6.9.0

This work-in-progress prerelease reconciles overworld item events and removes unnecessary duplication between ground Mega Stones and practical wild-family held sources.

## Download

- **Patch:** `HG-Retiled-Expansion-Patch.xdelta`
- **Size:** 31.2 MiB (32,753,563 bytes)
- **SHA-256:** `FD13E511E97A4CD126D8E66D6AB59CB3BD0F3673AD18CA04FBBFA9574762C890`

Apply this patch to a clean, legally obtained **Pokémon HeartGold (USA)** ROM matching the hashes in the repository README. Apply only this patch; do not stack it with another Retiled patch.

## Event-item fixes

- All 257 audited overworld pickups are explicitly classified as DSPRE `Item` objects and resolve to valid, non-empty item IDs.
- 166 pickup objects previously shown as `None` were corrected, 15 invalid pickup scripts were repaired, and one missing Route 29 pickup record was reconstructed.
- 13 ground Mega Stones with practical wild-family held sources were restored to their original items.
- 79 ground Mega Stone pickups remain for rare, static, conditional, unavailable, or pre-existing sources.
- Wild-held decisions include eligible prior evolutionary stages, not only the final Mega-capable species.
- The item guide now documents the retained ground stones, held-source-only stones, and all 13 restored pickups.

## Validation

- Clean source ROM SHA-256: `65F02A56842B75AA92D775D56D657A56FE3FA993550B04DC20704AB82D760105`
- Patched target ROM SHA-256: `91809B188477CF458F1C1E8465A6C61D3CB46F3A88C1B2F59287E72342738D2C`
- The xDelta patch completed a checksum-valid decode against the clean source ROM.
- The built ROM contains the exact corrected 491-member event NARC.
- A final idempotency audit reported zero remaining event-item changes.

## Work-in-progress warnings

- The project remains a prerelease and may contain map/tile issues or gameplay bugs.
- A full runtime playthrough has not been completed for this release.
- Keep rotating save backups, especially while collecting held Mega Stones.
- Z-Moves, Dynamax/Gigantamax, Terastallization, discontinued online services, Pal Park replacement, and Pokéwalker replacement are not included.

No ROM is included. This release contains only a binary difference patch, documentation, reconciliation reports, and reproducible audit tooling.
