# Pokémon HeartGold Retiled

An unfinished visual overhaul of **Pokémon HeartGold** for Nintendo DS, with redesigned and retiled overworld and cave maps.

There are still some awkward or glitchy tiles, but the project is playable and ready for community feedback. If you try it, please share what worked, what looked odd, and where you found it.

> [!IMPORTANT]
> This repository contains an xDelta patch and mapping resources only. It does **not** contain a Nintendo DS ROM, a DSPRE project, or an extracted ROM. You must supply your own legally obtained copy of Pokémon HeartGold.

## Screenshots

<p align="center">
  <img src="Pictures/Screenshot%202026-08-12%20210204.png" width="32%" alt="Retiled town scene">
  <img src="Pictures/Screenshot%202026-08-12%20210320.png" width="32%" alt="Retiled cave scene">
  <img src="Pictures/Screenshot%202026-08-12%20210437.png" width="32%" alt="Retiled waterside scene">
</p>

## Download and play

The current patch is [HG-Retiled-v1-0-0.xdelta](Delta/HG-Retiled-v1-0-0.xdelta?raw=1).

You will need:

- your own clean Pokémon HeartGold ROM dump;
- the `.xdelta` patch from this repository; and
- a reputable xDelta-compatible patcher.

To apply it:

1. Back up your clean ROM dump.
2. Open your xDelta patcher.
3. Select your clean ROM as the source file.
4. Select `Delta/HG-Retiled-v1-0-0.xdelta` as the patch.
5. Choose a new output filename and apply the patch.

The exact compatible ROM region/revision and source hash have not yet been documented. If your patcher reports a source mismatch, do not force it; check that you are using the correct clean, unmodified dump.

## Verify the download

SHA-256:

```text
CA0B1E7287BCBFFB70DF3F203AE51E13FDE2D7B9B17710D92BCD8BF2A34280DF  Delta/HG-Retiled-v1-0-0.xdelta
```

On PowerShell:

```powershell
Get-FileHash .\Delta\HG-Retiled-v1-0-0.xdelta -Algorithm SHA256
```

On macOS or Linux:

```bash
sha256sum Delta/HG-Retiled-v1-0-0.xdelta
```

The map archive hashes are recorded in [checksums.sha256](checksums.sha256).

## Maps for creators

The [Maps](Maps) directory is included for people interested in mapping or studying the project. It contains the expanded overworld and cave resources, plus convenience RAR archives.

See [MAPS.md](MAPS.md) for the contents, formats, archive checksums, and safe-use notes.

## Project status

This is a work in progress. Expect visual errors, awkward transitions, and incomplete polish in some locations.

When reporting a problem, please include:

- the location and nearest landmark;
- what the tile should look like;
- a screenshot if possible; and
- the patch version (`v1.0.0`).

Please do not attach ROMs, saves containing personal information, DSPRE workspaces, or extracted game data to issues or pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Legal notice

This is an unofficial, non-commercial fan project. Pokémon and Pokémon HeartGold are trademarks of their respective owners. This project is not affiliated with, endorsed by, or sponsored by Nintendo, The Pokémon Company, GAME FREAK, or Creatures Inc.

No game ROM is provided. You are responsible for complying with the laws that apply to you and for using a legally obtained copy of the game. Third-party game assets remain the property of their respective owners. No general license is granted for the repository contents; see [NOTICE.md](NOTICE.md).

