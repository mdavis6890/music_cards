import json
import uuid
import datetime

# Hardcoded UUIDs to ensure CrowdAnki updates the existing deck/notes
DECK_UUID = "750d1615-d202-4515-9f30-cbdc20bd101b"
MODEL_UUID = "573afed7-aff4-4afd-8d78-b99fde01ff84"
CONFIG_UUID = "23d66125-811c-4b9b-9347-0ba46aaf4d6c"

# Namespace for generating stable note UUIDs
NOTE_NAMESPACE = uuid.UUID(DECK_UUID)

# Current date for "last updated"
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

# SVG definitions
SVG_CRESCENDO = '<svg width="100" height="40" viewBox="0 0 100 40"><path d="M 10 20 L 90 5 M 10 20 L 90 35" fill="none" stroke="black" stroke-width="2"/></svg>'
SVG_DECRESCENDO = '<svg width="100" height="40" viewBox="0 0 100 40"><path d="M 10 5 L 90 20 M 10 35 L 90 20" fill="none" stroke="black" stroke-width="2"/></svg>'
SVG_ARPEGGIO = '<svg width="20" height="60" viewBox="0 0 20 60"><path d="M 10 0 C 0 5 20 10 10 15 C 0 20 20 25 10 30 C 0 35 20 40 10 45 C 0 50 20 55 10 60" fill="none" stroke="black" stroke-width="2"/></svg>'
SVG_SLUR = '<svg width="100" height="40" viewBox="0 0 100 40"><path d="M 10 30 Q 50 0 90 30" fill="none" stroke="black" stroke-width="2"/></svg>'
SVG_TIE = '<svg width="60" height="20" viewBox="0 0 60 20"><path d="M 5 5 Q 30 20 55 5" fill="none" stroke="black" stroke-width="2"/></svg>'

