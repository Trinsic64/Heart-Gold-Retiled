#!/usr/bin/env python3
"""Generate the Pokédex area lists from HG-Engine's encounter sources.

The a/1/3/3 archive stores eight area lists per canonical species:
special-area and route/city lists for morning, day, night, and special
encounters.  Regular water, fishing, and Rock Smash encounters are available
at every time of day; the night-fishing replacement is night-only. Pokégear
radio and Headbutt encounters use the special lists, while vanilla's map
deliberately omits swarm replacements.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


AREA_BY_ENCOUNTER_ID: dict[int, tuple[str, str] | None] = {
    0: ("route", "DEX_NEW_BARK_TOWN"),
    1: ("route", "DEX_ROUTE_29"),
    2: ("route", "DEX_CHERRYGROVE_CITY"),
    3: ("route", "DEX_ROUTE_30"),
    4: ("route", "DEX_ROUTE_31"),
    5: ("route", "DEX_VIOLET_CITY"),
    6: ("special", "DEX_SPROUT_TOWER"),
    7: ("special", "DEX_SPROUT_TOWER"),
    8: ("route", "DEX_ROUTE_32"),
    9: ("special", "DEX_RUINS_OF_ALPH"),
    10: ("special", "DEX_RUINS_OF_ALPH"),
    11: ("special", "DEX_RUINS_OF_ALPH"),
    12: ("special", "DEX_RUINS_OF_ALPH"),
    13: ("special", "DEX_RUINS_OF_ALPH"),
    14: ("special", "DEX_UNION_CAVE"),
    15: ("special", "DEX_UNION_CAVE"),
    16: ("special", "DEX_UNION_CAVE"),
    17: ("route", "DEX_ROUTE_33"),
    18: ("special", "DEX_SLOWPOKE_WELL"),
    19: ("special", "DEX_SLOWPOKE_WELL"),
    20: ("special", "DEX_ILEX_FOREST"),
    21: ("route", "DEX_ROUTE_34"),
    22: ("route", "DEX_ROUTE_35"),
    23: ("special", "DEX_NATIONAL_PARK"),
    # The Bug-Catching Contest table is event-only and vanilla deliberately
    # omits it from the morning/day/night map lists.
    24: None,
    25: ("route", "DEX_ROUTE_36"),
    26: ("route", "DEX_ROUTE_37"),
    27: ("route", "DEX_ECRUTEAK_CITY"),
    28: ("special", "DEX_BURNED_TOWER"),
    29: ("special", "DEX_BURNED_TOWER"),
    **{i: ("special", "DEX_BELL_TOWER") for i in range(30, 38)},
    38: ("route", "DEX_ROUTE_38"),
    39: ("route", "DEX_ROUTE_39"),
    40: ("route", "DEX_OLIVINE_CITY"),
    41: ("route", "DEX_ROUTE_40"),
    42: ("route", "DEX_ROUTE_41"),
    43: ("special", "DEX_WHIRL_ISLANDS"),
    44: ("special", "DEX_WHIRL_ISLANDS"),
    45: None,
    46: ("special", "DEX_WHIRL_ISLANDS"),
    47: None,
    48: ("special", "DEX_WHIRL_ISLANDS"),
    49: None,
    50: None,
    51: ("route", "DEX_CIANWOOD_CITY"),
    52: ("route", "DEX_ROUTE_42"),
    **{i: ("special", "DEX_MT_MORTAR") for i in range(53, 57)},
    57: ("route", "DEX_ROUTE_43"),
    58: ("route", "DEX_LAKE_OF_RAGE"),
    59: ("route", "DEX_ROUTE_44"),
    **{i: ("special", "DEX_ICE_PATH") for i in range(60, 64)},
    64: None,
    65: ("route", "DEX_BLACKTHORN_CITY"),
    66: ("special", "DEX_DRAGONS_DEN"),
    67: ("route", "DEX_ROUTE_45"),
    68: ("route", "DEX_ROUTE_46"),
    69: ("special", "DEX_DARK_CAVE"),
    70: ("special", "DEX_DARK_CAVE"),
    71: ("route", "DEX_ROUTE_47"),
    72: ("special", "DEX_MT_MOON"),
    73: ("special", "DEX_MT_MOON"),
    **{i: ("special", "DEX_SEAFOAM_ISLANDS") for i in range(74, 79)},
    **{i: ("special", "DEX_MT_SILVER_CAVE") for i in range(79, 82)},
    82: ("special", "DEX_CLIFF_EDGE_GATE"),
    83: ("special", "DEX_CLIFF_CAVE"),
    84: ("special", "DEX_BELL_TOWER"),
    85: ("route", "DEX_MT_SILVER"),
    **{i: ("special", "DEX_MT_SILVER_CAVE") for i in range(86, 90)},
    90: None,
    91: None,
    92: ("route", "DEX_ROUTE_12"),
    93: ("route", "DEX_ROUTE_19"),
    94: ("route", "DEX_ROUTE_20"),
    95: ("route", "DEX_PALLET_TOWN"),
    96: ("route", "DEX_VIRIDIAN_CITY"),
    97: ("route", "DEX_CERULEAN_CITY"),
    98: ("route", "DEX_VERMILION_CITY"),
    99: ("route", "DEX_CELADON_CITY"),
    100: ("route", "DEX_FUCHSIA_CITY"),
    101: ("route", "DEX_CINNABAR_CITY"),
    102: ("route", "DEX_ROUTE_48"),
    103: ("route", "DEX_ROUTE_26"),
    104: ("route", "DEX_ROUTE_27"),
    105: ("route", "DEX_ROUTE_28"),
    106: ("special", "DEX_MT_MOON"),
    107: ("special", "DEX_MT_MOON"),
    108: ("special", "DEX_ROCK_TUNNEL"),
    109: ("special", "DEX_ROCK_TUNNEL"),
    110: ("special", "DEX_VICTORY_ROAD"),
    111: ("route", "DEX_ROUTE_1"),
    112: ("route", "DEX_ROUTE_2"),
    113: ("route", "DEX_ROUTE_3"),
    114: ("route", "DEX_ROUTE_4"),
    115: ("route", "DEX_ROUTE_5"),
    116: ("route", "DEX_ROUTE_6"),
    117: ("route", "DEX_ROUTE_7"),
    118: ("route", "DEX_ROUTE_8"),
    119: ("route", "DEX_ROUTE_9"),
    120: ("route", "DEX_ROUTE_10"),
    121: ("route", "DEX_ROUTE_11"),
    122: ("route", "DEX_ROUTE_13"),
    123: ("route", "DEX_ROUTE_14"),
    124: ("route", "DEX_ROUTE_15"),
    125: ("route", "DEX_ROUTE_16"),
    126: ("route", "DEX_ROUTE_17"),
    127: ("route", "DEX_ROUTE_18"),
    128: ("route", "DEX_ROUTE_21"),
    129: ("route", "DEX_ROUTE_22"),
    130: ("route", "DEX_ROUTE_24"),
    131: ("route", "DEX_ROUTE_25"),
    132: ("special", "DEX_TOHJO_FALLS"),
    133: ("special", "DEX_DIGLETTS_CAVE"),
    134: ("special", "DEX_VICTORY_ROAD"),
    135: ("special", "DEX_VICTORY_ROAD"),
    136: ("route", "DEX_ROUTE_2_2"),
    137: ("special", "DEX_VIRIDIAN_FOREST"),
    138: None,
    139: ("special", "DEX_CERULEAN_CAVE"),
    140: ("special", "DEX_CERULEAN_CAVE"),
    141: ("special", "DEX_CERULEAN_CAVE"),
    # Retiled encounter tables added through header edits.
    142: ("route", "DEX_MAHOGANY_TOWN"),
    143: ("route", "DEX_ROUTE_16_2"),
    144: ("route", "DEX_PEWTER_CITY"),
    145: ("route", "DEX_AZALEA_TOWN"),
    146: ("route", "DEX_ROUTE_10"),
}


HEADBUTT_AREA_BY_FIELD: dict[str, tuple[str, str]] = {
    **{f"route{i}": ("route", f"DEX_ROUTE_{i}") for i in range(1, 49)},
    "newBarkTown": ("route", "DEX_NEW_BARK_TOWN"),
    "cherrygroveCity": ("route", "DEX_CHERRYGROVE_CITY"),
    "violetCity": ("route", "DEX_VIOLET_CITY"),
    "azaleaTown": ("route", "DEX_AZALEA_TOWN"),
    "ecruteakCity": ("route", "DEX_ECRUTEAK_CITY"),
    "olivineCity": ("route", "DEX_OLIVINE_CITY"),
    "cianwoodCity": ("route", "DEX_CIANWOOD_CITY"),
    "lakeOfRage": ("route", "DEX_LAKE_OF_RAGE"),
    "blackthornCity": ("route", "DEX_BLACKTHORN_CITY"),
    "palletTown": ("route", "DEX_PALLET_TOWN"),
    "viridianCity": ("route", "DEX_VIRIDIAN_CITY"),
    "pewterCity": ("route", "DEX_PEWTER_CITY"),
    "ceruleanCity": ("route", "DEX_CERULEAN_CITY"),
    "vermilionCity": ("route", "DEX_VERMILION_CITY"),
    "celadonCity": ("route", "DEX_CELADON_CITY"),
    "fuchsiaCity": ("route", "DEX_FUCHSIA_CITY"),
    "cinnabarIsland": ("route", "DEX_CINNABAR_CITY"),
    "mtSilver": ("route", "DEX_MT_SILVER"),
    "nationalPark": ("special", "DEX_NATIONAL_PARK"),
    "ilexForest": ("special", "DEX_ILEX_FOREST"),
    "viridianForest": ("special", "DEX_VIRIDIAN_FOREST"),
    "safariZoneGateOutside": ("route", "DEX_SAFARI_ZONE_GATE"),
    "route2414": ("route", "DEX_ROUTE_2_2"),
    "route16422": ("route", "DEX_ROUTE_16_2"),
    "mtSilverCaveLowerMountainside": ("special", "DEX_MT_SILVER_CAVE"),
}


SPECIES_PATTERN = re.compile(r"SPECIES_[A-Z0-9_]+")


def matching_brace(text: str, opening: int) -> int:
    depth = 0
    for index in range(opening, len(text)):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return index
    raise ValueError(f"unclosed initializer at byte {opening}")


def initializer(text: str, field: str) -> str:
    match = re.search(rf"\.{re.escape(field)}\s*=\s*\{{", text)
    if match is None:
        raise ValueError(f"missing .{field} initializer")
    opening = text.find("{", match.start())
    return text[opening + 1 : matching_brace(text, opening)]


def scalar(text: str, field: str) -> int:
    match = re.search(rf"\.{re.escape(field)}\s*=\s*(\d+)", text)
    if match is None:
        raise ValueError(f"missing .{field} value")
    return int(match.group(1))


def parse_species(species_header: Path) -> tuple[dict[str, int], int]:
    text = species_header.read_text(encoding="utf-8")
    canonical: dict[str, int] = {}
    for name, value in re.findall(r"^#define\s+(SPECIES_[A-Z0-9_]+)\s+(\d+)\b", text, re.MULTILINE):
        canonical[name] = int(value)
    max_match = re.search(r"#define\s+MAX_CANONICAL_MON_NUM\s+\((SPECIES_[A-Z0-9_]+)\)", text)
    if max_match is None or max_match.group(1) not in canonical:
        raise ValueError("could not resolve MAX_CANONICAL_MON_NUM")
    return canonical, canonical[max_match.group(1)]


def canonical_species(token: str, canonical: dict[str, int]) -> int:
    if token in canonical:
        return canonical[token]

    for suffix in ("_ALOLAN", "_GALARIAN", "_HISUIAN", "_PALDEAN"):
        if token.endswith(suffix):
            base = token[: -len(suffix)]
            if base in canonical:
                return canonical[base]

    raise ValueError(f"encounter species {token} has no canonical Pokédex mapping")


def parse_encounter_enum(encounter_header: Path) -> dict[str, int]:
    return {
        name: int(value)
        for name, value in re.findall(
            r"^\s*(ENCDATA_[A-Z0-9_]+)\s*=\s*(\d+)",
            encounter_header.read_text(encoding="utf-8"),
            re.MULTILINE,
        )
    }


def encounter_blocks(encounters_source: Path, enum_values: dict[str, int]) -> dict[int, str]:
    text = encounters_source.read_text(encoding="utf-8")
    blocks: dict[int, str] = {}
    for match in re.finditer(r"^    \[([^\]]+)\]\s*=\s*\{", text, re.MULTILINE):
        key = match.group(1).strip()
        encounter_id = int(key) if key.isdigit() else enum_values[key]
        opening = text.find("{", match.start())
        blocks[encounter_id] = text[opening + 1 : matching_brace(text, opening)]
    return blocks


def add_species(
    lists: list[list[set[str]]],
    tokens: list[str],
    list_index: int,
    area: str,
    canonical: dict[str, int],
) -> None:
    for token in tokens:
        species = canonical_species(token, canonical)
        if species != 0:
            lists[species][list_index].add(area)


def build_encounter_lists(
    encounters_source: Path,
    encounter_header: Path,
    canonical: dict[str, int],
    max_species: int,
) -> list[list[set[str]]]:
    lists = [[set() for _ in range(8)] for _ in range(max_species + 1)]
    blocks = encounter_blocks(encounters_source, parse_encounter_enum(encounter_header))

    unknown_ids = sorted(set(blocks) - set(AREA_BY_ENCOUNTER_ID))
    if unknown_ids:
        raise ValueError(f"encounter-area mapping missing IDs: {unknown_ids}")

    for encounter_id, block in sorted(blocks.items()):
        mapping = AREA_BY_ENCOUNTER_ID[encounter_id]
        if mapping is None:
            continue
        area_kind, area = mapping
        regular_offset = 0 if area_kind == "special" else 3
        special_index = 6 if area_kind == "special" else 7

        if scalar(block, "rateWalk"):
            for time_index, field in enumerate(("speciesMorning", "speciesDay", "speciesNight")):
                add_species(lists, SPECIES_PATTERN.findall(initializer(block, field)), regular_offset + time_index, area, canonical)
            for field in ("hoennSoundSpecies", "sinnohSoundSpecies"):
                add_species(lists, SPECIES_PATTERN.findall(initializer(block, field)), special_index, area, canonical)

        always_fields: list[str] = []
        if scalar(block, "rateSurf"):
            always_fields.append("surfSlots")
        if scalar(block, "rateRockSmash"):
            always_fields.append("rockSmashSlots")
        rod_rates = [scalar(block, field) for field in ("rateOldRod", "rateGoodRod", "rateSuperRod")]
        for enabled, field in zip(rod_rates, ("oldRodSlots", "goodRodSlots", "superRodSlots")):
            if enabled:
                always_fields.append(field)
        # The three swarm replacement fields are intentionally not shown by
        # HGSS's Pokédex area map; retain that vanilla behavior.
        if any(rod_rates):
            match = re.search(r"\.nightFish\s*=\s*(SPECIES_[A-Z0-9_]+)", block)
            add_species(lists, [match.group(1)], regular_offset + 2, area, canonical)

        always_tokens: list[str] = []
        for field in always_fields:
            always_tokens.extend(SPECIES_PATTERN.findall(initializer(block, field)))
        for time_index in range(3):
            add_species(lists, always_tokens, regular_offset + time_index, area, canonical)

    return lists


def add_headbutt_lists(
    lists: list[list[set[str]]],
    headbutt_source: Path,
    canonical: dict[str, int],
) -> None:
    text = headbutt_source.read_text(encoding="utf-8")
    for match in re.finditer(r"^    \.([A-Za-z0-9]+)\s*=\s*\{", text, re.MULTILINE):
        field = match.group(1)
        opening = text.find("{", match.start())
        block = text[opening + 1 : matching_brace(text, opening)]
        normal_count = scalar(block, "normalTreeCount")
        special_count = scalar(block, "specialTreeCount")
        if not normal_count and not special_count:
            continue
        if field not in HEADBUTT_AREA_BY_FIELD:
            raise ValueError(f"headbutt-area mapping missing active field: {field}")
        area_kind, area = HEADBUTT_AREA_BY_FIELD[field]
        list_index = 6 if area_kind == "special" else 7
        tokens: list[str] = []
        if normal_count:
            tokens.extend(SPECIES_PATTERN.findall(initializer(block, "normalSlots")))
        if special_count:
            tokens.extend(SPECIES_PATTERN.findall(initializer(block, "specialSlots")))
        add_species(lists, tokens, list_index, area, canonical)


def parse_dex_area_order(pokedex_header: Path) -> dict[str, int]:
    values: dict[str, int] = {}
    # Special-area and route/city IDs intentionally overlap, but each generated
    # list contains only one kind, so numeric sorting remains unambiguous.
    for name, value in re.findall(
        r"^\s*(DEX_[A-Z0-9_]+)\s*=\s*(0x[0-9A-Fa-f]+|\d+)",
        pokedex_header.read_text(encoding="utf-8"),
        re.MULTILINE,
    ):
        values[name] = int(value, 0)
    return values


def render(lists: list[list[set[str]]], dex_order: dict[str, int]) -> str:
    # Member zero doubles as the complete special-area ID catalogue in vanilla.
    lists[0][0] = {
        "DEX_SPROUT_TOWER", "DEX_RUINS_OF_ALPH", "DEX_UNION_CAVE",
        "DEX_SLOWPOKE_WELL", "DEX_ILEX_FOREST", "DEX_NATIONAL_PARK",
        "DEX_BURNED_TOWER", "DEX_BELL_TOWER", "DEX_WHIRL_ISLANDS",
        "DEX_MT_MORTAR", "DEX_ICE_PATH", "DEX_DRAGONS_DEN",
        "DEX_DARK_CAVE", "DEX_MT_MOON", "DEX_SEAFOAM_ISLANDS",
        "DEX_MT_SILVER_CAVE", "DEX_CLIFF_EDGE_GATE", "DEX_CLIFF_CAVE",
        "DEX_OLIVINE_CITY_SPECIAL", "DEX_ROCK_TUNNEL", "DEX_VICTORY_ROAD",
        "DEX_TOHJO_FALLS", "DEX_DIGLETTS_CAVE", "DEX_VIRIDIAN_FOREST",
        "DEX_CERULEAN_CAVE",
    }

    flattened: list[list[str]] = []
    for list_index in range(8):
        for species_lists in lists:
            flattened.append(sorted(species_lists[list_index], key=lambda area: (dex_order[area], area)))
    flattened.append([])  # Preserve the archive's trailing unused member.

    data: list[str] = []
    offsets: list[tuple[int, int]] = []
    for areas in flattened:
        offsets.append((len(data), len(areas) + 1))
        data.extend(areas)
        data.append("DEX_END_AREA_DATA")

    lines = [
        "/* Auto-generated by scripts/generate_pokedex_area.py. Do not edit. */",
        "static const u32 sPokedexAreaListData[] =",
        "{",
    ]
    lines.extend(f"    {area}," for area in data)
    lines.extend(["};", "", "const PokedexU32List sPokedexAreaLists[] =", "{"])
    lines.extend(
        f"    [{index}] = {{ &sPokedexAreaListData[{offset}], {count} }},"
        for index, (offset, count) in enumerate(offsets)
    )
    lines.extend(
        [
            "};",
            "_Static_assert(sizeof(sPokedexAreaLists) / sizeof(*sPokedexAreaLists) == (POKEDEX_CANONICAL_SPECIES_COUNT * 8) + 1, \"unexpected Pokédex area list count\");",
            "",
            "const u32 sPokedexAreaBaseMemberCount = sizeof(sPokedexAreaBaseMembers) / sizeof(*sPokedexAreaBaseMembers);",
            "const u32 sPokedexAreaListCount = sizeof(sPokedexAreaLists) / sizeof(*sPokedexAreaLists);",
            "",
        ]
    )
    return "\n".join(lines)


def compare_legacy(lists: list[list[set[str]]], legacy_source: Path, species_limit: int) -> int:
    """Compare generated Gen IV lists with the checked-in vanilla source."""
    text = legacy_source.read_text(encoding="utf-8")
    arrays: dict[str, set[str]] = {}
    for match in re.finditer(r"^static const u32 (sPokedexArea[A-Za-z0-9_]+)\[\]\s*=\s*\{", text, re.MULTILINE):
        opening = text.find("{", match.start())
        block = text[opening + 1 : matching_brace(text, opening)]
        arrays[match.group(1)] = set(re.findall(r"\bDEX_[A-Z0-9_]+\b", block)) - {"DEX_END_AREA_DATA"}

    entries = {
        int(index): name
        for index, name in re.findall(
            r"^\s*\[(\d+)\]\s*=\s*\{\s*(sPokedexArea[A-Za-z0-9_]+)\s*,",
            text,
            re.MULTILINE,
        )
        if not name.endswith("UnusedMember8602")
    }
    if not entries:
        raise ValueError(f"no legacy Pokédex area lists found in {legacy_source}")
    stride = (max(entries) + 1) // 8
    differences: list[str] = []
    for list_index in range(8):
        for species in range(1, min(species_limit, stride - 1) + 1):
            expected = arrays[entries[list_index * stride + species]]
            actual = lists[species][list_index]
            if expected != actual:
                differences.append(
                    f"list {list_index}, species {species}: expected {sorted(expected)}, got {sorted(actual)}"
                )
    if differences:
        print(f"legacy comparison found {len(differences)} differences", file=sys.stderr)
        for difference in differences[:30]:
            print(difference, file=sys.stderr)
        return 1
    print(f"legacy comparison passed for species 0-{min(species_limit, stride - 1)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--encounters", type=Path, default=Path("data/Encounters.c"))
    parser.add_argument("--headbutt", type=Path, default=Path("data/Headbutt.c"))
    parser.add_argument("--species", type=Path, default=Path("include/constants/species.h"))
    parser.add_argument("--encounter-ids", type=Path, default=Path("include/constants/encounter_tables.h"))
    parser.add_argument("--pokedex-ids", type=Path, default=Path("include/constants/pokedex.h"))
    parser.add_argument("--output", type=Path, default=Path("data/generated/PokedexAreaLists.inc"))
    parser.add_argument("--check", action="store_true", help="fail if the output is not current")
    parser.add_argument("--compare-legacy", type=Path, help="compare generated lists with a vanilla PokedexArea.c")
    parser.add_argument("--compare-species-limit", type=int, default=493)
    args = parser.parse_args()

    canonical, max_species = parse_species(args.species)
    lists = build_encounter_lists(args.encounters, args.encounter_ids, canonical, max_species)
    add_headbutt_lists(lists, args.headbutt, canonical)
    if args.compare_legacy is not None:
        return compare_legacy(lists, args.compare_legacy, args.compare_species_limit)
    output = render(lists, parse_dex_area_order(args.pokedex_ids))

    if args.check:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != output:
            print(f"{args.output} is out of date", file=sys.stderr)
            return 1
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8", newline="\n")
    print(f"generated {len(lists)} species across eight Pokédex area lists in {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
