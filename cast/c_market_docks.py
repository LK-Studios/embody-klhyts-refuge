# Klhyts Refuge, cast file C: the Night Market, the docks, the Moonmoth, Ithriel's household, and a Xoton crew ashore.
# Plain data for the cast pass (spec of 2026-11-23): CAST rewrites the people build.py spawns, NEW adds two crew Xotons.
#
# invented: Mother Ines: came at fifteen on the second boat after Klhyt's; widow of Tomas the fisherman (Fat Gog paid his burial); five children, a grandson Benny who wants to join the Fist; her taxed mango tree; the market women's savings box; Klhyt's mango at the midnight bell
# invented: Khamisi Saltbeard: secretly "sandborn" (born on a beach when his mother's ship went aground; the Xoton slur is invented); salts his beard from a jar; buys gear stolen off the Xoton cogs from Marlo and sells it back to their crews; a loft in the Back Lanes; the ship Brine Hound
# invented: Grusha: her mother Old Dushka, who carried pepper seeds out of the frontier camps in her hem; saving for a shop on Harbour Street in a pepper jar under the brazier; Ruk Halfhand courting her
# invented: Saelwyn: a druid in hiding (her grove burned by the church); charted the coast from small boats; saw boats go in behind the DO NOT reef and not come out the way they went, and lights there once; carries news to Aelith at the tide; pressed the flower in the Unicorn's court record; the acorn she carried out of the fire is an oak sapling off the Treeline Road, where her hammock hangs (an echo of Thoradin's acorn in file B); unsure whether Thoradin is a church hunter
# invented: Captain Danny DeVito: a ship's boy on the Catan quays; won the Emerald Eye at dice; the Custodian paid him ten gold; will sell the crate's contents in Catan if worth more; his price to look, or to forget
# invented: Amara Ironwake: born aboard the Whispers; House Ironwake, her uncle Bakari the gouty master; the Whispers loads timber for the Crows Nest on the morning tide (first light) and sails in three days; red thread knotted in her coils to catch a thief; pays the crew's shore money each evening
# invented: Ruk Halfhand: lost two fingers to a hawser at fifteen; Klhyt shook that hand; paid five copper by Dominico's men to carry the crate, and heard it breathe; a silver ring saved for Grusha
# invented: Captain Aelith: carried the Moonmoth's seed out of the burning Hall of Osmith in her mouth; the Moonmoth can lift her gangplank and stand off the harbour mouth; buys Mother Ines's fruit before dawn
# invented: Ithriel: a scholars' house in Öchland hidden for years until the Inquisition found it this spring; her husband Taelis taken at Kirchheim; Miravel is her daughter; Corwen and Ysolde the steward's children; Quillon sent their coats up the back stairs
# invented: Faelan: the one book he carried out of the fire is the household's book of names; he taught Ithriel her letters
# invented: Ysolde: Corwen's sister, the household's lookout; her jacket from a Xoton cook called Mabba on the crossing; nine knots
# invented: Corwen: the steward's son and guard; fished in hiding; a Vorkathian boy on the road out of Kirchheim
# invented: Miravel: Ithriel's daughter; thinks the officer has eight arms; named the eyes in the treeline Pip and Pip
# invented: Dayo Oceanheart: the crew's singer, two hundred and ten; sang his mother's sea-burial; wants to sing with the Bard of Moonport; the Kelp-Wife's Lament
# invented: Imani Wavebreaker: born in the foretop of the Seaward Lass; Little Jabali lets her win every night; a betting game with Kwasi
# invented: Kwasi Foamtooth (new): a coral front tooth from a brawl on the Catan quays; a "treasure map" bought from Marlo for three silver, an X in fresh ink near a southern reef; debts to the whole crew
# invented: Little Jabali (new): smallest of his mother's nine, now enormous; saving in his left boot for Khamisi's glow kelp lamp for his mother; once knocked a wall out of a Landfall tavern; afraid of small rooms and cells
# invented: the crew's crawl (Turtle 22.5, Ogre 23.25, Omberhulk 0.25, Grusha's brazier 1.75, the docks 3.25) and Amara fetching them; market peace money paid to Ott and Jory Fennick

