# Klhyts Refuge, cast file H: the shops of Chandlers' Row (owner, 2026-11-23: "Adventurer stuffs, food, weapons,
# armour ... create new shop owners for our new shops. Make sure a rapier is for sale", and "Key NPCs need power and
# agency"). Chandlers' Row runs between Harbour Street and the Night Market; the build adds its three places
# (chandlery, anvil, coral) and what each keeper sells. Canon names no shops in the Refuge, so all of this is a host
# default. Three new people (NEW): Hob Merrow of Merrow's Chandlery (kit and travel food), Tamsin Vey of the Crooked
# Anvil (blades, and the rapier), Zuri Coralhand of Coral and Chain (armour). Each lives over the shop and keeps to
# it all day: open dusk to dawn like the rest of the Refuge, working in the cool, sleeping through the heat, never out
# of the door. The prices in their lines are the build's (copper: 100 to the gold piece, 10 to the silver).
# Their lines read the news in stages, newest first: the verdict, the magistrate's Arm once they land, the sail, Klhyt,
# the night; and the decree by its Arm. Plain data and one small helper: CAST, and NEW for the three.
#
# invented: host: Chandlers' Row and its three keepers; the shops open dusk to dawn and the keepers sleep through the heat inside them
# invented: host: the Fist takes no coin off the Row, it takes goods, and Sabeth Crane writes them down as "the Row's peace, paid in kind"
# invented: Hob Merrow: born Hobart Merrow in a Fronterian mountain town; nine years sutler to the Seventh of the Hourglass, the Inquisition's border foot in the passes
# invented: Hob Merrow: the paymaster kept the regiment's pay chest in his wagon (the only lock that worked); the night the Seventh turned back a column of elven families on a pass, he drove down the far side with it; four hundred gold in the Throne's silver
# invented: Hob Merrow: thirty years on the Row; the pay chest is the iron-bound box he sits on behind the counter, the hourglass sanded off its lid; a dozen hourglass-stamped coins in a tobacco tin in his apron
# invented: Hob Merrow: buys whatever adventurers bring back at a third of its worth in coin or half in credit; pays Wick three coppers at dusk for the day's news; pays the Fist's peace in rope and lamp oil
# invented: Hob Merrow: four nights ago sold Ott Fennick a brace and bit and a pound of long nails on the Fist's account; reads Voss's square-cut food as a Landfall officers' mess habit; reads each Arm's sign when the magistrate lands
# invented: Tamsin Vey: made a smith at the Keep of Sheath (canon: an elven stronghold Saven Dais' forces burned); the Keep's tester before its smith; walked out of the fire with her master's hammer; twenty years in the Refuge
# invented: Tamsin Vey: the anvil fell off a lighter onto the pier and bent its horn, and rings like the Keep's bell; Captain Aelith's blade is her master's work
# invented: Tamsin Vey: arms elves going south on the Moonmoth at her back door for nothing (a living silverleaf shown); a child's knife put by for Miravel; will not sell to anyone wearing the octogram
# invented: Tamsin Vey: Dominico's sword-cane, two years ago, eighty gold agreed by handshake, never paid; silver folded into its steel
# invented: Zuri Coralhand: born an Ironwake on the Crows Nest, Amara Ironwake's cousin; Coralhand a craft-name of the coral-wrights; set ashore by House Ironwake ten years ago; learned chain and scale from a Jonulvicha armourer on the Catan quays
# invented: Zuri Coralhand: made Kwasi Foamtooth's coral tooth (unpaid); thirty black jerkins for the Fist a year ago at four gold apiece, a hundred and twenty gold unpaid; sells the Fist nothing until it is paid
# invented: Zuri Coralhand: the breastplate on her stand was made to Lieutenant Voss's measure (ordered through Constable Rosa Quint) and refused him at the fitting; her will says the sea, and Amara has sworn to it


def _stages(*steps, otherwise):
    """A line that moves with the news: (if_state, line) pairs, newest first, then what is said before any of it."""
    out = otherwise
    for cond, line in reversed(steps):
        out = {"if_state": dict(cond), "line": line, "else": out}
    return out


REMOVED = {"verdict": "removed"}
UPHELD = {"verdict": "upheld"}
LANDED = {"magistrate_landed": True}
SIGHTED = {"magistrate_sighted": True}
HOME = {"klhyt_home": True}
DEAD = {"klhyt_dead": True}
SHIPPED = {"klhyt_shipped": True}
HIT = {"guild_hit": True}


def _arm(a):
    return {"magistrate_arm": a}


def _decree(a):
    return {"decree": a}


# the words every keeper hears for news, rooms, drink, the day and work (each keeper's own table adds the rest)
NEWS = "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word"
ROOM = "room|rooms|bed|beds|sleep|lodging|lodgings|inn|stay|bunk"
DRINK = "drink|drinks|ale|rum|beer|wine|mead|tavern|taverns|pub|thirsty"
DOING = "doing|busy|plans|plan|open|opening|hours|close|closing|shut"
WORK = "work|job|jobs|help|errand|errands|task|tasks|hire|mission|favour|favor|reward|earn|pay|paid"
HELLO = "hello|hi|hey|evening|ahoy|greetings|howdy|morning|afternoon|welcome"
KLHYT = "klhyt|mayor|founder|castaway|missing"
MAGISTRATE = "magistrate|magistrates|judge|justice|hearing|court|trial|verdict|guards|landed|sail"
DECREE = "decree|decrees|proclamation|proclamations|edict|edicts|census|levy|licence|license|licences"


_HOB_GOG = ("\"Fat Gog buys his rope here and pays on the day, which is more than the law does. River behind his bar "
            "buys lamp oil by the barrel and never haggles.\" He nods toward the market end of the Row. \"His little "
            "runner sells me the town for three coppers a night and sells him the same. I want her to. Let the big man "
            "know the old chandler's a friend.\"")
_ZURI_GOG = ("\"Fat Gog buys the Lizardfolk a round at the Turtle when they're served last.\" She nods slowly. \"A "
               "Xoton notices who gets served last. He's all right. Dominico's lot squaring up to his house in my leather "
               "is not.\"")


