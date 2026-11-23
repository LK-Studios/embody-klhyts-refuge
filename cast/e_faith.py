# The faith of Vorkath, as the people of the Refuge met it: one topic each (two for those with a lot to say), in their
# own voices, from the LoreKeeper digest of the faith (the goddess with eight arms; the Eight Arms of War, Peace,
# Pleasure, Pain, Chaos, Destiny, Death and Life and their saints; the Inquisition Teflon founded at Kirchheim; the
# elves made enemies of the state; Emperor Arkmady Melenkov's missions abroad; the octogram; the roadside offerings to
# Percival, sweets for Gwendoline, a little prayer to Hester-Stanhope, Vistadine's bathhouses).
#
# Merged over a_powers.py, b_town.py, c_market_docks.py and d_vorkath.py by build.load_cast: each topic here JOINS the
# person's table. No new topic shares an alias with any topic the person already has. Three old topics are retired
# (None) and given again without "vorkath", so that word goes to the faith: Kael's home, Faelan's home, Dominico's
# officer-and-noble. Their lines are unchanged. Lieutenant Voss keeps his vorkath topic and gains one on the saints;
# the Custodian is left as he is.
#
# FAITH_TEXTS: "catechism", the missionary tract The Eight Arms and Their Saints; "library", one sentence for the Touchy
# Unicorn's shelf.
#
# invented: Sister Agathe: twenty years under the Life Arm, taught to weigh every thought against the goddess's; the
#   inquisitor she hit was a Pain Arm man come for three elves still in fever; the bedpan was copper
# invented: The Bard of Moonport: toasts Saint Pil's Loffgren nightly; every choirmaster in Landfall tried to save him
# invented: Kael Ironjaw: the camp soldiers told the half-orc children of Gideon every night instead of names
# invented: Grusha: the fort soldiers prayed to Gideon before the supper her mother cooked and ate on the floor
# invented: Ruk Halfhand: his father kept one camp custom, sweets for Gwendoline; Ruk has left a sweet on the warehouse
#   step four nights
# invented: Big Ludo: the frontier pits had a priest who blessed both fighters and took a cut of the bets; Gideon was
#   painted on the pit wall
# invented: Ithriel: her house paid the church its tithe and said its prayers at the gate for years
# invented: Faelan: born about 200 BV, older than the goddess; first heard of her as a rumour of a fire giant and two
#   battered young men, one with six fingers (Teflon's, in the lore)
# invented: Thoradin: a priest read out the grove's sins before it was lit
# invented: Saelwyn: her grove would not kneel when the church came for the old faiths (the lore's absorbing of the
#   druidic faiths as aspects of Vorkath, set against her canon fire)
# invented: Captain Aelith: the Army of the Faithful sang hymns as they burned the Hall of Osmith and the Keep of Sheath
# invented: Wendeline Moss: kept some of the records at Kirchheim; a missionary off a Landfall ship left the tract on
#   her desk last week
# invented: Captain Danny DeVito: said a little prayer to Hester-Stanhope before the two sixes that won him the
#   Emerald Eye
# invented: Hulda Ironwake: Landfall sailors paint an octopus on the bow for Hester-Stanhope and pray to her in a blow
# invented: Captain Eirik: every ship from Landfall now brings a priest and a box of little books (Melenkov's missions);
#   Xotons knew this coast before Hester-Stanhope and told nobody
# invented: Bosun Maggs: Port Brutzee's keepers nail wheat over the door for Pil's Loffgren; she was lost two days in
#   his Bewilderment as a deckhand
# invented: Mother Ines: leaves a mango on the milestone by the gate for Saint Percival every night, as her mother did;
#   Wick eats it
# invented: Harbourmaster Teague: the bishop's cargo he counted was forty casks of stout declared as holy water
# invented: Sergeant Pell Harrow: on the Fronterian border he turned back families and elves with an inquisitor at his
#   elbow
# invented: Constable Abel Fitch: his mother says eight prayers a night, one for each Arm, with the shutters shut
# invented: Constable Rosa Quint: since the lieutenant came, half the lanes wear the octogram over the shirt
# invented: Fat Gog: the old river gods were content with a fish left on a stone
# invented: Hessa: her mother's saying on the octopus
# invented: Klhyt: the Refuge has no temple, no tithe and no inquisitor, by Article One
# invented: Dominico: his father hanged the men the Inquisition sent him, with a prayer for each
# invented: Phillip Everuex: his mother keeps a family pew with a brass plate
# invented: Lieutenant Voss: serves the Arm of Pain, under Teflon
# invented: Master Quillon: the great houses of Aurelia were Soomian when he entered service and Vorkathian when he left
# invented: Husok Sourfist: went to a Vistadine bathhouse twice to be cured of leaving, and left both times
# invented: Wick: left two coppers of sweets for Gwendoline on the porch step, for her mother
# invented: Ned Tallow: a navy chaplain blessed the guns before every fight
# invented: Miravel: Faelan told her the goddess holds a saint's sign in every hand
# invented: catechism: printed at Kirchheim in 300 EV for Melenkov's missions; the octogram's eight points for the
#   eight Arms; "An Ory" read as the orrery; the Nameless One left unnamed; its closing line
# invented: library: the tract is new on the Touchy Unicorn's shelf, between the Inquisition and the jungle gods

