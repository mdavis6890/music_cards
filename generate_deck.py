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
SVG_STAFF_BG = '<path d="M 10 10 L 90 10 M 10 20 L 90 20 M 10 30 L 90 30 M 10 40 L 90 40 M 10 50 L 90 50" fill="none" stroke="gray" stroke-width="1"/>'
SVG_SLUR = f'<svg width="100" height="60" viewBox="0 0 100 60">{SVG_STAFF_BG}<ellipse cx="30" cy="40" rx="5" ry="4" fill="black" transform="rotate(-15 30 40)"/><path d="M 34 40 L 34 15" stroke="black" stroke-width="1.5"/><ellipse cx="70" cy="30" rx="5" ry="4" fill="black" transform="rotate(-15 70 30)"/><path d="M 74 30 L 74 10" stroke="black" stroke-width="1.5"/><path d="M 32 45 Q 50 55 68 35" fill="none" stroke="black" stroke-width="2"/></svg>'
SVG_TIE = f'<svg width="100" height="60" viewBox="0 0 100 60">{SVG_STAFF_BG}<ellipse cx="30" cy="30" rx="5" ry="4" fill="black" transform="rotate(-15 30 30)"/><path d="M 34 30 L 34 10" stroke="black" stroke-width="1.5"/><ellipse cx="70" cy="30" rx="5" ry="4" fill="black" transform="rotate(-15 70 30)"/><path d="M 74 30 L 74 10" stroke="black" stroke-width="1.5"/><path d="M 32 35 Q 50 45 68 35" fill="none" stroke="black" stroke-width="2"/></svg>'
SVG_BARLINE = f'<svg width="100" height="60" viewBox="0 0 100 60">{SVG_STAFF_BG}<path d="M 50 10 L 50 50" fill="none" stroke="black" stroke-width="2"/></svg>'
SVG_DOUBLE_BARLINE = f'<svg width="100" height="60" viewBox="0 0 100 60">{SVG_STAFF_BG}<path d="M 45 10 L 45 50 M 55 10 L 55 50" fill="none" stroke="black" stroke-width="2"/></svg>'
SVG_FINAL_BARLINE = f'<svg width="100" height="60" viewBox="0 0 100 60">{SVG_STAFF_BG}<path d="M 42 10 L 42 50" fill="none" stroke="black" stroke-width="1.5"/><path d="M 52 10 L 52 50" fill="none" stroke="black" stroke-width="5"/></svg>'