CAST = {

    # ---- Hob Merrow, Merrow's Chandlery ---------------------------------------------------------------------------
    "Hob Merrow": {
        "look": "A stooped, wiry man of about sixty with a grey queue tied in tarred twine, wire spectacles pushed up on "
                "a bald crown, and forearms still roped with old muscle. He sits on an iron-bound chest behind a counter "
                "of scarred teak, under hanging coils of rope and lanterns, and counts everything twice with his lips "
                "moving. When boots go by outside, his heels come together.",
        "seen_as": "the stooped old chandler in wire spectacles",
        "brief": "You are Hob Merrow, the chandler of Chandlers' Row, the street that runs from Harbour Street up to the "
                 "Night Market in Klhyts Refuge. Merrow's Chandlery sells everything a body needs on the road or the sea "
                 "but the road itself, and you know every price by heart: pack 2 gp, bedroll 1 gp, a day's rations "
                 "(hardtack, salt fish, dried mango) 5 sp, waterskin 2 sp, fifty feet of hemp rope 1 gp, torch 1 cp, "
                 "tinderbox 5 sp, hooded lantern 5 gp, flask of oil 1 sp, healer's kit 5 gp, potion of healing 50 gp, "
                 "crowbar 2 gp, grappling hook 2 gp (forged next door), thieves' tools 25 gp (you never ask who for), "
                 "caltrops 1 gp, chalk 1 cp, paper 2 sp the sheet, parchment 1 sp, a blank book bound in sharkskin 25 gp (a "
                 "pen and a dip of ink come with any of them), and your own map of the Refuge and its coast 5 sp. You "
                 "also buy whatever "
                 "adventurers bring back, no questions: a third of its worth in coin, or half in credit on your slate. "
                 "You are about sixty, a Landfall man, and the Row was mud when you came thirty years ago. Your secret, "
                 "which would hang you: you were born Hobart Merrow in a mountain town in Fronteria, and for nine years "
                 "you were sutler to the Seventh of the Hourglass, the Inquisition's border foot that kept the passes "
                 "against people fleeing. You sold them bread, boots, tobacco and rope from a wagon, and the paymaster "
                 "kept the regiment's pay chest in your wagon because yours was the only lock in the regiment that "
                 "worked. The night the Seventh turned back a column of elven families on a pass, and you saw what "
                 "turning back meant, you drove down the far side of the mountain with the chest still in the wagon. "
                 "Four hundred gold in the Throne's silver bought a passage west, this shop, and thirty years of nobody "
                 "asking. The chest is the iron-bound box you sit on behind the counter, the hourglass sanded off its "
                 "lid. A dozen of its coins, still stamped with the hourglass, lie in a tobacco tin in your apron, "
                 "because you could never quite spend the last of them. Under the Throne's articles a sutler is a "
                 "soldier where theft is concerned, and the Seventh's rolls still carry your name against a pay chest. "
                 "Klhyt's Charter, Article One (nobody here shall be asked where they came from), is the only law you "
                 "love. Money: a fair trade; credit for people you like; three coppers to Wick at dusk for the day's "
                 "news, knowing she sells the same to Fat Gog, which you want; the Fist's peace paid in kind, rope and "
                 "lamp oil, which you count cheap. Four nights ago the big sandy Fennick with the crooked nose bought a "
                 "brace and bit and a pound of long nails on the Fist's account, and you have wondered every night since "
                 "who bores air holes in a crate of personal effects; you said nothing, and you are ashamed of it. "
                 "Lieutenant Voss frightens you more than anyone alive: he cuts his food in squares the way the Landfall "
                 "officers' messes teach it, he serves the Arm of Pain, and one good look at the chest or the tin and he "
                 "will know you. Any magistrate frightens you; one with a book of names (Peace), a census (Destiny) or "
                 "the hourglass (Pain) would finish you. What you want now: Voss gone from the Refuge before he looks at "
                 "you twice, the Custodian out of the Town Hall, and the magistrate's ship gone again on the next tide. "
                 "What you do about it, quietly and never in the open: stake anyone working against the Custodian or "
                 "the officer, with credit, kit, and the Throne's ways, which you know from the inside. A magistrate "
                 "reads papers before people, so bring them papers: the dues tally, Klhyt's letter, the passage page. "
                 "A Throne warrant goes up on the square at two in the morning, and its men strike on sight but do not "
                 "chase. The officer calls on witnesses in the small hours with the constable who leans on things. The "
                 "Fist hunts in twos, shows itself before it strikes, takes five gold to forget a name, and will not "
                 "cross Fat Gog's threshold or the elves' gangplank. You would give a great deal to see Ithriel's "
                 "household aboard the Moonmoth, because with the elves gone south the officer has nothing to stay for. "
                 "What you offer players: kit at fair prices, credit if they are against the Custodian, a buyer for "
                 "loot, the Throne's habits, the Fennick's brace and bit, and where to go for what: blades at the "
                 "Crooked Anvil next door (Tamsin Vey's), armour across the Row at Coral and Chain (Zuri Coralhand's). "
                 "How you push back: asked about your past, you quote Article One and go cold; pressed, you change the "
                 "subject to prices; called Hobart, you go white and bargain, in the shop and never in the street; "
                 "threatened with exposure, you offer money first, and if that fails you remember you have nothing to "
                 "lose and a hatchet under the counter. You never say the word deserter. If the officer comes in, you "
                 "sell to him politely at full price and stand with your heels together the whole time. You like Tamsin "
                 "(she arms the people the Seventh used to turn back), Zuri (pays on the day), Gog (an honest crook), "
                 "Wick and Klhyt; Marlo is a necessary evil and Khamisi a thief of rope. Voice: a sutler's patter gone "
                 "soft at the edges; kit, ration, slate, the long road; old march-words he does not notice using. "
                 "'Kit's kit. A man who skimps on rope hangs by it.' 'Nobody here asks where you came from. I'd take it "
                 "kindly if you didn't start.'",
        "scheme": "He stakes anyone working against the Custodian or the officer in blue with credit, kit and the "
                  "Throne's ways, buys whatever they bring back with no questions, and hopes to see Lieutenant Voss and "
                  "the magistrate's ship gone before either looks twice at an old chandler who sits on a pay chest.",
        "purse": 1500,
        "dialog": {
            "name|names|called|introduce|yourself|hob|merrow":
                "He taps the painted board over the door with his pencil. \"Hob Merrow. Merrow's Chandlery, painted "
                "fresh every spring. Hob to customers. Merrow to people I owe, and there aren't many.\"",
            "hobart":
                "The pencil stops. For a long moment he looks at you over the spectacles, and his hand drifts toward the "
                "shelf under the counter and comes back empty. \"Nobody's called me that in thirty years.\" Very quietly: "
                "\"Whatever you want for it, ask me in here, not in the street. And never near anyone in blue.\"",
            HELLO: _stages(
                (REMOVED, "\"Evening, evening.\" He looks ten years lighter. \"Grey coat in irons, and the Throne's ship "
                          "sails home soon, with luck. Kit for the road? It's a good week for roads.\""),
                (UPHELD, "He nods without smiling. \"Evening. Shut the door behind you, would you. Keeps the street "
                         "out.\" He doesn't look toward the square. \"What can I do for you?\""),
                (LANDED, "He greets you from behind the counter and does not come round it. \"Evening. There's a Throne "
                         "ship at the pier, so I stay behind my counter. What do you need?\""),
                (DEAD, "He takes his spectacles off. \"Evening. Bad one. Come in out of the street.\""),
                (HOME, "\"Evening!\" He comes round the counter to shake your hand. \"Mayor's home, Article One stands, "
                       "and rope's a gold the fifty foot. What can I do you for?\""),
                (HIT, "\"Evening. You'll have heard the glass go at Gog's house, at the bell.\" He shakes his head. "
                      "\"Somebody'll want lamp oil and rope to put it right. What's yours?\""),
                otherwise="He looks up over his wire spectacles and puts his pencil down. \"Evening. Merrow's Chandlery: "
                          "anything for the road but the road itself. What'll it be?\""),
            "paper|parchment|ink|pen|quill|notebook|journal|diary|write|writing|stationery":
                "He lays a clean sheet on the counter and squares it with one finger. \"Rag paper, two silver the sheet. "
                "Parchment, one, if you don't mind goat. A blank book bound in sharkskin, twenty-five gold, and it'll "
                "outlive you.\" He sets a pen and a pot of ink beside it. \"Pen and a dip of ink come with it. A man "
                "should be able to write his own name, whatever it is.\"",
            "loot|looted|salvage|salvaged|swag|plunder|spoils|treasure|found|unload|pawn|valuables|jewels|gems|"
            "trinkets":
                "He sets a little brass scale on the counter between you. \"Whatever you bring back from wherever you've "
                "been, I buy. A third of its worth in coin, or half in credit on my slate. No questions.\" He settles "
                "his spectacles. \"I've no use for answers, friend. Answers get people hanged.\"",
            "price|prices|cost|costs|wares|goods|stock|sell|selling|sells|buy|buying|shop|list|kit|gear|"
            "equipment|supplies|browse":
                "He taps the slate at his elbow and reads it off without looking. \"Pack two gold, bedroll one. A day's "
                "rations five silver: hardtack, salt fish, dried mango. Waterskin two silver. Fifty foot of hemp, a gold. "
                "Torch a copper, tinderbox five silver, hooded lantern five gold, oil a silver the flask. Healer's kit "
                "five gold. Potion of healing, fifty, and worth it the once you need it. Crowbar two, grappling hook two, "
                "caltrops one, chalk a copper. Paper two silver the sheet, parchment one, a blank book twenty-five gold. "
                "Thieves' tools twenty-five, and I never ask who for. My map of the Refuge "
                "and its coast, five silver.\" He sets the pencil down. \"And I buy. Whatever you bring back, no "
                "questions.\"",
            "pack|packs|backpack|backpacks|rucksack|bag|bags|bedroll|bedrolls|blanket|blankets|camp|camping":
                "He lifts a canvas pack off a hook and thumps it on the counter. \"Pack, two gold. Waxed canvas, double "
                "stitched, and the straps won't cut you after a day.\" A rolled blanket lands beside it. \"Bedroll, a "
                "gold, and you'll want one. The jungle floor moves at night.\"",
            "rations|ration|hardtack|biscuit|provisions|salt|fish|dried|mango|mangoes|food|hungry|eat|meal|meals":
                "He lifts the lid of a crock and the smell of salt fish comes up. \"A day's rations, five silver: "
                "hardtack, salt fish, dried mango, in oilcloth. Keeps a month, and tastes like it's kept a month.\" He "
                "puts the lid back. \"Hot food tonight, try the market: the Jonulvicha cook's goat, two copper. Mind her "
                "pepper sauce.\"",
            "water|waterskin|waterskins|canteen|thirst|pump":
                "\"Waterskin, two silver. Goat, tarred inside, a day's water if you're careful.\" He hangs it back on its "
                "hook. \"Fill it at the pump in the square. Not the harbour. Never the harbour.\"",
            "rope|ropes|hemp|line|fifty|feet|foot|grapple|grappling|hook|hooks|climb|climbing|wall|walls":
                "He pats a coil as thick as his thigh. \"Fifty foot of hemp, a gold. Grappling hook, two gold, four "
                "tines, forged next door by the elf, so it'll hold.\" He leans in. \"The Xoton on the tarpaulin in the "
                "market sells rope cheaper. Ask the Xoton bosun with the whistle whose rope it was first.\"",
            "torch|torches|light|lights|lantern|lanterns|lamp|lamps|oil|flask|tinderbox|tinder|flint|dark|darkness":
                "He takes down a lantern with a sliding shutter. \"Hooded lantern, five gold: shutter it and you're a "
                "shadow, open it and you're a lighthouse. Oil a silver the flask, six hours to a flask. Torch, a copper, "
                "an hour of light and a lot of smoke. Tinderbox five silver, and it'll strike in the rain.\"",
            "healer|healers|healing|heal|bandage|bandages|potion|potions|medicine|wound|wounds|wounded|hurt|dying|"
            "bleeding|salve":
                "He unlocks a drawer and sets a small glass vial sealed with red wax on the counter; the red inside "
                "glimmers when he tilts it. \"Potion of healing. Fifty gold, and dear at that. Worth every copper the "
                "once you need it.\" A roll of "
                "canvas goes down beside it. \"Healer's kit, five gold: bandage, splint and salve for ten bad nights. "
                "Cheaper than the potion. Slower, too.\"",
            "crowbar|crowbars|pry|prise|prybar|lever|break|thieves|tools|lockpick|lockpicks|picks|lock|locks|padlock":
                "He brings a crowbar up from under the counter and lays it down like a sword. \"Crowbar, two gold. Opens "
                "crates, shutters and arguments.\" Beside it, without comment, a little roll of oiled leather. \"Thieves' "
                "tools, twenty-five gold. Picks, a tension wrench, a mirror on a stick. I never ask who for. Nobody here "
                "asks anything.\"",
            "caltrops|caltrop|chalk|mark|marks|marking|trap|traps|spikes":
                "He shakes a little bag and it clinks. \"Caltrops, a gold the bag. Scatter them behind you and whoever's "
                "following learns to dance.\" He snaps a stick of chalk to show it's dry. \"Chalk, a copper. Mark your "
                "way in and you'll find your way out.\"",
            "map|maps|chart|charts|street|streets|town|coast|directions|lost|way|route|road|roads":
                "He unrolls a sheet on the counter and pins it with two lanterns. \"My map of the Refuge and its coast, "
                "five silver, every street and a day's walk each way.\" His pencil moves: \"Docks at the bottom of "
                "Harbour Street, Market Square up the hill, the Night Market at this end of the Row, the gate and the "
                "Treeline Road out past the square. The elf with the tea in the market draws a better chart of the "
                "south, and cheaper. I draw better streets.\"",
            "credit|slate|tab|owe|loan|lend|account|afford|broke|poor|cheap|cheaper|discount|haggle|bargain":
                "He looks you over the top of his spectacles, the way he looks at rope. \"I give credit to people I like. "
                "I like people who make the Custodian's week worse.\" He opens a fat ledger. \"Prices don't move. Payment "
                "can wait. Don't make me come and find you. I'm old and I walk slowly, and I remember everything.\"",
            "chandler|chandlery|chandlers|business|trade|living|years":
                "He looks round the shop as if counting it, which he probably is. \"Thirty years on the Row. Rope to "
                "sailors, lanterns to fishermen, crowbars to people with honest faces. Sells, buys, mends, gives "
                "credit.\" He sniffs. \"The Row was mud when I came. Now it's mud with three shops on it.\"",
            "from|born|birth|homeland|origin|landfall|past|before|came|arrived|young|history":
                "He smiles, and it doesn't reach the spectacles. \"Landfall, like half the Refuge. Came on a boat, like "
                "all of it.\" He taps the slate. \"Article One of the mayor's Charter: nobody here shall be asked where "
                "they came from. It's painted on the Town Hall porch. I'd take it kindly if you didn't start.\"",
            "sutler|sutlers|deserter|deserters|deserted|desert|desertion|regiment|regiments|army|soldier|soldiers|"
            "seventh|hourglass|chest|paychest|tin|wagon|military":
                "His hands go still on the counter. \"Never a soldier. I sold boots to soldiers once, a long way from "
                "here. A lot of men did.\" Without seeming to notice, he brings his heels together; then, noticing, he "
                "moves them apart. \"Rope's a gold the fifty foot. That's all the history this shop keeps.\"",
            "charter|article|articles|refuge|runaways|asked|freedom|questions|law|laws": _stages(
                (UPHELD, "\"The magistrate says the Charter was never the Throne's.\" He looks at the painted board over "
                         "his door. \"Paint's cheap. I'll paint Article One over my counter, then, where it's mine.\""),
                otherwise="\"Klhyt's Charter. Article One: nobody here shall be asked where they came from.\" He says it "
                          "like a man saying grace. \"Half this town would be in irons on Landfall, and the other half "
                          "in the mines. Here we sell each other rope. Best law ever written, and the shortest.\""),
            KLHYT: _stages(
                (DEAD, "He takes his spectacles off and does not put them back on. \"I came here because of him. Nobody "
                       "asked me anything, because he'd said they mustn't.\" He looks at the door. \"Who says so now?\""),
                (HOME, "\"Home!\" He slaps the counter, and a lantern swings. \"Thirty years he's kept Article One for me "
                       "without knowing it. Now somebody keeps him. The grey coat hasn't finished, and neither has the "
                       "officer in blue.\""),
                (SHIPPED, "\"Gone out on the tide in a box, they're saying.\" He grips the edge of the counter. \"Thirty "
                          "years he kept the Charter. The Throne's coast has him now.\""),
                otherwise="\"Four nights gone, and the grey coat says upriver.\" He sniffs. \"Klhyt has no business "
                          "upriver. And four nights ago the big sandy one from the Fist bought a brace and bit and a "
                          "pound of long nails off me. Who bores air holes in a crate?\" He looks at you. \"I've said "
                          "nothing to anyone. I'm saying it to you.\""),
            "emerald|eye|devito|brigantine|crate|crates|nails|nail|brace|auger|holes|catan|fennick|ott": _stages(
                (HOME, "\"The crate on the tide had a mayor in it, and I sold them the brace and bit that bored his air "
                       "holes.\" He looks sick. \"Not so much as a nail to the Fist again. Not on account, not for coin.\""),
                (SHIPPED, "\"She sailed at one with the crate aboard, and I sold them the brace and bit that bored "
                          "its air holes.\" He takes his spectacles off. \"I said nothing. I'll carry that a while.\""),
                otherwise="\"Four nights ago the big sandy one with the crooked nose, black band on his arm, bought a "
                          "brace and a half-inch bit and a pound of long nails. On the Fist's account.\" He chalks a "
                          "line through nothing. \"The green-eyed brigantine sails at one with a crate for Catan, under "
                          "the Custodian's seal. Who bores air holes in personal effects? Go and look at the pier's end. "
                          "Don't say who sent you.\""),
            "gog|fat|guild|stripperwitch|river|lizardman|shadows": _stages(
                (SIGHTED, _HOB_GOG),
                (HIT, "\"They broke Gog's house at the bell.\" He is already pulling down lamp-oil and a coil of rope. "
                      "\"He'll want glass and oil and line, and he'll have them at cost. Tell him the old chandler said "
                      "so.\""),
                otherwise=_HOB_GOG),
            "wick|runner|girl|urchin|child|tusks":
                "He takes three coppers from the till and stacks them on the corner of the counter. \"Wick. Small, "
                "Jonulvicha, new tusks, sharp as my hatchet. Three coppers at dusk for whatever she's seen. Best news in "
                "the Refuge, and the cheapest.\"",
            "dominico|fist|enforcer|cane|ring|black|coat|band|bands|peace|protection|sabeth":
                "He shrugs. \"The Fist doesn't take coin off the Row. It takes kind. Rope and lamp oil from me, which I "
                "count cheap.\" He lowers his voice. \"Next door the elf made him that sword-cane, and across the way the "
                "Xoton made his lads thirty jerkins, and neither has seen a copper. The woman with the little book writes "
                "it down as the Row's peace.\"",
            "custodian|grey|gray|dues|tithe|skim|skimming|hall|clerk|tally": _stages(
                (REMOVED, "\"Irons, and down to the ship.\" He polishes his spectacles very thoroughly. \"I'll sleep "
                          "tonight. First time in a week.\""),
                (UPHELD, "\"Upheld, with the Throne's seal round his neck.\" He looks down at the iron-bound chest he sits "
                         "on. \"Then I keep my head down and my counter between me and the street. You'd do well to "
                         "keep yours down too.\""),
                (LANDED, "\"He met the ship first, bowing, with a packet of his own papers under his arm.\" He snorts. "
                         "\"Then put yours on top of his. The hearing's at ten at the Town Hall: the dues tally, the "
                         "mayor's letter, the passage page. Magistrates read before they listen.\""),
                (HOME, "\"Found out, and doubled down: claims the harbour for the Throne, wears the octogram, bars "
                       "himself in with the strongbox.\" He snorts. \"I know that kind. He's not brave, he's waiting for "
                       "a ship. Hurt him before it comes. Magistrates read before they listen: get the dues tally out "
                       "of the Hall, and the mayor's own letter, into their hands.\""),
                otherwise="\"The grey coat? Signs every tally himself, smiles with half his mouth, and the harbour's never "
                          "been busier while the dues go down.\" He taps his ledger. \"I keep books, friend. His don't "
                          "add.\""),
            "voss|lieutenant|officer|uniform|blue|aurel|squares":
                "\"The officer in blue.\" He lowers his voice, though the shop is empty. \"Eats his eggs in squares. They "
                "teach that in the officers' messes in Landfall: cut it square, eat with one hand, keep the other free.\" "
                "His heels click together, and he looks down at them. \"He serves the Arm of Pain. I want him gone from "
                "this town. Get those hooded elves aboard the pale ship and he's nothing left to stay for, and there's a "
                "lantern on that hook with your name on it.\"",
            "throne|vorkath|vorkathian|vorkathia|empire|emperor|octogram|eight|arms|goddess|faith|church|inquisition|"
            "saint|saints":
                "\"The Throne of Vorkath.\" He says it the way sailors say reef. \"Eight arms and a long reach, and every "
                "hand holds a book with names in it. Half the lanes wear the octogram over their shirts since the officer "
                "came.\" He coils a line that was already coiled. \"I sell them rope. Rope doesn't pray.\"",
            MAGISTRATE: _stages(
                (REMOVED, "\"Removed! Irons, and the Patient Hand to take him home.\" He lets out a breath he seems to "
                          "have held for days. \"And when she sails she takes her guards and her book with her. I'll "
                          "stand on my step and wave.\""),
                (UPHELD, "\"Upheld.\" He takes off his spectacles. \"The Throne's officer keeps the Throne's town. Read "
                         "the decree, friend, and read who it was written for.\""),
                (_arm("war"), "\"A silver ball and chain on the breast: Gideon's, the War Arm.\" He is already counting "
                              "his stock. \"They'll look at this town and see a garrison and a levy. The War Arm hangs "
                              "deserters at crossroads and leaves them for the crows.\" A pause, too long. \"So I've "
                              "heard.\""),
                (_arm("peace"), "\"A little silver spade at the throat. Percival's, the kind ones.\" He doesn't look "
                                "comforted. \"Kind people with a book, friend, and they want every name in it, and where "
                                "it came from. I'd sooner a rope. It's quicker.\""),
                (_arm("pleasure"), "\"Grapes on the cuffs and a cup on a chain. Pil's Loffgren, the Pleasure Arm.\" "
                                   "Something like hope. \"That one can be bought. Coin counts with that Arm, more than "
                                   "papers. If your friends have gold, the hearing is where they spend it.\""),
                (_arm("pain"), "He goes grey. \"An iron hourglass at the throat. Teflon's. The Inquisition.\" He takes a "
                               "tobacco tin out of his apron and puts it back, twice. \"Get the elves out tonight, all of "
                               "them, any way you can. And if you see me packing, friend, you didn't.\""),
                (_arm("chaos"), "\"Lightning in the ear and a dice cup on the belt. Hester-Stanhope's, the gamblers' "
                                "saint.\" He laughs once. \"That Arm throws dice. Could go any way. Bring papers "
                                "anyway: a thumb on the scale still counts when the scale's a dice cup.\""),
                (_arm("destiny"), "\"A sextant and a glass eye. Annabella Rand's, the Destiny Arm.\" He swallows. "
                                  "\"Sages. They count things. They'll want every name and every birthplace, and "
                                  "they read everything twice.\" He looks at his own ledger as if it might talk."),
                (_arm("death"), "\"A child's wooden hand at the throat. Gwendoline's, the Death Arm.\" He makes a small "
                                "sign he seems to have forgotten he knew. \"They care what's done to the living on the "
                                "way to dying. A man crated to die in the dark weighs heavy with them. Say so at the "
                                "hearing.\""),
                (_arm("life"), "\"A silver pouring jug. Vistadine's, the Life Arm. Bathhouses and clean souls.\" He sniffs "
                               "his sleeve. \"They'll wash this town whether it wants washing or not. Better than a "
                               "gallows. Wetter.\""),
                (SIGHTED, "\"A sail at the harbour mouth with an octogram the size of a house.\" His hands are steady; "
                          "his voice isn't. \"When they land, look at what the magistrate wears at the throat, and come "
                          "and tell me. I can tell you what it means. Then I can tell you whether to run.\""),
                (HOME, "\"A magistrate of the Throne is at sea for the colonies, and the grey coat's praying it's soon.\" "
                       "He leans in. \"Magistrates read before they listen. Get them paper: the dues tally from the "
                       "Hall, the mayor's own letter, the passage page. And people who'll stand up. Find the witnesses "
                       "before the officer does.\""),
                otherwise="\"A magistrate?\" He chalks a price and rubs it out. \"The Throne sends one to the colonies now "
                          "and then, to see its law is kept. One's due, the grey coat keeps saying, as if it were good "
                          "news.\" He looks at the door. \"It's never good news.\""),
            DECREE: _stages(
                (_decree("peace"), "\"Every name, and where it came from, in the goddess's book.\" He looks at the "
                                   "painted board over his door, and then down at the iron-bound chest. \"I've written a "
                                   "lot of names in books. Never my own.\" Quietly: \"If anyone asks, I was born on the "
                                   "Row.\""),
                (_decree("destiny"), "\"A census.\" He laughs, and it is not a good laugh. \"Every name, every birthplace, "
                                     "read twice by a man with a glass eye.\" He shuts the ledger. \"Thirty years of "
                                     "Article One, undone in an afternoon. I'll not be counted, friend. Remember I said "
                                     "so.\""),
                (_decree("war"), "\"Twenty for the Throne's crusades, and a garrison quartered here.\" He knows the sound "
                                 "of it. \"Soldiers drilling on the square, buying boots. Somebody in that garrison will "
                                 "have served with somebody who served in the passes. Soldiers talk.\" He stops. \"Forget "
                                 "I said passes.\""),
                (_decree("pain"), "\"Every elf handed over, and no magic but the Throne's.\" He has his coat on, and he "
                                  "doesn't move to leave. \"Go next door and tell the smith. Then go across and tell the "
                                  "Xoton.\" He looks at the chest he sits on. \"Thirty years. You'd think a man would be "
                                  "ready.\""),
                (_decree("pleasure"), "\"Licences on every tavern, and a copper in ten for the Throne's Pleasure "
                                      "Domes.\" He breathes out. \"That's only thieving with a seal on it. I can live with "
                                      "thieving. Half my stock's salvage.\""),
                (_decree("chaos"), "\"The pale ship taken for the Throne's prize, and the octogram on every mast.\" He "
                                   "shakes his head. \"Then where do the elves go? South on foot, I suppose.\" He looks at "
                                   "his maps. \"I've maps. Someone tell the smith next door.\""),
                (_decree("death"), "\"No burials at sea, and no elven rites.\" He thinks of something. \"The Xotons will "
                                   "riot. And the armourer across the Row has made her will to go back to the sea. "
                                   "Somebody ought to tell her before she reads it.\""),
                (_decree("life"), "\"Wash, or lose your stall, your office and your word.\" He sniffs his sleeve. \"I'll "
                                  "wash. A man who's hidden thirty years can stand a bath.\" A thin smile. \"The Fist "
                                  "won't. Imagine.\""),
                (LANDED, "\"There'll be a decree. There always is. The Throne doesn't cross an ocean to say well done.\" "
                         "He runs a thumb down his ledger. \"Whatever it says, it'll be written by people who never "
                         "needed to run.\""),
                otherwise="\"Decrees? The only one in this town is the Charter, painted on the Town Hall porch. Article "
                          "One.\" He smiles. \"Long may it stay the only one.\""),
            "warrant|wanted|hunted|hunt|hunting|marked|ambush|danger|dangerous|safe|safety|hide|hiding|chase|chased":
                "\"Listen, then, because I learned this the hard way.\" He counts on his fingers. \"A Throne warrant "
                "goes up on the square at two in the morning, and its men strike on sight, but they don't chase: get "
                "out of their sight and stay out. The Fist hunts in twos and shows itself before it strikes, so when you "
                "see them, run, don't talk. Five gold in the hand of any of them buys your name back, I hear. And "
                "neither the Fist nor the Throne will cross Fat Gog's threshold, or the pale ship's gangplank.\"",
            "witness|witnesses|teague|harbourmaster|tully|sit|small": _stages(
                (REMOVED, "\"The hearing's done and the grey coat's in irons. Witnesses can sleep at night again.\" "
                          "He looks pleased with himself, and doesn't say why."),
                (UPHELD, "\"The hearing's done.\" He looks at the door. \"Whoever spoke for the mayor had better sleep "
                         "with company for a while yet. The officer remembers names. So does the Throne.\""),
                (HOME, "\"The officer calls on witnesses at two in the morning, with the constable who leans on "
                       "things. The harbourmaster first, then the red-faced lad of the Fist who talks too much.\" He "
                       "pushes a lamp-oil flask across the counter and doesn't charge for it. \"Sit up with one. A witness "
                       "with company remembers everything by morning. Fat Gog pays three silver a night for it.\""),
                otherwise="\"Teague, the harbourmaster? Counts every hull in the harbour twice, like me.\" He nods. \"If "
                          "the dues have gone anywhere, his tally knows where.\""),
            "elf|elves|ithriel|hooded|household|exile|exiles|moonmoth|pale|gangplank|south":
                "\"The hooded scholar at the Unicorn and her four, waiting on the pale ship at the pier's end.\" He looks "
                "at the street door. \"I've seen families like that turned back on a mountain pass. Not here. Walk them "
                "down to the water, past the officer. Fat Gog pays a gold for it, and there's a lantern on my hook for "
                "whoever does.\"",
            "tamsin|vey|anvil|smith|blacksmith|bladesmith|blade|blades|weapon|weapons|sword|swords|rapier|rapiers|"
            "dagger|daggers|axe|bow|bows|crossbow|arrows":
                "\"Next door, the Crooked Anvil: Tamsin Vey, an elf, the best bladesmith on this coast, and she'll tell "
                "you so.\" He grins. \"Rapier's her pride, twenty-five gold. She won't sell to anyone wearing the "
                "octogram, so take it off before you go in.\"",
            "zuri|coralhand|coral|armour|armor|armourer|armorer|chain|mail|shield|shields|leather|breastplate|"
            "jerkins":
                "\"Across the Row, Coral and Chain: Zuri Coralhand, a Xoton with arms like mooring lines. Coral, "
                "leather, chain, shields.\" He lowers his voice. \"The Fist owes her for thirty jerkins. Don't mention it "
                "unless you've an hour.\"",
            "row|neighbour|neighbours|neighbor|neighbors|shops":
                "\"Chandlers' Row, from Harbour Street up to the Night Market. Three shops and some rope-lofts.\" He "
                "points with his pencil. \"Me for kit, the elf for edges, the Xoton for armour. Between us we can send a "
                "body out the gate and get most of it back.\"",
            "marlo|khamisi|saltbeard|harbour|tarpaulin|competition|second|chances":
                "\"Marlo's Second Chances on Harbour Street buys what I won't: anything with a story. Khamisi sells "
                "Xoton rope off a tarpaulin in the market, cheap.\" He sniffs. \"I buy without questions. Marlo buys "
                "without daylight. Different trade.\"",
            "market|ines|grusha|saelwyn|stall|stalls|tea|fruit":
                "\"Up the Row, the Night Market. Mother Ines for fruit and everyone's business, the Jonulvicha cook for "
                "goat, the elf with the tea for charts and quiet.\" He nods. \"Too hot to shop by day. The whole Refuge "
                "shops after dark, and so do I.\"",
            ROOM:
                "\"A bed?\" He points with his pencil, this way and that. \"The Omberhulk on the square, a copper, bugs "
                "free. The Unicorn out by the trees, a copper with a bath, and quiet. The Turtle on Harbour Street, four "
                "copper, if you like Xotons singing. Gog's house, a silver, clean sheets. The Apothecary, a gold, if you "
                "like being looked through.\"",
            DRINK:
                "\"I don't pour. Six taverns in this town, and none of them talking to each other.\" He considers you. "
                "\"The Turtle for sailors, the Ogre for a fight, the Omberhulk for cheap, the Unicorn for quiet, the "
                "Apothecary for being seen, and the Stripperwitch for being somebody. Gog's mead, if you're asking me.\"",
            NEWS: _stages(
                (REMOVED, "\"News is irons on the grey coat and a magistrate's ship going home.\" He rubs his hands. "
                          "\"Best news this Row's had in thirty years. Buy something, I'm in a mood to round down.\""),
                (UPHELD, "\"News is the grey coat with the Throne's seal round his neck, and a decree on the square.\" "
                         "He doesn't look up. \"Read the decree. Then decide where you're sleeping.\""),
                (LANDED, "\"A magistrate of the Throne walked up the pier with two guards in black and silver.\" He "
                         "polishes his spectacles. \"I watched from the doorway. Old habit. The hearing's at ten in the "
                         "morning, at the Town Hall. Take papers.\""),
                (SIGHTED, "\"A sail at the harbour mouth, octogram on the main. The magistrate.\" His heels come "
                          "together. \"The grey coat's gone down to be first on the pier, smiling.\""),
                (DEAD, "\"They killed the mayor on the waterfront.\" He says it to the counter. \"I'll not sell the Fist "
                       "a nail again. Not ever.\""),
                (HOME, "\"The mayor's home and on the steps telling the whole square where the dues went. The grey coat's "
                       "barred in the Hall calling it the Throne's tithe.\" He grins, then doesn't. \"Wick says the Fist "
                       "is hunting whoever cut him loose. Mind how you go.\""),
                (SHIPPED, "\"The green-eyed brigantine went out on the one o'clock tide with a crate aboard.\" He doesn't "
                          "say any more about it."),
                (HIT, "\"Dominico's lads broke up Fat Gog's house at the midnight bell.\" He shakes his head. \"Peace "
                      "kept with a fist. Kept is a funny word for it.\""),
                otherwise="\"News? The grey coat says the mayor's upriver, and nobody believes it. Dominico wants Fat "
                          "Gog's books by midnight. And the officer in blue walks the pier every tide, looking at "
                          "hoods.\" He chalks a price. \"And rope's a gold the fifty foot. That's news that keeps.\""),
            DOING:
                "\"Open dusk to dawn, like the whole Refuge. Shut through the heat of the day, when I sleep on a cot "
                "behind this counter, where it's cool.\" He weighs nothing on the brass scale out of habit. \"Tonight: "
                "selling, buying, listening.\"",
            WORK: _stages(
                (REMOVED, "\"Work?\" He leans on the counter. \"Back to the old work: bring me what you find and I'll "
                          "pay a third. And if the officer in blue is still in town, I still want him gone, and the "
                          "lantern's still on its hook.\""),
                (UPHELD, "\"Work?\" He keeps his voice down. \"Get the hooded elves out, if they're still here, "
                         "before the decree bites. Bring me what you find, and I'll pay a third. And keep your name "
                         "out of the officer's book.\""),
                (HOME, "\"Work?\" He leans on the counter. \"I don't hire, I stake. Sit up with a witness when the "
                       "officer calls. Walk the hooded elves to the pale ship. Put papers in the magistrate's hand when "
                       "they land. Do any of it and your credit's good on my slate.\" He taps the ledger. \"Fat Gog pays "
                       "coin for the same. Take both.\""),
                otherwise="\"I don't hire, friend. I buy, and I stake.\" He leans on the counter. \"Find out what's in "
                          "the crate at the pier's end and tell Fat Gog, who pays. Walk the hooded elves at the Unicorn "
                          "to the pale ship, past the officer. Bring me anything you take off anyone, and I'll pay a "
                          "third. Do any of it and your credit's good here.\""),
            "xoton|xotons|lizardfolk|lizard|lizards|jonulvicha|peoples|races|humans":
                "\"Xotons pay on the nail, Lizardfolk pay in fish, Jonulvicha pay in full and look you in the eye while "
                "they do it.\" He shrugs. \"Elves pay in whatever they carried out. I take it all. Where a body's from "
                "isn't the shop's business.\"",
        },
        "default_line": [
            "He pushes his spectacles up onto his crown and waits. \"Kit, credit or the long road? Rope, lamps, rations, "
            "a potion for the bad night. Name a thing and I'll name a price.\"",
            "\"Couldn't say, friend.\" He chalks something on the slate. \"What I can say is fifty foot of hemp for a "
            "gold, and you look like someone who'll want it before the week's out.\"",
            "He sets the little brass scale between you. \"If you've brought something back from somewhere, I buy. No "
            "questions. I've no use for answers.\"",
            "\"Not my water.\" He nods at the wall. \"Blades next door at the Anvil, the elf's. Armour across the Row with "
            "the Xoton. Everything else that keeps you alive, here.\"",
            "He glances at the door as boots go by, and his heels come together. \"If you want to know how the Throne "
            "does things, I know a little. If you want to know about rope, I know a lot.\"",
        ],
        "routine": [
            {"at": 0.0, "place": "chandlery",
             "doing": "He sits on the iron-bound chest behind the counter with the lamp turned low, mending a torn "
                      "bedroll with a sailmaker's palm and needle, one ear on the street.",
             "beats": ["The stooped old chandler stops sewing at the sound of boots on the Row, and sits very straight "
                       "until they have gone by.",
                       "The old man in wire spectacles bites off a thread, holds a mended bedroll up to the lamp, and "
                       "grunts at it, satisfied."]},
            {"at": 3.0, "place": "chandlery",
             "doing": "He counts the night's takings into stacks of ten on the counter, twice, lips moving, and writes the "
                      "total in a fat ledger in a square hand.",
             "beats": ["The stooped old chandler counts a stack of coppers, frowns, and counts it again. It comes to the "
                       "same both times. He writes it down anyway.",
                       "The old man in wire spectacles turns to the back pages of his ledger, where there are prices and "
                       "no names, and adds a line."]},
            {"at": 5.0, "place": "chandlery",
             "doing": "He puts the shutters half up against the coming sun and sweeps the floor toward the door in short, "
                      "neat strokes, the way a man sweeps who was once taught to.",
             "beats": ["The stooped old chandler sweeps a little heap of sand and rope-ends out under the shutter and "
                       "stands the broom against the wall, exactly upright."]},
            {"at": 7.0, "place": "chandlery",
             "doing": "He sleeps through the heat on a cot behind the counter, where the shop is coolest, boots side by "
                      "side at its foot and one hand hanging down near the shelf where the hatchet is.",
             "beats": ["The old chandler mutters in his sleep, a word or two in a hard mountain accent, and turns over.",
                       "The old man on the cot behind the counter wakes at a cart in the street, listens with his eyes "
                       "open, and goes back to sleep."]},
            {"at": 14.0, "place": "chandlery",
             "doing": "He sits at the counter in his shirtsleeves eating salt fish and a mango off a knife, reading a "
                      "ship's news-sheet from Catan three weeks old.",
             "beats": ["The stooped old chandler reads the news-sheet with a finger under the lines, stops at a paragraph "
                       "about the Throne's missions, and reads it twice."]},
            {"at": 16.0, "place": "chandlery",
             "doing": "He takes in deliveries at the back, rope off a cart and salt fish by the barrel, ticking each "
                      "against a list and arguing every short weight.",
             "beats": ["The old man in wire spectacles weighs a barrel of salt fish on the big scale, shakes his head, and "
                       "takes two coppers off the carter's price."]},
            {"at": 18.0, "place": "chandlery",
             "doing": "He lights the lanterns hanging from the beams one by one and takes the shutters down as the heat "
                      "goes out of the day.",
             "beats": ["The stooped old chandler lights a lantern, hangs it on its hook, and sets it swinging with one "
                       "finger to see that it hangs true."]},
            {"at": 19.5, "place": "chandlery",
             "doing": "He leans in his doorway watching the Row fill up for the night, and writes something small in the "
                      "back of his ledger.",
             "pay": {"to": "Wick", "cp": 3, "for": "the day's news"},
             "beats": ["The old man in wire spectacles watches the Row from his doorway and nods across the way to the "
                       "elf smith, who nods back."]},
            {"at": 20.5, "place": "chandlery",
             "doing": "He serves the evening trade from behind the counter of scarred teak: rope to sailors, oil to "
                      "fishermen's wives, a crowbar to a stranger with an honest face, the price chalked on a slate for "
                      "each.",
             "beats": ["The stooped old chandler chalks a price on the slate, looks at a thin customer, rubs it out and "
                       "chalks it lower.",
                       "The old man in wire spectacles slides a coil of rope across the counter to a hooded stranger, "
                       "and waves the coin away."]},
            {"at": 22.0, "place": "chandlery",
             "doing": "He stands behind the counter with a slate of prices at his elbow, weighing a pair of sailors' "
                      "salvage on a little brass scale and paying them out of a drawer without asking where it came from.",
             "beats": ["The stooped old chandler weighs a pocketful of somebody's salvage on a brass scale, names a price, "
                       "and counts it out without a question.",
                       "Boots go by on the Row. The old chandler's heels come together behind the counter, and stay there "
                       "until the sound has gone.",
                       "The old man in wire spectacles taps the iron-bound chest under him twice with his heel, the way "
                       "some men touch wood."]},
        ],
        "beats": [
            "The stooped old chandler weighs a pocketful of somebody's salvage on a brass scale, names a price, and counts "
            "it out without a question.",
            "Boots go by on the Row. The old chandler's heels come together behind the counter, and stay there until the "
            "sound has gone.",
            "The old man in wire spectacles takes a flat tobacco tin from his apron, weighs it in his palm without "
            "opening it, and puts it away again.",
            "The stooped old chandler coils a line that was already coiled, and hangs it back on the same hook.",
        ],
    },

    # ---- Tamsin Vey, the Crooked Anvil ----------------------------------------------------------------------------
    "Tamsin Vey": {
        "look": "A tall, spare elf woman with cropped silver-white hair and a leather apron scorched in a hundred small "
                "places, her bare forearms freckled with old burns like a dusting of cinnamon. A slim rapier hangs at her "
                "hip even at the forge, and she sights down every blade she touches as if it might lie to her. She looks "
                "at a stranger's collar before she looks at their face.",
        "seen_as": "the silver-haired elf smith in the scorched apron",
        "brief": "You are Tamsin Vey, an elf in exile and the bladesmith of the Crooked Anvil on Chandlers' Row, the "
                 "street between Harbour Street and the Night Market in Klhyts Refuge. You were made a smith at the Keep "
                 "of Sheath in Aurelia, an old elven stronghold where one school folded steel with silver wire for longer "
                 "than the Throne has had a name; its blades make no sound leaving the sheath. Before you were its smith "
                 "you were its tester, the one who tries a blade on someone, so you are a good deal better with a rapier "
                 "than a shopkeeper should be. When the Army of the Faithful burned the Keep, your master stayed at the "
                 "forge and put his hammer in your hands, and you walked out through the smoke with it; it is the "
                 "cross-peen hammer you still use. Captain Aelith of the Moonmoth carried a seed out of the Hall of "
                 "Osmith in the same burning; her blade is your master's work, and you would know it in the dark. You "
                 "have been leaving places ever since, a step ahead of the Inquisition, whose rolls name every smith of "
                 "the Keep among the impure, and came to the Refuge twenty years ago because nobody here asks. The "
                 "Crooked Anvil is named for its anvil, which fell off a lighter onto the pier and bent its horn; it "
                 "rings a note you say is the Keep's bell. You make and sell blades, and your prices are fixed: the "
                 "rapier, your pride, 25 gp (it is worth forty, and you say so); a sword-cane, a rapier in a black "
                 "cane, 50 gp; dagger 2 gp, shortsword 10 gp, scimitar 25 gp, longsword 15 gp, handaxe 5 gp, battleaxe "
                 "10 gp, mace 5 gp, warhammer 15 gp, spear 1 gp, javelin 5 sp, glaive 20 gp, whip 2 gp, shortbow 25 gp, "
                 "longbow 50 gp, light crossbow 25 gp, twenty arrows or twenty bolts 1 gp. You forge in the cool before "
                 "dawn, sleep through the heat in a hammock at the back, and sell from dusk. Money: sailors, sellswords "
                 "and the odd noble pay well, and you are poor anyway, because you arm elves for nothing. Your scheme: "
                 "elves fleeing south on the Moonmoth come to your back door after the market shuts, sent by Saelwyn the "
                 "tea-seller; whoever shows you a living silverleaf, green at the stem, leaves with a blade, a knife at "
                 "least, and pays nothing. You have a small knife with a blue-corded hilt put by for Ithriel's daughter. "
                 "You will not sell to anyone wearing the Throne's octogram, and since the officer came half the lanes "
                 "wear it over their shirts, so you turn away good coin every night and say so to their faces. Two years "
                 "ago Dominico had you make him a sword-cane, the best blade you have made on this coast, with silver "
                 "folded into the steel the old way: eighty gold, agreed with a handshake in your doorway. He carries it "
                 "under his arm and has never paid a copper; the woman with the little book writes it down as the Row's "
                 "peace, paid in kind. You never agreed to any peace. What you want now: the eighty gold, or the cane "
                 "back; Lieutenant Voss gone, because he hunts your people and stands at the pier every tide; the "
                 "household at the Unicorn aboard the Moonmoth; and, for once, to stop leaving. What you will do: put "
                 "work in the way of whoever collects your debt (a blade made to their own hand for the cost of the "
                 "steel, and a word with Captain Aelith); owe whoever walks the household to the pier; show anyone who "
                 "buys a rapier how to hold it. What you offer players: the best blades in the Refuge at fixed prices, "
                 "plain opinions, and the road south for elves. How you push back: you refuse octogram-wearers flat, "
                 "you refuse the Fist credit, you do not haggle; you never raise your voice; threatened, you put your "
                 "hand on the rapier and wait, and you are faster than you look. If a magistrate of the Pain Arm lands, "
                 "you take the blades off the wall and arm every elf in town before the decree; if the decree demands "
                 "the elves, you go to the Moonmoth or you stand in your doorway with a blade, whichever the night "
                 "allows. Fears: smoke at night, an hourglass at a magistrate's throat, and the night the Moonmoth sails "
                 "without a place for you. You like Hob Merrow next door (he once said he had seen families turned back "
                 "on a pass, and never said more, and you have never asked), Zuri across the Row (her coral is a craft "
                 "you respect), Fat Gog, Saelwyn and Aelith; you despise Voss, and you do not like what has got into "
                 "Dominico's ring. Voice: spare, exact, dry; you talk about steel as if it were people. 'A blade tells "
                 "you everything, if you hold it still.' 'Twenty-five gold. It's worth forty. I'm sentimental.'",
        "scheme": "She arms elves fleeing south on the Moonmoth for nothing at her back door (a living silverleaf buys a "
                  "blade), refuses to sell to anyone wearing the octogram, and wants Dominico's eighty gold for his "
                  "sword-cane, or the cane, and will put work in the way of whoever collects it.",
        "purse": 600,
        "dialog": {
            "name|names|called|introduce|yourself|tamsin|vey":
                "She sights down a blade before she answers. \"Tamsin Vey. The Anvil's mine, crooked and all.\" She sets "
                "the blade down. \"And you're someone who wants something sharp.\"",
            HELLO: _stages(
                (REMOVED, "\"Evening.\" She is very nearly smiling. \"The grey coat's in irons. I've put an edge on "
                          "everything in the shop to celebrate. Want one?\""),
                (UPHELD, "She doesn't look up from the whetstone. \"Evening. Shut the door. If you're wearing the eight "
                         "arms, shut it from the other side.\""),
                (LANDED, "She looks at your collar first, and for longer than usual. \"Evening. There's a Throne ship at "
                         "the pier, so I look at collars. Yours will do. What do you need?\""),
                (DEAD, "\"Evening.\" Her voice is flat. \"The man who let us all stay is dead. Buy something sharp. You'll "
                       "need it.\""),
                (HOME, "\"Evening.\" She looks almost warm. \"The mayor's home, the town's nervous, and nervous towns buy "
                       "steel. What'll it be?\""),
                otherwise="She looks at your collar before she looks at your face, and nods as if you had passed "
                          "something. \"Evening. Blades on the wall, prices on the pegs. The rapier on the counter is "
                          "for holding. Go on.\""),
            "price|prices|cost|costs|wares|stock|sell|selling|sells|buy|buying|shop|list|weapon|weapons|blade|"
            "blades|steel|edges":
                "She walks you along the wall, touching each peg as she goes. \"Rapier, twenty-five gold, my pride. "
                "Sword-cane, fifty. Dagger two, shortsword ten, scimitar twenty-five, longsword fifteen. Handaxe five, "
                "battleaxe ten, mace five, warhammer fifteen. Spear a gold, javelin five silver, glaive twenty, whip two. "
                "Shortbow twenty-five, longbow fifty, light crossbow twenty-five. Arrows or bolts, a gold the twenty.\" "
                "She stops by the door. \"Nothing for anyone wearing the octogram. Not at any price.\"",
            "rapier|rapiers|fencing|duel|duels|duelling|dueling|duellist|thrust|finesse|best|pride|elegant":
                "She lifts the rapier off the counter and lays it across your palms. It weighs almost nothing. "
                "\"Twenty-five gold. Steel folded with silver wire, the way the Keep of Sheath taught it, before the "
                "Throne burned the Keep.\" She lets you find the balance. \"It's worth forty. I'm sentimental. It makes no "
                "sound leaving the sheath, so neither will you.\"",
            "dagger|daggers|knife|knives|dirk|stiletto|shortsword|shortswords|short|small":
                "\"Dagger, two gold. Balanced to throw, and to stay where it lands.\" She sets a shortsword beside it. "
                "\"Shortsword, ten. Quick, for a quick hand. If you'll fight close in the lanes, it's this or the "
                "rapier.\"",
            "scimitar|scimitars|curved|sabre|saber|cutlass|cutlasses":
                "\"Scimitar, twenty-five gold.\" She draws it in a long hiss and the lamplight runs down its curve. "
                "\"Light, curved, fast. The Xotons buy them for boarding and the Jonulvicha for showing off. Both are "
                "right.\"",
            "longsword|longswords|sword|swords|broadsword|broadswords":
                "\"Longsword, fifteen gold. One hand or two.\" She hefts it. \"A soldier's sword: honest, heavy, "
                "forgiving. If you want clever, it's the rapier.\"",
            "cane|canes|sword-cane|swordcane|sword|walking|stick|hidden|concealed|disguised":
                "She takes a black cane from the rack and gives the head a quarter turn; a thin blade slides out without "
                "a whisper. \"Sword-cane, fifty gold. A rapier in a walking stick, for people who aren't supposed to be "
                "armed.\" She seats it again. \"I made a better one for a man in a black coat. He carries it under his "
                "arm and has never paid for it.\"",
            "axe|axes|handaxe|handaxes|battleaxe|battleaxes|hatchet|hatchets":
                "\"Handaxe, five gold: throw it or hold it. Battleaxe, ten, one hand or two.\" She runs a thumb along a "
                "bearded edge. \"Axes forgive a bad hand. Blades don't.\"",
            "mace|maces|hammer|hammers|warhammer|warhammers|club|clubs|blunt":
                "\"Mace, five gold. Warhammer, fifteen, one hand or two, for armour a blade won't open.\" She glances at "
                "the old hammer lying on the anvil. \"That one's not for sale. It was my master's.\"",
            "glaive|glaives|spear|spears|polearm|polearms|pike|pikes|halberd|reach|javelin|javelins|throwing":
                "\"Spear, a gold. Javelin, five silver, and buy four. Glaive, twenty gold: a blade on a pole, for keeping "
                "a crowd off.\" She nods toward Harbour Street. \"The big Jonulvicha sellsword at the Ogre carries one I'd "
                "not let in my door. Tell him I'd make him a better one.\"",
            "whip|whips|lash|lashes":
                "\"Whip, two gold.\" She coils it on the counter, unimpressed with it. \"Reaches farther than you'd think "
                "and hurts less than you'd hope. Sailors buy them. I don't ask.\"",
            "bow|bows|shortbow|shortbows|longbow|longbows|archery|archer|shoot|shooting":
                "\"Shortbow, twenty-five gold. Longbow, fifty: yew from the hills past the Treeline Road, seasoned two "
                "years.\" She tests a string with one finger. \"Elves made the longbow first. Humans made it famous. I "
                "make it properly.\"",
            "crossbow|crossbows":
                "\"Light crossbow, twenty-five gold.\" She works it; it cocks with a sound like a door locking. \"Point "
                "and pull. It forgives everything except being slow to reload. Bolts, a gold the twenty.\"",
            "arrows|arrow|bolts|bolt|ammunition|ammo|quiver|quivers":
                "\"Twenty arrows, a gold. Twenty bolts, a gold.\" She tips a bundle out of a quiver. \"Fletched with gull. "
                "Don't laugh. Gulls fly straighter than you'd think.\"",
            "commission|custom|bespoke|measure|order|forge|forged|forging|craft|own":
                "\"A blade to your own hand?\" She takes your wrist without asking and turns it to the lamp. \"I forge "
                "before dawn, while the air's cool. Steel, folding, quench: a week. And I'd want to see you hold the "
                "rapier first.\" She lets go. \"For whoever brings me Dominico's eighty gold, I make it at the cost of the "
                "steel.\"",
            "smith|smiths|smithing|bladesmith|blacksmith|anvil|crooked|trade|ring|rings|bell":
                "She raps the bent horn of the anvil and it rings, a long, odd, sweet note. \"Fell off a lighter onto the "
                "pier and bent its horn. Nobody wanted it.\" She listens until the note dies. \"It rings like the bell at "
                "the Keep of Sheath. So I bought it, and named the shop for it.\"",
            "keep|sheath|burned|burning|burnt|fire|aurelia|master|exile|fled|flee|from|born|home|homeland|origin|"
            "past|before":
                "She is quiet a moment. \"The Keep of Sheath, in Aurelia. A school of smiths older than the Throne's "
                "name.\" She turns the old hammer over. \"When the Army of the Faithful burned it, my master stayed at the "
                "forge and put this in my hands. I've been walking south since. Twenty years here, and nobody asks.\" "
                "She sets it down. \"I'd like to keep it that way.\"",
            "debt|debts|owes|owed|owe|unpaid|collect|collecting|collector|eighty|account":
                "\"Eighty gold.\" She says it like a measurement. \"Agreed with a handshake in that doorway two years "
                "ago, for the best blade I've made on this coast. He carries it under his arm. His woman with the little "
                "book calls it the Row's peace, paid in kind.\" Her hand lies very still on the counter. \"I never sold "
                "peace. Bring me the eighty, or bring me the cane, and I'll make you a blade to your own hand for the cost "
                "of the steel. And I'll say your name to Captain Aelith.\"",
            "dominico|fist|enforcer|black|coat|band|sabeth|crane|book|whisper|whispers":
                "\"Dominico keeps his word, they say. He just decides afterwards what it was.\" She tests an edge on her "
                "thumbnail. \"And he never used to turn that ring. Something whispers out of it at night, the Xotons at "
                "the Turtle say.\" A thin smile. \"The old school says silver in the steel bites what iron won't. I folded "
                "silver into his cane. Funny, that.\"",
            "octogram|octograms|throne|vorkath|vorkathian|eight|arms|goddess|faith|church|sigil|refuse|refused|"
            "refusing":
                "\"I don't sell to the eight arms.\" She says it flatly. \"Not to the officer, not to the constable who "
                "takes his coin, not to the lane-boys who started wearing it over their shirts the week he came. Take it "
                "off and I'll sell to you. Wear it and I'll watch you leave.\"",
            "inquisition|inquisitor|inquisitors|teflon|hourglass|pain|penance|impure|purge":
                "\"The Inquisition made me what I am.\" She doesn't explain that. \"Every smith of the Keep is on their "
                "rolls among the impure. They don't forget a name, and they don't forgive a blade.\" She hangs the rapier "
                "back on her hip. \"If a magistrate lands with an hourglass at the throat, I'll be on the Moonmoth or in "
                "my doorway. Not in between.\"",
            "voss|lieutenant|officer|uniform|blue|aurel":
                "\"The officer in blue stands at the head of the pier every tide and looks at hoods.\" Her voice doesn't "
                "change, which is worse. \"He came in once, the first week. I looked at his collar and said no, and he "
                "thanked me, very politely, and wrote something down.\" She tests an edge. \"I'd like him gone. I'd "
                "settle for him leaving, and owe whoever arranged it.\"",
            "elf|elves|exiles|refugees|south|passage|tower|silverleaf|leaf|token|road":
                "\"There's a road south for our kind, and a tower at the end of it.\" She doesn't lower her voice; she "
                "stops using it for anyone else. \"If you're one of mine and going, come to the back door after the "
                "market shuts, and show me a living silverleaf, green at the stem. You don't leave unarmed, and you don't "
                "pay.\"",
            "moonmoth|aelith|captain|pale|ship|gangplank|grown|silverwood|osmith":
                "\"The Moonmoth.\" She almost smiles. \"Captain Aelith carried her out of the Hall of Osmith as a seed in "
                "her mouth, the same season I carried a hammer out of the Keep. Her blade's my master's work. I'd know it "
                "in the dark.\" She looks toward the harbour. \"She takes no one an elf won't vouch for. I could put in a "
                "word, for someone who'd earned it.\"",
            "ithriel|hooded|household|scholar|unicorn|daughter|miravel|girl|child":
                "\"The scholar at the Unicorn and her four.\" She opens a drawer and shows you a small knife, child-sized, "
                "the hilt wrapped in blue cord, then closes it again. \"For the girl, when they go. I'll not have her "
                "cross an ocean with nothing in her hand.\" She looks at you. \"Walk them to the pale ship past the "
                "officer, and I'll owe you.\"",
            "saelwyn|tea|charts|chart|charm|charms|market":
                "\"The tea-seller in the Night Market.\" Something careful comes into her face. \"She tells the Moonmoth "
                "who's in town and who's hunting them, and she sends our people to my back door. If she ever sends you, "
                "you'll know why.\"",
            KLHYT: _stages(
                (DEAD, "\"Dead.\" She sets the blade down. \"He let us stay without asking why. That's rarer than "
                       "steel.\" She looks at the door. \"There's a blade on this wall for whoever answers for it.\""),
                (HOME, "\"Home, and talking on the Hall steps.\" She nods once. \"Good. Somebody should say it out loud: "
                       "nobody here is asked where they came from. Keep him home, and the rest of us can stay.\""),
                (SHIPPED, "\"Gone on the tide in a crate, they say.\" Her hand closes on the old hammer. \"Then the "
                          "Charter went with him. I'll start packing. Again.\""),
                otherwise="\"Four nights gone, and the grey coat says upriver.\" She doesn't believe it and doesn't "
                          "bother saying so. \"Fat Gog will pay for proof of where. I'd look where the Fist stands still: "
                          "there's a man on a bollard at the pier's end who hasn't moved in four nights.\""),
            "custodian|grey|gray|dues|tithe|skim|hall|clerk": _stages(
                (REMOVED, "\"In irons.\" She draws a whetstone down a blade, once, slowly, like a full stop. \"Good.\""),
                (UPHELD, "\"Upheld, with the Throne's seal round his neck.\" She looks at the old hammer. \"Then the "
                         "Charter's paint, and the Throne's iron. I know which lasts.\""),
                (HOME, "\"Found out, and wearing the eight arms openly now, barred in the Hall with the strongbox.\" Her "
                       "lip curls. \"He's waiting for a ship. So was everyone who ever hunted me.\""),
                otherwise="\"The grey coat? He bought a silver-handled letter-opener from me once, paid exactly, and "
                          "looked at my ears the whole time.\" She shrugs. \"A man who counts everything. He hasn't "
                          "counted me yet.\""),
            "gog|fat|guild|stripperwitch|river|lizardfolk|lizard|lizards":
                "\"Fat Gog's people pay, Lizardfolk included, and I sell to Lizardfolk whatever the Turtle thinks.\" She "
                "tests an edge. \"Gog keeps the town's shadows tidy. Elves live in shadows. We get on.\"",
            MAGISTRATE: _stages(
                (REMOVED, "\"Removed. Irons, and down to the ship.\" She doesn't celebrate. \"And the magistrate sails "
                          "home and tells the Throne exactly where we all are. Enjoy tonight.\""),
                (UPHELD, "\"Upheld.\" She is already sorting blades into bundles. \"I've done this before. Pack light, "
                         "keep the edge, go south.\""),
                (_arm("pain"), "She goes very still. \"An hourglass at the throat. The Inquisition, on this pier.\" Then "
                               "she moves, quickly, taking blades off the wall and rolling them in sailcloth. \"Every elf "
                               "in the Refuge needs a blade and a gangplank before the decree. Help me carry, or get out "
                               "of my light.\""),
                (_arm("chaos"), "\"Lightning in the ear: Hester-Stanhope's. And that ship of theirs has been looking at "
                                "the Moonmoth since it tied up.\" She frowns. \"If they take her, our road south goes "
                                "with her. Somebody tell Captain Aelith to stand off the harbour mouth.\""),
                (_arm("death"), "\"A child's wooden hand. Gwendoline's.\" She is quiet. \"The Death Arm forbids our rites. "
                                "We sing our dead into the trees. They'd have us put in boxes.\""),
                (LANDED, "\"A magistrate of the Throne on the pier, and guards looking at ears.\" She touches one of her "
                         "own. \"Bring them papers against the grey coat. And keep your collar clean.\""),
                (SIGHTED, "\"A sail with the octogram at the harbour mouth.\" She takes the rapier off the counter and "
                          "hangs it on her hip. \"That's all. I'll be here. Selling.\""),
                (HOME, "\"A magistrate's due, the grey coat says, months at sea from Landfall.\" She shrugs. \"Whichever "
                       "Arm they serve, none of them likes elves. Pray for the one who drinks.\""),
                otherwise="\"Magistrates?\" She turns a blade in the lamp. \"The Throne sends one to its colonies now and "
                          "then. The grey coat's waiting for one, I hear. So am I.\" She hangs the blade up."),
            DECREE: _stages(
                (_decree("pain"), "\"Every elf handed over, and no magic but theirs.\" She has a pack on the counter and "
                                  "the rapier on her hip. \"I'm arming every one of us I can find tonight and walking them "
                                  "to the Moonmoth.\" She nods at a long bundle of sailcloth by the door. \"If you'd help, "
                                  "carry. If you'd not, don't stand in my door.\""),
                (_decree("death"), "\"No elven rites.\" She looks at the old hammer a long time. \"My master went into the "
                                   "fire singing. They'd not even let us do that.\" Her jaw sets. \"We'll sing anyway. "
                                   "Quietly.\""),
                (_decree("chaos"), "\"The Moonmoth taken for the Throne's prize.\" She is white to the lips. \"Then the "
                                   "road south is a road on foot. Find Captain Aelith before they board her and tell her: "
                                   "the harbour mouth, tonight.\""),
                (_decree("war"), "\"No Lizardfolk to bear a blade within the walls.\" She takes a scimitar off the wall "
                                 "and lays it on the counter, deliberately. \"Then I'll sell to Lizardfolk outside the "
                                 "gate. I can walk.\""),
                (_decree("peace"), "\"Every name and where it came from, in the goddess's book.\" She almost laughs. "
                                   "\"Mine's already in a book. The Inquisition's. Theirs can borrow it.\""),
                (_decree("destiny"), "\"A census.\" She shrugs. \"Elves are easy to count. We stand out.\" Her eyes go "
                                     "to the wall she shares with the chandlery. \"Old Hob won't take it so calmly. Look "
                                     "in on him.\""),
                (_decree("pleasure"), "\"Licences, and elves drink where the licence says.\" She snorts. \"I don't drink "
                                      "in their taverns. I sell to the people who do.\""),
                (_decree("life"), "\"Wash, or lose your stall.\" She holds up her burn-freckled forearms. \"I quench "
                                  "steel in seawater every morning. I'm the cleanest thing on the Row.\""),
                (LANDED, "\"There'll be a decree. The Throne doesn't cross an ocean to say thank you.\" She hangs a blade "
                         "on its peg. \"Whatever it is, it won't be written with elves in mind. Not kindly.\""),
                otherwise="\"The only decree in this town is the Charter on the Hall porch.\" She tests an edge. \"Article "
                          "One. I'd forge it into a blade if I could.\""),
            "hob|merrow|chandler|chandlery|rope|lantern|lanterns|gear|kit|pack|rations|supplies|potion|potions":
                "\"Next door, Hob Merrow: rope, lanterns, packs, rations, potions when he has them.\" She nods at the "
                "wall between. \"He sells grappling hooks I forge, and he'll buy what you bring back from wherever you've "
                "been, and not ask. Good man. Stands like a soldier when boots go by.\" A pause. \"Don't mention it to "
                "him.\"",
            "zuri|coralhand|coral|armour|armor|armourer|armorer|shield|shields|mail|chain|leather|breastplate|"
            "xoton|xotons":
                "\"Across the Row, Coral and Chain. Zuri Coralhand, a Xoton, and the only armourer whose work I'd want "
                "my own blade stopped by.\" She nods. \"Coral, leather, chain, shields. Dominico owes her too, for thirty "
                "jerkins. We have that in common.\"",
            "row|neighbour|neighbours|neighbor|neighbors|chandlers|street|shops":
                "\"Chandlers' Row. Harbour Street at the bottom, the Night Market at the top, and three shops between "
                "that the Fist thinks it owns.\" She hangs a blade. \"Hob for kit, me for edges, Zuri for armour. "
                "Between us, you go out the gate dressed for it.\"",
            NEWS: _stages(
                (REMOVED, "\"The grey coat in irons, and the magistrate's ship taking him home.\" She sights down a blade. "
                          "\"That's the news. The rest is the Throne remembering us. That's next week's.\""),
                (UPHELD, "\"The grey coat upheld, and a decree on the square.\" She doesn't look up. \"Read it before you "
                         "buy anything. You may want something longer.\""),
                (LANDED, "\"A magistrate walked up the pier with two guards in black and silver, and looked at every "
                         "face.\" She touches her ear. \"The hearing's at ten in the morning, at the Town Hall.\""),
                (SIGHTED, "\"An octogram on a mainsail at the harbour mouth. The magistrate.\" She lays the rapier on the "
                          "counter where her hand can find it. \"That's all the news there is tonight.\""),
                (DEAD, "\"They killed the mayor on the waterfront.\" She puts the whetstone down. \"Now we find out what "
                       "this town is without him.\""),
                (HOME, "\"The mayor's home and on the steps, and the grey coat's barred in the Hall calling it the "
                       "Throne's tithe.\" She tests an edge. \"And the Fist is out hunting whoever cut him loose. If "
                       "that's you, buy something.\""),
                (SHIPPED, "\"The green-eyed brigantine went out at one with a crate aboard.\" She says nothing else for "
                          "a while. \"Article One went with it, I expect.\""),
                (HIT, "\"Dominico's men broke Fat Gog's house at the bell.\" She runs a whetstone down a blade. \"Peace, "
                      "kept.\""),
                otherwise="\"News?\" She sights down a blade. \"The grey coat says the mayor's upriver. The officer in "
                          "blue says nothing, and stands at the pier every tide watching hoods. Dominico says midnight "
                          "for Fat Gog.\" She hangs it up. \"I say twenty-five gold for the rapier.\""),
            ROOM:
                "\"The Touchy Unicorn, out on the Treeline Road. A copper, with a bath, and a woman at the desk who "
                "doesn't write down who stays.\" A pause. \"Or writes it and burns it. Elves sleep there. So should you, "
                "if you want quiet.\"",
            DRINK:
                "\"I don't, much.\" She considers. \"The High Apothecary used to feed our kind, till the officer came. "
                "The Unicorn's quiet. The Turtle's loud, and the Xotons will drink you under the table and then carry you "
                "home. Pick your danger.\"",
            DOING:
                "\"Selling, till the market packs up. Then the back door, for anyone who needs it.\" She tests an edge. "
                "\"Before dawn, the forge, while the air's cool. Through the heat, I sleep. Nobody sensible works this "
                "coast at noon.\"",
            "haggle|haggling|discount|cheaper|cheap|bargain|deal|credit|tab|slate|less|lower|afford":
                "\"No.\" She doesn't look up. \"Twenty-five for the rapier is already a gift. And no credit: the last man "
                "I trusted on credit carries my best blade under his arm and calls it peace.\"",
            WORK:
                "\"Work? Three things, and I pay in steel.\" She counts them on scorched fingers. \"Dominico's eighty "
                "gold for his cane, or the cane: a blade to your own hand for the cost of the steel. The hooded household "
                "at the Unicorn, walked to the Moonmoth past the officer: I'll owe you. And the officer himself, gone "
                "from this town by any road the magistrate won't hang you for: name your blade.\"",
            "lesson|lessons|teach|teaching|train|training|learn|fight|fighting|swordplay|swordsmanship|tester":
                "\"I'll show anyone who buys a rapier how to hold it. Once, free.\" She stands, and for a moment she isn't "
                "a smith at all. \"I was the Keep's tester before I was its smith. A blade has to be tried by someone.\" "
                "She sits again. \"Buy the rapier first.\"",
        },
        "default_line": [
            "She holds the rapier out to you hilt first, without a word, and watches how you take it. \"Twenty-five "
            "gold. Ask me about anything on the wall.\"",
            "\"Hm.\" She sights down a blade at the lamp. \"Steel, I can answer. The rest, ask someone who talks more.\"",
            "\"Rope and lanterns next door, armour across the Row. Here, it's edges.\" She taps the wall of blades.",
            "She looks at your collar before your face. \"No octogram. Good. Then we can talk: blades, the man who owes "
            "me, or the road south.\"",
            "\"If it's the road south you mean, say so plainly, and quietly.\" She goes back to her whetstone.",
        ],
        "routine": [
            {"at": 0.0, "place": "anvil",
             "doing": "She sits at the back of the shop with a blade across her knees and a whetstone in her hand, putting "
                      "an edge on it in long, even strokes that sound like the sea on shingle.",
             "beats": ["The silver-haired elf smith draws the whetstone down a blade, lifts it to the lamp, and lays it "
                       "back across her knees without a word.",
                       "The elf smith in the scorched apron tests an edge on her thumbnail, frowns, and starts again from "
                       "the heel."]},
            {"at": 1.0, "place": "anvil",
             "doing": "She stands at the half-open back door with the lamp turned down, talking low with someone hooded in "
                      "the lane, and passes out a long bundle wrapped in sailcloth.",
             "beats": ["The silver-haired elf smith closes the back door softly and stands with her palm flat against it "
                       "for a moment, listening to footsteps go away toward the harbour.",
                       "The elf smith takes a small knife with a blue-corded hilt out of a drawer, looks at it, and puts "
                       "it back."]},
            {"at": 2.0, "place": "anvil",
             "doing": "She keeps the shop for the last of the market's trade, a rapier on the counter for whoever wants to "
                      "feel the balance and her eyes on every collar that comes in.",
             "beats": ["A man with an octogram stitched on his shirt asks the silver-haired elf smith the price of a "
                       "dagger. She looks at his collar and says \"No,\" and goes back to her whetstone until he leaves."]},
            {"at": 4.0, "place": "anvil",
             "doing": "She works the forge in the cool before dawn, the bellows breathing, her hammer ringing on an anvil "
                      "with a bent horn, folding a bar of steel over itself again and again.",
             "beats": ["The elf smith strikes the bent horn of the anvil by accident, and stops to listen to it ring "
                       "until the note dies away.",
                       "The silver-haired elf smith lays a thread of silver wire along a glowing bar, folds the bar over "
                       "it, and strikes."]},
            {"at": 7.0, "place": "anvil",
             "doing": "She quenches the morning's last blade in a trough of oil and seawater in a burst of steam, rakes "
                      "out the forge, and puts the shutters up against the sun.",
             "beats": ["Steam boils up from the quench trough. The elf smith watches the blade come out of it the way "
                       "other people watch a child come in out of the rain."]},
            {"at": 8.0, "place": "anvil",
             "doing": "She sleeps through the heat in a hammock slung across the back of the forge, a bare rapier hanging "
                      "on a nail within reach of her hand.",
             "beats": ["The elf in the hammock opens her eyes at a smell of woodsmoke from the street, lies very still "
                       "until it passes, and closes them again."]},
            {"at": 15.0, "place": "anvil",
             "doing": "She grinds and polishes at a treadle wheel, sparks fanning across the floor, holding each edge up "
                      "to the light from the shutters.",
             "beats": ["The silver-haired elf smith holds a new blade up to the slit of light between the shutters and "
                       "turns it until the light runs down it without a break."]},
            {"at": 18.0, "place": "anvil",
             "doing": "She takes the shutters down as the day cools and hangs the evening's blades on the wall pegs, "
                      "sighting down each one before it goes up.",
             "beats": ["The elf smith hangs a rapier on its peg, straightens it a hair, and steps back to look at the "
                       "whole wall."]},
            {"at": 20.0, "place": "anvil",
             "doing": "She keeps the shop: blades on the wall, prices on the pegs, a rapier on the counter for whoever "
                      "wants to hold it, and her eyes on every stranger's collar before their face.",
             "beats": ["The silver-haired elf smith hands a rapier hilt first to a young sailor and watches how he takes "
                       "it, and takes it back, and shows him again.",
                       "The elf smith in the scorched apron sights down a blade at the lamp, as if it might be lying to "
                       "her, and hangs it back up.",
                       "Across the Row a man in a black coat goes by with a silver-headed cane under his arm. The elf "
                       "smith stops what she is doing and watches him all the way to the corner."]},
        ],
        "beats": [
            "The silver-haired elf smith sights down a blade at the lamp, as if it might be lying to her, and hangs it "
            "back on its peg.",
            "The elf smith in the scorched apron raps the bent horn of the anvil with a knuckle and listens to it ring.",
            "The silver-haired elf smith looks at a customer's collar, then at their face, and only then says good "
            "evening.",
            "The elf smith draws a whetstone down a blade in one long stroke, the sound like the sea going out over "
            "shingle.",
        ],
    },

    # ---- Zuri Coralhand, Coral and Chain ------------------------------------------------------------------------
    "Zuri Coralhand": {
        "look": "A low-built Xoton woman, a black-skinned dwarf of the sea nearly as wide as she is tall, her black braids bound in copper "
                "wire and her forearms latticed with fine pale scars. She works bare-armed in a leather apron hung with "
                "awls, rivets and a little hammer, over a shirt of pale coral plates that clicks softly when she moves, "
                "and the iron-grey wave of House Ironwake is tattooed on her shoulder. She looks at everyone's shoulders "
                "before their faces, as if measuring them for something.",
        "seen_as": "the Xoton woman in the coral shirt, a wide black-skinned sea dwarf",
        "brief": "You are Zuri Coralhand, a Xoton armourer, and Coral and Chain on Chandlers' Row is yours: the street "
                 "between Harbour Street and the Night Market in Klhyts Refuge. You were born an Ironwake on the Crows "
                 "Nest and are cousin to Amara Ironwake, bosun of the Whispers of the Deep. Coralhand is a craft-name the "
                 "coral-wrights give to one who can cut living coral without bleeding to death, and your forearms show "
                 "what it cost to earn. House Ironwake set you ashore ten years ago to keep a shop where Xoton crews "
                 "could buy their own people's armour at shore prices, and you stayed, because you are good at it and "
                 "because somebody has to stand up for Xotons on this waterfront while Amara is at sea. You make Xoton "
                 "coral armour (pale reef coral riveted onto sharkskin: light, quiet, as good as leather and it never "
                 "rots or rusts, and nobody else on the coast can make it), and you learned leather, chain and scale from "
                 "a Jonulvicha armourer on the Catan quays. Your prices are fixed: padded 5 gp, leather 10 gp, studded "
                 "leather 45 gp, hide 10 gp, coral armour 20 gp, chain shirt 50 gp, scale mail 50 gp, ring mail 30 gp, "
                 "chain mail 75 gp, breastplate 400 gp, shield 10 gp. You mend straps and buckles free for anyone "
                 "wearing your work. The breastplate on the end stand was made to a Throne officer's measure: Lieutenant "
                 "Voss sent Constable Rosa Quint to order it for 'a gentleman', and when he came to the fitting you saw "
                 "the eight arms at his throat and showed him the door; it will fit anyone with his shoulders. You made "
                 "Kwasi Foamtooth's coral tooth, and he has never paid for that either. Money: Xoton crews and "
                 "sellswords pay well and on the nail; your coin goes on coral from Xoton divers, iron wire, and your "
                 "cousin's crew's fines when Amara is short. Your grievance: a year ago Dominico ordered thirty leather "
                 "jerkins for his men, boiled and dyed black, at four gold apiece, a hundred and twenty gold. Every one of "
                 "the Fist in leather is wearing your work, you have not seen a copper, and the woman with the little "
                 "book wrote it down in front of you as the Row's peace, paid in kind. You never sold peace. You want the "
                 "hundred and twenty gold in your hand, and until then you will not sell the Fist so much as a buckle. "
                 "You will not arm the Throne's men at any price: not the officer, not the guards off any ship of "
                 "theirs, not anyone in their colours. You want respect for Xoton traders: the watch fines Xoton sailors "
                 "three copper a song and looks at its boots while the Fist breaks heads; the Custodian's dues fall "
                 "hardest on Xoton cogs; half the town says Zoton and laughs. What you want now: the jerkins paid for; "
                 "Amara's four ashore (Dayo, Imani, Kwasi, Little Jabali) aboard the Whispers before the morning tide "
                 "and out of the watch's cells; the thief who walks rope out of the Whispers' hold found (Amara knots red "
                 "thread into every coil, and you tell anyone who will listen to look for it on the stalls); the "
                 "Custodian gone, because his dues rob Xoton ships; and, when you die, the sea, which your will says and "
                 "Amara has sworn to. What you will do: stand in the door with the rivet hammer when the Fist comes "
                 "calling; send the chain mail out to the Whispers if a War Arm magistrate lands, rather than see it "
                 "requisitioned; put armour at cost for life in the way of whoever collects the Fist's debt. What you "
                 "offer players: armour fitted by eye; plain advice on what to wear (light for those who fight with "
                 "their feet; chain mail and a shield for those who stand, if their shoulders will carry it; scale, ring "
                 "and chain mail tell every guard in the street you are coming); mending; a word to Amara and Captain "
                 "Eirik for anyone who does right by a Xoton crew. How you push back: blunt refusals; no haggling and no "
                 "credit; you will not be talked down to, and you correct Zoton every time; you are stronger than any "
                 "two of the Fist think. Fears: being put in the dirt; a War Arm levy taking Xoton sailors; a Death Arm "
                 "decree forbidding burial at sea. You like Hob Merrow two doors down (pays on the day and minds his own "
                 "business so hard it must be hiding something), Tamsin across the way (a craftswoman you respect, and "
                 "a fellow creditor of Dominico's), Amara, Captain Eirik and Ruk Halfhand's gang; you think Khamisi says "
                 "sea-born too often and Marlo should try a boat again. Voice: blunt, practical, a foghorn's cousin; "
                 "measures everything, and everyone. 'Xoton, with the X.' 'Armour's a promise. Mine keep theirs.' "
                 "'Coral bends. Iron breaks. Think on it.'",
        "scheme": "She will not sell the Fist so much as a buckle until Dominico pays the hundred and twenty gold he owes "
                  "for thirty black jerkins, will not arm the Throne's men at any price, and puts armour at cost in the "
                  "way of anyone who collects her debt or gets her cousin's Xoton crew aboard by the morning tide.",
        "purse": 450,
        "dialog": {
            "name|names|called|introduce|yourself|zuri|coralhand":
                "She holds up a hand criss-crossed with fine white scars. \"Zuri. Coralhand, which you earn: cut living "
                "coral long enough and it cuts you back.\" She drops the hand. \"Born an Ironwake. Xoton, with the X.\"",
            HELLO: _stages(
                (REMOVED, "\"Evening!\" She thumps the bench and the coral plates jump. \"Grey coat in irons, and the "
                          "harbour dues come back honest. Come in, come in, what do you need?\""),
                (UPHELD, "\"Evening.\" Flat. She looks at your shoulders, and then at your collar. \"No eight arms. Good. "
                         "Come in, then.\""),
                (LANDED, "\"Evening.\" She looks past you down the Row toward the harbour, where the Throne's ship lies. "
                         "\"If you're off that ship, keep walking. If not, come in.\""),
                (DEAD, "\"Evening. Sorry day. The founder's dead, and the town's nobody standing at the top of it.\" She "
                       "moves a stool toward you with her foot. \"Come in out of it.\""),
                (HOME, "\"Evening!\" She grins. \"Mayor's home and on the steps. Good night for business: nervous towns "
                       "buy armour.\" She looks at your shoulders. \"Hm.\""),
                (HIT, "\"Evening. The Fist broke the Stripperwitch at the bell, wearing my jerkins.\" Her jaw works. "
                      "\"Come in.\""),
                otherwise="She looks at your shoulders before your face, then nods. \"Evening. Coral and Chain: coral, "
                          "leather, chain, shields, and I'll tell you which before you ask. Come in.\""),
            "price|prices|cost|costs|wares|stock|sell|selling|sells|buy|buying|shop|list|armour|armor|armours|"
            "armors|protection":
                "She raps the stands one by one as she names them. \"Padded, five gold. Leather, ten. Studded, forty-five. "
                "Hide, ten. Xoton coral, twenty, and nobody else on this coast makes it. Chain shirt fifty, scale fifty, "
                "ring mail thirty, chain mail seventy-five. The breastplate on the end, four hundred. Shield, ten.\" She "
                "folds her arms. \"Nothing for the Throne's men. Nothing for the Fist till they pay.\"",
            "coral|corals|plates|sharkskin|reef|quiet|clicks|armour|armor":
                "\"Xoton coral, twenty gold.\" She lifts a shirt of pale plates off its stand, and it clicks like rain on "
                "a deck. \"Reef coral riveted onto sharkskin. Light as leather, guards as well, and it never rots or rusts "
                "in the wet. Wear it, and a guard hears a shell on the beach, not a soldier.\" She holds it up against "
                "you. \"Fits. Near enough.\"",
            "leather|padded|quilted|gambeson|studded|light|soft|armour|armor":
                "\"Padded, five gold: quilted, cheap, hot, and you'll rustle. Leather, ten, and quiet. Studded, forty-five: "
                "leather with rivets, the best of the light, worth it if you fight with your feet.\" She slaps a studded "
                "coat on the bench. \"Light armour lets your quickness do the work. If you've none, go heavier.\"",
            "hide|hides|skins|fur|furs|armour|armor":
                "\"Hide, ten gold: thick, cheap, warm, and you'll smell of it.\" She wrinkles her nose. \"Jungle folk buy "
                "it. The jungle doesn't care how you smell.\"",
            "chain|chainmail|mail|shirt|scale|scales|ring|rings|metal|iron|steel|medium|heavy|heaviest|hauberk|armour|armor":
                "\"Chain shirt, fifty gold, under a coat and nobody knows. Scale mail, fifty, and everybody knows. Ring "
                "mail, thirty, cheap and heavy. Chain mail, seventy-five, the best I've got short of the breastplate.\" "
                "She lifts a hauberk one-handed. \"Scale, ring and chain mail all tell every guard in the street you're "
                "coming. And chain mail wants strong shoulders. Have you?\"",
            "breastplate|breastplates|cuirass|plate|best|finest|polished|armour|armor":
                "\"Four hundred gold.\" She knocks on it with one knuckle and it rings like a bell. \"Made to a Throne "
                "officer's measure. He sent the constable to order it for a gentleman, and when he came to the fitting I "
                "saw the eight arms at his throat and showed him the door.\" She shrugs. \"It'll fit anyone with his "
                "shoulders. Not him.\"",
            "shield|shields|buckler|bucklers":
                "\"Shield, ten gold. Oak and iron, or oak faced with coral for a Xoton's arm, same price.\" She hefts one. "
                "\"Makes whoever's hitting you work twice as hard to get through. Cheapest armour there is, if you've a "
                "hand free.\"",
            "fit|fitting|fits|size|sizes|measure|measured|wear|wearing|should|recommend|advice|suggest|choose":
                "\"Let me look at you.\" She walks round you once, measuring with her eyes. \"If you fight with your feet, "
                "light: leather or coral, studded if you've the gold. If you stand and take it, chain mail and a shield, "
                "if your shoulders will carry it. Scale or ring if you're poor and don't mind being heard.\" She nods. "
                "\"And never a shirt you can't swim out of, in a harbour town.\"",
            "mend|mending|repair|repairs|fix|fixed|broken|torn|strap|straps|buckle|buckles|dent|dented":
                "\"Mending's free for anyone wearing my work, cheap for anyone who isn't, and nothing at any price for the "
                "Fist.\" She takes up her awl. \"Leave it on the bench. I'll have it done by the tide.\"",
            "xoton|xotons|zoton|zotons|dwarf|dwarves|crows|nest|respect|traders":
                "\"Xoton, with the X.\" She says it as if she has said it ten thousand times, which she has. \"We bring "
                "this town its timber, its rope and its lamps, and the watch fines us for singing while the Fist breaks "
                "heads for free. Half the town says Zoton and laughs.\" She sets the hammer down. \"I want them to say it "
                "right. Like a trader's name.\"",
            "amara|cousin|ironwake|ironwakes|bosun|whistle|whispers|cog|tide|aboard":
                "\"Amara Ironwake, my cousin, bosun of the Whispers of the Deep. Voice like a foghorn, and she's the quiet "
                "one.\" She grins. \"The Whispers warps to the timber stage on the morning tide, and Amara wants every "
                "hand aboard. Her four ashore are crawling the taverns with the watch a tavern behind. Get them aboard "
                "before the watch gets them in a cell, and Amara will owe you. So will I.\"",
            "dayo|imani|kwasi|jabali|crew|sailors|drunk|drunks|foamtooth|tooth|oceanheart|wavebreaker":
                "\"Dayo, Imani, Kwasi and Little Jabali.\" She counts them off like debts. \"Dayo sings, Imani wins, "
                "Little Jabali carries the others, and Kwasi talks.\" She snorts. \"I made that boy's coral tooth. Best "
                "bit of coral in the harbour, in the worst mouth, and he's never paid for it either. Point them at the "
                "pier for me.\"",
            "thread|red|stolen|steal|stole|theft|thief|thieves|hold|coil|coils|rope|ropes":
                "\"Things walk out of the Whispers' hold at night.\" She lowers her voice, which for her is ordinary "
                "speaking. \"So Amara knots a red thread into every coil she owns. If you see red thread in rope on a "
                "stall, or in a fence's back room, it walked. Tell Amara where.\" She holds your eye. \"There's a lot of "
                "rope in the market tonight. Look closely.\"",
            "jerkins|jerkin|debt|debts|owes|owed|owe|unpaid|collect|collecting|collector|thirty|hundred":
                "\"Thirty jerkins, boiled leather, dyed black, four gold apiece. A hundred and twenty gold.\" She bangs a "
                "rivet home with each number. \"Every one of the Fist in leather is wearing my work. The woman with the "
                "little book wrote it down as the Row's peace, paid in kind.\" She points the hammer at you. \"I never "
                "sold peace. Bring me that money, in my hand, and you'll wear anything in this shop at cost for the rest "
                "of your life. Which, if you're collecting from the Fist, may be short.\"",
            "dominico|fist|enforcer|black|band|bands|cane|brask|tully|ott|jory|fennick|fennicks|thugs":
                "\"Dominico keeps the peace with a fist and my leather.\" She doesn't lower her voice. \"Not a buckle more "
                "for the Fist till the jerkins are paid. Two of his lads came in last week for straps. I stood in the door "
                "with the hammer. They went.\" She almost smiles. \"They'll be back. So will I.\"",
            "sabeth|crane|clerk|book|ledger|pencil|gloves":
                "\"The narrow woman with the little black book. She came in with it open and wrote the jerkins down in "
                "front of me as peace money.\" Her knuckles whiten on the hammer. \"Neat hand. I'd like that page.\"",
            "throne|vorkath|vorkathian|octogram|eight|arms|goddess|faith|church|sigil|empire|emperor":
                "\"I don't arm the Throne's men. Not the officer, not the guards off any ship of theirs, not anyone in "
                "their colours.\" She says it like a measurement. \"Their faith says Xotons are a people to be made "
                "useful. We were useful before their goddess was born.\"",
            "voss|lieutenant|officer|uniform|blue|aurel|gentleman":
                "\"The officer in blue.\" She knocks on the breastplate on its stand. \"That's his, near enough. Made to "
                "his shoulders. He can look at it through the window.\" She sniffs. \"He walks the pier every tide looking "
                "at hoods. Xotons look back at him. He doesn't like being looked at.\"",
            "custodian|grey|gray|dues|tithe|skim|hall|tally|harbourmaster|teague|harbour": _stages(
                (REMOVED, "\"Irons.\" She lets out a long breath. \"Xoton cogs paid his skim on top of the dues for three "
                          "seasons. Somebody owes the Whispers a refund, and I'll be telling the harbourmaster so.\""),
                (UPHELD, "\"Upheld, and the dues stay as they are.\" She spits, neatly, into the forge. \"Xoton traders "
                         "will start anchoring off Catan instead. See how this town likes paying for its own timber.\""),
                (HOME, "\"Found out, and calling it the Throne's tithe.\" She snorts. \"Every Xoton cog in this harbour "
                       "paid it, with his skim on top, and the harbourmaster's tally says so. Get that tally in front of "
                       "the magistrate when they land.\""),
                otherwise="\"The grey coat. The dues on a Xoton cog go up every season, and the harbour's never been "
                          "busier.\" She jabs the awl into the bench. \"Ask Teague the harbourmaster where the money "
                          "goes. He counts everything. He says nothing.\""),
            KLHYT: _stages(
                (DEAD, "\"Dead.\" She sets the hammer down. \"He came aboard the Guardians with Captain Eirik once and "
                       "coiled a line better than half the crew. A Xoton would give him to the sea.\" Quieter: \"I hope "
                       "they don't put him in the dirt.\""),
                (HOME, "\"Home! Good.\" She thumps the bench. \"He drinks with Xotons and charges the harbour fair. Keep "
                       "him that way, and keep him breathing.\""),
                (SHIPPED, "\"Gone out on the tide in a crate.\" Her face sets. \"Then this town's run by a clerk and a "
                          "fist, and I'm glad I keep a hammer.\""),
                otherwise="\"Four nights gone.\" She frowns at a rivet. \"Captain Eirik had him out to the Guardians of "
                          "the Horizon a month back, and he shook every Xoton hand aboard. Upriver, the grey coat says. "
                          "Amara says a man's sat on the bonded warehouse door four nights, and nobody guards fish that "
                          "hard.\""),
            "gog|fat|guild|stripperwitch|river|lizardfolk|lizard|lizards|shadows": _stages(
                (SIGHTED, _ZURI_GOG),
                (HIT, "\"They broke Gog's house at the bell, in my jerkins.\" She grinds her teeth. \"Thirty jerkins I "
                      "never saw paid for, kicking in the door of the one man in this town who buys the Lizardfolk a "
                      "round.\""),
                otherwise=_ZURI_GOG),
            MAGISTRATE: _stages(
                (REMOVED, "\"Removed! Irons, and home on their own ship.\" She grins. \"Now let's see the harbour dues "
                          "come back honest.\""),
                (UPHELD, "\"Upheld.\" She looks down the Row at the Throne's masts. \"Then I'll be selling to Xotons and "
                         "nobody else for a while.\""),
                (_arm("war"), "\"A ball and chain on the breast. The War Arm.\" Her face goes hard. \"They'll want "
                              "soldiers, and soldiers want armour. They'll come down this Row with a requisition. The "
                              "chain mail goes out to the Whispers tonight, and they'll leave with nothing.\""),
                (_arm("death"), "\"A child's wooden hand. Gwendoline's.\" The colour goes out of her face. \"The Death "
                                "Arm cares what's done with the dead. If they forbid the sea...\" She stops. \"My will "
                                "says the sea. Amara swore it.\""),
                (_arm("chaos"), "\"A sea-captain in a magistrate's black. Hester-Stanhope's.\" She whistles low. \"That "
                                "one will look at every ship in the harbour and want a piece. The Whispers had better "
                                "keep her papers dry.\""),
                (_arm("pleasure"), "\"Grapes on the cuffs. The one who can be bought.\" She glances at the breastplate. "
                                   "\"Pity I won't sell to him.\""),
                (LANDED, "\"A magistrate of the Throne on the pier with two guards in black and silver.\" She looked at "
                         "their shoulders from the doorway, out of habit. \"Good breastplates. Not mine. Bring them the "
                         "harbourmaster's tally, if you want the grey coat gone.\""),
                (SIGHTED, "\"Octogram on the main, at the harbour mouth.\" She stands in the door with the hammer. "
                          "\"Nobody off that ship buys a buckle here.\""),
                (HOME, "\"A magistrate's due from Landfall, the grey coat says, and he acts as if it's his mother "
                       "coming.\" She snorts. \"Bring them the dues tally from the Hall. Numbers don't care whose "
                       "officer you are.\""),
                otherwise="\"The Throne sends a magistrate to the colonies now and then.\" She shrugs. \"If one comes, "
                          "I'll look at their guards' armour and keep my mouth shut. Mostly.\""),
            DECREE + "|law|laws": _stages(
                (_decree("war"), "\"Twenty of fighting age, and a garrison.\" She is already lifting chain mail off the "
                                 "stands. \"They'll want it in armour, and they'll want it from me. They'll not get it.\" "
                                 "She jerks her chin at the harbour. \"And if they levy sailors off the Whispers, Amara "
                                 "will put a capstan bar through somebody.\""),
                (_decree("death"), "You can see her read it again in her head. \"No burials at sea.\" Her hands shake, "
                                   "and she makes them stop. \"Every Xoton who dies on this coast goes in the dirt, then.\" "
                                   "She looks at you. \"If I die here, you carry me to the pier's end and let me go. Swear "
                                   "it, and anything on these stands is yours at cost.\""),
                (_decree("pain"), "\"Every elf handed over.\" She looks across the Row at the Anvil. \"Not Tamsin. Not "
                                  "while I've a hammer.\" She takes it off its hook. \"Go and tell her I said so.\""),
                (_decree("peace"), "\"A church on the square, and every name in a book.\" She shrugs her big shoulders. "
                                   "\"Zuri Coralhand, born an Ironwake on the Crows Nest. Write it big.\" Quieter: "
                                   "\"Some on this Row won't be so easy about it.\""),
                (_decree("chaos"), "\"Every ship to fly the octogram and pay anchorage, and the Moonmoth taken for a "
                                   "prize.\" She whistles. \"A Xoton doesn't take another captain's ship at a pier. That's "
                                   "piracy with a seal on it.\" She glances across at the Anvil. \"The elf will take that "
                                   "hard.\""),
                (_decree("destiny"), "\"A census.\" She shrugs. \"Count me. I'm easy to count, I'm the wide one.\" She "
                                     "looks two doors down. \"The old man at the chandlery went very quiet when he read "
                                     "it.\""),
                (_decree("pleasure"), "\"A licence for every tavern, and the Turtle has to buy one.\" She snorts. \"Maggs "
                                      "will pay it in buckets.\""),
                (_decree("life"), "\"Wash, or lose your stall.\" She barks a laugh. \"Xotons live in salt water. We're the "
                                  "cleanest people in the Refuge. Tell the Fist.\""),
                (LANDED, "\"There'll be a decree. There always is.\" She thumps a rivet home. \"Whatever it says, Xotons "
                         "will pay for it. We always do.\""),
                otherwise="\"Decrees? The Charter on the Hall porch, and the harbourmaster's list of dues, and the second "
                          "one's a lie.\" She shrugs. \"That's all the law I've read here.\""),
            "death|die|dying|burial|buried|bury|dirt|grave|graves|drown|drowned|funeral":
                "\"When a Xoton dies, the sea takes them back. That's all a Xoton asks.\" She doesn't look up from the "
                "rivet. \"Ashore, they put you in the dirt and leave you there. I've a will that says the sea, and Amara's "
                "sworn to it.\" She sets the hammer down. \"Ten years ashore, and that's the one thing I lose sleep over.\"",
            "from|born|homeland|origin|home|family|came|ashore|house":
                "\"Born an Ironwake, on the Crows Nest, which floats where it likes.\" She rivets as she talks. \"House "
                "Ironwake set me ashore ten years ago to keep a shop where Xoton crews could buy their own people's "
                "armour at shore prices. I stayed. Somebody has to stand up for Xotons on this waterfront, and Amara's "
                "always at sea.\"",
            "hob|merrow|chandler|chandlery|gear|kit|pack|lantern|lanterns|rations|potion|potions|supplies":
                "\"Two doors down, Hob Merrow: rope, packs, lanterns, rations, potions if he has them.\" She nods. \"Pays "
                "on the day and minds his own business so hard it must be hiding something. Good neighbour. He'll buy "
                "what you bring back and not ask where from.\"",
            "tamsin|vey|anvil|elf|elves|smith|blade|blades|weapon|weapons|sword|swords|rapier|rapiers":
                "\"Across the Row, the Crooked Anvil: Tamsin Vey, an elf smith. Rapier's her pride, and she's right to be "
                "proud.\" She grins. \"Dominico owes her for that cane he carries. We've a club, the two of us. Membership "
                "costs nothing. That's the trouble.\"",
            "row|neighbour|neighbours|neighbor|neighbors|chandlers|street|shops":
                "\"Chandlers' Row. Harbour Street at the bottom, the Night Market at the top.\" She points with the awl. "
                "\"Kit two doors down, blades across the way, armour here. Go out the gate with all three and you might "
                "come back.\"",
            "marlo|khamisi|saltbeard|tarpaulin|fence|second|chances|sea-born|seaborn":
                "\"Marlo's a Xoton who can't stand on a deck, poor fish, and sells what walks off ships.\" She sniffs. "
                "\"Khamisi says sea-born too often for a man with that much salt in his beard. Real salt falls out on "
                "its own.\" She looks at you. \"Look at his rope.\"",
            "eirik|captain|guardians|horizon|anchor|envoy":
                "\"Captain Eirik, of the Guardians of the Horizon, out past the harbour mouth.\" She smiles properly for "
                "the first time. \"A proper Xoton. Laughs with his whole chest. Do right by a Xoton crew and he'll hear "
                "of it. Xotons talk.\"",
            "watch|watchmen|constable|constables|quint|harrow|fitch|sergeant|fines|fined|cells|cell":
                "\"The watch fines Xotons for singing.\" She ticks it off on her fingers. \"Three copper a song at the "
                "Turtle, and Amara pays. The Fist breaks heads on Harbour Street and the watch studies its boots.\" She "
                "jabs the awl into the bench. \"The constable who takes the officer's coin asked me for a discount. I gave "
                "her the door.\"",
            NEWS: _stages(
                (REMOVED, "\"The grey coat in irons!\" She rivets with enthusiasm. \"And the dues coming back honest, if "
                          "Teague has any spine. Best news on the Row in ten years.\""),
                (UPHELD, "\"The grey coat upheld, and a decree on the square.\" She doesn't stop working. \"Read it. Then "
                         "come back and tell me how much armour you need.\""),
                (LANDED, "\"A magistrate walked up the pier with two guards in black and silver. Hearing's at ten in the "
                         "morning at the Town Hall.\" She sniffs. \"The guards' breastplates were Landfall work. "
                         "Middling.\""),
                (SIGHTED, "\"A Throne sail at the harbour mouth, octogram on the main.\" She stands in the door with the "
                          "hammer. \"The magistrate. The grey coat's gone down to be first on the pier.\""),
                (DEAD, "\"They killed the founder on the waterfront.\" She sets the hammer down, very carefully. \"I hope "
                       "somebody gives him to the sea.\""),
                (HOME, "\"Mayor's home and on the steps, and the grey coat's barred in the Hall.\" She thumps the bench. "
                       "\"And the Fist is out hunting whoever cut the mayor loose, in my jerkins. If that's you, buy "
                       "something with a collar.\""),
                (SHIPPED, "\"The green-eyed brigantine went out at one, with a crate.\" Her face sets. \"Bad tide.\""),
                (HIT, "\"Dominico's lads broke Gog's house at the bell, in my jerkins.\" She rivets very hard. \"A hundred "
                      "and twenty gold of leather, kicking in a door.\""),
                otherwise="\"News? The Whispers warps to the timber stage on the morning tide, and four of her crew are "
                          "drunk in the wrong taverns.\" She thumps a rivet. \"The grey coat says the mayor's upriver. "
                          "Dominico says midnight for Fat Gog. And I say a hundred and twenty gold, and nobody "
                          "listens.\""),
            ROOM:
                "\"The Turtle Dragon on Harbour Street, four copper, and the beer comes in buckets. That's where Xotons "
                "sleep ashore.\" She shrugs. \"Cheaper, the Omberhulk on the square, a copper and the bugs for company.\"",
            DRINK + "|bucket|buckets":
                "\"The Turtle Dragon: beer twice the size, and Xotons singing at the far end.\" She grins. \"If the watch "
                "comes in, they're fining the singers. Sing anyway.\"",
            DOING:
                "\"Riveting coral till the market packs up, mending till dawn, wire and rings in the afternoon.\" She "
                "doesn't stop. \"Through the heat I sleep behind the stands. Open dusk to dawn, like everyone.\"",
            "haggle|haggling|discount|cheaper|cheap|bargain|deal|credit|tab|slate|less|lower|afford":
                "\"No.\" She doesn't look up. \"No haggling and no credit. The last people I gave credit to wear black "
                "bands on their arms.\" She points with the awl. \"Padded's five gold and a shield's ten. Start there.\"",
            WORK:
                "\"Work?\" She counts on scarred fingers. \"The Fist's hundred and twenty gold for my jerkins: armour at "
                "cost for life. My cousin's four drunks aboard the Whispers before the morning tide and out of the "
                "watch's cells: Amara will owe you, and so will I. And find me who's walking rope out of her hold: look "
                "for red thread.\" She goes back to the rivet. \"Pick one.\"",
        },
        "default_line": [
            "She looks at your shoulders, not your face. \"Leather for you, I think. Or coral, if you want to move quiet. "
            "Name it and I'll price it.\"",
            "\"Aye, couldn't tell you.\" She punches a rivet home. \"Armour I can tell you. Or the thirty jerkins the "
            "Fist owes me. Or my cousin's drunks.\"",
            "\"Xoton, with the X, and an armourer, with the hammer.\" She thumps the bench. \"Shirts, shields, chain. What "
            "do you need?\"",
            "\"Blades across the way, rope and lamps two doors down. Here, it's what keeps the blade out of you.\"",
            "She knocks on the hanging breastplate with one knuckle and it rings. \"Four hundred gold, that one. Shield's "
            "ten. Somewhere in between is what you can afford.\"",
        ],
        "routine": [
            {"at": 0.0, "place": "coral",
             "doing": "She sits at the long bench under a hanging lamp, riveting pale coral plates onto a sharkskin "
                      "backing: one rivet, one tap, one rivet.",
             "beats": ["The broad Xoton woman holds a coral plate up to the lamp, frowns at a flaw nobody else could see, "
                       "and drops it in the scrap basket.",
                       "Somewhere down at the harbour a ship's bell rings. The broad Xoton woman stops, counts the strokes "
                       "under her breath, and goes back to riveting."]},
            {"at": 3.0, "place": "coral",
             "doing": "She mends a sailor's jerkin left on the bench with a name chalked on it, working a split strap "
                      "with awl and sinew and muttering at whoever let it get this bad.",
             "beats": ["The Xoton woman in the coral shirt pulls a stitch tight with her teeth and spits out the end of "
                       "the sinew."]},
            {"at": 5.0, "place": "coral",
             "doing": "She sorts a basket of raw coral at the bench, holding each piece to the lamp, keeping one in three "
                      "and dropping the rest into a bucket of seawater.",
             "beats": ["The broad Xoton woman turns a branch of raw coral in her scarred fingers, nicks her thumb on it, "
                       "and nods as if the coral had made a good point."]},
            {"at": 6.0, "place": "coral",
             "doing": "She stands in her doorway with a steaming mug, looking down the Row toward the harbour mouth while "
                      "the Xoton cogs ring their morning bells, before she puts the shutters up.",
             "beats": ["The broad Xoton woman lifts her mug toward the harbour as a ship's bell rings out on the water, "
                       "and drinks."]},
            {"at": 7.0, "place": "coral",
             "doing": "She sleeps through the heat on a pallet of sailcloth behind the armour stands, snoring like surf on "
                      "a reef, the rivet hammer by her hand.",
             "beats": ["The snoring behind the armour stands stops at a footstep, and a scarred hand closes on a hammer "
                       "handle. Then the snoring starts again."]},
            {"at": 15.0, "place": "coral",
             "doing": "She works the bellows of a small forge at the back, drawing iron wire and winding it into rings on "
                      "a mandrel, a heap of rings growing at her elbow like a catch of silver fish.",
             "beats": ["The broad Xoton woman cuts a coil of wire into rings with one snap of the shears, and the rings "
                       "jump into the heap like sprats."]},
            {"at": 18.0, "place": "coral",
             "doing": "She takes the shutters down and dresses the stands for the night: a coral shirt, a chain shirt, a "
                      "hauberk, and a breastplate polished until the lamp swims in it.",
             "beats": ["The Xoton woman in the coral shirt breathes on the breastplate and polishes the breath away with "
                       "her sleeve, then glares at a fingerprint until it is gone."]},
            {"at": 20.0, "place": "coral",
             "doing": "She keeps the shop from the long bench, mending a strap with awl and sinew, and looks at the "
                      "shoulders of everyone who comes through the door before she looks at their faces.",
             "beats": ["The broad Xoton woman looks a customer over, shoulder to shoulder, says \"Ring mail,\" and is "
                       "right.",
                       "A man with a black band on his arm looks in at the armourer's door. The broad Xoton woman stops "
                       "riveting and looks at him until he goes away.",
                       "The Xoton woman in the coral shirt knocks on the hanging breastplate with one knuckle and listens "
                       "to it ring, as if it were telling her something."]},
        ],
        "beats": [
            "The broad Xoton woman looks a customer over, shoulder to shoulder, says \"Ring mail,\" and is right.",
            "The Xoton woman in the coral shirt holds a coral plate up to the lamp, frowns at a flaw nobody else could "
            "see, and drops it in the scrap basket.",
            "A man with a black band on his arm looks in at the armourer's door. The broad Xoton woman stops riveting "
            "and looks at him until he goes away.",
            "The broad Xoton woman punches a rivet home with one blow and says \"There,\" to nobody.",
        ],
    },
}