CAST = {
    "Sister Agathe": {"dialog": {
        "saint|saints|goddess|god|gods|arms|eight|octogram|baptist|bathhouse|bathhouses|ankh|holy|waters|jug|jugs":
            "She touches the wimple. \"Eight arms preserve us, child. I served the one that pours: Saint Vistadine, the "
            "Baptist. Holy water, clean floors, and every thought weighed against the goddess's before you were let to "
            "think it.\" She wipes a table hard. \"I weighed mine. Kept the nursing. Gave back the rest.\"",
        "inquisitor|inquisitors|bedpan|heretic|heretics|heresy|penance|impure|teflon":
            "Her hands go flat on the bar. \"He was a Pain Arm man, Teflon's sort: suffer for your soul, and see that "
            "everybody else does too. He wanted three elves out of their beds with the fever still on them.\" A short, "
            "hard breath. \"It was a copper bedpan, child. It rang like a bell. I'd do it again with a heavier one.\"",
    }},
    "The Bard of Moonport": {"dialog": {
        "loffgren|pil|pils|saint|saints|brewer|brewers|stout|toast|bewilderment|pleasure":
            "He raises his cup to the rafters. \"To Saint Pil's Loffgren, One For The Road! Master brewer, inventor of "
            "stout, a very prolific bard, dead of his liver in the year twelve.\" He drinks. \"The only saint who'd have "
            "bought a round. I toast him nightly. It's the nearest I come to church.\"",
        "vorkath|vorkathian|goddess|god|gods|faith|church|pray|prayer|hymn|hymns|choir|arms|octogram|temple|inquisition|inquisitor":
            "\"Vorkath? Eight arms, a hymn for every one, and not one of them in a key a man can sing after midnight.\" "
            "He tunes a string. \"Every choirmaster in Landfall has tried to save my soul. My soul declined, politely, "
            "in four parts.\"",
    }},
    "Kael Ironjaw": {"dialog": {
        "from|born|homeland|frontier|camps|vorkathia|vorkath|raised|origin|home": None,
        "from|born|homeland|frontier|camps|vorkathia|raised|origin|home":
            "\"The frontier camps, Vorkathia's side. Dozens of us half-and-halfs, raised by soldiers too busy for names. "
            "Good soldiers, mostly.\" He considers. \"Bad cooks, all of them.\"",
        "vorkath|gideon|saint|saints|chain|borgund|unifier|everliving|goddess|god|gods|faith|pray|prayer|church|octogram|arms":
            "\"Saint Gideon!\" He punches the air and nearly hits a lamp. \"Unifier of Orcs! Big man, ball and chain, "
            "killed a fire giant. Soldiers told us about him every night, instead of names.\" He grins. \"The goddess I "
            "don't know so good. Gideon I know. Wanted to be him. Got a glaive out of a ditch instead. Close enough.\"",
    }},
    "Grusha": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|gideon|pray|prayer|prayers|arms|octogram|unifier|priest|priests":
            "\"Gideon, Unifier of Orcs.\" She snorts smoke. \"The soldiers prayed to him before supper. My mother cooked "
            "the supper and ate hers on the floor.\" She turns a skewer. \"Unified. Ha. Eat first. Pray after, if "
            "you're still hungry.\"",
    }},
    "Ruk Halfhand": {"dialog": {
        "vorkath|goddess|god|gods|faith|pray|prayer|church|saint|saints|gwendoline|candy|sweets|sweet|heaven|octogram|arms": {
            "line": "\"Sweets for the little girl. Gwendoline. She holds your hand to heaven, if you paid her.\" He turns "
                    "a tally stick. \"I left one on the warehouse step. Four nights.\" A slow breath. \"Nobody needed it. "
                    "Good.\"",
            "if_state": {"klhyt_home": True},
            "else": "\"My father kept one thing from the camps. Sweets for the little girl. Gwendoline. She holds your hand "
                    "when you die, if you paid her.\" He turns a tally stick. \"I left one on the warehouse step. Four "
                    "nights.\" He stops. \"For nobody.\""},
    }},
    "Big Ludo": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|priest|priests|bless|blessed|octogram|gideon|arms":
            "He rubs the broken tusk. \"Pit priest. Blessed both fighters. Took a cut of the bets.\" A shrug that takes a "
            "while. \"Gideon on the pit wall. Ball and chain.\" He sets a mug down. \"Gog never blessed me. Paid me.\"",
    }},
    "Ithriel": {"dialog": {
        "goddess|god|gods|faith|church|saint|saints|pray|prayer|prayers|octogram|tithe|decree|enemies|heretic|heretics|impure":
            "\"My house paid the church its tithe for years, and said its prayers at the gate whenever the collector "
            "came.\" She closes the book on one finger. \"It did not make us less elven. The decree names us enemies of "
            "the state.\" A pause. \"Nobody asked the goddess.\"",
    }},
    "Faelan": {"dialog": {
        "from|born|homeland|origin|raised|grew|kirchheim|landfall|vorkath|inquisition|long|brought|came|arrived|fled": None,
        "from|born|homeland|origin|raised|grew|kirchheim|landfall|inquisition|long|brought|came|arrived|fled":
            "\"I taught history at Kirchheim, before they burned the library. Nine thousand books. I carried out one.\" "
            "He pats it. \"Then sixty years teaching a household in a cellar, then a Xoton trader, and eleven nights "
            "here. Long enough to learn which stair creaks.\"",
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|religion|calendar|era|heathen|teflon|octogram|arms":
            "\"Well now. I was born in the year two hundred Before Vorkath, as they count it now, so I am older than the "
            "goddess, and a great deal older than her church.\" He rubs his knee. \"Footnote: when I first heard of her "
            "she was a rumour about a fire giant and two very battered young men. One had six fingers on his left hand. "
            "Nobody believes that part.\"",
    }},
    "Saelwyn": {"dialog": {
        "goddess|god|gods|faith|church|saint|saints|pray|prayer|octogram|arms|kneel|aspect|aspects|heathen|pagan|inquisition|inquisitor":
            "\"When the church came for the old faiths, it called my grove heathen and burned it. Now the emperor says the "
            "old faiths were the goddess all along. An aspect of her.\" She turns her cup a quarter turn. \"Still. First "
            "they ask you to kneel. Mine would not.\"",
    }},
    "Thoradin": {"dialog": {
        "goddess|god|gods|faith|church|saint|saints|pray|prayer|prayers|priest|priests|heathen|temple|octogram|arms|sin|sins":
            "\"They have a saint for builders, a saint for brewers, a saint for gamblers. None for trees.\" His hand goes "
            "to his shirt. \"A priest stood in our grove and read out its sins before they lit it. Oaks have no sins. They "
            "have rings.\"",
    }},
    "Captain Aelith": {"dialog": {
        "goddess|god|gods|faith|church|saint|saints|pray|prayer|faithful|dais|sheath|octogram|arms|heretic|heretics|hymn|hymns":
            "\"The Army of the Faithful burned the Hall of Osmith, and the Keep of Sheath with it. They sang hymns while "
            "they did it, and they sang them well.\" She lays her palm on the rail. \"She does not pray. She grows. It is "
            "the older answer.\"",
    }},
    "Wendeline Moss": {"dialog": {
        "tract|tracts|pamphlet|missionary|missionaries|catechism|goddess|god|gods|faith|church|saint|saints|pray|prayer|octogram|arms":
            "\"A missionary off a Landfall ship left a tract on my desk last week. The Eight Arms and Their Saints, eight "
            "pages, illustrated.\" She lowers her spectacles. \"I shelved it. I shelve everything. That is the difference "
            "between me and the people who printed it.\"",
        "inquisitor|inquisitors|teflon|decree|decrees|heretic|heretics|heresy|records|archive|archives|archivist|jotun|cleansing|impure":
            "\"Kirchheim is where Teflon founded the Inquisition, in the year one. It keeps the finest records in "
            "Landfall. I know. I kept some of them.\" She takes off her spectacles and polishes them. \"Geror Jotun's "
            "decree on the elven races is very short. The worst ones always are.\"",
    }},
    "Captain Danny DeVito": {"dialog": {
        "hester|stanhope|hester-stanhope|saint|saints|vorkath|goddess|god|gods|faith|church|pray|prayer|dice|gambler|gamblers|gambling|yolo|octogram|arms":
            "He kisses a gold coin and flips it. \"Captain-Lady Hester-Stanhope, sweetheart. Saint of travellers and "
            "gamblers. I said a little prayer to her, threw two sixes, and a drunk Landfall factor handed me a ship.\" He "
            "catches the coin. \"They say you can still hear her on the waves, yelling YOLO. Nobody knows what it means. "
            "I know what it means. It means bet the ship.\"",
    }},
    "Hulda Ironwake": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|hester|stanhope|hester-stanhope|octopus|octogram|arms":
            "She doesn't stop coiling. \"Their goddess? Never seen her haul a line. Landfall sailors paint an octopus on "
            "the bow for Hester-Stanhope and pray to her in a blow.\" One short blast on the whistle, at nobody. \"She "
            "mapped the world and vanished at twenty-six without a copper. Fine sailor. Bad purser.\"",
    }},
    "Captain Eirik": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|hester|stanhope|hester-stanhope|mission|missions|missionary|missionaries|priest|priests|emperor|melenkov|octogram|arms":
            "\"Your saint Hester-Stanhope found this coast, friend, and Landfall has not stopped arriving since.\" He "
            "laughs. \"Xotons knew it first. We told nobody. Now the Emperor sends missions to every corner of the world, "
            "and every ship from Landfall brings a priest and a box of little books.\" He shrugs, enormous. \"I take a "
            "book. I say thank you. On land I am furniture.\"",
    }},
    "Bosun Maggs": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|loffgren|pil|bewilderment|wheat|catacombs|octogram|arms":
            "\"Every keeper in Port Brutzee nails a sheaf of wheat over the door for Saint Pil's Loffgren. I nailed up "
            "harpoons.\" She jerks a thumb at them. \"Got lost two days in his Bewilderment when I was a deckhand. A pub "
            "with catacombs, under a fifth of the town. Best two days of my life, sailor, and I can't remember either.\"",
    }},
    "Mother Ines": {"dialog": {
        "percival|builder|offering|offerings|milestone|roadside|deed|deeds|kindness|vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|octogram|arms":
            "She laughs. \"Every night I put one mango on the milestone by the gate, for Saint Percival. Habit, love. My "
            "mother did it, back in Landfall.\" She fans herself. \"Whoever's hungry eats it, and they're meant to pass "
            "the good deed on. Wick eats it. Wick's never passed on anything but gossip.\"",
    }},
    "Harbourmaster Teague": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|bishop|bishops|tithe|tithes|holy|priest|priests|octogram|arms":
            "\"I counted a bishop's cargo at Port Brutzee. Forty casks, declared as holy water from the Vistadine springs, "
            "duty free.\" He sharpens a pencil with his thumbnail. \"It was stout. I wrote 'stout, forty casks, duty "
            "owing', and caught the next boat.\" He sighs. \"Eight arms, and every one of them out for a tithe.\"",
    }},
    "Sergeant Pell Harrow": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|inquisition|inquisitor|inquisitors|octogram|arms|border|borders|refugee|refugees":
            "He sighs. \"Twenty years on the Fronterian border, son, with an inquisitor at my elbow, turning back folk who "
            "wanted out. Families. Elves. They'd pray at me, and I'd say it wasn't my gate, it was the goddess's.\" He "
            "looks down the open road. \"This one's mine. It stays open.\"",
    }},
    "Constable Abel Fitch": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|prayers|octogram|arms|religion|worship":
            "\"My mother still says her prayers, sir. Eight of them, one for each Arm, with the shutters shut.\" He frowns "
            "at his spear. \"That's allowed! Article One. Nobody asks where you came from, so nobody can ask who you pray "
            "to. I think that follows.\" A pause. \"I'll ask the sergeant.\"",
    }},
    "Constable Rosa Quint": {"dialog": {
        "goddess|god|gods|faith|church|saint|saints|pray|prayer|octogram|arms|religion|pious|devout|inquisition|inquisitor":
            "\"Between you and me, love, half the lanes wear an octogram under the shirt, and since the lieutenant came, "
            "the other half wear it over.\" She chews. \"My mam can tell which from the washing. The sweat goes round it "
            "different.\"",
    }},
    "Fat Gog": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|octogram|arms|priest|priests|religion|worship":
            "He folds his hands on his belly. \"I have watched gods come up the river before, friend. The old ones were "
            "content with a fish left on a stone.\" A slow breath through the nostrils. \"This one is young, and hungry, "
            "and wants the whole town on its knees. Young things are always hungry. I was.\"",
    }},
    "River": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|inquisition|inquisitor|inquisitors|octogram|arms|heretic|heretics|theology":
            "She glances at the long mirror behind the bar, then back at you. \"Vorkath likes her magic licensed, love, "
            "her gods sanctioned, and her grandmothers quiet.\" She pours. \"I'll serve anyone. I won't kneel for anyone. "
            "Drink first. Then theology.\"",
    }},
    "Ssark": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|octogram|arms|priest|priests|worship":
            "His tongue tastes the air. \"Your goddess has eight arms. A thing with eight arms wants to hold a great "
            "deal.\" A long silence. \"She is new. New things are hungry. The sea is old. It holds everything and asks "
            "for nothing.\"",
    }},
    "Hessa": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|octopus|octogram|arms|priest|priests|worship":
            "\"The warm ones from over the sea draw an octopus on their boats, for their goddess.\" She shifts the gaff to "
            "the other hand. \"My mother says an octopus is clever, and hungry, and never full. I keep the old one's "
            "door. Not hers.\"",
    }},
    "Klhyt": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|octogram|arms|religion|temple|temples|tithe|worship": {
            "line": "\"Four nights in a box, shipmate. I've prayed to all eight of her arms and a few legs.\" A cracked "
                    "laugh. \"The only one who ever answered me was a lizard with a waterskin.\"",
            "if_state": {"bound": True},
            "else": "\"Pray to whoever you like in my town, shipmate, or to nobody. Article One: nobody here shall be asked "
                    "where they came from.\" He scratches his beard. \"Gods come from somewhere too, so we don't ask. No "
                    "temple, no tithe, no inquisitor. A pump and a lot of pubs.\""},
    }},
    "Dominico": {"dialog": {
        "phillip|everuex|voss|officer|noble|vorkath|lieutenant": None,
        "phillip|everuex|voss|officer|noble|lieutenant":
            "\"There's a Vorkathian officer at that table eating steak, and a powdered Everuex at that one, sweating "
            "through his coat. One wants elves, the other wants a woman.\" He doesn't look at either. \"Neither is my "
            "business, until they make trouble on my street.\"",
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|inquisition|inquisitor|inquisitors|octogram|arms|heretic|heretics":
            "He turns the silver ring once, all the way round. \"My father hanged the men the Inquisition sent him, and "
            "said a prayer for each, so the rope would hold.\" He listens a moment, to something that is not you. \"They "
            "burn men for the books on my shelf. In Landfall I would be ash. Here, nobody asks.\"",
    }},
    "Phillip Everuex": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|octogram|arms|pious|devout|pew|cathedral|religion":
            "He produces a little silver octogram from his waistcoat and holds it up like a ticket. \"The family is "
            "devout. Terribly devout. Mother has a pew with our name on a brass plate, and nobody may sit in it, "
            "including Mother.\" He tucks it away. \"I pray every morning. Mostly for shade.\"",
    }},
    "Lieutenant Voss": {"dialog": {
        "saint|saints|teflon|pain|penance|pray|prayer|prayers|goddess|god|gods|faith|church|octogram|heretic|heretics|impure|purity|purification|doctrine":
            "\"I serve the Arm of Pain, under Teflon, First of Many, who founded the Inquisition.\" He touches the sigil "
            "at his throat. \"He suffered for the purification of the soul, and so must we all. Pleasure has no "
            "sweetness without pain to give it context.\" He cuts a precise square of steak. \"This, for example.\"",
    }},
    "Master Quillon": {"dialog": {
        "goddess|god|gods|faith|church|saint|saints|pray|prayer|soomian|soomi|grace|convert|converted|octogram|arms|religion":
            "\"The great houses of Aurelia were Soomian when I entered service, and Vorkathian when I left.\" He adjusts a "
            "glove. \"The silver did not change, nor the linen. Only the grace before meat. The house learned the new one "
            "in a week.\"",
    }},
    "Husok Sourfist": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|vistadine|bathhouse|habit|habits|cure|cured|octogram|arms":
            "\"Saint Vistadine cures you of a bad habit. It's in her gospel.\" He drinks. \"I went to her bathhouse twice "
            "to be cured of leaving.\" He looks into the cup. \"Left both times. Halfway through.\"",
    }},
    "Wick": {"dialog": {
        "gwendoline|sweet|sweets|candy|heaven|vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|octogram|arms":
            "\"The little girl! Gwendoline. You pay her sweets and she holds your hand all the way to heaven. Mother Ines "
            "says.\" She digs a toe in the dust. \"I gave her two for Mum. Two coppers of sweets, on the porch step. To be "
            "safe.\" Then, brightly: \"That one's free.\"",
    }},
    "Ned Tallow": {"dialog": {
        "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|chaplain|chaplains|bless|blessed|blessing|octogram|arms":
            "\"Thirty years at sea, friend. The chaplain blessed the guns before every fight, and I loaded them after.\" "
            "He trims a wick with his thumbnail. \"Guns never seemed to know the difference.\" He looks out at the "
            "harbour mouth. \"Steady.\"",
    }},
    "Miravel": {"dialog": {
        "goddess|god|gods|pray|prayer|saint|saints|church|faith":
            "\"Faelan says the goddess has eight arms too, and holds a saint's thing in every hand. A chain and a spade "
            "and some sweets.\" She draws eight arms on a moth, frowning. \"I'd hold cats.\"",
    }},
}

