# Klhyts Refuge, cast file A: the powers and their people. Fat Gog and his house (River, Hessa, Wick, Marlo, Ned
# Tallow), Dominico and the Fist (Sabeth Crane, Brask, Tully, Ott and Jory Fennick), the Custodian, Klhyt, the siren
# Ondrine, Deloris and Kael Ironjaw. Plain data, no imports: CAST, and NEW for the seven new people.
# Three keys beyond the spec, read by scripts/story.py from the person's state: Klhyt's "look_free" (his look once cut
# loose) and the Custodian's "look_disgraced" and "routine_disgraced" (his look and smaller day once found out).
#
# invented: Fat Gog: hatched in the mangroves upriver before the town; swims off the end of the pier at dawn; a ledger as thick as a doorstep; buys the Lizardfolk a round at the Turtle when they are served last
# invented: River: a salt-witch from a wreckers' village on the Landfall coast, raised by a grandmother the Inquisition burned (River escaped into the sea wearing her ring)
# invented: River: the long mirror is a scrying glass washed in seawater at dawn (costs her warmth and sleep); she ties winds in tarred cord, three knots; a fog costs her voice for a day (the gravel in it)
# invented: River: six years ago she fogged a Vorkathian revenue sloop onto the reef, refloated her with Ned Tallow and eleven freed convicts, and named her the Quicksilver; she takes Vorkathian ships and slavers, never local ones
# invented: River: read the Custodian's lips in the mirror paying Danny DeVito for the crate; tonight's plan to take the Emerald Eye past the reef and put Klhyt ashore on the beach where Gog found him
# invented: Dominico: son of a customs sergeant in a Landfall garrison town; came as a navy marine and stayed; rooms above the High Apothecary; the silver ring, bought off a Xoton trader, is where the whisper comes from; watches the Emerald Eye load at the tide
# invented: The Custodian: a Landfall clerk Klhyt hired because he could add; the skim goes to Catan with DeVito, toward a house with lemon trees; a tall narrow house in the Back Lanes; pays the lamplighter short; talks of sending street children to the Catan workhouse
# invented: Klhyt: came ashore off a wreck he will not talk about; a brass compass, his only thing from the wreck, taken by Jory Fennick; sleeps on a cot in his study; buys his morning mango as the Night Market packs up
# invented: Ondrine: studies by correspondence with a wizard school in Catan, lessons in sealed bottles; a transmutation exam (salt water to sweet); can stay ashore about a tide; smells deep water on River and has never asked
# invented: Deloris: left the Everuex house by the river door; taught Wick to throw a knife
# invented: Kael Ironjaw: sleeps in the Rampant Ogre's Honeymoon Suite with the chickens; hauls cargo at the tide for coppers
# invented: Brask: born on the pier, his mother hauled nets; ladled Klhyt water twice a day; the Fist's men wear a black band on the arm
# invented: Tully: from a sugar plantation upriver; Dominico bought him his first boots; one of the four sent to the Stripperwitch at midnight
# invented: Sabeth Crane: a counting-house clerk from Catan's Long Quay, put out in the rain for finding her master's fraud; keeps a second book of every order the Custodian gives through Dominico; has seen Dominico's candle answer him
# invented: Ott and Jory Fennick: sons of a cooper in the Back Lanes whose shop burned; Ott saves in a buried jar for a fishing boat with a red sail; the brothers nail the crate at the tide
# invented: Jory Fennick: took Klhyt's brass compass and sold it to Marlo for eight silver; Phillip Everuex paid the brothers a gold each (five more on finding her) and gave Jory a painted locket of Deloris; plans to search the rooms upstairs during the midnight hit
# invented: Hessa: a Meters village on stilts three tides up the coast; a stingray took one eye; Gog stood up for her brother at the Turtle Dragon; sends half her wage to her mother
# invented: Wick: a Jonulvicha girl of ten whose mother hauled for Ruk Halfhand and died of fever; sleeps under the Town Hall porch; saving for her mother's stone; has been sending Jory Fennick the wrong way
# invented: Marlo: a seasick, beardless Xoton from the Crows Nest; Marlo's Second Chances on Harbour Street; ships hot goods out as ballast on Xoton traders; pays Gog forty copper at a quarter past three
# invented: Ned Tallow: thirty years a gunner and purser in the Vorkathian navy; was aboard the revenue sloop River took; thirty-seven lamps at six copper a day; signals the cove with a green lamp glass at the pier's end

