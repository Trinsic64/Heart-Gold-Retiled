# Heartfelt Gold gameplay features

This page reflects the current hg-engine authoring configuration supplied for Pokémon Heartfelt Gold. The release patch has not been independently decoded to confirm every setting.

## Start and progression

- The three starter choices are Treecko, Torchic, and Mudkip. The starter creation code gives each its matching Mega Stone.
- The National Dex is configured to be available from the start.
- Mega Evolution is configured in the engine. The existing Oak event is the documented Mega Ring source.
- A level cap is enabled in `include/config.h` and uses save variable `0x416F`. Its value and progression must be checked in game; the source switch alone does not establish the cap schedule.

## Quality of life

| Feature | Current source setting |
| --- | --- |
| TMs | Reusable |
| HMs | Can be forgotten |
| Frame rate | Uncapped in the overworld and battles |
| Text speed | Instant text is not forced |
| Marts | Expanded stock, including evolution items, specialty Poké Balls, and selected Mega Stones |

The [Evolution Guide](Evolution-Guide.md) lists the current configured methods, and the [Static Encounter Guide](Static-Encounter-Guide.md) lists scripted species and levels from the supplied DSPRE export. Shop inventories are defined in [mart.c](../../HG-Engine/src/field/mart.c); some entries can depend on story state.

The [Wild Encounter Guide](Wild-Encounter-Guide.md) and [Trainer Guide](Trainer-Guide.md) are generated from the current encounter and trainer tables. Online services, Pokéwalker dependencies, and Pal Park migration are not documented as restored by these changes.
