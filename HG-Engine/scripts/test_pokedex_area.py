import tempfile
import unittest
from pathlib import Path
import generate_pokedex_area as g

class HabitatTests(unittest.TestCase):
    def test_encounter_indentation_and_numeric_ids(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'Encounters.c'
            source.write_text('        [ENCDATA_TEST] = { .rateWalk = 1 },\t[145] = { .rateWalk = 2 },\n')
            self.assertEqual(set(g.encounter_blocks(source, {'ENCDATA_TEST': 1})), {1, 145})
            source.write_text('[1] = {},\n    [1] = {},\n')
            with self.assertRaisesRegex(ValueError, 'duplicate'):
                g.encounter_blocks(source, {})
            source.write_text('no encounter records')
            with self.assertRaisesRegex(ValueError, 'no encounter'):
                g.encounter_blocks(source, {})

    def test_forms_and_current_sources(self):
        root = Path(__file__).resolve().parents[1]
        canonical, maximum = g.parse_species(root / 'include/constants/species.h')
        for form, base in [('SPECIES_TAUROS_AQUA','SPECIES_TAUROS'),('SPECIES_DECIDUEYE_HISUIAN','SPECIES_DECIDUEYE'),('SPECIES_LYCANROC_DUSK','SPECIES_LYCANROC')]:
            self.assertEqual(g.canonical_species(form, canonical), canonical[base])
        blocks = g.encounter_blocks(root / 'data/Encounters.c', g.parse_encounter_enum(root / 'include/constants/encounter_tables.h'))
        self.assertEqual(set(blocks), set(range(147)))
        lists = g.build_encounter_lists(root / 'data/Encounters.c', root / 'include/constants/encounter_tables.h', canonical, maximum)
        expected = [[set() for _ in range(8)] for _ in range(maximum + 1)]
        # Every enabled grass slot must mark its area at that exact time.
        for index, block in blocks.items():
            mapping = g.AREA_BY_ENCOUNTER_ID[index]
            if not mapping:
                continue
            kind, area = mapping
            offset = 0 if kind == 'special' else 3
            def add(field, indices):
                for token in g.SPECIES_PATTERN.findall(g.initializer(block, field)):
                    species = g.canonical_species(token, canonical)
                    if species:
                        for index in indices:
                            expected[species][index].add(area)
            if g.scalar(block, 'rateWalk'):
                for time, field in enumerate(('speciesMorning','speciesDay','speciesNight')):
                    add(field, [offset + time])
                for field in ('hoennSoundSpecies','sinnohSoundSpecies'):
                    add(field, [6 if kind == 'special' else 7])
            for rate, field in [('rateSurf','surfSlots'),('rateRockSmash','rockSmashSlots'),('rateOldRod','oldRodSlots'),('rateGoodRod','goodRodSlots'),('rateSuperRod','superRodSlots')]:
                if g.scalar(block, rate):
                    add(field, range(offset, offset + 3))
            if any(g.scalar(block, rate) for rate in ('rateOldRod','rateGoodRod','rateSuperRod')):
                token = g.re.search(r'\.nightFish\s*=\s*(SPECIES_[A-Z0-9_]+)', block).group(1)
                species = g.canonical_species(token, canonical)
                if species:
                    expected[species][offset + 2].add(area)
        self.assertEqual(lists, expected)
        g.add_headbutt_lists(lists, root / 'data/Headbutt.c', canonical)
        self.assertEqual(g.render(lists, g.parse_dex_area_order(root / 'include/constants/pokedex.h')), (root / 'data/generated/PokedexAreaLists.inc').read_text(encoding='utf-8'))

if __name__ == '__main__':
    unittest.main()
