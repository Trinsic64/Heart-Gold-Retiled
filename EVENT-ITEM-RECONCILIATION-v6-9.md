# HG-Retiled v6.9 Event Item Reconciliation

This reconciliation targets `HG-Retiled-v6-9 (patched)_DSPRE_contents`, the working extraction for `HG-Retiled-v6-9 (patched).nds`.

## Rules applied

- Every audited overworld pickup is explicitly classified as DSPRE type `Item` (`3`) and resolves to a non-empty item ID.
- Held Mega Stones are checked against the actual holder species in `HG-Engine/data/Species.c`. This includes prior evolutionary stages such as Gastly, Flaaffy, Bulbasaur, Charmander, and Squirtle.
- A ground Mega Stone is restored to its pre-v6.6 item when a holder in its family reaches more than a 5% effective ordinary encounter rate.
- A ground Mega Stone remains when its wild holder has a maximum effective rate of 5% or less, is conditional/static, or has no held-item source.
- Six pickups that were already Mega Stones before the v6.6 replacement pass remain unchanged because the audited source inventory has no earlier non-Mega item ID for them.

## Results

- 257 pickup objects audited and validated.
- 166 `None` classifications corrected to `Item`.
- 15 pickup scripts corrected.
- One missing Route 29 pickup record reconstructed from the pre-change event backup. It remains Clefablite because Clefairy's maximum effective encounter rate is 5%.
- 13 duplicated ground Mega Stones restored to their original items.
- 79 ground Mega Stones retained: 68 rare/static/conditional sources, five with no wild held source, and six pre-existing placements.
- Final idempotency audit: zero changes remaining.

## Restored ground items

| Removed ground Mega Stone | Restored item | Maximum effective holder rate |
|---|---|---:|
| Gengarite | HP Up | 20% |
| Pidgeotite | Paralyze Heal | 20% |
| Beedrillite | Antidote | 26% |
| Sablenite | X Defense | 15% |
| Ampharosite | Super Repel | 10% |
| Medichamite | Iron | 24% |
| Mawilite | Escape Rope | 10% |
| Floettite | Max Potion | 10% |
| Raichunite X | Full Heal | 10% |
| Staraptite | Ultra Ball | 20% |
| Lucarionite Z | Ultra Ball | 10% |
| Meowsticite | Ultra Ball | 15% |
| Tatsugirinite | Ultra Ball | 40% |

The complete per-stone decision log is in `outputs/event-item-reconciliation-v6-9/mega-ground-pickup-decisions.csv`. The complete 257-object validation is in `outputs/event-item-reconciliation-v6-9/event-item-audit.csv`.

## Built ROM and recovery

- Fixed ROM: `HG-Retiled-v6-9 (event-items-fixed).nds` (local build; not committed or released)
- ROM SHA-256: `91809B188477CF458F1C1E8465A6C61D3CB46F3A88C1B2F59287E72342738D2C`
- Embedded event NARC SHA-256: `D31CE2FBBB5B59DDFC0253C2258B4E07202D7C2CA71F136FF6E0AEC6057A5B9E`
- Recovery backup: `HG-Retiled-v6-9 (patched)_event-item-backup-20260817` (local, outside the repository)

The original `HG-Retiled-v6-9 (patched).nds` was not overwritten.
