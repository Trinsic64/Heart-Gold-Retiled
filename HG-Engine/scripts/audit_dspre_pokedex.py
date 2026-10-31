"""Audit HGSS dynamic headers against the actual Pokédex overlay and archive."""
import argparse
import hashlib
import json
import struct
from pathlib import Path


def narc_members(data):
    assert data[:4] == b'NARC'
    assert struct.unpack_from('<I', data, 8)[0] == len(data)
    offset = struct.unpack_from('<H', data, 12)[0]
    sections = {}
    for _ in range(struct.unpack_from('<H', data, 14)[0]):
        tag = data[offset:offset+4]
        size = struct.unpack_from('<I', data, offset+4)[0]
        assert size >= 8 and offset + size <= len(data)
        sections[tag] = data[offset+8:offset+size]
        offset += size
    fat, payload = sections[b'BTAF'], sections[b'GMIF']
    count = struct.unpack_from('<H', fat)[0]
    result = []
    for i in range(count):
        start, end = struct.unpack_from('<II', fat, 4+i*8)
        assert start <= end <= len(payload)
        result.append(payload[start:end])
    return result


def dynamic_header(path):
    data = path.read_bytes()
    assert len(data) == 24, (path, len(data))
    xy = struct.unpack_from('<H', data, 2)[0]
    flags = struct.unpack_from('<I', data, 20)[0]
    return {'id': int(path.name), 'encounter': data[0], 'mapSection': data[18],
            'region': flags & 1, 'mapType': (flags >> 8) & 15,
            'worldX': (xy >> 4) & 63, 'worldY': (xy >> 10) & 63}


def audit(project, engine):
    headers = {int(p.name): dynamic_header(p) for p in (project/'unpacked/dynamicHeaders').iterdir() if p.is_file() and p.name.isdigit()}
    overlay = (project/'arm9_overlays/ov018.bin').read_bytes()
    # Anchors verified against the HGSS overlay-18 source. Fail closed if moved
    # or duplicated rather than trusting absolute addresses in a rebuilt ROM.
    locations = {}
    for kind, values, count in [('route',[65535,60,33,67,34,35,73],70), ('special',[65535,155,113,99,177,117,96],26)]:
        pattern = struct.pack('<'+'H'*len(values), *values)
        at = overlay.find(pattern)
        assert at >= 0 and overlay.find(pattern, at+1) < 0, f'{kind} map table not uniquely found'
        locations[kind] = list(struct.unpack_from('<'+'H'*count, overlay, at))
    archive_path = project/'files/a/1/3/3'
    members = narc_members(archive_path.read_bytes())
    assert len(members[0]) == 26*4 and len(members[1]) == 70*36
    import generate_pokedex_area as g
    dex = g.parse_dex_area_order(engine/'include/constants/pokedex.h')
    split = (engine/'include/constants/pokedex.h').read_text().split('DEX_NEW_BARK_TOWN')[0]
    special_names = set(g.re.findall(r'DEX_[A-Z0-9_]+', split))
    area_enum = (engine/'include/constants/pokedex.h').read_text().split('enum DexTimeOfDay')[0]
    area_names = set(g.re.findall(r'DEX_[A-Z0-9_]+', area_enum))
    names = {(('special' if name in special_names else 'route'), value): name for name, value in dex.items() if value and name in area_names}
    supported = []
    unsupported = []
    for kind, ids in locations.items():
        for area, header_id in enumerate(ids):
            if not area or header_id == 65535:
                continue
            if header_id not in headers:
                unsupported.append({'kind':kind,'area':area,'reason':'missing representative dynamic header'})
                continue
            if kind == 'route':
                row = members[1][area*36:(area+1)*36]
                width, height = row[2:4]
                valid = width > 0 and height > 0 and width*height <= 32 and any(row[4:4+width*height])
            else:
                row = members[0][area*4:(area+1)*4]
                valid = bool(row[0] or row[1])
            if not valid:
                unsupported.append({'kind':kind,'area':area,'header':header_id,'reason':'empty/invalid highlight geometry'})
                continue
            supported.append({'kind':kind,'area':area,'constant':names[kind,area], 'header':header_id, **{k:headers[header_id][k] for k in ('mapSection','region','mapType')}})
    mapping = {}
    assignments = []
    skipped = []
    for h in headers.values():
        if h['encounter'] == 255:
            continue
        candidates = [a for a in supported if a['header'] == h['id']]
        reason = 'overlay representative header'
        if not candidates:
            candidates = [a for a in supported if a['mapSection'] == h['mapSection'] and a['region'] == h['region']]
            reason = 'matching dynamic map section and region'
            if len(candidates) > 1:
                preferred = [a for a in candidates if (a['kind']=='special') == (h['mapType']==3)]
                if preferred:
                    candidates = preferred
        if len(candidates) != 1:
            skipped.append({**h,'reason':'ambiguous area' if candidates else 'no supported highlight','candidates':[a['constant'] for a in candidates]})
            continue
        area = candidates[0]
        pair = [area['kind'], area['constant']]
        mapping.setdefault(str(h['encounter']), [])
        if pair not in mapping[str(h['encounter'])]:
            mapping[str(h['encounter'])].append(pair)
        assignments.append({**h,'area':area['constant'],'kind':area['kind'],'basis':reason})
    entries = {int(p.name): p.read_bytes() for p in (project/'unpacked/encounters').iterdir() if p.is_file() and p.name.isdigit()}
    assert all(len(data)==196 for data in entries.values())
    packed_path = project/'files/a/0/3/7'
    packed = narc_members(packed_path.read_bytes()) if packed_path.exists() else []
    packed_differences = [i for i,data in entries.items() if i >= len(packed) or data != packed[i]]
    return {'headerCount':len(headers),'encounterFileCount':len(entries),'archiveMembers':len(members),'archiveSha256':hashlib.sha256(archive_path.read_bytes()).hexdigest(),
            'supportedAreas':supported,'unsupportedAreas':unsupported,'assignments':assignments,'skippedHeaders':skipped,
            'encounterAreaMapping':mapping,'packedVsUnpackedEncounterDifferences':packed_differences,
            'unreferencedEncounterIds':sorted(set(entries)-{h['encounter'] for h in headers.values()})}


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project',type=Path)
    parser.add_argument('--engine',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    report=audit(args.project,args.engine)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({key:value for key,value in report.items() if key not in ('supportedAreas','assignments','encounterAreaMapping')},indent=2))