FAITH_TEXTS = {
    "catechism": (
        "THE EIGHT ARMS AND THEIR SAINTS\n"
        "A short instruction in the faith, for the Colonies.\n"
        "Printed at Kirchheim in the year 300 of the Era of Vorkath, for the Missions of His Imperial Majesty Arkmady "
        "Melenkov, Emperor of Greater Vorkathia, to the known and unknown corners of the globe.\n"
        "\n"
        "Vorkath is the Saviour of humankind. She heard the cries of her first disciples in the dark beneath the earth, "
        "and raised them up. With her followers she cast down the one whose name is forbidden, and brought new wealth "
        "and peace to humankind. She is shown as a woman with eight arms, and in each hand she holds the sign of one of "
        "her saints.\n"
        "\n"
        "These are her Eight Arms, and the saint of each.\n"
        "War. Saint Gideon, the Everliving: Hero of Vorkathia, Destroyer of Sief, Herald of the Morning Star, Unifier "
        "of Orcs. His sign is the ball and chain.\n"
        "Peace. Saint Percival, the Builder: patron of good deeds, author of The Kindness of Strangers. His sign is the "
        "spade, the mill or the saw.\n"
        "Pleasure. Saint Pil's Loffgren, One For The Road: master brewer, inventor of stout, the Right Hand Man. His sign "
        "is wine, stout, grapes or wheat.\n"
        "Pain. Teflon, First of Many: First Cleric of Vorkath, who founded the Inquisition at Kirchheim. His sign is the "
        "skewered man, the spider or the hourglass.\n"
        "Chaos. Saint Captain-Lady Hester-Stanhope, the Fearless: patron of travellers, adventurers and gamblers, who "
        "first discovered Shalamar. Her sign is lightning, the storm, a ship, the octopus or the crab.\n"
        "Destiny. Miss Annabella Rand, the Blind Savant: master of calculus, inventor of triangles, explainer of flight, "
        "mother of order. Her sign is the sextant, the glass eye, the orrery or the triangle.\n"
        "Death. Saint Gwendoline, Handholder to Heaven: the little girl who holds out her hand to the dying. Her sign is "
        "a toy, sweets or a hand.\n"
        "Life. Saint Vistadine, the Baptist: the healing water. Her sign is the infinity, the ankh or the pouring jug.\n"
        "\n"
        "The Octogram. The simple sign of the faith is the octogram, eight points for the Eight Arms, on a warrior's "
        "shield or around a priest's neck. Where it is drawn as a crab, an octopus or a spider, it is hers still.\n"
        "\n"
        "Instruction for the faithful.\n"
        "Leave an offering at the roadside for Saint Percival. If you are in need, eat of it, and pass on the good deed.\n"
        "Pay Saint Gwendoline in sweets, that she may grant safe passage to the afterlife.\n"
        "Before a journey, say a little prayer to Saint Hester-Stanhope, and hope the wind will carry it.\n"
        "In sickness, pray to Saint Vistadine, and weigh each thought by whether it reflects the mind of Vorkath.\n"
        "Work until your hands bleed, as Teflon did, for pleasure cannot taste of sweetness without pain to give it "
        "context.\n"
        "Report unsanctioned magic, and the worship of other gods, to the Inquisition.\n"
        "Remember that the elven races are enemies of the state.\n"
        "Eight arms has Vorkath, and room in every one for you."
    ),
    "library": (
        "New on the shelf, between the Inquisition and the jungle gods: The Eight Arms and Their Saints, a thin tract "
        "printed at Kirchheim for the colonies, still smelling of a ship's hold."
    ),
}
