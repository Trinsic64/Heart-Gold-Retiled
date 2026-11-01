# Pokémon Heartfelt Gold v1.0.1

This update fixes newly caught wild Pokémon losing their held items when they join a party with an open slot. The battle cleanup restored held items across the enlarged party using a snapshot taken before the catch, which cleared the new Pokémon's item. Cleanup now applies only to Pokémon present when the battle began. This also prevents a caught Pokémon's item from being treated as a newly stolen item and added to the Bag.

Wild species with two configured, different held items now receive one every encounter, with a 50% chance for each, regardless of a Compound Eyes lead. Species with the same item in both slots continue to hold that item every time. Species with only one or no configured item keep the original game behavior.

The v1.0.1 build also includes the queued Cyclizar wild encounters at Whirl Islands B3F and Route 24, along with updated trainer and Pokédex habitat data. See [next update notes](Docs/Next-Update-Notes.md).

Previously caught Pokémon that lost an item are not repaired retroactively. Check the Bag for a stone that may have been moved there, or catch a new Pokémon using v1.0.1. Back up your save before switching ROM builds; keep the save filename matched to the patched ROM filename in your emulator.

## Patch and verification

- Patch: `xDelta/Heartfelt-Gold-v1.0.1-Patch.xdelta` (34,542,123 bytes)
- Patch SHA-256: `9c3054b3e1b2d8492d75262eb7f0e6c61d80a48e3a0b7e3300dcab9438db6020`
- Compatible source: clean Pokémon HeartGold (USA), SHA-256 `65f02a56842b75aa92d775d56d657a56fe3fa993550b04dc20704ab82d760105` (MD5 and SHA-1 in the [README](README.md)). Apply this patch directly to the clean source, not to v1.0.0.
- Decoded ROM SHA-256: `3d63814b9ccbb22caca659c8721bff8127261db60cf1b7b05dc33dbff3b2a700` (209,627,104 bytes).

The patch decoded successfully against the clean source and reproduced the build byte for byte. The hg-engine build and DSPRE archive verification passed. The released build's Squirtle, Totodile, and Weedle personal data holds Blastoisinite, Feraligite, and Beedrillite respectively in both slots. An in-game capture test of this exact build is still pending.

The corresponding hg-engine code changes are recorded in [the source patch](HG-Engine/patches/held-items-v1.0.1.patch), based on hg-engine commit `398a30209`.