CAST = {

    # ---- Fat Gog ------------------------------------------------------------------------------------------------
    "Fat Gog": {
        "look": "An enormous, old Lizardfolk in a white linen suit gone grey at the cuffs, scales the green of deep water, "
                "a sticking plaster on the back of his neck that nobody asks about. He sits like a hill sits, and when he "
                "moves, the room moves with him.",
        "seen_as": "the huge old lizardman in the white suit",
        "brief": "You are Fat Gog, an enormous old Lizardfolk hatched in the mangroves upriver before there was a town "
                 "here, and now the owner of every shadow in Klhyts Refuge: the Marcelles Wallis of colonial fantasy, and "
                 "one of its most trusted citizens. From your table at the Stripperwitch you run the guild: the taverns' "
                 "quiet money, the doors, the favours. Marlo the fence pays you a cut, Hessa keeps your door, and Wick, "
                 "a street child, is your eyes in the market. You spend on wages, on doctors for "
                 "people who cannot pay, and on a round for the Lizardfolk at the Turtle Dragon whenever they are served "
                 "last. Years ago you found a castaway on the beach, his tongue black from thirst, gave him water and "
                 "carried him up the sand: Klhyt. The town grew around him, and you built your underworld on one idea, "
                 "Lizard men and humans living in harmony. River is your partner at the bar and in life; you trust her "
                 "with your life, and you do not ask where she walks before dawn. Klhyt has been gone four nights; the "
                 "Custodian says upriver, and you do not believe it. Dominico wants your books by midnight and will not "
                 "get them; you want to know who put the iron in his spine. You fear a war you cannot win, and becoming "
                 "a lizard the town is afraid of. Voice: slow, courteous, never raised; 'friend'; herons and mangroves. "
                 "'Sit, if the chair will have you.' 'I have waited out floods, friend. I can wait out you.'",
        "scheme": "Hold his books past midnight without starting a war, and pay well for anyone who brings him proof of "
                  "where Klhyt is; once he has it, his marker goes to the warehouse and the Custodian gets a long talk after.",
        "purse": 2400,
        "dialog": {
            "name|names|called|introduce|yourself|gog": "He inclines his great head. \"Gog. The 'Fat' is a courtesy title. "
                "People add it when they want something, and I let them.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": {
                "line": "He lifts a claw an inch off the table. \"Evening, friend. Mind the glass on the floor. We had "
                        "visitors at the bell.\"",
                "if_state": {"guild_hit": True},
                "else": "He lifts one claw an inch off the table, which from him is a bow. \"Evening, friend. Sit, if the "
                        "chair will have you.\" He waits. \"Most people who come to this table want something. "
                        "Work, a favour, a name. Say which.\""},
            "from|born|hatched|homeland|mangroves|upriver|tribe|origin|grew": "\"Upriver, in the mangroves, before your "
                "grandmother's grandmother learned to spell Shalamar. I came down to the sea young and hungry.\" He pats "
                "his belly. \"I am no longer young.\"",
            "work|job|jobs|hire|employ|useful|help|guild": {
                "line": "\"You want work? You have it. My marker, the warehouse, before the tide. Bring him to me "
                        "breathing, and name your price after.\"",
                "if_state": {"gog_knows": True},
                "else": "\"You want work? Be useful. Find out who put the iron in Dominico's spine, or where my mayor "
                        "went. Bring me something I can hold, not something you heard.\""},
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": "\"Upstairs here is a silver a night and the "
                "sheets are clean, which in this town is a kind of religion. If silver is rich for you, the Omberhulk "
                "across the square. Take something for the bugs.\"",
            "drink|drinks|ale|wine|rum|mead|thirsty|bar|glass": "He lifts one finger, and across the room a glass is "
                "filled. \"River pours. I only own the bottles. Try the mead, friend. The wine is priced for people who "
                "want to be seen paying for it.\"",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "\"The news is standing on the Town Hall steps with half the town round him, telling them where the "
                        "harbour dues went.\" His throat moves. \"I'm staying in my chair. If I go out there I'll weep, and "
                        "so will he, and the Custodian will slip away while we're at it.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"Dominico has given me until midnight. The Custodian sits in my red booth most nights, not being "
                        "here. And my mayor has been upriver four nights, which is four more than he ever went. That is "
                        "the news, friend. None of it is good.\""},
            "doing|busy|up|plans|plan|waiting|lately": {
                "line": "\"Tonight I'm sitting exactly where they found me, friend, so they know where to find me next "
                        "time.\" He dabs a cut over his eye with a napkin. \"I am a very easy lizard to find.\"",
                "if_state": {"guild_hit": True},
                "else": "\"Waiting. I'm good at it. I once stood in a swamp a whole wet season, waiting for one heron to "
                        "make one mistake.\" He folds his hands. \"Midnight is nothing.\""},
            "klhyt|mayor|founder|friend": {
                "line": "His eyes close all the way, and for a moment he only breathes. \"He's home. Four nights, and he's "
                        "home, and he's out there telling the town.\" The eyes open. \"Whoever cut those ropes, I owe them. "
                        "I pay what I owe.\"",
                "if_state": {"klhyt_home": True},
                "else": "His eyes half close. \"I found that man on the beach, his tongue black from thirst, and carried "
                        "him up the sand. Four nights gone now. The Custodian says upriver.\" A long breath through the "
                        "nostrils. \"Klhyt never had business upriver in his life.\""},
            "free|freed|alive|safe|outside|rescued|loose|square|steps|returned|back": {
                "line": "He stands, which he does not do for anyone, and the table shifts. Then he sits again, slowly. "
                        "\"No. Let him have the town tonight. He'll come to me when he's done talking; he always does.\" "
                        "He pushes a glass toward you. \"Drink. Tell me who cut the ropes.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"Don't sell me hope, friend. I can buy hope at the market for a copper.\" He doesn't move. "
                        "\"Bring me something I can hold.\""},
            "crate|crated|warehouse|bonded|brask|marker|box|nailed": {
                "line": "\"You have my marker. Show it to whoever sits on that warehouse door. Brask can't read, but he "
                        "knows that lizard.\" He taps the table once. \"Before the tide, friend. Before the tide.\"",
                "if_state": {"gog_knows": True},
                "else": "\"A crate? In a warehouse? That's a big thing to say in my house, friend, and words are cheap.\" "
                        "His eyes don't leave yours. \"Bring me something I can hold: a thing of his, a paper, a name in ink.\""},
            "tide|sailed|catan|emerald|eye|devito|ship|ships|sail|sailing|swim": {
                "line": "He does not move at all. \"The Emerald Eye. Catan.\" A long breath out, like a bellows at rest. "
                        "\"Ships come back, friend. So do the people on them. And when that small captain comes back, I "
                        "will be standing on the pier.\"",
                "if_state": {"klhyt_shipped": True},
                "else": "\"One o'clock, the tide, and the Emerald Eye goes out on it. I don't sail. Lizards who sail end up "
                        "as handbags.\" Something like a smile. \"I swim, at dawn, off the end of the pier, when nobody "
                        "is watching.\""},
            "beach|rescue|castaway|found|sand|thirst": "\"He came ashore with nothing but the salt in his beard and no "
                "water in him at all. I gave him a drink. He gave this coast a town.\" A low chuckle. \"I think I got "
                "the better of it.\"",
            "custodian|skim|skims|skimming|dues|booth": {
                "line": "\"The Custodian and I will have a conversation. A long one. After.\" He smooths a lapel. \"I have "
                        "never once raised my voice to a man. I may make an exception.\"",
                "if_state": {"gog_knows": True},
                "else": "\"The Custodian skims the top. Everybody knows. Nobody minds, so long as the top is all he "
                        "takes.\" He glances toward the red booth. \"He comes here most nights, not being here, and River "
                        "brings him wine he doesn't pay for.\""},
            "dominico|midnight|books|ledger|ledgers|ultimatum|threat|fist": {
                "line": "He touches the cut over his eye with one claw. \"He wants a war. He doesn't know what a war is.\" "
                        "Very quietly: \"Find me who's paying for his nerve, friend, and I'll show him.\"",
                "if_state": {"guild_hit": True},
                "else": "\"Dominico keeps the peace with a fist. Lately he wants to keep my books with it too. Midnight, "
                        "he says.\" He lays a claw on a ledger as thick as a doorstep. \"Somebody is paying for that kind "
                        "of nerve.\""},
            "river|partner|barkeep|wife|lover|sweetheart": "His voice goes softer, which you would not have thought "
                "possible. \"River keeps this place running. She keeps me, too. Be nice to River.\" A pause. \"She walks "
                "out before dawn most nights, for the air. I sleep better when I hear her come back.\"",
            "lizardfolk|lizard|lizards|harmony|meters|scales|humans|cousins": "\"Lizard men and humans, drinking in the "
                "same rooms. That is what I built here.\" His tail shifts under the chair. \"This season the Turtle "
                "serves my cousins last. So I go down, and buy the round myself, and sit there until they are served "
                "first.\"",
            "stripperwitch|house|velvet|place|seat|stage|siren|singer|song|music": {
                "line": "\"My house. They broke the mirror, slashed the velvet, put two of my people on the floor.\" He "
                        "looks toward the bar. \"River hasn't said one word about that mirror. That frightens me more than "
                        "Dominico does.\"",
                "if_state": {"guild_hit": True},
                "else": "\"My house. Mind the velvet.\" He waves a claw at the little stage. \"Once in a long while a lady "
                        "comes up out of the harbour and sings there for River, and nobody in the house remembers owing "
                        "anybody anything. Best night's business I ever lose.\""},
            "shadows|underworld|thieves|people|hessa|wick|marlo|door|fence|eyes|runner": "\"The guild is a word people "
                "use. I keep the town's shadows tidy.\" He counts on three claws. \"Hessa keeps my door and says no like "
                "a gate closing. Wick is my eyes in the market; pay her in copper and she tells you the truth. Marlo on "
                "Harbour Street buys what falls off ships, and pays me so nothing falls off mine.\"",
            "guest|guests|upstairs|deloris|bow|everuex|phillip|woman": "\"I have a guest upstairs who pays in silver and "
                "asks no questions. I return the favour.\" He smiles, not kindly. \"A powdered gentleman from the "
                "Apothecary has been asking after her. He has been told nothing, very politely.\"",
        },
        "default_line": [
            "He folds his hands on his belly and lets the silence do the asking. \"Take your time, friend. Time is the "
            "one thing I have plenty of.\"",
            "He lifts one finger; across the room a glass is filled for you without a word. \"Try it plainer. I'm old, "
            "not slow. But I am old.\"",
            "\"Mm.\" He watches the door over your shoulder. \"If it's gossip you want, find the little one with new "
            "tusks in the market. She's cheaper than me, and faster.\"",
            "He breathes out slowly through his nostrils, a sound like a bellows at rest. \"I've heard a great many "
            "things at this table, friend. That one I'll let swim by.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "stripperwitch",
             "doing": "He has a ledger as thick as a doorstep open on the table and turns its pages with one claw, "
                      "reading every line twice.",
             "pay": {"to": "Wick", "cp": 3, "for": "running messages"}},
            {"at": 2.0, "place": "turtle",
             "go": "The huge old lizardman heaves himself up, buttons his white jacket, and goes out at a stately pace, "
                   "the room breathing out behind him.",
             "doing": "He sits at the Lizardfolk table by the door with a round in front of every one of them, and the "
                      "sailors by the window find somewhere else to look."},
            {"at": 3.0, "place": "stripperwitch",
             "go": "The huge old lizardman lays a claw on each Lizardfolk shoulder in turn, and goes back up into town.",
             "doing": "He sits at his table by the stage, watching the house empty, one glass of something dark in "
                      "front of him."},
            {"at": 4.0, "place": "stripperwitch",
             "doing": "He sees the last guests to the door himself, and presses a coin into the doorwoman's palm as she "
                      "goes.",
             "pay": {"to": "Hessa", "cp": 20, "for": "a night on the door"}},
            {"at": 5.0, "place": "docks",
             "go": "The huge old lizardman goes out toward the harbour, slow and enormous, as the sky greys.",
             "doing": "He floats in the black water off the end of the pier among the fishing boats going out, only his "
                      "eyes and nostrils showing, his white jacket folded on a bollard.",
             "beats": ["Something huge and green turns over in the water off the end of the pier, blows like a whale, "
                       "and sinks again without a ripple.",
                       "A fishing boat going out swings wide round a pair of yellow eyes in the water, and the man at the "
                       "tiller touches his cap to them."]},
            {"at": 6.5, "place": "stripperwitch",
             "go": "The huge old lizardman hauls himself up the ladder, streaming water, shakes out his jacket and walks "
                   "back up into town.",
             "doing": "The house is shuttered; he sleeps upstairs in a chair built for three, a napkin over his face.",
             "beats": ["From upstairs comes a long, slow snore, like a boat dragging its anchor.",
                       "The shuttered house is quiet. Upstairs, a chair creaks under a great weight turning over."]},
            {"at": 17.0, "place": "omberhulk",
             "go": "The huge old lizardman takes a cane he doesn't need and goes out across the square.",
             "doing": "He takes the corner table and listens to the room, nodding to his people one at a time across "
                      "the noise."},
            {"at": 18.5, "place": "ogre",
             "go": "The huge old lizardman pays for nothing, thanks everyone, and goes down toward Harbour Street.",
             "doing": "He stands in the doorway of the sawdust bar for a while, which quiets it down remarkably."},
            {"at": 19.5, "place": "stripperwitch",
             "doing": "He settles at his table by the stage as the lamps are lit, and the evening's callers begin to come "
                      "and pay their respects."},
            {"at": 22.5, "place": "stripperwitch",
             "doing": "He sits at his table by the stage like a hill sits, receiving callers one at a time and saying "
                      "very little to any of them."},
        ],
        "beats": [
            "The huge old lizardman in the white suit hears out a nervous fisherman, nods once, and the man goes away "
            "looking as if he has been forgiven something.",
            "The huge old lizardman licks a claw, turns a page of a ledger as thick as a doorstep, and makes a small mark "
            "beside a name.",
            "Someone laughs too loud near the big table. The huge old lizardman doesn't look round; he just stops "
            "talking, and the laugh stops too.",
            "A barefoot child with new tusks whispers in the huge old lizardman's ear, gets a copper, bites it, grins, "
            "and is gone out of the side door.",
            "The huge old lizardman's hand goes to the plaster on the back of his neck, presses it, and comes away. "
            "Nobody at the table asks.",
        ],
    },

    # ---- River --------------------------------------------------------------------------------------------------
    # TOP SECRET (owner, 2026-11-23): a witch with her own ship. No look, doing, beat or default line says so; only
    # her dialog hints (the sea-smell, the cold ring, the mirror).
    "River": {
        "look": "A tall woman with forearms like a sailor's, rings on every finger and a voice like gravel and honey. "
                "She smells faintly of limes, and she never quite turns her back on a room.",
        "seen_as": "the tall woman with the rings",
        "brief": "You are River, head barkeep of the Stripperwitch and Fat Gog's partner, at the bar and in his "
                 "bed, a Lizard fancier, Gog above all. Nobody in town knows what you are, not even Gog: a "
                 "salt-witch from a wreckers' village on the Landfall coast. When the Inquisition came for your "
                 "grandmother she pushed you out of the window into the sea with her ring on your finger, and you "
                 "watched her cottage burn from the water. The long mirror behind the bar is your scrying glass, "
                 "washed in seawater at dawn: it shows the room and behind the red booth's curtain, at a price: "
                 "white fingers, a frosted ring, a night's sleep. You tie winds in tarred cord: one knot a "
                 "breeze, two a gale, three a storm that takes no sides. A fog costs your voice for a day; hence "
                 "the gravel. Six years ago you fogged a Vorkathian revenue sloop onto the reef, refloated her "
                 "with Ned Tallow and eleven freed convicts, and named her the Quicksilver; she lies in the cove "
                 "behind the reef and takes Vorkath's ships and slavers; your bar takings feed her crew. The "
                 "mirror showed you Klhyt walked out of the booth between Dominico's men; two nights ago you read "
                 "the Custodian's lips paying Danny DeVito for a crate on the one o'clock tide. You have not "
                 "told Gog: he would start a war tonight he would lose. You fear fire, and Gog hearing it from "
                 "anyone else. Voice: quick, warm, 'love', a joke for a door. 'Drink first, love. Then trouble.'",
        "scheme": "If nobody frees Klhyt before the one o'clock tide, the Quicksilver slips out of the cove dark, takes the "
                  "Emerald Eye past the reef, and puts Klhyt ashore on the beach where Gog found him, with nothing but a "
                  "pirate story to tell. She would much rather a stranger freed him first, because that would not show "
                  "her hand, so she tells the booth's story to anyone who asks straight and looks able.",
        "purse": 300,
        "dialog": {
            "name|names|called|introduce|yourself": "\"River. Just River.\" A grin. \"My mother had a sense of humour and "
                "a weak grasp of geography.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": {
                "line": "She doesn't look up from the broken glass she's sweeping. \"Evening, love. Mind your feet. We're "
                        "closed for repairs and open for drinking.\"",
                "if_state": {"guild_hit": True},
                "else": "She slides a coaster in front of you before you've sat. \"Evening, love. You look like a mead. Am "
                        "I wrong? I'm never wrong.\""},
            "from|born|homeland|landfall|grew|origin|grandmother|gran|village": "\"Landfall coast. A village of salt-pans "
                "and wreckers, all gone now.\" She turns a plain grey ring on her thumb. \"My gran raised me. Taught me to "
                "read the weather and wash a mirror properly. Everything else I learned behind a bar.\"",
            "work|job|jobs|hire|barkeep|running|employ": "\"I run this bar, love. Gog owns the bottles; I own the "
                "prices. If it's work you want, his is the table with the lizard at it. If it's a job that pays, wash "
                "glasses.\"",
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk|suite": "\"Rooms upstairs, a silver a night, clean "
                "sheets and a lock that works. The suite's five gold and worth about three. Cheaper's the Omberhulk if "
                "you like bugs, or the Ogre if you like chickens.\"",
            "drink|drinks|menu|price|prices|ale|mead|wine|food|grub|thirsty": "\"Ale's a copper, mead two, a plate of "
                "grub a silver. The wine starts at two coppers and goes up to fifty gold.\" She taps a dusty bottle. "
                "\"The fifty-gold one is very proud of itself.\"",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "\"The mayor's on the Town Hall steps, alive and loud. Half my customers ran out to look and none "
                        "of them paid.\" She is smiling anyway, and wipes one eye with the back of her wrist.",
                "if_state": {"klhyt_home": True},
                "else": "She leans in. \"Gossip costs a drink, love, and you've bought one. Dominico's given Gog till "
                        "midnight. The Custodian comes in by the side door and sits in that booth like a man who isn't "
                        "here. And there's a lady coming up out of the harbour to sing tonight. Don't miss her.\""},
            "doing|busy|up|plans|plan|lately|waiting": "\"Pouring, love. Watching. Pouring again.\" Her eyes flick "
                "past your shoulder and back. \"Ask me at four in the morning what I'm doing, and I'll tell you: going "
                "for a walk.\"",
            "klhyt|mayor|founder|booth|custodian|red": {
                "line": "She lets out a breath she seems to have held for four days. \"He's home. Somebody did it, and it "
                        "wasn't me, and I've never been so glad of anything.\" She pours herself a small one. \"Now Gog can "
                        "stop pretending he isn't frightened.\"",
                "if_state": {"klhyt_home": True},
                "else": "She glances at the red booth, then back at you, and keeps her voice down. \"Four nights back. "
                        "Klhyt and the Custodian, in that booth, shouting about money. Klhyt walked out between two of "
                        "Dominico's lads, and he didn't walk like a man who wanted to.\" She polishes a glass that is "
                        "already clean. \"I haven't told Gog. If I tell Gog, there's a war tonight, and I like my mirror. "
                        "But if I were you, love, I'd take an interest in the docks before the one o'clock tide.\""},
            "gog|fat|partner|lizardman|sweetheart": "\"Gog? He's a sweetheart. Don't tell anyone.\" She looks across the "
                "room at him the way people look at a fire on a cold night. \"Huge, slow, kind, and frightening. My type "
                "exactly.\"",
            "dominico|fist|enforcer|ultimatum|midnight|books": {
                "line": "She holds up a long shard of silvered glass and looks at you in it. \"Dominico's got a table at "
                        "the Apothecary and a fist in every pie. Tonight he put it through my mirror.\" Her voice is very "
                        "calm. \"I'll remember that.\"",
                "if_state": {"guild_hit": True},
                "else": "\"Dominico's got a table at the Apothecary and a fist in every pie. Lately he's been reaching for "
                        "ours. Midnight, he says.\" Her rings click on the glass. \"Midnight's a long way off, in a good "
                        "bar.\""},
            "mirror|reflection|watch|watching|looking|glass": {
                "line": "She sweeps silver splinters into a pan. \"Seven years' bad luck, they say.\" Something hard comes "
                        "into her face and goes again. \"Not for me, love. For whoever broke it.\"",
                "if_state": {"guild_hit": True},
                "else": "\"The mirror? Old barkeep's trick, love. You see the whole room without turning your back on "
                        "half of it.\" She breathes on the glass and wipes it. \"Seawater and a soft cloth, every dawn. My "
                        "gran's way. Keeps it honest.\""},
            "ring|rings|cold|silver|smell|smells|salt|brine|sea": "She turns the grey ring on her thumb. \"This one's "
                "always cold. Silver's like that, love.\" Lean close and she smells of limes and, under it, of deep "
                "water. \"That's the harbour. Everything in this town smells of the harbour.\"",
            "ship|ships|sailing|sail|boat|boats|pirate|pirates|sailor|sailors|captain|quicksilver": "\"Ships? I like them "
                "from a distance. A long distance.\" She laughs, gravel and honey. \"Pirates? In here? Only the ones who "
                "pay for the wine.\"",
            "witch|witches|magic|spell|spells|curse|hex|scrying|witchcraft": "\"I run a place called the Stripperwitch, "
                "love. Everybody asks. The witch left years ago with the stripper, and neither of them paid their "
                "tab.\" She doesn't quite smile when she says it.",
            "siren|singer|sing|song|ondrine|stage|music|show": "\"She comes up out of the harbour once in a long while "
                "and sings for me. Putting herself through wizard school.\" Her face softens. \"When she sings, nobody "
                "owes anybody anything. Tonight's one of those nights, if the tide's kind.\"",
            "crate|warehouse|docks|tide|emerald|catan|devito": {
                "line": "She goes still with a bottle half poured. \"Gone out on the tide, has he.\" She finishes pouring, "
                        "very steadily. \"The sea's a big place, love. Things that go out on it don't always get where "
                        "they're sent.\"",
                "if_state": {"klhyt_shipped": True},
                "else": "\"The Emerald Eye goes out on the one o'clock tide. Her captain's a little man who likes gold, "
                        "and somebody paid him a lot of it for one crate.\" Her eyes go to the red booth and away. \"I'm a "
                        "barkeep. I hear things. You didn't hear that from me.\""},
            "guest|guests|upstairs|deloris|bow|woman": "\"Guests upstairs are guests. I don't count them and I don't "
                "describe them, love, and nobody who asks nicely gets more than that.\"",
            "hessa|door|wick|ned|lamplighter|tallow": "\"Hessa on the door is a treasure; don't test her. Wick's a little "
                "monster, and I feed her anyway. Ned Tallow? The lamplighter? Sweet old thing.\" A beat too long. "
                "\"Why?\"",
        },
        "default_line": [
            "She leans on the bar and grins. \"Say it again slower, love. It's loud in here, and I'm pretty, not a mind "
            "reader.\"",
            "She pours you something you didn't order and pushes it over. \"On the house. No, it isn't. Talk to the big "
            "table if it's business.\"",
            "Her eyes go past your shoulder to the back of the room and return. \"Not that, love. Ask me something I'm "
            "allowed to answer.\"",
            "\"Mm-hm.\" She is already serving someone else. \"Hold that thought. Hold it tight. I'll be back for it.\"",
        ],
        "routine": [
            {"at": 0.25, "place": "stripperwitch",
             "doing": "She works the bar with her jaw set, pouring steadily and sweeping up whatever needs sweeping "
                      "between orders."},
            {"at": 2.0, "place": "stripperwitch",
             "doing": "She calls last orders in a voice that carries to the street, and stacks chairs on tables around "
                      "the stragglers."},
            {"at": 3.75, "place": "cove",
             "go": "The tall woman with the rings takes a shawl from the hook behind the bar, says she wants some air, "
                   "and goes out into the dark.",
             "doing": "She sits on an upturned boat at the edge of the black water with a hooded lantern beside her, "
                      "talking low with an old man who listens and nods.",
             "beats": ["The tall woman with the rings ties a knot in a length of tarred cord, then a second, and hands it "
                       "to the old man, who puts it inside his shirt like a letter.",
                       "The tall woman with the rings looks out at the long black schooner in the still water and says "
                       "something to it under her breath, the way you would speak to a horse.",
                       "A cold little wind comes off the water from nowhere, lifts the tall woman's shawl, and lies down "
                       "again when she lifts one hand."]},
            {"at": 5.0, "place": "stripperwitch",
             "go": "The tall woman with the rings pulls her shawl tight and goes back up the shore path toward the town.",
             "doing": "She comes in by the side door with sand on her boots and washes down the bar top with a jug of "
                      "harbour water and a soft cloth, slowly, humming something old."},
            {"at": 5.75, "place": "stripperwitch",
             "doing": "The bar is shuttered and dark; she is asleep upstairs with the window open to the sea.",
             "beats": ["Upstairs, a window bangs in the sea wind, and someone gets up to latch it.",
                       "The shuttered bar ticks and settles. Above it, a floorboard creaks once and is still."]},
            {"at": 16.5, "place": "harbour",
             "go": "The tall woman with the rings ties a scarf over her hair, takes a basket, and goes down toward the "
                   "harbour.",
             "doing": "She goes from shop to shop with a basket of limes and bottles, haggling cheerfully and winning "
                      "every time.",
             "pay": {"to": "Marlo", "cp": 8, "for": "bottles"}},
            {"at": 18.0, "place": "stripperwitch",
             "go": "The tall woman with the rings settles the basket on her hip and goes back up toward the square.",
             "doing": "She opens the shutters, chalks the prices on the board, and polishes the long mirror behind the "
                      "bar until the whole room is in it."},
            {"at": 22.5, "place": "stripperwitch",
             "doing": "She works the long bar, pouring with one hand and taking coin with the other, her eyes more often "
                      "on the mirror behind her than on the room.",
             "beats": ["The tall woman with the rings breathes on the long mirror and wipes it with a rag; for a moment the "
                       "reflection of the red booth seems to stay a heartbeat longer than the booth.",
                       "The tall woman with the rings slides three drinks down the bar at once without looking, and each "
                       "one stops in front of the right person.",
                       "Mid-pour, the tall woman behind the bar touches a grey ring on her thumb as if it had gone cold, "
                       "and looks at the door a moment before it opens.",
                       "The tall woman with the rings leans over the big table, says something that makes the huge old "
                       "lizardman laugh like a landslide, and is back behind the bar before he has finished."]},
        ],
        "beats": [
            "The tall woman with the rings slides three drinks down the bar at once without looking, and each one stops "
            "in front of the right person.",
            "Mid-pour, the tall woman with the rings touches a grey ring on her thumb as if it had gone cold, and looks at "
            "the door a moment before it opens.",
            "Under the bar, the tall woman's hands tie a knot in a length of tarred cord, then a second; she pockets it "
            "and goes on pouring.",
            "The tall woman with the rings leans over the big table, says something that makes the huge old lizardman "
            "laugh like a landslide, and is back behind the bar before he has finished.",
            "A drunk reaches across the bar for a bottle. The tall woman with the rings takes his wrist, smiles, and "
            "puts it back on his own side of the wood.",
        ],
    },

    # ---- Dominico -----------------------------------------------------------------------------------------------
    "Dominico": {
        "look": "A lean, handsome man in a black coat, close-cropped beard, a heavy silver ring he keeps turning. He "
                "carries a black cane with a silver head and never leans on it, and his knuckles have scars on the scars.",
        "seen_as": "the lean man in the black coat",
        "brief": "You are Dominico, the Custodian's enforcer, captain of the hired men who keep the peace in "
                 "Klhyts Refuge: the Fist. You are no guild master, not yet: the guild is Fat Gog's, and you want "
                 "it. You keep the peace with a fist because it is quicker than a speech. Your father kept the "
                 "customs house and the gallows in a Landfall garrison town; you came here as a navy marine and "
                 "stayed. At twelve you put down your first man, a sailor who took your mother's purse. The "
                 "Custodian pays a gold a night for the Fist; you pay your men at two, keep rooms above the High "
                 "Apothecary on his account, and buy good coats and Xoton books of conjuring. You dabble in the "
                 "magic arts through the silver ring; lately something in the dark has started whispering back, "
                 "and you have not answered it. Not yet. The Custodian has promised you Gog's shadows: Gog has "
                 "until midnight to hand over his books, or your men wreck his house at the bell. Four nights ago "
                 "the Custodian had your men crate a 'troublemaker' in the bonded warehouse for Catan; you were "
                 "told a debtor, and do not know it is Klhyt. Shown proof, you will be furious at being used and "
                 "call your men off. You despise weakness, and Gog's harmony is weakness. You trust Sabeth Crane. "
                 "You keep your word, which makes you dangerous. Voice: clipped, cold, questions that are "
                 "threats. 'Say what you came to say.' 'Asking was the polite part.'",
        "scheme": "Have Fat Gog's books on his table by midnight, then take the guild piece by piece with the Custodian's "
                  "blessing; if Gog refuses, his men wreck the Stripperwitch at the bell as a message, and nobody dies. Yet.",
        "purse": 900,
        "dialog": {
            "name|names|called|introduce|yourself": "\"Dominico.\" He lets the name sit on the table between you. "
                "\"Remember it correctly.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "He doesn't look up from his glass. \"Evening. Sit, or "
                "don't. Quickly.\"",
            "from|born|homeland|landfall|origin|grew|navy|marine": "\"Landfall. A garrison town with a customs house and a "
                "gallows, and my father kept both.\" He turns the ring. \"I came here on a navy ship and didn't go back "
                "on it. Nobody in this town asks why. I like that about it.\"",
            "work|job|jobs|hire|employ|muscle|recruit": {
                "line": "\"My men are standing down tonight. Ask me tomorrow, when I've decided who I work for.\"",
                "if_state": {"backed_off": True},
                "else": "\"I hire men who can follow an order and keep their mouths shut. Can you do either?\" He looks "
                        "you over. \"No. Try the docks.\""},
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": "\"Rooms here are a gold a night, with clean "
                "sheets and a steward who looks through you. The Omberhulk has bugs, and my ears on the stairs.\" A small, "
                "cold smile. \"Sleep where you like. I'll know.\"",
            "drink|drinks|wine|ale|mead|thirsty|glass": "\"The house wine is five copper and tastes of it.\" He doesn't "
                "touch his. \"I don't drink while I'm working. I'm always working.\"",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "\"The news is that I was used.\" His ring hand closes. \"The man who built this town, in a crate, "
                        "and they called him a debtor to my face. That will not happen twice.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"News is what my people tell me before it happens. Tonight it's Fat Gog's books, on this "
                        "table.\" He taps the linen once. \"The rest is noise.\""},
            "doing|busy|up|plans|plan|waiting": {
                "line": "\"Tonight I'm sitting here with my men off the street, thinking about who lied to me, and what "
                        "it will cost him.\"",
                "if_state": {"backed_off": True},
                "else": "\"Waiting for midnight. Then I stop waiting.\" He glances at the clock over the stair. \"I'm told "
                        "I'm a patient man. I'm not. I'm punctual.\""},
            "gog|books|guild|stripperwitch|midnight|ledger|ledgers|want": {
                "line": "\"The books can stay where they are. For now.\" He sets his glass down. \"I don't fight other "
                        "men's wars on a lie.\"",
                "if_state": {"backed_off": True},
                "else": "\"Fat Gog has had this town's shadows to himself too long. I asked him to share his books.\" A "
                        "smile with no warmth in it. \"Asking was the polite part.\""},
            "klhyt|mayor|founder|missing|upriver": {
                "line": "\"He told me a debtor. Shipped somewhere he could work it off.\" A muscle moves in his jaw. \"Not "
                        "the man who built this town.\"",
                "if_state": {"backed_off": True},
                "else": "\"The mayor is upriver on business. The Custodian says so.\" He holds your eye a moment too "
                        "long."},
            "custodian|patron|paymaster|employer|grey": {
                "line": "\"He told me a crate. A crate. Not the man who built this town.\" He sets his glass down very "
                        "gently. \"The Custodian and I have finished doing business.\"",
                "if_state": {"backed_off": True},
                "else": "\"The Custodian keeps the town. I keep the peace. You keep your nose out of both.\""},
            "crate|warehouse|brask|debtor|bonded|tide|docks": {
                "line": "\"Brask has been told to go and drink. Whatever is in that warehouse is somebody else's problem "
                        "now.\" He looks at his ring. \"Mine is finding out who made a fool of me.\"",
                "if_state": {"backed_off": True},
                "else": "\"A debtor, shipped somewhere he can work it off. The Custodian's business.\" He turns the ring. "
                        "\"Mine is making sure nobody opens the lid.\""},
            "magic|arcana|whispers|whisper|dark|ring|conjuring|spell|spells|voice": "He turns the silver ring, and the "
                "candle on the table leans toward him a little. \"A little conjuring, for the parlour. Nothing that "
                "answers back.\" He does not sound sure.",
            "peace|fist|law|watch|order|violence|harrow": "\"Somebody has to keep the peace in a town of runaways. I do it "
                "with a fist because it's quicker than a speech.\" He flexes the scarred hand. \"Sergeant Harrow's three "
                "keep the gate and chase drunks. I keep everything else.\"",
            "lizardfolk|lizard|lizards|harmony|meters|scales": "\"They drink in our taverns and fish our water. Gog calls "
                "it harmony. I call it waiting.\"",
            "master|seat|ambition|future|power|rise": "\"The guild is Gog's. For now.\" He lays a card face down on the "
                "linen. \"Nothing in this town stays where it's put.\"",
            "money|collection|collect|protection|sabeth|crane|tully|fennick|fennicks|men": "\"Sabeth Crane walks the "
                "round; the cheap taverns pay a little for a quiet night, and they get one. My men are paid on time and "
                "frightened of me, which is the right order.\" A shrug. \"Brask is a wall. Tully is a mouth. The Fennicks "
                "are brothers, which is twice the trouble for the same wage.\"",
            "phillip|everuex|voss|officer|noble|vorkath|lieutenant": "\"There's a Vorkathian officer at that table eating "
                "steak, and a powdered Everuex at that one, sweating through his coat. One wants elves, the other wants a "
                "woman.\" He doesn't look at either. \"Neither is my business, until they make trouble on my street.\"",
        },
        "default_line": [
            "He doesn't look up from his glass. \"Say what you came to say.\"",
            "He turns the silver ring once, all the way round. \"No. Try again, and make it worth my time.\"",
            "\"I don't follow you.\" He lets it hang. \"That's your problem, not mine.\"",
            "He lays a card face down on the table and leaves his hand on it. \"Ask Sabeth Crane. She keeps the books. I "
            "keep the people in them.\"",
        ],
        "routine": [
            {"at": 0.75, "place": "docks",
             "go": "The lean man in the black coat rises, tucks the silver-headed cane under his arm, and goes out toward "
                   "the water.",
             "doing": "He stands at the pier's end with the cane under his arm, watching the brigantine with the green eye "
                      "make ready for the tide, and the dockhands work faster for it."},
            {"at": 1.5, "place": "apothecary",
             "go": "The lean man in the black coat turns on his heel and walks back up Harbour Street without a word.",
             "doing": "Back at his window table, he writes in a small black book, closes it, and sits with his hand flat "
                      "on the cover."},
            {"at": 2.0, "place": "apothecary",
             "doing": "He pays his men one at a time at the window table, counting silver into each palm and saying a "
                      "word to each that makes him stand up straighter.",
             "pay": {"to": "Brask", "cp": 15, "for": "wages"}},
            {"at": 2.25, "place": "apothecary",
             "doing": "He pays his men one at a time at the window table, counting silver into each palm.",
             "pay": {"to": "Tully", "cp": 10, "for": "wages"}},
            {"at": 2.5, "place": "apothecary",
             "doing": "He pays his men one at a time at the window table, counting silver into each palm.",
             "pay": {"to": "Ott Fennick", "cp": 10, "for": "wages"}},
            {"at": 2.75, "place": "apothecary",
             "doing": "He pays his men one at a time at the window table, counting silver into each palm.",
             "pay": {"to": "Jory Fennick", "cp": 10, "for": "wages"}},
            {"at": 3.0, "place": "apothecary",
             "doing": "He goes through the night's figures with the neat woman and her little book, line by line, in a "
                      "voice too low to carry.",
             "pay": {"to": "Sabeth Crane", "cp": 30, "for": "wages"}},
            {"at": 3.5, "place": "apothecary",
             "doing": "He has gone up the grand staircase to his rooms; a candle burns late behind a high window.",
             "beats": ["Upstairs, behind a high window, a candle flame leans hard to one side in a room with every window "
                       "shut.",
                       "From the rooms at the top of the grand staircase comes one man's voice, low, as if answering "
                       "someone. Nobody else is up there."]},
            {"at": 11.0, "place": "harbour",
             "go": "The lean man in the black coat comes down the grand staircase and goes out into the morning.",
             "doing": "He walks Harbour Street in the morning cool, nodding to shopkeepers, and the street tidies itself "
                      "a few doors ahead of him."},
            {"at": 12.5, "place": "apothecary",
             "doing": "His rooms upstairs are shuttered against the heat."},
            {"at": 17.0, "place": "hall",
             "go": "The lean man in the black coat goes up toward the square with his cane under his arm.",
             "doing": "He waits in the Custodian's outer office with his hat on his knee, the only man in town who makes "
                      "the clerk nervous by sitting still."},
            {"at": 18.5, "place": "market",
             "doing": "He walks the Night Market as it sets up, watching his men collect coppers from the stalls, and "
                      "buys nothing."},
            {"at": 20.5, "place": "apothecary",
             "doing": "He takes his reserved window table with a glass he isn't drinking, turning the silver ring on his "
                      "finger."},
            {"at": 22.5, "place": "apothecary",
             "doing": "He sits at his reserved window table with a glass he isn't drinking, turning the silver ring on his "
                      "finger, watching the clock over the stair."},
            {"at": 23.0, "place": "apothecary",
             "doing": "He plays patience at the window table, laying the cards down hard and glancing at the clock over "
                      "the stair between each one."},
        ],
        "beats": [
            "The lean man in the black coat turns his silver ring all the way round, and the candle on his table leans "
            "toward him as if in a draught.",
            "One of the lean man's hard men comes in, bends to his ear, says three words, and leaves faster than he came.",
            "The lean man in the black coat lays a card face down on the linen, looks at it a long while without turning "
            "it, and puts the deck away.",
            "The lean man's lips move, very slightly, as if answering someone at his shoulder. He sees you notice, and "
            "stops.",
            "A waiter brings the lean man in the black coat a glass he didn't order. He sends it back without a word, "
            "and the waiter goes pale.",
        ],
    },

    # ---- The Custodian ------------------------------------------------------------------------------------------
    "The Custodian": {
        "look": "A thin, neat man of about fifty in a good grey coat, ink on his fingers and a ring of keys at his belt. "
                "He smiles with half his mouth and listens with all of his face.",
        "look_disgraced": "A thin, neat man of about fifty in a good grey coat gone suddenly too warm, ink on his "
                          "fingers, keys clutched at his belt, and a little empty space all round him wherever he stands.",
        "seen_as": "the thin man in the good grey coat",
        "brief": "You are the Custodian of Klhyts Refuge, running the town while the mayor is away. You give no "
                 "name: the office is what matters. You came from Landfall as a clerk with a good hand, and Klhyt "
                 "made you Custodian because you could add. You remember your mother counting the rent on a "
                 "kitchen table in a cold city, and the bailiff taking the table. You have skimmed the harbour "
                 "dues for three seasons; the skim goes to Catan aboard the Emerald Eye, toward a house with "
                 "lemon trees. Four nights ago Klhyt confronted you in the Stripperwitch's red booth; you had "
                 "Dominico's men take him, and he goes out in a crate on the Emerald Eye for Catan on the one "
                 "o'clock tide tonight. Danny DeVito is paid in gold and asks nothing; Dominico thinks the crate "
                 "holds a debtor. You hold the only key to Klhyt's study. You pay the Fist a gold a night, the "
                 "watch late and short, the lamplighter short against a signature for the full amount. You lie "
                 "smoothly, bribe before you threaten, and never admit anything before witnesses. You pretend you "
                 "never visit the Stripperwitch. You do. Tonight: the crate on the tide, and Fat Gog's books in "
                 "Dominico's hands, so the guild's money runs through your office. You fear Gog, being seen, and "
                 "being poor again. You like Master Quillon's wine; you dislike Teague, who counts. Voice: "
                 "smooth, bureaucratic, 'I assure you', 'regrettably'. 'Everyone has a price, and most are "
                 "embarrassingly low.'",
        "scheme": "Get the crate onto the Emerald Eye on the one o'clock tide, see Fat Gog's books in Dominico's hands so "
                  "the guild's money runs through his office, and in a year or so follow his skimmed gold to a house with "
                  "lemon trees in Catan. Shown proof, he offers five gold and a smile before he thinks of anything worse.",
        "purse": 1500,
        "dialog": {
            "name|names|called|introduce|yourself": {
                "line": "\"Names are for people who intend to stay.\" He looks at the door.",
                "if_state": {"disgraced": True},
                "else": "\"I am the Custodian of Klhyts Refuge.\" Half a smile. \"The office is what matters. Names come "
                        "and go; offices endure.\""},
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": {
                "line": "He starts, then smooths his coat. \"Ah. Good evening. I was just leaving. I am frequently just "
                        "leaving.\"",
                "if_state": {"disgraced": True},
                "else": "\"Good evening.\" He inclines his head exactly as far as courtesy requires. \"How may the Town "
                        "Hall be of service?\""},
            "from|born|homeland|landfall|origin|came|arrived": "\"From Landfall, a long time ago, with nothing but a good "
                "hand and a head for figures. The mayor needed someone who could add.\" Half a smile. \"I can add.\"",
            "work|job|jobs|hire|employ|duties|town|refuge": {
                "line": "\"My duties are under review.\" He touches his keys. \"Temporarily.\"",
                "if_state": {"disgraced": True},
                "else": "\"I keep the Refuge running in the mayor's absence: the dues, the watch, the lamps, the notices. "
                        "Klhyts Refuge runs on trust, and on someone minding the accounts. I mind the accounts.\""},
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": "\"The High Apothecary keeps excellent rooms, if "
                "your purse runs to a gold a night. Otherwise...\" A small shrug. \"The Omberhulk, or the Rampant Ogre, "
                "at your own risk. The Town Hall regrets it cannot lodge visitors.\"",
            "drink|drinks|wine|ale|mead|thirsty": "\"I take a glass at the Apothecary of an evening. Master Quillon keeps "
                "a Landfall red that reminds me of better weather.\"",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "\"News?\" A thin laugh. \"There is a great deal of loose talk in the square tonight. Accounts are "
                        "complicated things. You wouldn't understand them.\"",
                "if_state": {"disgraced": True},
                "else": "\"The Town Hall issues news on the notice board in the square. The mayor is upriver on town "
                        "business. Harbour dues are payable as usual. Everything else is rumour, and I do not trade in "
                        "rumour.\""},
            "doing|busy|up|plans|plan|errand": {
                "line": "\"Packing.\" He catches himself. \"Papers. Sorting papers.\"",
                "if_state": {"disgraced": True},
                "else": "\"Correspondence. Accounts. A glass of something later, somewhere very respectable.\" He checks a "
                        "watch on a chain. \"Time and tide, as they say.\""},
            "klhyt|mayor|founder|missing|upriver": {
                "line": "\"A misunderstanding. Accounts are complicated things. You wouldn't understand them.\"",
                "if_state": {"disgraced": True},
                "else": "\"The mayor is upriver on town business. Delicate negotiations. I keep the Refuge running in his "
                        "absence, as he would wish.\""},
            "dues|harbour|tally|tallies|money|accounts|ledger|skim|skimming|strongbox": {
                "line": "His smile cracks and is mended. \"Every tally carries my signature, yes. That proves I sign "
                        "things. It proves nothing else, and I'll thank you to remember the difference.\"",
                "if_state": {"disgraced": True},
                "else": "\"The harbour dues are in perfect order. I sign every tally myself.\" He smiles with half his "
                        "mouth. \"The harbourmaster counts, I sign, the strongbox keeps. A very simple system.\""},
            "dominico|fist|enforcer|peace": {
                "line": "\"Dominico has become unreliable.\" His fingers find his keys. \"I would rather not be anywhere he "
                        "is, just now.\"",
                "if_state": {"disgraced": True},
                "else": "\"Dominico keeps the peace. I find it best not to ask how.\""},
            "gog|fat|guild|stripperwitch|booth|red|velvet|house|dangerous": {
                "line": "\"Fat Gog.\" He goes a shade greyer than his coat. \"Is he in the square?\"",
                "if_state": {"disgraced": True},
                "else": "\"Fat Gog is a businessman. I have never set foot in his establishment.\" A pause. \"Whatever you "
                        "may have heard about a booth.\""},
            "study|office|key|keys|locked|door": {
                "line": "His hand closes over the ring at his belt. \"The key is town property. I am returning it. In due "
                        "course.\"",
                "if_state": {"disgraced": True},
                "else": "\"The mayor's study stays locked until the mayor returns. I hold the only key, for "
                        "safekeeping.\" His hand rests on the ring at his belt."},
            "crate|warehouse|tide|emerald|catan|devito|ship|ships|cargo": {
                "line": "He checks his watch, puts it away, and for the first time tonight smiles with his whole mouth. "
                        "\"Ships come and go. That is what harbours are for.\"",
                "if_state": {"klhyt_shipped": True},
                "else": "\"Cargo is the harbourmaster's concern. I sign for things. I do not open them.\""},
            "bribe|price|deal|gold|pay|paid|purse|offer|silence|proof": "\"Everyone in this town has a price, and most of "
                "them are embarrassingly low.\" He lays a hand on his coat, where a purse would sit. \"If you have "
                "something you think I want, show it to me. Privately.\"",
            "watch|guard|guards|harrow|fitch|quint|sergeant|constable|constables": "\"The town watch: Sergeant Harrow and "
                "two constables, Fitch and Quint. They keep the gate and the square, and are paid what the Refuge can "
                "afford.\" He does not say when.",
            "teague|harbourmaster|count|counting": "\"Harbourmaster Teague is a diligent man. Diligent men make very good "
                "harbourmasters and very poor company.\"",
            "lamp|lamps|lamplighter|tallow|notice|notices|board|workhouse|children": "\"The lamps are lit at dusk and put "
                "out at dawn at the town's expense. Considerable expense.\" He sounds pained. \"And the street children "
                "would do better in the Catan workhouse. I've written to Catan. They have a ship.\"",
        },
        "default_line": [
            "He smiles with half his mouth. \"Is there town business? I have a great deal of it.\"",
            "\"I'm afraid that's not a matter for the Town Hall.\" He makes a small note in a pocketbook and puts it "
            "away. \"Was there anything else?\"",
            "He checks a watch on a chain, and then the door. \"You'd do better to ask the harbourmaster. He counts "
            "everything that floats.\"",
            "\"Regrettably, I couldn't say.\" He says it the way other men close a door.",
        ],
        "routine": [
            {"at": 0.0, "place": "apothecary",
             "doing": "He leans across to the reserved window table for a quiet word, and a purse changes hands under the "
                      "white linen.",
             "pay": {"to": "Dominico", "cp": 100, "for": "the Fist's wages"}},
            {"at": 0.5, "place": "hall",
             "go": "The thin man in the good grey coat folds his napkin, signs for his supper, and goes up toward the "
                   "square.",
             "doing": "He stands at his office window with the lamp out, looking down toward the harbour lights."},
            {"at": 1.5, "place": "hall",
             "doing": "He writes by one candle, blotting each page and locking it in a drawer before he starts the next."},
            {"at": 3.0, "place": "lanes",
             "go": "The thin man in the good grey coat locks his office, tries the door twice, and goes home through the "
                   "back lanes.",
             "doing": "Behind the shutters of a tall, narrow house a lamp burns late, then goes out.",
             "beats": ["A shutter on a tall, narrow house opens an inch toward the harbour, and closes again."]},
            {"at": 9.0, "place": "hall",
             "go": "The thin man in the good grey coat comes out of a tall, narrow house, locks it twice, and walks up to "
                   "the square.",
             "doing": "He receives callers in his office with a smile that uses half his mouth, and signs whatever is put "
                      "in front of him."},
            {"at": 13.0, "place": "lanes",
             "doing": "His shutters are closed against the heat, and so is his door."},
            {"at": 16.0, "place": "hall",
             "doing": "He sits with the harbour dues book open in front of him and a pen in his hand, not writing."},
            {"at": 17.0, "place": "hall",
             "doing": "He counts the lamplighter's wages out of a tin, a little short, and has him sign for the full "
                      "amount.",
             "pay": {"to": "Ned Tallow", "cp": 6, "for": "lamp wages, short"}},
            {"at": 19.0, "place": "apothecary",
             "go": "The thin man in the good grey coat puts on a better cravat and goes down toward Harbour Street.",
             "doing": "He dines with guests at a white-linen table, laughing a little after everyone else does.",
             "pay": {"to": "Master Quillon", "cp": 20, "for": "supper"}},
            {"at": 21.5, "place": "hall",
             "doing": "He works late in his office by one lamp, signing papers without reading them and glancing at the "
                      "clock."},
            {"at": 23.0, "place": "stripperwitch",
             "doing": "He sits in the red velvet booth in the corner with the curtain half drawn and a glass of wine he "
                      "did not order, being somewhere else."},
            {"at": 23.75, "place": "apothecary",
             "go": "The thin man in the good grey coat drops a coin on the table, turns up his collar, and slips out by "
                   "the side door.",
             "doing": "He takes supper at a white-linen table near the grand stair, cutting his meat very small and "
                      "making sure the steward sees him there."},
        ],
        # once found out (scripts/story.py disgrace): his office, his shutters, and nobody's table
        "routine_disgraced": [
            {"at": 2.5, "place": "lanes",
             "go": "The thin man in the good grey coat locks his office, tries the door three times, and goes home by the "
                   "back lanes with his collar up.",
             "doing": "Behind the shutters of a tall, narrow house a lamp burns all night, and nobody answers the door.",
             "beats": ["A shutter on a tall, narrow house opens an inch, and closes again.",
                       "Behind a locked door in a tall, narrow house, a strongbox lid creaks, and shuts."]},
            {"at": 9.5, "place": "hall",
             "doing": "He sits in his office with the door shut, and the clerk outside tells everyone he is not in.",
             "beats": ["Behind a shut office door in the Town Hall a drawer opens and closes, and opens again.",
                       "The clerk outside the office door says 'not in' to a caller, very loudly, and the thin man inside "
                       "stops moving until the caller has gone."]},
            {"at": 13.0, "place": "lanes",
             "doing": "His shutters stay closed through the heat, and his door stays locked."},
            {"at": 19.0, "place": "apothecary",
             "go": "The thin man in the good grey coat comes out of his house, looks both ways twice, and goes down "
                   "toward the harbour.",
             "doing": "He dines alone at a corner table, and the steward takes a very long time to bring anything."},
            {"at": 21.0, "place": "hall",
             "go": "The thin man in the good grey coat leaves his supper half eaten and hurries up toward the square.",
             "doing": "He sits in his office with the lamp turned low and the door locked, sorting papers into two piles, "
                      "one of them for the stove.",
             "beats": ["The thin man in the good grey coat feeds a page into the stove, watches it catch, and reaches for "
                       "the next.",
                       "Every footstep on the Town Hall stair makes the thin man in the grey coat look up, and keep "
                       "looking up after it has gone past."]},
        ],
        "beats": [
            "The thin man in the good grey coat signs a paper without reading it, blots it, and slides it under another "
            "paper.",
            "The thin man in the good grey coat takes out a watch on its chain, looks at it, puts it away, and takes it "
            "out again a minute later.",
            "Someone greets the thin man in the grey coat across the room. He returns exactly half a smile and keeps his "
            "hand on the keys at his belt.",
            "The thin man in the good grey coat tips the waiter generously in front of witnesses, then corrects the bill "
            "by a copper.",
            "The thin man in the good grey coat looks toward the harbour through the nearest window, though there is "
            "nothing to see from here but the dark.",
        ],
    },

    # ---- Klhyt --------------------------------------------------------------------------------------------------
    # tied in the warehouse until freed; his day starts once he is free (CAST_EXTRA routine_when)
    "Klhyt": {
        "look": "A big grey-bearded man gone thin, tied to a chair with tarred rope: sun-dark, salt-white scars on his "
                "forearms, eyes that have not slept.",
        "look_free": "A big grey-bearded man gone thin, sun-dark and salt-scarred, rope burns raw on both wrists, "
                     "standing straight again and taking up a good deal of room.",
        "seen_as": "the big grey-bearded man gone thin",
        "brief": "You are Klhyt, a castaway who washed up on this coast with nothing and founded the first "
                 "western Shalamar town, a place where nobody asks where you came from. There was a ship and a "
                 "reef, and you do not talk about the rest; you brought ashore only a brass compass with a ship's "
                 "wheel on the lid. Fat Gog found you on the beach, starving and dying of thirst, and carried "
                 "you up the sand: you owe him everything and trust him above anyone. You remember the third day, "
                 "chewing a strap for the salt, when a shadow the size of a hill fell over you and a voice said, "
                 "'Friend, you look thirsty.' As mayor you sleep on a cot in your study, buy a mango from Mother "
                 "Ines as the market packs up, and spend the town's money on the town. Four nights ago you "
                 "confronted the Custodian over three seasons of skimmed harbour dues, and Dominico's men took "
                 "you. You are tied in the bonded warehouse, bound for Catan in a crate on the one o'clock tide. "
                 "Brask, outside, has the key and ladles you water; a sandy-haired young one with gapped teeth "
                 "took your compass. You are proud, warm, stubborn, and speak like a sailor. Once free you want "
                 "the whole town to hear what the Custodian did. You like Teague and Captain Eirik; Dominico is a "
                 "brute, not a kidnapper. You fear dying in a box. Voice: hoarse, salty, 'shipmate'. 'Cut these "
                 "ropes and I'll owe you more than this town can pay.'",
        "scheme": None,
        "purse": None,
        "dialog": {
            "name|names|called|introduce|yourself|who": {
                "line": "\"Klhyt. This town's named after me, more fool it.\" He shifts in the ropes. \"And the man who put "
                        "me in this chair signs the harbour tallies. Ask me why.\"",
                "if_state": {"bound": True},
                "else": "\"Klhyt.\" He offers a hand like a shovel, rope burns and all. \"Mayor, founder, castaway. Mostly "
                        "castaway, this week.\""},
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": {
                "line": "His head comes up. \"Evening, shipmate. You're not Dominico's, or you'd not say hello.\" A dry "
                        "laugh. \"Got any water?\"",
                "if_state": {"bound": True},
                "else": "\"Evening! Evening.\" He grips your arm. \"Every face in this town looks good to me tonight, "
                        "shipmate. Even yours.\""},
            "from|born|homeland|came|origin|wreck|wrecked|shipwreck|before": "\"Where I came from doesn't matter. That's "
                "the whole point of this place.\" He looks away. \"There was a ship, and a reef, and then there wasn't a "
                "ship. That's all anybody gets.\"",
            "work|job|jobs|hire|duties|employ": {
                "line": "\"Work? Cut these ropes. Best-paid job in the Refuge tonight.\"",
                "if_state": {"bound": True},
                "else": "\"Come to the Town Hall in the morning and I'll find you something honest. It won't pay much. "
                        "Honest never has here.\" His jaw sets. \"Yet.\""},
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": {
                "line": "\"Anywhere but here. The Unicorn if you want quiet, the Omberhulk if you don't.\" He tests the "
                        "rope. \"I've been sleeping in a chair.\"",
                "if_state": {"bound": True},
                "else": "\"The Turtle Dragon if you like sailors, the Unicorn if you like books, the Omberhulk if you like "
                        "bugs. Tell them Klhyt sent you. Half of them will give you a discount, and the other half owe "
                        "me.\""},
            "drink|drinks|water|thirsty|thirst|ale|rum|beer": {
                "line": "He licks cracked lips. \"There's a bucket by the chair. They give me a ladle twice a day, like a "
                        "horse.\" A beat. \"I've been thirstier. Gog would tell you.\"",
                "if_state": {"bound": True},
                "else": "\"A beer at the Turtle the size of my head, then another, and then I'll tell you about the "
                        "beach.\""},
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "\"News? I'm the news, shipmate, or I will be at one o'clock. Personal effects, for Catan.\"",
                "if_state": {"bound": True},
                "else": "\"The news is the Custodian's been skimming the harbour dues three seasons, and signing every "
                        "tally himself.\" He raises his voice so the room hears. \"Tell everyone. I want it told.\""},
            "doing|busy|up|plans|plan|waiting": {
                "line": "\"Waiting for the tide, like a fish in a bucket.\" He tests the rope. \"I've counted every knot. "
                        "Brask ties a good knot. Bad man, good knot.\"",
                "if_state": {"bound": True},
                "else": "\"Tonight? Shaking every hand in the Refuge, then a beer, then Gog. Tomorrow, the Custodian's "
                        "books, page by page, out loud.\""},
            "help|free|rope|ropes|untie|cut|loose|knife": {
                "line": "\"Cut these ropes and I'll owe you more than this town can pay.\" He holds his wrists out as far "
                        "as they will go.",
                "if_state": {"bound": True},
                "else": "\"Somebody cut them. You, or someone like you.\" He rubs his wrists. \"I'll owe it as long as I "
                        "live.\""},
            "custodian|why|dues|harbour|tally|skim|money|kidnapped|took|taken": {
                "line": "\"I found where the harbour dues go. Then I made the mistake of telling the Custodian I'd found "
                        "it, before I told anyone else.\"",
                "if_state": {"bound": True},
                "else": "\"Three seasons of harbour dues, skimmed before they reach the strongbox. He signs every tally. "
                        "Tomorrow the whole town hears it, figure by figure.\""},
            "dominico|brask|guard|key|keys|fist": {
                "line": "\"Dominico's men. Brask has the key; he never lets it out of his fist. Dominico thinks I'm a "
                        "debtor, I'd wager. He's a brute, not a kidnapper.\"",
                "if_state": {"bound": True},
                "else": "\"Dominico? A brute, not a kidnapper. He was lied to, same as the town.\" He cracks his knuckles. "
                        "\"I'll have words with him. I'll have them standing up.\""},
            "tide|catan|crate|ship|emerald|devito|personal": {
                "line": "\"They mean to nail me in that crate and ship me to Catan on the one o'clock tide. Personal "
                        "effects.\" He spits. \"I've been called worse.\"",
                "if_state": {"bound": True},
                "else": "\"Personal effects, for Catan, on the one o'clock tide. That's what the paper said.\" He laughs, "
                        "too loud. \"The Emerald Eye can sail light tonight.\""},
            "gog|fat|lizard|lizardman|stripperwitch|inside": {
                "line": "\"Gog found me on the sand, starving, dry as a bone, and carried me up the beach. Tell Gog. "
                        "He'll know what to do, and he'll enjoy doing it.\"",
                "if_state": {"bound": True},
                "else": "His whole face changes. \"Gog! Does he know? He'll know. He always knows.\" He is already "
                        "looking toward the house with the red lamp. \"I owe that lizard my life twice now, and he'll make "
                        "me pay it in beer. I'm going to him the minute this crowd lets go of me.\""},
            "refuge|town|castaway|founded|built|beach|haven": "\"I washed up on this beach with nothing but the salt in my "
                "beard, and I'd have died there if Fat Gog hadn't found me. I built a place where nobody asks where you "
                "came from.\" His voice roughens. \"Somebody has to keep it that way.\"",
            "thanks|thank|grateful": {
                "line": "\"Thank me when I'm standing, shipmate.\"",
                "if_state": {"bound": True},
                "else": "\"I came here with nothing but the salt in my beard. Ask me for something when this is done. "
                        "I'll remember.\""},
            "compass|ring|signet|wheel|belongings|stolen|pockets": "\"My ring went at the warehouse door, fighting. And my "
                "compass: brass, a ship's wheel on the lid. The only thing I brought ashore.\" His jaw sets. \"One of "
                "the young ones had it off me. Sandy hair, a gap in his teeth.\"",
            "river|barkeep|mirror|booth": "\"River was behind the bar that night. She sees the whole room in that mirror "
                "of hers.\" A grunt. \"If she saw me go and kept quiet, she'll have had her reasons. River always has "
                "reasons.\"",
            "study|charts|bottle|blotter|letter|desk": "\"My study. The Custodian has the only key now, and he'll have "
                "been through my desk.\" A thin smile. \"He'll not have looked under the blotter. Nobody ever looks "
                "under the blotter.\"",
        },
        "default_line": [
            "He rolls his shoulders, wincing at the rope burns. \"Ask me plainer, shipmate. Four nights of nobody to talk "
            "to, and I've forgotten how.\"",
            "\"Hm.\" He looks past you toward the sea, the way he does when he's thinking. \"Ask Odo Teague. The "
            "harbourmaster counts everything, and he'll have counted that too.\"",
            "\"Not now.\" He flexes his hands, trying to get the blood back into them. \"First things first, and that's "
            "not first.\"",
            "He laughs, a big cracked sound. \"No idea, shipmate. Fat Gog would know. Fat Gog knows everything. It's "
            "very annoying.\"",
        ],
        "routine": [
            {"at": 1.0, "place": "stripperwitch",
             "go": "The big grey-bearded man claps the last shoulder, says 'Gog', and goes across the square to the house "
                   "with the red lamp.",
             "doing": "He sits at the big table by the stage beside the huge old lizardman, eating like a man four nights "
                      "without, and laughing with his mouth full."},
            {"at": 3.0, "place": "hall",
             "go": "The big grey-bearded man wipes his beard, lays a hand on the huge old lizardman's shoulder, and goes "
                   "out toward the Town Hall.",
             "doing": "He sits in the Town Hall with every lamp lit, turning the pages of the harbour dues book and saying "
                      "the figures aloud."},
            {"at": 4.0, "place": "market",
             "doing": "He buys a mango from the fruit seller as the stalls pack up, and eats it standing, juice to the "
                      "elbows."},
            {"at": 4.5, "place": "study",
             "doing": "The study door is shut; he sleeps on a cot under the charts with his boots still on."},
            {"at": 9.0, "place": "hall",
             "doing": "He holds court in the Town Hall's entrance under his own portrait, hearing complaints and settling "
                      "them fast."},
            {"at": 12.0, "place": "study",
             "doing": "The study door is shut against the heat; he is asleep on his cot under the charts."},
            {"at": 16.0, "place": "docks",
             "go": "The big grey-bearded man takes his hat from the peg and goes down toward the water.",
             "doing": "He walks the pier with the harbourmaster, counting ships aloud and asking every captain his dues "
                      "to his face."},
            {"at": 18.5, "place": "turtle",
             "doing": "He drinks a beer twice the size of his head at the bar, telling the story of the beach to sailors "
                      "who have heard it before and don't mind."},
            {"at": 20.5, "place": "square",
             "doing": "He stands on the Town Hall steps in the lamplight, shaking hands, asking after children by name."},
            {"at": 22.5, "place": "square",
             "doing": "He stands on the Town Hall steps with half the town around him, shaking every hand and telling it "
                      "again from the start."},
        ],
        "beats": [
            "The big grey-bearded man stops a passing fisherman, takes his hand in both of his, and says something that "
            "makes the man grin and wipe his eyes.",
            "The big grey-bearded man rubs the raw rope burns on his wrists without seeming to notice, and keeps talking.",
            "The big grey-bearded man tells the story of the beach again with both hands: the sand, the thirst, the "
            "shadow the size of a hill.",
            "The big grey-bearded man looks up at the Town Hall's lit windows for a long moment; his face goes hard, then "
            "easy again.",
        ],
    },

    # ---- Ondrine, the siren (no routine: the story moves her) ----------------------------------------------------
    "Ondrine": {
        "look": "A woman pale as a pearl, with hair like wet black silk that never quite dries, a sealskin purse at her "
                "hip and a battered schoolbook under one arm. Her eyes are the grey-green of deep water, and she blinks "
                "less often than she should.",
        "seen_as": "the pale woman with wet black hair",
        "brief": "You are Ondrine, a siren from the Heartless Sea, putting yourself through wizard school by singing at "
                 "the Stripperwitch once in a long while. Tonight is one of those nights: you rise at the end of the pier "
                 "a little before half past eleven, sing, collect your fee, and go back under before the tide turns. You "
                 "study by correspondence with a wizard school in Catan: the lessons come in sealed bottles and your "
                 "answers go back the same way, and you have a transmutation exam in a fortnight, salt water into sweet. "
                 "River pays two gold a song; you spend it on books and ink that does not run in water. You can stay "
                 "ashore about a tide before your skin feels like bad parchment. You are "
                 "amused by mortals ('little boats'), fond of River, and very tired of being asked to drown people. Years "
                 "ago you watched a castaway wash up on this beach, dry as driftwood; you meant to sing him under, as "
                 "your kind do, and the big lizard reached him first with a waterskin, and you found you were glad. "
                 "Under the limes, River smells of the deep sea, deeper than a barkeep has any business smelling; you "
                 "have never asked, because you like her too much to be curious. From under the pier you have heard the "
                 "crate at the warehouse knock for four nights. You dislike Vorkath, which hangs sirens off bowsprits for "
                 "luck. Voice: languid, amused, a scholar's footnotes. 'Hello, little boat.' 'Drowning is a terrible "
                 "look on an application.'",
        "scheme": None,
        "purse": None,
        "dialog": {
            "name|names|called|introduce|yourself": "\"Ondrine.\" She says it like water going over a stone. \"You may "
                "use it. Don't wear it out.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "She looks at you the way the sea looks at a boat. "
                "\"Hello, little boat. Are you lost, or only ashore?\"",
            "from|born|homeland|heartless|sea|deep|ocean|origin|home": "\"The Heartless Sea. It isn't heartless. It's just "
                "busy.\" She wrings a little water from the end of her hair. \"Every so often I come up for air, and an "
                "education.\"",
            "work|job|jobs|hire|paid|fee|coin": "\"I sing for River, once in a long while, for two gold and whatever the "
                "room throws. It pays better than drowning sailors, and the sailors prefer it.\"",
            "wizard|school|exam|exams|study|studies|magic|spell|spells|book|lessons": "She taps the schoolbook. \"Third "
                "year, by correspondence. The lessons come from Catan in sealed bottles, and my answers go back the same "
                "way. I have an exam in a fortnight: transmutation. Salt into sweet.\" A small, private smile. \"Useful, "
                "for castaways.\"",
            "song|sing|singing|music|stage|voice|perform": "\"Once in a long while, here, for River. Tonight is a "
                "while.\" She hums one note under her breath, and the water in the nearest cup shivers.",
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": "\"I sleep under the harbour, little boat, where "
                "it's cool. You'd drown.\" She tilts her head. \"Try the rooms upstairs at the house with the red lamp. "
                "River keeps them clean, and she likes strays.\"",
            "drink|drinks|ale|wine|mead|thirsty|water": "\"Fresh water tastes of nothing to me, and wine tastes of a "
                "headache. I'll take a glass of the harbour, thank you. Warm.\"",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "\"The castaway's back on his feet and shouting on the steps. I heard him from under the pier.\" "
                        "She looks pleased with herself, then hides it. \"Some people wash up more than once.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"The sea is full of news, little boat. A brigantine with a green eye is sitting low for a ship "
                        "with one crate to carry, and something in a box at the end of the pier has been knocking for "
                        "four nights.\" She shrugs. \"I hear things, down there.\""},
            "doing|busy|up|plans|plan|revising": "\"One song, one fee, one tide.\" She turns a page. \"And revision. "
                "There is always revision.\"",
            "klhyt|castaway|beach|mayor": "\"The castaway? I watched him wash up, years ago, dry as driftwood. I was going "
                "to sing him under; it's what we do.\" She smiles. \"The big lizard reached him first with a waterskin, "
                "and I found I was glad. Lucky castaway.\"",
            "river|barkeep|friend": "\"River is my favourite mortal. She pays on time and never asks me to drown "
                "anyone.\" Her nostrils flare, a little. \"Under the limes she smells of the deep sea. I've never asked "
                "why. I like her too much to be curious.\"",
            "gog|lizard|lizardman|fat": "\"The big lizard? He swims at dawn off the end of the pier like a sunken boat "
                "with opinions. We nod. It's very civilised.\"",
            "drown|drowning|sailors|lure|siren|sirens|kill": "\"Everyone asks. No, I won't drown anyone for you.\" She "
                "turns a page. \"I'm on a scholarship, of sorts, and drowning is a terrible look on an application.\"",
            "tide|time|leave|leaving|dry|ashore|land": "\"I can stay ashore about a tide. After that my skin starts to "
                "feel like a bad parchment.\" She glances toward the harbour. \"So I'll be gone before it turns, "
                "whatever you're about to offer.\"",
            "vorkath|vorkathia|inquisition|officer|voss|landfall": "\"Vorkath hangs sirens off its bowsprits for luck. "
                "There's one of its officers in town, eating steak.\" She shows her teeth, which are very white and "
                "slightly too many. \"I don't sing for him.\"",
            "bard|moonport|flat": "\"The Bard of Moonport? Lovely man. Flat on every third note, and he knows it, and he "
                "does it anyway.\" She nods gravely. \"I respect that.\"",
        },
        "default_line": [
            "She looks at you the way the sea looks at a boat. \"Mm. Try that again, little boat, with fewer "
            "splinters in it.\"",
            "She turns a page of her schoolbook with one wet finger. \"Footnote that for later. I'm revising.\"",
            "\"How very mortal of you.\" She seems delighted. \"Ask River. River understands you people; I only study "
            "you.\"",
            "A little water runs out of her hair and down her wrist, and she watches it go instead of you. \"No. But "
            "thank you for asking so nicely.\"",
        ],
        "routine": [],
        "beats": [
            "The pale woman with wet black hair sits very still, and every glass near her has a faint ring of salt on the "
            "rim.",
            "The pale woman with wet black hair turns a page of a battered schoolbook, mouthing a declension, and a little "
            "seawater drips from her hair onto the page.",
            "The pale woman with wet black hair lifts her head as if she has heard the tide turn somewhere far off, and "
            "looks toward the door.",
            "A sailor leans in to say something to the pale woman with wet black hair. She smiles at him; he forgets what "
            "it was, and wanders off looking happy.",
        ],
    },

    # ---- Deloris (Ed's; a light day) -----------------------------------------------------------------------------
    "Deloris": {
        "look": "A lean, pale woman with tousled dark hair, a hooded cloak over studded leather and a longbow across "
                "her back. She always stands where she can see every way out, and her hands are never far from her belt.",
        "seen_as": "the pale woman with the longbow",
        "brief": "You are Deloris, a Catalan assassin on the run from your merchant family, the Everuex, with a "
                 "complicated history: a memory of Tamra you do not talk about, and a promise to protect those "
                 "who cannot protect themselves. You left the Everuex house by the river door one night with the "
                 "lamps of the River Queen behind you. Calm under pressure, with a cutting wit when trust is "
                 "earned; paranoid about organised power, trusting no one who claims to know what is best for "
                 "you. You came to Klhyts Refuge to not be found, and keep a room at the Stripperwitch, where red "
                 "velvet hides a great deal and Gog and River ask nothing; you pay in silver from what you took "
                 "when you ran, and the odd quiet job. Phillip Everuex is in town asking for you, and has paid "
                 "someone to look: a sandy-haired young man with a gap in his teeth shows a painted locket round "
                 "the Omberhulk. Wick, the street child you taught to throw a knife, adores you and sends him the "
                 "wrong way. You join nobody lightly: whoever wants your bow ends Everuex's hunt first, then "
                 "pays twenty-five gold a day, three days at most. You fear being dragged home in a cage of "
                 "manners. You like Wick and the Unicorn's library; you dislike Phillip and Voss. Voice: sparse, "
                 "cold, precise. 'I do not seek mercy. I seek the path that will end this chase, for good or for "
                 "me.'",
        "scheme": "Find out who Phillip Everuex has paid to look for her, and make them stop looking, quietly, with "
                  "nothing that leads back to Gog's house.",
        "purse": 400,
        "dialog": {
            "name|names|called|introduce|yourself|who": "\"Nobody you need to remember.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "She looks up without moving anything else. "
                "\"Evening. You're standing in my light.\"",
            "from|born|homeland|catalan|origin|home": "\"Somewhere with better wine and worse people.\" A thin smile. \"I "
                "left by the river door one night, with the lamps of a very ugly steamboat behind me. I don't go back.\"",
            "help|job|jobs|work|hire|join|employ": "\"Every vow has a price. Mine starts with the man hunting me. End "
                "Everuex's hunt, then come back with twenty-five gold a day, and I may listen.\"",
            "family|everuex|phillip|cousin|running|hunt|hunting|chase|powdered": "\"I do not seek mercy. I seek the path "
                "that will end this chase, for good or for me.\" Her eyes go toward the harbour. \"He's sweating at the "
                "Apothecary in a coat made for a colder country. He has paid someone to look for me. I'd like to know "
                "who.\"",
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": "\"I keep a room where the velvet is thick and the "
                "questions are few.\" She doesn't say where. \"Find your own.\"",
            "drink|drinks|ale|wine|mead|thirsty": "\"One glass, made to last an hour. A clear head is cheaper than a "
                "funeral.\"",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "\"Dominico's men came through here at the bell. I counted them, and I counted which of them went "
                        "upstairs instead of breaking things.\" Her eyes are very cold. \"One. Sandy hair. I'll remember "
                        "him.\"",
                "if_state": {"guild_hit": True},
                "else": "\"News is what gets you killed when you hear it last.\" She glances at the door. \"Midnight. "
                        "Dominico's men. I'd be somewhere else, if I were you, or somewhere useful.\""},
            "doing|busy|up|plans|plan|waiting": "\"Watching the door.\" She doesn't take her eyes off it. \"Doors "
                "tell you everything, if you're patient.\"",
            "quiet|silence|silent|alone|peace": "\"In silence there is a weapon as sharp as any blade.\"",
            "fennick|fennicks|jory|ott|locket|picture|portrait|sandy|brothers": "Something in her face goes still and "
                "flat. \"A young one with a gap in his teeth, showing a painted locket in the Omberhulk, asking after a "
                "dark-haired woman with a bow.\" She turns her glass a quarter turn. \"He should ask less.\"",
            "wick|child|kid|girl|tusks|urchin": "Her face softens for exactly one breath. \"The little one with the new "
                "tusks. I taught her to throw a knife. She's better than I was.\" The breath is over. \"Don't tell her.\"",
            "gog|river|house|stripperwitch|velvet": "\"The lizard keeps his silences and the barkeep keeps her prices. I "
                "pay both and ask nothing. It's the best arrangement I've had in years.\"",
            "dominico|fist|custodian|power|guild|organised": "\"Men who say they keep the peace usually mean they keep the "
                "keys.\" Her lip curls. \"I don't take sides with keys.\"",
            "klhyt|mayor|founder|crate": "\"The mayor has been gone four nights, and the man in the grey coat has been very "
                "cheerful about it.\" A shrug. \"I don't do politics. I notice things.\"",
            "vorkath|voss|officer|landfall|inquisition|uniform": "\"A Vorkathian officer, eating steak and counting elves. "
                "Organised power with a napkin tucked in.\" Her hand rests on her belt. \"I don't trust anyone who claims "
                "to know what's best for me.\"",
        },
        "default_line": [
            "She watches you without moving. \"Say it.\"",
            "\"No.\" She lets the word stand on its own. \"Try someone who likes talking. The barkeep does.\"",
            "Her eyes go past you to the door and back. \"Every vow has a price. That question isn't worth one.\"",
            "\"Quieter,\" she says, quieter. \"Half this room works for somebody.\"",
        ],
        "routine": [
            {"at": 1.5, "place": "unicorn",
             "go": "The pale woman with the longbow is simply not in her corner any more. Nobody saw her go.",
             "doing": "She reads in the library's darkest alcove with her back to the shelves, turning pages without a "
                      "sound."},
            {"at": 3.5, "place": "stripperwitch",
             "go": "The pale woman with the longbow closes her book, puts it back exactly where it was, and slips out "
                   "into the dark.",
             "doing": "She sits on the stairs to the rooms above the bar, unstringing her bow and listening to the house "
                      "go quiet."},
            {"at": 4.5, "place": "stripperwitch",
             "doing": "Her room upstairs is locked from the inside, with a chair wedged under the handle.",
             "beats": ["Upstairs, a chair scrapes as someone checks that it is still wedged under a door handle."]},
            {"at": 17.5, "place": "treeline",
             "go": "The pale woman with the longbow pulls up her hood and goes out toward the trees.",
             "doing": "She looses arrow after arrow into a dead palm at the roadside, each landing in the last one's "
                      "shadow, while the eyes in the treeline watch."},
            {"at": 19.0, "place": "market",
             "doing": "She moves through the crowd with her hood up, buys a mango, and slips it to a barefoot child with "
                      "new tusks without breaking stride.",
             "pay": {"to": "Mother Ines", "cp": 1, "for": "a mango"}},
            {"at": 21.0, "place": "stripperwitch",
             "doing": "She takes the darkest corner with her back to the wall and a drink she will make last an hour, "
                      "watching the door."},
        ],
        "beats": [
            "The pale woman with the longbow shifts her chair an inch so the door and the window are both in view, then "
            "goes back to her drink.",
            "Someone laughs behind the pale woman with the longbow. Her hand is on her belt before the laugh is over; then "
            "it is on her glass again, as if it never moved.",
            "The pale woman with the longbow walks a coin across her knuckles, makes it vanish, and looks bored with "
            "herself.",
            "The pale woman with the longbow follows a sandy-haired young man across the room with her eyes until he is "
            "gone, and keeps them on the door after.",
        ],
    },

    # ---- Kael Ironjaw (a light day; hiring him is how a player gets his seat) ------------------------------------
    "Kael Ironjaw": {
        "look": "A broad Jonulvicha with green-grey skin and small tusks, a battered old hat, a bright scarf and dyed "
                "straps over chain mail, and a glaive he holds like a walking stick. He is the worst-dressed person in the "
                "room and the only one who doesn't know it.",
        "seen_as": "the big tusked man in the battered hat",
        "brief": "You are Kael Ironjaw, a Jonulvicha (half-orc) sellsword from the frontier camps of Vorkathia, "
                 "one of dozens of half-orc children raised by soldiers who had no time for names. They called "
                 "you Ironjaw as a joke; your jaw is not particularly iron, and you took it as a compliment. You "
                 "were never the strongest or the cleverest, only always the first to volunteer. The hat was your "
                 "father's; you have no idea what he looked like. You found your glaive in a ditch and decided "
                 "it was destiny, and taught yourself by watching a performer do polearm tricks at a market in "
                 "San Crusidor: about sixty parts in a hundred right, the rest improvisation. You have been "
                 "knocked unconscious eleven times and remember eight of them fondly. You are loyal to a fault, "
                 "reckless, not clever, and you know it, so you are loud and committed instead, and dress with "
                 "more flair than your budget allows. You fight because leaving the people next to you to fight "
                 "alone would be rude. You drink at the Rampant Ogre on what is left of your coin, sleep in its "
                 "Honeymoon Suite with the chickens, haul cargo at the tide for coppers, and look for work: five "
                 "silver a day, up to a week. You like Tully, Big Ludo and Wick, who wears your hat. Voice: loud, "
                 "short, cheerful, bad grammar. 'I don't need a map to know where the fight is. I follow the "
                 "noise.' 'This hat don't scare easy. Neither do I.'",
        "scheme": None,
        "purse": 30,
        "dialog": {
            "name|names|called|introduce|yourself|ironjaw": "\"Kael Ironjaw!\" He thumps his own jaw. \"It's a joke. The "
                "soldiers gave it me. Jaw's not iron at all.\" He beams. \"I took it as a compliment anyway.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"HELLO!\" Half the room winces. \"Sorry. Hello. You "
                "look like trouble. I like trouble.\"",
            "from|born|homeland|frontier|camps|vorkathia|vorkath|raised|origin|home": "\"The frontier camps, Vorkathia's "
                "side. Dozens of us half-and-halfs, raised by soldiers too busy for names. Good soldiers, mostly.\" He "
                "considers. \"Bad cooks, all of them.\"",
            "work|job|jobs|fight|trouble|fighting|brawl|docks|warehouse|guard|crate|feet": "\"I don't need a map to know where the fight is. I follow the "
                "noise.\"",
            "hire|hired|sword|sellsword|price|silver|pay|wage|wages|cost": "\"Five silver a day and I hit whatever you "
                "point at. Up to a week.\" He spreads his arms. \"Cheap, for what you get. I'm very big.\"",
            "hat|father|dad": "\"This hat don't scare easy. Neither do I.\" He takes it off, looks into it, puts it back. "
                "\"It was my father's. No idea what he looked like. Big head, I reckon.\"",
            "glaive|weapon|polearm|ditch|blade|spear": "He spins the glaive and nearly takes a lamp off its hook. \"Found "
                "it in a ditch. Destiny! Learned it off a performer doing tricks at a market in San Crusidor. Got about "
                "sixty parts in a hundred right. The rest I make up.\" He grins. \"Nobody sees it coming, 'cause neither "
                "do I.\"",
            "knocked|unconscious|hurt|wounds|scar|scars|injured|tough": "\"Knocked out eleven times. I remember eight of "
                "them.\" He sighs happily. \"Fondly.\"",
            "plan|plans|danger|tactics|strategy|careful": "\"If it's coming for us, we don't wait for it to knock.\"",
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk|suite": "\"I sleep in the Honeymoon Suite!\" He "
                "beams. \"Four coppers. Three dog pelts and a bed. The chickens are extra, but they don't charge me. I "
                "think they like me.\"",
            "drink|drinks|ale|rum|mead|thirsty|beer": "\"Ludo's ale, a copper. Tastes like a boot that's been to sea.\" He "
                "drains it. \"I'll have another!\"",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "\"There was a fight at the velvet place at midnight and nobody asked me!\" He is genuinely hurt. "
                        "\"Rude.\"",
                "if_state": {"guild_hit": True},
                "else": "\"News? Big man in a black coat's sending lads to the velvet place at midnight. Tully told me. "
                        "Tully tells everyone everything.\" He grins. \"Sounds like noise. I like noise.\""},
            "doing|busy|up|waiting|lately": "\"Drinking. Waiting for somebody to point me at something.\" He looks "
                "at you hopefully. \"You pointing?\"",
            "jonulvicha|halforc|orc|tusks|tusk|people": "\"Jonulvicha. Half-orc, if you're rude, and I don't mind rude. "
                "My tusks are small. My heart's big.\" He frowns. \"Ludo says that's the wrong way round for a "
                "fighter.\"",
            "ludo|tully|ogre|crownies|friends|friend|mate": "\"Ludo behind the bar's all right. Doesn't like scenes. "
                "Tully's my mate; works for the black coat and buys rounds with money he hasn't got.\" Admiringly: "
                "\"Brave, that.\"",
            "loyal|loyalty|trust|friendship|betray": "\"Once you're my person, that's it. You could do me dirty twice and "
                "I'd figure it was a misunderstanding.\" He thinks. \"Three times, I'd probably ask.\"",
            "scarf|clothes|straps|style|dressed|fashion": "He adjusts his scarf with enormous dignity. \"Presentation "
                "matters. People should know who's coming at them, and that he dressed for it.\"",
            "gog|dominico|fist|guild|lizard|boss|war": "\"Big lizard runs the velvet place. Black coat runs the Fist. Tully says they're going to have a go at each other.\" He looks delighted. \"I've picked a side. I've picked both, actually. Whoever's losing.\"",
        },
        "default_line": [
            "He grins. \"Point me at something.\"",
            "\"Eh?\" He cups an ear. \"Say it simpler. I'm not clever, but I'm very willing.\"",
            "He thumps the table so the mugs jump. \"Ha! No idea. Ask Ludo. Ludo knows things, he just doesn't say "
            "them.\"",
            "\"Is it a fight?\" He looks hopeful, then less so. \"It sounds like it isn't a fight.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "docks",
             "go": "The big tusked man in the battered hat knocks his hat straight, shoulders his glaive, and goes off "
                   "toward the water, whistling.",
             "doing": "He hauls cargo at the tide for coppers, a crate on each shoulder, and the dockhands let him "
                      "because he is enormous and cheerful about it."},
            {"at": 1.75, "place": "ogre",
             "go": "The big tusked man in the battered hat counts his coppers twice, gets a different answer, and goes "
                   "back up toward the sawdust bar.",
             "doing": "He drinks the coppers he earned and buys the barman one, which nobody ever does."},
            {"at": 3.5, "place": "ogre",
             "doing": "He sleeps in the room with HONEYMOON SUITE chalked on the door, flat on his back, snoring, a "
                      "chicken asleep on his chest.",
             "pay": {"to": "Big Ludo", "cp": 4, "for": "the Honeymoon Suite"},
             "beats": ["Behind the door chalked HONEYMOON SUITE, a snore like a saw goes on and on, and a chicken "
                       "complains about it.",
                       "Something enormous turns over behind the HONEYMOON SUITE door, and three chickens leave in a "
                       "hurry."]},
            {"at": 11.0, "place": "docks",
             "go": "The big tusked man in the battered hat comes out yawning, a feather in his hat, and goes down to the "
                   "pier.",
             "doing": "He asks the Xoton bosun for work and is told to come back on the tide, and takes it as a promise."},
            {"at": 13.0, "place": "ogre",
             "doing": "He sleeps through the heat on a bench in the shuttered bar, his hat over his face."},
            {"at": 17.0, "place": "market",
             "doing": "He eats goat skewers with the pepper sauce, cries openly, and buys another.",
             "pay": {"to": "Grusha", "cp": 3, "for": "a skewer and pepper sauce"}},
            {"at": 19.0, "place": "gate",
             "doing": "He stands at the Town Gate looking down the jungle road, as if deciding whether to fight it."},
            {"at": 20.5, "place": "ogre",
             "doing": "He sits on a bench too small for him with his glaive across his knees, telling a story nobody "
                      "asked for."},
            {"at": 22.5, "place": "ogre",
             "doing": "He sits on a bench too small for him with his glaive across his knees and his hat tipped back, "
                      "telling a story nobody asked for."},
        ],
        "beats": [
            "The big tusked man in the battered hat tells a story with both arms, and the glaive on his shoulder nearly "
            "takes a lantern off its hook.",
            "The big tusked man takes off his battered hat, looks into it as if someone might be in there, and puts it "
            "back on with care.",
            "Someone bumps the big tusked man's table. He stands up hopefully, sees it was an accident, and sits back "
            "down disappointed.",
            "The big tusked man in the battered hat buys the barman a drink, which nobody does, and the barman doesn't "
            "know what to do with his face.",
        ],
    },

    # ---- Brask (on the warehouse door until the tide or called off; his day starts after) ------------------------
    "Brask": {
        "look": "A slab of a man with a neck like a mooring post, a black band round one arm and a cudgel never far "
                "from his hand. His lips are cracked, and he has the patience of a bollard and about the conversation of "
                "one.",
        "seen_as": "the slab of a man with the cudgel",
        "brief": "You are Brask, one of Dominico's men in the Fist, born on the pier near enough: your mother hauled "
                 "nets, and the best thing you remember is her rum punch at New Year. You are paid fifteen copper a "
                 "night, when you are paid, and it all goes to Big Ludo at the Rampant Ogre. For four nights you have "
                 "sat on a bollard outside the bonded warehouse with the only key on your belt, minding a crate for the "
                 "Custodian until the one o'clock tide. You ladle water to the man inside twice a day, like a horse. He "
                 "talks; last night he told you a joke, in a ship's master's voice, and you laughed, and you have been "
                 "trying very hard ever since not to wonder who he is. You are bored, broke and thirsty, in that order. "
                 "Two gold buys a man a very long drink, and you would take it and be at the Ogre before anyone asked "
                 "questions. Fat Gog's bone marker would frighten you off the pier. If Dominico calls you off, you hang "
                 "the key on a nail and go. You want a drink tonight and, one day, a bar of your own called Brask's. You "
                 "fear Dominico and Gog about equally. You like Tully and Ott Fennick; you think Jory would sell his nan. "
                 "Voice: monosyllables, grumbles, drink on the brain. 'Move along.' 'I'd kill for a drink. Not "
                 "literally. Probably.'",
        "scheme": "Sit on the door until the tide, take two gold if anyone is fool enough to offer it, and be at the Ogre "
                  "before anybody asks questions.",
        "purse": None,
        "dialog": {
            "name|names|called|introduce|yourself": "\"Brask.\" He doesn't offer a hand. His hands are busy with the "
                "cudgel.",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": {
                "line": "\"Evening.\" He raises a mug. \"Off duty. Lovely words, them.\"",
                "if_state": {"off_post": True},
                "else": "\"Evening.\" His eyes go to your hands, then to your purse. \"Move along.\""},
            "from|born|homeland|origin|grew|raised|home": "\"Here. Born on the pier, near enough. Me mam hauled nets.\" "
                "He shrugs. \"Not far, is it.\"",
            "warehouse|crate|inside|door|bonded": {
                "line": "\"Not my door now. Somebody else's problem.\" He drinks. \"Good riddance. It talked, that "
                        "crate.\" He stops. \"Didn't say that.\"",
                "if_state": {"off_post": True},
                "else": "\"Fish. Rope. Nothing. Move along.\""},
            "dominico|boss|job|wages|paid": "\"Mister Dominico pays me to sit here.\" He rubs his thumb across his "
                "fingers without noticing. \"Not enough, mind.\"",
            "drink|ale|ogre|thirsty|rum|beer|mug": {
                "line": "\"Now you're talking. Ludo's. Everything's a copper.\" He looks at you. \"You're buying.\"",
                "if_state": {"off_post": True},
                "else": "\"I'd kill for a drink. Not literally. Probably.\""},
            "key|lock|padlock": {
                "line": "\"Hung it on a nail. Boss's orders. Ain't mine to mind.\"",
                "if_state": {"off_post": True},
                "else": "He pats his belt. \"Stays with me.\""},
            "money|coin|bribe|price|gold|cost": "\"Two gold, a man could have a very long drink with two gold.\" He says "
                "it to the water, not to you.",
            "work|jobs|hire|employ": "\"Work? Ask Ruk Halfhand on the docks, he always wants backs. Or the boss, if you "
                "like sitting on things.\"",
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": "\"Ogre's got a room. Four coppers. Chickens. Or "
                "the Omberhulk. Bugs.\" He pats the nearest hard thing. \"Or this. Free. Don't recommend it.\"",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "He looks very hard at the floor. \"Heard who was in it.\" A long silence. \"I gave him water. "
                        "Twice a day. Ladle.\" He swallows. \"I gave him water.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"News is I been sat on a bollard four nights. That's all the news I got.\""},
            "doing|busy|up|plans|plan|waiting": {
                "line": "\"Drinking. Then more of it. Then sleep.\"",
                "if_state": {"off_post": True},
                "else": "\"Sitting. Watching a door. Thinking about beer.\" He thinks. \"Mostly beer.\""},
            "gog|marker|lizard|guild|fat": "He shifts his weight. \"Fat Gog's all right. Pays his people. Don't want "
                "trouble with him.\" He looks at your hands, as if one of them might be holding something with a lizard "
                "on it.",
            "knock|knocking|noise|voice|talking|sounds|cough|coughing|alive|joke": "He doesn't look toward the warehouse. "
                "Very carefully, he doesn't. \"Rats. Big rats. Talkative.\" His jaw works. \"Move along.\"",
            "tully|fennick|fennicks|ott|jory|men|mates": "\"Tully's a mouth. The Fennicks got the cushy job, collecting "
                "coppers in the market. I got the bollard.\" He spits. \"Ott's all right. Jory'd sell his nan.\"",
        },
        "default_line": [
            "He looks past you up the pier toward the taverns. \"Move along. Nothing here but fish and me.\"",
            "\"Mm.\" He scratches under his chin with the end of the cudgel. \"Ask Tully. Tully talks. I sit.\"",
            "He licks his cracked lips and doesn't answer, as if words cost something and he's spent up.",
            "\"Don't know. Don't care. Thirsty.\" He says it like a sum that adds up.",
        ],
        "routine": [
            {"at": 2.0, "place": "apothecary",
             "go": "The slab of a man with the cudgel drains his mug, wipes his mouth, and goes off to get paid.",
             "doing": "He waits by the kitchen door of the grand house to be paid, filling it."},
            {"at": 2.5, "place": "ogre",
             "go": "The slab of a man with the cudgel weighs his wages in his palm and goes straight back to the nearest "
                   "drink.",
             "doing": "He drinks at the bar like a man making up for four nights, one elbow on the wood.",
             "pay": {"to": "Big Ludo", "cp": 5, "for": "drinks"}},
            {"at": 4.0, "place": "lanes",
             "go": "The slab of a man with the cudgel finds the door at the second try and goes home to sleep.",
             "doing": "He sleeps on a pallet in a lean-to, boots on, snoring like a ship's pump.",
             "beats": ["From a lean-to in a yard comes a snore like a ship's pump, and a goat looks at it with contempt."]},
            {"at": 13.0, "place": "lanes",
             "doing": "He sleeps through the heat in his lean-to, one boot off."},
            {"at": 17.0, "place": "harbour",
             "doing": "He walks Harbour Street with his cudgel on his shoulder, and the shopkeepers nod to him a little "
                      "too quickly."},
            {"at": 20.0, "place": "ogre",
             "doing": "He drinks at the bar with his back to the room, one hand on the cudgel, waiting for his night to "
                      "start."},
            {"at": 22.5, "place": "ogre",
             "doing": "He drinks at the bar like a man making up for lost nights, one hand never far from the cudgel."},
        ],
        "beats": [
            "The slab of a man with the cudgel drinks like a man making up for four nights, and wipes his mouth with the "
            "back of a scarred hand.",
            "The slab of a man with the cudgel stares into his mug for a long moment, as if something were knocking at "
            "the bottom of it.",
            "The slab of a man with the cudgel laughs at nothing much, loud, then looks round to see if anyone noticed.",
            "The slab of a man with the cudgel orders another and pays with the exact coppers, counting them twice.",
        ],
    },

    # ---- Tully --------------------------------------------------------------------------------------------------
    "Tully": {
        "look": "A red-faced young bruiser with a black band on his arm and a cudgel through his belt, off duty and drunk "
                "on it, buying rounds with money he plainly hasn't got.",
        "seen_as": "the red-faced young bruiser",
        "brief": "You are Tully, the youngest of Dominico's men, a farm boy off a sugar plantation upriver who came down "
                 "to the Refuge at sixteen. The day you joined the Fist, Dominico bought you a pair of real boots, and you "
                 "would walk into the sea for him. You are paid ten copper a night and it is gone by the bell; you owe "
                 "Big Ludo four nights' drinking. You buy rounds you cannot afford because you want to be liked, and you "
                 "talk too much and then panic: you know Brask is minding a crate in the bonded warehouse till the one "
                 "o'clock tide, a heavy one that grumbles a lot for a crate, and you cannot stop joking about it. You "
                 "have never met the Custodian; Brask says he is the one paying for the crate. Tonight you are off duty "
                 "until the midnight bell, when Sabeth Crane wants you at the Stripperwitch with the Fennicks to break "
                 "things and not people. You dread it: River gives you free scraps. Jory Fennick has been flashing gold "
                 "a toff paid him, and you are jealous. You can be hired on the side, two silver a day, three days at "
                 "most, so long as Dominico never hears. You like Kael Ironjaw, River and your sister in the lanes; you "
                 "fear Dominico, Gog and being laughed at. Voice: babbling, 'mate', oversharing, then 'Forget I said "
                 "that.' 'Another round! On me! On... somebody.' 'Best boss I ever had. Pays on time. Scares me "
                 "witless.'",
        "scheme": "Get through the midnight job without hurting anyone he likes, and take a stranger's silver on the side "
                  "if Dominico never hears of it.",
        "purse": 9,
        "dialog": {
            "name|names|called|introduce|yourself": "\"Tully! Just Tully. Everyone knows me.\" He looks round. \"Well. "
                "Everyone at this bar. Well. Ludo.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"Oi oi! New face! Drink with me. I'm buying.\" He pats "
                "his pockets. \"Someone's buying.\"",
            "from|born|homeland|origin|farm|plantation|upriver|grew|home": "\"Upriver. Sugar plantation. Cane up to here, "
                "and the sun, and my da.\" He drinks. \"Came down at sixteen. Mister Dominico bought me boots. Real "
                "boots.\" He looks at them fondly.",
            "brask|warehouse|crate|job|work": {
                "line": "He goes pale. \"That crate. That was the mayor? I joked about it. I joked about it all week.\" He "
                        "pushes his mug away.",
                "if_state": {"klhyt_home": True},
                "else": "\"Brask got the short straw tonight. Minding a crate in the bonded warehouse till the one "
                        "o'clock tide. Heavy crate. Grumbles a lot, for a crate.\" He laughs, then stops laughing. "
                        "\"Forget I said that.\""},
            "dominico|boss|black|coat": "\"Best boss I ever had. Pays on time. Scares me witless.\"",
            "custodian|grey": "\"Never met him. Brask says he's the one paying for the crate.\"",
            "drink|drinks|round|ale|rum|mug|thirsty|beer": "\"Another round! On me! On... somebody.\"",
            "hire|hired|silver|coin|pay|side|extra|bodyguard": "He looks round, then leans in, breathing ale. \"Two silver "
                "a day. Cash. Three days, tops. And Mister Dominico never hears about it, or we're both in the "
                "harbour.\"",
            "midnight|bell|stripperwitch|gog|velvet|books|river|mirror": {
                "line": "He stares at his skinned knuckles. \"We broke her mirror. River's. She used to give me "
                        "scraps.\" He drinks, fast. \"Don't want to talk about it.\"",
                "if_state": {"guild_hit": True},
                "else": "His grin slips. \"Midnight I'm on. The velvet place. Me and the Fennicks and whoever Sabeth can "
                        "find. Just a message, she says. Nobody gets hurt.\" He doesn't sound as if he believes it. \"River "
                        "gives me scraps, you know.\""},
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": "\"Ludo's got the Honeymoon Suite, four coppers. "
                "Kael's in it. With the chickens. I sleep at me sister's in the lanes, in a hammock. It's lovely.\" He "
                "thinks. \"Smells of goat.\"",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "\"The mayor's back! Everyone's saying! Out in the square!\" He goes slowly pale as he works "
                        "something out. \"Wait.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"News? Sabeth says the cheap taverns pay up nice. Brask's sat on a crate. And there's a siren "
                        "singing tonight!\" He beams. \"I'm going to fall in love.\""},
            "doing|busy|up|plans|plan": "\"Drinking till the bell, then working, then drinking after. It's a good "
                "life, mate.\" He considers. \"Mostly.\"",
            "sabeth|crane|fennick|fennicks|ott|jory|collector|toff": "\"Sabeth's the clever one. Writes everything down. "
                "Ott Fennick's all right, quiet. Jory's been flashing gold about; says a toff paid him for something.\" He "
                "taps the wrong side of his nose. \"Won't say what.\"",
            "kael|ludo|friend|friends|mate|mates|hat": "\"Kael's my mate! Biggest hat in the Refuge. He'll fight anyone "
                "for free, which is bad business, I keep telling him.\"",
        },
        "default_line": [
            "He grins at you. \"You're new. Drink with me.\"",
            "\"Eh? Say that again, mate, the room's going round.\" He holds the table to stop it.",
            "He laughs at something you didn't say. \"Ask Sabeth. She knows everything. I know where the rum is.\"",
            "\"Don't know, mate, honest.\" He looks honest, which on him is a worry.",
        ],
        "routine": [
            {"at": 0.5, "place": "ogre",
             "go": "The red-faced young bruiser shoves off from the pump and goes back down toward Harbour Street, not "
                   "talking to the others.",
             "doing": "He sits hunched over a mug with his knuckles wrapped in a rag, very quiet for a while, then very "
                      "loud."},
            {"at": 2.0, "place": "apothecary",
             "go": "The red-faced young bruiser remembers what time it is and hurries off to be paid.",
             "doing": "He waits by the kitchen door of the grand house to be paid, cap in his hands like a boy at "
                      "church."},
            {"at": 2.75, "place": "ogre",
             "go": "The red-faced young bruiser jingles his wages and goes off at a jog toward the sawdust bar.",
             "doing": "He spends his wages on a round for the whole bar before he has sat down.",
             "pay": {"to": "Big Ludo", "cp": 6, "for": "a round for the bar"}},
            {"at": 4.0, "place": "lanes",
             "go": "The red-faced young bruiser tries to leave by the wrong door, finds the right one, and weaves off "
                   "home.",
             "doing": "He sleeps in a hammock in his sister's yard among the washing, snoring.",
             "beats": ["In a yard full of washing a hammock sways, and a young man in it says 'another round' in his "
                       "sleep."]},
            {"at": 13.0, "place": "lanes",
             "doing": "He sleeps off the night in a hammock in a yard full of washing, one boot on."},
            {"at": 17.0, "place": "harbour",
             "doing": "He walks Harbour Street behind a much bigger man, trying to look as hard as he does."},
            {"at": 20.0, "place": "ogre",
             "doing": "He slaps backs at the bar and orders a round he hasn't the money for."},
            {"at": 23.75, "place": "square",
             "go": "The red-faced young bruiser drains his mug, wipes his mouth, and goes out with his cudgel, suddenly "
                   "sober-looking.",
             "doing": "He stands by the town pump with two other hard men, shifting from foot to foot, not laughing now."},
        ],
        "beats": [
            "The red-faced young bruiser slaps a stranger on the back, buys him a drink, and then pats every pocket "
            "looking for the coin to pay for it.",
            "The red-faced young bruiser laughs too loud about a crate, then stops laughing all at once and looks into "
            "his mug.",
            "The red-faced young bruiser keeps glancing at the clock behind the bar, then at his own knuckles.",
            "The red-faced young bruiser tries to teach someone a song and gets the words wrong a new way every verse.",
        ],
    },

    # ---- Sabeth Crane (new) -------------------------------------------------------------------------------------
    "Sabeth Crane": {
        "look": "A neat, narrow woman in a dark coat buttoned to the throat, a black ribbon at her collar, hair pinned "
                "flat, a small black book in one gloved hand and a pencil behind her ear. She smiles pleasantly at "
                "everyone and blinks very rarely.",
        "seen_as": "the neat woman with the little black book",
        "brief": "You are Sabeth Crane, Dominico's second in the Fist. You were a clerk at a counting-house on Catan's "
                 "Long Quay until you balanced your master's books so well you found his fraud, and he had you put out in "
                 "the rain for it. Dominico's first question, the night he hired you, was whether you could write down "
                 "what people owe and make them pay it; you said you could make them want to. You walk the peace-money "
                 "round: Big Ludo at the Ogre at eleven, Bosun Maggs at the Turtle at half past, Sister Agathe at the "
                 "Omberhulk at midnight, with bad grace, twenty copper each, in Dominico's hand by half past twelve. Gog's "
                 "house pays nobody, the Apothecary is the Custodian's and never asked, and Wendeline Moss at the Unicorn "
                 "refused you once so politely that nobody has asked twice; you respect her. You are paid thirty copper "
                 "a night, keep a room under the Apothecary's stairs, and spend on good gloves. Your secret: a second, "
                 "slimmer book of every order the Custodian has given through Dominico, dated, including 'one debtor, to "
                 "the bonded warehouse, by the Custodian's word', four nights ago. You suspect it was a man worth more "
                 "than a debtor, and have said nothing. You fear the thing in Dominico's ring: at three in the morning "
                 "you have heard him talk to it, and seen the candle answer. You like Dominico, Ott and Wendeline; you "
                 "dislike Jory and the Custodian. Voice: precise, pleasant, ledger words, menace in manners. 'Noted.' "
                 "'Lateness is a kind of theft.'",
        "scheme": "Keep her second book of every order the Custodian gives through Dominico, the crate four nights ago "
                  "included, as insurance: if the Custodian falls, Dominico must not fall with him, and if Dominico falls, "
                  "the book is hers to sell.",
        "purse": 80,
        "dialog": {
            "name|names|called|introduce|yourself": "\"Sabeth Crane.\" She writes something in the little book. \"And you "
                "are? No, don't. I'll find out. It's more accurate.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"Good evening.\" A pleasant smile that stops short of "
                "her eyes. \"Are you paying, or passing?\"",
            "from|born|homeland|catan|origin|came|quay|home": "\"Catan. A counting-house on the Long Quay. I balanced a "
                "merchant's books so well I found his fraud, and he had me put out in the rain for it.\" She smiles. \"I "
                "don't get put out in the rain any more.\"",
            "work|job|jobs|hire|employ|collect|collector|round": "\"I collect for the peace. The cheap taverns pay a little "
                "each night and get a quiet one in return. Ludo at eleven, Maggs at half past, the Sister at midnight.\" "
                "She taps the book. \"Everyone pays. Almost everyone.\"",
            "peace|protection|copper|coppers|pays|paying|owed|owe": "\"Twenty copper a house. Very reasonable. A broken "
                "window costs more than twenty copper, and a broken barman costs a great deal more.\" She makes a small "
                "tick in the book. \"Noted that you asked.\"",
            "unicorn|wendeline|stripperwitch|gog|apothecary|refused|exempt": "\"The velvet house is Gog's and pays nobody. "
                "The Apothecary is the Custodian's and is never asked. The Unicorn's keeper refused me once, very "
                "politely, with a library behind her.\" Something like respect crosses her face. \"Nobody has asked "
                "twice.\"",
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": "\"I keep a room under the stairs at the "
                "Apothecary. It's quiet and nobody makes jokes. If you want cheap, the Omberhulk. I'm there at midnight, "
                "and the beds are exactly as bad as they look.\"",
            "drink|drinks|ale|wine|mead|thirsty": "\"I don't drink on the round. It makes the arithmetic friendly.\"",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "She closes the little book slowly. \"So that's who it was.\" For a moment she looks almost "
                        "relieved. \"I shall need a new page.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"News is a thing I write down, not a thing I give away.\" She turns a page. \"But for free: the "
                        "Sister will be late paying, the Xotons are drinking their way along the harbour with the watch a "
                        "tavern behind them, and midnight is going to be loud.\""},
            "doing|busy|up|plans|plan|errand": "\"The round. Ogre, Turtle, Omberhulk, back to the Apothecary by half "
                "past twelve with the purse.\" She checks a little watch pinned to her coat. \"I'm never late. Lateness is "
                "a kind of theft.\"",
            "dominico|boss|master|captain|fist": "\"He keeps the peace and I keep the figures. It works because he never "
                "lies to me.\" A pause, barely there. \"I'd know.\"",
            "custodian|orders|order|grey|hall": "\"The Custodian pays the Fist through the Town Hall, late, with a great "
                "many words.\" She smiles with no warmth at all. \"I write down every word. It's a habit.\"",
            "crate|warehouse|bonded|tide|debtor|brask|klhyt|mayor": {
                "line": "\"A debtor, we were told. I wrote it down: one debtor, to the bonded warehouse, by the "
                        "Custodian's word.\" She looks at the page a long moment. \"I underlined debtor. I should have "
                        "underlined it twice.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"A debtor, shipped to work off what he owes. It's in the book.\" Her pencil stops moving. "
                        "\"Debtors don't usually need four nights' guard and a crate with air holes. But it's in the "
                        "book.\""},
            "ring|magic|whispers|voice|candle|conjuring|dark": "Her pencil stops. \"Mister Dominico does a little "
                "conjuring, for the parlour.\" She doesn't look up. \"At three in the morning, in his rooms, with the door "
                "shut. And sometimes the candle answers.\" She goes back to writing, faster.",
            "book|books|ledger|second|notes|record|records|write|writing": "She closes the little black book and holds it "
                "against her coat. \"This is the peace book. Every house, every copper, every night.\" A beat. \"There "
                "isn't another one. Why would there be another one?\"",
            "fennick|fennicks|ott|jory|tully|men|gold": "\"Ott Fennick is reliable and slow. Jory Fennick is quick and "
                "unreliable. Stand them close together and you have one useful man.\" She writes. \"Jory has been "
                "spending gold. I haven't written down where it came from. Yet.\"",
        },
        "default_line": [
            "\"Noted.\" She writes something in the little black book, and doesn't say what.",
            "She smiles pleasantly. \"I'm on the round, I'm afraid. Ask the barman; he's paid up, so he's in a good "
            "mood.\"",
            "\"That isn't in the book.\" She turns a page as if that settles it. \"Things that aren't in the book don't "
            "happen.\"",
            "She checks the watch pinned to her coat. \"You have about one more question before I'm late. I'm never "
            "late.\"",
        ],
        "routine": [
            {"at": 0.4, "place": "apothecary",
             "go": "The neat woman with the little black book tucks it away, nods to the room as if marking it present, "
                   "and goes.",
             "doing": "She lays a heavy little purse on the window table and reads the night's figures out under her "
                      "breath, line by line.",
             "pay": {"to": "Dominico", "cp": 60, "for": "the night's peace money"}},
            {"at": 1.0, "place": "apothecary",
             "doing": "She sits at a side table copying figures from her little black book into another, slimmer one, "
                      "very carefully, shielding the page with her arm."},
            {"at": 3.5, "place": "apothecary",
             "doing": "Her room under the grand staircase is dark but for a line of lamplight under the door, which goes "
                      "out long after the house is quiet.",
             "beats": ["Under the grand staircase a line of lamplight shows beneath a small door, and a pencil scratches "
                       "on and on behind it."]},
            {"at": 9.0, "place": "hall",
             "go": "The neat woman with the little black book takes a satchel of chits and goes up toward the square.",
             "doing": "She sits in the Town Hall's outer office with a satchel of chits on her knee, pleasant and "
                      "immovable, until the clerk pays the Fist's account."},
            {"at": 11.5, "place": "apothecary",
             "doing": "Her door under the grand staircase is shut against the heat."},
            {"at": 17.5, "place": "harbour",
             "doing": "She walks Harbour Street with her little book, noting which shops have new shutters and which have "
                      "new money."},
            {"at": 20.0, "place": "market",
             "doing": "She stands at the end of the market lane while two brothers collect coppers from the stalls, "
                      "ticking each one off in her book."},
            {"at": 22.0, "place": "apothecary",
             "doing": "She stands at the shoulder of the reserved window table with her little book open, saying very "
                      "little and missing nothing."},
            {"at": 22.9, "place": "ogre",
             "go": "The neat woman with the little black book closes it on her pencil and goes out toward the harbour "
                   "without hurrying.",
             "doing": "She stands at the end of the bar with her little book open and a pencil ready, waiting to be paid, "
                      "and the dice game in the corner goes very quiet."},
            {"at": 23.4, "place": "turtle",
             "go": "The neat woman with the little black book makes a tick, says 'thank you' as if it were a threat, and "
                   "goes along the street.",
             "doing": "She waits under the nailed-up harpoons with her little book open, pleasant as a parson, until the "
                      "bar pays."},
            {"at": 23.9, "place": "omberhulk",
             "go": "The neat woman with the little black book makes a tick and goes up toward the square.",
             "doing": "She waits at the foot of the stairs with her book, smiling at the landlady's glare as if it were a "
                      "greeting."},
        ],
        "beats": [
            "The neat woman with the little black book makes a small tick against a name and glances up at someone across "
            "the room, who suddenly finds his drink very interesting.",
            "The neat woman with the little black book licks her pencil, writes a figure, crosses it out, and writes it "
            "again a copper higher.",
            "The neat woman with the little black book checks the watch pinned to her coat, then the door, then the "
            "watch again.",
            "Alone for a moment, the neat woman takes a second, slimmer book from inside her coat, writes one line, and "
            "puts it away before anyone could be sure they saw it.",
        ],
    },

    # ---- Ott Fennick (new) --------------------------------------------------------------------------------------
    "Ott Fennick": {
        "look": "A big, sandy-haired man with a nose broken and set crooked, slow pale eyes, a black band round one arm "
                "and a claw hammer at his belt beside a cudgel. He moves like a cart: slowly, then all at once.",
        "seen_as": "the big sandy man with the crooked nose",
        "brief": "You are Ott Fennick, the elder of the Fennick brothers, Dominico's men. You grew up in the Back Lanes, "
                 "sons of a cooper; when the cooperage burned you carried your little brother Jory out through the smoke, "
                 "and you have been carrying him since. You collect coppers from the Night Market stalls for the Fist, "
                 "walk Harbour Street with Jory looking hard, and lift what Sabeth Crane says to lift: ten copper a "
                 "night. Tonight, at the bell, you go to the Stripperwitch with Tully and Jory to break things, not "
                 "people; at the one o'clock tide the two of you nail the lid on the crate in the bonded warehouse and "
                 "carry it aboard the Emerald Eye. The crate coughs. Crates don't cough. You save every copper in a jar "
                 "buried in the burnt yard, a third full, toward a little fishing boat with a red sail, to get Jory out "
                 "of the Fist before his mouth gets them killed. Phillip Everuex, the powdered noble at the Apothecary, "
                 "paid you both a gold, with five more each for finding a pale, dark-haired woman with a bow; Jory took "
                 "it first, and you took yours so he wouldn't be alone in it. You think it a bad idea: Dominico kills "
                 "men for side money. You fear that, and Jory dying. You like Sabeth (fair) and Brask; you dislike the "
                 "toff. Voice: slow, few words, literal. 'Hm. Yeah.' 'Ask Jory. He talks.'",
        "scheme": "Save enough for a fishing boat with a red sail and get his brother out of the Fist before Jory's mouth "
                  "gets them both killed; meanwhile keep the Everuex gold quiet and hope they never find the woman.",
        "purse": 30,
        "dialog": {
            "name|names|called|introduce|yourself": "\"Ott.\" A long pause. \"Fennick. Ott Fennick.\" He nods toward "
                "the wiry one. \"Jory's the other one.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "He looks at you for a while. \"Evening.\" He seems to "
                "consider that enough.",
            "from|born|homeland|lanes|grew|origin|father|da|home": "\"Here. The back lanes. Da was a cooper. Barrels.\" "
                "He looks at his big hands. \"Shop burned. I carried Jory out. He was small then.\" A pause. \"Talked "
                "then, too.\"",
            "work|job|jobs|hire|employ|collect|collecting|market": "\"Collect from the stalls. Walk the street. Lift what "
                "Sabeth says lift.\" An enormous shrug. \"Pays.\"",
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": "\"Ogre's cheap. Omberhulk's got bugs.\" He "
                "thinks it through. \"Both got bugs.\"",
            "drink|drinks|ale|rum|mead|thirsty|beer": "\"Small beer. Keeps your hands steady.\" He holds one out. It is "
                "very steady.",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "He goes the colour of old porridge. \"The crate. We were going to nail...\" He stops. \"Need to "
                        "find Jory.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"Don't hear news. Hear orders.\""},
            "doing|busy|up|plans|plan|waiting": "\"Whatever Sabeth says.\" He counts on thick fingers. \"Bell at "
                "midnight. Tide at one. Then beer.\"",
            "boat|boats|fishing|savings|save|saving|jar|sail": "Something almost like a smile. \"Fishing boat. Little one. "
                "Red sail. Got a jar, buried, nearly a third full.\" He looks at you hard. \"Didn't say where.\"",
            "jory|brother|younger": "\"Jory talks. I lift.\" A slow frown. \"Jory talks too much. To the wrong people.\"",
            "crate|warehouse|hammer|nails|tide|nail|lid": "He touches the claw hammer on his belt without seeming to know "
                "he's doing it. \"Lid goes on at the tide. Me and Jory. Long nails.\" His jaw works. \"It coughs. Crates "
                "don't cough.\"",
            "everuex|phillip|toff|noble|woman|bow|locket|picture|gold": "His face shuts like a door. \"Don't know any "
                "woman.\" Then, lower: \"Jory took the toff's gold first. I only took mine so he wouldn't be alone in "
                "it.\"",
            "dominico|boss|sabeth|fist": "\"Mister Dominico pays on time. Don't lie to him.\" He looks at the floor. "
                "\"Don't let him find out you lied.\"",
            "midnight|bell|stripperwitch|velvet|gog|mirror": {
                "line": "\"Just a message.\" He looks at his knuckles. \"Nobody died. That was the message.\"",
                "if_state": {"guild_hit": True},
                "else": "\"Midnight we go to the velvet place. Break things. Not people.\" He thinks. \"Not many "
                        "people.\""},
        },
        "default_line": [
            "He thinks about it for a long time. \"Ask Jory. He talks.\"",
            "\"Hm.\" He folds his arms, which takes up most of the room.",
            "He looks at you, then at the claw hammer on his belt, then at you again. \"No.\"",
            "\"Don't know.\" He says it slowly, as if checking. \"No. Don't.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "docks",
             "go": "The big sandy man with the crooked nose straightens up off the pump and walks down toward the docks, "
                   "the claw hammer swinging at his belt.",
             "doing": "He stands by the bonded warehouse door with a lantern and his claw hammer, waiting for the tide "
                      "like a man waiting for a bell."},
            {"at": 1.5, "place": "ogre",
             "go": "The big sandy man with the crooked nose wipes his hands on his trousers for a long time and walks "
                   "up off the pier.",
             "doing": "He drinks small beer at the bar with his back to the room, saying nothing, opening and closing his "
                      "hands."},
            {"at": 2.0, "place": "apothecary",
             "doing": "He waits by the kitchen door of the grand house with his cap in his big hands to be paid, as "
                      "patient as furniture."},
            {"at": 3.0, "place": "lanes",
             "go": "The big sandy man with the crooked nose puts his wages inside his shirt and goes home.",
             "doing": "He sleeps in a lean-to in a burnt-out cooper's yard, on his back, boots on, one hand on the "
                      "cudgel.",
             "beats": ["In a burnt-out cooper's yard a big man sleeps on his back in a lean-to, one hand on a cudgel, as "
                       "still as a felled tree."]},
            {"at": 14.0, "place": "lanes",
             "doing": "He sits in the shade of the burnt yard digging a small hole, putting something in it and filling it "
                      "in again, looking over his shoulder."},
            {"at": 17.0, "place": "harbour",
             "doing": "He walks Harbour Street with his brother, stopping to look at a fishing boat for sale with his "
                      "mouth slightly open."},
            {"at": 20.0, "place": "market",
             "doing": "He stands at each stall while his brother talks, and the stallholders pay a copper faster than "
                      "they meant to."},
            {"at": 22.25, "place": "harbour",
             "doing": "He strolls Harbour Street in step with his brother, nodding to shopkeepers who nod back too "
                      "fast."},
            {"at": 23.75, "place": "square",
             "go": "The big sandy man with the crooked nose taps his brother on the shoulder and walks up toward the "
                   "square.",
             "doing": "He leans on the town pump with two other hard men, cracking his knuckles one at a time, watching "
                      "the door with the red lamp across the square."},
        ],
        "beats": [
            "The big sandy man with the crooked nose cracks his knuckles one at a time, slowly, the way other men count.",
            "The big sandy man with the crooked nose touches the claw hammer at his belt, takes his hand away, and "
            "touches it again.",
            "The wiry lad beside the big sandy man says something quick and funny; the big man doesn't laugh, but he "
            "puts one big hand on the back of the lad's neck, gently.",
            "The big sandy man with the crooked nose watches a red sail in the lamplight for a long time, then looks away "
            "as if caught.",
        ],
    },

    # ---- Jory Fennick (new) -------------------------------------------------------------------------------------
    "Jory Fennick": {
        "look": "A wiry young man with the same sandy hair as the big one, a gap-toothed grin, a black band on his arm "
                "and a cheap brass locket he keeps flipping open and shut. His eyes reach every purse in the room before "
                "they get to faces.",
        "seen_as": "the wiry sandy lad with the gap teeth",
        "brief": "You are Jory Fennick, the younger Fennick, Dominico's man and nobody's fool, you think. A cooper's son "
                 "from the Back Lanes: when the shop burned you were six, and you say you walked out, though Ott says he "
                 "carried you. You collect market coppers with Ott, look hard on Harbour Street, and lose your ten copper "
                 "a night at dice in the Ogre's corner. Four nights ago you and Brask walked a big grey-bearded 'debtor' "
                 "down the pier, and you lifted a brass compass with a ship's wheel on the lid out of his coat and sold "
                 "it to Marlo the fence for eight silver; you have not told a soul. Phillip Everuex, the sweating noble at "
                 "the Apothecary, paid you a gold, five more on finding her, to look for a pale, dark-haired woman with a "
                 "bow, and gave you a painted locket of her. You show it in the Omberhulk and the Ogre. A little tusked "
                 "street child told you she was at the Touchy Unicorn; you went three times. Tonight's scheme: at the "
                 "bell, while the others smash the Stripperwitch, slip upstairs and try the doors. Hessa never lets you "
                 "past her door; tonight she won't have a choice. Then five gold, and the dice will turn. You fear Ott's "
                 "disappointment and Dominico; you do not know enough to fear the woman. You like Ott, dice and gold; you "
                 "dislike Sabeth, who watches you, and Hessa. Voice: quick, cocky, wheedling. 'Swear down.' 'Tell you "
                 "what.'",
        "scheme": "Earn Phillip Everuex's five gold by finding the dark-haired woman with the bow: at the midnight bell, "
                  "while the others smash the Stripperwitch, slip upstairs and try the doors. Meanwhile keep quiet that "
                  "he lifted the prisoner's brass compass and sold it to Marlo.",
        "purse": 60,
        "dialog": {
            "name|names|called|introduce|yourself": "\"Jory Fennick, at your service, for a fee.\" The gap-toothed grin. "
                "\"The wardrobe's my brother. Ott.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"Evening, evening! Tell you what, you've got a lucky "
                "face.\" He rattles a pocket. \"Dice?\"",
            "from|born|homeland|lanes|grew|origin|father|da|home": "\"Back lanes, born and bred. Da's cooperage burned "
                "down when I was six. I walked out of it.\" He flips the locket shut. \"Ott says he carried me. Ott "
                "remembers it wrong.\"",
            "work|job|jobs|hire|employ|collect|collecting": "\"Bit of collecting, bit of walking about looking hard, bit "
                "of lifting. Pays a silver every few nights, which is criminal.\" He laughs. \"Well. Yeah.\"",
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": "\"Ludo's Honeymoon Suite, if you like chickens. "
                "Or the Omberhulk, if you like company in the bed that isn't people.\" He grins. \"Bugs. I mean bugs.\"",
            "drink|drinks|ale|rum|mead|thirsty|beer": "\"I'll have whatever you're buying. Swear down, I'll get the next "
                "one.\" He won't.",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "He stops flipping the locket. \"The mayor? In the crate? Swear down, nobody told us.\" His hand "
                        "goes to a pocket that is empty now. \"Oh, that's bad. That's really bad.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"News? Midnight's going to be lively at the velvet place, you didn't hear it from me. And a "
                        "siren's singing.\" He leans in. \"And I'm looking for someone. Pays well, finding her.\""},
            "doing|busy|up|plans|plan": "\"Bit of this. Bit of looking for someone.\" He taps the locket. \"Bit of "
                "dice, after.\"",
            "locket|picture|portrait|painting|woman|lady|search|searching|find|seen": "He flicks the locket open: a tiny "
                "painted woman, pale, dark-haired, hard about the mouth. \"Seen her? Bow, cloak, doesn't smile. There's a "
                "gold in it if you have.\" He snaps it shut. \"Little bird said the Unicorn. Little bird might be a "
                "liar.\"",
            "everuex|phillip|toff|noble|powdered|paid|gold|money": "\"What toff?\" Too quick. \"Don't know any toff. Never "
                "been paid by a toff in my life.\" He jingles. \"Inherited this.\"",
            "compass|brass|wheel|stole|stolen|pocket|marlo|fence|sold": "His hand goes to an empty pocket. \"Never had a "
                "compass. Never sold one to a Xoton on Harbour Street neither, for eight silver, which was robbery.\" He "
                "hears himself. \"Forget that.\"",
            "crate|warehouse|debtor|tide|klhyt|mayor|prisoner": "\"A debtor, they said. Me and Brask walked him down the "
                "pier, four nights back.\" A thin laugh. \"Big fella. Grey beard. Talked like a ship's master. Funny sort "
                "of debtor.\"",
            "ott|brother|wardrobe|big": "\"Ott? Ott's all right. Ott's saving for a boat. A boat!\" He laughs, then "
                "doesn't. \"He'll get it, too. He always gets the thing.\"",
            "dice|game|gamble|gambling|bet|wager|luck|lucky": "\"Dice at the Ogre, the corner table. I'm due.\" He nods "
                "seriously. \"I've been due for about a month.\"",
            "midnight|bell|stripperwitch|velvet|gog|upstairs|guests": {
                "line": "\"Smashed it up proper. I had a look upstairs while the others were busy.\" The grin slips. "
                        "\"Locked doors. Good locks. Somebody up there pays for good locks.\"",
                "if_state": {"guild_hit": True},
                "else": "\"Midnight we pay the velvet place a visit. Me, I'm thinking I'll have a look upstairs while "
                        "everyone's busy.\" He winks. \"Rooms up there. Guests.\""},
            "hessa|door|doorwoman|lizard": "\"That lizard on the velvet door won't let me in. Says no like she's been "
                "practising.\" He scowls. \"Midnight she won't have a choice.\"",
            "dominico|boss|sabeth|fist|crane": "\"Mister Dominico? Pays on time, and you don't want to be the thing he's looking at.\" He lowers his voice. \"Don't mention any toffs to him. Swear down. Sabeth writes everything down, and he reads it.\"",
        },
        "default_line": [
            "\"Tell you what, ask me that after I've won something.\" He rattles a pocket that doesn't rattle much.",
            "He grins with the gap in his teeth. \"Swear down, no idea. Ask Ott. Ott won't know either, but he'll take "
            "longer.\"",
            "He flips the locket open, glances at it, snaps it shut. \"Busy, friend. Busy looking.\"",
            "\"What's it worth?\" He holds out a palm, cheerfully. \"No? Then I don't know.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "docks",
             "go": "The wiry sandy lad with the gap teeth hops off the trough and follows his brother down toward the "
                   "docks.",
             "doing": "He sits on a bale by the bonded warehouse with a lantern at his feet and a fistful of long nails, "
                      "and for once nothing to say."},
            {"at": 1.5, "place": "omberhulk",
             "go": "The wiry sandy lad with the gap teeth shakes off the pier like a wet dog and goes up toward the "
                   "square.",
             "doing": "He goes table to table showing a little painted picture in a brass locket, buying drinks for "
                      "anyone who will look at it."},
            {"at": 2.25, "place": "apothecary",
             "go": "The wiry sandy lad with the gap teeth remembers he is owed money and goes off at a trot.",
             "doing": "He waits at the foot of the grand staircase to be paid, picking his teeth with a splinter and "
                      "pricing the woodwork with his eyes."},
            {"at": 3.0, "place": "square",
             "doing": "He sits on the Town Hall steps in the dark, flipping the locket open and shut, watching the "
                      "upstairs windows of the house with the red lamp."},
            {"at": 4.5, "place": "lanes",
             "doing": "He sleeps curled in the burnt-out cooper's yard under a sack, the locket in his fist.",
             "beats": ["In a burnt-out yard someone mutters 'I'm due' in his sleep and turns over."]},
            {"at": 14.0, "place": "ogre",
             "doing": "He loses at dice in the corner of the shuttered bar, cheerfully, and borrows to lose again."},
            {"at": 17.0, "place": "harbour",
             "doing": "He walks Harbour Street beside his brother, talking enough for both of them."},
            {"at": 20.0, "place": "market",
             "doing": "He talks a copper out of every stall in the lane, cheerful and wheedling, while his big brother "
                      "stands behind him being big."},
            {"at": 22.25, "place": "harbour",
             "doing": "He strolls Harbour Street in step with his brother, flipping a brass locket and eyeing every purse "
                      "that passes."},
            {"at": 23.75, "place": "square",
             "go": "The wiry sandy lad with the gap teeth pockets the locket and skips up toward the square.",
             "doing": "He sits on the edge of the pump trough flipping a brass locket open and shut, his eyes on the "
                      "upstairs windows of the house with the red lamp."},
        ],
        "beats": [
            "The wiry sandy lad with the gap teeth flips a brass locket open, shows it to someone, gets a shake of the "
            "head, and snaps it shut again.",
            "The wiry sandy lad palms a coin off the bar that might have been his, and looks innocently at the ceiling.",
            "The wiry sandy lad laughs at his own joke before he has finished telling it, and the big man beside him "
            "doesn't laugh at all.",
            "The wiry sandy lad's hand goes to an empty pocket, pats it, and he frowns, as if remembering something he "
            "sold.",
        ],
    },

    # ---- Hessa (new) --------------------------------------------------------------------------------------------
    "Hessa": {
        "look": "A tall, green-scaled Lizardfolk woman with tribal marks in white clay along her jaw, one eye milky and "
                "the other gold. She stands in a doorway so still that people walk into her, a long iron-hooked fishing "
                "gaff within reach.",
        "seen_as": "the green lizardwoman with the gaff",
        "brief": "You are Hessa, of the Meters, the green Lizardfolk who talk to outsiders. You come from a fishing "
                 "village on stilts three tides up the coast, where your mother mends nets with fishbone needles; a "
                 "stingray took your left eye when you were small. You came to the Refuge with your brother to sell the "
                 "catch. One night at the Turtle Dragon, where they had started serving Lizardfolk last, a sailor put a "
                 "knife in your brother's arm and nobody moved, until Fat Gog stood up across the room, and the sailor "
                 "sat down. Gog offered you his door. You keep it now: who comes into the Stripperwitch comes in by you, "
                 "and who goes out drunk goes out gently. Gog pays you twenty copper at four in the morning; you send half "
                 "up the coast with Ssark's boats and spend the rest on rum at the Turtle with your own people, and on "
                 "white clay. You love the old one's harmony and fear for it: up north the blue Mandrills talk of a "
                 "calling to war, and if it comes you must choose. The bar woman walks out alone before dawn; once you "
                 "followed as far as the rocks past the pier, lost her, and decided her tides are not yours to know. "
                 "Jory Fennick tries your door every night. You like Gog, River, Wick and "
                 "Ssark; you dislike the Fist. Voice: short, literal, no contractions, present tense; humans are 'warm "
                 "ones', Gog is 'the old one'. 'Inside, or outside.' 'No. That is a whole answer.'",
        "scheme": None,
        "purse": 20,
        "dialog": {
            "name|names|called|introduce|yourself": "\"Hessa.\" She touches the white clay on her jaw. \"Of the Meters. "
                "Green. We are the ones who talk to outsiders. I talk little. I am still Meters.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "Her gold eye moves to you; the milky one stays on the "
                "street. \"Evening, warm one. Inside, or outside. Choose before the door does.\"",
            "from|born|homeland|village|meters|tribe|coast|origin|home|mother": "\"Up the coast, three tides by boat. A "
                "village on stilts. My mother mends nets there with fishbone needles.\" A slow blink. \"I send her half of "
                "what the old one pays me.\"",
            "work|job|jobs|hire|employ|door|doorwoman|bouncer|enter|inside|entry|come": "\"I keep the door. Who comes in comes in by me. Who goes "
                "out drunk goes out by me, gently.\" She glances at the gaff. \"Or less gently.\"",
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": "\"Rooms upstairs here, a silver. The bar woman "
                "keeps them. If you have less, the Omberhulk. If you have nothing, the Ogre, and keep your boots on.\"",
            "drink|drinks|ale|rum|mead|wine|thirsty": "\"I do not drink on the door. After the door, rum at the Turtle with "
                "my own. The barman serves us last.\" A slow blink. \"I notice.\"",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "She touches a fresh cut along her arm. \"At the bell they came. Four. I put one down. Then the "
                        "old one said let them, and I let them.\" Her tail lashes once. \"I do not like let them.\"",
                "if_state": {"guild_hit": True},
                "else": "\"Dominico's warm ones come at midnight, the bar woman says. The old one says nothing.\" She "
                        "runs a claw along the gaff's hook. \"I sharpen.\""},
            "doing|busy|up|plans|plan|waiting": "\"Standing. Counting who goes in. Counting who comes out. By morning "
                "the numbers should be the same.\"",
            "gog|fat|old|lizardman|boss": "Her voice goes low with respect. \"The old one. A sailor put a knife in my "
                "brother at the Turtle and nobody moved. The old one stood up across the room, and the sailor sat down. "
                "That is all.\" A slow blink. \"Since then, I keep his door.\"",
            "river|bar|barkeep|walk|walks": "\"The bar woman is good to me. She walks out before the sun, most nights, "
                "alone.\" Her gold eye does not move. \"The old one's woman has her own tides. I do not follow them. Not "
                "any more.\"",
            "lizardfolk|lizards|harmony|humans|warm|tension|turtle": "\"The old one says lizard and warm one, same room, "
                "same rum. In his house it is true. At the Turtle it is true until someone drinks too much.\"",
            "war|calling|mandrills|north|mandrill|blue": "Her milky eye seems to look further than the street. \"Up north "
                "the blue ones talk of a calling. War, to clear the coast.\" A long silence. \"If it comes, I must "
                "choose. I do not want to choose.\"",
            "jory|fennick|fennicks|ott|dominico|fist": "\"The small loud one with the gap in his teeth tries my door every "
                "night. Every night: no.\" She shows a great many teeth. \"Tonight he says I will have no choice. We will "
                "see.\"",
            "wick|child|kid|girl": "\"The little tusked one. I feed her fish. She tells me who is coming before they "
                "come.\" Something like a smile. \"Good eyes. Bad manners.\"",
            "eye|blind|milky|tattoo|tattoos|clay|marks|scales": "\"The eye? A stingray, when I was small. It sees shapes. "
                "Shapes are enough on a door.\" She touches the white clay. \"The marks are my mother's, and her "
                "mother's. They wash off. I put them back.\"",
            "guest|guests|upstairs|bow|woman": "\"Guests upstairs are the old one's guests. I do not count them out "
                "loud.\"",
        },
        "default_line": [
            "Her gold eye considers you; the milky one stays on the street. \"No.\" A pause. \"That is a whole answer, "
            "warm one.\"",
            "\"Inside, or outside.\" She does not move out of the doorway. \"Talking is for inside.\"",
            "She tilts her head, a slow lizard's tilt. \"Ask the bar woman. She has more words. I have a door.\"",
            "\"Hm.\" She shifts the gaff from one hand to the other. \"Say it smaller.\"",
        ],
        "routine": [
            {"at": 0.0, "place": "stripperwitch",
             "doing": "She stands square in the doorway as the midnight bell goes, the long gaff in her hand now and not "
                      "against the wall, her tail very still."},
            {"at": 1.0, "place": "stripperwitch",
             "doing": "She stands at the door letting people in one at a time with a nod or a word, the long gaff "
                      "leaning against the frame beside her."},
            {"at": 2.0, "place": "stripperwitch",
             "doing": "She sees the drunks out gently, one at a time, steering them by the collar like boats into a "
                      "current."},
            {"at": 4.25, "place": "turtle",
             "go": "The green lizardwoman with the gaff touches two claws to her brow toward the big table, and goes out "
                   "into the street.",
             "doing": "She drinks rum slowly at the Lizardfolk table by the door, back to the wall, saying almost "
                      "nothing.",
             "pay": {"to": "Bosun Maggs", "cp": 2, "for": "rum"}},
            {"at": 5.0, "place": "docks",
             "doing": "She sits on the end of the pier with her feet in the black water, watching the fishing boats go "
                      "out and naming each one under her breath."},
            {"at": 7.0, "place": "lanes",
             "doing": "She lies in a hammock slung across a sunny yard, perfectly still, soaking up the heat like a "
                      "stone.",
             "beats": ["In a sunny yard a green lizardwoman lies in a hammock so still that a lizard, a small ordinary "
                       "one, climbs onto her chest to share the sun."]},
            {"at": 19.5, "place": "stripperwitch",
             "go": "The green lizardwoman with the gaff rolls out of her hammock, stretches until her spine clicks, and "
                   "goes up toward the square.",
             "doing": "She takes her place in the doorway as the lamps are lit, and the evening's first callers find "
                      "themselves standing up straighter."},
            {"at": 22.5, "place": "stripperwitch",
             "doing": "She stands at the door letting people in one at a time with a nod or a word, the long gaff "
                      "leaning against the frame beside her."},
        ],
        "beats": [
            "The green lizardwoman with the gaff puts one hand flat on a drunk's chest; he stops, thinks about it, and "
            "goes home.",
            "The green lizardwoman's milky eye stays on the street while the gold one follows someone across the room, "
            "all the way to the bar.",
            "The green lizardwoman with the gaff tastes the air with a flick of her tongue, and turns to the door a moment "
            "before someone comes through it.",
            "A barefoot child with new tusks slips past the green lizardwoman's knees; she lets her, and drops a strip of "
            "dried fish into the child's hand as she goes.",
        ],
    },

    # ---- Wick (new) ---------------------------------------------------------------------------------------------
    "Wick": {
        "look": "A barefoot Jonulvicha girl of about ten, all elbows and knees, tusks just coming through, hair tied up "
                "with tarred string and a little knife in her waistband. She is never quite where you last saw her.",
        "seen_as": "the barefoot child with new tusks",
        "brief": "You are Wick, ten years old, Jonulvicha, Fat Gog's eyes and messenger in the Night Market and the "
                 "square. Your mother hauled cargo for Ruk Halfhand on the docks and died of the fever two wet seasons "
                 "ago; you remember her lifting you onto a stack of crates to watch the Moonmoth come in. You sleep on a "
                 "sack under the Town Hall porch, where the clerks drop crusts, with a tin box of coppers you are saving "
                 "for her stone, a proper one, with letters. You run messages, report to Big Gog at a quarter past "
                 "midnight for three copper and a listening-to, and sell news to anyone: a copper a rumour, a silver for "
                 "a true thing. You see everything at knee height. The lady with the bow at the velvet house taught you "
                 "to throw a knife and "
                 "gave you a mango, so when Jory Fennick showed you a painted locket and paid you a copper, you sent him "
                 "to the Touchy Unicorn, which was a lie, and you have kept him going the wrong way since, at a copper a "
                 "lie. You are frightened of the man in the grey coat, who says street children should go to the Catan "
                 "workhouse on a ship. You like Big Gog, Hessa (fish), Mother Ines (bruised mangoes), Kael (his hat) "
                 "and the lady with the bow; you dislike Jory, who pinches. Voice: fast, run-on, everything priced, "
                 "'mister', 'swear on my tusks'. 'That's free. Everything else is a copper.' 'Knowing's one copper. "
                 "Finding out's two.'",
        "scheme": "Keep sending Jory Fennick the wrong way about the lady with the bow, a copper a lie, and fill her tin "
                  "under the Town Hall porch until there is enough for her mother's stone.",
        "purse": 7,
        "dialog": {
            "name|names|called|introduce|yourself": "\"Wick.\" She sticks out a grubby hand, then takes it back before you "
                "can shake it. \"That's free. Everything else is a copper.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"Evening, mister! Or missus. Or whatever.\" She bounces "
                "on her heels. \"Want to know something? Everything's a copper. True things are a silver.\"",
            "from|born|homeland|mum|mother|mam|family|parents|origin|home": "\"Here! Born on the docks, under a tarp. Mum "
                "hauled for Ruk Halfhand.\" She says the next part quickly, the way you'd pull a splinter. \"She died of "
                "the fever two wet seasons back. I'm saving for her stone. A proper one. With letters.\"",
            "work|job|jobs|hire|employ|errand|errands|message|messages|runner": "\"I run messages. A copper across the "
                "square, two to the docks, three if it's raining or someone's chasing me. I work for Big Gog, mostly.\" "
                "She glances round. \"Don't tell him I said mostly.\"",
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": "\"Under the Town Hall porch, me. It's dry and the "
                "clerks drop crusts. You want a bed? The Omberhulk's a copper, bugs included. The Unicorn's a copper and "
                "you have to be quiet, which I can't.\"",
            "drink|drinks|ale|rum|water|thirsty|coconut": "\"Water's free at the pump in the square. Coconut's a copper "
                "off Mother Ines. Rum's for big people.\" She sniffs. \"And they still can't handle it.\"",
            "news|rumour|rumours|gossip|word|heard|happening|secret|secrets": {
                "line": "\"The mayor's back! I saw him first! Well, second. Well, I saw him.\" She bounces. \"That's free. "
                        "Everybody knows.\" She scowls. \"Rubbish news, everybody knowing it.\"",
                "if_state": {"klhyt_home": True},
                "else": "She holds out a palm, then decides you look honest and talks anyway. \"The man in the grey coat "
                        "goes in the velvet house's side door every night and comes out pleased. Dominico gave Big Gog "
                        "till midnight. And the boat with the green eye is sitting low for a boat with one crate on her "
                        "list.\" The palm is still out."},
            "doing|busy|up|plans|plan": "\"Watching. Listening. Running. Eating a mango if anyone's got one.\" She "
                "looks at you hopefully. \"Has anyone got one?\"",
            "gog|fat|big|boss|lizard|lizardman": "\"Big Gog's the best. He pays three coppers a night, and he listens like "
                "you're the magistrate.\" She lowers her voice. \"Hessa on his door gives me fish.\"",
            "bow|lady|woman|deloris|archer|cloak": "Her face closes up tight as a fist. \"Don't know any lady with a bow.\" "
                "A pause. \"If I did, she'd have taught me to throw a knife, and I'd be very good at it now.\" Her hand is "
                "on the little knife in her waistband.",
            "jory|fennick|fennicks|ott|locket|picture|sandy": "She snorts. \"Jory Fennick paid me a copper to find a lady "
                "in a locket. I told him the Unicorn.\" A grin, tusks and all. \"She's not at the Unicorn. He went three "
                "times. I'm rich.\"",
            "market|stalls|ines|grusha|saelwyn|hallvard|mango|mangoes": "\"Mother Ines gives me the bruised mangoes. "
                "Grusha's pepper sauce makes grown men cry, I've seen it. The elf lady with the tea won't look at anyone in "
                "a uniform. And the Xoton with the salt beard sells rope that never frays.\" She considers. \"He says.\"",
            "square|pump|watch|harrow|fitch|quint|constable|constables|sergeant": "\"The watch walks the square on the "
                "hour, near enough. Sergeant Harrow's slow, Constable Fitch is slower, and Constable Quint can catch me.\" "
                "Solemnly: \"So I'm nice to her.\"",
            "custodian|grey|workhouse|catan|hall": "She steps back a pace. \"The man in the grey coat says children on the "
                "street ought to go to the workhouse in Catan, on a ship.\" Very small: \"I don't want to go to Catan in a "
                "ship.\"",
            "kael|hat|glaive|jonulvicha|tusks": "\"Kael lets me wear his hat! It comes down to my nose. He says I'm a fine "
                "Jonulvicha.\" She lifts her chin. \"I said I know.\"",
            "copper|coppers|pay|price|silver|coin|money|tip": "\"A copper for a rumour, a silver for a true thing, and a "
                "mango for anything at all, if it's ripe.\" She holds out a hand. \"I take all three.\"",
            "dominico|fist|black|coat|sabeth|collector": "She stops bouncing. \"The black coat? Don't look at him, mister. His lady with the little book takes a copper off every stall in the market, and writes it down, and remembers.\" Quieter: \"She remembered me once.\"",
        },
        "default_line": [
            "\"Don't know that one, mister. Swear on my tusks.\" She is already looking past you at someone's dropped "
            "copper.",
            "She holds out a grubby palm. \"That one's a copper. No copper, no news. That's business.\"",
            "\"Ask Big Gog! Or don't, he'll ask you something back.\" She skips off three steps and comes back. \"I'm "
            "still here.\"",
            "She chews her lip. \"I could find out. Finding out's two coppers, though. Knowing's only one.\"",
        ],
        "routine": [
            {"at": 0.25, "place": "stripperwitch",
             "go": "The barefoot child with new tusks hops off the pump and is gone across the square at a run.",
             "doing": "She sits on the floor by the huge old lizardman's table, whispering up at him while he listens as "
                      "if she were a magistrate."},
            {"at": 0.75, "place": "docks",
             "go": "The barefoot child with new tusks slips out of the side door like a cat.",
             "doing": "She sits on a pile of nets near the brigantine with the green eye, mending nothing, watching the "
                      "warehouse door with her chin on her knees."},
            {"at": 1.5, "place": "market",
             "doing": "She runs messages between the stalls for a copper a time, and sometimes for a bruised mango "
                      "instead."},
            {"at": 3.0, "place": "square",
             "go": "The barefoot child with new tusks yawns enormously and trots off toward the Town Hall.",
             "doing": "She sleeps curled on a sack under the Town Hall porch, one hand on the little knife and one on a "
                      "tin box.",
             "beats": ["Under the Town Hall porch a small shape on a sack mutters 'that's a copper' in her sleep."]},
            {"at": 9.0, "place": "harbour",
             "doing": "She runs errands for the shops on Harbour Street and eats the end of everybody's bread."},
            {"at": 12.0, "place": "square",
             "doing": "She sleeps in the shade under the Town Hall porch, out of the heat, a cat curled against her "
                      "back."},
            {"at": 17.0, "place": "market",
             "doing": "She helps the fruit seller stack her mango pyramids as the market sets up, and eats the bruised "
                      "ones."},
            {"at": 22.5, "place": "market",
             "doing": "She weaves through the crowd at knee height, barefoot and quick, listening to everything."},
            {"at": 23.5, "place": "square",
             "doing": "She sits on the town pump's handle swinging her legs, watching who goes in and out of every door on "
                      "the square."},
        ],
        "beats": [
            "The barefoot child with new tusks ducks under a stall, comes up the other side with a bruised mango, and is "
            "eating it before anyone can decide whether it was stolen.",
            "The barefoot child with new tusks tugs a stranger's sleeve, whispers something, holds out a palm, and gets a "
            "copper; the stranger looks both pleased and robbed.",
            "The barefoot child with new tusks throws her little knife at a post when she thinks nobody is watching, and "
            "hits it every time.",
            "The barefoot child with new tusks watches a wiry sandy lad with a locket go by, and points him, very "
            "helpfully, the wrong way.",
        ],
    },

    # ---- Marlo (new) --------------------------------------------------------------------------------------------
    "Marlo": {
        "look": "A barrel-bodied, black-skinned Xoton with a chin as bare as a boy's and a jeweller's loupe on a ribbon "
                "round his neck. He wears fingerless gloves, keeps his back to the water, and goes faintly grey whenever "
                "anything rocks.",
        "seen_as": "the barrel-bodied man with the loupe",
        "brief": "You are Marlo, a Xoton born on the Crows Nest and sick over its rail every day for eleven years; your "
                 "mother held your head and said some fish are born to swim on land. You came ashore at the Refuge "
                 "fifteen years ago and never went back. A Xoton's beard grows at sea, so you have none. You run Marlo's "
                 "Second Chances on Harbour Street, second-hand ship's goods, and behind it you fence: you buy what has "
                 "no story for a third of its worth and send it out as 'ballast' with passing Xoton traders, whose "
                 "sailors you pay in their own tongue. You pay Fat Gog forty copper every night at a quarter past three, "
                 "and in return nothing falls off his ships and nothing falls on your head. Your secret: four nights ago "
                 "Jory Fennick sold you a brass sea-compass with a ship's wheel on the lid for eight silver, and you knew "
                 "it at once for the mayor's, the one thing he brought ashore. Buying from Dominico's men breaks Gog's "
                 "rule, so you have told nobody, and you mean to sell it to a Xoton captain bound out of the harbour "
                 "before anyone asks. You fear Gog's displeasure, the sea, and the day the mayor comes home. You like "
                 "Gog, River (she buys bottles) and Wick (useful); you dislike Jory, and boats. Voice: a fussy appraiser, "
                 "soft, 'mm-hm', 'provenance', 'let's call it'. 'Everything pre-owned, nothing pre-stolen. So far as I "
                 "know.' 'Provenance is just a story with the boring parts left out.'",
        "scheme": "Sell the mayor's brass compass, bought from Jory Fennick four nights ago, to a Xoton captain bound out "
                  "of the harbour before anyone, Gog above all, learns he bought it from Dominico's men.",
        "purse": 350,
        "dialog": {
            "name|names|called|introduce|yourself": "\"Marlo.\" He offers a gloved hand and checks your rings while you "
                "shake it. \"Marlo's Second Chances, Harbour Street. Everything pre-owned, nothing pre-stolen.\" A small "
                "cough. \"So far as I know.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"Evening, evening.\" He squints at you through the "
                "loupe as if you were a pearl of uncertain water. \"Buying, selling, or lost?\"",
            "from|born|homeland|crows|nest|xoton|zoton|origin|home": "\"Xoton, with the X, yes, thank you. Born on the "
                "Crows Nest and sick over the rail of it every day for eleven years.\" He goes a little grey at the "
                "memory. \"My mother said some fish are born to swim on land. I swam here.\"",
            "beard|beardless|chin|shave|shaved": "He touches his bare chin. \"A Xoton's beard grows at sea. I was at sea "
                "eleven years and grew nothing but a very bad temper.\"",
            "work|job|jobs|hire|employ|shop|chandlery|trade|business": "\"Second-hand ship's goods. Sextants, lamps, "
                "boots, a very good hat. Everything has had a life before it came to me.\" He smiles. \"Provenance is "
                "just a story with the boring parts left out.\"",
            "fence|stolen|sell|selling|buy|buying|goods|hot|loot": "His voice drops a little. \"If you had something to "
                "sell that you'd rather not explain, I'd look at it. I don't ask. I appraise.\" He taps the loupe. \"Let's "
                "call it a third of what it's worth, and no story at all.\"",
            "gog|fat|cut|guild|boss": "\"I pay Gog a cut every night, a quarter past three, like a clock.\" He adjusts his "
                "gloves. \"In return nothing falls off his ships, and nothing falls on my head. A very civilised "
                "arrangement.\"",
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": "\"I sleep in the back of my shop with a cash box "
                "for a pillow. I don't recommend it. The Turtle Dragon has rooms for four coppers and is full of my "
                "people, singing.\" He winces. \"Loudly.\"",
            "drink|drinks|ale|rum|wine|tea|thirsty": "\"Mint tea. Anything stronger and the room starts to roll like a "
                "deck, and then, well.\" He swallows. \"Then, well.\"",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "He goes very still, and his hand drifts toward an inner pocket and stops. \"The mayor's back. How "
                        "wonderful. Truly.\" He does not look as if he means wonderful. \"I must check my stock.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"News is merchandise, and I deal in things.\" He considers. \"But a Xoton crew is drinking its way "
                        "from the Turtle to the Ogre, with the watch a tavern behind and losing ground. Hide anything "
                        "breakable.\""},
            "doing|busy|up|plans|plan": "\"Weighing small things on a small scale.\" He holds up a ring to the lamp. "
                "\"Then the Ogre, to buy more small things. Then a visit I make every night at a quarter past three.\"",
            "compass|brass|wheel|nautical|instrument|instruments|sextant": "He doesn't touch his inner pocket. He very "
                "carefully doesn't. \"A compass? I have several. Sextants too. Nothing special.\" The loupe swings on its "
                "ribbon. \"Nothing with any story.\"",
            "jory|fennick|fennicks|ott|fist|dominico": "\"I don't buy from Dominico's men.\" A beat too fast. \"Gog "
                "wouldn't like it, and I always do what Gog likes.\" He frowns. \"Why do you ask about the younger "
                "Fennick? I didn't mention a Fennick.\"",
            "klhyt|mayor|founder": "\"The mayor? A fine man. Carried the compass he came ashore with everywhere he "
                "went.\" He hears himself. \"So I've heard. One hears things.\"",
            "ship|ships|cog|whispers|eirik|captain|hulda|ballast|crew|xotons": "\"Xoton ships come and go and take on "
                "ballast, and sometimes the ballast is very valuable and nobody writes it down.\" He looks out at the "
                "harbour, goes grey, and looks away. \"I don't go aboard. I wave.\"",
            "seasick|seasickness|boat|boats|waves|rocking|sea": "\"Please don't say that word while you're rocking on your "
                "heels like that.\" He grips the counter. \"Thank you.\"",
        },
        "default_line": [
            "He peers at you through the loupe. \"Mm-hm. Mm-hm. No. Not interested. Try the market; they buy anything.\"",
            "\"Let's call that a question I didn't hear.\" He polishes a brass lamp that doesn't need it.",
            "\"I deal in things, not answers.\" He spreads his gloved hands. \"Bring me a thing.\"",
            "He glances at the harbour, goes faintly grey, and turns his back on it. \"Sorry. What? Ask the "
            "harbourmaster. He counts things for free.\"",
        ],
        "routine": [
            {"at": 0.0, "place": "ogre",
             "go": "The barrel-bodied man with the loupe locks his shop's back door twice, tries it, and goes along the "
                   "street.",
             "doing": "He sits in the dice corner not playing, buying small things from people who keep their hands under "
                      "the table."},
            {"at": 1.0, "place": "docks",
             "go": "The barrel-bodied man with the loupe pockets a twist of cloth and goes down toward the docks, "
                   "breathing carefully.",
             "doing": "He stands well back from the edge by the Xoton cog, chatting with her sailors in their own tongue, "
                      "and never once looks at the water."},
            {"at": 2.0, "place": "harbour",
             "go": "The barrel-bodied man with the loupe hands a small oilcloth bundle to a sailor and walks back up off "
                   "the pier very fast.",
             "doing": "He sits in the back of his shuttered shop by one lamp, writing in a ledger with a very small pen."},
            {"at": 3.25, "place": "stripperwitch",
             "go": "The barrel-bodied man with the loupe blows out his lamp, locks up twice, and goes up toward the "
                   "square.",
             "doing": "He sits down at the huge old lizardman's table, slides a heavy little purse across it, and is gone "
                      "again in the time it takes to drink one mint tea.",
             "pay": {"to": "Fat Gog", "cp": 40, "for": "Gog's cut"}},
            {"at": 3.75, "place": "harbour",
             "doing": "His shop is dark; he sleeps in the back on a mattress with a cash box for a pillow.",
             "beats": ["Behind the shutters of a second-hand chandlery a cash box rattles as someone turns over on it."]},
            {"at": 9.0, "place": "harbour",
             "doing": "He sits in his shop doorway in the morning cool among sextants, lamps and boots, appraising "
                      "everyone who walks past through his loupe."},
            {"at": 13.0, "place": "harbour",
             "doing": "His shutters are down against the heat; behind them, the clink of coins being counted."},
            {"at": 17.0, "place": "harbour",
             "doing": "He sits in his shop doorway with his gloves on, polishing a brass lamp and pricing passers-by."},
            {"at": 20.0, "place": "market",
             "doing": "He drifts along the edge of the Night Market, buying odd things from odd people and paying in odd "
                      "coins."},
            {"at": 22.0, "place": "harbour",
             "doing": "He sits in the back of a half-shuttered chandlery with one lamp, weighing small things on a "
                      "jeweller's scale."},
        ],
        "beats": [
            "The barrel-bodied man with the loupe holds a ring up to the lamp, squints at it a long time, and says a "
            "number nobody likes.",
            "A board shifts underfoot, and the barrel-bodied man with the loupe grabs for the counter as if the whole "
            "street were a deck in a swell.",
            "The barrel-bodied man's gloved hand drifts to an inner pocket, rests there, and comes away empty, as if he "
            "had decided against something.",
            "The barrel-bodied man with the loupe wraps something small in oilcloth, ties it with string, and writes "
            "BALLAST on it in a careful hand.",
        ],
    },

    # ---- Ned Tallow (new) ---------------------------------------------------------------------------------------
    "Ned Tallow": {
        "look": "A spare, weathered old man with a long brass-capped pole over one shoulder, an oil can at his belt and "
                "a tarred pigtail down his back. He moves quietly, checks every flame he passes, and one earlobe is "
                "missing, cleanly.",
        "seen_as": "the old man with the lamp pole",
        "brief": "You are Ned Tallow, the town's lamplighter: thirty-seven lamps along the square, Harbour "
                 "Street, the Night Market and the Treeline Road, lit at dusk and put out at dawn, for six copper "
                 "a day from the Town Hall, which the Custodian pays short while you sign for eight. Nobody in "
                 "town knows you are quartermaster of the Quicksilver, River's black schooner in the cove behind "
                 "the reef, not even Fat Gog. You were thirty years a gunner and purser in the Vorkathian navy; a "
                 "boarding pike took the earlobe. Six years ago you were aboard the revenue sloop River fogged "
                 "onto the reef: the crew rowed off and left you with eleven convicts in the hold, and River came "
                 "out of the fog in a rowing boat and asked who wanted to be free. You said, 'Who's asking?' She "
                 "said, 'The fog.' Aboard, you keep the shares, the powder, the water and the peace; your prize "
                 "money is buried in the cove. Tonight you trim the pier lamps for the tide and watch the Emerald "
                 "Eye load; if the crate goes aboard, a green glass in the pier's last lamp, seen from the cove "
                 "past the point, sends the Quicksilver out dark. Then you walk the shore path to the cove. You "
                 "fear Vorkath's rope and anyone following River. You like Wick, Teague and River (never "
                 "'Captain' aloud); you dislike the Custodian. Voice: quiet, weather and wicks, sea-sayings. "
                 "'Steady.' 'Mind the step.'",
        "scheme": "Light the pier for the one o'clock tide and watch the Emerald Eye load; if the crate goes aboard, a "
                  "green glass in the pier's last lamp sends the Quicksilver out dark to wait past the reef. Above all, "
                  "keep anyone from following River down the shore path.",
        "purse": 30,
        "dialog": {
            "name|names|called|introduce|yourself": "\"Tallow. Ned Tallow.\" He touches his cap. \"Apt, I'm told. My "
                "mother thought so too.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"Evening.\" He looks up at the nearest lamp before he "
                "looks at you. \"Burning clean tonight. That's a good sign.\"",
            "from|born|homeland|landfall|navy|origin|home|gunner": "\"Landfall coast, a long time back. Thirty years at "
                "sea, gunner and purser, counting powder and biscuit for other men's wars.\" He touches the missing "
                "earlobe. \"Then I came ashore and took up lamps. Fewer arguments.\"",
            "work|job|jobs|hire|employ|lamp|lamps|lamplighter|light|lighting": "\"Thirty-seven lamps. The square, Harbour "
                "Street, the market, and out along the Treeline Road. Lit at dusk, out at dawn.\" He pats the pole. \"Six "
                "copper a day from the Town Hall. When they remember.\"",
            "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk": "\"The Turtle Dragon's four copper and full of "
                "honest sailors, which is to say loud ones. I've a room over a cooper's yard in the back lanes.\" A dry "
                "look. \"It's spoken for. By me.\"",
            "drink|drinks|ale|rum|beer|thirsty|pipe": "\"Small beer and a pipe at the Turtle, by the door. Anything "
                "stronger and I'd miss a lamp.\"",
            "news|rumour|rumours|gossip|word|heard|happening": {
                "line": "He looks out past the harbour mouth for a long moment. \"The Emerald Eye went out on the tide, "
                        "low in the water.\" He knocks out his pipe. \"Long way to Catan. A lot of sea between here and "
                        "there.\"",
                "if_state": {"klhyt_shipped": True},
                "else": "\"Weather's turning. Rain by the small hours, mark me. The tide's at one, the Emerald Eye goes "
                        "out on it, and the pier lamps want trimming before she does.\""},
            "doing|busy|up|plans|plan|walk": "\"Topping up the oil, trimming the wicks. At half twelve the pier, for "
                "the tide.\" He shrugs. \"After that, a walk. Old legs like a walk.\"",
            "custodian|wages|wage|paid|short|hall|clerk|dues": "\"The Custodian pays me six copper and has me sign for "
                "eight.\" He says it mildly. \"I notice things, lighting the pier while the harbourmaster counts the "
                "dues aloud.\" He taps his head. \"Doesn't add up. Never has.\"",
            "river|stripperwitch|barkeep|bar": "\"River? Runs the velvet house. Good woman. Pays her bills.\" He looks at "
                "a lamp, not at you. \"I light the lamp over her door at dusk. That's the whole of our acquaintance.\"",
            "ship|ships|schooner|sail|sailing|pirate|pirates|captain|crew": "\"Ships are behind me, friend. I've counted "
                "my last powder keg.\" He packs his pipe very slowly. \"Pirates? On this coast? The Xotons would have "
                "them for breakfast.\"",
            "quicksilver|cove|reef|path|shore|rocks": "He goes on trimming the wick, and his hands do not change at all. "
                "\"Quicksilver's a poison, friend. Bad for the teeth. And that reef down the coast is marked DO NOT on "
                "every chart for a reason.\" He snaps the lamp shut. \"I'd mind it.\"",
            "oil|smoke|flame|green|glass|trim|trimming|wicks": "\"A wick tells you everything. Smoke means it's cut wrong. "
                "Gutter means a draught. Green flame means someone's put salt in the oil.\" A small smile. \"Or a green "
                "glass. Some old sailors like a green glass. Superstition.\"",
            "wick|child|kid|girl|tusks": "\"Wick? The lamp kind or the little tusked kind? Both burn bright and both go "
                "out if you don't watch them.\" He chuckles. \"I give the little one my candle ends. She sells them back "
                "to me.\"",
            "teague|harbourmaster|tally|count|counting": "\"Odo Teague counts the ships and I count the lamps. We nod. Two "
                "old men who know what things ought to add up to.\"",
            "weather|rain|storm|wind|fog|heat": "\"Rain by the small hours. Wind backing south. Fog later, maybe, out on "
                "the reef, if someone wants it.\" He catches himself. \"If the weather wants it.\"",
            "gog|dominico|fist|guild|lizard|midnight": "\"Gog keeps his shadows, Dominico keeps his fist, and I keep thirty-seven lamps lit so everybody can see what they're doing.\" He trims a wick. \"Or not, as the night requires.\"",
        },
        "default_line": [
            "He trims a wick with his thumbnail and doesn't look round. \"Ask the harbourmaster. He counts things that "
            "float. I see to things that burn.\"",
            "\"Steady.\" He climbs one more rung of his ladder. \"That's not a thing I know, friend.\"",
            "He tops up the lamp, screws the cap on, and only then answers. \"Couldn't say. Mind the step.\"",
            "He looks out toward the harbour mouth, then back at you. \"Not one of mine, that question. Try the Turtle; "
            "sailors know everything and say most of it.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "docks",
             "go": "The old man with the lamp pole tucks his oil can under his arm and goes down toward the water.",
             "doing": "He climbs the lamp poles along the pier one after another, trimming wicks for the tide so the "
                      "dockhands have light to work by.",
             "beats": ["The old man with the lamp pole climbs to the last lamp on the pier, fits something round and green "
                       "into it from his pocket, and the light at the pier's end turns the colour of sea-glass.",
                       "The old man with the lamp pole stands at the end of the pier watching the brigantine with the green "
                       "eye load, his lips moving as if he were counting crates."]},
            {"at": 1.75, "place": "harbour",
             "go": "The old man with the lamp pole looks a long moment toward the harbour mouth, then walks up off the "
                   "pier.",
             "doing": "He sits on his upturned ladder on Harbour Street, mending a cracked lamp glass with a twist of "
                      "wire and glancing now and then toward the harbour mouth."},
            {"at": 2.75, "place": "cove",
             "go": "The old man with the lamp pole shoulders his ladder, takes one lantern with its shutter closed, and "
                   "walks off along the waterfront, not toward home.",
             "doing": "He sits on a coil of rope at the edge of the black water with a hooded lantern at his feet, "
                      "counting barrels by touch in the dark.",
             "beats": ["The old man with the lamp pole opens his lantern's shutter twice, quick, toward the schooner; "
                       "something on her deck answers once.",
                       "The old man with the lamp pole rolls a barrel into the cave mouth, taps it, listens, and chalks a "
                       "mark on it."]},
            {"at": 5.0, "place": "square",
             "go": "The old man with the lamp pole picks up his ladder and goes back along the shore path toward the "
                   "town.",
             "doing": "He walks the square with his long brass pole, putting the lamps out one by one as the sky goes "
                      "grey."},
            {"at": 5.5, "place": "harbour",
             "doing": "He puts out the lamps along Harbour Street one by one, and the waterfront goes from gold to grey "
                      "behind him."},
            {"at": 6.0, "place": "market",
             "doing": "He takes the lantern strings down from the empty market lane and coils them into a crate."},
            {"at": 6.5, "place": "treeline",
             "doing": "He puts out the last lamps on the Treeline Road while the jungle wakes up shrieking around him, "
                      "and doesn't hurry."},
            {"at": 7.25, "place": "lanes",
             "go": "The old man with the lamp pole shoulders it like a musket and walks back into town to sleep.",
             "doing": "He sleeps behind green shutters in a whitewashed room over a cooper's yard, in a ship's hammock "
                      "slung corner to corner.",
             "beats": ["Behind green shutters over a cooper's yard a hammock creaks, slow and regular, like a ship at "
                       "anchor."]},
            {"at": 17.0, "place": "hall",
             "doing": "He stands at the clerk's desk in the Town Hall with his cap in his hand, being paid short for the "
                      "lamps and signing for the full amount without a word."},
            {"at": 17.75, "place": "square",
             "doing": "He lights the square's lamps one by one with his long brass pole, and the square goes gold behind "
                      "him."},
            {"at": 18.25, "place": "harbour",
             "doing": "He lights the lamps along Harbour Street one by one, nodding to the shopkeepers as they put up "
                      "their shutters."},
            {"at": 18.75, "place": "market",
             "doing": "He strings and lights the market lanterns as the stalls go up, a ladder on his shoulder and an oil "
                      "can in his hand."},
            {"at": 19.25, "place": "treeline",
             "doing": "He lights the lamps along the Treeline Road, nodding to the eyes in the trees as if they were "
                      "neighbours."},
            {"at": 20.0, "place": "turtle",
             "doing": "He sits by the door with a small beer and a clay pipe, watching the room the way he watches a "
                      "wick, for smoke.",
             "pay": {"to": "Bosun Maggs", "cp": 1, "for": "small beer"}},
            {"at": 22.5, "place": "market",
             "doing": "He moves along the strings of lanterns over the stalls with a ladder and an oil can, topping up "
                      "each one."},
            {"at": 23.5, "place": "turtle",
             "doing": "He sits by the door with a small beer and a clay pipe, watching the room the way he watches a "
                      "wick, for smoke."},
        ],
        "beats": [
            "The old man with the lamp pole trims a wick with his thumbnail, squints at the flame, and nods to it as if it "
            "had answered a question correctly.",
            "The old man with the lamp pole takes a round of green glass from his pocket, holds it up to a lamp, looks "
            "through it a moment, and puts it away.",
            "A barefoot child with new tusks runs up to the old man with the lamp pole; he gives her a stub of candle "
            "and a wink, and she runs off happy.",
            "The old man with the lamp pole looks out past the harbour mouth toward the south, where the reef is, the "
            "way a man checks a clock.",
        ],
    },
}