# Flashcard data: (Front, Back, Category, Tags)
cards_data = [
    ("Grave", "Very slow and solemn (20–40 BPM)", "Tempo", ["tempo"]),
    ("Largo", "Slow and broad (40–60 BPM)", "Tempo", ["tempo"]),
    ("Lento", "Slow (40–60 BPM)", "Tempo", ["tempo"]),
    ("Adagio", "Slow, at ease (66–76 BPM)", "Tempo", ["tempo"]),
    ("Adagietto", "Slightly faster than adagio (70–80 BPM)", "Tempo", ["tempo"]),
    ("Andante", "At a walking pace (76–108 BPM)", "Tempo", ["tempo"]),
    ("Andantino", "Slightly faster than andante (80–108 BPM)", "Tempo", ["tempo"]),
    ("Moderato", "Moderately (108–120 BPM)", "Tempo", ["tempo"]),
    ("Allegretto", "Moderately fast (112–120 BPM)", "Tempo", ["tempo"]),
    ("Allegro", "Fast, quickly and bright (120–156 BPM)", "Tempo", ["tempo"]),
    ("Vivace", "Lively and fast (156–176 BPM)", "Tempo", ["tempo"]),
    ("Presto", "Very fast (168–200 BPM)", "Tempo", ["tempo"]),
    ("Prestissimo", "Even faster than presto (200+ BPM)", "Tempo", ["tempo"]),
    ("accel.", "Accelerando: Gradually getting faster", "Tempo Change", ["tempo_change"]),
    ("rall.", "Rallentando: Gradually getting slower", "Tempo Change", ["tempo_change"]),
    ("rit.", "Ritardando: Gradually getting slower", "Tempo Change", ["tempo_change"]),
    ("riten.", "Ritenuto: Suddenly slower, held back", "Tempo Change", ["tempo_change"]),
    ("A tempo", "Return to the original tempo", "Tempo Change", ["tempo_change"]),
    ("Rubato", "Flexible tempo, 'stolen' time", "Tempo Change", ["tempo_change"]),
    ("Stringendo", "Pressing forward, getting faster", "Tempo Change", ["tempo_change"]),
    ("pp", "Pianissimo: Very soft", "Dynamics", ["dynamics"]),
    ("p", "Piano: Soft", "Dynamics", ["dynamics"]),
    ("mp", "Mezzo-piano: Moderately soft", "Dynamics", ["dynamics"]),
    ("mf", "Mezzo-forte: Moderately loud", "Dynamics", ["dynamics"]),
    ("f", "Forte: Loud", "Dynamics", ["dynamics"]),
    ("ff", "Fortissimo: Very loud", "Dynamics", ["dynamics"]),
    ("sfz", "Sforzando: Suddenly loud, forced", "Dynamics", ["dynamics"]),
    (SVG_CRESCENDO, "Crescendo: Gradually getting louder", "Dynamics", ["dynamics"]),
    (SVG_DECRESCENDO, "Decrescendo / Diminuendo: Gradually getting softer", "Dynamics", ["dynamics"]),
    ("rfz", "Rinforzando: Suddenly reinforced", "Dynamics", ["dynamics"]),
    (".", "Staccato: Short and detached (dot above/below note)", "Articulation", ["articulation"]),
    ("𝅘𝅥𝅾", "Staccatissimo: Very short and detached", "Articulation", ["articulation"]),
    (SVG_SLUR, "Legato: Smooth and connected", "Articulation", ["articulation"]),
    ("-", "Tenuto: Held for its full value (line above/below note)", "Articulation", ["articulation"]),
    ("^", "Marcato: Strongly accented", "Articulation", ["articulation"]),
    (">", "Accent: Emphasized", "Articulation", ["articulation"]),
    ("Portato", "Semi-staccato, pulses between notes", "Articulation", ["articulation"]),
    ("𝄞", "Treble Clef: G-clef, used for high pitches", "Symbol", ["symbol"]),
    ("𝄢", "Bass Clef: F-clef, used for low pitches", "Symbol", ["symbol"]),
    ("𝄡 (on 3rd line)", "Alto Clef: C-clef centered on 3rd line", "Symbol", ["symbol"]),
    ("𝄡 (on 4th line)", "Tenor Clef: C-clef centered on 4th line", "Symbol", ["symbol"]),
    ("Grand Staff", "Treble and Bass staves joined by a brace", "Symbol", ["symbol"]),
    ("Ledger Lines", "Short lines above/below the staff", "Symbol", ["symbol"]),
    ("Bar Line", "Vertical line dividing measures", "Symbol", ["symbol"]),
    ("Double Bar Line", "Two lines indicating a new section", "Symbol", ["symbol"]),
    ("Final Bar Line", "Indicates the end of the piece", "Symbol", ["symbol"]),
    ("𝄴", "Common Time: 4/4 time signature", "Rhythm", ["rhythm"]),
    ("𝄵", "Cut Time: 2/2 time signature", "Rhythm", ["rhythm"]),
    ("Time Signature", "Tells beats per measure and beat value", "Rhythm", ["rhythm"]),
    ("Measure / Bar", "A segment of time defined by beats", "Rhythm", ["rhythm"]),
    (SVG_TIE, "Tie: Connects two notes of the same pitch", "Rhythm", ["rhythm"]),
    (SVG_SLUR, "Slur: Connects notes of different pitches", "Rhythm", ["rhythm"]),
    ("Beam", "Connects stems of eighth/sixteenth notes", "Rhythm", ["rhythm"]),
    ("Dot (after note)", "Increases note value by half", "Rhythm", ["rhythm"]),
    ("Double Dot (after note)", "Increases note value by 3/4", "Rhythm", ["rhythm"]),
    ("tr", "Trill: Rapid alternation between two notes", "Ornament", ["ornament"]),
    ("𝄗", "Mordent: Single alternation with note above", "Ornament", ["ornament"]),
    ("𝄘", "Inverted Mordent: Single alternation with note below", "Ornament", ["ornament"]),
    ("𝄑", "Turn: Note above, note, note below, note", "Ornament", ["ornament"]),
    ("𝄒", "Inverted Turn: Note below, note, note above, note", "Ornament", ["ornament"]),
    ("Appoggiatura", "Leaning note (takes half the main note value)", "Ornament", ["ornament"]),
    ("Acciaccatura", "Grace note, 'crushed' note", "Ornament", ["ornament"]),
    ("Glissando", "Continuous slide between pitches", "Ornament", ["ornament"]),
    ("D.C.", "Da Capo: From the beginning", "Form", ["form"]),
    ("D.S.", "Dal Segno: From the sign", "Form", ["form"]),
    ("𝄋", "Segno: The sign used with D.S.", "Form", ["form"]),
    ("𝄌", "Coda: Tail, closing section", "Form", ["form"]),
    ("Fine", "The end", "Form", ["form"]),
    ("𝄆 𝄇", "Repeat Sign: Repeat the music between the dots", "Form", ["form"]),
    ("First Ending", "Play the first time through a repeat", "Form", ["form"]),
    ("Second Ending", "Play the second time through a repeat", "Form", ["form"]),
    ("Cantabile", "In a singing style", "Expression", ["expression"]),
    ("Dolce", "Sweetly", "Expression", ["expression"]),
    ("Espressivo", "Expressively", "Expression", ["expression"]),
    ("Grazioso", "Gracefully", "Expression", ["expression"]),
    ("Leggiero", "Lightly", "Expression", ["expression"]),
    ("Maestoso", "Majestically", "Expression", ["expression"]),
    ("Molto", "Very, much", "Expression", ["expression"]),
    ("Poco a poco", "Little by little", "Expression", ["expression"]),
    ("Sempre", "Always", "Expression", ["expression"]),
    ("Subito", "Suddenly", "Expression", ["expression"]),
    ("Agitato", "Agitated", "Expression", ["expression"]),
    ("Animato", "Animated", "Expression", ["expression"]),
    ("Brillante", "Brilliant", "Expression", ["expression"]),
    ("Con brio", "With spirit/vigor", "Expression", ["expression"]),
    ("Con fuoco", "With fire", "Expression", ["expression"]),
    ("Morendo", "Dying away", "Expression", ["expression"]),
    ("Pesante", "Heavy", "Expression", ["expression"]),
    ("Scherzando", "Joking, playful", "Expression", ["expression"]),
    ("Sotto voce", "In an undertone, quiet", "Expression", ["expression"]),
    ("Tranquillo", "Tranquil", "Expression", ["expression"]),
    ("8va", "Octave: Play an octave higher", "Other", ["other"]),
    ("8vb", "Octave below: Play an octave lower", "Other", ["other"]),
    ("Con sordino", "With mute", "Other", ["other"]),
    ("Senza sordino", "Without mute", "Other", ["other"]),
    (SVG_ARPEGGIO, "Arpeggio: Notes of a chord played in succession", "Other", ["other"]),
    ("𝄐", "Fermata: Hold the note longer than indicated", "Other", ["other"]),
    ("G.P.", "Grand Pause: Entire ensemble pauses", "Other", ["other"]),
    ("//", "Caesura: A pause or break in music", "Other", ["other"]),
    ("Simile", "Continue in a similar manner", "Other", ["other"]),
    ("Allargando", "Broadening, getting slower and louder", "Tempo", ["tempo"]),
    ("Giocoso", "Joyful, merry", "Expression", ["expression"]),
    ("Meno Mosso", "Less motion (slower)", "Tempo Change", ["tempo_change"]),
    ("Più Mosso", "More motion (faster)", "Tempo Change", ["tempo_change"]),
    ("Agnus Dei", "Lamb of God (often used in Requiem/Mass)", "Term", ["term"]),
    ("Cadenza", "Ornamental passage for a soloist", "Form", ["form"]),
    ("Concerto", "Work for soloist and orchestra", "Form", ["form"]),
    ("Symphony", "Large work for orchestra", "Form", ["form"]),
    ("Libretto", "The text of an opera", "Term", ["term"]),
    ("Vibrato", "Small fluctuation in pitch", "Expression", ["expression"]),
    ("Enharmonic", "Notes that sound the same but have different names (e.g., C# and Db)", "Term", ["term"]),
    ("Diatonic", "Belonging to the current scale or key", "Term", ["term"]),
    ("Chromatic", "Using notes outside the current scale/key", "Term", ["term"]),
    ("Syncopation", "Emphasizing the weak beats or off-beats", "Rhythm", ["rhythm"]),
    ("Transposition", "Shifting music to a different pitch level", "Term", ["term"]),
    ("Modulation", "Changing from one key to another", "Term", ["term"]),
    ("Relative Key", "Major and minor keys that share the same key signature", "Term", ["term"]),
    ("Parallel Key", "Major and minor keys that share the same tonic", "Term", ["term"]),
    ("Alberti Bass", "A broken chord accompaniment pattern", "Expression", ["expression"]),
    ("Ostinato", "A continually repeated musical phrase or rhythm", "Form", ["form"]),
    ("Sequence", "Restatement of a motif at a higher or lower pitch", "Form", ["form"]),
    ("Inversion", "Turning a melody or chord upside down", "Term", ["term"]),
    ("Cadence", "A melodic or harmonic configuration that creates a sense of resolution", "Form", ["form"]),
    ("Picardy Third", "Ending a minor-key piece with a major chord", "Term", ["term"]),
    ("Motif", "A short musical idea or fragment", "Form", ["form"]),
    ("Theme", "A complete musical thought used as a building block", "Form", ["form"]),
    ("Counterpoint", "The relationship between independent melodic lines", "Form", ["form"]),
    ("Fugue", "A contrapuntal composition based on a main theme (subject)", "Form", ["form"]),
    ("Suite", "A collection of short musical pieces", "Form", ["form"]),
    ("Overture", "An introductory piece to an opera or larger work", "Form", ["form"]),
    ("Oratorio", "A large-scale musical work for orchestra and voices, usually on a religious theme", "Form", ["form"]),
    ("Aria", "A self-contained piece for a single voice, usually in an opera", "Form", ["form"]),
    ("Recitative", "A style of delivery in which a singer is allowed to adopt the rhythms of ordinary speech", "Form", ["form"]),
    ("Chorus", "A large group of singers", "Term", ["term"]),
    ("Timbre", "The quality or 'color' of a sound", "Expression", ["expression"]),
    ("Texture", "How melodic, rhythmic, and harmonic materials are combined", "Term", ["term"]),
    ("Monophony", "A single melodic line without accompaniment", "Term", ["term"]),
    ("Polyphony", "Multiple independent melodic lines", "Term", ["term"]),
    ("Homophony", "A primary melody with chordal accompaniment", "Term", ["term"]),
    ("Heterophony", "Multiple versions of the same melody played simultaneously", "Term", ["term"]),
    ("Consonance", "Stable, pleasant-sounding intervals or chords", "Expression", ["expression"]),
    ("Dissonance", "Unstable, harsh-sounding intervals or chords", "Expression", ["expression"]),
    ("Resolution", "Movement from dissonance to consonance", "Expression", ["expression"]),
    ("Atonality", "Absence of a tonal center or key", "Term", ["term"]),
    ("Bitonality", "Use of two different keys simultaneously", "Term", ["term"]),
    ("Polytonality", "Use of multiple keys simultaneously", "Term", ["term"]),
    ("Microtonality", "Use of intervals smaller than a semitone", "Term", ["term"]),
    ("Pentatonic Scale", "A five-note scale", "Term", ["term"]),
    ("Whole Tone Scale", "A scale consisting entirely of whole steps", "Term", ["term"]),
    ("Chromatic Scale", "A scale consisting entirely of half steps", "Term", ["term"]),
    ("Octatonic Scale", "An eight-note scale alternating whole and half steps", "Term", ["term"]),
    ("♯", "Sharp: Raises a note by a half step", "Symbol", ["symbol"]),
    ("♭", "Flat: Lowers a note by a half step", "Symbol", ["symbol"]),
    ("♮", "Natural: Cancels a previous sharp or flat", "Symbol", ["symbol"]),
    ("𝄪", "Double Sharp: Raises a note by a whole step", "Symbol", ["symbol"]),
    ("𝄫", "Double Flat: Lowers a note by a whole step", "Symbol", ["symbol"]),
    ("Major Second", "An interval of 2 semitones (e.g., C to D)", "Interval", ["interval"]),
    ("Minor Second", "An interval of 1 semitone (e.g., C to Db)", "Interval", ["interval"]),
    ("Major Third", "An interval of 4 semitones (e.g., C to E)", "Interval", ["interval"]),
    ("Minor Third", "An interval of 3 semitones (e.g., C to Eb)", "Interval", ["interval"]),
    ("Perfect Fourth", "An interval of 5 semitones (e.g., C to F)", "Interval", ["interval"]),
    ("Tritone", "An interval of 6 semitones (Augmented 4th / Diminished 5th)", "Interval", ["interval"]),
    ("Perfect Fifth", "An interval of 7 semitones (e.g., C to G)", "Interval", ["interval"]),
    ("Major Sixth", "An interval of 9 semitones (e.g., C to A)", "Interval", ["interval"]),
    ("Minor Sixth", "An interval of 8 semitones (e.g., C to Ab)", "Interval", ["interval"]),
    ("Major Seventh", "An interval of 11 semitones (e.g., C to B)", "Interval", ["interval"]),
    ("Minor Seventh", "An interval of 10 semitones (e.g., C to Bb)", "Interval", ["interval"]),
    ("Perfect Octave", "An interval of 12 semitones (e.g., C to C)", "Interval", ["interval"])
]

