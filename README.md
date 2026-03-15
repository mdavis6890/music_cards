# Music Theory Essentials Flashcards

A comprehensive collection of **168 music theory flashcards** designed for the Anki flashcard system. This deck covers a wide range of topics from basic symbols to advanced theoretical concepts, making it suitable for students and musicians at various levels.

## Features

- **168 Cards**: Includes terms, symbols, tempo indications, and more.
- **Categorized**: Cards are tagged by category (Tempo, Dynamics, Articulation, Rhythm, etc.).
- **Visuals**: Includes Unicode symbols and custom SVG graphics for musical notation.
- **Stable Updates**: Built with stable UUIDs, allowing you to re-import the file to update existing cards without losing your study progress.
- **Clear Layout**: Symbols and abbreviations are presented on the front, with detailed definitions and BPM ranges on the back.

## Categories Covered

- **Tempo**: Italian terms and specific BPM ranges.
- **Dynamics**: Volume markings from *ppp* to *fff*.
- **Articulation**: Staccato, legato, accents, and more.
- **Symbols**: Clefs, staff notation, and accidental markings.
- **Rhythm**: Time signatures, note values, and rhythmic patterns.
- **Form & Terms**: Musical structures (Fugue, Sonata, Symphony) and essential terminology.
- **Intervals**: Ear training and theory for all standard intervals.

## How to Import

1. **Install CrowdAnki**: You will need the [CrowdAnki](https://ankiweb.net/shared/info/1788670778) add-on installed in Anki.
2. **Download**: Ensure you have the `music_cards.json` file.
3. **Import**:
   - Open Anki.
   - Go to **File > CrowdAnki: Import from JSON**.
   - Select the `music_cards` folder (or the folder containing `music_cards.json`).

## Maintenance

If you wish to add your own terms or modify the deck:
1. Open `generate_deck.py`.
2. Add your data to the `cards_data` list.
3. Run the script: `python generate_deck.py`.
4. Re-import into Anki.
