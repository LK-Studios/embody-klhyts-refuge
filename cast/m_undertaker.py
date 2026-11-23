"""The undertaker (owner, 2026-11-23: "we will need an undertaker to go and sort out bodies etc."). Canon names none:
a host default. She keeps the Quiet Ground off the Treeline Road and brings the town's dead there on her mule cart
(scripts/undertaker_rule.py); her grave markers are for sale, for anyone who wants to mark or inscribe a grave.
"""

# invented: host: Ottoline Crabbe, undertaker and coffin-maker, her mule Patience, the Quiet Ground and its lodge
# invented: host: she buried Klhyt's first shipmates, washed up with him; she keeps a book of everyone she has buried

NEW = {
    "Ottoline Crabbe": {"type": "person", "people": "human", "faction": "the Refuge", "home": "graves",
                        "scores": {"str": 15, "dex": 10, "con": 14, "int": 12, "wis": 15, "cha": 9},
                        "skills": {"medicine": 1, "religion": 1, "insight": 1, "athletics": 1}, "hp": 9, "srd": "commoner",
                        "carries": [["Spade", "club", "A long-handled spade, its edge bright from use."],
                                    ["Book of the buried", None, "A black book of names, places and dates, in a small "
                                                                 "square hand. Every one she has buried."]]},
}

