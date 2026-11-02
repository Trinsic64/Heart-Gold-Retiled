# Pokémon Heartfelt Gold v1.0.2

This update fixes regional-form Pokémon, their battle sprite positioning, and a Pokédex freeze. It includes the fixes from v1.0.1.

## Fixes

- Regional forms in wild encounters and trainer parties now use the correct base species and form number when creating Pokémon. This fixes the invalid species/form combinations behind the reported post-capture Pokédex registration crash.
- Battle sprites now use the regional form's animation and positioning metadata. This lowers Alolan Diglett by 23 DS pixels and Hisuian Sneasel by 16 DS pixels compared with the incorrect base-form positioning in the earlier test build. Form resolution also avoids converting an already adjusted sprite ID twice.
- Pokédex height and weight text loads one entry at a time. Loading the entire expanded text bank could exhaust the available heap and overwrite executable memory, freezing the game while viewing an entry after searching.
- The two-slot wild held-item rule now reads the form-specific item slots.

## Save compatibility

**Save import friendly and compatible with previous Heartfelt Gold versions. No new game is required.** The save format is unchanged.

Back up your existing in-game save, then import it or copy it with the filename expected by your emulator for the new ROM. Start the new ROM and load the in-game save. Emulator save states contain the older game's code and memory, so do not use an older build's save state to start this update.

The form correction applies when Pokémon are generated. It does not automatically rewrite malformed regional-form Pokémon previously stored by an older build.

## Patch

- File: `xDelta/Heartfelt-Gold-v1.0.2-Patch.xdelta`
- Size: 39,712,133 bytes
- SHA-256: `341d63d598ddaee8f0379e85de548d74bd54010a5d8410d7bf038f8df5b0c2dc`
- Required source: clean Pokémon HeartGold (USA), SHA-256 `65f02a56842b75aa92d775d56d657a56fe3fa993550b04dc20704ab82d760105`; MD5 `258cea3a62ac0d6eb04b5a0fd764d788`; SHA-1 `4fcded0e2713dc03929845de631d0932ea2b5a37`.
- Decoded ROM: 209,627,616 bytes; SHA-256 `706bafd0405a2086887de628a450ffedfea81a495b7d1accd800ebf987d0e44f`.

Apply this patch directly to the clean USA source. Do not stack it on an older Heartfelt Gold ROM. Your save can be transferred separately.

## Verification

The supplied patch decoded against the clean USA source and reproduced the approved Test 4 ROM byte for byte. The hg-engine build and DSPRE archive audit passed. Compiled ARM tests covered 1,536 species/form inputs, 1,828 sprite form lookups, and the image-to-positioning handoff for Alolan Diglett, Hisuian Sneasel, and a normal Charizard. The final ROM retains the corrected height/weight message-loading instructions. These checks do not represent a full game playthrough.

The engine changes are recorded in [the v1.0.2 source patch](HG-Engine/patches/regional-forms-v1.0.2.patch). It applies after [the v1.0.1 source patch](HG-Engine/patches/held-items-v1.0.1.patch) on hg-engine commit `398a30209`.
