import json
import uuid
import datetime

# Unique IDs for the deck, note model, and configuration
deck_uuid = str(uuid.uuid4())
model_uuid = str(uuid.uuid4())
config_uuid = str(uuid.uuid4())

# Current date for "last updated"
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

# SVG definitions
SVG_CRESCENDO = '<svg width="100" height="40" viewBox="0 0 100 40"><path d="M 10 20 L 90 5 M 10 20 L 90 35" fill="none" stroke="black" stroke-width="2"/></svg>'
SVG_DECRESCENDO = '<svg width="100" height="40" viewBox="0 0 100 40"><path d="M 10 5 L 90 20 M 10 35 L 90 20" fill="none" stroke="black" stroke-width="2"/></svg>'
SVG_ARPEGGIO = '<svg width="20" height="60" viewBox="0 0 20 60"><path d="M 10 0 C 0 5 20 10 10 15 C 0 20 20 25 10 30 C 0 35 20 40 10 45 C 0 50 20 55 10 60" fill="none" stroke="black" stroke-width="2"/></svg>'
SVG_SLUR = '<svg width="100" height="40" viewBox="0 0 100 40"><path d="M 10 30 Q 50 0 90 30" fill="none" stroke="black" stroke-width="2"/></svg>'
SVG_TIE = '<svg width="60" height="20" viewBox="0 0 60 20"><path d="M 5 5 Q 30 20 55 5" fill="none" stroke="black" stroke-width="2"/></svg>'