notes = []
for front, back, category, tags in cards_data:
    # Stable note UUID based on front content
    note_uuid = str(uuid.uuid5(NOTE_NAMESPACE, front))
    notes.append({
        "__type__": "Note",
        "crowdanki_uuid": note_uuid,
        "guid": note_uuid[:10],
        "fields": [front, back, category, current_date],
        "note_model_uuid": MODEL_UUID,
        "tags": tags
    })

deck = {
    "__type__": "Deck",
    "children": [],
    "crowdanki_uuid": DECK_UUID,
    "deck_configurations": [
        {
            "__type__": "DeckConfig",
            "crowdanki_uuid": CONFIG_UUID,
            "name": "Default",
            "new": {"perDay": 20},
            "rev": {"perDay": 200}
        }
    ],
    "deck_config_uuid": CONFIG_UUID,
    "desc": "168 Music Theory Flashcards generated for Michael with stable UUIDs for updates.",
    "media_files": [],
    "name": "Music Theory Essentials",
    "note_models": [
        {
            "__type__": "NoteModel",
            "crowdanki_uuid": MODEL_UUID,
            "flds": [
                {
                    "name": "Front",
                    "ord": 0,
                    "sticky": False,
                    "rtl": False,
                    "font": "Arial",
                    "size": 20,
                    "media": []
                },
                {
                    "name": "Back",
                    "ord": 1,
                    "sticky": False,
                    "rtl": False,
                    "font": "Arial",
                    "size": 20,
                    "media": []
                },
                {
                    "name": "Category",
                    "ord": 2,
                    "sticky": False,
                    "rtl": False,
                    "font": "Arial",
                    "size": 20,
                    "media": []
                },
                {
                    "name": "Last Updated",
                    "ord": 3,
                    "sticky": False,
                    "rtl": False,
                    "font": "Arial",
                    "size": 20,
                    "media": []
                }
            ],
            "name": "Music Theory Card",
            "css": ".card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n",
            "type": 0,
            "sortf": 0,
            "tags": [],
            "vers": [],
            "tmpls": [
                {
                    "name": "Card 1",
                    "ord": 0,
                    "qfmt": '<div style="font-family: Arial; font-size: 14px; color: gray; margin-bottom: 10px;">{{Category}}</div><div style="font-family: Arial; font-size: 32px; text-align: center;">{{Front}}</div>',
                    "afmt": '{{FrontSide}}\n\n<hr id=answer>\n\n<div style="font-family: Arial; font-size: 20px; text-align: center;">{{Back}}</div>\n<div style="font-family: Arial; font-size: 12px; color: gray; text-align: center; margin-top: 20px;">Updated: {{Last Updated}}</div>'
                }
            ]
        }
    ],
    "notes": notes
}

with open("music_cards.json", "w", encoding="utf-8") as f:
    json.dump(deck, f, indent=2, ensure_ascii=False)

print("Done generating music_cards.json with stable UUIDs.")
