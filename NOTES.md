# Project Notes: Music Theory Flashcards

## Goal
Generate 150+ music theory flashcards (terms, symbols, tempo indications) in CrowdAnki JSON format for Anki import.

## Status
- [x] Researched CrowdAnki JSON format.
- [x] Defined 168 music theory terms and symbols.
- [x] Created `generate_deck.py` to automate JSON generation.
- [x] Generated `music_cards.json` with 168 cards.
  - Renamed from `music_theory_deck.json` to match the directory name (`music_cards`) for CrowdAnki compatibility.
  - Fixed "missing field `sticky`" error by adding required `NoteModel` properties.
  - **Hardcoded UUIDs**: Switched from content-hashing (uuid.uuid5) to hardcoding note UUIDs in `generate_deck.py` to ensure perfect stability even when card content (SVGs) changes.
  - Added Anki **guid** field to each note for stable imports.
  - Added **Category** field to each card (e.g., Tempo, Dynamics, Articulation).
  - Included **Specific numeric ranges (BPM)** for all tempo indications.
  - **Refined Layout**: Symbols and abbreviations are now alone on the **Front**, with names and definitions on the **Back**.
  - **Custom SVG Visuals**: 
    - Added custom SVGs for **Bar Line**, **Double Bar Line**, and **Final Bar Line** with staff backgrounds.
    - Added improved SVGs for **Tie** and **Slur** on a staff with noteheads to clarify their difference.
    - Added custom SVGs for **Upper Mordent** and **Lower (Inverted) Mordent**.
  - **Updated Unicode Symbols**: Turn (`𝆗`), Inverted Turn (`𝆘`), Appoggiatura (`𝆕`), and Acciaccatura (`𝆔`).
  - Includes "Last Updated" field (2026-03-25).
- [x] Updated `crowdanki-expert` skill with a new workflow rule: "run the generator script before committing".
- [x] Verified JSON structure and SVG embedding.
- [x] Committed and pushed all changes to the remote repository.

## Files
- `generate_deck.py`: Python script used to build the deck.
- `music_cards.json`: The final CrowdAnki export file.
- `NOTES.md`: Project notes and status tracking.

## Next Steps
- User to re-import `music_cards.json` into Anki using the CrowdAnki add-on to apply the latest visual updates.
- Maintain and update this deck as needed.