# Flashcard data: (Front, Back, Tags)
cards_data = [
    ("Grave", "Very slow and solemn", ["tempo"]),
    ("Largo", "Slow and broad", ["tempo"]),
    ("Lento", "Slow", ["tempo"]),
    ("Adagio", "Slow, at ease", ["tempo"]),
    ("Adagietto", "Slightly faster than adagio", ["tempo"]),
    ("Andante", "At a walking pace", ["tempo"]),
    ("Andantino", "Slightly faster than andante", ["tempo"]),
    ("Moderato", "Moderately", ["tempo"]),
    ("Allegretto", "Moderately fast", ["tempo"]),
    ("Allegro", "Fast, quickly and bright", ["tempo"]),
    ("Vivace", "Lively and fast", ["tempo"]),
    ("Presto", "Very fast", ["tempo"]),
    ("Prestissimo", "Even faster than presto", ["tempo"]),
    ("Accelerando (accel.)", "Gradually getting faster", ["tempo_change"]),
    ("Rallentando (rall.)", "Gradually getting slower", ["tempo_change"]),
    ("Ritardando (rit.)", "Gradually getting slower", ["tempo_change"]),
    ("Ritenuto (riten.)", "Suddenly slower, held back", ["tempo_change"]),
    ("A tempo", "Return to the original tempo", ["tempo_change"]),
    ("Rubato", "Flexible tempo, 'stolen' time", ["tempo_change"]),
    ("Stringendo", "Pressing forward, getting faster", ["tempo_change"]),
    ("Pianissimo (pp)", "Very soft", ["dynamics"]),
    ("Piano (p)", "Soft", ["dynamics"]),
    ("Mezzo-piano (mp)", "Moderately soft", ["dynamics"]),
    ("Mezzo-forte (mf)", "Moderately loud", ["dynamics"]),
    ("Forte (f)", "Loud", ["dynamics"]),
    ("Fortissimo (ff)", "Very loud", ["dynamics"]),
    ("Sforzando (sfz)", "Suddenly loud, forced", ["dynamics"]),
    ("Crescendo " + SVG_CRESCENDO, "Gradually getting louder", ["dynamics"]),
    ("Decrescendo / Diminuendo " + SVG_DECRESCENDO, "Gradually getting softer", ["dynamics"]),
    ("Rinforzando (rfz)", "Suddenly reinforced", ["dynamics"]),
    ("Staccato (dot above/below)", "Short and detached", ["articulation"]),
    ("Staccatissimo (𝄾)", "Very short and detached", ["articulation"]),
    ("Legato " + SVG_SLUR, "Smooth and connected", ["articulation"]),
    ("Tenuto (- above/below)", "Held for its full value", ["articulation"]),
    ("Marcato (^) ", "Strongly accented", ["articulation"]),
    ("Accent (>) ", "Emphasized", ["articulation"]),
    ("Portato", "Semi-staccato, pulses between notes", ["articulation"]),
    ("Treble Clef (𝄞)", "G-clef, used for high pitches", ["symbol"]),
    ("Bass Clef (𝄢)", "F-clef, used for low pitches", ["symbol"]),
    ("Alto Clef (𝄡)", "C-clef centered on 3rd line", ["symbol"]),
    ("Tenor Clef (𝄡)", "C-clef centered on 4th line", ["symbol"]),
    ("Grand Staff", "Treble and Bass staves joined by a brace", ["symbol"]),
    ("Ledger Lines", "Short lines above/below the staff", ["symbol"]),
    ("Bar Line", "Vertical line dividing measures", ["symbol"]),
    ("Double Bar Line", "Two lines indicating a new section", ["symbol"]),
    ("Final Bar Line", "Indicates the end of the piece", ["symbol"]),
    ("Common Time (𝄴)", "4/4 time signature", ["rhythm"]),
    ("Cut Time (𝄵)", "2/2 time signature", ["rhythm"]),
    ("Time Signature", "Tells beats per measure and beat value", ["rhythm"]),
    ("Measure / Bar", "A segment of time defined by beats", ["rhythm"]),
    ("Tie " + SVG_TIE, "Connects two notes of the same pitch", ["rhythm"]),
    ("Slur " + SVG_SLUR, "Connects notes of different pitches", ["rhythm"]),
    ("Beam", "Connects stems of eighth/sixteenth notes", ["rhythm"]),
    ("Dot (after note)", "Increases note value by half", ["rhythm"]),
    ("Double Dot (after note)", "Increases note value by 3/4", ["rhythm"]),
    ("Trill (tr)", "Rapid alternation between two notes", ["ornament"]),
    ("Mordent (𝄗)", "Single alternation with note above", ["ornament"]),
    ("Inverted Mordent (𝄘)", "Single alternation with note below", ["ornament"]),
    ("Turn (𝄑)", "Note above, note, note below, note", ["ornament"]),
    ("Inverted Turn (𝄒)", "Note below, note, note above, note", ["ornament"]),
    ("Appoggiatura", "Leaning note (takes half the main note value)", ["ornament"]),
    ("Acciaccatura", "Grace note, 'crushed' note", ["ornament"]),
    ("Glissando", "Continuous slide between pitches", ["ornament"]),
    ("Da Capo (D.C.)", "From the beginning", ["form"]),
    ("Dal Segno (D.S.)", "From the sign", ["form"]),
    ("Segno (𝄋)", "The sign used with D.S.", ["form"]),
    ("Coda (𝄌)", "Tail, closing section", ["form"]),
    ("Fine", "The end", ["form"]),
    ("Repeat Sign (𝄆 𝄇)", "Repeat the music between the dots", ["form"]),
    ("First Ending", "Play the first time through a repeat", ["form"]),
    ("Second Ending", "Play the second time through a repeat", ["form"]),
    ("Cantabile", "In a singing style", ["expression"]),
    ("Dolce", "Sweetly", ["expression"]),
    ("Espressivo", "Expressively", ["expression"]),
    ("Grazioso", "Gracefully", ["expression"]),
    ("Leggiero", "Lightly", ["expression"]),
    ("Maestoso", "Majestically", ["expression"]),
    ("Molto", "Very, much", ["expression"]),
    ("Poco a poco", "Little by little", ["expression"]),
    ("Sempre", "Always", ["expression"]),
    ("Subito", "Suddenly", ["expression"]),
    ("Agitato", "Agitated", ["expression"]),
    ("Animato", "Animated", ["expression"]),
    ("Brillante", "Brilliant", ["expression"]),
    ("Con brio", "With spirit/vigor", ["expression"]),
    ("Con fuoco", "With fire", ["expression"]),
    ("Morendo", "Dying away", ["expression"]),
    ("Pesante", "Heavy", ["expression"]),
    ("Scherzando", "Joking, playful", ["expression"]),
    ("Sotto voce", "In an undertone, quiet", ["expression"]),
    ("Tranquillo", "Tranquil", ["expression"]),
    ("Octave (8va)", "Play an octave higher", ["other"]),
    ("Octave below (8vb)", "Play an octave lower", ["other"]),
    ("Con sordino", "With mute", ["other"]),
    ("Senza sordino", "Without mute", ["other"]),
    ("Arpeggio " + SVG_ARPEGGIO, "Notes of a chord played in succession", ["other"]),
    ("Fermata (𝄐)", "Hold the note longer than indicated", ["other"]),
    ("G.P. (Grand Pause)", "Entire ensemble pauses", ["other"]),
    ("Caesura (//)", "A pause or break in music", ["other"]),
    ("Simile", "Continue in a similar manner", ["other"]),
    ("Allargando", "Broadening, getting slower and louder", ["tempo"]),
    ("Giocoso", "Joyful, merry", ["expression"]),
    ("Meno Mosso", "Less motion (slower)", ["tempo_change"]),
    ("Più Mosso", "More motion (faster)", ["tempo_change"]),
    ("Agnus Dei", "Lamb of God (often used in Requiem/Mass)", ["term"]),
    ("Cadenza", "Ornamental passage for a soloist", ["form"]),
    ("Concerto", "Work for soloist and orchestra", ["form"]),
    ("Symphony", "Large work for orchestra", ["form"]),
    ("Libretto", "The text of an opera", ["term"]),
    ("Vibrato", "Small fluctuation in pitch", ["expression"])
]

