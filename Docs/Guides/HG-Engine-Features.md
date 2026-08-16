# HG-Engine Features and Expansion Changes

This page documents features that are confirmed by the build configuration and release audit for HeartGold Retiled Expansion v6.6.0.

## Battle and data features

| Feature | Expansion behavior |
| --- | --- |
| Rules baseline | Generation 9 is selected as the latest mechanics generation. |
| Pokémon data | 1391 species/form records are configured. The internal species/form index extends through 1315. |
| Moves | 923 move records are present, with per-move physical/special/status split data. |
| Items | 2685 item records are present, including later-generation evolution items and Mega Stones. |
| Fairy type | Enabled. |
| Weather | Snow Warning summons Snow under the Generation 9 rule selection. |
| Sleep | Uses the configured modern 2–4 turn range. |
| Battle style | Set mode is not forced; use the normal in-game choice. |
| Double battles | Trainers can be configured as double battles without a partner trainer. |
| Frame rate and text | Uncapped frame rate and instant text options are not forced in this build. |
| National Dex | Normal story progression is retained; it is not granted automatically. |

## Mega Evolution and Primal Reversion

- Professor Oak gives the Mega Ring immediately after giving the Pokédex. The same scene enables Mega Evolution.
- All 92 configured Mega Stones have one visible overworld pickup.
- 82 stones also appear in wild held-item slots on members of the matching evolution families. Mewtwo X/Y, Latiasite, Latiosite, and Diancite have static sources; five future-family stones are ground-only.
- Rayquaza Mega Evolves by knowing Dragon Ascent rather than holding a stone.
- Groudon and Kyogre can hold the Red Orb and Blue Orb, and the original late-game orb scene awards both orbs in one save.
- Z-Moves, Dynamax/Gigantamax, and Terastallization remain unavailable: their reserved activation flags have no setters in this release.

> [!WARNING]
> The release audit flags a possible Items-pocket stress case if a save accumulates close to 290 distinct entries. Keep more than one save backup, especially while collecting all 92 stones.

## Offline event access

| Content | Source | Requirement | What it unlocks |
| --- | --- | --- | --- |
| Enigma Stone | Ruins of Alph Research Center | National Dex and all 28 Unown | Original Pewter Museum Latias/Latios event |
| Celebi Lv. 30 | Ilex Forest shrine | Elite Four cleared | Original Ilex/Giovanni time-travel event |
| Guaranteed-shiny Pichu Lv. 30 | Ilex Forest shrine | Elite Four cleared | Original Spiky-eared Pichu sequence via lead-species check |
| Arceus Lv. 50 | Ruins of Alph | All 28 Unown seen | Original Sinjoh Ruins sequence |
| Shaymin Lv. 30 | National Park | National Dex | Gracidea from the Goldenrod Flower Shop |
| Diancie Lv. 50 | Sinjoh Ruins | Sinjoh scene complete | Diancite-compatible static encounter |

## Encounter and trainer redesign

- Wild tables contain 420 time-specific records across 140 areas, with expanded grass, Surf, fishing, swarm, Rock Smash, and Pokégear radio selections.
- The trainer table contains 738 entries. 645 regular entries use class-theme rebalancing, while bosses and rematches use curated assignments.
- See the [Wild Encounter Guide](Wild-Encounter-Guide.md) and [Trainer Guide](Trainer-Guide.md) for the exact data.

## Unchanged or unavailable systems

- Pokéwalker course dependencies remain tied to Pokéwalker/save support.
- Pal Park still depends on the original migration subsystem.
- GTS, Wi-Fi Plaza, online Battle Tower modes, and Battle Video services are not restored.
- The Lock Capsule has no new in-game use.
