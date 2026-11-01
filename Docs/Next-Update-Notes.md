# Changes queued for the next Heartfelt Gold patch

These source changes were made after the Pokémon Heartfelt Gold v1.0.0 patch. The Cyclizar encounters are included in the v1.0.1 patch. In-game encounter checks are still pending.

## Cyclizar wild encounters

In response to [issue #9](https://github.com/Trinsic64/Heart-Gold-Retiled/issues/9), Cyclizar has been added to the grass encounter table at **morning, day, and night** in both areas below:

| Area | Level | Share of grass encounters, after a battle triggers |
| --- | ---: | ---: |
| Whirl Islands B3F, ledge overlooking Lugia's room | 39 | 6% |
| Route 24 | 68 | 8% |

The [encounter source](../HG-Engine/data/Encounters.c) has two Cyclizar slots in each area's morning, day, and night table. The public [Wild Encounter Guide](Guides/Wild-Encounter-Guide.md) still describes the v1.0.0 build and needs an update.
