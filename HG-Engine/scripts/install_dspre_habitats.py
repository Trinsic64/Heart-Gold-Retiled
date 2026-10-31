"""Build DSPRE habitat NARC from engine encounters, preserving ROM highlight geometry."""
import argparse
import hashlib
import json
import struct
from pathlib import Path
import audit_dspre_pokedex as audit
import generate_pokedex_area as g


def pack_narc(members):
    payload = bytearray()
    entries = bytearray()
    for member in members:
        start = len(payload)
        payload.extend(member)
        entries.extend(struct.pack('<II', start, len(payload)))
        payload.extend(b'\xff' * (-len(payload) % 4))
    def chunk(tag, data):
        return tag + struct.pack('<I', len(data) + 8) + data
    body = chunk(b'BTAF', struct.pack('<HH', len(members), 0) + entries)
    body += chunk(b'BTNF', struct.pack('<IHH', 4, 0, 1))
    body += chunk(b'GMIF', payload)
    return b'NARC' + struct.pack('<HHIHH', 0xfffe, 0x100, len(body)+16, 16, 3) + body


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    parser.add_argument('--engine', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--install', action='store_true')
    args = parser.parse_args()
    root = args.engine
    report = audit.audit(args.project, root)
    # Require all ordinary mappings to agree with the actual dynamic headers.
    # Contest-only table 24 is deliberately omitted by the engine generator.
    for encounter_id, old in g.AREA_BY_ENCOUNTER_ID.items():
        actual = report['encounterAreaMapping'].get(str(encounter_id), [])
        if encounter_id == 24:
            continue
        assert actual == ([list(old)] if old else []), (encounter_id, old, actual)
    canonical, maximum = g.parse_species(root/'include/constants/species.h')
    lists = g.build_encounter_lists(root/'data/Encounters.c', root/'include/constants/encounter_tables.h', canonical, maximum)
    g.add_headbutt_lists(lists, root/'data/Headbutt.c', canonical)
    order = g.parse_dex_area_order(root/'include/constants/pokedex.h')
    g.render(lists, order)
    target = args.project/'files/a/1/3/3'
    before = target.read_bytes()
    original = audit.narc_members(before)
    members = original[:2]
    for group in range(8):
        for species in range(maximum+1):
            values = sorted(order[area] for area in lists[species][group]) + [0]
            members.append(struct.pack('<'+'I'*len(values), *values))
    members.append(b'\0'*4)
    assert len(members) == len(original) == 8611
    packed = pack_narc(members)
    assert audit.narc_members(packed) == members
    assert members[:2] == original[:2]
    report['changedMembers'] = sum(a != b for a,b in zip(original,members))
    report['encountersSha256'] = hashlib.sha256((root/'data/Encounters.c').read_bytes()).hexdigest()
    report['newArchiveSha256'] = hashlib.sha256(packed).hexdigest()
    report['source'] = 'HG-Engine/data/Encounters.c and data/Headbutt.c; DSPRE geometry and dynamic headers'
    report['installed'] = args.install
    args.output.mkdir(parents=True, exist_ok=True)
    backup = args.output/'3.before'
    if not backup.exists():
        backup.write_bytes(before)
    (args.output/'3').write_bytes(packed)
    (args.output/'installation-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    if args.install:
        assert target.read_bytes() == before, 'Archive changed during generation'
        target.write_bytes(packed)
        assert target.read_bytes() == packed
    print(json.dumps({key:report[key] for key in ('changedMembers','encountersSha256','newArchiveSha256','installed')},indent=2))


if __name__ == '__main__':
    main()