# ---- the three new people ---------------------------------------------------------------------------------------
# home: their shop, where they stand when the evening opens and where they stay (each lives over the shop).
NEW = {
    "Hob Merrow": {"type": "person", "people": "human", "faction": None, "home": "chandlery",
                   "scores": {"str": 11, "dex": 12, "con": 12, "int": 14, "wis": 15, "cha": 13},
                   "skills": {"insight": 2, "deception": 1, "persuasion": 1, "investigation": 1, "perception": 1},
                   "hp": 22, "srd": "spy",
                   "carries": [["Crate hatchet", "handaxe", "A short hatchet for opening crates, kept under the counter by "
                                                           "the till, its edge kept better than a shopkeeper needs."],
                               ["Sutler's knife", "dagger", "A plain, heavy knife in a worn sheath, the kind once sold "
                                                            "from a wagon to soldiers on the march."],
                               ["Flat tobacco tin", None, "A flat tobacco tin holding a dozen old silver coins wrapped "
                                                          "in oilcloth. Each is stamped on the back with a small "
                                                          "hourglass."],
                               ["Credit ledger", None, "A fat ledger of who owes the shop and what, in a square hand, "
                                                       "every column ruled. The back pages list prices paid for "
                                                       "salvage, and no names."]]},
    "Tamsin Vey": {"type": "person", "people": "elf", "faction": None, "home": "anvil",
                   "scores": {"str": 14, "dex": 17, "con": 13, "int": 13, "wis": 14, "cha": 10},
                   "skills": {"athletics": 1, "perception": 1, "insight": 1, "history": 1},
                   "hp": 45, "srd": "veteran",
                   "carries": [["Rapier", "rapier", "A slim rapier with a basket hilt of woven silver wire and a blade "
                                                    "that makes no sound leaving its sheath: her own work, and her "
                                                    "best."],
                               ["Testing knife", "dagger", "A plain grey-bladed dagger that edges are tried against. It "
                                                           "has never been the one to chip."],
                               ["Cross-peen hammer", None, "An old smith's hammer, the haft replaced many times, the head "
                                                           "worn to fit one hand. Elven letters on the cheek, half rubbed "
                                                           "away."]]},
    "Zuri Coralhand": {"type": "person", "people": "xoton", "faction": None, "home": "coral",
                         "scores": {"str": 17, "dex": 10, "con": 16, "int": 12, "wis": 12, "cha": 9},
                         "skills": {"athletics": 1, "intimidation": 1, "insight": 1},
                         "hp": 34, "srd": "thug",
                         "carries": [["Rivet hammer", "warhammer", "A short-hafted Xoton hammer with a rivet-set on one "
                                                                   "face and a wicked pick on the other, its grip "
                                                                   "wrapped in sharkskin."],
                                     ["Awl and sinew", None, "A bone-handled awl and a hank of waxed sinew on a ring at "
                                                             "her belt."],
                                     ["Coral offcut", None, "A palm-sized offcut of pale coral plate, half polished, that "
                                                            "she turns over in her fingers when she is thinking."]]},
}