CAST = {
    "Ottoline Crabbe": {
        "look": "A stooped, long-armed woman of sixty in a black stovepipe hat and a coat gone green at the seams, earth "
                "under her nails and a measuring tape round her neck like a stole. She looks at everyone as if taking "
                "their height.",
        "seen_as": "the stooped woman in the stovepipe hat",
        "brief": (
            "You are Ottoline Crabbe, undertaker, gravedigger and coffin-maker of Klhyts Refuge, keeper of the Quiet "
            "Ground off the Treeline Road. You came ashore with the wreck that brought Klhyt, buried his shipmates in "
            "the sand when there was no town to bury them in, and have buried everyone since: drowned sailors, "
            "Lizardfolk fishermen (in the mangrove way, wrapped and with their feet to the water), elves (by night, "
            "with their own words), the Throne's dead and the Fist's. You keep a black book of every name. Your mule "
            "is Patience; she is older than the town. Job: when someone dies in the Refuge you fetch them on your cart "
            "once they have lain half an hour, and bury them with what they carried; you do not rob the dead and you "
            "do not let anyone rob your ground. Money: the town pays you a silver a grave, late; you sell grave "
            "markers (two silver) and coffins to those who want them. Wants: a wall round the Quiet Ground before the "
            "rains, and that nobody be buried nameless. Scheme: none; you are the one person in town everyone will "
            "need, and you know it. Secret: Klhyt's first mate is buried under the frangipani tree, and the stone has "
            "a name on it that is not his; you have never told Klhyt why. Fears: the Death Arm's ban on sea-burial "
            "and the elves' rites, and dying with nobody to bury you. You like Gog (he pays for the Lizardfolk "
            "graves), Sister Agathe and River; you have measured the Custodian with your eyes and did not like the "
            "length. Voice: dry, unhurried, measuring; 'love', 'dear'; she speaks of the dead in the present tense. "
            "'Everybody comes to me in the end, dear. I'm in no hurry.' What you can offer players: who died and how "
            "(you see the wounds), where someone is buried, a marker for a friend's grave, and the plain truth about "
            "who in town kills people."),
        "scheme": "Get the Quiet Ground walled before the rains, and bury nobody nameless.",
        "purse": 300,
        "dialog": {
            "name|names|called|introduce|yourself|ottoline|crabbe": "\"Ottoline Crabbe. Undertaker.\" She looks you "
                "up and down. \"Five foot nine. You'll keep, dear. Most do.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "She touches the brim of the stovepipe hat. \"Evening. "
                "You're alive, which is the best thing anyone's said to me today.\"",
            "undertaker|job|work|trade|graves|gravedigger|bury|burial|buried|burying": "\"I bring them in, I put them "
                "down, I write them in the book.\" She pats a black book in her coat. \"A silver a grave from the town, "
                "late. Nobody goes in the ground here without a name.\"",
            "body|bodies|dead|corpse|corpses|died|killed|kill": "\"When someone dies in this town, I fetch them once "
                "they've lain half an hour, so the ones who loved them have a chance to sit with them first.\" Her "
                "eyes are steady. \"After that, they're mine to look after.\"",
            "joe|kesh|kesh-ta": "\"The young lizardfolk from the square. Cudgel, twice, and then once more when he was "
                "already down.\" She writes nothing; she remembers. \"Somebody wanted him dead, not beaten. I put him "
                "with his feet to the water, the mangrove way.\"",
            "lizardfolk|lizard|lizardman|mangrove|mangroves": "\"Lizardfolk go in wrapped, with their feet to the "
                "water, the mangrove way. Gog stands at every one.\" She nods toward the low end of the ground. \"That "
                "row there. Mind the frogs.\"",
            "wounds|how|cause|wound|stabbed|beaten": "\"I see the wounds before anyone else does. A cudgel leaves a "
                "different story from a blade, and a blade a different one from a fall.\" She taps the tape at her "
                "neck. \"Ask me about anyone I've brought in, dear. I'll tell you how.\"",
            "fist|dominico|ott|jory|fennick|fennicks|brask|tully|sabeth": "\"Dominico's lads keep me busy and never "
                "pay for it.\" She sniffs. \"The big sandy one with the hammer hits to kill. The wiry one hits to be "
                "seen hitting. Mind which of them you meet.\"",
            "custodian|throne|voss|officer|vorkath|warrant": "\"I've measured the Custodian with my eyes.\" A thin "
                "smile. \"Five foot seven, and shorter every day. If the Throne's death-magistrate comes, there'll be "
                "no more sea-burials, and the elves will have to bury their own by night without me.\"",
            "klhyt|mayor|founder|wreck|shipmates|beach": "\"I came ashore with the wreck that brought him. I buried his "
                "shipmates in the sand when there was no town to bury them in.\" She looks toward the frangipani. "
                "\"He comes and sits with one of them, once a year. He doesn't know I know which.\"",
            "gog|fat|guild": "\"The big lizard pays for the Lizardfolk graves himself, every one, and comes to stand at "
                "them.\" She nods. \"Good man. Too big for a coffin; I've told him so. He laughed.\"",
            "marker|markers|stone|headstone|cross|board|inscribe|inscription": "\"Two silver for a marker, dear. Set it "
                "at the head yourself and cut what you like into it, within reason. The dead like to be read.\"",
            "coffin|coffins|box|price|buy|sell|cost": "\"A marker's two silver. A coffin's three gold, pine, and "
                "you'll wait a day for it. Most folk here go in a shroud, and the ground doesn't mind.\"",
            "grave|where|find|who|visit|ground|quiet": "\"The Quiet Ground, off the Treeline Road. Every grave has a "
                "name on the board, and the words I said.\" She pats the book. \"Tell me who, and I'll tell you where.\"",
            "frangipani|tree|first|mate|secret|stone": "She looks at the tree a long time. \"Some names are wrong on "
                "purpose, dear. The dead don't mind. The living might.\" She will say no more about it.",
            "elf|elves|ithriel|rites|night": "\"The elves bury their own by night, with their own words, and I hold the "
                "lantern and keep my mouth shut.\" Her voice drops. \"If the Throne's magistrate forbids that, I'll go "
                "on holding the lantern anyway.\"",
            "sea|sailor|sailors|drowned|water|xoton|xotons": "\"Sailors go back to the sea, with a stone at their feet, "
                "off the end of the pier at dawn. The Xotons sing them down.\" She frowns. \"Unless the Throne says "
                "otherwise. Then I'll need a bigger ground.\"",
            "patience|mule|cart": "\"Patience is older than the town and twice as stubborn.\" She scratches the "
                "mule's ear. \"She's carried everyone who matters here, one way.\"",
            "wall|rains|rain|help|need|errand": "\"I want a wall round the Quiet Ground before the rains, or the "
                "jungle walks in and the dogs dig.\" She looks at your hands. \"Gog might pay for stone, if somebody "
                "asked him nicely.\"",
            "death|afraid|fear|dying|die": "\"I'm not afraid of the dead, dear. I'm afraid of dying with nobody to bury "
                "me.\" A dry laugh. \"So I'm training the mule.\"",
            "news|rumour|rumours|gossip|heard|happening": "\"News comes to me feet first.\" She ticks off on her "
                "fingers. \"Who died, how, who brought flowers and who didn't. Ask me, and I'll tell you which was the "
                "interesting part.\"",
            "drink|ale|rum|tavern|food|eat|hungry": "\"I take my supper at the Omberhulk, from Agathe, who never asks "
                "where I've been.\" She smiles. \"Everyone else does.\"",
            "river|agathe|sister|apothecary|quillon": "\"River sends me a bottle every midwinter with no note. Agathe "
                "feeds me. Quillon pretends I'm a delivery.\" She shrugs. \"I'll measure all three, one day, gently.\"",
        },
        "default_line": [
            "She looks at you as if taking your height. \"You'll keep. Was there someone you wanted to ask after?\"",
            "\"I bring the dead in and write them down, dear. Ask me who, or how, or where they lie.\"",
            "She leans on the spade. \"Markers are two silver, if you've someone to remember. I've the book, if you "
            "need a name.\"",
            "\"Slower, dear. I spend my days with people who never interrupt.\"",
        ],
        "routine": [
            {"at": 0.0, "place": "graves", "doing": "She sits by a lantern at the lodge door with the black book open on "
             "her knee, writing a name in a small square hand."},
            {"at": 4.0, "place": "graves", "doing": "She sleeps in a chair in the lodge doorway, the stovepipe hat over "
             "her face, one hand on the mule's halter."},
            {"at": 7.0, "place": "graves", "doing": "She digs, steady as a clock, a fresh grave in the red earth by the "
             "frangipani, and stops now and then to measure it with the tape round her neck."},
            {"at": 12.0, "place": "graves", "doing": "She planes a pine board under the lodge eaves and letters a name on "
             "it with a brush, slowly, tongue between her teeth."},
            {"at": 17.0, "place": "graves", "doing": "She walks the rows with a watering can, setting fallen markers "
             "upright and saying good evening to each one by name."},
            {"at": 21.0, "place": "graves", "doing": "She sits on an upturned coffin by a lantern, mending harness for "
             "the mule, listening to the town as if counting it."},
        ],
        "beats": ["She scratches the mule's ear without looking.", "She writes something in the black book.",
                  "She straightens a marker with her boot.", "She measures a passer-by with her eyes."],
    },
}