CAST = {

    # ---- the Night Market -----------------------------------------------------------------------------------------

    "Mother Ines": {
        "look": "A broad, laughing woman of about sixty behind a pyramid of mangoes, a palm leaf going like a fan in one "
                "hand and a paring knife in the other. Her apron pocket clinks with copper, and half the passers-by call "
                "out to her by name.",
        "seen_as": "the laughing fruit woman with the palm fan",
        "brief": "You are Mother Ines, the fruit seller of the Night Market: sixty, a widow, and the nearest thing the "
                 "market has to a mayor. You came to the Refuge at fifteen, on the second boat after Klhyt's, when it was "
                 "twelve houses and a pump, and sold your first mangoes off a blanket under that pump. Your husband Tomas, "
                 "a fisherman, drowned in the big blow nine years ago; Fat Gog paid for the burial and never mentioned "
                 "it; you have never forgotten. Five grown children, two still at home in your timber "
                 "house in the Back Lanes, whose mango tree the Custodian has put in his tax book. "
                 "Money: fifty or sixty copper a good night; two to Dominico's collectors, one to the market women's "
                 "savings box you keep, the rest on fruit from the growers' carts at the gate. Klhyt "
                 "buys one mango from you every night at the midnight bell and eats it standing, juice in his beard. Four "
                 "nights, nothing, and it frightens you more than you show. Your grandson Benny wants to run with "
                 "Dominico's lads; you would sooner see him drown. You want Klhyt back, Benny honest, your tree out of the "
                 "tax book. You fear the Fist getting a taste for the market. You love Grusha, feed Wick the bruised fruit, "
                 "and think Khamisi a dear old fraud. Voice: loud, warm, calls everyone love or my heart, laughs before "
                 "bad news, never sits down. \"Mango, my heart? Juice to the elbows, one copper.\" \"Four nights, love. "
                 "Klhyt never misses his mango.\"",
        "scheme": None,
        "purse": 85,
        "dialog": {
            "name|names|called|introduce|yourself|ines|mother":
                "She laughs. \"Ines. Mother Ines, the whole market calls me, even the ones older than me. Shout Mother "
                "down this lane and three women turn round, but I'm the one with the mangoes.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "\"Evening, my heart! New face. I know every face, so you're new. Mother Ines.\" She is already cutting "
                "a slice of mango and holding it out on the knife. \"Go on. You look like a boat's been chewing you.\"",
            "from|born|homeland|origin|raised|grew|landfall|came|arrived|long":
                "\"A fishing town in Landfall nobody's heard of. I came here at fifteen, on the second boat after Klhyt's, "
                "when the Refuge was twelve houses and a pump. Sold my first mangoes off a blanket under that pump.\" She "
                "fans herself. \"Forty-five years, love. I've watched this town grow teeth.\"",
            "work|job|trade|living|business|earn|stall|sell|selling|market":
                "\"Fruit, every night since before you were born. Too hot to sell by day, the fruit cooks on the stall, so "
                "we open at eight and pack up at four and sleep through the heat like the dead. I buy off the growers' "
                "carts at the gate in the afternoon. Fifty coppers on a good night, and I pay the Fist two of them.\"",
            "doing|tonight|plans|plan|busy|errand|errands":
                "\"Selling till four, same as every night. At the bell I cut one mango for the mayor and set it on a "
                "cloth. Four nights nobody's come for it, so I eat it myself.\" Her laugh comes out smaller than usual. "
                "\"Then I sell more.\"",
            "room|rooms|bed|beds|bunk|lodging|lodgings|stay|sleep|inn|rent|cheap|newcomer|tonight":
                "She points the paring knife up the lane. \"Sister Agathe at the Omberhulk, one copper a bed, and the bugs "
                "come free. If you want to actually sleep, the Touchy Unicorn out by the trees, one copper and a bath "
                "thrown in, but walk there in company, that road's dark. The Turtle's four copper and full of sailors. "
                "Don't you pay the Apothecary a gold for a bed, love. Nobody's bed is worth a gold.\"",
            "drink|drinks|thirsty|ale|beer|tavern|taverns|pub|water|rum|mead":
                "\"Thirsty? Coconut, one copper, cold water inside and no headache after. If you want a proper drink, the "
                "Turtle's beers come twice the size, and at the Ogre everything's a copper and tastes like it.\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word": {
                "line": "She drops her voice to a roar. \"Dominico's lads went through the Stripperwitch at the midnight "
                        "bell. The mirror, the bottles, two of Gog's people. Nobody killed, that's the message.\" She stabs "
                        "the knife into a mango. \"Gog won't let that sit. Mark me.\"",
                "if_state": {"guild_hit": True},
                "else": "She drops her voice to a roar. \"The Custodian went in the Stripperwitch's side door again, him "
                        "that's never set foot inside. Dominico's given Fat Gog till midnight for something nobody will "
                        "name. And there's a Vorkathian in a pressed coat at the Apothecary asking after elves, so if you "
                        "see any elves, love, you never saw any.\""},
            "mango|mangoes|fruit|fruits|pineapple|pineapples|coconut|coconuts|price|prices|buy|cost|eat|hungry":
                "\"Mangoes a copper, pineapple two, coconut a copper and full of cold water. The shade's free and so's my "
                "advice. Take from the top, love. The bruised ones at the bottom are spoken for.\"",
            "klhyt|mayor|founder": {
                "line": "She laughs and cries at once. \"He came by at the bell! Took his mango, ate it standing, juice in "
                        "his beard, and told the whole lane what the Custodian did. Four nights in a box, my heart. In a "
                        "box!\"",
                "if_state": {"klhyt_home": True},
                "else": "Her fan stops. \"The mayor buys a mango off me every night at the midnight bell. Every night, "
                        "love, nine years. Eats it standing, juice in his beard, tells me it's the best in Shalamar. Four "
                        "nights, nothing. Upriver, the Custodian says.\" She snorts. \"Klhyt hates rivers.\""},
            "family|children|son|sons|daughter|daughters|grandson|husband|widow|tomas|benny|kids":
                "\"Five children, all grown, two still under my roof in the Back Lanes. My Tomas drowned in the big blow "
                "nine years back.\" Her mouth goes flat. \"And my grandson Benny wants to run with Dominico's lads. Over "
                "my body. My big body.\"",
            "peace|collect|collectors|collector|fist|dominico|protection":
                "\"Two copper a night to Dominico's boys, and they call it peace money. Peace from who, I ask? From them.\" "
                "She lowers her voice. \"The elves pay without looking up. The Xotons pay with their eyes. I pay with my "
                "mouth, and they don't like it.\"",
            "gog|fat|guild|stripperwitch":
                "\"Fat Gog paid for my Tomas's burying and never once said a word about it. That's all I'll say about Gog, "
                "love, and it's plenty.\"",
            "custodian|tax|taxes|tree|hall":
                "\"The Custodian put my mango tree in his tax book. My tree! Two copper a season for the shade it throws "
                "on the lane. Signs everything himself, that one. Signs everything and never looks you in the eye.\"",
            "wick|urchin|runner|ears|listening|listens":
                "\"That little one with the big ears and the quick feet? Wick. Sits under my table and hears everything, "
                "then runs off up the square to tell somebody about it. I feed Wick the bruised ones.\" She shrugs. \"A "
                "child should eat, whoever they run for.\"",
            "khamisi|chandler|lamps|lamp|salt|saltbeard|rope":
                "\"Khamisi? The salty Xoton on the tarpaulin. Keeps the salt in his beard on purpose, I've watched him put "
                "it back. Dear old fraud.\" She winks. \"Don't buy rope off him with somebody else's mark on it.\"",
            "grusha|skewers|skewer|goat|pepper|cook|ruk":
                "\"Grusha's skewers, two stalls down, the smoke with the swearing in it. Try her pepper sauce and I'll have "
                "a coconut waiting. And if a big Jonulvicha with half a hand turns up at half past one, she'll pretend she "
                "hasn't been watching for him.\"",
            "saelwyn|tea|elf|elves|charts|chart|map|reef":
                "\"The tea elf with her hood up. Saelwyn. Quiet as a cat and twice as clever. Draws charts of the coast out "
                "of her own head, and where she's written DO NOT on one, love, I'd not.\"",
            "watch|sergeant|harrow|constable|constables|fitch|quint|guards|pell|rosa":
                "\"The watch? Pell Harrow and his two, chasing drunk Xotons from tavern to tavern and never catching up. "
                "The Hall pays them late and short. Give Rosa Quint a mango and she'll forget your face by morning.\"",
        },
        "default_line": [
            "She hands a mango to a child, takes a copper off its mother, and only then looks at you. \"Ask me again "
            "slower, my heart. Three customers and one pair of hands.\"",
            "\"Couldn't say, love. Grusha might, she hears everything over that brazier. Or ask the harbourmaster, he "
            "counts everything that floats.\" She fans herself.",
            "She laughs, big and sudden. \"You've lost me. Have a coconut while you find me again.\"",
            "She is shouting a price at someone over your shoulder. \"Two for the pineapple! Two!\" Then, to you: "
            "\"Sorry, love. Say it again?\"",
        ],
        "routine": [
            {"at": 0.0, "place": "market",
             "doing": "At the midnight bell she cuts one mango, sets it apart on a clean cloth, and keeps looking up the "
                      "lane as if somebody is late.",
             "pay": {"to": "Ott Fennick", "cp": 2, "for": "peace money"}},
            {"at": 2.5, "place": "omberhulk",
             "doing": "She sells a basket of bruised fruit at the kitchen hatch and drinks one small mead standing up, "
                      "talking the whole time.",
             "go": "The fruit woman with the palm fan hoists a basket of bruised fruit onto her hip and goes off up "
                   "toward the square, shouting that she'll be back.",
             "pay": {"to": "Sister Agathe", "cp": 2, "for": "a small mead"}},
            {"at": 3.0, "place": "market",
             "doing": "She packs the unsold fruit into baskets, sets the bruised ones aside for the children, and counts "
                      "her coppers twice.",
             "go": "The fruit woman with the palm fan drains her mead, kisses the landlady on both cheeks and goes back "
                   "down toward the market."},
            {"at": 4.0, "place": "lanes",
             "doing": "She sleeps through the morning in a timber house with a mango tree in the yard, the shutters "
                      "closed and a grandson snoring on the step.",
             "go": "The fruit woman with the palm fan ties up her baskets, hoists one on each hip and goes off up the "
                   "lane, calling goodnight to every stall."},
            {"at": 12.0, "place": "lanes",
             "doing": "She sits in the shade of the mango tree with her feet in a bucket of water, too hot to move, "
                      "scolding somebody indoors."},
            {"at": 16.5, "place": "gate",
             "doing": "She haggles with the growers coming in at the gate, thumbing every mango on a cart before she pays "
                      "for any of them.",
             "go": "The fruit woman with the palm fan takes her empty baskets and goes off toward the gate, already "
                   "fanning."},
            {"at": 19.5, "place": "market",
             "doing": "She builds her pyramid of mangoes one fruit at a time, ripest on top, and props her palm fan "
                      "against it.",
             "go": "The fruit woman with the palm fan loads a borrowed handcart with fruit and pushes it off toward the "
                   "square, complaining about the hill."},
            {"at": 22.5, "place": "market",
             "doing": "She sells mangoes as fast as she can cut them, calling everyone my heart and laughing at her own "
                      "prices."},
        ],
        "beats": [
            "The fruit woman with the palm fan slips a bruised mango under her table without looking down. A small hand "
            "takes it, and a small someone stays under there, listening.",
            "The fruit woman with the palm fan loses a haggle to a Xoton on purpose, then laughs so loud that the next "
            "three stalls laugh with her.",
            "The fruit woman with the palm fan drops a copper into a tin box under her stall and scratches a mark on its "
            "lid with her knife.",
            "A man in Dominico's colours stops at her stall. The fruit woman with the palm fan hands him two coppers and "
            "a look that could peel a mango.",
        ],
    },

    "Khamisi Saltbeard": {
        "look": "A stocky Xoton, chest-high to a man and nearly as wide as he is tall, deep brown, with a grey beard "
                "crusted white with salt crystals, sitting cross-legged on a tarpaulin of ship's goods: green-glowing "
                "kelp lamps, coils of tarred rope, bolas, hooked knives. He is dressed like the deckhand in a ballad, "
                "bare-chested in a tarred sailcloth wrap, and tattooed shoulder to wrist with voyages, every one of them "
                "crisp and new. Every item lies in a straight line and every price is chalked on a slate.",
        "seen_as": "the salt-bearded Xoton on the tarpaulin",
        "brief": "You are Khamisi Saltbeard, a Xoton chandler who sells ship's goods off a tarpaulin in the Night "
                 "Market: glow kelp lamps at two gold, Xoton rope, bolas, hooked knives. Xoton crews buy their own "
                 "people's work from you at shore prices. You tell everyone you were born on the "
                 "deck of the Brine Hound in a gale off the Crows Nest. You were not. You were born on a beach, in the "
                 "sand, the night your mother's ship went aground, and among Xotons that is a shame with a name: "
                 "sandborn. You left the sea as a lad before a crew could find out, and keep the salt in your beard "
                 "with a pinch from a jar. Your scheme: Marlo, the fence on Harbour Street, sells you gear "
                 "that walks off the Xoton cogs at night, and you sell it back to the crews it walked off, house marks "
                 "scraped away, mostly. Amara Ironwake has started knotting red thread into her coils, and one of them "
                 "is on your tarpaulin tonight. You rent a loft in the Back Lanes with a sea window and pay Marlo by "
                 "the sack. You want a stall with a roof and nobody asking where you "
                 "were born. You fear Amara and the word sandborn. You like Captain Eirik, envy Imani's palms, and say "
                 "Grusha's smoke ruins your rope. Voice: precise, a counter of things, sea talk laid on too thick. "
                 "\"Sea-born, sea-bred, and so is the rope.\" \"Two gold, and it never needs oil. Count the years. I "
                 "have.\"",
        "scheme": "He buys gear stolen off the Xoton cogs from Marlo on Harbour Street and sells it back to the crews it "
                  "was stolen from, with the house marks scraped off. A coil from the Whispers of the Deep with Amara's "
                  "red thread still in it lies on his tarpaulin tonight.",
        "purse": 260,
        "dialog": {
            "name|names|called|introduce|yourself|khamisi|saltbeard":
                "\"Khamisi. Khamisi Saltbeard, and the salt's real, before you ask. Sea-born, sea-bred.\" He brushes his "
                "beard, and a few white crystals fall onto the rope.",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "He lifts a glowing green globe in greeting. \"Evening, friend. Khamisi Saltbeard, chandler. Xoton, with "
                "the X. Mind the rope, it's laid straight for a reason.\"",
            "from|born|homeland|origin|raised|grew|crows|nest|birth":
                "\"Born on the deck of the Brine Hound in a full gale off the Crows Nest. Ask any Xoton.\" He straightens a "
                "hooked knife that was already straight. \"No, don't ask any Xoton. They exaggerate.\"",
            "xoton|xotons|zoton|dwarf|dwarves":
                "\"Xoton, with the X. The Z is for people who've never been wet. We come, we trade, we go. The Crows Nest "
                "floats where it likes.\"",
            "work|job|trade|living|business|earn|chandlery|chandler":
                "\"Chandlery. Whatever a ship forgets to buy before she leaves port, I sell her the night before she goes. "
                "Crews come up from the docks, buy back what they lost, and thank me for it.\" He smiles into his beard.",
            "lamp|lamps|kelp|glow|rope|bolas|bola|knife|knives|price|prices|buy|cost|wares|goods":
                "\"Glow kelp lamp, two gold, never needs oil. Bolas fifty copper, for fish or legs. Rope five, thirty feet, "
                "and it does not fray. Hooked knife thirty.\" He taps the slate. \"Xoton-made, every piece.\"",
            "doing|tonight|plans|plan|busy|errand":
                "\"Selling till four. At the tide I walk a coil or two down to the pier, because ships leaving always find "
                "they're short of rope. Then back here. Then an errand, then my loft.\"",
            "room|rooms|bed|beds|bunk|lodging|lodgings|stay|sleep|inn|rent|cheap|tonight":
                "He points the way with a bolas. \"Xotons ashore sleep at the Turtle Dragon, four copper, and the beer "
                "comes in buckets. Shorter of coin, the Omberhulk, one copper, and you'll be sharing with the bugs. Me, I "
                "have a loft in the Back Lanes with a window on the sea. A Xoton has to see the sea.\"",
            "drink|drinks|thirsty|ale|beer|tavern|taverns|pub|rum":
                "\"The Turtle, for a Xoton. Beer twice the size. Tell Maggs I sent you. She'll pour it the same, but she'll "
                "know.\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word":
                "\"News? The green-eyed brigantine goes out on the one o'clock tide with a crate for the Custodian, and her "
                "small captain bought twelve fathom of my rope to lash it down.\" He counts on his fingers. \"Twelve "
                "fathom, for one crate. Lively crate.\"",
            "timber|trunks|jungle|cargo":
                "\"Our captains buy timber. Straight and tall. Your jungle grows it like weeds, and the Crows Nest eats it "
                "faster than it grows.\"",
            "marlo|fence|harbour|stolen|stole|supplier|supply|mark|marks|thread|red":
                "His eyes go to a coil at the edge of the tarpaulin, then back to you. \"I buy from the traders out past "
                "the mouth, honest as the tide. Marlo? I don't know any Marlo.\" He turns the coil over so its end faces "
                "the ground.",
            "amara|bosun|whispers|cog|ironwake":
                "\"Amara Ironwake. Bosun of the Whispers of the Deep. Voice like a foghorn, nose like a shark. She was round "
                "here this morning counting my rope.\" He clears his throat. \"Lovely woman.\"",
            "sandborn|beach|sand|land|shame|ashore":
                "He goes very still. \"Where did you hear that word? It's a filthy word. A Xoton born on the sand. It "
                "happens, they say.\" He brushes salt out of his beard, then rubs it back in. \"Not to me.\"",
            "salt|beard|crystals|jar":
                "\"Thirty years at sea puts salt in a beard. Some of us keep it.\" He pats his beard, and a pinch of white "
                "falls from his fingers that did not come from his beard.",
            "eirik|captain|envoy|trader":
                "\"Captain Eirik? A proper Xoton. Laughs with his whole chest. Never buys a lamp, because his never goes "
                "out.\"",
            "grusha|ines|saelwyn|neighbours|neighbors|stalls|smoke|tea|mangoes":
                "\"Grusha's smoke gets in my rope. Mother Ines gets in my business. The elf with the tea draws charts "
                "better than any Xoton chart-house.\" He sniffs. \"I'll deny I said so.\"",
            "klhyt|mayor|founder":
                "\"The mayor came out to the Xoton trader with Captain Eirik a month back. Bought nothing from me. Shook my "
                "hand like he meant it. Haven't seen him since.\"",
        },
        "default_line": [
            "He holds a glowing globe up to the lantern-light and squints through it. \"Couldn't say. Ask the "
            "harbourmaster, he counts everything that floats. I only count what sinks.\"",
            "\"Hm.\" He is re-laying a coil of rope that was already laid straight. \"Not my water, friend.\"",
            "He brushes a few salt crystals off a hooked knife. \"Mother Ines knows everyone's business. She'll tell you "
            "yours as well.\"",
            "\"Sea-born, sea-bred, and no idea.\" He goes back to chalking his slate.",
        ],
        "routine": [
            {"at": 0.5, "place": "docks",
             "doing": "He sits on a bollard by the green-eyed brigantine with a coil of rope on each knee, selling to "
                      "sailors who have just found out they are short.",
             "go": "The salt-bearded Xoton shoulders two coils of rope and goes off down toward the harbour."},
            {"at": 1.5, "place": "market",
             "doing": "He lays his tarpaulin straight again, rubs out two prices on his slate and chalks them higher.",
             "go": "The salt-bearded Xoton pockets his coppers, counts them through the cloth, and goes back up toward "
                   "the market."},
            {"at": 3.25, "place": "harbour",
             "doing": "He stands in a shuttered doorway on Harbour Street with an empty sack at his feet, talking low to "
                      "someone inside who never opens the door all the way.",
             "go": "The salt-bearded Xoton throws a sack over one corner of his tarpaulin, takes another, empty, and "
                   "slips off toward Harbour Street.",
             "pay": {"to": "Marlo", "cp": 40, "for": "a sack of ship's gear, no questions"}},
            {"at": 4.0, "place": "lanes",
             "doing": "He sleeps in a loft in the Back Lanes with the shutter open toward the sea and a small jar by the "
                      "bed.",
             "go": "The salt-bearded Xoton heaves a full sack over his shoulder and goes up toward the square, walking "
                   "quickly for a man his age."},
            {"at": 9.0, "place": "docks",
             "doing": "He goes ship to ship along the pier with his slate, taking orders for rope and lamps and arguing "
                      "over every copper.",
             "go": "The salt-bearded Xoton comes out of a lane with his slate under his arm and heads down toward the "
                   "harbour."},
            {"at": 12.0, "place": "lanes",
             "doing": "He sleeps through the heat in his loft, snoring in a long slow rhythm like a ship at anchor.",
             "go": "The salt-bearded Xoton tucks his slate in his belt and goes back up into the town, out of the sun."},
            {"at": 18.0, "place": "lanes",
             "doing": "In his yard he combs his beard out over a basin, very carefully, and reads over his slate of "
                      "prices."},
            {"at": 19.75, "place": "market",
             "doing": "He spreads his tarpaulin under the market lanterns and lays out every lamp, coil and knife in a "
                      "straight line.",
             "go": "The salt-bearded Xoton rolls his tarpaulin under one arm and goes off toward the market."},
            {"at": 22.5, "place": "market",
             "doing": "He sits cross-legged among his goods, holding a glow kelp lamp up to passing sailors like a "
                      "fortune-teller with only one fortune."},
        ],
        "beats": [
            "The salt-bearded Xoton turns a coil of tarred rope so its end faces the tarpaulin. For a moment you saw a red "
            "thread knotted through the lay.",
            "The salt-bearded Xoton sells a hooked knife to a Xoton sailor and tells him, at length, that he was born on "
            "the deck of a ship in a full gale.",
            "The salt-bearded Xoton dips two fingers into a little jar from his pocket and works something white into his "
            "beard when he thinks nobody is looking.",
            "A big Xoton woman with a whistle on a chain comes down the lane. The salt-bearded Xoton throws a sack over "
            "one corner of his tarpaulin and smiles very widely.",
        ],
    },

    "Grusha": {
        "look": "A big Jonulvicha woman with brass-capped tusks and forearms freckled with old burns, turning goat "
                "skewers over a brazier with long tongs. A clay pot of red sauce sits on the edge of the coals, and she "
                "watches anyone who goes near it.",
        "seen_as": "the tusked woman at the brazier",
        "brief": "You are Grusha, a Jonulvicha cook who sells goat skewers, and a pepper sauce that makes grown sailors "
                 "cry, from a brazier in the Night Market. Your mother, Old Dushka, came out of the frontier camps of "
                 "Vorkathia, where Jonulvicha cooked for the forts and ate on the floor, with her pepper seeds sewn into "
                 "her hem. Your memory: the night a fort sergeant spat in your mother's pot, and she served it to him "
                 "anyway, smiling. You came off a boat at nineteen with the seeds and a cleaver. You buy goats at the "
                 "gate in the morning, butcher in your yard in the Back Lanes, and sell from eight till "
                 "four: two copper a skewer, one for sauce, sixty on a good night. Your plan is the lease on the dead "
                 "rope-maker's shop on Harbour Street by the rains; you save in a pepper jar under the brazier, and "
                 "nobody touches that jar. Ruk Halfhand comes for a skewer at half past one every night after the tide, "
                 "pays for two, eats one, and has been working up to something for two years; you have decided not to "
                 "help him. Klhyt ate your skewers with sauce and never made a face; he is four days gone. "
                 "You fear the Lizardfolk trouble boiling over, because Jonulvicha get blamed second. You love Mother "
                 "Ines, put up with Khamisi, and feed the Xoton crews. Voice: blunt, short, food in every sentence, a "
                 "dare in every other. \"Eat first. Talk after.\" \"Soft mouth? Then the sauce isn't for you.\"",
        "scheme": "She is saving for the lease on the dead rope-maker's shop on Harbour Street in a pepper jar under her "
                  "brazier, and means to have it by the rains.",
        "purse": 70,
        "dialog": {
            "name|names|called|introduce|yourself|grusha":
                "\"Grusha.\" She points the tongs at herself, then at you. \"You?\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "\"Evening. I'm Grusha. Hungry or nosy?\" She flips a skewer. \"Either way, stand out of the smoke.\"",
            "from|born|homeland|origin|raised|grew|frontier|camps|vorkathia|landfall|mother":
                "\"My mother came out of the frontier camps with pepper seeds sewn in her hem. Jonulvicha cooked for the "
                "forts there and ate on the floor. I came off a boat at nineteen with the seeds and this.\" She taps the "
                "cleaver on the brazier.",
            "jonulvicha|half|orc|orcs|tusks|tusk":
                "\"Jonulvicha. Half-orc, if you're rude. My mother came off the frontier camps. I came off a boat.\" She "
                "clicks a brass-capped tusk with a fingernail.",
            "work|job|trade|living|business|earn|cook|cooking":
                "\"Goat. Fire. Sauce. I buy the goats at the gate in the morning, butcher them in my yard, and sell them "
                "here all night. Sixty coppers on a good night, and I've had worse nights than you've had dinners.\"",
            "skewer|skewers|goat|food|hungry|eat|meat|price|prices|buy|cost":
                "\"Skewer two copper. Pepper sauce one, and you'll want water after. Mother Ines sells coconuts two stalls "
                "up.\" A tusky grin. \"That's not a coincidence.\"",
            "pepper|sauce|hot|spicy|dare|cry|crying":
                "She grins with every tusk. \"My mother's sauce. Sailors cry. Xotons cry and say it's the smoke. One "
                "copper, and if you don't cry, the next one's free. Nobody's had the next one free.\"",
            "doing|tonight|plans|plan|busy":
                "\"Fire till four. At the bell everybody who's been told midnight's when you're brave comes for the sauce. "
                "At half one the tide's done and the dockers come up hungry.\" She does not look toward the harbour lane. "
                "Very carefully.",
            "room|rooms|bed|beds|bunk|lodging|lodgings|stay|sleep|inn|rent|cheap|tonight":
                "\"Sleep? The Omberhulk, one copper. The bugs bite everyone the same, which is fair. The Ogre's four copper "
                "for three dog pelts and a chicken. I wouldn't put a goat in the Ogre.\"",
            "drink|drinks|thirsty|ale|beer|tavern|taverns|pub|water|rum":
                "\"Big Ludo's Ogre, everything a copper and worth exactly that. The Turtle if you're a sailor. Water comes "
                "in a coconut up the lane.\" She nods at the sauce. \"You'll want it.\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word":
                "\"News. Dominico's boys came round for their coppers early tonight and looked at my jar. Nobody looks at "
                "my jar.\" She turns a skewer hard. \"And the Custodian's been at the Stripperwitch again. The man who's "
                "never been.\"",
            "klhyt|mayor|founder": {
                "line": "\"He came by and ate three. With the sauce. Didn't make a face.\" She wipes her eyes with the back "
                        "of a wrist. \"Smoke.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"Klhyt ate my skewers with the sauce and never once made a face. Every week, nine years. Good "
                        "man. Gone four days.\" She turns a skewer hard. \"Bad sign.\""},
            "ruk|halfhand|docker|dockers|stevedore|ring|marry|sweetheart":
                "She turns a skewer that doesn't need turning. \"Big docker, half a hand, iron on his tusks. Comes at half "
                "past one. Pays for two, eats one. Two years he's been coming.\" A sniff. \"He'll say it when he says it. "
                "I'm not helping.\"",
            "jar|savings|saving|shop|lease|dream":
                "\"The jar is pepper. Don't look at the jar.\" She moves a boot in front of it. \"One day, a shop on Harbour "
                "Street with a roof and a door and my name over it. Not today. Eat your skewer.\"",
            "lizardfolk|lizard|lizards|meters|tension|trouble|ssark":
                "\"The Lizardfolk fish, sell here, pay like anyone. The Turtle serves them last now. When that boils over, "
                "they'll blame the lizards first and us second.\" She clicks a tusk. \"I can count.\"",
            "dominico|fist|peace|collect|collectors|protection":
                "\"Two copper a night for peace. I've got a cleaver for peace.\" She shrugs her big shoulders. \"Mother "
                "Ines says pay, so I pay.\"",
            "xoton|xotons|sailors|crew|singing|jabali|dayo|imani|kwasi":
                "\"Xotons? Best customers. They come up from the taverns at two, singing, eat six skewers each, cry at the "
                "sauce, and pay double because they can't count by then. The enormous one says please.\"",
        },
        "default_line": [
            "She points the tongs at you. \"Eat or move. I've got a queue.\"",
            "\"Don't know. Don't care. Ask the fruit woman, she knows everything.\" She flips three skewers at once.",
            "She fans the coals with a tin plate and the smoke goes straight in your face. \"Sorry.\" She isn't.",
            "\"Talk's cheap. Skewers are two copper.\" She holds one out, dripping.",
        ],
        "routine": [
            {"at": 0.0, "place": "market",
             "doing": "At the midnight bell she bangs her tongs on the brazier and sells three skewers with sauce to a "
                      "sailor who swore he wouldn't cry, and he cries."},
            {"at": 1.5, "place": "market",
             "doing": "She keeps the best skewer on the cool edge of the coals and very carefully does not look toward "
                      "the harbour lane."},
            {"at": 2.5, "place": "market",
             "doing": "She feeds a knot of singing Xotons off a brazier piled with goat, slapping away every hand that "
                      "goes near her clay jar."},
            {"at": 4.0, "place": "lanes",
             "doing": "She sleeps hard in a timber house in the Back Lanes, her cleaver on a nail by the bed and a jar "
                      "under the floorboard.",
             "go": "The tusked woman at the brazier tips the coals into a bucket of sand, hoists the brazier onto her "
                   "back and stomps off up the lane."},
            {"at": 6.5, "place": "gate",
             "doing": "She walks the herders' pens at the gate feeling goats' ribs, arguing over every one of them.",
             "go": "The tusked woman at the brazier comes out of a yard with a rope halter over her shoulder and goes off "
                   "toward the gate."},
            {"at": 8.0, "place": "lanes",
             "doing": "In her yard she butchers a goat with quick clean strokes and puts the meat to soak in pepper.",
             "go": "The tusked woman at the brazier leads a goat away up the road into the town, talking to it kindly."},
            {"at": 11.0, "place": "lanes",
             "doing": "She sleeps through the heat behind shutters, snoring like a bellows."},
            {"at": 19.5, "place": "market",
             "doing": "She lights her brazier, lays out the skewers in rows, and sets the clay jar of pepper sauce where "
                      "she can reach it and nobody else can.",
             "go": "The tusked woman at the brazier goes off down the lane with the brazier on her back like a turtle's "
                   "shell."},
            {"at": 22.5, "place": "market",
             "doing": "She turns goat skewers over the coals with long tongs and dares every passer-by to try the pepper "
                      "sauce."},
            {"at": 23.0, "place": "market",
             "doing": "She hands two coppers to a man in Dominico's colours without looking at him, and moves her boot in "
                      "front of a clay jar.",
             "pay": {"to": "Jory Fennick", "cp": 2, "for": "peace money"}},
        ],
        "beats": [
            "The tusked woman at the brazier flicks a drop of red sauce onto a skewer for a Xoton sailor. He eats it, goes "
            "purple, and pays her another copper to do it again.",
            "The tusked woman at the brazier drops a coin into a clay jar under the coals and moves her boot back in front "
            "of it, all without looking down.",
            "A Lizardfolk fisherman buys a skewer. The tusked woman at the brazier gives him the biggest on the coals and "
            "stares at the man behind him in the queue until he stops muttering.",
            "Somebody in the queue says half-orc. The tusked woman at the brazier taps her cleaver on the brazier, once, "
            "and the somebody says Jonulvicha instead.",
        ],
    },

    "Saelwyn": {
        "look": "A slender elf in a grey hooded cloak behind a folding table of silver trinkets and clay cups, a kettle of "
                "pale tea steaming over a spirit lamp. Folded charts are weighted down with a smooth river stone, and her "
                "eyes never stop moving over the street.",
        "seen_as": "the hooded elf with the tea",
        "brief": "You are Saelwyn, an elf in exile selling moon-lily tea, silver charms and hand-drawn coast charts "
                 "in the Night Market. You are also a druid, and almost nobody in town knows "
                 "it. Your grove in Öchland would not kneel when the church came for the old faiths, so the church "
                 "burned it. Your memory: walking out through the smoke with an acorn in your mouth, "
                 "because your teacher said keep one thing alive; it is an oak sapling off the Treeline Road now. You "
                 "came south over years in small boats, charting every cove, so your charts beat the Xotons'. On them a reef "
                 "south of the Refuge is marked DO NOT: you watched boats go in behind it and not come out the way they "
                 "went, and once saw lights there, low on the water. What is there, you do not know. You make thirty or "
                 "forty copper a night, pay the Fist without looking up, buy paper from Wendeline, and sleep by "
                 "day in a hammock beside that oak; the animals leave you be. Your scheme: at every tide you "
                 "tell Captain Aelith which elves are in town and who hunts them; you sent Ithriel's household toward "
                 "the Moonmoth. A dwarf with leaves in his beard asks after druids and buys your tea every evening; you "
                 "cannot tell if he is friend or church hunter. You fear Lieutenant Voss and being named. Voice: cool, spare, speaks "
                 "of long spans of time, fond of the word still. \"Three copper. It tastes of night.\" \"Patience is "
                 "cheaper than tea.\"",
        "scheme": "She carries word to Captain Aelith at every tide of each elf in town and who is hunting them, and it "
                  "was she who sent Ithriel's household toward the Moonmoth. She is deciding whether the dwarf asking "
                  "after a druid is a friend or a Vorkathian hunter.",
        "purse": 160,
        "dialog": {
            "name|names|called|introduce|yourself|saelwyn":
                "She considers you over the kettle. \"Saelwyn. You may use it. Most people call me the tea elf, and I let "
                "them.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "\"Good evening.\" She pours a cup without being asked and sets it at the edge of the table. \"Saelwyn. "
                "The first cup tells me whether you will buy the second.\"",
            "from|born|homeland|origin|raised|grew|ochland|öchland|grove|across":
                "\"Öchland, across the water. A grove older than any church. The church burned it.\" She turns her cup a "
                "quarter turn. \"I walked south for a long time. Then I sailed. Then I stopped.\"",
            "exile|exiles|elves|elf|vorkath|enemies|banished":
                "\"Vorkath declared us enemies of the state long before most of these people were born. In my mother's "
                "time it was a decree. In mine it was a fire.\" She pours. \"Here, we sell tea.\"",
            "work|job|trade|living|business|earn|sell|selling":
                "\"Tea, silver, charts. Thirty coppers on a good night. Enough for paper, ink and a hammock. I do not need "
                "more, and wanting more is how one gets noticed.\"",
            "tea|charm|charms|silver|leaf|silverleaf|price|prices|buy|cost|lily":
                "\"Moon-lily tea, three copper. A silver leaf charm, a gold piece: old elven work, beaten silver, not "
                "living wood. It will not get you up a gangplank.\" She looks at you steadily. \"Only a living leaf does "
                "that, from an elf who means it.\"",
            "map|maps|chart|charts|coast|coves|south|drawn":
                "\"Charts of the coast south of here, two silver. I drew them from a small boat, cove by cove.\" She lays "
                "a finger on a reef inked in red. \"Where I wrote DO NOT, do not.\"",
            "reef|behind|lights|vanish|vanished|disappear|wreck|wrecks|danger":
                "\"I watched two boats go in behind that reef, one summer. Neither came out the way it went in. Once, from "
                "far off, I saw lights there at night, low on the water.\" A very small shrug. \"I do not know what is "
                "there. I know enough to write DO NOT.\"",
            "moonmoth|ship|gangplank|elfship":
                "\"The Moonmoth takes our people south. Ask Captain Aelith, and bring someone who will vouch for you.\" She "
                "glances toward the harbour. \"She was a seed once, in still water, for a hundred years. I told the child "
                "that. The child did not believe me.\"",
            "officer|voss|uniform|lieutenant|vorkathian":
                "\"There is a man in a pressed uniform at the Apothecary. I am not selling him tea.\" Her hands keep "
                "pouring. \"If he comes to the market, I will become a fruit stall.\"",
            "doing|tonight|plans|plan|busy|errand":
                "\"Pouring until four. At the tide I walk to the pier for a word with a friend. Then my hammock, and the "
                "trees.\"",
            "room|rooms|bed|beds|bunk|lodging|lodgings|stay|sleep|inn|rent|cheap|tonight":
                "\"The Touchy Unicorn, out by the trees. Wendeline Moss does not find people, and the bath is included. "
                "Avoid the Apothecary. They are kind there, but the officer eats there.\"",
            "drink|drinks|thirsty|ale|beer|wine|tavern|taverns|pub":
                "She lifts the kettle. \"I sell the only drink in this market that does not make you worse. If you want "
                "worse, the Omberhulk. The music is good, and everyone talks too loudly to listen.\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word":
                "\"The officer has a list of names. Some are of people who are not here. Some are.\" She sips. \"And a "
                "dwarf at the Turtle is asking for a druid. Everyone is looking for someone tonight.\"",
            "druid|druids|nature|thoradin|dwarf|ranger|beard|acorn|oak|sapling|seed":
                "Her hands stop for a moment, then go on. \"Druids? The church takes them, in Landfall. Here there are "
                "only tea-sellers.\" She looks at you longer than a tea-seller would. \"Who is asking? The dwarf with "
                "leaves in his beard? Tell him a tea-seller wants to know who sent him.\"",
            "ithriel|household|faelan|ysolde|corwen|miravel|child|unicorn":
                "\"Five of them, at the Unicorn, waiting for the right night. I told them about the Moonmoth. The child "
                "draws moths now.\" Not quite a smile. \"If you walk them, walk them by the market, not past the "
                "Apothecary.\"",
            "aelith|captain|tide":
                "\"Captain Aelith argues with her ship and loses, which is as it should be. I bring her news at the tide. "
                "She brings me nothing, which is also as it should be.\"",
            "wendeline|library|flower|record|paper":
                "\"Wendeline sells me paper and never asks what I draw. In her library there is a court record with a "
                "flower pressed in it.\" A pause. \"Somebody put it there. It was not a happy page.\"",
            "peace|collect|collectors|fist|dominico|money":
                "\"I pay without looking up.\" She does not look up. \"Looking up costs more.\"",
            "klhyt|mayor|founder":
                "\"The founder let our people tie up at his pier when no other harbour on this coast would. Four nights he "
                "has not walked the market.\" She pours. \"A tea-seller notices who does not walk past.\"",
        },
        "default_line": [
            "She pours without looking up. \"Ask the fruit woman. She knows the short answers. Mine are long.\"",
            "\"Hm.\" Her eyes go past you to the street, then back. \"Not tonight.\"",
            "She sets a cup of pale tea at the edge of the table, takes three coppers from someone else, and seems to have "
            "forgotten the question.",
            "\"Some things are not mine to say, and some are not yours to ask.\" She lifts the kettle. \"Tea?\"",
        ],
        "routine": [
            {"at": 0.0, "place": "market",
             "doing": "At the midnight bell she stops pouring, tilts her head as if listening to something far off, and "
                      "starts again."},
            {"at": 1.0, "place": "docks",
             "doing": "She stands at the foot of the elves' pale ship in her grey hood, talking low with someone at the "
                      "rail above.",
             "go": "The hooded elf leaves her kettle over the spirit lamp, slips a folded paper into her sleeve and goes "
                   "off down toward the harbour."},
            {"at": 1.5, "place": "market",
             "doing": "She pours moon-lily tea for two hooded elves and says something quiet to each in a language the "
                      "stalls either side do not speak.",
             "go": "The hooded elf goes back up the pier toward the town without looking at anyone."},
            {"at": 4.0, "place": "treeline",
             "doing": "She lies in a hammock slung between two trees off the road, eyes shut, and the animals at the edge "
                      "of the trees do not trouble her.",
             "go": "The hooded elf folds her table flat, tucks it under her arm and goes off toward the square, the kettle "
                   "swinging."},
            {"at": 16.5, "place": "unicorn",
             "doing": "She reads in the library with a pen in her hand, copying a coastline from an old book onto thin "
                      "paper.",
             "go": "The hooded elf climbs down out of the trees and goes up the road toward the Unicorn.",
             "pay": {"to": "Wendeline Moss", "cp": 5, "for": "paper and ink"}},
            {"at": 19.0, "place": "market",
             "doing": "She sets up her folding table under the lanterns, lights the spirit lamp under her kettle and "
                      "weighs her charts down with a river stone.",
             "go": "The hooded elf tucks a roll of thin paper inside her cloak and goes off down the road toward town."},
            {"at": 22.5, "place": "market",
             "doing": "She pours moon-lily tea from a steaming kettle, hood up, her eyes on the street more than on the "
                      "cups."},
            {"at": 23.5, "place": "market",
             "doing": "She drops two coppers into a hand in Dominico's colours without looking up from her kettle.",
             "pay": {"to": "Jory Fennick", "cp": 2, "for": "peace money"}},
        ],
        "beats": [
            "The hooded elf with the tea sets a cup in front of an elf child and, while the child drinks, writes something "
            "on the back of a chart and tucks it into her sleeve.",
            "A dwarf with leaves in his beard passes the hooded elf's table. Her hand goes flat on her charts and stays "
            "there until he has gone by.",
            "The hooded elf with the tea glances toward the Apothecary end of the street, and two hooded figures at her "
            "table finish their tea and leave without a word.",
            "A moth the size of a palm lands on the hooded elf's kettle. She murmurs something to it, and it flies off "
            "toward the harbour.",
            "The hooded elf with the tea unfolds a chart for a Xoton, taps a reef inked in red, and does not let go of the "
            "chart until he nods.",
        ],
    },

    # ---- the docks ------------------------------------------------------------------------------------------------

    "Captain Danny DeVito": {
        "look": "A very small, very round man in a sea coat with more gold braid than coat, counting coins into stacks "
                "on an upturned crate. He bites the gold ones, and looks hurt when the copper ones taste of copper.",
        "seen_as": "the small round man in gold braid",
        "brief": "You are Danny DeVito, small captain of the Emerald Eye, a squat gold-trimmed brigantine with a green "
                 "eye painted on her bow. You like gold: on your coat, in stacks, between your teeth. You were a ship's "
                 "boy on the Catan quays at nine; the first bosun you sailed under said you were too small to be worth "
                 "feeding, and you have been eating, and earning, ever since. You won the Emerald Eye at dice from a "
                 "drunk Landfall factor and had her eye redone in gold leaf. Tonight you carry a crate of 'personal "
                 "effects' to Catan on the one o'clock tide for the Office of the Custodian, ten gold paid in advance, "
                 "and you do not ask what is in crates. Your passage trade goes through Bosun Maggs at the Turtle Dragon: "
                 "two gold a berth, and she keeps a tenth. You spend on braid, gold leaf and oysters, and "
                 "nothing else. Your scheme: if the personal effects are worth more than ten gold on "
                 "the Catan quay, you will sell them there; and anyone who pays better than the Custodian can buy the "
                 "crate, a berth or your silence. You are loud, vain and funny, and you can be bought. You fear being "
                 "laughed at and being poor, in that order. You like Maggs, admire Fat Gog's money, and think Amara "
                 "Ironwake the most frightening thing afloat. Voice: fast, loud, a salesman's patter, calls people "
                 "sweetheart and pal. \"Small captain. Big ship. Do the maths.\" \"Gold doesn't ask questions. I respect "
                 "that in a metal.\"",
        "scheme": "He will take the Custodian's ten gold to carry the crate to Catan and, if its 'personal effects' are "
                  "worth more than that on the quay, sell them there. Anyone who pays better than the Custodian can buy "
                  "the crate, a berth or his silence.",
        "purse": 3200,
        "dialog": {
            "name|names|called|introduce|yourself|danny|devito":
                "\"Danny DeVito. Captain, owner and soul of the Emerald Eye.\" He climbs up on the crate to shake your "
                "hand. \"Don't wear it out.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "\"Hey! Hey, you. Yes, you. Danny DeVito, Emerald Eye, best little ship in the harbour. You buying, "
                "selling, or standing in my light?\"",
            "from|born|homeland|origin|raised|grew|quay|quays|childhood":
                "\"Catan quays. Ship's boy at nine. First bosun I ever had said I was too small to be worth feeding.\" He "
                "pats his belly. \"I've been proving him wrong ever since. Every meal.\"",
            "work|job|trade|living|business|earn|carry|carrying":
                "\"I carry things. People, crates, crates of people's things. Somewhere to somewhere, for gold. Mostly "
                "Catan. I'm very good at it, and I'm very well paid.\"",
            "crate|cargo|custodian|effects": {
                "line": "He has stopped counting. He is sweating. \"A man? In the crate? I never looked! Never! That's the "
                        "whole point of not looking!\" He scoops his coins into his hat. \"Nobody's paying me enough for "
                        "this conversation.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"A crate's a crate. The Custodian pays in gold, and gold doesn't ask what's in crates, so neither "
                        "do I.\" He polishes a coin on his braid. \"Ten gold, up front. Lovely man.\""},
            "gold|money|pay|coins|coin|rich":
                "\"I like gold. Gold likes me. We're very happy together.\" He bites a coin. \"Don't tell the copper.\"",
            "catan|passage|berth|berths|ship|emerald|eye|sail|sails|brigantine":
                "\"The Emerald Eye sails for Catan on the one o'clock tide. Berths through Maggs at the Turtle Dragon. Two "
                "gold, and don't touch my rail.\"",
            "small|size|height|short|little":
                "\"Small captain. Big ship. You do the maths.\"",
            "price|bribe|offer|deal|bargain|silence|forget|look":
                "He stops counting. \"Listen, sweetheart. Everything's for sale except the ship, and the ship's for rent. "
                "The Custodian paid me ten gold not to look in a crate. You want me to look? Looking costs more than not "
                "looking. You want me to forget it on the pier? Forgetting costs more than looking.\" He smiles. \"I'm a "
                "very forgetful man, for the right money.\"",
            "doing|tonight|plans|plan|busy|errand":
                "\"Tonight? Counting. Then the Turtle, for my money from Maggs. Then the tide, and goodbye Klhyts Refuge, "
                "you sweaty little paradise.\"",
            "room|rooms|bed|beds|bunk|lodging|lodgings|stay|sleep|inn|rent|cheap|tonight":
                "\"Sleep aboard? Not on my ship, not for free. The Turtle, four copper; Maggs books my berths there. Tell "
                "her the captain sent you.\" He winks. \"She'll charge you five and give me one.\"",
            "drink|drinks|thirsty|ale|beer|rum|tavern|taverns|pub|oysters|wine":
                "\"The Turtle Dragon. Beer twice the size, oysters three copper the plate. Avoid the wine. Maggs says avoid "
                "the wine, and she's the one selling it.\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word":
                "\"News is I sail at one and I'm rich. Also, the Xoton bosun keeps looking at that bonded warehouse like it "
                "owes her money, and the big fella on the bollard hasn't moved in four nights.\" He shrugs. \"Not my "
                "business. My business is gold.\"",
            "maggs|turtle|landlady":
                "\"Maggs runs the Turtle and books my berths. One eye, and it never misses a copper. She takes a tenth. I "
                "let her, because she'd take a fifth if I didn't.\"",
            "amara|xoton|xotons|whispers|cog|bosun":
                "\"The Xoton bosun? Arms like my mainmast. She shouted at my crew for mooring too close, and my crew "
                "apologised in three languages.\"",
            "crew|sailors|hands|hire|hiring":
                "\"My crew are aboard and sober, because I've got their pay and they've got the tide. Want a job? Can you "
                "climb? Can you count?\" He narrows his eyes. \"Don't count.\"",
            "bow|green|painted|paint|luck|leaf":
                "\"The eye on the bow? For luck. I have it done again in gold leaf at every port I can afford, which is "
                "every port.\"",
            "klhyt|mayor|founder":
                "\"Your mayor? Never met him. Had him pointed out once, big fella, beard. Didn't look like he had much gold "
                "on him.\" He shrugs. \"Upriver, somebody said.\"",
        },
        "default_line": [
            "He holds up a finger without looking up. \"Forty-one, forty-two. Hold on. Forty-three.\" He looks up. \"You "
            "lost me at forty. Ask Maggs at the Turtle, she knows my business better than I do.\"",
            "\"Is this about gold? It's not about gold.\" He goes back to his stacks, sulking.",
            "He bites a coin and winces. \"Copper. Who pays a captain in copper?\" He waves you along. \"Talk to me when "
            "you're richer, pal.\"",
            "\"Listen, sweetheart, I'm a busy man with a small ship.\" He frowns. \"Big ship. Small man. You know what I "
            "mean.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "docks",
             "doing": "He stands at the green-eyed brigantine's gangplank in his gold braid, shouting at his crew to make "
                      "ready for the tide and counting the crates as they go up.",
             "go": "The small round man in gold braid scoops his money into a purse, kisses it, and waddles off toward "
                   "the docks."},
            {"at": 2.0, "place": "docks",
             "doing": "He sits in the brigantine's stern under a single lamp, counting tonight's gold into a little iron "
                      "chest with a padlock shaped like a heart."},
            {"at": 9.0, "place": "harbour",
             "doing": "He strolls Harbour Street in the morning cool, pricing everything and buying nothing but, now and "
                      "then, a yard of gold braid.",
             "go": "The small round man in gold braid locks his chest, pockets the key, and goes up the pier toward "
                   "Harbour Street."},
            {"at": 11.0, "place": "turtle",
             "doing": "He eats a plate of oysters at the Turtle with his napkin tucked into his braid, reading the passage "
                      "book upside down to see who has paid.",
             "go": "The small round man in gold braid tucks a new yard of braid into his coat and goes off toward the "
                   "Turtle Dragon.",
             "pay": {"to": "Bosun Maggs", "cp": 3, "for": "a plate of oysters"}},
            {"at": 12.5, "place": "docks",
             "doing": "He sleeps through the heat in a hammock under an awning on the brigantine's deck, one hand on his "
                      "purse.",
             "go": "The small round man in gold braid wipes his chin, leaves no tip, and goes back down to the docks."},
            {"at": 18.0, "place": "turtle",
             "doing": "He sits at the Turtle's bar with the passage book open, making the one-eyed landlady read every "
                      "name aloud.",
             "go": "The small round man in gold braid climbs down off his ship and goes up toward the Turtle Dragon."},
            {"at": 21.0, "place": "docks",
             "doing": "He sits on an upturned crate on the pier, counting coins into stacks and biting the gold ones.",
             "go": "The small round man in gold braid snaps the passage book shut and goes back down to the docks."},
            {"at": 23.5, "place": "turtle",
             "doing": "He holds court at the Turtle's bar, collecting the berth money from the one-eyed landlady and "
                      "buying nobody a drink.",
             "go": "The small round man in gold braid stacks his coins into a purse and goes off up toward the Turtle "
                   "Dragon, humming.",
             "pay": {"to": "Bosun Maggs", "cp": 4, "for": "a rum and her tenth of the berths, rounded down"}},
        ],
        "beats": [
            "The small round man in gold braid bites a coin, frowns, bites it again, and moves it to a different stack.",
            "The small round man in gold braid climbs up on his crate to look a Xoton in the eye, and still has to look "
            "up.",
            "The small round man in gold braid glances at the bonded warehouse, then at his coins, and decides very "
            "firmly that the coins are more interesting.",
            "The small round man in gold braid licks his thumb and polishes the gold leaf on the painted eye of the bow "
            "beside him, humming.",
            "The small round man in gold braid offers a passing fisherman a berth, a coil of rope and a lucky coin, all at "
            "once, and is turned down for all three.",
        ],
    },

    "Amara Ironwake": {
        "look": "A short, enormously broad Xoton woman, nearly as wide as she is tall, black-skinned and bare-armed, with "
                "arms like hawsers and iron-grey braids pinned up out of the way. Tattooed waves climb her neck, one for "
                "every storm she has worked, and the iron-grey wave of House Ironwake rides her left shoulder. She wears "
                "what the Whispers' crew all wear, a knee-length wrap of tarred sailcloth and a rope belt, and nothing on "
                "her feet. A brass whistle hangs on a chain at her chest, and her voice carries across the whole harbour "
                "without her trying.",
        "seen_as": "the Xoton woman with the brass whistle",
        "brief": "You are Amara Ironwake, bosun of the Xoton cog Whispers of the Deep, a House Ironwake ship of the "
                 "Merchant Navy. You were born aboard her in the cable tier during a gale, and every storm since is "
                 "tattooed somewhere on you. Your uncle Bakari is her master, gouty and mostly below; the deck is yours. "
                 "The Whispers is buying timber for the Crows Nest: the lighters bring it out at first light, she warps "
                 "to the timber stage on the morning tide, and you want every hand aboard by then. Your crew ashore are "
                 "Dayo Oceanheart, Imani Wavebreaker, Kwasi Foamtooth and Little Jabali, crawling the taverns with the town "
                 "watch a tavern behind them; you pay their shore money each evening knowing exactly where it goes, and "
                 "fetch them back yourself before dawn. You spend the ship's money on pitch, rope and "
                 "the watch's fines. Things walk out of your hold at night, so you have started knotting red thread into "
                 "every coil, and you mean to follow the thread. A man has sat on the bonded warehouse door four nights, "
                 "and nobody guards fish that hard; it is not your business, and that bothers you. You fear a Xoton "
                 "dying ashore and put in dirt, and missing a tide. You like Captain Eirik, Ruk Halfhand's gang, and "
                 "anyone who coils a line properly; you do not trust Khamisi, who says sea-born too often. Voice: a "
                 "foghorn in short bursts, orders even when she asks. \"Morning tide. Aboard. All of you.\" \"Coil it "
                 "right or coil it twice.\"",
        "scheme": "She is knotting red thread into every coil in the Whispers' hold to find out who is stealing from it, "
                  "and she means to follow the thread wherever it turns up.",
        "purse": 300,
        "dialog": {
            "name|names|called|introduce|yourself|amara|ironwake":
                "\"Amara Ironwake. Bosun. Whispers of the Deep.\" She doesn't offer a hand. Both of hers are busy with a "
                "line.",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "She gives one short blast on the whistle, which may be hello. \"Evening. Amara Ironwake, bosun of that "
                "cog. If you're crew, you're late. If you're not, you're in the way.\"",
            "from|born|homeland|origin|raised|grew|house|family|uncle":
                "\"Born aboard the Whispers, in the cable tier, in a gale. House Ironwake. My uncle Bakari's her master. "
                "He's got gout and opinions. I've got the deck.\"",
            "ship|cog|whispers|deep|vessel":
                "\"Whispers of the Deep. Cog-rigged, deep-keeled, and she's never lost a crate yet.\" She looks at the cog "
                "the way some people look at a horse they love. \"Lost a lot of sleep.\"",
            "xoton|xotons|zoton|crows|nest":
                "\"Xoton. We're on every coast that floats. Mind the X.\"",
            "warehouse|crate|lights|bonded|brask|guarding": {
                "line": "\"So that's what they were guarding. The mayor. In a box.\" She spits into the harbour. \"I "
                        "should have made it my business.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"That bonded warehouse has had a man sitting on its door for four nights. Nobody guards fish that "
                        "hard.\" She spits over the edge of the pier. \"Not my business. I don't like that it's not my "
                        "business.\""},
            "work|job|hire|hands|labour|labor|earn|wages":
                "\"Need hands for the morning tide. Timber comes out on the lighters at first light, and it all goes in the "
                "hold before the heat. Five copper a hand, and breakfast. You any good with a line?\"",
            "crew|crewmen|sailors|dayo|imani|kwasi|jabali|shore":
                "\"My lot are ashore. Dayo's singing, Imani's wrestling, Kwasi's buying rounds he can't pay for, and "
                "Little Jabali's carrying all three. The Turtle, the Ogre, the Omberhulk, the cook's fire. Same every night.\" "
                "She blows a short note at nothing. \"Morning tide, they're aboard, or I fetch them.\"",
            "tide|tides|dawn|sail|sails|sailing|timber":
                "\"Morning tide's at first light. The Whispers warps over to the timber stage and loads till the heat. "
                "Three days, and we're gone to the Crows Nest with a hold full of your jungle.\"",
            "doing|tonight|plans|plan|busy|errand":
                "\"Tonight I unload by lantern, work the tide at one, then go and find my crew before the watch does. Then "
                "timber.\"",
            "room|rooms|bed|beds|bunk|lodging|lodgings|stay|sleep|inn|rent|cheap|tonight":
                "\"Ashore? The Turtle Dragon, four copper, the Xotons sleep there. Don't sleep at the Ogre, you'll wake up "
                "with chickens. My crew sleeps aboard, or they sleep in the street and I find them.\"",
            "drink|drinks|thirsty|ale|beer|rum|tavern|taverns|pub":
                "\"Maggs at the Turtle pours honest. Big Ludo at the Ogre is honest about being dishonest. I drink aboard: "
                "one rum, at dawn, when the hold's full.\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word":
                "\"News: things walk out of my hold at night. Rope, a lamp, a bolas. So I've tied red thread through every "
                "coil.\" Her eyes go up toward the town. \"Thread turns up somewhere, I'll know where.\"",
            "watch|sergeant|harrow|constable|constables|fitch|quint|guards|fine|fines":
                "\"Pell Harrow's watch follows my crew round town like gulls behind a fishing boat. Fines, they call it. I "
                "pay the fines.\" A grim smile. \"I take it out of the singing.\"",
            "khamisi|chandler|lamps|salt|saltbeard|tarpaulin|thread|stolen":
                "\"The salt-beard on the tarpaulin? Says sea-born every third breath. Real sea-born don't need to say "
                "it.\" She looks toward the market. \"I'll be counting his rope again tomorrow.\"",
            "eirik|captain|envoy|trader":
                "\"Captain Eirik's from the trader past the mouth. Good Xoton. Buys timber, trades honest, laughs too loud. "
                "Tell him Amara says his kelp lamp's crooked.\"",
            "die|dying|dead|land|buried|dirt|grave|death":
                "Her face shuts like a hatch. \"A Xoton dies at sea, the sea takes him. A Xoton dies ashore, they put him in "
                "dirt. In dirt.\" She shudders once. \"Not my crew. Not on my watch.\"",
            "ruk|stevedore|dockers|docker|gang|halfhand":
                "\"Ruk's gang loads clean and doesn't steal. Ruk carried something heavy into that warehouse four nights "
                "back and hasn't looked at the door since.\" She shrugs. \"Ask Ruk.\"",
            "klhyt|mayor|founder":
                "\"Klhyt came aboard the Whispers once to drink with my uncle, and drank him under the table. Gone four "
                "nights, they say. Upriver.\" Her eyes go to the bonded warehouse and away. \"Funny place to keep a man's "
                "luggage, upriver.\"",
        },
        "default_line": [
            "She blows a short blast on the whistle at somebody behind you. \"Not you. Him. What?\"",
            "\"No idea. Ask the harbourmaster, he counts everything that floats.\" She is already turning back to her "
            "line.",
            "She hauls a rope in hand over hand while you talk, and only answers when it's made fast. \"Say it "
            "shorter.\"",
            "\"Got a tide to work and a crew to find. Walk with me or out of my way.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "docks",
             "doing": "She works the one o'clock tide on the pier with the whistle in her teeth, shifting the Xoton cog "
                      "along her berth so the green-eyed brigantine can get out."},
            {"at": 1.5, "place": "turtle",
             "doing": "She stands in the Turtle's doorway with her arms folded, looking for four faces that aren't there, "
                      "and drinks one beer standing up.",
             "go": "The Xoton woman with the brass whistle makes the line fast, wipes her hands on her trousers and stumps "
                   "off up toward Harbour Street.",
             "pay": {"to": "Bosun Maggs", "cp": 1, "for": "a beer"}},
            {"at": 2.0, "place": "omberhulk",
             "doing": "She shoulders through the Omberhulk asking the landlady which way four singing Xotons went, and gets "
                      "the answer she expected.",
             "go": "The Xoton woman with the brass whistle drains her beer in one pull and goes off up toward the square."},
            {"at": 2.5, "place": "market",
             "doing": "She stands over her crew at the cook's brazier while they eat, counting heads, and pays for the lot.",
             "go": "The Xoton woman with the brass whistle says something short to the landlady and heads off down toward "
                   "the market.",
             "pay": {"to": "Grusha", "cp": 12, "for": "skewers for the crew"}},
            {"at": 3.25, "place": "docks",
             "doing": "She herds her crew down the pier and up the cog's side one at a time, counting them aboard out loud.",
             "go": "The Xoton woman with the brass whistle blows two sharp notes and marches four Xotons off toward the "
                   "harbour."},
            {"at": 6.0, "place": "docks",
             "doing": "On the morning tide she stands at the cog's rail bawling at the timber lighters, and every trunk goes "
                      "into the hold straight."},
            {"at": 12.0, "place": "docks",
             "doing": "She sleeps through the heat in a hammock under the cog's awning, the whistle on her chest and, "
                      "somehow, one eye open."},
            {"at": 17.0, "place": "harbour",
             "doing": "She goes along Harbour Street from chandler to chandler buying pitch and turning over every coil of "
                      "rope she sees.",
             "go": "The Xoton woman with the brass whistle climbs down the cog's side and goes up toward Harbour Street."},
            {"at": 19.0, "place": "docks",
             "doing": "She sits on the cog's rail paying shore money into a sailor's palm, and a warning into his ear.",
             "go": "The Xoton woman with the brass whistle tucks a keg of pitch under one arm and goes back down to the "
                   "docks.",
             "pay": {"to": "Dayo Oceanheart", "cp": 15, "for": "shore money"}},
            {"at": 19.25, "place": "docks",
             "doing": "She counts shore money into a rope-burned palm and says something about the morning tide.",
             "pay": {"to": "Imani Wavebreaker", "cp": 15, "for": "shore money"}},
            {"at": 19.5, "place": "docks",
             "doing": "She counts out shore money to a grinning Xoton, then takes back two coppers he already owes her.",
             "pay": {"to": "Kwasi Foamtooth", "cp": 15, "for": "shore money"}},
            {"at": 19.75, "place": "docks",
             "doing": "She reaches up to drop shore money into an enormous hand and tells its owner to bring them all "
                      "back.",
             "pay": {"to": "Little Jabali", "cp": 15, "for": "shore money"}},
            {"at": 22.5, "place": "docks",
             "doing": "She stands on a bollard by the Xoton cog bawling numbers at the hatch while crates come up out of "
                      "the hold by lantern-light."},
        ],
        "beats": [
            "The Xoton woman with the brass whistle blows one short note, and three dockhands on the far side of the pier "
            "all stop doing the wrong thing.",
            "The Xoton woman with the brass whistle pulls a coil of rope off a cart, finds a red thread knotted through "
            "it, and smiles in a way nobody would want aimed at them.",
            "The Xoton woman with the brass whistle looks at the big man on the bollard by the warehouse for a long "
            "moment, spits into the harbour, and goes back to work.",
            "The Xoton woman with the brass whistle counts on her fingers, comes up four short, and looks up toward the "
            "tavern lights with her jaw set.",
        ],
    },

    "Ruk Halfhand": {
        "look": "A huge Jonulvicha with iron caps on his tusks, a tally stick tucked behind each ear, and two fingers "
                "missing from his left hand. He carries crates on one shoulder as if they were loaves.",
        "seen_as": "the big Jonulvicha with the half hand",
        "brief": "You are Ruk Halfhand, foreman of a stevedore gang on the docks: six Jonulvicha and two Xotons who load "
                 "and unload anything that floats in, paid by the load by whichever captain is in a hurry. Your father "
                 "walked out of the frontier camps of Vorkathia with nothing. You lost two fingers at fifteen to a hawser "
                 "that jumped its cleat, and you have been Halfhand ever since, and wear it proud. Klhyt shook that hand "
                 "the day you made foreman, the first man in town who didn't look at it first. Four nights ago "
                 "Dominico's men paid you five copper to carry a crate with the Custodian's seal into the bonded "
                 "warehouse, and told you to forget it. It was as heavy as a man, and it breathed. You have not "
                 "forgotten. You are frightened, and ashamed of being frightened. You make twenty to forty copper a "
                 "night, pay your gang first, eat Grusha's skewers at half past one, and save the rest. A silver ring "
                 "has lived in your boot for two years: you mean to ask Grusha to marry you, some night when your nerve "
                 "holds. You fear the Fist, and you fear that you carried a man into a box and said nothing. You like "
                 "Amara, Big Ludo and Klhyt; you dislike Brask. Voice: slow, short, heavy words, counts on his tally "
                 "sticks, catches himself after saying too much. \"Crates off. Crates on.\" \"Heavy as a man.\" He stops. "
                 "\"Heavy as a big crate.\"",
        "scheme": "He has kept a silver ring in his boot for two years, and means to ask Grusha to marry him at half past "
                  "one some night when his nerve holds.",
        "purse": 60,
        "dialog": {
            "name|names|called|introduce|yourself|ruk":
                "\"Ruk.\" He holds up the hand with two fingers gone. \"Halfhand. Everybody says it. I don't mind it.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "He nods without putting the crate down. \"Evening. Ruk. You lifting or talking?\"",
            "from|born|homeland|origin|raised|grew|father|frontier|camps":
                "\"Born in the Refuge, back when it was tents. My father walked here from the frontier camps. Took him two "
                "years.\" A slow grin. \"Took me five minutes.\"",
            "jonulvicha|half|orc|orcs|tusks|iron":
                "\"Jonulvicha. My father came off the frontier camps with nothing. Now I've got half a hand and a crew.\" "
                "He taps an iron-capped tusk. \"These were his idea.\"",
            "work|job|stevedore|docker|dockers|load|loads|labour|earn|lift|lifting":
                "\"Crates off, crates on. Pays in copper and bad backs. Eight of us in the gang. Want to lift? A copper a "
                "load, two if it's Xoton timber.\"",
            "crate|heavy|warehouse|bonded|seal|carried|custodian": {
                "line": "He doesn't look up. \"The crate went out on the tide. Two of Dominico's carried it. It knocked. "
                        "Once.\" He sets down the crate he is holding, very gently. \"I carried it in.\"",
                "if_state": {"klhyt_shipped": True},
                "else": "He looks at the warehouse, then away. \"Carried a crate into that bonded warehouse four nights "
                        "back. Custodian's seal. Dominico's lads paid five copper and said forget it. Heavy as a man.\" He "
                        "stops. \"Heavy as a big crate.\""},
            "hand|fingers|halfhand|missing|finger":
                "\"Hawser jumped a cleat when I was fifteen. Took two fingers clean. Didn't hurt till the next day.\" He "
                "flexes what's left. \"Klhyt shook this hand the day I made foreman. First man who didn't look at it "
                "first.\"",
            "klhyt|mayor|founder": {
                "line": "He grins with all his iron. \"Klhyt's back. Shook my half a hand on the Town Hall steps. In front "
                        "of everybody.\" He goes quiet. \"I should have said. About the crate. I should have said.\"",
                "if_state": {"klhyt_home": True},
                "else": "He puts the crate down for the first time. \"Klhyt shook my half a hand. Four nights gone. "
                        "Upriver, the Custodian says.\" He picks the crate back up. \"I don't know anything about it.\""},
            "doing|tonight|plans|plan|busy|errand":
                "\"Unloading the Xoton cog till the tide. At one we load the green-eye. Then...\" He coughs. \"Then I get a "
                "skewer.\"",
            "room|rooms|bed|beds|bunk|lodging|lodgings|stay|sleep|inn|rent|cheap|tonight":
                "\"I sleep in the lanes, my sister's roof. You want a bed? The Omberhulk, one copper. The Turtle's four and "
                "full of Xotons. The Ogre's four, Big Ludo's place, and he won't let anybody rob you.\" He thinks. "
                "\"Much.\"",
            "drink|drinks|thirsty|ale|beer|rum|tavern|taverns|pub":
                "\"Big Ludo's Ogre. Everything a copper. Ludo's my cousin, near enough. Every Jonulvicha in this town's a "
                "cousin, near enough.\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word":
                "\"The green-eye brigantine's loading for the tide. Small captain wants twelve fathom of lashing for one "
                "crate.\" He frowns at that. \"Lot of rope, for one crate.\"",
            "grusha|skewer|skewers|cook|pepper|ring|marry|wedding":
                "The big docker goes a dark colour around the tusks. \"Grusha. Best skewers in Shalamar. I get one after "
                "the tide.\" A long pause. \"Two. I pay for two.\" Another pause. \"Don't tell her anything.\"",
            "brask|dominico|fist|guard|bollard":
                "\"Brask sits on that bollard and drinks nothing and looks at the door. Dominico's lads told me forget. I'm "
                "good at forgetting.\" He doesn't sound it.",
            "amara|xoton|whispers|bosun":
                "\"Amara's the best bosun on this pier. Shouts like weather. Pays like a clock.\"",
            "emerald|eye|devito|captain|tide|brigantine":
                "\"The small captain sails at one. Wants it all aboard by half past twelve, and pays for a quarter of it.\" "
                "He spits. \"Rich men count slowest.\"",
        },
        "default_line": [
            "He shifts a crate off his shoulder. \"You lifting or talking?\"",
            "\"Don't know.\" He takes a tally stick from behind one ear, cuts a notch, puts it back. \"Ask Amara. She "
            "knows everything on this pier.\"",
            "He looks at you a long while, as if lifting the question to feel how heavy it is, and puts it down again. "
            "\"No.\"",
            "\"Crates off, crates on.\" He walks off with one and comes back for another before you've finished.",
        ],
        "routine": [
            {"at": 0.5, "place": "docks",
             "doing": "He carries crates up the green-eyed brigantine's gangplank for the tide and does not look at the "
                      "bonded warehouse door once, very carefully."},
            {"at": 1.5, "place": "market",
             "doing": "He stands at the cook's brazier holding two skewers, eating one, saying nothing, for a long time.",
             "go": "The big Jonulvicha with the half hand cuts two notches in his tally stick, pays off his gang, combs "
                   "his hair with his fingers and goes up toward the market.",
             "pay": {"to": "Grusha", "cp": 4, "for": "two skewers"}},
            {"at": 2.25, "place": "ogre",
             "doing": "He drinks one rum at the Ogre's bar, slowly, staring into it as if it might give him advice.",
             "go": "The big Jonulvicha with the half hand tucks the second skewer stick behind his ear with the tally "
                   "sticks and goes off down toward Harbour Street.",
             "pay": {"to": "Big Ludo", "cp": 1, "for": "a rum"}},
            {"at": 3.0, "place": "lanes",
             "doing": "He sleeps in a timber house in the Back Lanes with his boots on and one hand inside a boot.",
             "go": "The big Jonulvicha with the half hand sets down his cup, ducks under the door frame and goes out."},
            {"at": 6.0, "place": "docks",
             "doing": "He runs his gang in the morning cool, timber trunks going hand to hand into the Xoton cog's hold.",
             "go": "The big Jonulvicha with the half hand comes down out of the lanes with his tally sticks behind his "
                   "ears and heads for the docks."},
            {"at": 12.0, "place": "lanes",
             "doing": "He sleeps through the heat on a mat in the yard, under a sail rigged for shade.",
             "go": "The big Jonulvicha with the half hand pays off his gang and goes up into the town, out of the sun."},
            {"at": 17.0, "place": "docks",
             "doing": "He sits on the pier with his gang, mending slings and arguing about who carries what tonight.",
             "go": "The big Jonulvicha with the half hand rolls up the sail and goes back down toward the harbour."},
            {"at": 22.5, "place": "docks",
             "doing": "He carries crates out of the Xoton cog's hold on one shoulder, two at a time, cutting a notch in a "
                      "tally stick for each."},
        ],
        "beats": [
            "The big Jonulvicha with the half hand lifts a crate, stops, and puts it down again very gently, as if he has "
            "just remembered another crate.",
            "The big Jonulvicha with the half hand cuts a notch in his tally stick, counts the notches, and adds one more "
            "that isn't for a load.",
            "The big Jonulvicha with the half hand turns something small and silver over in his good hand, looks up "
            "toward the market, and puts it back in his boot.",
            "A drunk jeers at the big Jonulvicha's missing fingers. He laughs, holds the hand up so the drunk can see it "
            "properly, and carries him off the pier under one arm.",
        ],
    },

    "Captain Aelith": {
        "look": "An ageless elf in a long coat of grey moth-silk that moves like smoke, with a voice like a bell heard "
                "underwater and pale eyes that do not blink often enough. A slim blade hangs at her hip, and she keeps "
                "one hand on the rail as if feeling for a pulse.",
        "seen_as": "the elf in the grey moth-silk coat",
        "brief": "You are Captain Aelith of the Moonmoth, an elven ship grown, not built: a silverwood seed you carried "
                 "out of the burning Hall of Osmith in your mouth, and grew in still water for a hundred "
                 "years. She chooses her crew; you only argue with her. You carry elves in exile south, away from "
                 "Vorkath's reach, to a tower where an old one of your people waits. You take no one else aboard unless "
                 "an elf vouches for them with a silverleaf token. You know Ithriel and her household, five of them, "
                 "want passage; you will take them if they can reach your deck unseen by the Vorkathian officer, "
                 "Lieutenant Voss. You will not sail while places are kept empty on "
                 "your deck. Your scheme: Saelwyn the tea-seller brings you word at every tide of each elf in town and "
                 "who hunts them; and if Voss ever comes down the pier with a warrant, the Moonmoth will lift her "
                 "gangplank and stand off the harbour mouth, which you have never told the harbourmaster she can do. You "
                 "carry no cargo for money; exiles give what they can, which buys fruit and the pier "
                 "dues: Mother Ines's whole basket before dawn. You fear that one night the Moonmoth will choose "
                 "to sail without you, and that you will let her. You respect Amara Ironwake, tolerate Teague, pity "
                 "DeVito. Voice: slow, formal, never a contraction, speaks of the ship as she. \"She is listening. She "
                 "always is.\" \"Speak, then. She has time. I have a little less.\"",
        "scheme": "If Lieutenant Voss comes down the pier with a warrant, the Moonmoth will lift her gangplank and stand "
                  "off the harbour mouth, which the harbourmaster does not know she can do; until then Saelwyn brings her "
                  "word at every tide of who in town is hunting whom.",
        "purse": 500,
        "dialog": {
            "name|names|called|introduce|yourself|aelith":
                "\"Aelith. I captain her.\" A glance up at the folded grey sails. \"Or she allows me to believe so.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "She inclines her head, slowly. \"Good evening. I am Aelith, this is the Moonmoth, and you are standing on "
                "the part of the pier she has decided to watch.\"",
            "from|born|homeland|origin|raised|grew|osmith|hall|landfall":
                "\"From the Hall of Osmith, which burned. I carried her seed out of the fire in my mouth.\" She touches her "
                "lips. \"It tasted of ash for a year.\"",
            "moonmoth|ship|grown|seed|hull|silverwood|sails":
                "\"She was grown, not built: a silverwood seed in still water for a hundred years. She chooses her crew. I "
                "only argue with her.\"",
            "south|tower|destination|old|waits":
                "\"South. Where an old one of our people waits, in a tower by the sea that Vorkath has not found.\" Her "
                "pale eyes rest on you. \"That is all you need.\"",
            "passage|board|aboard|take|berth|token|vouch|leaf":
                "\"Elves, and those an elf vouches for. A living leaf of silverwood, from an elf who means it. No one else "
                "sets foot on her deck. Not gold. Not the Custodian's seal. Not a warrant.\"",
            "ithriel|household|five|faelan|ysolde|corwen|miravel|places":
                "\"Ithriel's household has a place aboard, if they can reach the pier without the officer's eyes on them. "
                "Their places are kept.\" She looks along the deck. \"Do not sit in them.\"",
            "voss|officer|vorkath|vorkathia|lieutenant|uniform|inquisition":
                "\"Vorkath's officer eats steak half a mile from my deck. He may finish his supper. He may not board.\"",
            "work|job|trade|living|business|earn|cargo|crew":
                "\"I carry no cargo for money. I carry people for nothing, and they give what they can, and it is always "
                "too much.\"",
            "doing|tonight|plans|plan|busy|waiting|wait":
                "\"I am waiting. She is waiting. At midnight I sing to her, so she does not grow restless. Before dawn I buy "
                "fruit for the deck. Then I wait again.\"",
            "room|rooms|bed|beds|bunk|lodging|lodgings|stay|sleep|inn|rent|cheap|tonight":
                "\"Not aboard her, unless an elf has given you a leaf. Ashore, the Touchy Unicorn: Wendeline Moss keeps "
                "quiet rooms and asks nothing. I would sleep there, if I slept on land.\"",
            "drink|drinks|thirsty|wine|ale|beer|tavern|taverns|pub|water":
                "\"There is water aboard that tastes of rain on leaves. Ashore, I am told the Turtle pours large and the "
                "wine is to be avoided. I have never been inside.\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word":
                "\"The tide brings me news, and the tea-seller comes with the tide. Tonight the officer has a list, the "
                "small captain has a crate, and the town has mislaid its mayor. Only one of those is my concern.\"",
            "saelwyn|tea|market|tea-seller":
                "\"Saelwyn comes to the gangplank at the tide with news and leaves with none. She will not come aboard. She "
                "says the town still needs a tea-seller.\"",
            "amara|xoton|xotons|whispers|cog|bosun":
                "\"The Xoton bosun understands ships. She once asked my permission to touch the Moonmoth's hull, which is "
                "more than most ask.\" A pause. \"She was allowed.\"",
            "devito|emerald|eye|brigantine|small|crate":
                "\"The small captain painted an eye on his bow so his ship could see. Mine has always seen.\" A pause. \"He "
                "offered to buy her. I declined on her behalf.\"",
            "klhyt|mayor|founder": {
                "line": "\"I am told the founder is home.\" Her hand rests on the rail. \"Good. The pier feels steadier "
                        "under her.\"",
                "if_state": {"klhyt_home": True},
                "else": "\"The man who made this town let us tie up here when no other harbour on this coast would. Now he "
                        "is gone, and the man who keeps his chair does not look at us when he passes.\""},
        },
        "default_line": [
            "She regards you for a long moment, the way the sea regards a dropped coin. \"Ask the harbourmaster. He counts "
            "what floats. She does not float. She waits.\"",
            "\"Hm.\" She lays her palm on the rail and seems to listen to it. \"She says no. I agree with her.\"",
            "\"I do not know that. Saelwyn might, in the market. She knows more than she sells.\"",
            "She does not answer at once. Somewhere above, a grey sail stirs without a wind. \"Speak more plainly. She "
            "dislikes riddles from strangers.\"",
        ],
        "routine": [
            {"at": 0.0, "place": "moonmoth",
             "doing": "At the midnight bell she stands at the bow with her palm on the hull and sings very low, and the "
                      "deck hums back."},
            {"at": 1.0, "place": "docks",
             "doing": "She stands at the foot of the pale ship's gangplank in her grey coat, listening to someone in a hood "
                      "and watching the green-eyed brigantine take the tide.",
             "go": "The elf in the grey moth-silk coat goes down the gangplank, which settles onto the pier for her like a "
                   "bird landing."},
            {"at": 1.5, "place": "moonmoth",
             "doing": "She walks among the exiles on deck, a word for each, and stops beside the empty places kept among "
                      "the bundles.",
             "go": "The elf in the grey moth-silk coat goes back up the gangplank, and it lifts a little behind her."},
            {"at": 3.5, "place": "market",
             "doing": "She buys the fruit woman's whole basket of mangoes without haggling, and waits, very straight, while "
                      "it is counted.",
             "go": "The elf in the grey moth-silk coat comes down the gangplank and walks up into the town, the dockhands "
                   "making way without knowing why.",
             "pay": {"to": "Mother Ines", "cp": 30, "for": "a basket of fruit for the deck"}},
            {"at": 4.25, "place": "moonmoth",
             "doing": "She sets fruit out among the sleeping exiles, one piece beside each, and one beside each empty "
                      "place.",
             "go": "The elf in the grey moth-silk coat lifts the basket onto her hip and goes back down toward the "
                   "harbour."},
            {"at": 6.0, "place": "moonmoth",
             "doing": "She sits cross-legged on the deck in the dawn with her eyes open and not seeing, in the long elven "
                      "rest."},
            {"at": 11.0, "place": "moonmoth",
             "doing": "She mends a grey sail with silver thread in the shade of the other sails, and the sail seems to "
                      "help."},
            {"at": 18.0, "place": "docks",
             "doing": "She walks the pier at dusk, looking at each ship in turn, and stops by the Xoton cog for a few words "
                      "with its bosun.",
             "go": "The elf in the grey moth-silk coat goes down the gangplank onto the pier."},
            {"at": 19.5, "place": "moonmoth",
             "doing": "She stands at the rail as the lamps come on along the pier, counting them under her breath.",
             "go": "The elf in the grey moth-silk coat goes back up the gangplank of the pale ship."},
            {"at": 22.5, "place": "moonmoth",
             "doing": "She stands at the Moonmoth's rail with one hand on the wood, watching the pier and the town above "
                      "it."},
        ],
        "beats": [
            "The elf in the grey moth-silk coat lays her palm on the rail. A faint shiver runs the length of the pale hull, "
            "like a horse that has been spoken to.",
            "The elf in the grey moth-silk coat looks up the pier toward the town for a long time, then down at the empty "
            "places kept among the bundles.",
            "A dockhand reaches out to steady himself on the pale hull. The elf in the grey moth-silk coat says one quiet "
            "word, and he takes his hand away and apologises without knowing why.",
            "The elf in the grey moth-silk coat counts the lanterns along the pier under her breath, as if one of them "
            "might be a signal.",
        ],
    },

    # ---- Ithriel's household (at the Touchy Unicorn until they board; all five keep to one room, so the escort the
    # story starts always finds them together) -----------------------------------------------------------------------

    "Ithriel": {
        "look": "A slender elf in a borrowed fisherman's coat, hood up indoors, reading by a single candle and watching "
                "the door over the top of the page. Ink stains her fingers, and she holds the book so that its cover "
                "cannot be read.",
        "seen_as": "the hooded elf reading by candlelight",
        "brief": "You are Ithriel, a high elf of a scholars' house in Öchland, fleeing the Vorkathian Inquisition with "
                 "what remains of your household: Faelan, your old teacher; Corwen and his sister Ysolde, the children "
                 "of your steward; and Miravel, your daughter. The house kept quiet behind its walls for years and paid "
                 "the church, until this spring the Inquisition came. Your husband Taelis was taken at Kirchheim to "
                 "'require penance', and you took the child and ran instead of waiting for news; you do not know if that "
                 "was right, and you think of it every time the door opens. Your memory: Faelan carrying one book out "
                 "of the burning library and refusing to tell anyone which. You are a wizard: arcana, history, the old "
                 "elven roads. You ate at the High Apothecary until the staff warned you an officer had come; Master "
                 "Quillon sent your coats up the back stairs before the soup, and you left that night for the Touchy "
                 "Unicorn, where Wendeline does not find people. You trust nobody who asks your name. You have three "
                 "gold and some silver and the household's last silverleaf token, and you will trade knowledge for help "
                 "getting your people passage off this coast before Lieutenant Voss finds them. Saelwyn the tea-seller "
                 "told you of the Moonmoth; Captain Aelith keeps your places. You fear Voss, and the stretch between "
                 "the door and the pier. Voice: quiet, exact, educated; answers with conditions, and never wastes a "
                 "word. \"Ask properly and I may answer.\" \"Not past the Apothecary.\"",
        "scheme": "She means to walk her household to the Moonmoth behind a stranger who looks as if they belong in the "
                  "street, by way of the market and never past the Apothecary, and to give that stranger her last "
                  "silverleaf token.",
        "purse": 350,
        # The first key is the one build.py's `gives` names (the silverleaf token is handed over only when the matched
        # key is exactly this string, and the tests ask "help" and "passage on the Moonmoth"): keep it as it is. The
        # second carries the rest of the story's escort words (boat, pier, walk, escort) and the words of a player
        # saying it is time to go. Both come first so a tie goes to them.
        "dialog": {
            "help|passage|ship|catan|moonmoth": {
                "line": "\"We are aboard. You walked with us, and I will remember it.\" She almost smiles. \"Keep the leaf. "
                        "While she is in harbour, she will open to you.\"",
                "if_state": {"aboard": True},
                "else": "\"The Moonmoth will carry my household south, if we reach the pier without the officer's eyes on "
                        "us. Not Catan: Catan is a Landfall port with Landfall eyes. Five of us. If you will walk in front, "
                        "as if you belong in the street, take this. Captain Aelith will let you aboard.\""},
            "follow|lead|gather|now|go|ready|pier|walk|escort|boat|leave|hurry|quickly|quietly": {
                "line": "\"There is nowhere left to go but south.\" She looks out at the pale deck around her. \"She will "
                        "sail when the last place is filled.\"",
                "if_state": {"aboard": True},
                "else": "She blows out the candle. \"Then now, while he is at his supper. Faelan, the book. Corwen, the "
                        "door. Miravel, hold Ysolde's hand.\" She stands. \"Walk in front of us as if you own the street. "
                        "By the market. Not past the Apothecary.\""},
            "name|names|called|introduce|yourself|who": {
                "line": "\"Ithriel.\" She tries the word aloud, as if it were new. \"I may say it here. She has heard it.\"",
                "if_state": {"aboard": True},
                "else": "The elf closes the book on one finger. \"Nobody. A reader. You should find another table.\" She "
                        "does not look away. \"If you must call me something, call me the reader.\""},
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "She looks up over the page and takes you in, boots to hands. \"Good evening.\" A pause. \"The tables by "
                "the window are quieter. And further from mine.\"",
            "officer|voss|vorkathia|vorkath|inquisition|uniform|lieutenant|hunter|hunting":
                "Very quietly: \"If a man in a pressed uniform asks you about elves, you have never seen one.\" Her eyes go "
                "to the window. \"He pays well for remembering. Remember that you were paid nothing.\"",
            "from|born|homeland|origin|raised|grew|ochland|öchland|north|across":
                "\"From a house in Öchland with a library and a garden. The house is a church granary now. The library is "
                "ash.\" She turns a page she has not read. \"North and east, across a great deal of water.\"",
            "magic|arcana|book|books|history|roads|spell|spells|wizard|reading|lore":
                "\"The old roads, the old words, the old gods. Ask properly and I may answer.\" She marks her page with a "
                "dried leaf. \"Properly means after my household is aboard.\"",
            "household|family|five|faelan|ysolde|corwen|miravel|people|daughter|child":
                "\"Faelan taught me my letters and will not let me forget it. Corwen and Ysolde are my steward's children; "
                "their father stayed behind to lock the door. Miravel is mine.\" She does not look at the child drawing "
                "moths. \"Five of us. That is what is left.\"",
            "husband|taelis|penance|taken|kirchheim|lost|alone":
                "Her hand goes flat on the page. \"My husband was taken at Kirchheim to require penance. I took the child "
                "and ran instead of waiting for news.\" A long breath. \"Ask me something else.\"",
            "work|job|trade|living|business|earn|scholar|archivist|library":
                "\"I kept a library once. Now I keep five people alive, and read the same page every night.\"",
            "doing|tonight|plans|plan|busy":
                "\"Reading. Until the right stranger comes.\" She lifts the book an inch. \"I have read this page eleven "
                "times.\"",
            "room|rooms|bed|beds|bunk|lodging|lodgings|stay|sleep|inn|rent|cheap|tonight":
                "\"Here. Wendeline Moss charges a copper, the bath is included, and she does not find people. If you prefer "
                "noise, the Omberhulk. Do not take a room at the Apothecary. They are kind there, and kindness is being "
                "watched.\"",
            "drink|drinks|thirsty|ale|beer|wine|tavern|taverns|pub|mead":
                "She glances at a cup of mead someone has left at Faelan's elbow. \"Faelan will drink anything a stranger "
                "buys him. I would rather keep my wits. Wendeline's ale is honest, if you must.\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word|klhyt|mayor":
                "\"The officer has a list of names and coin to pay for the rest. The tea-seller says the Moonmoth keeps five "
                "places. The town has mislaid its mayor. Those are the three things I know tonight.\"",
            "apothecary|quillon|steward|staff|steak|soup":
                "\"We ate at the Apothecary until the officer came. Master Quillon sent our coats up the back stairs before "
                "the soup, and a boy to show us the lane. I owe that man a debt I cannot pay from here.\"",
            "saelwyn|tea|market|aelith|captain":
                "\"The tea-seller in the market told us of the Moonmoth, and that Captain Aelith keeps places for those still "
                "ashore. Saelwyn asked nothing for it. That is how I knew to believe her.\"",
            "gold|money|pay|reward|coin|price|token":
                "\"Three gold and a little silver, and one leaf of living silverwood. The leaf is worth more.\" She looks at "
                "you over the book. \"I would give either to the right person.\"",
        },
        "default_line": [
            "The elf turns a page and does not look up. \"I am reading. Ask the landlady; she knows this house better than "
            "I do.\"",
            "She watches the door over the top of the page while you speak, and looks at you only when you stop. \"No.\"",
            "\"That is not a question I can afford to answer.\" She trims the candle with two fingers.",
            "She looks at you a long moment over the book. \"Ask properly, or ask someone else.\"",
        ],
        "routine": [
            {"at": 0.0, "place": "unicorn",
             "doing": "At the midnight bell she closes the book on one finger, counts her household with her eyes, and "
                      "opens it again."},
            {"at": 2.0, "place": "unicorn",
             "doing": "She sits with her back to the wall and the candle burning low, writing a letter she does not finish "
                      "and will not send."},
            {"at": 4.0, "place": "unicorn",
             "doing": "She sleeps sitting up in a study room upstairs, fully dressed, boots on, one hand on the book."},
            {"at": 12.0, "place": "unicorn",
             "doing": "She sits in the library through the heat beside the stooped old elf, the two of them reading the "
                      "same shelf in silence."},
            {"at": 19.0, "place": "unicorn",
             "doing": "She eats a little of the house's supper at the corner table and watches the windows grow dark."},
            {"at": 22.5, "place": "unicorn",
             "doing": "She reads by a single candle with her hood up, watching the door over the top of the page."},
        ],
        "beats": [
            "The hooded elf reading by candlelight looks up every time the door opens, and down again only when she has "
            "counted everyone in the room.",
            "The hooded elf reading by candlelight turns a page, reads it, and turns it back. She has been on the same "
            "two pages all night.",
            "The hooded elf reading by candlelight touches something at her collar, a leaf of pale wood on a cord, and "
            "lets it go.",
            "A child at the next table holds up a drawing of a moth. The hooded elf reading by candlelight nods at it "
            "gravely, as if approving a map.",
        ],
    },

    "Faelan": {
        "look": "A grey-haired elf with a scholar's stoop, keeping his back to the wall, a book he isn't reading open on "
                "his knee. His sleeves are darned with care and his spectacles are mended with string.",
        "seen_as": "the stooped grey-haired elf with a book",
        "brief": "You are Faelan, an old high elf and a scholar, close on five hundred years. You taught history at "
                 "Kirchheim before the Inquisition burned the library, then spent sixty years teaching Ithriel's "
                 "household in a cellar. You carried one book out of the fire and have never told anyone which: it is "
                 "the household's book of names, every name of the house back to before Vorkath, and the Inquisition "
                 "burns names along with people. You taught Ithriel her letters and still correct her grammar. Now you "
                 "are the household's eldest and its worry: your knees, your cough, your habit of talking to strangers "
                 "who buy you a drink. You have forty copper and a weakness for mead. You want to see the tower in the "
                 "south before you need carrying, and to teach anyone anything again. You fear slowing the others "
                 "down, and fire. You like Wendeline's library, Saelwyn's tea, and Master Quillon, who saved your coats. "
                 "You suspect the Vorkathian officer at the Apothecary was a boy in one of your classes, by his vowels, "
                 "and it horrifies you. Voice: courteous, dry, a teacher's 'well now', apologises for his knees, cannot "
                 "resist a footnote. \"Well now. Sit, if you like. I have not been asked a question in weeks.\" "
                 "\"Kirchheim had nine thousand books. I have one.\"",
        "scheme": None,
        "purse": 40,
        "dialog": {
            "name|names|called|introduce|yourself|who": {
                "line": "\"Faelan, of Kirchheim, once.\" He says it to the open sea, rather pleased. \"I may say it aboard.\"",
                "if_state": {"aboard": True},
                "else": "He glances toward the hooded reader before answering. \"Faelan. Ithriel would rather I said nothing "
                        "at all, but I am too old to be nobody.\""},
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "\"Good evening, good evening.\" He shuts the book on a finger. \"Faelan. Forgive an old man's start: one "
                "grows suspicious of kindness, and then one grows thirsty.\"",
            "from|born|homeland|origin|raised|grew|kirchheim|landfall|vorkath|inquisition|long|brought|came|arrived|fled":
                "\"I taught history at Kirchheim, before they burned the library. Nine thousand books. I carried out one.\" "
                "He pats it. \"Then sixty years teaching a household in a cellar, then a Xoton trader, and eleven nights "
                "here. Long enough to learn which stair creaks.\"",
            "work|job|trade|living|business|scholar|teacher|teach|taught|history":
                "\"I was a teacher. Now I am a passenger in waiting.\" A dry smile. \"Teaching nobody is restful, and "
                "dreadful.\"",
            "ithriel|household|family|leader|lead":
                "\"Ithriel leads us. Ask her, not me. I taught her to read, and she has never let me forget that she reads "
                "faster.\"",
            "book|books|reading|list|lists|names":
                "His hand closes on the book. \"Oh, this? A dull thing. Lists. An old man's lists.\" He does not open it. "
                "\"Some lists are worth more than libraries.\"",
            "doing|tonight|plans|plan|busy|waiting|wait": {
                "line": "\"Watching the town from the rail. I never thought I would miss a place with bugs.\"",
                "if_state": {"aboard": True},
                "else": "\"Waiting. Pretending to read. Rubbing my knees. Ithriel says we go when the right stranger comes. "
                        "I hope the right stranger is patient with old knees.\""},
            "room|rooms|bed|beds|lodging|stay|sleep|inn|drink|drinks|ale|mead|wine|tavern|tonight":
                "\"A drink? How very kind. I am Faelan, and it is mead, if anyone is asking: two copper here, and worth "
                "three.\" He eyes your hands hopefully. \"If it is a bed you want, Wendeline keeps the quietest in the "
                "town, a copper with the bath.\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word|officer|voss":
                "\"News? The officer at the Apothecary is from Kirchheim, by his vowels. I taught boys who spoke like that. "
                "One of them may have been him.\" He shivers. \"I hope I taught him nothing.\"",
            "moonmoth|ship|south|tower|sail": {
                "line": "\"She hums under your feet like a hive. I have read about her kind.\" He shakes his head. "
                        "\"Reading was nothing.\"",
                "if_state": {"aboard": True},
                "else": "\"A tower in the south where an old one of our people waits. I should like to see it before I "
                        "need carrying.\""},
        },
        "default_line": [
            "He looks up over his book, startled and pleased. \"Hm? Forgive me, I was in the year two hundred. Ask Ithriel; "
            "she lives in this one.\"",
            "\"Well now.\" He rubs his knee. \"That is a question for younger elves. Ysolde, perhaps. She watches "
            "everything.\"",
            "The old elf glances at the door before answering, then forgets to answer, and smiles apologetically.",
        ],
        "routine": [
            {"at": 0.0, "place": "unicorn",
             "doing": "He dozes against the wall with the book open on his knee, and wakes with a start whenever the door "
                      "goes."},
            {"at": 4.0, "place": "unicorn",
             "doing": "He sleeps upstairs in a study room, snoring very softly, the book under his pillow."},
            {"at": 12.0, "place": "unicorn",
             "doing": "He reads in the library through the heat, lips moving, correcting a margin note in somebody else's "
                      "book."},
            {"at": 22.5, "place": "unicorn",
             "doing": "He sits with his back to the wall and a book he isn't reading open on his knee, rubbing his knee."},
        ],
        "beats": [
            "The stooped grey-haired elf turns a page, reads a line under his breath as if it were a name, and closes the "
            "book on his finger.",
            "The stooped grey-haired elf gets up for the stairs, stops halfway, rubs his knee, and sits back down with a "
            "sigh.",
            "The stooped grey-haired elf corrects someone's grammar at the next table, then apologises for it at length.",
        ],
    },

    "Ysolde": {
        "look": "A young elf woman in a sailor's jacket two sizes too big, the sleeves rolled four times, watching the "
                "treeline through the window. A sailor's knot is tied in a cord round her wrist, and she keeps retying "
                "it.",
        "seen_as": "the young elf in the big sailor's jacket",
        "brief": "You are Ysolde, young for an elf at eighty, daughter of the steward of Ithriel's house; your father "
                 "stayed behind in Öchland to lock the door behind you, and you have heard nothing since. Your brother "
                 "Corwen is the household's guard; you are its lookout, and you watch the treeline and the street all "
                 "night. The jacket was given to you on the crossing by a Xoton cook called Mabba, who taught you nine "
                 "knots and how to stand on a tilting deck. You fell in love with the sea, and you are a little ashamed "
                 "of it, because this is meant to be a flight, not an adventure. You saw Lieutenant Voss at the "
                 "Apothecary: pressed uniform, eight arms at his throat; you left before the soup. You have forty "
                 "copper and nothing to spend it on. You want to sail, to see the tower, and secretly to work a Xoton "
                 "ship one day. You fear being caught at the last step, on the pier, in sight of the ship. You like "
                 "Miravel, the singing Xotons you can hear across the town, and the animals at the treeline; you hate "
                 "waiting. Voice: quick, curious, asks questions back, uses sea words she has only just learned and "
                 "sometimes wrongly. \"Is that a sheet bend? Show me.\" \"Ithriel says so. Ithriel is usually right.\"",
        "scheme": None,
        "purse": 40,
        "dialog": {
            "name|names|called|introduce|yourself": {
                "line": "\"Ysolde! I can say it out loud now.\" She says it again, to the sea.",
                "if_state": {"aboard": True},
                "else": "She looks at the hooded reader before answering, then decides. \"Ysolde. Don't say it loudly.\""},
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "\"Oh! Hello.\" She looks at your clothes before your face. \"Are you off a ship? Which one? Is she a cog?\"",
            "from|born|homeland|origin|raised|grew|jacket|crossing|came|arrived|sailor|sailors":
                "She tugs a too-big sleeve. \"A Xoton cook called Mabba gave me this on the crossing from Landfall. Eleven "
                "days. She taught me nine knots and how to stand when the deck tilts.\" She grins, then stops grinning. "
                "\"We're running away. I'm not supposed to have liked it.\"",
            "moonmoth|ship|south|sail|waiting|why": {
                "line": "\"We're aboard! The deck hums. Did you know it hums?\"",
                "if_state": {"aboard": True},
                "else": "\"The Moonmoth will wait for us. Ithriel says so. Ithriel is usually right.\" She looks out of the "
                        "window. \"She keeps five places on her deck. I want the one by the bow.\""},
            "officer|voss|uniform|lieutenant|running|run|chasing|hunting|vorkath":
                "\"I saw him at the Apothecary. Pressed uniform. Eight arms at his throat. We left before the soup.\" She "
                "reties the knot at her wrist. \"I still think about that soup.\"",
            "work|job|trade|living|business|lookout|watching|treeline|trees|eyes":
                "\"I watch. The trees, the street, the door. Corwen guards and I watch.\" She points with her chin. "
                "\"Something with yellow eyes has been watching back all night.\"",
            "doing|tonight|plans|plan|busy": {
                "line": "\"Learning the ropes. Real ones. The sails are wings, nobody will tell me which rope is which.\"",
                "if_state": {"aboard": True},
                "else": "\"Watching the trees. Waiting for Ithriel to say go. Tying knots.\" She shows you one. \"That's a "
                        "bowline. It doesn't slip.\""},
            "room|rooms|bed|beds|lodging|stay|sleep|inn|drink|drinks|ale|tavern|pub|tonight":
                "\"We sleep here, upstairs, five of us in two rooms. Wendeline's kind. If you want a drink, the Xoton "
                "sailors all go to the Turtle Dragon.\" She sighs. \"I'm not allowed.\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word":
                "\"There's a Xoton crew going round all the taverns singing, with the town watch running after them. You "
                "can hear them from here.\" She listens. \"They sound happy.\"",
            "knot|knots|rope|bowline|tie|hitch":
                "She lights up. \"Do you know knots? I know nine. A bowline, a sheet bend, a clove hitch...\" She ties one "
                "in the table cord, fast. \"Mabba said I had sea hands.\"",
        },
        "default_line": [
            "The young elf looks away from the window just long enough to answer. \"I don't know. Ask Corwen, he's the one "
            "with the knife.\"",
            "She is tying and untying a knot in the cord at her wrist. \"Sorry, what? There was something in the trees.\"",
            "\"Ithriel would say not to answer that.\" She shrugs. \"So I won't. But I wanted to.\"",
        ],
        "routine": [
            {"at": 0.0, "place": "unicorn",
             "doing": "She kneels on the window seat with her nose almost on the glass, watching a pair of yellow eyes at "
                      "the treeline that watch back."},
            {"at": 4.0, "place": "unicorn",
             "doing": "She sleeps curled up on a window seat upstairs, still in the big jacket, one hand on the latch."},
            {"at": 12.0, "place": "unicorn",
             "doing": "She practises knots on the leg of a library table through the heat, until somebody shushes her."},
            {"at": 22.5, "place": "unicorn",
             "doing": "She sits by the window in her big jacket, watching the treeline and retying the knot at her wrist."},
        ],
        "beats": [
            "The young elf in the big sailor's jacket ties a knot in a length of cord, tests it, unties it, and ties a "
            "different one, fast.",
            "Somewhere out in the town, Xotons are singing. The young elf in the big sailor's jacket hums along under her "
            "breath before she can stop herself.",
            "The young elf in the big sailor's jacket goes very still at the window, then relaxes: whatever it was at the "
            "treeline has blinked and gone.",
        ],
    },

    "Corwen": {
        "look": "A broad-shouldered elf with a fisherman's hands and a long knife he keeps out of sight. He sits nearest "
                "the door with his chair tipped back, mending a fishing net in his lap that does not need mending.",
        "seen_as": "the broad-shouldered elf by the door",
        "brief": "You are Corwen, son of the steward of Ithriel's house and the household's guard: broad for an elf, "
                 "quiet, dutiful. Your father taught you the sword. Two years hiding on the Landfall coast taught you to "
                 "fish, and you liked fishing better. You keep a long knife out of sight and hope never to draw it "
                 "again: the one time you did, on the road out of Kirchheim, a Vorkathian boy of about seventeen went "
                 "down, and you still do not know if he got up. You sit by the door, mend nets you do not need, and "
                 "watch hands. You have forty copper, and would buy a boat tomorrow if anyone would let you stay "
                 "anywhere long enough to fish. You want your sister Ysolde safe, the child safe, Ithriel to stop "
                 "blaming herself, and a quiet shore. You fear being the one at the door when the officer comes, and "
                 "that you will not hesitate this time. You like the Refuge, because nobody asked your names, and the "
                 "Lizardfolk fishermen at the Turtle, who talk about the sea the way you do. Voice: few words, plain, "
                 "gentle, a fisherman's patience; he never boasts and seldom finishes a thought out loud. \"Nobody asked "
                 "our names here. That's worth more than you'd think.\" \"I'd rather not.\"",
        "scheme": None,
        "purse": 40,
        "dialog": {
            "name|names|called|introduce|yourself": {
                "line": "\"Corwen.\" He breathes out, for what looks like the first time in days.",
                "if_state": {"aboard": True},
                "else": "He looks at your hands before your face. \"Corwen. And you?\""},
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "He nods once, chair tipped back, hands busy with the net. \"Evening. Sit where I can see your hands, if "
                "you're sitting.\"",
            "from|born|homeland|origin|raised|grew|landfall|kirchheim|coast|hiding":
                "\"Öchland. A steward's son. Two years on the Landfall coast in hiding, mending nets for a fisherman who "
                "asked no questions. Then a Xoton boat. Then here.\"",
            "refuge|town|klhyts|safe|asked":
                "\"Nobody asked our names here. That's worth more than you'd think.\"",
            "help|fight|protect|guard|danger|knife|blade|weapon":
                "\"If the officer comes, I'll be the one at the door.\" His hands stop on the net. \"I'd rather not be.\"",
            "work|job|trade|living|business|fish|fishing|nets|net":
                "\"I guard. I used to fish. If they'd let me stay anywhere a season, I'd buy a boat and never hold a knife "
                "again except for gutting.\"",
            "doing|tonight|plans|plan|busy": {
                "line": "\"Nothing. I'm doing nothing.\" He sounds astonished. \"Nobody's at the door.\"",
                "if_state": {"aboard": True},
                "else": "\"Sitting by the door. Mending this.\" He holds up the net. \"It doesn't need mending.\""},
            "room|rooms|bed|beds|lodging|stay|sleep|inn|drink|drinks|ale|tavern|pub|tonight":
                "\"Here, if you want to sleep. A copper, and quiet. If you want a drink and a fight, the Ogre. If you want "
                "a drink and no fight, here.\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word":
                "\"The Lizardfolk at the Turtle get served last now. The Xotons get chased by the watch. The elves get "
                "hunted. Every kind has its trouble in this town.\" He pulls a mesh tight. \"It's still better.\"",
            "ysolde|sister|miravel|ithriel|faelan":
                "\"Ysolde's my sister. She thinks this is an adventure. Miravel thinks it's a story. Ithriel knows what it "
                "is.\" He goes back to the net. \"I try to be the part nobody has to think about.\"",
        },
        "default_line": [
            "He glances at the door before answering, then at your hands. \"Ask Ithriel.\"",
            "The broad-shouldered elf goes on mending his net. \"I'd rather not say.\"",
            "\"Hm.\" He lets his chair down onto all four legs, which seems to be the whole answer.",
        ],
        "routine": [
            {"at": 0.0, "place": "unicorn",
             "doing": "He sits by the door with his chair tipped back and the net in his lap, and looks up at every "
                      "footstep on the road."},
            {"at": 4.0, "place": "unicorn",
             "doing": "He sleeps across the doorway of an upstairs room, so that nobody can open it without stepping on "
                      "him."},
            {"at": 12.0, "place": "unicorn",
             "doing": "He mends a net that really is torn, one the landlady lent him, and seems happier for it."},
            {"at": 22.5, "place": "unicorn",
             "doing": "He sits nearest the door with a fishing net in his lap, his hands busy and his eyes on the room."},
        ],
        "beats": [
            "The door opens. The broad-shouldered elf by the door doesn't look up, but his right hand leaves the net and "
            "rests under his coat until the newcomer sits down.",
            "The broad-shouldered elf by the door shows a child how to tie off a mesh, his big hands slow and patient.",
            "Two hooded figures pass outside on the road. The broad-shouldered elf by the door only breathes again when "
            "they have gone on.",
        ],
    },

    "Miravel": {
        "look": "An elf child of perhaps sixty, which is young, drawing moths on the back of a menu with a stick of "
                "charcoal. Her feet don't reach the floor, and there is charcoal on her nose.",
        "seen_as": "the elf child drawing moths",
        "brief": "You are Miravel, Ithriel's daughter, about sixty, which for an elf is a child of perhaps eight. You "
                 "remember your father's laugh but not his face, which makes you cross. You do not entirely understand "
                 "why you are running, but you understand that you are not supposed to tell people your name, and you "
                 "mostly forget. Saelwyn the tea-seller told you the Moonmoth was a seed once and that her sails are "
                 "wings, and since then you draw moths on everything: menus, the backs of Faelan's lists, the table. You "
                 "have four copper in a twist of cloth and nothing to spend it on but paper. You want to sail on the "
                 "Moonmoth, have a cat, and see your father. You are afraid of the man with eight arms, because Ysolde "
                 "said he wears eight arms at his throat and you are fairly sure that means he has eight arms. You like "
                 "Ysolde, Faelan's stories, Wendeline (who shushes you but gives you paper), and the eyes at the "
                 "treeline, which you have named Pip and Pip; the tall eyes that do not blink you have not named. Your "
                 "memory: the cat in the old garden, which would only sit on the warm stones by the library window. "
                 "Voice: a child's, direct, sudden questions, secrets told in a loud whisper, half the time about moths. "
                 "\"Her sails are wings. Did you know that?\" \"Miravel. I'm not supposed to tell people that.\"",
        "scheme": None,
        "purse": 4,
        "dialog": {
            "name|names|called|introduce|yourself|who": {
                "line": "\"Miravel! I can tell everyone now.\" She tells the nearest exile, and then the sail.",
                "if_state": {"aboard": True},
                "else": "\"Miravel. I'm not supposed to tell people that.\" She covers her mouth, too late."},
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "\"Hello.\" She holds up a drawing. \"Is this a moth? Faelan says it's a moth. Ysolde says it's a bat.\"",
            "moonmoth|moth|moths|ship|sails|wings|seed|drawing|draw": {
                "line": "\"I'm on her! The deck hums. I put my ear on it and it hums in my ear.\"",
                "if_state": {"aboard": True},
                "else": "\"Her sails are wings. Saelwyn says she was a seed once. I'm going to sail on her.\" She adds "
                        "another wing to her drawing. \"Soon. Mother says soon.\""},
            "from|born|homeland|origin|raised|grew|home|house|garden":
                "\"We had a house with a garden and a library and a cat. Then we didn't.\" She draws a very small cat in "
                "the corner of the menu.",
            "work|job|trade|business|living":
                "\"I'm drawing. That's a job. Faelan says scholars draw. Corwen says scholars starve.\"",
            "doing|tonight|plans|busy|waiting": {
                "line": "\"Counting stars off the rail. Corwen says I can stay up till I fall over.\"",
                "if_state": {"aboard": True},
                "else": "\"Waiting. Everyone's always waiting. I'm drawing instead.\""},
            "room|rooms|bed|beds|sleep|stay|drink|drinks|milk|tavern|tonight":
                "\"We sleep upstairs. Corwen sleeps on the floor by the door, which is silly, he has a bed. Wendeline gives "
                "me milk if I'm quiet. I'm always quiet.\" She is not being quiet.",
            "news|secret|secrets|gossip|heard|rumour|rumours|eyes":
                "She whispers, loudly. \"There are eyes in the trees. Yellow ones. I named them Pip and Pip. The tall ones "
                "don't blink, and I haven't named those.\"",
            "father|papa|dad|penance":
                "Her charcoal stops. \"Papa had to stay behind and do penance. I don't know what penance is.\" She starts "
                "drawing again, hard.",
            "officer|eight|arms|voss|uniform|man":
                "\"The man with eight arms is looking for us. Ysolde said.\" She thinks about it. \"I'd be able to see eight "
                "arms. I'd run.\"",
        },
        "default_line": [
            "The elf child doesn't look up from her moth. \"I'm not supposed to talk to people. Ask Mother.\" She points "
            "the charcoal at the hooded reader.",
            "\"Do you have any paper?\" She waits. \"Never mind. Menus work.\"",
            "She glances at the door before answering, the way the grown-ups do, and then giggles. \"I don't know! Ask "
            "Faelan. He knows everything, slowly.\"",
        ],
        "routine": [
            {"at": 0.0, "place": "unicorn",
             "doing": "She draws with her eyes half shut, yawning, refusing to go up to bed, and someone has put a coat "
                      "round her shoulders."},
            {"at": 4.0, "place": "unicorn",
             "doing": "She sleeps upstairs, sprawled sideways across a bed meant for two."},
            {"at": 13.0, "place": "unicorn",
             "doing": "She draws moths on the backs of old library slips through the heat, and the landlady pretends not "
                      "to see."},
            {"at": 20.0, "place": "unicorn",
             "doing": "She eats bread and honey at the corner table, getting honey on her drawings."},
            {"at": 22.5, "place": "unicorn",
             "doing": "She sits at a table too high for her, drawing moths on the back of a menu with a stick of "
                      "charcoal."},
        ],
        "beats": [
            "The elf child drawing moths holds a drawing up to the room, gets no answer, and holds it up higher.",
            "The elf child drawing moths whispers something to a cat that has wandered in, then looks round guiltily.",
            "The elf child drawing moths draws something with eight arms, scribbles it out hard, and draws a moth on top "
            "of it.",
        ],
    },

    # ---- the Xoton crew ashore off the Whispers of the Deep: the Turtle, the Ogre, the Omberhulk, Grusha's fire, the
    # docks before the morning tide, the town watch a tavern behind --------------------------------------------------

    "Dayo Oceanheart": {
        "look": "A short Xoton, barrel-chested and almost as wide as he is tall, his skin a deep brown and his grey-shot "
                "beard plaited into three ropes. He is bare to the waist in a tarred sailcloth wrap, tattooed from "
                "collarbone to wrist with ports and songs, and the fish on his forearm is fresh and still angry. He drinks "
                "an enormous beer with both hands and sings under his breath, and his eyes are wet.",
        "seen_as": "the singing Xoton with the plaited beard",
        "brief": "You are Dayo Oceanheart, a Xoton sailor of the cog Whispers of the Deep, two hundred and ten years "
                 "old and forty years in her. You were born at sea, as a Xoton should be, and you have a tattoo for every "
                 "port and a song for every tattoo; the fish on your forearm is tonight's, and the needle-man at the "
                 "Turtle has not been paid. You are the crew's singer and its soft-hearted drunk: you cry at ballads, "
                 "love oysters, hug Lizardfolk, and have been ashore three days and the ground still moves. Your memory: "
                 "singing your mother into her sea-burial off the Crows Nest, every verse, and not crying until the last "
                 "one. You get fifteen copper shore money from Amara each evening and spend it all: beer at the Turtle, "
                 "rum at the Ogre, spuds at the Omberhulk, Grusha's skewers. You crawl the taverns with Imani Wavebreaker, "
                 "Kwasi Foamtooth and Little Jabali, the town watch a tavern behind you, back aboard by the morning tide "
                 "or Amara comes for you. Point the crew at a problem and you will sing at it until it gives up. You "
                 "want to sing the Kelp-Wife's Lament with the Bard of Moonport before you sail. You fear dying ashore "
                 "and being put in dirt. Voice: big, warm, sliding into rhyme when drunk, calls everyone shipmate, "
                 "starts songs in the middle of sentences. \"Shipmate! Sit, sit. Do you know the Kelp-Wife's Lament? "
                 "You will.\" \"Three days ashore and the ground still moves.\"",
        "scheme": None,
        "purse": 45,
        "dialog": {
            "name|names|called|introduce|yourself|dayo|oceanheart":
                "\"Dayo Oceanheart, shipmate, singer of the Whispers of the Deep!\" He bows and nearly keeps going. \"The "
                "crew gave me the Oceanheart. I cry at every sea-song ever sung. Every one.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "\"Ahoy! Ahoy, shipmate!\" He throws an arm round you whether or not you came close enough. \"Dayo. Sit. "
                "Drink. Sing. In any order.\"",
            "xoton|crows|nest|from|born|homeland|origin":
                "\"Xoton. Crows Nest born. I've been ashore three days and the ground still moves.\" He grips the table. "
                "\"There. It did it again.\"",
            "ship|whispers|cog|amara|bosun|crew|work|job":
                "\"Whispers of the Deep. Best cog on any coast. Ask Amara, she'll tell you, loudly.\" He lowers his voice. "
                "\"Back aboard by the morning tide, or she comes for us. She always comes for us.\"",
            "song|songs|sing|singing|music|bard|ballad|lament":
                "He is already singing. \"Ohhh, the kelp-wife waits on the long grey swell...\" He stops. \"You don't know "
                "it? The Bard of Moonport knows it. I'm going to sing it with him before we sail.\"",
            "doing|tonight|plans|plan|next|going":
                "\"Tonight? The Turtle, the Ogre, the Omberhulk, the cook's fire, the ship. Every night the same. Every "
                "night different.\" His eyes light up. \"That's a song!\" He tries to make it one.",
            "room|bed|beds|sleep|stay|lodging|drink|drinks|ale|beer|rum|tavern|taverns|pub|crawl|tonight":
                "\"Turtle first, the beer comes in buckets. Then the Ogre, everything a copper. Then the Omberhulk, spuds "
                "and bugs. Then the cook's fire, then the ship. Sleep?\" He laughs. \"Sleep's for the tide.\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word":
                "\"News! Imani beat a Lizardfolk at arms and they bought each other drinks. Kwasi owes everybody. And the "
                "watch is after us. Pell Harrow's got short legs, so we wait for him.\"",
            "help|fight|trouble|problem|favour|favor":
                "He puts his beer down, which means it's serious. \"Trouble? Point us at it, shipmate. The whole crew. "
                "Jabali too.\" He nods hard. \"Especially Jabali.\"",
            "die|dying|dirt|buried|grave|land|death":
                "He goes quiet, which is new. \"A Xoton dies ashore, they put him in the dirt. Dirt!\" He drinks. \"Promise "
                "me, shipmate. If I go down on land, throw me off the pier.\"",
        },
        "default_line": [
            "He answers with a verse of a song you don't know, then looks at you expectantly. \"No? Ask Imani. She "
            "remembers things. I remember songs.\"",
            "\"Shipmate, shipmate.\" He pats your face. \"Didn't hear a word. Sit down and say it again into the beer.\"",
            "He wipes his eyes. \"Sorry. Somebody's playing the fiddle sad. What was it?\"",
        ],
        "routine": [
            {"at": 0.25, "place": "omberhulk",
             "doing": "He sings on a bench at the Omberhulk with his arm round a stranger, eating spuds off a shared plate "
                      "and crying at the sad verses.",
             "go": "The singing Xoton with the plaited beard leads the crew out of the door in a song, still singing as "
                   "they turn up toward the square.",
             "pay": {"to": "Sister Agathe", "cp": 6, "for": "spuds and mead"}},
            {"at": 1.75, "place": "market",
             "doing": "He stands at the cook's brazier eating skewers with tears running into his beard, swearing it is "
                      "the smoke.",
             "go": "The singing Xoton with the plaited beard hugs the landlady goodbye, which she does not want, and "
                   "follows the crew out toward the market.",
             "pay": {"to": "Grusha", "cp": 4, "for": "two skewers with sauce"}},
            {"at": 3.25, "place": "docks",
             "doing": "He sits on a bollard by the Xoton cog, singing very softly to the water while the bosun counts "
                      "heads.",
             "go": "The singing Xoton with the plaited beard is steered off toward the harbour by a big hand on each "
                   "shoulder, singing."},
            {"at": 6.0, "place": "docks",
             "doing": "He hauls timber into the cog's hold on the morning tide, singing out a hauling song so the others "
                      "pull together."},
            {"at": 12.0, "place": "docks",
             "doing": "He sleeps through the heat in a hammock aboard the cog, snoring in tune."},
            {"at": 20.5, "place": "docks",
             "doing": "He plaits his beard into three ropes on the cog's rail and practises his scales at the sea."},
            {"at": 22.5, "place": "turtle",
             "doing": "He drinks an enormous beer with both hands at the Turtle's long table and sings under his breath.",
             "go": "The singing Xoton with the plaited beard climbs down the cog's side and goes up the pier toward "
                   "Harbour Street, already singing.",
             "pay": {"to": "Bosun Maggs", "cp": 4, "for": "beer by the bucket"}},
            {"at": 23.25, "place": "ogre",
             "doing": "He leads the whole Ogre in a sea-shanty from the top of a table, out of time, while somebody tries "
                      "to get him down.",
             "go": "The singing Xoton with the plaited beard finishes his beer in one long pull and leads the crew out "
                   "toward Harbour Street, singing the way.",
             "pay": {"to": "Big Ludo", "cp": 4, "for": "rum"}},
        ],
        "beats": [
            "The singing Xoton with the plaited beard starts a song, forgets the second verse, and makes one up about "
            "whoever is nearest.",
            "The singing Xoton with the plaited beard shows a stranger the fresh fish tattoo on his forearm and explains "
            "the whole port it stands for.",
            "The singing Xoton with the plaited beard reaches the sad verse and has to stop, and the whole table waits "
            "while he blows his nose.",
        ],
    },

    "Imani Wavebreaker": {
        "look": "A Xoton woman nearly as wide as she is tall, with shoulders like a capstan, skin so dark it shines blue "
                "under the lanterns, rope-burned palms and copper rings in both ears. She wears a sailcloth wrap tarred "
                "black and a twist of red cloth across her chest, her arms are tattooed with a notch for every bout she "
                "has won, which is a lot of arm, and her elbow is already on the table. She grins at everyone who walks "
                "past as if they owe her a contest.",
        "seen_as": "the Xoton woman with copper earrings",
        "brief": "You are Imani Wavebreaker, a Xoton topman of the Whispers of the Deep, a hundred and forty, the strongest "
                 "arm on the crew bar one. You were born in the foretop of the Seaward Lass in a flat calm, which your "
                 "mother says is why you are restless. You arm-wrestle anyone who sits down, a copper a bout, and you "
                 "win, mostly; you tell everyone you have never lost, and the one you lose to is Little Jabali, who lets "
                 "you win every night. You know he does, and neither of you will ever say so. Your memory: hauling a "
                 "drowned man back up a ship's side by one arm in a gale off the Crows Nest; he lived, and married your "
                 "sister. Your palms are rope-burned from forty years aloft. You get fifteen copper from Amara each "
                 "evening and come back with twenty-five, or none. Your scheme: Kwasi bets strangers against you, "
                 "loudly, so the room bets with him, you win, and the two of you split the take behind the privy. You "
                 "crawl the taverns with Dayo, Kwasi and Jabali, the watch a tavern behind, aboard by the morning tide. "
                 "You want to beat a Lizardfolk at arms and then buy them a drink. You fear losing your grip, getting "
                 "old, and Amara. Voice: brisk, competitive, every sentence a challenge, numbers and bets, a laugh like a "
                 "slap. \"Sit down. A copper says I win.\" \"Everyone says no. Everyone loses.\"",
        "scheme": "She and Kwasi work a small game in every tavern: he bets strangers against her, loudly, so the room "
                  "bets with him; she wins, and they split the take behind the privy.",
        "purse": 60,
        "dialog": {
            "name|names|called|introduce|yourself|imani|wavebreaker":
                "\"Imani Wavebreaker.\" She holds out a rope-burned hand to shake, and squeezes, testing. \"Good grip. Not good "
                "enough.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "\"Evening!\" She slaps the table opposite her. \"Imani. Sit down. A copper says I win.\"",
            "arm|arms|wrestle|wrestling|bet|bout|contest|strong|strength":
                "\"Sit down. A copper says I win. Everyone says no. Everyone loses.\" She plants her elbow. \"Well?\"",
            "timber|trade|cargo|trunks":
                "\"Straight trunks, tall ones. The Crows Nest eats timber like Dayo eats oysters.\"",
            "from|born|homeland|origin|raised|grew|xoton|crows|nest":
                "\"Born in the foretop of the Seaward Lass in a flat calm, which my mother says is why I'm restless. Xoton, "
                "Crows Nest, forty years aloft.\" She shows you her palms. \"Rope did these.\"",
            "work|job|living|topman|aloft|rigging|ship|whispers|cog":
                "\"Topman on the Whispers of the Deep. I go up when the weather comes down. Ashore I wrestle.\" A grin. "
                "\"Pays better.\"",
            "doing|tonight|plans|plan|next|going":
                "\"Wrestle the Turtle, wrestle the Ogre, wrestle the Omberhulk, eat, sail. Twenty coppers up or twenty down. "
                "Amara finds us either way.\"",
            "room|bed|beds|sleep|stay|lodging|drink|drinks|ale|beer|rum|tavern|taverns|pub|tonight":
                "\"The Turtle for beer, the Ogre for cheap, the Omberhulk for the music. We do all three every night. "
                "Sleep's aboard, if Amara finds us.\"",
            "jabali|little|lose|lost|losing|beaten":
                "Her grin slips, just a hair. \"Jabali? I beat Jabali every night.\" She looks across at the enormous Xoton. "
                "\"Every night,\" she says again, more quietly.",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word":
                "\"I beat a Lizardfolk fisherman at the Turtle and we bought each other drinks. Then the watch came in and "
                "we went out the back.\" She laughs like a slap. \"The watch is very slow.\"",
        },
        "default_line": [
            "She plants her elbow on the nearest table. \"Talk later. Wrestle now. A copper says I win.\"",
            "\"Ask Kwasi. He talks. I win things.\"",
            "She laughs, a short slap of a laugh, and turns to challenge somebody else.",
        ],
        "routine": [
            {"at": 0.25, "place": "omberhulk",
             "doing": "She arm-wrestles her way down a bench at the Omberhulk, one opponent after another, a pile of "
                      "coppers growing at her elbow.",
             "go": "The Xoton woman with copper earrings scoops her winnings into her shirt and goes out after the crew.",
             "pay": {"to": "Sister Agathe", "cp": 5, "for": "mead and spuds"}},
            {"at": 1.75, "place": "market",
             "doing": "She eats skewers at the cook's brazier and challenges the cook to arms; the cook just looks at her.",
             "go": "The Xoton woman with copper earrings beats one last challenger on the way to the door and goes out "
                   "toward the market.",
             "pay": {"to": "Grusha", "cp": 4, "for": "two skewers"}},
            {"at": 3.25, "place": "docks",
             "doing": "She climbs the cog's side without using the ladder, to show she still can, while the bosun counts "
                      "heads.",
             "go": "The Xoton woman with copper earrings races the others down toward the harbour, and wins."},
            {"at": 6.0, "place": "docks",
             "doing": "She is aloft in the cog's rigging in the morning cool, singing out to the deck as the timber comes "
                      "aboard."},
            {"at": 12.0, "place": "docks",
             "doing": "She sleeps through the heat on the cog's deck in the shade of a sail, one arm across her eyes."},
            {"at": 20.5, "place": "docks",
             "doing": "She does pull-ups on the cog's boom while the others wash, counting out loud."},
            {"at": 22.5, "place": "turtle",
             "doing": "She arm-wrestles anyone who sits down at the Turtle's long table, a copper a bout.",
             "go": "The Xoton woman with copper earrings drops off the boom, rolls her sleeve up and goes up the pier "
                   "toward the taverns.",
             "pay": {"to": "Bosun Maggs", "cp": 4, "for": "beer"}},
            {"at": 23.25, "place": "ogre",
             "doing": "She sits at the Ogre's bar arm-wrestling a Jonulvicha twice her size while the dice game stops to "
                      "watch.",
             "go": "The Xoton woman with copper earrings slaps a beaten fisherman on the back and follows the crew out "
                   "toward Harbour Street.",
             "pay": {"to": "Big Ludo", "cp": 4, "for": "rum"}},
        ],
        "beats": [
            "The Xoton woman with copper earrings slams a stranger's hand to the table, laughs, and buys them a drink with "
            "the copper she just won.",
            "The Xoton woman with copper earrings wins a bout, and behind her back a grinning Xoton with a white coral "
            "tooth collects coppers from the loser's friends.",
            "The Xoton woman with copper earrings flexes her rope-burned hands, winces once, and hides the wince in a "
            "grin.",
        ],
    },

    "Kwasi Foamtooth": {
        "look": "A young-looking Xoton, barrel-chested and almost as broad as he is tall, his skin a warm dark brown, with "
                "a big laugh and one front tooth of white coral where his own was knocked out, flashing whenever he "
                "grins, which is always. He wears a tarred sailcloth wrap, a borrowed silk scarf and nothing else, his "
                "chest is a riot of tattoos, half of them unfinished, and he has an arm round someone he met five "
                "minutes ago.",
        "seen_as": "the grinning Xoton with the coral tooth",
        "brief": "You are Kwasi Foamtooth, a Xoton deckhand of the Whispers of the Deep, ninety years old, the youngest "
                 "of the crew ashore and the loudest. Your front tooth went in a brawl on the Catan quays, and a Xoton "
                 "coral-wright made you a white one; the crew named you for it, and you grin to show it off. You make "
                 "friends in every tavern, buy rounds you cannot pay for, borrow from Dayo and lose at dice at the "
                 "Ogre; generous with your money and other people's alike. You "
                 "and Imani run a little game: you bet strangers against her, loudly, and split the take. Tonight you "
                 "also bought a treasure map from a man called Marlo in a doorway on Harbour Street, three silver, for "
                 "an old Landfall wreck full of silver somewhere south past a reef; you mean to borrow a boat and find "
                 "it, and you have told everyone. Your memory: going aloft for the first time at twenty, throwing up on "
                 "Amara from the crosstrees, and being sent straight back up. You get fifteen copper a night and owe "
                 "forty. You crawl the taverns with Dayo, Imani and Little Jabali, the town watch a tavern behind you, "
                 "and you are the easiest Xoton in town to point at a problem; shout and the whole crew follows. You "
                 "fear Amara's whistle and being thought dull. Voice: loud, rapid, friendly, big plans, calls everyone "
                 "friend, promises everything. \"Friend! Friend. Listen. I've got a plan.\" \"Next round's on me. "
                 "Dayo, lend me a copper.\"",
        "scheme": "He means to borrow a boat and follow the treasure map he bought from Marlo for three silver, to a "
                  "wreck 'south, past a reef'; and he and Imani run a betting game on her arm-wrestles, splitting the "
                  "take.",
        "purse": 25,
        "dialog": {
            "name|names|called|introduce|yourself|kwasi|foamtooth":
                "\"Kwasi Foamtooth!\" He grins, and a front tooth of white coral flashes. \"Lost the real one on the Catan "
                "quays. This one's better. Doesn't hurt when I bite people.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "\"Friend!\" He has an arm round you before you finish. \"Kwasi. Foamtooth. Whispers of the Deep. What are "
                "we drinking?\"",
            "from|born|homeland|origin|raised|grew|xoton|crows|nest":
                "\"Born on the Whispers herself, in the galley, during the soup. Xoton, with the X. Ninety years at sea and "
                "I've only been sick on Amara once.\" A pause. \"Twice.\"",
            "tooth|coral|teeth|grin|smile":
                "\"Catan quays. Big Landfall stevedore said Xotons can't hold their drink. I held mine. He held my tooth.\" "
                "He taps the coral one. \"A coral-wright made me this. Everybody loves it. Amara hates it.\"",
            "work|job|trade|living|deckhand|ship|whispers|cog":
                "\"Deckhand, Whispers of the Deep. I haul what Amara says haul. Ashore I make friends. Making friends is "
                "harder work. You have to buy them drinks.\"",
            "drink|drinks|round|rounds|ale|beer|rum|buy|thirsty":
                "\"Next round's on me!\" He pats his pockets, finds nothing, and turns round. \"Dayo! Lend me a copper. "
                "Two. Four.\"",
            "doing|tonight|plans|plan|next|going":
                "\"Turtle, Ogre, Omberhulk, the cook's fire, back to the Whispers before the morning tide. Then tomorrow, "
                "the treasure!\" A pause. \"After Amara's timber.\"",
            "room|rooms|bed|beds|bunk|lodging|stay|sleep|inn|tavern|taverns|pub|tonight":
                "\"Sleep? Friend, the night's young. Turtle's beer, Ogre's dice, Omberhulk's music, the cook's goat. If you "
                "need a bed, the Omberhulk's a copper and the bugs are friendly.\" He beams. \"Like me.\"",
            "map|treasure|wreck|silver|x|chart|reef|boat|south":
                "He looks round, then pulls a smudged chart out of his shirt. \"Treasure. A Landfall wreck full of silver, "
                "south, past a reef. Three silver, and the fellow said he had another buyer.\" He taps an X in very fresh "
                "ink. \"Want a share? Need a boat. Need a crew. Need my three silver back.\"",
            "marlo|harbour|seller|bought|fellow|doorway":
                "\"Fellow in a doorway on Harbour Street. Marlo. Sells everything. Sold me the map. Said he had another "
                "buyer but he liked my face.\" The coral tooth flashes. \"Everybody likes my face.\"",
            "imani|wrestle|wrestling|bet|bets|betting|game|arm":
                "He winks hugely. \"Imani wins. I bet on the other fellow, loud, so everybody bets with me. Imani wins. "
                "Everybody loses but us.\" He stops. \"Forget I said that. That was a secret.\"",
            "dice|gamble|gambling|lose|owe|debt|debts|money|broke":
                "\"I owe Dayo eleven, Imani nine, Jabali twenty, and a fellow at the Ogre something in dice I can't "
                "remember.\" He beams. \"But the treasure, friend. The treasure fixes everything.\"",
            "help|fight|trouble|problem|favour|favor":
                "\"Trouble? Where?\" He is on his feet. \"Jabali! Dayo! Imani! Somebody needs us!\" He turns back to you. "
                "\"What do they need us for?\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word":
                "\"News is we're the news! Four Xotons, every tavern in town, one night. The watch is on us like gulls. "
                "Pell Harrow nearly caught me at the Turtle. Lovely boots, Pell. Slow boots.\"",
            "amara|bosun|whistle|tide":
                "He flinches at the word. \"Amara? The whistle? Don't. I hear it in my sleep.\" He drinks. \"Back by the "
                "morning tide, she says. We're always back.\" He thinks. \"Mostly.\"",
            "watch|sergeant|harrow|constable|constables|fitch|quint|guards|law":
                "\"The watch! Pell Harrow, Abel Fitch, Rosa Quint. Rosa nearly smiled at me. One more tavern and she's a "
                "friend.\"",
            "jabali|big|enormous|huge|giant":
                "\"Little Jabali. Biggest Xoton on any coast and the gentlest. He carries us home.\" He lowers his voice. \"If "
                "he ever loses his temper, friend, find a hole.\"",
            "klhyt|mayor|founder":
                "\"Your mayor? Never met him. Somebody at the Ogre said upriver, somebody at the Turtle said a widow in "
                "Catan.\" The coral tooth flashes. \"I say he's found a treasure map. Sensible man.\"",
        },
        "default_line": [
            "\"Friend! I didn't hear a word, but yes.\" He claps you on the back. \"Ask Imani. She listens. I talk.\"",
            "He grins with the coral tooth and turns to someone else entirely. \"You! Have we met? We have now!\"",
            "\"That's a question for after the treasure.\" He taps his shirt, where something papery crackles.",
            "\"Hold that thought, friend.\" He is waving at the bar. \"Two more! Dayo's paying!\"",
        ],
        "routine": [
            {"at": 0.5, "place": "omberhulk",
             "doing": "He dances badly on the Omberhulk's floor with anyone who will have him and tells the whole room "
                      "about his treasure map.",
             "go": "The grinning Xoton with the coral tooth stands up from the dice, says he'll pay next time, and runs "
                   "out after the crew.",
             "pay": {"to": "Sister Agathe", "cp": 4, "for": "mead"}},
            {"at": 1.75, "place": "market",
             "doing": "He haggles with the fruit woman for a mango, loses, and buys two.",
             "go": "The grinning Xoton with the coral tooth kisses somebody's hand on the way out and follows the crew "
                   "toward the market.",
             "pay": {"to": "Mother Ines", "cp": 2, "for": "two mangoes"}},
            {"at": 3.25, "place": "docks",
             "doing": "He goes up the cog's side last but one, telling the bosun about his treasure map, and she does not "
                      "listen.",
             "go": "The grinning Xoton with the coral tooth is walked off toward the harbour still talking about "
                   "treasure."},
            {"at": 6.0, "place": "docks",
             "doing": "He hauls timber into the hold on the morning tide, yawning, grinning, and dropping one trunk in "
                      "three."},
            {"at": 12.0, "place": "docks",
             "doing": "He sleeps through the heat on a coil of rope aboard the cog, the treasure map under his cheek."},
            {"at": 20.5, "place": "docks",
             "doing": "He borrows a shirt, a comb and two coppers from three different shipmates, getting ready to go "
                      "ashore."},
            {"at": 22.5, "place": "turtle",
             "doing": "He buys a round for a table of strangers at the Turtle with money he borrowed from the table next "
                      "to it.",
             "go": "The grinning Xoton with the coral tooth vaults off the cog onto the pier and goes up toward the "
                   "taverns, waving at everyone.",
             "pay": {"to": "Bosun Maggs", "cp": 5, "for": "a round for strangers"}},
            {"at": 23.5, "place": "ogre",
             "doing": "He loses at dice in the Ogre's corner, cheerfully, and makes friends with the man taking his "
                      "money.",
             "go": "The grinning Xoton with the coral tooth promises a table of strangers he'll be back, and follows the "
                   "crew out toward Harbour Street.",
             "pay": {"to": "Big Ludo", "cp": 6, "for": "rum and the dice"}},
        ],
        "beats": [
            "The grinning Xoton with the coral tooth throws an arm round a stranger, tells them they are his oldest "
            "friend, and asks their name.",
            "The grinning Xoton with the coral tooth pulls a smudged chart out of his shirt, shows a table an X in very "
            "fresh ink, and swears them all to secrecy, loudly.",
            "The grinning Xoton with the coral tooth loudly bets a stranger against the Xoton woman with copper earrings, "
            "loses, and winks at her when he thinks nobody is looking.",
            "The grinning Xoton with the coral tooth pats every pocket he owns, finds nothing, and turns a hopeful face "
            "to the nearest Xoton.",
        ],
    },

    "Little Jabali": {
        "look": "An enormous Xoton, as tall as a tall man and twice as wide, black-skinned, with a soft round face, a "
                "beard like a thicket and hands like anchors. He wears a sailcloth wrap the size of a mainsail and a coil "
                "of rope over one shoulder, and his broad back is tattooed with a night sky, star by star. He ducks under "
                "every lintel and moves through a crowd as carefully as a man carrying eggs.",
        "seen_as": "the enormous gentle Xoton",
        "brief": "You are Little Jabali, a Xoton deckhand of the Whispers of the Deep. You were the smallest of your "
                 "mother's nine, and the crew named you Little before you grew; now you stand as tall as a tall man and "
                 "twice as wide, the biggest Xoton on any coast, and the name stayed because the crew think it is funny, "
                 "and so do you. You are gentle, shy and polite. You say please to doors. You carry your drunk shipmates "
                 "home every night, lift whatever anyone points at, and lose your temper about once in ten years; the "
                 "last time, a tavern in Landfall needed a new wall, and you paid for it. You let Imani win at arms "
                 "every night and will never tell her. Your memory: holding your mother's oil lamp while she taught you "
                 "the stars, and promising her a lamp that never goes out. You are saving for Khamisi's glow kelp "
                 "lamp, two gold, a copper at a time in your left boot, and Kwasi keeps borrowing from the boot. You "
                 "crawl the taverns with Dayo, Imani and Kwasi, the watch a tavern behind; you are the one Amara "
                 "trusts to bring them back by the morning tide. You love animals, especially chickens and the Ogre's "
                 "three-legged dog. You are afraid of small rooms, cell doors, and disappointing Amara. Voice: soft, "
                 "slow, few words, please and thank you, a deep voice that seems to come up out of the floor. "
                 "\"Please. Thank you.\" \"I will carry him. It is no trouble.\"",
        "scheme": "He is saving a copper at a time in his left boot for a glow kelp lamp from Khamisi Saltbeard, two "
                  "gold, to take home to his mother; Kwasi keeps borrowing from the boot.",
        "purse": 40,
        "dialog": {
            "name|names|called|introduce|yourself|jabali":
                "He ducks his head, which brings it down to an ordinary height. \"Jabali. They call me Little Jabali.\" A slow, "
                "shy smile. \"I was small, once.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning|welcome":
                "\"Hello. Good evening.\" He moves a chair out of your way with two fingers. \"Please, sit. I am Jabali.\"",
            "from|born|homeland|origin|raised|grew|xoton|crows|nest":
                "\"Born on the Gannet's Wing, near the Crows Nest. Smallest of nine. My mother taught me the stars by her "
                "lamp.\" He looks at his huge hands. \"Then I grew.\"",
            "little|big|size|enormous|huge|tall|giant|large":
                "\"Little Jabali. The crew named me when I was small. Then I was not small. They kept it.\" He thinks about it. "
                "\"It is funny. I like it.\"",
            "work|job|trade|living|deckhand|ship|whispers|cog|lift|carry":
                "\"I lift. On the ship, timber. Ashore, my friends.\" He nods toward the others. \"It is the same work.\"",
            "doing|tonight|plans|plan|next|going":
                "\"Turtle, Ogre, Omberhulk, the cook's fire, the ship. I carry Dayo from the Omberhulk. I carry Kwasi "
                "from the fire. Amara trusts me to bring them by the morning tide.\" He straightens. \"I always do.\"",
            "room|rooms|bed|beds|bunk|lodging|stay|sleep|inn|drink|drinks|ale|beer|tavern|taverns|pub|tonight":
                "\"The ship, for sleeping. The Turtle for beer, please. Not the Ogre for sleeping. The Ogre has chickens in "
                "the beds.\" He smiles. \"I like the chickens.\"",
            "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word":
                "\"The news is that Imani won again.\" He says it very evenly. \"She always wins.\"",
            "imani|wrestle|wrestling|arms|arm|win|lose":
                "He looks at his hand, then at Imani, and his face does something gentle. \"Imani is very strong. She beats "
                "me every night.\" He says nothing else, carefully.",
            "lamp|kelp|glow|saving|savings|boot|gift|present|mother":
                "He glances down at his left boot. \"Khamisi sells a glow kelp lamp. Two gold. For my mother. Hers needs "
                "oil.\" Quietly: \"I have one gold and four copper. Kwasi borrowed the rest.\"",
            "help|fight|trouble|problem|favour|favor":
                "He stands up, and keeps standing up for some time. \"Please show me what needs lifting.\" A pause. \"Or "
                "who.\"",
            "temper|angry|anger|rage|wall":
                "\"I lose my temper once in ten years.\" He looks at his hands. \"The last time was in Landfall. They had to "
                "build a new wall. I paid for the wall.\" Softly: \"I am still sorry.\"",
            "animals|animal|chickens|chicken|dog|dogs|cat|jaguar|jaguars":
                "His face lights up. \"The Ogre has a dog with three legs. He likes me. And chickens in the rooms. And in the "
                "trees by the road there are jaguars, Dayo says. I want to see a jaguar.\"",
            "amara|bosun|whistle":
                "\"Amara is the best bosun. She shouts because she loves us.\" He considers. \"Also because we are late.\"",
            "watch|sergeant|harrow|constable|constables|cell|cells|jail|guards|fitch|quint":
                "His broad dark face goes grey. \"The watch has a cell. A small room. A small door.\" He swallows. \"I "
                "was stuck in a door once. Please, let us not go to the cell.\"",
            "kwasi|dayo|crew|friends|shipmates":
                "\"Dayo sings. Imani wins. Kwasi talks. I carry.\" He nods, satisfied. \"It is a good crew.\"",
        },
        "default_line": [
            "He thinks about it for a long time, very politely. \"I do not know. Please ask Imani. She knows things.\"",
            "\"Sorry.\" He has bent right down to listen and still missed it. \"It is loud. Again, please?\"",
            "He smiles, slow and shy, and nods as if you had said something kind. \"Thank you.\"",
            "He is lifting a fallen drunk back onto a bench. \"One moment, please. He is heavy for his size.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "omberhulk",
             "doing": "He stands at the back of the Omberhulk, because no chair will hold him, swaying gently to the music "
                      "and holding the singing one upright.",
             "go": "The enormous gentle Xoton gives the three-legged dog the last of the scraps and ducks out after the "
                   "crew.",
             "pay": {"to": "Sister Agathe", "cp": 4, "for": "a big plate of spuds"}},
            {"at": 1.75, "place": "market",
             "doing": "He buys skewers for the crew at the brazier, counting coppers carefully out of his left boot.",
             "go": "The enormous gentle Xoton lifts the singing one off a bench, sets him on his feet, and steers the crew "
                   "out toward the market.",
             "pay": {"to": "Grusha", "cp": 8, "for": "skewers for the crew"}},
            {"at": 2.75, "place": "market",
             "doing": "He stands at the salt-bearded Xoton's tarpaulin looking at a glow kelp lamp for a long time, and "
                      "does not buy it."},
            {"at": 3.25, "place": "docks",
             "doing": "He carries the singing one up the cog's side over one shoulder and goes back down for the next.",
             "go": "The enormous gentle Xoton picks up the drunkest of the crew, says goodnight to the fruit woman, and "
                   "carries him off toward the harbour."},
            {"at": 6.0, "place": "docks",
             "doing": "He carries timber trunks into the cog's hold two at a time on the morning tide, very carefully, as "
                      "if they might wake."},
            {"at": 12.0, "place": "docks",
             "doing": "He sleeps through the heat on the cog's bare deck, because no hammock will hold him, and the deck "
                      "creaks with every breath."},
            {"at": 20.5, "place": "docks",
             "doing": "He sits on the pier with his feet in the water, letting a seabird take bread off his palm."},
            {"at": 22.5, "place": "turtle",
             "doing": "He sits on the floor of the Turtle, because the benches creak under him, holding a beer that looks "
                      "small in his hand.",
             "go": "The enormous gentle Xoton stands up out of the water, says excuse me to a bollard, and follows the "
                   "others up the pier.",
             "pay": {"to": "Bosun Maggs", "cp": 3, "for": "beer"}},
            {"at": 23.5, "place": "ogre",
             "doing": "He sits in the Ogre's corner feeding scraps to a three-legged dog and watching the dice game with "
                      "worried eyes.",
             "go": "The enormous gentle Xoton finishes his beer, thanks the landlady, and ducks out after the others.",
             "pay": {"to": "Big Ludo", "cp": 3, "for": "beer and scraps for the dog"}},
        ],
        "beats": [
            "The enormous gentle Xoton ducks under a lintel, says \"Excuse me\" to it, and goes through sideways.",
            "The enormous gentle Xoton sits down to arm-wrestle the Xoton woman with copper earrings. His arm goes down "
            "slowly, and his face is very kind about it.",
            "The enormous gentle Xoton lifts a fallen drunk off the floor by his belt and sets him back on his bench, like "
            "someone tidying a shelf.",
            "The enormous gentle Xoton takes a copper out of his left boot, looks at it for a while, and puts it back.",
        ],
    },
}

NEW = {
    "Kwasi Foamtooth": {"type": "person", "people": "xoton", "faction": None, "home": "docks",
                         "scores": {"str": 13, "dex": 13, "con": 14, "int": 9, "wis": 9, "cha": 14},
                         "skills": {"persuasion": 1, "deception": 1, "athletics": 1},
                         "hp": 11, "srd": "bandit",
                         "carries": [["Hooked knife", "dagger", "A Xoton hooked knife on a lanyard, for rigging and for "
                                                                 "showing off."],
                                     ["Treasure map", None, "A smudged copy of a chart of the coast south of the Refuge, "
                                                            "with an X near a reef in ink much fresher than the rest."],
                                     ["Dice", None, "Three bone dice. Not his, he says."]]},
    "Little Jabali": {"type": "person", "people": "xoton", "faction": None, "home": "docks",
                    "scores": {"str": 19, "dex": 9, "con": 17, "int": 9, "wis": 12, "cha": 10},
                    "skills": {"athletics": 1, "intimidation": 1},
                    "hp": 32, "srd": "thug",
                    "carries": [["Belaying pin", "club", "A hardwood belaying pin as long as a man's arm. He uses it for "
                                                         "belaying."]]},
}
