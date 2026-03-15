# Project Notes: Music Theory Flashcards

## Goal
Generate 100 music theory flashcards (terms, symbols, tempo indications) in CrowdAnki JSON format for Anki import.

## Status
- [x] Researched CrowdAnki JSON format.
- [x] Defined 100+ music theory terms and symbols.
- [x] Created `generate_deck.py` to automate JSON generation.
- [x] Generated `music_cards.json` with 100 cards.
  - Renamed from `music_theory_deck.json` to match the directory name (`music_cards`) for CrowdAnki compatibility.
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
