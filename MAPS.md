# Mapping resources

The `Maps` directory contains the mapping resources used by Pokémon HeartGold Retiled. They are published for study, troubleshooting, and continued mapping work—not as a substitute for the original game.

## Layout

```text
Data/
└── Matrices/       Matrix data used by the maps

Maps/
├── Caves/          Current expanded cave mapping resources
├── Overworld/      Current expanded overworld mapping resources
├── Caves.rar       Convenience snapshot of cave resources
└── Overworld.rar   Convenience snapshot of overworld resources
```

The resources include textures, models, materials, collision/camera data, and Pokémon DS Map Studio project files. The `.imd` metadata identifies Pokémon DS Map Studio 1.0 as the generator for the model data.

Common formats include:

- `.png` textures;
- `.obj`, `.mtl`, and `.imd` model/material data;
- `.nsbmd` and `.nsbtx` Nintendo DS model/texture outputs;
- `.bdhc`, `.bdhcam`, `.bgs`, `.bld`, `.per`, and `.bin` map support data; and
- `.pdsmap` and `.pdsts` Pokémon DS Map Studio files; and
- `.mtx` binary matrix data.

The expanded `Maps/Caves` and `Maps/Overworld` directories are the current working resources. The RAR files are retained as smaller convenience snapshots and may not include the latest individual map edits.

## Archive verification

```text
B7F42BDD1CE0E3CEDCFC6A305B68AEAFC50B48501FB911DAFC3E1D0680593AAB  Maps/Overworld.rar
C4FE05D4193E720B00C887509EA1AB9E694C6C813FC1A4F5F0CD8096EEFC0314  Maps/Caves.rar
```

Both archives were inventoried before publication. No `.nds`, `.srl`, executable, save, DSPRE, overlay, or recognizable extracted-ROM project paths were found.

## Safe use

- Obtain tools from their official or otherwise trusted sources; no patcher or mapping executable is bundled here.
- Scan downloaded archives before extracting them.
- Extract into a new empty directory.
- Do not redistribute ROMs or extracted ROM projects alongside your changes.
- Submit changes only to mapping resources you have permission to share.

These files may incorporate or depend on third-party game assets. Their inclusion does not grant ownership of those assets or permission for commercial use.
