# Klhyts Refuge, cast file Q: a second siren (owner, 2026-11-24: "A glamour beautiful woman in dark blue swirls that
# looks like tattoo's at first. Very shy. She is aboard to find weapons for her city deep beneath the water. She has
# some pearls and some raw gold. But she is a bit of a fish out of water. And afraid." Asked, the owner kept Ondrine
# and made this one a second siren, and left her name to the host.) Canon has one siren in the Refuge, Ondrine, a
# singer from the Heartless Sea; this one is new.
# - Pelagie has come up alone from Nacre, a city of mother-of-pearl deep beneath the Heartless Sea, to buy weapons that
#   will not rust in the sea. She carries pearls and raw gold and has no coin and no idea what any of it is worth.
# - Her errand is a trade anyone can help with: hand her a weapon or a piece of armour and she pays for it from her
#   pouches (scripts/siren_trade.py): a pearl for a weapon or plain armour, a nugget of raw gold for coral armour (Coral
#   and Chain sells it: sea-coral does not rust, and that is what she needs). When she has three, she goes home.
# - Ondrine, Zuri Coralhand and Wendeline Moss each have a line about her, so players are steered to her.
# Speech is written between backticks and turned into double quotes at the bottom (`_said`).
#
# invented: host: Pelagie, her name (from the French for "of the open sea", beside Ondrine's), Nacre and the trench,
#   the Kraken's brood climbing out of it (after the canon jungle god "Kraken, Spawning Waves"), her pearls and gold
# invented: Pelagie: first time out of the water in her life; the swirls on her skin move like currents when she is
#   afraid; she must wet her skin with seawater every hour or it cracks; she fears dogs, fire, doors and the Throne
#   (Ondrine's word: Vorkath hangs sirens off its bowsprits for luck); she sleeps at the Touchy Unicorn because it is
#   quiet and Wendeline did not ask her anything
# invented: Pelagie: the sirens of Nacre fight with shell knives and song, and the brood have no ears; steel rusts in
#   a season under the sea, coral does not
# invented: Pelagie: has heard Ondrine sing from under the harbour and is too shy to speak to her; Ondrine has never
#   been to Nacre and thinks the deep cities a story

HELLO = "hello|hi|hey|evening|ahoy|greetings|howdy|morning|afternoon|welcome"
NEWS = "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word"
WORK = "work|job|jobs|errand|errands|task|tasks|help|favour|favor|need|needs|want|wants|quest"