# Ensure we have exactly 100 or more (the user asked for 100)
# Let's verify count
print(f"Total cards defined: {len(cards_data)}")

notes = []
for front, back, tags in cards_data[:100]:
    notes.append({
        "__type__": "Note",
        "fields": [front, back, current_date],
        "note_model_uuid": model_uuid,
        "tags": tags
    })

deck = {
    "__type__": "Deck",
    "children": [],
    "crowdanki_uuid": deck_uuid,
    "deck_configurations": [
        {
            "__type__": "DeckConfig",
            "crowdanki_uuid": config_uuid,
            "name": "Default",
            "new": {"perDay": 20},
            "rev": {"perDay": 200}
        }
    ],
    "deck_config_uuid": config_uuid,
    "desc": "100 Music Theory Flashcards generated for Michael.",
    "media_files": [],
    "name": "Music Theory Essentials",
    "note_models": [
        {
            "__type__": "NoteModel",
            "crowdanki_uuid": model_uuid,
            "flds": [
                {"name": "Front", "ord": 0},
                {"name": "Back", "ord": 1},
                {"name": "Last Updated", "ord": 2}
            ],
            "name": "Music Theory Card",
            "tmpls": [
                {
                    "name": "Card 1",
                    "qfmt": '<div style="font-family: Arial; font-size: 24px; text-align: center;">{{Front}}</div>',
                    "afmt": '{{FrontSide}}\n\n<hr id=answer>\n\n<div style="font-family: Arial; font-size: 20px; text-align: center;">{{Back}}</div>\n<div style="font-family: Arial; font-size: 12px; color: gray; text-align: center; margin-top: 20px;">Updated: {{Last Updated}}</div>'
                }
            ]
        }
    ],
    "notes": notes
}

with open("music_cards.json", "w", encoding="utf-8") as f:
    json.dump(deck, f, indent=2, ensure_ascii=False)

print("Done generating music_cards.json")
