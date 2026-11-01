# Changes queued for the next Heartfelt Gold patch

These source changes were made after the Pokémon Heartfelt Gold v1.0.0 patch. They are **not in the current downloadable ROM patch**. A new ROM build, xDelta patch, and in-game check are still needed before these changes become playable.

## Cyclizar wild encounters

In response to [issue #9](https://github.com/Trinsic64/Heart-Gold-Retiled/issues/9), Cyclizar has been added to the grass encounter table at **morning, day, and night** in both areas below:

| Area | Level | Share of grass encounters, after a battle triggers |
| --- | ---: | ---: |
| Whirl Islands B3F, ledge overlooking Lugia's room | 39 | 6% |
| Route 24 | 68 | 8% |

The [encounter source](../HG-Engine/data/Encounters.c) has two Cyclizar slots in each area's morning, day, and night table. The public [Wild Encounter Guide](Guides/Wild-Encounter-Guide.md) continues to describe the existing v1.0.0 build until the next patch is made.