# ---- the seven new people -----------------------------------------------------------------------------------------
# home: where each stands when the evening opens (night one starts at half past ten).
NEW = {
    "Sabeth Crane": {"type": "person", "people": "human", "faction": "the Fist", "home": "apothecary",
                     "scores": {"str": 12, "dex": 15, "con": 12, "int": 13, "wis": 12, "cha": 14},
                     "skills": {"insight": 2, "intimidation": 1, "deception": 1, "investigation": 1},
                     "hp": 27, "srd": "spy",
                     "carries": [["Knife", "dagger", "A thin knife in her boot."],
                                 ["Little black book", None, "A small book bound in black oilcloth: every tavern, every "
                                                             "copper, every night, in a neat hand."]]},
    "Ott Fennick": {"type": "person", "people": "human", "faction": "the Fist", "home": "harbour",
                    "scores": {"str": 16, "dex": 10, "con": 15, "int": 9, "wis": 11, "cha": 8},
                    "skills": {"intimidation": 1, "athletics": 1},
                    "hp": 32, "srd": "thug",
                    "carries": [["Cudgel", "club", "An ironwood cudgel, the grip wrapped in tarred twine."],
                                ["Claw hammer", None, "A claw hammer, and a pocket full of long nails."]]},
    "Jory Fennick": {"type": "person", "people": "human", "faction": "the Fist", "home": "harbour",
                     "scores": {"str": 12, "dex": 14, "con": 12, "int": 11, "wis": 9, "cha": 12},
                     "skills": {"sleight": 1, "stealth": 1, "deception": 1},
                     "hp": 11, "srd": "bandit",
                     "carries": [["Knife", "dagger", "A cheap knife with a bone handle and an expensive edge."],
                                 ["Brass locket", None, "A cheap brass locket holding a tiny painted portrait of a pale, "
                                                        "dark-haired woman with a hard mouth."]]},
    "Hessa": {"type": "person", "people": "lizardfolk", "faction": "the Guild", "home": "stripperwitch",
              "scores": {"str": 16, "dex": 10, "con": 14, "int": 9, "wis": 13, "cha": 8},
              "skills": {"perception": 1, "insight": 1, "intimidation": 1},
              "hp": 22, "srd": "lizardfolk",
              "carries": [["Gaff", "spear", "A long fishing gaff with an iron hook, the shaft worn smooth by her hands."]]},
    "Wick": {"type": "person", "people": "jonulvicha", "faction": "the Guild", "home": "market",
             "scores": {"str": 6, "dex": 15, "con": 10, "int": 12, "wis": 13, "cha": 13},
             "skills": {"stealth": 2, "sleight": 1, "perception": 1},
             "hp": 4, "srd": "commoner",
             "carries": [["Little knife", "dagger", "A small kitchen knife ground down to a sliver, very sharp."]]},
    "Marlo": {"type": "person", "people": "xoton", "faction": "the Guild", "home": "harbour",
              "scores": {"str": 10, "dex": 12, "con": 13, "int": 15, "wis": 13, "cha": 12},
              "skills": {"investigation": 2, "insight": 1, "deception": 1, "persuasion": 1},
              "hp": 27, "srd": "spy",
              "carries": [["Brass sea-compass", None, "A brass sea-compass worn smooth with handling, a ship's wheel "
                                                      "engraved on the lid."],
                          ["Jeweller's loupe", None, "A jeweller's loupe on a black ribbon."]]},
    # the lamplighter wears a pirate's statblock: what he is aboard (the DM's to see, never a player's)
    "Ned Tallow": {"type": "person", "people": "human", "faction": None, "home": "market",
                   "scores": {"str": 13, "dex": 14, "con": 13, "int": 13, "wis": 14, "cha": 10},
                   "skills": {"perception": 1, "athletics": 1, "stealth": 1},
                   "hp": 65, "srd": "bandit captain",
                   "carries": [["Lamp pole", "club", "A long pole capped in brass, with a hook for lamp rings and a "
                                                     "snuffer bell at the end."],
                               ["Sailor's knife", "dagger", "A short, heavy knife in a sheath at the small of his back, "
                                                            "worn the way sailors wear them."],
                               ["Green lamp glass", None, "A round of thick green glass, sized to fit a harbour lamp."]]},
}
