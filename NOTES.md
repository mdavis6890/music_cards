# Project Notes: Music Theory Flashcards

## Goal
Generate 100 music theory flashcards (terms, symbols, tempo indications) in CrowdAnki JSON format for Anki import.

## Status
- [x] Researched CrowdAnki JSON format.
- [x] Defined 100+ music theory terms and symbols.
- [x] Created `generate_deck.py` to automate JSON generation.
- [x] Generated `music_cards.json` with 100 cards.
  - Renamed from `music_theory_deck.json` to match the directory name (`music_cards`) for CrowdAnki compatibility.
  - Fixed "missing field `sticky`" error by adding required `NoteModel` properties.
  - Added **Category** field to each card (e.g., Tempo, Dynamics, Articulation).
  - Included **Specific numeric ranges (BPM)** for all tempo indications.
  - **Refined Layout**: Symbols (e.g., `𝄞`, `𝄐`) and abbreviations (e.g., `mf`, `accel.`) are now alone on the **Front**, with names and definitions on the **Back**.
  - Includes Unicode symbols for standard notations.
  - Includes embedded SVG for complex symbols (hairpins, slurs, arpeggios).
  - Includes "Last Updated" field (2026-03-15).
- [x] Verified JSON structure and SVG embedding.

## Files
- `generate_deck.py`: Python script used to build the deck.
- `music_cards.json`: The final CrowdAnki export file.

## Next Steps
- User to import `music_cards.json` into Anki using the CrowdAnki add-on.
- Maintain and update this deck as needed.
