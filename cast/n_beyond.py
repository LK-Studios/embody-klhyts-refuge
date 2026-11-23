"""What the town knows of the Verde and what lies beyond the walls (owner, 2026-11-23: "Also I forgot about the river
that runs through the town... the Verde river. Legends have it is the body of Kteol submerged. It goes out to the
jungle. Not in the game yet, but out side the city walls, farms, lizard tribes and about 30 miles down a wiggly river is
Malice. All of this is in the Lorekeeper lore. So you can start to give characters and the city knowledge of what is
beyond.")

Twenty-five people get new topics, merged over the earlier files (each key here is new, so it adds a topic; Hanklevode's
old origin topic is retired and written again without "malice" and "smith", so those words reach his new Malice topic).
Each knows what their life would give them. Canon and sources are in notes/beyond.md. The era is before the war: Kteol
is asleep and a legend, Santa Guistina stands, the Smith rules Malice and has no pact with the Refuge, and nothing is
infected.

Geography the lines keep to (host defaults where canon is silent): the Verde comes out of the mountains at Malice (canon:
"the Fortress in the Mountain Range at the End of the Green"), winds thirty miles through jungle, mangrove, Meters
fishing camps and stilt farms of cane and plantain, comes in under the town wall at the River Gate, runs under the stone
bridge by the market and out into the harbour. Malice is therefore UP the river from the town, and the river is the
only way there (owner, 2026-11-23: "No road to malice. It's only accessibly by the river"): three days poling up against
the current, two coming down with it. A farm path runs along the bank as far as the last farm and stops.

Malice is known, not reached (owner, 2026-11-23: "Malice shouldn't be accessible yet, it's just known about as a
location"). Nothing beyond the walls is a place you can go, and the lines never offer the trip: the farm boats take no
passengers, and no boatman in the Refuge goes past the last farm, not for silver, not for rum.

Speech is written between backticks here and turned into double quotes at the bottom (`_said`), as in
cast/i_klhyt_river.py.
"""

# invented: host: the river's ways: Malice three days poling up by boat and two down (no road: the owner's word); eleven to fifteen flatboats a day; a copper a boat at the bridge quay; the farm boats take no passengers and no boatman goes past the last farm (Malice known, not reached: the owner's word)
# invented: host: the farms: Corran's sugar plantation a day up on the left bank (Tully's father cuts cane there); the widow Lusk's plantain farm is the last farm, and she has not come down in nine days; farmers ring a bell on a pole at every third farm
# invented: host: something has been taking goats off the stilts at the far farms (the scratches go up the posts); red scales seen standing in the cane after dark (Bar-Kays, the warrior colour); left open for the owner
# invented: host: Lizardfolk lore of Kteol as the town tells it: his head in the mountains and his tail in the harbour; his eye frozen open where the river starts, and the shamans keep a green stone away from it (canon: the Eye of Green, "used to keep the Demi God Ktoel asleep", later stolen and plunged into his frozen eye to wake him); the bridge lies on his back; the Meters say the river keeps one drowned in nine for him
# invented: host: the Mandrills' calling is a song about Kteol waking (Hessa's mother's word); canon has the Festival of Kteol's Awakening and the calling to war, not this link
# invented: host: the Smith's envoy came down the Green last dry season with an iron badge and his terms; Klhyt gave him a rum and read him Article One, Gog gave him a fish, the Custodian gave him a receipt; the Smith's iron barge comes twice a season and its bargemen count the town
# invented: host: the Smith's recruiter at the Ogre last month (a hammer badge, three hot meals and a fight a week); Ludo threw him out
# invented: Hanklevode: he built the lock on the strongroom under the Smith's forge, and will draw it for ten gold; on clear days "something goes up from the sheds behind the forge" (a hint of the Smith's airships, never named)
# invented: Klhyt: Article Four of the Charter: the Verde is free water, any boat may come down it and any people fish it, and a copper at the bridge keeps the quays; "the stream" in his beach story was the Green's mouth, choked with mangrove; he signed money for a watch post at the last farm and it went where the dues went
# invented: Fat Gog: Corran's sugar makes the Stripperwitch's rum, never counted by the Custodian
# invented: Phillip Everuex: the family's "understanding" with some Lizardfolk upriver about timber (canon has a rumoured Everuex deal with the Lizardfolk over the forests, in a later era); the family keeps a house in Santa Guistina; his father sends the Smith a case of wine a year and gets a horseshoe back, eleven so far
# invented: Captain Eirik: ironwood and redheart up the Green, floated down by the Meters for a silver a trunk; twenty silver to whoever brings him a Meters elder's mark on a raft of fifty
# invented: Ottoline Crabbe: her hook on a pole at the bridge quay, the Meters paid in salt for what they find; the Gentleman From Upriver (good Landfall coat, iron nails in his pockets, a Blackbyrd dart in his neck); she hears Saint Meren's bell from the mangroves where the Green meets the salt; two Tidewardens asked her after a fingerbone in a silver case
# invented: Thoradin: followed the Green twelve days; saw the Monkey Temple north of the river where the hills start and did not go in; has not found the falls
# invented: Wendeline Moss: "Thirty Miles of Green", the journal of Amos Pettibone of the Landfall Survey, third shelf; page forty-one, a lake at the head of the river that does not ripple, round as an eye
# invented: the Bard of Moonport: the Meters song "The Green Lies Down"; Naga Juan walks as an old Fronterian gentleman in a white hat (canon: "an old spanish man"); Dosa's thousand heroes stand in the Serpent's Egg
# invented: Harrow: the River Gate's portcullis winch is rusted solid and the Town Hall will not pay for grease; the Lusk bell rang twice last week after midnight
# invented: Wick: the men off the Malice barge paid her a silver to say where the watch sleeps and how many keep Gog's door
# invented: Captain Aelith: the Moonmoth will not go up the Verde ("it is not water; it is someone sleeping")
# invented: River: the Verde as her weather glass (lime-green after storms in the hills, glass-still before a blow) and the dawn fog down it that covers the harbour

# the news, as flags on the speaker (Klhyt only: tied in the warehouse, or nailed in the Emerald Eye's hold)
BOUND = {"bound": True}


