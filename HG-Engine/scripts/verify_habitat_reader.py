"""Check assembled overlay habitat indices against all generated species lists."""
import argparse
import struct
from pathlib import Path
import generate_pokedex_area as g
from audit_dspre_pokedex import narc_members

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('engine', type=Path)
args = parser.parse_args()
root = args.engine
canonical, maximum = g.parse_species(root/'include/constants/species.h')
stride = maximum + 1
data = (root/'base/overlay/overlay_0018.bin').read_bytes()
pool = struct.unpack_from('<7I', data, 0x021E86F8 - 0x021E5900)
groups = [0, 1, 2, 6, 3, 4, 5, 7]
bases = [2, *pool]
assert bases == [2 + group * stride for group in groups], (bases, stride)
# Check that each case still reads the literal pool we patched.
for i, address in enumerate(range(0x021E86BE, 0x021E86D7, 4)):
    instruction = struct.unpack_from('<H', data, address - 0x021E5900)[0]
    assert instruction & 0xff00 == 0x4b00
    assert ((address + 4) & ~3) + (instruction & 255)*4 == 0x021E86F8+i*4
members = narc_members((root/'build/narc/dexareas.narc').read_bytes())
assert len(members) == stride*8+3
lists = g.build_encounter_lists(root/'data/Encounters.c', root/'include/constants/encounter_tables.h', canonical, maximum)
g.add_headbutt_lists(lists, root/'data/Headbutt.c', canonical)
order = g.parse_dex_area_order(root/'include/constants/pokedex.h')
g.render(lists, order)
for base, group in zip(bases, groups):
    for species in range(stride):
        expected = sorted(order[area] for area in lists[species][group]) + [0]
        member = members[base + species]
        assert list(struct.unpack('<'+'I'*(len(member)//4), member)) == expected, (group, species)
assert (root/'base/root/a/1/3/3').read_bytes() == (root/'build/narc/dexareas.narc').read_bytes()
print(f'PASS: all {stride*8} runtime lookups match the engine habitat lists; archive copy matches.')