# Flashcard data: (Front, Back, Category, Tags)
cards_data = [
    ("88719cb1-e68f-5881-b1a0-840923a63a6c", "Grave", "Very slow and solemn (20–40 BPM)", "Tempo", ["tempo"]),
    ("f5a0366b-1946-5326-a771-777342eb513e", "Largo", "Slow and broad (40–60 BPM)", "Tempo", ["tempo"]),
    ("f277841b-37f5-5f78-9bf4-40b22f661706", "Lento", "Slow (40–60 BPM)", "Tempo", ["tempo"]),
    ("90232367-8870-5a23-b099-061f7820cdad", "Adagio", "Slow, at ease (66–76 BPM)", "Tempo", ["tempo"]),
    ("4c35a614-a60f-51b1-9dc5-f2371abb0bb6", "Adagietto", "Slightly faster than adagio (70–80 BPM)", "Tempo", ["tempo"]),
    ("a19fec64-06f0-5bab-ab71-62531598c76b", "Andante", "At a walking pace (76–108 BPM)", "Tempo", ["tempo"]),
    ("2b8fa333-24c3-5b31-8c0e-19cb3cec8eee", "Andantino", "Slightly faster than andante (80–108 BPM)", "Tempo", ["tempo"]),
    ("0770ac8d-8612-538d-8fa1-5b6a719fd5eb", "Moderato", "Moderately (108–120 BPM)", "Tempo", ["tempo"]),
    ("fe58ee32-fb3f-528a-865c-399311655a88", "Allegretto", "Moderately fast (112–120 BPM)", "Tempo", ["tempo"]),
    ("af6df346-44fa-576e-bb5f-648a17de68c9", "Allegro", "Fast, quickly and bright (120–156 BPM)", "Tempo", ["tempo"]),
    ("eed7d8cc-ce79-56eb-837a-a9f551e12256", "Vivace", "Lively and fast (156–176 BPM)", "Tempo", ["tempo"]),
    ("66cf19a4-8443-5264-b618-05423f68d4d6", "Presto", "Very fast (168–200 BPM)", "Tempo", ["tempo"]),
    ("6910befd-526d-52f7-babe-d724a557662f", "Prestissimo", "Even faster than presto (200+ BPM)", "Tempo", ["tempo"]),
    ("c8d67714-2d67-5a53-8a51-c79ab7c83f5f", "accel.", "Accelerando: Gradually getting faster", "Tempo Change", ["tempo_change"]),
    ("844e8854-c0a5-5c9e-833e-39af1a595c15", "rall.", "Rallentando: Gradually getting slower", "Tempo Change", ["tempo_change"]),
    ("fb42a599-426f-5bde-b97c-35e84fbced38", "rit.", "Ritardando: Gradually getting slower", "Tempo Change", ["tempo_change"]),
    ("cf46f986-26ee-5d06-9af5-47f531fd3768", "riten.", "Ritenuto: Suddenly slower, held back", "Tempo Change", ["tempo_change"]),
    ("2a050663-312f-5d87-8bd5-a8dc714ffced", "A tempo", "Return to the original tempo", "Tempo Change", ["tempo_change"]),
    ("2483689c-bbc7-57ca-b239-e2b2138beb9e", "Rubato", "Flexible tempo, 'stolen' time", "Tempo Change", ["tempo_change"]),
    ("c3e0bd78-60b9-527c-84c7-d3edfc6de174", "Stringendo", "Pressing forward, getting faster", "Tempo Change", ["tempo_change"]),
    ("7ead6690-ba94-5e02-9db4-63b623376cf6", "pp", "Pianissimo: Very soft", "Dynamics", ["dynamics"]),
    ("1576a367-3942-5bc1-9714-047c7bba7536", "p", "Piano: Soft", "Dynamics", ["dynamics"]),
    ("908495f8-6aac-5547-8bc0-b4c363ae6ed9", "mp", "Mezzo-piano: Moderately soft", "Dynamics", ["dynamics"]),
    ("54bfb3c3-74f4-51f8-be1d-36502345f1b2", "mf", "Mezzo-forte: Moderately loud", "Dynamics", ["dynamics"]),
    ("5d656f7d-b2bb-553a-acfc-c4db4296fa3b", "f", "Forte: Loud", "Dynamics", ["dynamics"]),
    ("ee3c3fbb-c3d4-50d9-8f26-77bc2fb51b4f", "ff", "Fortissimo: Very loud", "Dynamics", ["dynamics"]),
    ("4bd07902-e545-51a5-a27b-af9d9ad09957", "sfz", "Sforzando: Suddenly loud, forced", "Dynamics", ["dynamics"]),
    ("8507ac5a-3668-5f09-bff2-9b5fcad8caed", SVG_CRESCENDO, "Crescendo: Gradually getting louder", "Dynamics", ["dynamics"]),
    ("12111dca-94d7-512d-9e0b-1b076de59d82", SVG_DECRESCENDO, "Decrescendo / Diminuendo: Gradually getting softer", "Dynamics", ["dynamics"]),
    ("4f38f85e-cfa9-58ca-b428-bdbb946bd9b0", "rfz", "Rinforzando: Suddenly reinforced", "Dynamics", ["dynamics"]),
    ("582c7cd2-ab4c-506c-8b35-4ef6b2dfbd46", ".", "Staccato: Short and detached (dot above/below note)", "Articulation", ["articulation"]),
    ("dea357ad-aeb3-59b9-bb47-803b72c1f1f9", "𝅘𝅥𝅾", "Staccatissimo: Very short and detached", "Articulation", ["articulation"]),
    ("0a975e55-41c3-5077-8713-1f8c637f8b67", SVG_SLUR, "Legato: Smooth and connected", "Articulation", ["articulation"]),
    ("e47d757c-51e4-596c-bf23-0f82818dee91", "-", "Tenuto: Held for its full value (line above/below note)", "Articulation", ["articulation"]),
    ("69e2fd43-bee1-5d36-936f-d7fb82de57ec", "^", "Marcato: Strongly accented", "Articulation", ["articulation"]),
    ("ce05c8bc-6447-5809-9601-633b8b303022", ">", "Accent: Emphasized", "Articulation", ["articulation"]),
    ("6d6a8ab8-e192-5a03-a574-873bfde5c2a0", "Portato", "Semi-staccato, pulses between notes", "Articulation", ["articulation"]),
    ("40468115-0eeb-5360-aefb-490b0cf25b27", "𝄞", "Treble Clef: G-clef, used for high pitches", "Symbol", ["symbol"]),
    ("13cc217c-bc6e-5cea-b83c-06f0795e0c91", "𝄢", "Bass Clef: F-clef, used for low pitches", "Symbol", ["symbol"]),
    ("e6ed116c-df3a-56f0-a2ab-1e4d718037f2", "𝄡 (on 3rd line)", "Alto Clef: C-clef centered on 3rd line", "Symbol", ["symbol"]),
    ("7d2fb29d-9729-5b41-ab87-0554964e53f9", "𝄡 (on 4th line)", "Tenor Clef: C-clef centered on 4th line", "Symbol", ["symbol"]),
    ("97595a84-97db-5c18-a16e-53b766e9a59f", "Grand Staff", "Treble and Bass staves joined by a brace", "Symbol", ["symbol"]),
    ("85cae761-d40b-5128-8fab-5b23b673544f", "Ledger Lines", "Short lines above/below the staff", "Symbol", ["symbol"]),
    ("8e12e0a5-0ca1-5f3c-bfac-a916b67f444b", SVG_BARLINE, "Bar Line: Vertical line dividing measures", "Symbol", ["symbol"]),
    ("f4272b47-3753-5886-b627-c18ccc9fa4eb", SVG_DOUBLE_BARLINE, "Double Bar Line: Two lines indicating a new section", "Symbol", ["symbol"]),
    ("283499f5-974d-5bcc-9e3a-236e58cc64d0", SVG_FINAL_BARLINE, "Final Bar Line: Indicates the end of the piece", "Symbol", ["symbol"]),
    ("cfa5922b-9ac9-509d-82a4-304bc15846e9", "𝄴", "Common Time: 4/4 time signature", "Rhythm", ["rhythm"]),
    ("cee24773-4f5b-5619-89a3-2c757208bf98", "𝄵", "Cut Time: 2/2 time signature", "Rhythm", ["rhythm"]),
    ("fcc07bda-2733-53d3-baaa-aefced23f8be", "Time Signature", "Tells beats per measure and beat value", "Rhythm", ["rhythm"]),
    ("e2599e68-aebf-5332-812f-11d6f34ce5aa", "Measure / Bar", "A segment of time defined by beats", "Rhythm", ["rhythm"]),
    ("2987ed94-399d-5606-8c46-497a5a33cdb0", SVG_TIE, "Tie: Connects two notes of the same pitch", "Rhythm", ["rhythm"]),
    ("0a975e55-41c3-5077-8713-1f8c637f8b67", SVG_SLUR, "Slur: Connects notes of different pitches", "Rhythm", ["rhythm"]),
    ("bad8de26-49b6-50e2-8bec-0c439db3389f", "Beam", "Connects stems of eighth/sixteenth notes", "Rhythm", ["rhythm"]),
    ("5ffdb3fb-5e50-5e5d-a95b-099c646c7765", "Dot (after note)", "Increases note value by half", "Rhythm", ["rhythm"]),
    ("1c0e4f93-1f9a-5003-8841-717f1bde1365", "Double Dot (after note)", "Increases note value by 3/4", "Rhythm", ["rhythm"]),
    ("2a5066f8-ff34-521b-b00d-b19e44b72f5d", "tr", "Trill: Rapid alternation between two notes", "Ornament", ["ornament"]),
    ("6230f423-8c6e-5e4f-ab95-fae464534340", "𝄗", "Mordent: Single alternation with note above", "Ornament", ["ornament"]),
    ("d01040b5-e533-5667-b191-e3d25ca6273f", "𝄘", "Inverted Mordent: Single alternation with note below", "Ornament", ["ornament"]),
    ("8d5d9677-a485-51b9-96c2-f69bbe1f0b22", "𝄑", "Turn: Note above, note, note below, note", "Ornament", ["ornament"]),
    ("dc930161-b13f-5f3a-98ed-9208c4239f7c", "𝄒", "Inverted Turn: Note below, note, note above, note", "Ornament", ["ornament"]),
    ("2455b9b1-2dde-51e7-80b4-bd56a891fc72", "Appoggiatura", "Leaning note (takes half the main note value)", "Ornament", ["ornament"]),
    ("cd89be6b-9947-5a86-862f-91b50bee3284", "Acciaccatura", "Grace note, 'crushed' note", "Ornament", ["ornament"]),
    ("f7e5fde7-648a-5501-a22e-f8718a3d3ac8", "Glissando", "Continuous slide between pitches", "Ornament", ["ornament"]),
    ("e57ecd3e-8086-5743-833c-08bdcf23ffc0", "D.C.", "Da Capo: From the beginning", "Form", ["form"]),
    ("19ed6638-a4c5-5202-a6c8-ec95e61e2c4d", "D.S.", "Dal Segno: From the sign", "Form", ["form"]),
    ("a98e9561-d1c4-5756-958c-005e6e0b50dc", "𝄋", "Segno: The sign used with D.S.", "Form", ["form"]),
    ("56d863f5-392c-5668-84d0-e64094cf793b", "𝄌", "Coda: Tail, closing section", "Form", ["form"]),
    ("023cf994-143c-5aff-9fef-8885c542bca4", "Fine", "The end", "Form", ["form"]),
    ("511f3bc3-e055-5ccb-91ae-41db2be05981", "𝄆 𝄇", "Repeat Sign: Repeat the music between the dots", "Form", ["form"]),
    ("53700c96-99c6-5fdb-be11-a3550883de20", "First Ending", "Play the first time through a repeat", "Form", ["form"]),
    ("4f4b493b-66e7-5a7f-8493-78ff96e9f256", "Second Ending", "Play the second time through a repeat", "Form", ["form"]),
    ("9d7b2fca-83c0-5e6b-88a8-f21d097ff26b", "Cantabile", "In a singing style", "Expression", ["expression"]),
    ("97c38e6c-b397-55db-9d4b-80cc062d2cc1", "Dolce", "Sweetly", "Expression", ["expression"]),
    ("2c7a8642-e752-552c-8398-9c1b06f05a60", "Espressivo", "Expressively", "Expression", ["expression"]),
    ("b47f4f0e-fb24-5029-8226-6dc64912979c", "Grazioso", "Gracefully", "Expression", ["expression"]),
    ("c72a0c06-acf9-5511-8d0e-443376cb636f", "Leggiero", "Lightly", "Expression", ["expression"]),
    ("38a0a137-e37b-5030-b9c6-f098c422afaa", "Maestoso", "Majestically", "Expression", ["expression"]),
    ("d9008abb-bb2c-5aba-be09-efca565b6e2a", "Molto", "Very, much", "Expression", ["expression"]),
    ("7d438f7b-96fe-5b20-a7bc-c884d35f1d0d", "Poco a poco", "Little by little", "Expression", ["expression"]),
    ("f76b8990-3fcd-59c7-815f-05be3a6548c0", "Sempre", "Always", "Expression", ["expression"]),
    ("f24bf8bc-6591-557c-8680-3e749b1f1091", "Subito", "Suddenly", "Expression", ["expression"]),
    ("ef73be5a-74c0-53c6-abb5-344ae91d95e3", "Agitato", "Agitated", "Expression", ["expression"]),
    ("b1fdac29-4f0a-5f63-93c5-0ca9b18ef01b", "Animato", "Animated", "Expression", ["expression"]),
    ("2c9e9849-9de7-513d-88ed-2618de7d22d7", "Brillante", "Brilliant", "Expression", ["expression"]),
    ("8deed60d-c000-581d-9782-a0031a6e4212", "Con brio", "With spirit/vigor", "Expression", ["expression"]),
    ("e97d125c-d40e-54eb-bdc3-c55288908752", "Con fuoco", "With fire", "Expression", ["expression"]),
    ("bf62c485-292e-5184-85f4-dbd0c0695143", "Morendo", "Dying away", "Expression", ["expression"]),
    ("799e152b-f3cc-5976-8199-a092f1e09a0d", "Pesante", "Heavy", "Expression", ["expression"]),
    ("9a7349c9-80d2-5780-8dd1-3012f8bc5f7b", "Scherzando", "Joking, playful", "Expression", ["expression"]),
    ("ffb27646-c65d-58c9-9f28-3c8d387d8bab", "Sotto voce", "In an undertone, quiet", "Expression", ["expression"]),
    ("e5966d69-05d2-500d-a85c-f21968a540dc", "Tranquillo", "Tranquil", "Expression", ["expression"]),
    ("c7e5b963-559c-57cf-8506-3b92f2a408e8", "8va", "Octave: Play an octave higher", "Other", ["other"]),
    ("09a2c67b-2f32-5216-b816-2ee9a53e5417", "8vb", "Octave below: Play an octave lower", "Other", ["other"]),
    ("7b602378-904f-508f-a689-e052799bdf4a", "Con sordino", "With mute", "Other", ["other"]),
    ("17f936c3-947a-54f0-9c2c-32dc967cff8e", "Senza sordino", "Without mute", "Other", ["other"]),
    ("24ba2a7b-5d08-5f0f-8fcd-df2cf08f9142", SVG_ARPEGGIO, "Arpeggio: Notes of a chord played in succession", "Other", ["other"]),
    ("d07c8331-6850-5a7c-b724-2709bc9429b5", "𝄐", "Fermata: Hold the note longer than indicated", "Other", ["other"]),
    ("39e8f21a-49c1-5564-908e-215b5accaaea", "G.P.", "Grand Pause: Entire ensemble pauses", "Other", ["other"]),
    ("b9b2a46b-9a6b-5ac9-a8fc-35f7f571c271", "//", "Caesura: A pause or break in music", "Other", ["other"]),
    ("fd9fb649-05e9-5750-adf2-e6459eb64d7b", "Simile", "Continue in a similar manner", "Other", ["other"]),
    ("119d5d85-021f-5748-be44-2808cd48bfe5", "Allargando", "Broadening, getting slower and louder", "Tempo", ["tempo"]),
    ("efa2832a-2780-5ef0-9842-b2f108e89c1f", "Giocoso", "Joyful, merry", "Expression", ["expression"]),
    ("fa746066-0aa8-5eb7-8e7d-6992601ba92e", "Meno Mosso", "Less motion (slower)", "Tempo Change", ["tempo_change"]),
    ("280ccf9d-e190-57a0-a412-5edae6d073a6", "Più Mosso", "More motion (faster)", "Tempo Change", ["tempo_change"]),
    ("1a04f53a-2d86-5711-9cb2-ce77a891dcb6", "Agnus Dei", "Lamb of God (often used in Requiem/Mass)", "Term", ["term"]),
    ("c9ad2e1e-57b3-5278-ba59-7bf850add1d0", "Cadenza", "Ornamental passage for a soloist", "Form", ["form"]),
    ("67a7d862-b5fe-5d99-ba7f-c9189e677463", "Concerto", "Work for soloist and orchestra", "Form", ["form"]),
    ("a085d905-264a-54c2-bb5b-bd57df758a74", "Symphony", "Large work for orchestra", "Form", ["form"]),
    ("98955af0-713a-5368-9a2a-7a85acec93de", "Libretto", "The text of an opera", "Term", ["term"]),
    ("f74433b2-b51a-5b12-a53d-e9956edfacff", "Vibrato", "Small fluctuation in pitch", "Expression", ["expression"]),
    ("8dc42a61-e57c-5f8a-a9d0-cf24401894fe", "Enharmonic", "Notes that sound the same but have different names (e.g., C# and Db)", "Term", ["term"]),
    ("542fb67a-87ba-58b1-afbb-1bbad194e872", "Diatonic", "Belonging to the current scale or key", "Term", ["term"]),
    ("a8ef03e2-3d45-5ab9-8430-b8e1c1fbf9cc", "Chromatic", "Using notes outside the current scale/key", "Term", ["term"]),
    ("eba82659-06bf-57ef-bf76-c0280db2deb8", "Syncopation", "Emphasizing the weak beats or off-beats", "Rhythm", ["rhythm"]),
    ("6d47177e-2298-5fc6-b647-82b6da75ef4f", "Transposition", "Shifting music to a different pitch level", "Term", ["term"]),
    ("215f53fd-67b6-55b8-9c5c-ac54dd30e680", "Modulation", "Changing from one key to another", "Term", ["term"]),
    ("bfbf1328-8884-539b-9583-4c4df5b38533", "Relative Key", "Major and minor keys that share the same key signature", "Term", ["term"]),
    ("61bafbe5-339f-5c9e-accd-0a4ff86a9519", "Parallel Key", "Major and minor keys that share the same tonic", "Term", ["term"]),
    ("9f7f0044-bc99-5b7d-902b-cfc34c923448", "Alberti Bass", "A broken chord accompaniment pattern", "Expression", ["expression"]),
    ("f72cf92d-2976-54c0-99ba-0a62192d8b4f", "Ostinato", "A continually repeated musical phrase or rhythm", "Form", ["form"]),
    ("445c55d2-68be-541d-a576-a45ca3703b19", "Sequence", "Restatement of a motif at a higher or lower pitch", "Form", ["form"]),
    ("fe75373c-5ff5-5493-9512-f3948fe0e38f", "Inversion", "Turning a melody or chord upside down", "Term", ["term"]),
    ("f1c109c0-328f-599c-861f-e0079c1ac384", "Cadence", "A melodic or harmonic configuration that creates a sense of resolution", "Form", ["form"]),
    ("9f9c4968-17c6-51d5-8dae-b1055611c42c", "Picardy Third", "Ending a minor-key piece with a major chord", "Term", ["term"]),
    ("644c3089-acb6-5b80-b1d5-1ad945ac79f4", "Motif", "A short musical idea or fragment", "Form", ["form"]),
    ("7c81f975-0acf-5949-b5da-8dffd526350c", "Theme", "A complete musical thought used as a building block", "Form", ["form"]),
    ("c3dfb52f-5dbb-567a-aa70-24b26d8a5419", "Counterpoint", "The relationship between independent melodic lines", "Form", ["form"]),
    ("1728c28c-c4dd-570f-b4ee-a96589a4e277", "Fugue", "A contrapuntal composition based on a main theme (subject)", "Form", ["form"]),
    ("d620d6cb-a972-5921-b141-cc4ba7082f95", "Suite", "A collection of short musical pieces", "Form", ["form"]),
    ("0af7e583-a5c8-5c96-9729-194328ef2120", "Overture", "An introductory piece to an opera or larger work", "Form", ["form"]),
    ("77ae1737-570d-53d1-a425-1a201ed8ac8b", "Oratorio", "A large-scale musical work for orchestra and voices, usually on a religious theme", "Form", ["form"]),
    ("a32b7dea-4d65-5d4a-8101-4434ab7b0590", "Aria", "A self-contained piece for a single voice, usually in an opera", "Form", ["form"]),
    ("da795800-632a-59e8-9f06-0785b3f4594d", "Recitative", "A style of delivery in which a singer is allowed to adopt the rhythms of ordinary speech", "Form", ["form"]),
    ("5594993d-9246-51f2-b10b-e532a6aa4978", "Chorus", "A large group of singers", "Term", ["term"]),
    ("f7e00f7b-1bd7-51ed-85d2-9d3371774f91", "Timbre", "The quality or 'color' of a sound", "Expression", ["expression"]),
    ("766cff11-cf70-5073-b392-c1ef4c9248e5", "Texture", "How melodic, rhythmic, and harmonic materials are combined", "Term", ["term"]),
    ("5154a34b-a98d-548f-878b-5d8e20471cd4", "Monophony", "A single melodic line without accompaniment", "Term", ["term"]),
    ("5bcf3b81-b80f-51d2-afc2-b0b83fa351ee", "Polyphony", "Multiple independent melodic lines", "Term", ["term"]),
    ("237f3e40-e592-501d-a4a2-601a6e884270", "Homophony", "A primary melody with chordal accompaniment", "Term", ["term"]),
    ("19d13780-b8fa-5c60-8a59-0d0d38901a95", "Heterophony", "Multiple versions of the same melody played simultaneously", "Term", ["term"]),
    ("654e6f09-40bd-5a3e-bd9a-da693ee1dd8c", "Consonance", "Stable, pleasant-sounding intervals or chords", "Expression", ["expression"]),
    ("60a155b3-b32a-54db-abf2-c64b833846c1", "Dissonance", "Unstable, harsh-sounding intervals or chords", "Expression", ["expression"]),
    ("4739ba53-3b29-5352-91ff-22b06880eb93", "Resolution", "Movement from dissonance to consonance", "Expression", ["expression"]),
    ("40701154-4d36-56b5-a7ac-0be8fed5d90a", "Atonality", "Absence of a tonal center or key", "Term", ["term"]),
    ("352aacd6-5add-5d40-bc37-ebaf77941c1d", "Bitonality", "Use of two different keys simultaneously", "Term", ["term"]),
    ("1ed719f5-c893-533c-a983-5234ab593ab7", "Polytonality", "Use of multiple keys simultaneously", "Term", ["term"]),
    ("e570a192-d2ed-5652-8fcd-b4c917e7786b", "Microtonality", "Use of intervals smaller than a semitone", "Term", ["term"]),
    ("afa1b390-0d7f-5747-9a40-0581a0f28c96", "Pentatonic Scale", "A five-note scale", "Term", ["term"]),
    ("efcea7dc-0287-589b-b3f5-a059ba7cba6e", "Whole Tone Scale", "A scale consisting entirely of whole steps", "Term", ["term"]),
    ("7fb5670d-658b-58ad-ba26-a84812c99f16", "Chromatic Scale", "A scale consisting entirely of half steps", "Term", ["term"]),
    ("390dbc7c-90ae-5d91-b2d8-141e13e828f9", "Octatonic Scale", "An eight-note scale alternating whole and half steps", "Term", ["term"]),
    ("3f857ac3-47ff-532f-b1c5-1421c562662a", "♯", "Sharp: Raises a note by a half step", "Symbol", ["symbol"]),
    ("11d395e7-5bfe-5fcb-a209-908b40f5805f", "♭", "Flat: Lowers a note by a half step", "Symbol", ["symbol"]),
    ("f31fb3cf-0a98-5cf5-941d-dd912752fcd2", "♮", "Natural: Cancels a previous sharp or flat", "Symbol", ["symbol"]),
    ("87ac8f68-f015-58ed-9614-86e08113ac29", "𝄪", "Double Sharp: Raises a note by a whole step", "Symbol", ["symbol"]),
    ("df3d330c-39f3-572a-8d02-b0d860006815", "𝄫", "Double Flat: Lowers a note by a whole step", "Symbol", ["symbol"]),
    ("01915202-1121-5610-8125-8cf5c8ecaf67", "Major Second", "An interval of 2 semitones (e.g., C to D)", "Interval", ["interval"]),
    ("bd25baa6-b59e-5e8b-9e06-1bea368433fc", "Minor Second", "An interval of 1 semitone (e.g., C to Db)", "Interval", ["interval"]),
    ("bada120e-9fb5-5c3c-8440-89cd2e3218ec", "Major Third", "An interval of 4 semitones (e.g., C to E)", "Interval", ["interval"]),
    ("975becf1-f6a8-55c2-b6fb-54dfbb44be74", "Minor Third", "An interval of 3 semitones (e.g., C to Eb)", "Interval", ["interval"]),
    ("e3a55620-cd67-5b24-a01f-15c61b674267", "Perfect Fourth", "An interval of 5 semitones (e.g., C to F)", "Interval", ["interval"]),
    ("ec23429b-a0e0-5caa-8ea9-252884aea175", "Tritone", "An interval of 6 semitones (Augmented 4th / Diminished 5th)", "Interval", ["interval"]),
    ("2a663145-50e8-5e9e-ab6e-5a797d36918f", "Perfect Fifth", "An interval of 7 semitones (e.g., C to G)", "Interval", ["interval"]),
    ("cbe90e1c-74d0-5e11-98f8-34c13b9cc346", "Major Sixth", "An interval of 9 semitones (e.g., C to A)", "Interval", ["interval"]),
    ("1d2fc571-1ddb-5f52-834c-1136f1d3791c", "Minor Sixth", "An interval of 8 semitones (e.g., C to Ab)", "Interval", ["interval"]),
    ("fee773a3-0475-5676-a585-a19377dd4e15", "Major Seventh", "An interval of 11 semitones (e.g., C to B)", "Interval", ["interval"]),
    ("d3df7588-cb78-5d7c-8f11-a88908e1145b", "Minor Seventh", "An interval of 10 semitones (e.g., C to Bb)", "Interval", ["interval"]),
    ("bc7e248f-42f0-5a4d-aa91-7dbd2f80bca7", "Perfect Octave", "An interval of 12 semitones (e.g., C to C)", "Interval", ["interval"])
]

notes = []
for note_uuid, front, back, category, tags in cards_data:
    # Using hardcoded UUIDs for true stability
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