def staged(*steps):
    """(if_state, line) pairs, newest news first, then the line for when none of them holds."""
    *pairs, last = steps
    out = last
    for cond, line in reversed(pairs):
        out = {"if_state": cond, "line": line, "else": out}
    return out


CAST = {
    # ---- the Meters fisherman: the tribes, the god in the river, the camps upriver, what lives in the water --------
    "Ssark": {
        "brief_more": (
            "The Verde and beyond (owner, 2026-11-23). You call the river Kteol: the god lying down, asleep, his eye "
            "frozen open far up where it starts; the shamans keep a green stone away from that eye, and while it is "
            "kept he sleeps. You leave him a fish at dusk and never stand under the bridge. You know the four colours of your people (blue Mandrills of Calak Mul, red Bar-Kays, yellow-black "
            "Blackbyrds, green Meters), the Meters camps past the farms, and the pythons and crocodiles in the "
            "shallows. For a poured tot you go as far as the last camp in your dugout, never past it."),
        "dialog": {
            "kteol|verde|river|rivers|snake|serpent|serpents|snakes|legend|legends|asleep|sleeping|lying|bridge|stone|stones|offering|offerings|dusk|eye|frozen":
                "He is quiet a long time. `You call it Verde. It is Kteol. The god, lying down, from the mountains to "
                "the sea.` He turns his cup a quarter turn. `He sleeps. Far up, where the river starts, his eye is frozen "
                "open. The shamans keep a green stone, and keep it away from that eye. Stone kept, god sleeps. My "
                "grandmother says so.` A pause. `So we leave him a fish at dusk. And nobody "
                "stands under the bridge. The bridge is on his back.`",
            "tribes|calak|mul|blackbyrds|blackbyrd|bar-kays|barkays|kays|clans|colours|colors|blue|red|yellow|villages":
                "`Four colours.` He holds up four claws. `Blue: the Mandrills. They rule, from Calak Mul in the north. "
                "Pyramids in the trees. Red: the Bar-Kays. They fight. Yellow and black: the Blackbyrds. You do not "
                "see them. That is the point.` He folds the claws down. `Green: Meters. We fish. We talk to outsiders. "
                "Too much, the others say.` A long pause. `If you see red scales on the river, go home.`",
            "upriver|farms|farm|farmers|fields|cane|camps|camp|outside|beyond|walls|jungle|towpath|dugout|guide|journey":
                "`Past the River Gate: cane, plantain, farmers on stilts. Then Meters camps. Smoke on the bank, my "
                "people drying fish.` He tastes the air. `Then mangrove. Then jungle, and the river goes on without "
                "you.` He looks at the bottle. `My dugout goes to the camps and back, with fish, and nobody in it but "
                "me. Past the last camp I do not go, and I take nobody. Nobody pays enough for past the last camp.`",
            "python|pythons|crocodile|crocodiles|caiman|swim|swimming|danger|dangers|dangerous|beasts|beast|guardian":
                "`Pythons. Long as a dugout.` He holds his claws apart, then further. `Longer. They lie in the "
                "shallows past the farms and look like logs until they are not.` A pause. `My people say they guard "
                "the river. They take the greedy ones: the man who nets more than he can carry, the boat that leaves "
                "no fish.` Another. `Also crocodiles. Crocodiles take anyone.`",
        },
    },

    # ---- Fat Gog: the god under the town, the Smith, everything that comes down the Green --------------------------
    "Fat Gog": {
        "brief_more": (
            "The Verde and beyond (owner, 2026-11-23). Your people call the river Kteol, asleep with his head in the "
            "mountains and his tail in the harbour; you told Klhyt so when he built here. Everything that comes down the "
            "Green comes past you sooner or later. The Smith in Malice wants every river mouth on this coast, and this "
            "is the best one: his envoy came last dry season and got a rum from Klhyt and a fish from you, and no "
            "answer. This season the far farms lose goats and Tully's father has seen red scales in the cane; you pay "
            "for news from upriver."),
        "dialog": {
            "verde|river|rivers|green|kteol|snake|serpent|serpents|snakes|legend|legends|asleep|sleeping|lying|bridge|stones":
                "He is quiet a while, the way a big thing is quiet. `The Green. My people call it Kteol, the great "
                "serpent, asleep with his head in the mountains and his tail in our harbour. When Klhyt wanted to build "
                "here I told him he was building on a god's tail.` A low chuckle. `He said a god asleep is a quiet "
                "neighbour, and put up a pump. Forty-odd years, friend, and the god has not complained. Leave him his "
                "fish at dusk and do not stand under the bridge, and he never will.`",
            "malice|smith|king|kingdom|fortress|mountains|forge|hammer|envoy|envoys|kneel|knee|sigil|badge|bargemen":
                "He folds his hands on his belly. `The Smith. A big man who came with a ship full of tools and walked "
                "them up into the mountains at the head of the Green, and calls himself King of Shalamar.` His eyes do "
                "not smile. `His envoy came down the river last dry season with an iron badge: bend the knee, get the "
                "protection. Klhyt gave him a rum. I gave him a fish. Neither of us gave him an answer.` A slow blink. "
                "`Every river needs a mouth, friend, and this is the best mouth on the coast. If his bargemen ask you "
                "how many keep my door, say a hundred.`",
            "farms|farm|farmers|fields|cane|sugar|plantain|plantains|plantation|plantations|outside|beyond|walls|jungle|barge|barges|flatboat|flatboats|boats|cargo|trade|goats|upstream":
                "`Everything that comes down the Green comes past this town sooner or later, and so past me: plantains, "
                "sugar, birds in cages, the Smith's iron, a drowned man now and then.` He lifts one claw. `The farms "
                "past the River Gate pay no dues and get no watch, and Corran's sugar makes my rum, which the Custodian "
                "has never once counted.` The claw comes down. `This season the far farms are losing goats off their "
                "stilts, and Tully's father has seen red scales standing in the cane. Red is the warrior colour, "
                "friend. Bring me anything you hear from up the river. I pay for news. You know I do.`",
        },
    },

    # ---- the thief out of Malice: the city, the Smith, the way there ------------------------------------------------
    "Hanklevode": {
        "brief_more": (
            "Malice (owner, 2026-11-23; canon, LoreKeeper): a fortress-city of black stone in a mountain valley at the "
            "head of the Green, one great gate of iron-banded timber, a forge district that smokes day and night and a "
            "hammer you hear for miles. The Smith holds court at his own forge and hammers while you talk; he named the "
            "city after his first mule; his rule is bend the knee, get the protection, and a second visit for those who "
            "refuse. You built the lock on the strongroom under his forge and would draw it for ten gold. The way: thirty "
            "miles as the river winds and only by the river, three days poling up through Blackbyrd country, two down; "
            "there is no road, and no boatman in the Refuge will take anyone up it. You came down once and are not going back."),
        "dialog": {
            "from|home|born|malice|smith|came|arrived|brought": None,  # retired: "malice" and "smith" have their own topic now
            "from|home|born|came|arrived|brought":
                "`Malice dried up. The Smith's people want you to swear to him, and swearing doesn't pay.` The coin "
                "walks. `Before that, a Landfall port and a locksmith who taught me better than he meant to.`",
            "malice|smith|king|kingdom|fortress|forge|hammer|hammering|mule|kneel|swear|sworn|sigil|valley|mountains|strongroom":
                "The coin stops. `Malice. Black stone walls in a valley at the head of the Green, one great gate of "
                "iron-banded timber, and a hammer you can hear three miles off that never stops. The Smith holds court "
                "at his own forge and hammers while you talk. Named the city after his first mule.` The coin walks "
                "again. `The rule is simple: bend the knee, get the protection. Refuse, and you get a second visit. I "
                "never met anyone who wanted the third. And on clear days something goes up from the sheds behind the "
                "forge that I'm not paid enough to describe.` A small smile. `I built the lock on the strongroom under "
                "his forge. I could draw it for you. Ten gold, and you'll never use it, because nobody robs the Smith "
                "and walks home.`",
            "malice|road|route|journey|travel|towpath|miles|thirty|days|walk|walked|trip|far|distance|verde|river|green|boat":
                "`Thirty miles as the river winds, and it winds like a drunk going home. And there's no road, before "
                "you ask. Past the last farm the banks are mangrove and the jungle comes down to the water: you go by "
                "boat or you don't go, and you don't go, because there's not a boatman on the quay who'll take you past "
                "the last farm. I asked. For fun.` He counts on his fingers. `Three days poling up against the current, "
                "if anyone would. Two coming down. Blackbyrd country both banks, all the way. You won't see them. That's "
                "how you know they're there.` He shrugs. `I came down with my eyes shut. I recommend it.`",
        },
    },

    # ---- the dwarven ranger: the river to its end, the peoples out there, the temple, the dwarf under the falls ----
    "Thoradin": {
        "brief_more": (
            "The jungle beyond (owner, 2026-11-23). You followed the Green twelve days once, to the mountains and the "
            "hammering of Malice. You know the Lintah Serpents (lizardfolk who leave bone totems on what they burn), the "
            "Hoofbound horse clans of Stormstride, and the black Toucan elves on feathered beasts; you saw the Monkey "
            "Temple with nine gods on its wall and did not go in. The Meters tell of a dwarf under a waterfall up a side "
            "stream who trades stories: if anyone knows where a druid is, he does, and you have not found the falls."),
        "dialog": {
            "verde|river|rivers|green|towpath|banks|bank|python|pythons|mangroves|mangrove|followed|source|mountains|upstream|boat":
                "`I followed the Green twelve days once, looking for a druid.` He picks a leaf out of his beard. `A day "
                "of cane and stilt-houses. A day of Meters camps. Then mangrove, then jungle so close over the water "
                "you pole in the dark at noon. Pythons in the shallows, longer than the boat. At the end, mountains, "
                "and a hammering in them like a heart.` He drops the leaf. `No druid.`",
            "beyond|outside|walls|wild|wilds|inland|interior|tribes|tribe|lintah|serpents|hoofbound|horse|horses|stormstride|totems|clans|riders|toucan|toucans|dinosaur|dinosaurs|feathered|elves|peoples|jungle":
                "`Past the walls? Farmers. Then Meters, who'll trade. Then the ones who won't.` He counts on blunt "
                "fingers. `Lintah Serpents: lizardfolk who leave bone totems on the fences they burn. Horse clans on a "
                "hill-fort inland, Stormstride, the Hoofbound: good horses, bad tempers, and they hate the Lintah. And "
                "black-skinned elves on feathered beasts bigger than a house. Toucan elves, the Meters call them.` He "
                "looks at his hands. `They watched me cross a river once and let me. I don't know why.`",
            "monkey|monkeys|temple|ruin|ruins|carvings|carved|nine|gods|egg|statues":
                "`There's a temple north of the river, where the hills start. Monkeys keep it.` He is quiet a moment. "
                "`Nine gods cut in the wall by the door: a turtle, a giant, a bird, a spider, a tree, a jaguar, a snake, "
                "a squid as big as a ship, and a mushroom, which I didn't like the look of.` He frowns. `The door goes "
                "down. The air coming up smelled of snake. I didn't go in. The Meters call it the Serpent's Egg and "
                "won't say more.`",
            "falls|waterfall|waterfalls|baelin|root|roots|rootfolk|dwarves|stories|story|thousand":
                "`The Meters tell of a dwarf under a waterfall, up a side stream off the Green. Root folk, the shy "
                "kind. Sat down a thousand years ago with a table and a chair and asked travellers for stories, and the "
                "roots grew into him.` His hand goes to the bundle at his chest. `If anyone in this jungle knows where a "
                "druid is, it's him. I haven't found the falls. Find them and tell me, and I'll owe you more than "
                "coin.`",
        },
    },

    # ---- the elf druid at the tea table: the river's spirit, the jungle's own elves, a witch to refuse --------------
    "Saelwyn": {
        "brief_more": (
            "The Verde and beyond (owner, 2026-11-23). You have put your hand in the river at dawn and felt it breathe "
            "in its sleep; you do not chart it, because the Meters say it turns over and the channels move. The jungle's "
            "own elves, the Toucan elves behind their endless storm on a great lake, are no kin of yours and friends of "
            "the Lizardfolk. You warn people off Nereth Korr, the jungle witch who makes bargains."),
        "dialog": {
            "verde|river|rivers|green|kteol|snake|serpent|serpents|spirit|spirits|asleep|sleeping|breathing|bridge|legend|channels|current":
                "`The Lizardfolk say the river is a god, lying down. Kteol.` She turns her cup a quarter turn. `I put my "
                "hand in it at dawn once, by the bridge. It was warm in the wrong places, and slow, like something "
                "breathing in its sleep.` A pause. `Still asleep. Leave it so. My charts stop at the river mouth, and "
                "nobody charts the Green: the Meters say it turns over in its sleep, and the channels move.`",
            "toucan|toucans|cousins|kin|lake|storm|dinosaurs|dinosaur|feathered|jungle":
                "`The jungle has its own elves. Black-skinned, feathered, riding beasts out of an older world. They live "
                "behind a storm that never ends, on a great lake, and they do not come to the coast.` Her voice cools. "
                "`They are not our cousins, whatever the colonists think. To them we are newcomers with sad stories and "
                "long ships.` She sips. `They are friends of the Lizardfolk. And the Lizardfolk are listening to a "
                "calling.`",
            "witch|witches|nereth|korr|bargain|bargains|hag|curse|curses|cursed":
                "`If a thin woman in rags of colonist cloth and lizard leather offers you a bargain in the jungle, "
                "refuse before she finishes the sentence.` She does not smile. `Nereth Korr. Older than most of the "
                "groves out there. Colonists who cross her come home weeping, and very cooperative.` She sips. `The "
                "Lizardfolk leave her shiny shells and pass her words to their hatchlings. I would leave her shells "
                "too.`",
        },
    },

    # ---- the Everuex son: what the River Queen is for, the city up the coast, the horseshoes -----------------------
    "Phillip Everuex": {
        "brief_more": (
            "The Verde and beyond (owner, 2026-11-23). The River Queen is a river boat, and the family means her to go "
            "up the Verde to the plantations and the timber, where it has an understanding with some Lizardfolk you are "
            "not to mention. You would rather be in Santa Guistina, the biggest and most Vorkathian city on Shalamar, "
            "where the family keeps a house. Your father sends the Smith a case of wine a year and gets back a "
            "horseshoe."),
        "dialog": {
            "verde|river|green|upriver|trade|plantations|plantation|timber|understanding|deal|jungle|lizardfolk":
                "`The Verde! At last, a river, which is what the River Queen is for.` He fans himself. `Father means "
                "her to go up it, to the plantations and the timber, and talk business with some Lizardfolk with whom "
                "the family has an understanding. I am not to mention the understanding.` He mentions it again, to "
                "himself. `I am not going up it. There are snakes in it longer than the boat. A man at the Turtle told "
                "me so, and then he laughed, which I thought unkind.`",
            "santa|guistina|north|city|cathedral|governor|civilisation|civilization|winters|tailors":
                "`Santa Guistina. Up the coast, to the north: paved streets, a cathedral of the Eight with real glass, "
                "a governor who dines at eight, and nobody sweating in public.` He sighs. `The biggest city on "
                "Shalamar, and the only one with tailors. The family keeps a house there. Say my name at the door and "
                "they will give you a glass of water and possibly a chair.`",
            "malice|smith|king|kingdom|horseshoe|horseshoes|forge|hammer":
                "`The Smith? A blacksmith who calls himself King of Shalamar.` He sniffs. `Father sends him a case of "
                "wine every year, and every year a horseshoe comes back, and Father puts it in a drawer and will not "
                "discuss it. There are eleven horseshoes in that drawer.` He fans faster. `I don't like to think what "
                "the twelfth means.`",
        },
    },

    # ---- the harbourmaster: river traffic and the iron barge ---------------------------------------------------------
    "Harbourmaster Teague": {
        "brief_more": (
            "The river (owner, 2026-11-23). Eleven to fifteen flatboats a day come down the Verde past the River Gate, a "
            "copper a boat at the bridge quay, which goes up the hill and comes back short. They come down at dawn and go "
            "back up on the towline at noon, and they take no passengers: you have asked. Malice sends iron down twice a "
            "season on a covered barge whose bargemen ask for receipts, count the town, and take nobody back with them."),
        "dialog": {
            "verde|river|green|bridge|quay|quays|flatboat|flatboats|barges|boats|boat|plantain|plantains|cane|cargo|farm|farms|downriver|towline|seat|ride":
                "`The Verde?` He finds a clean page. `Eleven to fifteen flatboats a day down past the River Gate: "
                "plantains, cane, sugar in loaves, hides, birds in cages, once a live crocodile for the Apothecary. A "
                "copper a boat at the bridge quay, which I collect, and which goes up the hill, and which comes back "
                "short like everything.` He sharpens the pencil with his thumbnail. `They come down at dawn and go back "
                "up on the towline at noon, and they take no passengers. Farmers don't. And past the last farm nobody "
                "goes at all, not the Meters, not for rum. The river's for coming down.`",
            "malice|smith|iron|nails|barge|bargemen|bargeman|receipt|receipts|hammer|forge|kingdom|king":
                "`Malice sends iron down twice a season on a covered barge: nails, hinges, hooks, tools better than "
                "Landfall's.` He taps the tally. `The Smith's bargemen pay their dues to the copper and ask for a "
                "receipt, which nobody else has done in eleven years. Then they stand on the quay and look at the town "
                "the way a man looks at a house he means to buy.` He swallows. `Last time one of them asked me how many "
                "ships the harbour holds. I said I'd have to count.`",
        },
    },

    # ---- the fruit woman: the farms she buys from, and the rule of the bridge ---------------------------------------
    "Mother Ines": {
        "brief_more": (
            "The farms (owner, 2026-11-23). You buy off the growers' carts at the gate: cane on the left bank, plantain "
            "on the right, houses on stilts against the wet-season floods. The widow Lusk at the last farm has not come "
            "down in nine days, and you have asked the sergeant twice to send somebody up the bank, and he says the "
            "watch stops at the wall. Nobody throws anything off the bridge: the Meters asked, the first year, and "
            "Klhyt said do as they say."),
        "dialog": {
            "farm|farms|farmer|farmers|growers|grower|fields|plantain|plantains|cane|sugar|plantation|plantations|outside|beyond|walls|stilts|countryside|lusk|widow|carts|cart":
                "`The farms, love? Out the River Gate: cane on the left bank, plantain on the right, and houses on "
                "stilts, because the Green comes up every wet season and takes the chickens.` She laughs, then "
                "doesn't. `I buy off their carts at the gate. The widow Lusk at the last farm brings the best plantains "
                "on the river, and she's not been down in nine days. Nine! She's never missed three.` She fans hard. "
                "`I've asked the sergeant twice to send somebody up the bank to see she's breathing, and he says the "
                "watch stops at the wall, as if the wall was the end of the world.` She fans harder. `Maybe it is.`",
            "verde|river|rivers|green|bridge|kteol|snake|serpent|scraps|throw|throwing|superstition|legend|quay":
                "`Nobody throws anything off the bridge, my heart, not so much as a mango skin.` She wags a finger. "
                "`The first year the Meters asked us nicely, and Klhyt said do as they say, it's their river and their "
                "god in it. Forty-five years, and nobody has.` She drops her voice to a roar. `A sailor did, once. "
                "Threw a bottle off it at the fish. They found him three days later at the bridge quay, love, and "
                "nobody had touched him, and the bottle was still in his hand.`",
        },
    },

    # ---- the chandler: kit for the long road -------------------------------------------------------------------------
    "Hob Merrow": {
        "brief_more": (
            "The long way (owner, 2026-11-23). Malice is thirty miles as the Green winds and only by the river, "
            "three days poling up, two down; there is no road, and nobody takes passengers up it. You price the kit "
            "anyway, from your own shelves (eleven gold and a half with a hooded lantern, six and a half with torches), "
            "for the day somebody does, and tell people to boil the river water. Nobody sells a map of the Green: it "
            "moves."),
        "dialog": {
            "verde|river|green|upriver|malice|miles|distance|far|towpath|journey|expedition|trek|travel|trip|jungle|beyond|outside|kit|kitted|outfit":
                "`The long way, friend, and it's all water.` He leans on the counter. `Malice: thirty miles as the "
                "Green winds, and no road to it, so don't let anyone sell you one. Three days poling up, two back "
                "down, and not a boatman at the bridge quay who'll take you past the last farm. But if one ever does: "
                "pack, bedroll, four days' rations, one for luck, two waterskins, fifty foot of rope for the snags, a "
                "hooded lantern and a flask of oil.` He chalks it on the slate anyway. `Eleven gold and a half with the "
                "lantern, six and a half with a bundle of torches. "
                "Boil the river water, or drink it and go and see Sister Agathe. And don't ask me for a map of the "
                "Green. Nobody sells one. It moves.`",
        },
    },

    # ---- Klhyt: the river he built on, the Smith's envoy, the farms he promised ------------------------------------
    "Klhyt": {
        "brief_more": (
            "The Verde and beyond (owner, 2026-11-23). You hate rivers, and built your town at the mouth of one: the "
            "\"stream\" in your beach story was the Green's mouth, choked with mangrove, and the Meters helped cut the "
            "first quay. Article Four of your Charter: the Verde is free water, any boat may come down it and any people "
            "fish it, and a copper at the bridge keeps the quays. The Smith's envoy came last dry season with terms; you "
            "gave him a rum and Article One, and you want a town that can say no in one voice when the second visit "
            "comes. You promised the farms a watch post at the widow Lusk's and signed the money; it went where the "
            "dues went."),
        "dialog": {
            "verde|river|rivers|green|bridge|quay|quays|kteol|serpent|snake|stream|mouth|mangrove|mangroves": staged(
                (BOUND, "`The river?` He listens. `I can hear it from in here, shipmate, going out under the pier like "
                        "it's late for something.` He tests the rope. `Get me out, and I'll tell you everything I know "
                        "about it, which is mostly that I hate it.`"),
                "`When I tell it, I say there was a stream.` He grins through his beard. `There wasn't. It was the "
                "Green's mouth, choked with mangrove so you couldn't see it was a river at all, and Gog laughed at me "
                "for a year. The Meters helped us cut it open for the first quay.` He sobers. `I hate rivers, shipmate; "
                "everybody knows. That one I keep a truce with. Article Four: the Verde is free water, any boat may come "
                "down it and any people fish it, and a copper at the bridge keeps the quays. And the Meters' rule, which "
                "isn't written anywhere and matters more: a fish at dusk, and nobody stands under the bridge.`"),
            "malice|smith|king|kingdom|fortress|envoy|envoys|kneel|knee|sigil|hammer|forge": staged(
                (BOUND, "`The Smith?` He laughs through cracked lips. `If his envoy came back this week he'd find the "
                        "mayor in a box and the Custodian holding the pen. Get me out of here before somebody signs "
                        "something.`"),
                "`The Smith.` He snorts. `A man with a hammer who calls himself King of Shalamar. His envoy came down "
                "the Green last dry season with an iron badge and his master's terms: bend the knee, get the "
                "protection.` He spreads his big hands. `I gave him a rum and read him Article One. He said the Smith "
                "would pay a second visit. I said bring rum.` A pause. `He will one day, shipmate, and not with rum. "
                "When that barge comes I want a town that can say no in one voice. That's what the Custodian's thieving "
                "costs me. Not the money. The voice.`"),
            "farm|farms|farmer|farmers|fields|cane|plantain|plantains|outside|beyond|walls|growers|stilts|lusk|jungle": staged(
                (BOUND, "`The farms?` He rattles the chair. `I promised them a watch post at the last farm and signed "
                        "the money over. I'd bet the money's where I am: somewhere the Custodian put it. Cut me loose "
                        "and I'll find both.`"),
                "`Past the River Gate it's farms: folk who came here with nothing and cleared an acre with a cane "
                "knife.` His voice warms. `They pay no dues and get no watch, and when the jungle comes, they come "
                "inside. That's what the wall is for.` His face clouds. `I promised them a watch post at the last farm, "
                "the widow Lusk's. I signed the money for it last spring. Ask the Custodian where it went.`"),
        },
    },

    # ---- the undertaker: what the river gives back, and the drowned bell ----------------------------------------------
    "Ottoline Crabbe": {
        "brief_more": (
            "The river (owner, 2026-11-23). The Verde gives back its drowned slowly: three days from the farms to the "
            "bridge quay, five from past the mangroves. You keep a hook on a pole at the quay and pay the Meters in "
            "salt for what they bring; the Meters say the river keeps one in nine for the god. On still evenings you "
            "hear Saint Meren's bell from the drowned chapel in the mangroves where the Green meets the salt, and two "
            "Tidewardens once asked you after a fingerbone in a silver case."),
        "dialog": {
            "verde|river|green|bridge|drowned|downriver|current|hook|pole|floater|floaters|quay":
                "`The Verde gives back what it takes, dear, but slowly, and never where it took it.` She touches the "
                "tape at her neck. `Three days for a drowned man to come down from the farms to the bridge quay, five "
                "from past the mangroves. I keep a hook on a long pole at the quay, and the Meters bring me what they "
                "find, and I pay them in salt. They say the river keeps one in nine for the god. I've never had the "
                "numbers to argue.` She looks at nothing. `Last rains it gave me a man in a good Landfall coat with "
                "iron nails in his pockets and a little feathered dart in his neck. Blackbyrd work, the Meters said. "
                "Nobody claimed him. He's in the book as the Gentleman From Upriver.`",
            "bell|bells|meren|chapel|tidewardens|toll|tolls|tolling|relic|reliquary|fingerbone|saint":
                "`On still evenings, with the wind off the sea, you can hear a bell from the mangroves where the Green "
                "meets the salt.` She doesn't look toward it. `The Meters say it's an old chapel the tide took, Saint "
                "Meren's, a fisher-saint. It tolls for the drowned at sundown.` A dry smile. `Every time I've heard it, "
                "the river has given me someone within three days. And last rains two hooded men came asking if "
                "anything had come down with a fingerbone in a silver case. Tidewardens, they called themselves. I said "
                "no, dear, and it was true.`",
        },
    },

    # ---- River: the river as a weather glass (her secret is never said) ----------------------------------------------
    "River": {
        "brief_more": (
            "The Verde (owner, 2026-11-23). You read it like weather: lime-green after a storm in the hills and the bridge "
            "quay flooding by midnight, still as glass before a blow, and before dawn a fog that comes down it out of the "
            "jungle and lies on the harbour like a sheet. You may hint what a boat could do under that fog. You never "
            "say what yours does."),
        "dialog": {
            "verde|green|bridge|quay|quays|upriver|downriver|kteol|serpent|snake|flood|floods|flooding|current":
                "`The Verde?` She leans on the bar. `It tells the weather two hours before the sky does, love. Goes the "
                "colour of limes when it's stormed in the hills, and then the bridge quay floods by midnight. Goes "
                "still as glass before a big blow.` She polishes a glass that doesn't need it. `And before dawn the fog "
                "comes down it out of the jungle and lies on the harbour like a sheet till the sun eats it. A boat could "
                "go out under that and nobody on the pier the wiser.` A smile. `Not that anyone would. Drink?`",
        },
    },

    # ---- the Bard: the river's song, and the mule's ------------------------------------------------------------------
    "The Bard of Moonport": {
        "brief_more": (
            "The Verde and beyond (owner, 2026-11-23). You covet the Meters song The Green Lies Down: Kteol asleep, the "
            "seven snake lords who keep his rest, Dosa in the Serpent's Egg with her thousand stone heroes, and Naga Juan "
            "walking about as an old Fronterian gentleman in a white hat. You have eleven hanging verses about the "
            "Smith and his mule, and have never been to Malice."),
        "dialog": {
            "kteol|snake|serpent|serpents|verde|river|green|legend|legends|lords|egg|heroes|medusa|naga|juan|dosa":
                "`Ah! The Meters have a song I'd give my lute to set properly: The Green Lies Down.` He picks out a "
                "slow, sliding tune. `The river is Kteol asleep, head in the mountains, tail in our harbour, and seven "
                "snake lords keep his rest. One is Dosa, in the Serpent's Egg, whose look turns heroes to stone: a "
                "thousand went in for her and stand there still, very handsome, very quiet. One, Naga Juan, walks about "
                "as an old Fronterian gentleman in a white hat.` He stops playing. `So if an old man in a white hat asks "
                "you for a light, give it him and walk away. A copper for the verse. Two for the one about when the god "
                "wakes, and I only sing that one in daylight.`",
            "malice|smith|king|mule|forge|hammer|anvil":
                "`The Smith named his city after his first mule, and I have eleven verses about it that would get me "
                "hanged, one for each.` He grins. `Malice! A fortress where the hammer never stops, a king who's never "
                "told a soul his name, and a gate you go through on your knees, figuratively, then literally.` He plays "
                "a heavy, clanking chord. `They say he likes songs about himself and pays in iron. I'm told a great many "
                "things about Malice. I've never been. I'd like to keep my knees.`",
        },
    },

    # ---- the landlady: the farm folk who come in to drink -----------------------------------------------------------
    "Sister Agathe": {
        "brief_more": (
            "The farms (owner, 2026-11-23). Farm folk drink at the Omberhulk on market nights and pay in sugar loaves "
            "when short. One told you something is taking goats off the stilts at the far farms, and not crocodiles: "
            "the scratches go up the posts."),
        "dialog": {
            "farm|farms|farmer|farmers|growers|cane|cutters|plantain|plantains|fields|outside|beyond|walls|goats|goat|stilts|countryside":
                "`The farm folk? Market nights, child: cane-cutters with hands like rope, plantain wives, the odd Meters "
                "boatman. They drink fast, because they've a boat to pole home by dawn, and when they're short they pay "
                "me in sugar loaves.` She lowers her voice. `One told me Tuesday that something's taking goats off the "
                "stilts at the far farms. Not crocodiles, she said. The scratches go up the posts.` She makes the sign "
                "of the Eight. `Arms preserve us. I gave her a second mug for nothing, and I'd do it again.`",
        },
    },

    # ---- the farm boy in the Fist: his father's cane, and what stands in it at night --------------------------------
    "Tully": {
        "brief_more": (
            "The farms (owner, 2026-11-23). Your father still cuts cane at Corran's sugar plantation, a day up the Green "
            "on the left bank. He sent word down with the sugar boat: red Lizardfolk standing in the cane after dark, "
            "watching. You want someone to tell him you have boots."),
        "dialog": {
            "cane|sugar|da|dad|father|corran|fields|cutting|cutter|cutters|overseer|red|farms|plantations|lizards":
                "`The cane? Corran's place, a day up the Green on the left bank. My da still cuts there. Sun like a "
                "hammer, cane up to here, and the overseer counting your fingers at night to see you've still got ten.` "
                "He drinks. `Da sent word down with the sugar boat: lizardfolk standing in the cane after dark, just "
                "watching. Red ones. Da says red's the fighting kind.` He laughs too loud. `Forget I said that. If you "
                "go up, mate, tell my da I've got boots. Real boots.`",
        },
    },

    # ---- Gog's door: the god in the river and what the calling sings ------------------------------------------------
    "Hessa": {
        "brief_more": (
            "Kteol (owner, 2026-11-23). Your mother says the god sleeps while the shamans keep the green stone; if a "
            "fool takes it to his frozen eye, far up where the river starts, he wakes hungry. The Mandrills sing about him waking: that is what the "
            "calling is. The old one does not sing it, so you do not."),
        "dialog": {
            "kteol|verde|river|green|snake|serpent|serpents|legend|sleeping|asleep|stone|wake|waking|awake|god":
                "`The warm ones say Verde. It is Kteol. Lying down.` She does not blink. `My mother says he sleeps "
                "while the shamans keep the green stone. If a fool takes the stone to his frozen eye, far up where the "
                "river starts, he wakes. He wakes hungry.` A long pause. `The Mandrills sing about him waking. That is what the calling "
                "is.` Her claw finds the gaff. `The old one does not sing it. So I do not.`",
        },
    },

    # ---- the Xoton envoy: timber up the Green, and the Meters ---------------------------------------------------------
    "Captain Eirik": {
        "brief_more": (
            "Up the Green (owner, 2026-11-23). You met the Meters first with a boat of shells and coral (canon) and they "
            "are your best partners on the coast. The best trunks, ironwood and redheart, are up the Green past the "
            "farms; the Meters float them down for a silver a trunk with no licence. You would pay twenty silver to "
            "whoever brings you a Meters elder's mark on a raft of fifty."),
        "dialog": {
            "verde|river|green|ironwood|redheart|trunks|raft|rafts|float|elder|elders|deal|contact|shells|coral|camps|upstream|timber":
                "`The first time I met the Meters, friend, I came ashore with a boat of shells and coral, and they came "
                "out of the trees with spears, and we all stood there an hour being polite.` He roars with laughter. "
                "`Now they're the best partners on this coast. The best trunks are up the Green past the farms: "
                "ironwood and redheart, straight as masts. The Meters cut them and float them down for a silver a "
                "trunk, no licence, no seal.` He taps his nose. `Bring me a Meters elder's mark on a raft of fifty, and "
                "there's twenty silver in it for you. I'm furniture, friend, but I'm generous furniture.`",
        },
    },

    # ---- the sergeant: the River Gate that will not shut, and the farm bells ----------------------------------------
    "Sergeant Pell Harrow": {
        "brief_more": (
            "The River Gate and the farms (owner, 2026-11-23). The River Gate's portcullis hangs a man's height over the "
            "Verde and its winch is rusted solid; you have asked the Town Hall three times for grease. Past the wall the "
            "farmers ring a bell on a pole at every third farm; the Lusk bell rang twice last week after midnight and "
            "stopped, and three of you cannot go out to it."),
        "dialog": {
            "rivergate|portcullis|watergate|verde|river|green|chain|winch|grease":
                "He sighs before he speaks. `The River Gate's no gate, son. Portcullis hung a man's height up so the "
                "boats pass under, and the chain hasn't moved since the day Klhyt hung it. 'Shut it only if the jungle "
                "comes,' he said.` He rubs his knee. `If the jungle comes by river, it comes under a portcullis that "
                "won't drop. The winch is rusted solid, and the Town Hall won't pay for grease. In my book: three times "
                "I've asked.`",
            "farm|farms|farmers|outside|beyond|bell|bells|jungle|lusk|walls|lookout":
                "`Past the wall the farmers keep their own lookout: a bell on a pole at every third farm.` He sighs. "
                "`Some nights you hear one from here. The Lusk bell rang twice last week, after midnight, and stopped.` "
                "He looks out at the dark. `Three of us, love. I can't send one of three out into that. I wrote it in "
                "the book. The book doesn't go and look either.`",
        },
    },

    # ---- the officer: the Throne's city in the north, and the heathen river -----------------------------------------
    "Lieutenant Voss": {
        "brief_more": (
            "The beyond (owner, 2026-11-23). Santa Guistina, up the coast to the north, is what a colony should be: walls, "
            "a cathedral of the Eight, a governor and a register of every soul. The serpent stones under the Refuge's "
            "bridge and the Lizardfolk's fish would be broken and given to the poor there; when the Throne comes here, it "
            "will not step around them."),
        "dialog": {
            "santa|guistina|north|city|cathedral|governor|colony|register|faithful":
                "`Santa Guistina is what a colony should be.` He dabs his mouth. `Walls. A cathedral of the Eight. A "
                "governor, and a register of every soul and where each came from. It is the largest city on Shalamar, "
                "and the most faithful.` A thin smile. `This Refuge is what a colony becomes when no one is watching. "
                "Someone is watching now.`",
            "kteol|verde|river|green|snake|serpent|serpents|stones|carvings|bridge|idol|idols|lizardfolk|lizards|heathen":
                "`The lizards leave fish for their river. Under your bridge there are serpents cut into the stones, "
                "older than your town, and your townsfolk step around them.` He folds his napkin with care. `In Santa "
                "Guistina such stones are broken, and the fish go to the poor. Here they are left, and a heathen god is "
                "fed.` He looks at you. `When the Throne comes, it will not step around them.`",
        },
    },

    # ---- the street child: the bridge, and the barge men's silver ---------------------------------------------------
    "Wick": {
        "brief_more": (
            "The river (owner, 2026-11-23). You swim everywhere but under the bridge. The men off the Malice barge paid "
            "you a silver to say where the watch sleeps and how many keep Gog's door; you told them the Town Hall porch "
            "(you) and a hundred, and you sell the story for a copper."),
        "dialog": {
            "verde|river|green|bridge|swim|swimming|dive|diving|boats|boat|flatboat|barge|quay|quays|malice|bargemen":
                "`Nobody swims under the bridge, mister, not even me, and I swim everywhere, swear on my tusks. The "
                "Meters won't, and they know things.` She lowers her voice. `That's free. This isn't: the men off the "
                "Malice barge gave me a whole silver to say where the watch sleeps and how many keep Big Gog's door. I "
                "said the watch sleeps under the Town Hall porch, which is me, and a hundred keep his door.` She grins "
                "and holds out a palm. `Telling you was a copper, mister. You already heard it, so you owe it.`",
        },
    },

    # ---- the stevedore: the iron barge and its bargemen --------------------------------------------------------------
    "Ruk Halfhand": {
        "brief_more": (
            "The river (owner, 2026-11-23). Your gang unloads the farm boats at the quays (light) and the Malice iron "
            "barge (heavy, two coppers a load). Its bargemen do not drink or sing; they asked you how many ships the "
            "harbour holds and how many men on the watch, and you told Gog."),
        "dialog": {
            "verde|river|green|quay|quays|barge|barges|flatboat|flatboats|boats|bridge|malice|smith|iron|bargemen":
                "`River boats. Plantains. Sugar. Light.` He counts on his tally sticks. `Malice barge. Iron. Heavy as "
                "sin. Two coppers a load and worth it.` He frowns. `Their bargemen don't drink. Don't sing. Count "
                "things. Asked me how many ships the harbour holds. How many men on the watch.` A long pause. `I said "
                "I count crates.` He stops. `Then I told Gog.`",
        },
    },

    # ---- the sellsword: the Smith is hiring ---------------------------------------------------------------------------
    "Kael Ironjaw": {
        "brief_more": (
            "Malice (owner, 2026-11-23). The Smith's recruiter came to the Ogre last month: swear to the Smith, get a "
            "hammer badge, three hot meals and a fight a week. Ludo threw him out for not buying a drink. You would go "
            "to Malice with anyone who asked, to be first through the gate."),
        "dialog": {
            "malice|smith|king|army|recruiter|recruiting|recruit|swear|hammer|soldier|soldiers|soldiering":
                "`The Smith? Big fella up the river with a hammer and a army.` He grins. `His recruiter come in the "
                "Ogre last month. Swear to the Smith, get a hammer badge, three hot meals and a fight every week, he "
                "says.` He scratches under the hat. `Sounded great. Ludo threw him out for not buying a drink. Ludo's "
                "got principles.` He thinks about it. `You going to Malice, I'll come. Somebody's got to be first "
                "through the gate.`",
        },
    },

    # ---- the librarian: the one book on the Green --------------------------------------------------------------------
    "Wendeline Moss": {
        "brief_more": (
            "The Green (owner, 2026-11-23). Your library has one book on it: Thirty Miles of Green, the journal of Amos "
            "Pettibone of the Landfall Survey, who came back down in a Meters canoe raving. Page forty-one: at the head "
            "of the river, below the mountain fortress, a lake that does not ripple, cold as winter, round as an eye."),
        "dialog": {
            "verde|river|green|kteol|surveyor|journal|pettibone|frozen|lake|source|jungle|serpent|snake":
                "`We have one book on the Green.` She does not get up. `Thirty Miles of Green, the journal of a "
                "surveyor, Amos Pettibone, Landfall Survey. Third shelf, spine out. He went up the river to map it and "
                "came back down in a Meters canoe, raving.` She quotes from memory. `Page forty-one: at the head of the "
                "river, below the mountain fortress, a lake that does not ripple, cold as winter in the jungle, round "
                "as an eye. He would not drink from it. He would not say why.` A pause. `Read it in here. Not in bed.`",
        },
    },

    # ---- the Custodian: the Throne does not recognise a crown of horseshoes ----------------------------------------
    "The Custodian": {
        "brief_more": (
            "Malice (owner, 2026-11-23). The Smith is a blacksmith who crowned himself; the Throne recognises one crown. "
            "When his envoy came, Klhyt gave him a rum and you gave him a receipt for it. You would pay a silver a name "
            "for anyone in town who talks to his bargemen."),
        "dialog": {
            "malice|smith|king|kingdom|crowned|envoy|envoys|hammer|forge|rebel|usurper|horseshoe|horseshoes|bargemen":
                "`The so-called Smith.` The small smile. `A blacksmith who has crowned himself in mountains the Throne "
                "has not yet troubled to look at. His envoy brought the mayor an iron badge. The mayor gave him rum.` "
                "He straightens a paper. `I gave him a receipt for the rum. The Throne recognises one crown, and it is "
                "not made of horseshoes.` His eyes come back to you. `The Town Hall would be grateful for the names of "
                "anyone in this town who talks to his bargemen. A silver a name.`",
        },
    },

    # ---- the Moonmoth's captain: she will not go up that river ------------------------------------------------------
    "Captain Aelith": {
        "brief_more": (
            "The Verde (owner, 2026-11-23). The Moonmoth will not go up it: she says it is not water but someone "
            "sleeping, and one does not sail over a sleeper. You go south by the sea."),
        "dialog": {
            "verde|river|green|upriver|kteol|snake|serpent|sleeper":
                "Aelith is quiet a while. `She will not go up that river. I asked her once. She drew in her sails and "
                "would not answer me for a day.` Her pale eyes rest on you. `She says it is not water. It is someone "
                "sleeping. One does not sail over a sleeper.` She looks away, toward the harbour mouth. `We go south, "
                "by the sea, and leave the Green to the ones who feed it.`",
        },
    },
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