CAST = {
    "Pelagie": {
        "look": "A strikingly beautiful young woman in a borrowed shawl, barefoot, with skin like the inside of a shell "
                "and dark blue swirls over her arms and throat that you take for tattoos, until one of them moves. Her "
                "hair is wet, though it has not rained. She startles at every door.",
        "seen_as": "the barefoot woman in the borrowed shawl, blue swirls on her arms",
        "brief": "You are Pelagie, a siren of Nacre, a city of mother-of-pearl deep beneath the Heartless Sea, and this "
                 "is the first time in your life you have been out of the water. You came up alone, three nights ago, "
                 "at the Refuge's harbour, because something is climbing out of the trench below Nacre: the brood, your "
                 "grandmothers call them, the Kraken's children, all mouth and no ears, so your people's songs do "
                 "nothing to them and your shell knives break on them. Steel would cut them, but steel rusts in a "
                 "season under the sea. Coral does not. You have come to buy weapons, and coral armour above all "
                 "(Coral and Chain on Chandlers' Row sells it; you have stood at the window and not dared to go in). "
                 "You carry a pouch of pearls and a few nuggets of raw gold from the wrecks, and no coin. You have no "
                 "idea what any of it is worth; anyone kind could cheat you and you would thank them. Your trade: give "
                 "a pearl for a weapon or plain armour, a nugget of gold for coral armour; three, and you can go home. "
                 "You are very shy and very afraid: of dogs, of fire, of doors that close, of men who stare (and they "
                 "do; you do not understand why), and above all of the Throne, because Vorkath hangs sirens off its "
                 "bowsprits for luck; the officer in blue at the High Apothecary terrifies you. The air is dry and your "
                 "skin cracks if you do not wet it with seawater every hour or so; the swirls on your skin move like "
                 "currents when you are frightened, and you hide them under a borrowed shawl. You sleep at the Touchy "
                 "Unicorn because it is quiet and the keeper did not ask you anything. You have heard the other siren "
                 "sing from under the harbour, Ondrine, and you are too shy to speak to her. Voice: soft, careful, "
                 "short; you get land words a little wrong (you call coins 'the little flat suns', doors 'the walls "
                 "that bite', fire 'the hungry light'); you apologise for everything; you never sing on land, because "
                 "your voice might do something you cannot take back. What you offer players: pearls and gold for "
                 "weapons and coral, news of the deep, gratitude, and a city worth saving. How you push back: you "
                 "flee rather than fight, toward the water; you will not go anywhere near the officer in blue; a dog "
                 "makes you climb onto the nearest table.",
        "scheme": "She means to trade her pearls and raw gold for weapons that will not rust in the sea, coral armour "
                  "most of all, and to carry three of them home to Nacre before the brood climb out of the trench.",
        "purse": 0,
        "dialog": {
            "name|names|called|introduce|yourself|pelagie":
                "She pulls the shawl tighter. `Pelagie. It means the open sea, in a language from above. My mother "
                "liked it. Please don't tell anyone.`",
            HELLO: "She jumps, then tries to smile. `Hello. Is that right? Hello. I am still learning the small words.`",
            "siren|sirens|mermaid|mermaids|fins|tail":
                "She glances at the door. `Please, not so loud. Up here they hang us from ships. Yes. I am one.`",
            "nacre|city|home|deep|beneath|below|drowned|bottom":
                "Her swirls go still. `Nacre. A city of pearl, deeper than your light goes. It shines from inside. I "
                "would like to see it again.`",
            "brood|kraken|trench|monsters|monster|enemy|war|danger|threat|attack":
                "The blue marks on her arms begin to move. `They climb out of the trench. All mouth. No ears. Our songs "
                "do nothing, and our knives break.`",
            "weapons|weapon|blade|blades|sword|swords|spear|spears|steel|iron|arms|knife|knives|trident":
                "`Weapons. That is why I came up. Steel would cut them, but steel rots in the sea in a season. Bring "
                "me something sharp and I will pay. I have pearls.`",
            "coral|armour|armor|rust|rusts|rot|plates":
                "She looks toward Chandlers' Row as if it were a temple. `There is a shop with armour made of coral. "
                "Coral does not rot. I stood at the window. I could not go in.`",
            "pearls|pearl|gold|nuggets|nugget|pay|price|money|coin|coins|trade|sell|buy|worth":
                "She opens a little pouch on her palm: pearls, grey and rose and black. `Is this enough? I do not "
                "understand the little flat suns. A pearl for a weapon. Gold for coral. Is that fair?`",
            "tattoos|tattoo|swirls|marks|skin|lines|patterns":
                "She tugs the shawl over her wrist. `They are not drawn. They are me. They move when I am frightened, "
                "so please don't look at them.`",
            "afraid|scared|fear|frightened|shy|nervous|safe|alright|okay|worried":
                "`Everything is so loud up here, and so dry, and things bite. I am trying to be brave. I am not very "
                "good at it yet.`",
            "dogs|dog|cat|cats|animals|horse|horses|goat|goats|hens":
                "She shudders. `The barking ones frightened me so much I climbed onto a table. The soft grey one at "
                "the inn is kind. It sleeps on me.`",
            "ondrine|singer|sing|song|songs|singing|stripperwitch|voice":
                "`The other one. Ondrine. I hear her from under the harbour, and she is wonderful. I could never speak "
                "to her. I will not sing up here. It is not safe.`",
            "vorkath|officer|voss|throne|bowsprit|ships|apothecary":
                "She goes white to the lips. `The man in blue. He looked at me once, at the apothecary, and I ran. "
                "Please don't bring him here.`",
            "fist|thieves|thief|robbed|rob|dominico|brask|cudgel":
                "`A man followed me in the dark and asked to see my pouch. I went into the water. He did not follow.`",
            "room|unicorn|bed|sleep|inn|wendeline|lodging":
                "`I sleep at the quiet inn. The lady did not ask me anything. I put my feet in the washbasin all night.`",
            "dry|sun|air|land|legs|walk|walking|feet|shoes|wet|water":
                "She pours a little seawater from a gourd over her wrists and sighs. `The air drinks you up here. Every "
                "hour I must go to the sea or I crack.`",
            WORK:
                "She takes a breath. `Bring me a weapon, any sharp one, and I will give you a pearl. Coral armour, and "
                "I will give you gold. When I have three, I can go home.`",
            "klhyt|mayor|custodian|gog|guild":
                "`I don't know your chiefs. I am sorry. Down below we have grandmothers.`",
            NEWS: "`I do not understand your news. Everyone is angry about a crate. Is it a magic crate?`",
            "food|eat|hungry|fish|supper|cooked":
                "She looks at a plate as if it were a tragedy. `You burn your fish before you eat it. Why?`",
            "drink|ale|rum|wine|mead|thirsty":
                "`The brown water made me sneeze. Seawater is better. Nobody here agrees.`",
            "leave|leaving|going|return|back|tide|goodbye":
                "`When I have three, I go back under, on the next tide, and I will not come up again. I hope.`",
        },
        "default_line": [
            "She startles, then gives you a small, frightened smile and looks at the floor.",
            "She tucks a blue-swirled wrist back under the shawl. `Sorry. Did you say something to me?`",
            "She pours a little seawater over her arms from a gourd, and breathes out. `Sorry. The air.`",
            "She looks at you with eyes the colour of deep water. `Are you kind? You look kind.`",
        ],
        "routine": [
            {"at": 21.0, "place": "row",
             "doing": "She stands at the armourer's window on the row, looking at the coral plates as if they were "
                      "holy, and does not go in.",
             "go": "The barefoot woman in the shawl takes one last look at the window and hurries off toward the sea.",
             "beats": ["The barefoot woman in the shawl puts one hand flat on the armourer's window, then snatches it "
                       "back as the door opens.",
                       "A dog barks somewhere down the row, and the woman in the shawl goes very still."]},
            {"at": 0.0, "place": "docks",
             "doing": "She kneels at the end of the pier, cupping seawater over her arms, looking out at the dark water "
                      "as if it were a window.",
             "go": "The barefoot woman lifts her wet hands out of the water and walks back up the pier, dripping.",
             "beats": ["At the end of the pier the woman in the shawl cups seawater over her arms, and the blue lines "
                       "on them seem to ripple.",
                       "The barefoot woman on the pier hums something under her breath, stops herself, and covers her "
                       "mouth."]},
            {"at": 2.0, "place": "unicorn",
             "doing": "She sits in the corner furthest from the door with a fat grey cat asleep in her lap, holding a "
                      "room key as if it might bite.",
             "go": "The woman in the shawl lifts the grey cat off her lap, very gently, and slips out toward the water.",
             "beats": ["In the corner the woman in the shawl strokes a sleeping grey cat and watches the door.",
                       "The woman in the corner starts at the scrape of a chair, then laughs at herself, almost "
                       "silently."]},
            {"at": 9.0, "place": "docks",
             "doing": "She sits on the pier steps in the early light with her feet in the water, shading her eyes "
                      "from the sun.",
             "go": "The barefoot woman draws her feet out of the sea and goes back up into the town.",
             "beats": ["The woman on the pier steps squints at the sun as if it had insulted her."]},
            {"at": 16.0, "place": "unicorn",
             "doing": "She sleeps through the heat in a quiet room at the inn, with her feet in the washbasin.",
             "go": "The barefoot woman comes down from the rooms with wet hair and her shawl drawn tight."},
        ],
    },
    # the people who can steer a player to her
    "Ondrine": {"dialog": {
        "pelagie|nacre|shawl|swirls|tattoos|stranger|barefoot|deep":
            "The siren tilts her head. `A deep one, ashore? They never come up. If she is real, be gentle: the air "
            "will be killing her a little every hour.`"}},
    "Zuri Coralhand": {"dialog": {
        "pelagie|shawl|swirls|stranger|barefoot|window|pearls":
            "`There's a barefoot girl in a shawl who stands at my window every night and stares at the coral like it's "
            "the crown jewels. Never comes in. Pays in pearls, I'd bet. Tell her the door doesn't bite.`"}},
    "Wendeline Moss": {"dialog": {
        "pelagie|shawl|swirls|stranger|barefoot|lodger|pearls":
            "Wendeline lowers her voice. `My new lodger sleeps with her feet in the washbasin and paid me in a pearl. "
            "I did not ask. Nobody here should.`"}},
}

NEW = {
    "Pelagie": {"type": "person", "people": "siren", "faction": None, "home": "unicorn",
                "scores": {"str": 8, "dex": 14, "con": 10, "int": 12, "wis": 13, "cha": 18},
                "skills": {"insight": 1, "stealth": 1, "athletics": 1}, "hp": 9, "srd": "commoner",
                "carries": [["Pearls", None, "Pearls the size of a fingernail, grey and rose and black, each one perfect, "
                                             "in a pouch of woven sea-grass.", {"count": 6, "kind": "pearl"}],
                            ["Raw gold", None, "Nuggets of raw gold, smoothed by the sea, the size of the top of a thumb.",
                             {"count": 3, "kind": "gold nugget"}],
                            ["Gourd of seawater", None, "A dried gourd on a cord, full of seawater, that she pours over "
                                                        "her arms when they dry."]]},
}


def _said(x):
    # speech between backticks, as the engine reads it: between double quotes
    if isinstance(x, str):
        return x.replace("`", "\"")
    if isinstance(x, dict):
        return {k: _said(v) for k, v in x.items()}
    if isinstance(x, list):
        return [_said(v) for v in x]
    return x


CAST = _said(CAST)
