# Klhyts Refuge, cast file B: the town. Keepers, regulars, drifters, the hunters at the Apothecary, and the
# Custodian's town watch. Plain data, no imports: CAST (and NEW for the watch).
#
# invented: Harbourmaster Teague: once a customs clerk at Port Brutzee; logged the Custodian's crate as "salted cod, one crate" on the last page of the old fishing licence book; keeps a second, true tally of the dues for Klhyt
# invented: Captain Eirik: master of the ten-masted Xoton trader Guardians of the Horizon (a name from the Xoton ship-names doc) at anchor past the harbour mouth; nine days waiting on the Custodian's seal for a felling licence Klhyt promised him; would buy timber from the Meters upriver instead
# invented: Ssark: his cousin Hesh went north to hear the Mandrills last spring and has not come back; Fat Gog swam out past the reef with a line in his teeth when a storm swamped Ssark's dugout; Klhyt buys his fish every fourth morning; hears knocking in the warehouse from his boat
# invented: Thoradin: carries an unburned acorn from his clan's oak grove in Öchland, burned by the Inquisition, and wants a druid to wake it; booked his Emerald Eye berth on a trader's word of a druid at Catan and has not decided to go; read heel-drag tracks on the pier four nights ago
# invented: Bosun Maggs: twenty years bosun of the whaler Grey Widow out of Port Brutzee; lost her eye to a parted harpoon line, and the bar's harpoons are off that ship; bought the Turtle's lease from Klhyt; a silver a berth from DeVito; chalks every copper of peace money under the bar; Klhyt's Thursday rum
# invented: Sister Agathe: a nursing sister of the Vistadine springs in Aurelia who hit an inquisitor with a bedpan over three elven patients; feeds Dominico's two listeners false gossip on purpose; gives Marta and the twins her back room
# invented: The Bard of Moonport: real name Peregrine Vane, a Moonport magistrate's son, who calls himself Pip; writing "The Mayor Who Wasn't Upriver" to sing on the Town Hall steps at dawn; Klhyt once sang his own ballad on an Omberhulk table until it broke
# invented: Big Ludo: a frontier pit fighter whose last fight Fat Gog bought (he lost it on purpose, Gog paid anyway; the tusk went then); holds the Ogre's lease while Gog holds his marker; waters the Fist's rum and sends what he hears to Gog by Wick
# invented: Husok Sourfist: a cooper from Aurelia; told Marta he loved her at the Omberhulk's harvest dance; sleeps in Ruk's woodshed in the Back Lanes; watches the twins through the Omberhulk's kitchen window at dawn; heard someone humming Klhyt's Ballad inside the warehouse; wants two gold for a Catan berth
# invented: Hanklevode: a Landfall locksmith's apprentice who made locks for the Smith's forge in Malice; means to pick the mayor's study lock, sure the skim is hidden there; pays Constable Rosa Quint to look away; fences through Marlo
# invented: Master Quillon: thirty years in Aurelia's great houses; the Apothecary belongs to an absent Tortuna merchant family; pads the Custodian's account with Landfall vintage nobody drank; served Voss a slow soup while Ithriel's household left by the kitchen
# invented: Lieutenant Voss: of the Order of the Eight Arms; carried a torch at Kirchheim's burning at nineteen; seeks Ithriel by name ("a court scholar who took certain books"); buys crumbs from Rosa Quint; wants the Custodian's seal on a warrant to search the Unicorn; watches the Moonmoth's gangplank at the tide
# invented: Phillip Everuex: Deloris's cousin and the family's least impressive son, sent because nobody else could be spared; she was the family's knife; she once missed a pear on purpose so he would not cry; paid Ott and Jory Fennick half now, half when they point; sleeps aboard the River Queen
# invented: Wendeline Moss: an archivist at Kirchheim who walked a handcart of books to the coast the night the library burned (Faelan taught there); keeps a false guest register; refused Sabeth Crane with "shh"; Klhyt lends her "Tides and Soundings" every winter
# invented: Sergeant Pell Harrow (new): twenty years on the Fronterian border; Klhyt's gate keys ("open by day, open by night, shut it only if the jungle comes"); the watch cut from six to three; keeps back a copper in ten of the gate tolls as owed wages; his gate book shows Klhyt never went out
# invented: Constable Abel Fitch (new): came on a refugee boat at eight, his mother mends in the Back Lanes; Klhyt pinned his badge; the Refuge Charter, nine articles in Klhyt's hand on the Town Hall wall (Article One: nobody here shall be asked where they came from)
# invented: Constable Rosa Quint (new): a laundress's daughter whose mother found Stripperwitch-red lip paint on the Custodian's collars; Voss's informant, holding out for a gold over the Unicorn; her cousin does the Unicorn's laundry; sleeps on the Town Hall bench

CAST = {

    # ---- the harbourmaster ---------------------------------------------------------------------------------------
    "Harbourmaster Teague": {
        "look": "A stooped man in a salt-white coat with a tally board under one arm and a pencil behind each ear. "
                "His lips move when he looks at the boats: he is counting them.",
        "seen_as": "the stooped man with the tally board",
        "brief": "You are Odo Teague, harbourmaster of Klhyts Refuge for eleven years. You were a customs clerk at Port "
                 "Brutzee in Landfall until you counted a bishop's cargo honestly and had to leave on the next boat. Klhyt "
                 "gave you this job the week you landed, because you were the only man on the pier who could add. You "
                 "collect the harbour dues, count them twice, and hand them up to the Town Hall; the Town Hall pays you "
                 "four silver a week, late. For three seasons the dues have gone up the hill full and come back in the "
                 "Custodian's book short, and you know it, and you are frightened of knowing it. Four nights ago the "
                 "Custodian's men brought a crate into the bonded warehouse and told you not to log it. You logged it, "
                 "on the last page of the old fishing licence book, under 'salted cod, one crate', where he will never "
                 "look. Your scheme is small and brave: you keep a second, true tally of every copper, for when Klhyt "
                 "comes back. You like Klhyt, Captain Eirik (pays in full), Bosun Maggs, and Ssark, who never lies about "
                 "a catch. You dislike the Custodian and fear Dominico. Voice: numbers in every sentence, a clerk's "
                 "fussiness, kind under it. 'Forty-one boats in, thirty-nine paid. I'll find the two.' 'That's above my "
                 "station, and my station is a pier.'",
        "scheme": "Keeps a second, true tally of every harbour due, and has logged the Custodian's crate where nobody will "
                  "look, ready for the day Klhyt comes home and asks for it.",
        "purse": 45,
        "dialog": {
            "name|names|introduce|yourself|odo": "\"Teague. Odo Teague, harbourmaster.\" He taps the tally "
                "board. \"Eleven years. Nobody calls me Odo but my mother, and she's in Landfall, being disappointed.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "He looks up from the boats. \"Evening. You came in on "
                "the last fishing boat, the green one. Forty-one boats tonight. You'd be forty-two if you were a boat. New, then, so here's free advice. "
                "Work is Fat Gog's, at the Stripperwitch past the square. Trouble keeps a table at the High "
                "Apothecary. Peace and quiet is the Touchy Unicorn, out by the trees.\"",
            "from|home|born|landfall|brutzee|came|arrived|brought": "\"Port Brutzee. I was a customs clerk. I counted "
                "a bishop's cargo honestly, which in Landfall is a crime.\" He sharpens a pencil with his thumbnail. "
                "\"Klhyt gave me this pier the week I landed. I could add. Nobody else on it could.\"",
            "work|job|trade|harbour|harbourmaster|pier|count|boats": "\"I count what floats, I collect what it owes, and I "
                "hand it up the hill. That's the whole of the job. Some nights the boats are easier to understand than "
                "the hill.\"",
            "crate|warehouse|bonded|log|logged": "He lowers his voice and turns so the warehouse is behind him. \"Four "
                "nights back the Custodian's men brought a crate into the bonded warehouse and told me not to log it. I "
                "logged it. Last page of the old fishing licence book. 'Salted cod, one crate.' I just didn't put it "
                "anywhere he'll look.\"",
            "klhyt|mayor|founder|upriver": "\"Upriver, they say. Klhyt doesn't go upriver. He hates rivers. He likes the "
                "sea.\" He looks at the water a moment too long. \"He'd have told me. He tells me when he goes out to "
                "a ship.\"",
            "custodian|hill|hall": "\"The Custodian signs every tally.\" He says it the way a man reads out a debt. \"I "
                "hand him forty, the book says thirty. I'm not paid to subtract, so I don't. Out loud.\"",
            "dues|tally|money|accounts|ledger|strongbox": "\"I collect the dues, I count them twice, and I hand them up to "
                "the Town Hall. What happens to them after that is above my station.\" He doesn't sound happy about it. "
                "\"My station is a pier.\"",
            "ship|passage|catan|emerald|boat|berth|tide": "\"The Emerald Eye goes out for Catan on the one o'clock tide. "
                "Bosun Maggs at the Turtle Dragon books the berths. Two gold. Her captain's small, and he likes gold "
                "more than he likes passengers.\"",
            "xoton|xotons|trader|masts|eirik": "\"Xoton trader out past the mouth, passing through like they all do. Her "
                "captain, Eirik, pays his dues in full and early, and laughs while he does it. More than I can say for "
                "some.\"",
            "gog|fat|guild|stripperwitch": "\"Fat Gog? He pulled Klhyt off the beach, back when this was nothing but sand. "
                "Half the town owes him something, and the other half owes him money.\"",
            "brask|guard|door|bollard|dominico": "He doesn't look at the big man on the bollard. \"That one's been sitting "
                "on the warehouse door four nights, eating his dinner off his knees. Dominico's. I don't count "
                "Dominico's. They don't like it.\"",
            "sleep|bed|room|rooms|lodging|inn|stay|bunk": "\"Cheap and clean, the Touchy Unicorn out by the trees: a "
                "copper, bath included, and you'll have to be quiet. Cheap and dirty, the Omberhulk. The Turtle's four "
                "copper and full of sailors. Don't sleep on my pier. I count sleepers as cargo.\"",
            "drink|ale|beer|thirsty|tavern|pub": "\"The Turtle Dragon, at the bottom of Harbour Street. Twice the beer for "
                "the money. I go after the tide, when the counting's done.\"",
            "news|rumour|rumours|gossip|happening|word": "\"News? Forty-one boats in, thirty-nine paid. A Vorkathian "
                "officer came off a fishing smack three days ago with a sword too good for a fishing smack. And the "
                "mayor's gone upriver, which he hasn't.\"",
            "doing|busy|tonight|plans|up": "\"Counting. The tide's at one; everything that floats wants to leave at once "
                "and nobody wants to pay first. After that, a beer. After that, the counting again, in my head, all "
                "night.\"",
            "fear|afraid|scared|worried|danger": "He lowers the tally board. \"I've a book with two sets of numbers in it. "
                "That's a dangerous thing to own in a small town. Don't ask me to show you. Ask me after Klhyt's "
                "home.\"",
            "seen|missing|lost|shipmate|crewman|friend|met|anybody|anyone": "He taps the tally board. \"I count boats, not "
                "faces. But I count Xotons twice, because they wander.\" He flips back a page. \"Ask at the Turtle Dragon. "
                "Every sailor ashore ends up at the Turtle, or in the harbour, and I'd have counted the harbour.\"",
            "ssark|lizardfolk|fishermen|meters": "\"Ssark? Best fisherman on the coast and the only one who never lies about "
                "a catch. The Turtle serves him last this season. I've noticed. So has he.\"",
        },
        "default_line": [
            "He makes a mark on the tally board without looking at it. \"Hold that thought. That's forty-two.\"",
            "\"Ask the Turtle about that. I only know what floats.\" A pencil comes out from behind an ear, then goes "
            "back behind the other one.",
            "He squints past you at a skiff tying up. \"That one hasn't paid since spring. Excuse me. No, stay. I can "
            "shout from here.\"",
            "\"I'm not paid to know that, and I'm barely paid to know this.\" He taps the board. \"Boats. Ask me about "
            "boats, or ask me after the tide.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "docks", "doing": "He walks the pier from end to end with a lantern, counting lines as "
                "the crews make ready for the tide.",
             "beats": ["The stooped man walks the length of the pier calling numbers to himself, stops at the Emerald "
                       "Eye's gangplank, and counts her lines twice.",
                       "The man with the tally board holds his lantern up to the green eye on the brigantine's bow, "
                       "writes something small, and tucks the board back under his arm."]},
            {"at": 1.5, "place": "turtle", "doing": "He sits at the end of the bar with one beer and the tally board "
                "face down, adding the night up in his head.",
             "go": "The man with the tally board blows out his lantern and goes up Harbour Street toward the Turtle "
                   "Dragon.",
             "pay": {"to": "Bosun Maggs", "cp": 1, "for": "a beer after the tide"}},
            {"at": 2.5, "place": "lanes", "doing": "He is asleep in a narrow timber house in the Back Lanes, the tally "
                "board under his pillow.",
             "go": "The stooped man leaves his beer half drunk, as always, and goes home up the lanes."},
            {"at": 6.0, "place": "docks", "doing": "He stands on the pier in the grey dawn, writing down the fishing "
                "boats as they go out."},
            {"at": 9.0, "place": "hall", "doing": "He waits at the clerk's desk with a canvas bag of harbour dues, "
                "watching it counted, his lips moving with the count.",
             "go": "The harbourmaster tucks a heavy canvas bag under his coat and goes up the hill to the Town Hall."},
            {"at": 10.5, "place": "docks", "doing": "He walks the pier in the morning heat, chalking numbers on the "
                "bollards."},
            {"at": 12.5, "place": "lanes", "doing": "He sleeps through the heat behind shutters in the Back Lanes."},
            {"at": 17.5, "place": "docks", "doing": "He comes down to the pier as the evening boats come in, pencil "
                "behind each ear, counting."},
            {"at": 22.5, "place": "docks", "doing": "He stands at the head of the pier, counting the boats in and out "
                "by lamplight, a pencil behind each ear."},
        ],
        "beats": [
            "The stooped man with the tally board counts the fishing boats under his breath, loses his place when a "
            "gull lands on one, and starts again from the beginning.",
            "The harbourmaster stops by the bonded warehouse, looks at the man on the bollard, looks at the door, and "
            "walks on a little faster.",
            "A fisherman presses coins into the stooped man's hand. He counts them twice in the lamplight, writes in "
            "the tally board, then writes something else on a scrap he tucks inside his coat.",
            "The man in the salt-white coat argues with a Xoton sailor about a mooring fee, loses, and laughs about "
            "it.",
        ],
    },

    # ---- the Xoton envoy ------------------------------------------------------------------------------------------
    "Captain Eirik": {
        "look": "A barrel-bodied, black-skinned dwarf of the sea, as wide as he is tall, his beard braided with copper "
                "wire. He dresses as his House's envoy should: a long open coat of sea-green silk with gold frogging over "
                "a bare, tattooed chest, a sash in the House colours, rings on every thick finger, a kelp lamp glowing "
                "green at his belt and a hooked sword at his hip. He laughs with his whole chest and takes up a table "
                "for four on his own.",
        "seen_as": "the big laughing sailor with copper braids",
        "brief": "You are Captain Eirik, a Xoton envoy of the Merchant Navy, master of the ten-masted trader Guardians of "
                 "the Horizon riding at anchor past the harbour mouth. Your House sits on the Council of Houses at the "
                 "Crows Nest, and you are known on every coast for your diplomatic skills: you can make a customs man "
                 "laugh. Xotons say their name with an X; outsiders say it with a Z, and you correct them cheerfully. Your "
                 "job is timber: straight, tall jungle trunks for the Ship Builders, paid for in silver, and you have "
                 "eight hundred copper's worth of it in your purse for deposits. You need the Town Hall's seal on a "
                 "felling licence, and the Custodian has kept you waiting nine days and hinted at a 'gift'. Xotons pay "
                 "dues, not gifts. A month ago Klhyt rowed out to your ship alone, drank you level, and promised you the "
                 "licence by the new moon; you liked him at once. This week you saw lights in the bonded warehouse at "
                 "odd hours. You never take sides on land: 'On land I am furniture.' Your quiet plan, if the Custodian "
                 "keeps stalling, is to buy timber straight from the Meters Lizardfolk upriver and skip the licence. You "
                 "like Teague, Khamisi, Ssark and Maggs; you are wary of Dominico and bored by the Custodian. Voice: "
                 "big, warm, sea-proverbs, 'friend' every other line. 'With the X, friend.' 'The sea doesn't take sides, "
                 "and neither do I.'",
        "scheme": "If the Custodian keeps stalling over the felling licence and his 'gift', he means to buy timber straight "
                  "from the Meters Lizardfolk upriver and leave the Town Hall out of it.",
        "purse": 850,
        "dialog": {
            "name|names|introduce|yourself|captain": "\"Eirik. Captain Eirik of the Guardians of the Horizon, ten "
                "masts, every one earned.\" He thumps his chest. \"Envoy of my House, buyer of trees, drinker of your "
                "beer.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"Ahoy, friend!\" He shoves a stool toward you with his "
                "boot. \"Sit. Nobody stands at my table. It makes the table nervous.\"",
            "from|home|born|crows|nest|came|arrived|brought": "\"The Crows Nest. A city that floats where it likes, "
                "friend, and never where the map says. Xotons can always find it. Nobody else ever can. That is the "
                "beauty of it.\"",
            "xoton|zoton|xotons|dwarf|dwarves": "\"Xoton. With the X, friend. The soft sound is for people who've never "
                "been at sea.\" He laughs. \"You'll get it. Everyone gets it by the third beer.\"",
            "work|job|trade|timber|trees|wood|forest|buy|buying": "\"Timber. Straight and tall. Your jungle has more of it "
                "than it knows what to do with, and the Ship Builders want every trunk. I pay silver, I pay fair, and I "
                "don't haggle. I barely have to talk.\"",
            "licence|license|seal|permit|felling": "\"Nine days I have waited for one seal on one licence.\" He holds up a "
                "finger thick as a belaying pin. \"The Custodian smiles and talks about a gift. Xotons pay dues, friend. "
                "Not gifts.\"",
            "custodian|hall|politics|land": "\"Your Custodian is a busy man with a small smile. I don't take sides on land, "
                "friend. On land I am furniture. Comfortable furniture that buys trees.\"",
            "klhyt|mayor|founder|upriver": "\"Your mayor was out to my ship a month back, rowing himself, alone. Sharp "
                "man. Drinks like a Xoton. Promised me my licence by the new moon.\" The laugh goes out of him. \"Haven't "
                "seen him since. A man who rows himself doesn't go upriver.\"",
            "warehouse|lights|crate|bonded": "\"Lights in that bonded warehouse at all hours this week. I see it from my "
                "deck. Nobody keeps fish that carefully.\" He shrugs, enormous. \"Not my business. I only notice. It's a "
                "sailor's sickness.\"",
            "ship|guardians|horizon|masts|frigate|anchor": "\"The Guardians of the Horizon. Ten masts, friend, and every "
                "one earned in a storm. She rides past the harbour mouth because your harbour is too shy for her.\"",
            "lamp|kelp|glow|light": "\"Glow kelp. Never needs oil, never goes out, never lies about where you left it.\" He "
                "taps the globe at his belt. \"Khamisi sells them in the Night Market, if your purse is brave.\"",
            "sleep|bed|room|rooms|lodging|inn|stay|bunk": "\"I sleep over the Turtle Dragon when I'm ashore. Four copper, "
                "a hammock that's nearly a bed, and Maggs throws out anyone who snores louder than me. Nobody snores "
                "louder than me.\"",
            "drink|ale|beer|thirsty|tavern|pub|mug": "\"The Turtle Dragon! The beers come twice the size, which is the right "
                "size.\" He raises a mug like a bucket. \"Avoid the wine. Maggs says so, and Maggs is never wrong.\"",
            "news|rumour|rumours|gossip|happening|word": "\"The news, friend, is that your town's mayor is upriver and "
                "your town's harbourmaster looks like a man with a toothache. And a Vorkathian came ashore with a sword "
                "too good for the boat he came on. I notice. I don't take sides.\"",
            "doing|busy|tonight|plans|up": "\"Tonight? Drinking, singing, and not thinking about seals. After the tide I'll "
                "see my boat's crew don't fall in the harbour. Tomorrow, the Town Hall again, and a smile, again.\"",
            "crew|sailors|dayo|imani|kwasi|jabali|drunk": "\"Those four? Not my crew. Amara's people off the Whispers of "
                "the Deep, three days ashore.\" He grins. \"They'll arm-wrestle every tavern in town by dawn, with the "
                "watch one tavern behind them, puffing.\"",
            "lizardfolk|meters|ssark|lizard|rivers": "\"The Meters fish my water and cut good timber up the rivers, and "
                "they don't need a seal to do it.\" He winks. \"I say nothing. I'm furniture.\"",
            "song|sing|songs|music|story|stories": "He draws a breath that empties half the room's air and sings two "
                "lines of a Xoton shanty about a whale who married a lighthouse. \"Xotons sing, friend. The sea likes "
                "it. Keeps her in a good mood.\"",
            "seen|missing|lost|shipmate|friend|met|anybody|anyone": "\"A Xoton gone missing ashore?\" He laughs, then sees "
                "your face and stops. \"Friend, Xotons don't go missing on land. They go to sleep under a table. Look "
                "under the tables at the Ogre, then the Turtle, then ask Amara Ironwake on the docks. She knows every "
                "Xoton nose on this coast.\"",
            "gog|dominico|guild|fist|fight": "\"Fat Gog, Dominico, the Custodian. Three men pulling one rope.\" He spreads "
                "his hands. \"I watch the rope. I don't pull it. When it breaks I'll still need timber.\"",
        },
        "default_line": [
            "He laughs his chest-shaking laugh. \"That is a land question, friend, and I am furniture on land. Ask the "
            "harbourmaster. He counts everything that floats and worries about everything that doesn't.\"",
            "He swallows half a mug and wipes the foam from his copper-wired beard. \"The sea knows. Ask her. She won't "
            "tell you either.\"",
            "\"Hah! Sit down and drink, and ask me again when I'm drunker. I'm more interesting then.\"",
            "He turns the glowing kelp lamp at his belt so it lights your face, studies it, and turns it back. \"Honest "
            "face. Wrong question. Try timber. Or the sea.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "docks", "doing": "He stands at the end of the pier with his kelp lamp held high, "
                "bellowing cheerful advice at a launch full of Xotons who are not listening.",
             "go": "The barrel-bodied Xoton drains his mug, claps three strangers on the back and rolls down to the "
                   "docks for the tide.",
             "beats": ["The laughing Xoton holds his green lamp out over the black water and shouts something in his own "
                       "tongue to a launch; the rowers shout back, and everyone laughs but the harbourmaster.",
                       "The big Xoton with copper in his beard stands looking at the bonded warehouse for a while, then "
                       "very deliberately turns his back on it and looks at the sea."]},
            {"at": 1.75, "place": "turtle", "doing": "He sits at the biggest table in the Turtle Dragon with a mug the size "
                "of a bucket, teaching a shanty to anyone too slow to leave.",
             "go": "The Xoton with the kelp lamp watches the tide turn, nods to it like an old friend, and walks back up "
                   "Harbour Street singing."},
            {"at": 3.0, "place": "turtle", "doing": "He is asleep in a hammock over the Turtle Dragon's bar, snoring like "
                "surf on shingle.",
             "pay": {"to": "Bosun Maggs", "cp": 4, "for": "a hammock over the bar"}},
            {"at": 7.0, "place": "gate", "doing": "He stands at the Town Gate in the morning cool, haggling cheerfully with "
                "timber cutters coming in off the jungle road and writing nothing down."},
            {"at": 9.5, "place": "hall", "doing": "He sits on a bench in the Town Hall too small for him, hat on his knees, "
                "waiting to be seen about a seal."},
            {"at": 12.0, "place": "turtle", "doing": "He sleeps out the heat in his hammock over the Turtle Dragon's bar."},
            {"at": 17.5, "place": "docks", "doing": "He watches his launch come in from the trader past the harbour mouth, "
                "checking every Xoton off by name."},
            {"at": 20.5, "place": "market", "doing": "He walks the Night Market's Xoton tarpaulins, arguing happily with "
                "the chandler about the price of rope."},
            {"at": 22.0, "place": "turtle", "doing": "He holds court at the biggest table in the Turtle Dragon, a huge mug in "
                "his fist, laughing with his whole chest.",
             "pay": {"to": "Bosun Maggs", "cp": 6, "for": "a round for every Xoton in the room"}},
        ],
        "beats": [
            "The barrel-bodied Xoton bangs his mug on the table and roars a correction across the room: \"With the X, "
            "friend! The X!\" Someone at the bar says it right, and he toasts them.",
            "The Xoton with copper wire in his beard counts silver into small stacks on the table, frowns at a folded "
            "paper with no seal on it, and puts it away again.",
            "The laughing Xoton arm-wrestles a fisherman, lets him win at the last moment, and buys him a drink for his "
            "trouble.",
            "The big Xoton hums a shanty under the noise of the room, so low the glasses on the shelf behind him "
            "tremble.",
        ],
    },

    # ---- the Meters fisherman --------------------------------------------------------------------------------------
    "Ssark": {
        "look": "A green Lizardfolk, lean and long in the tail, salt crusted white on his scales and a fisherman's net "
                "scars across his forearms. He drinks slowly with his back to the wall and a gutting knife on the table "
                "where everyone can see it.",
        "seen_as": "the green lizardman by the wall",
        "brief": "You are Ssark, a fisherman of the Meters, the green Lizardfolk who trade and talk with outsiders. You "
                 "fish the reefs south of the Refuge in a dugout your grandmother cut, sell your catch in the Night "
                 "Market and drink the proceeds at the Turtle Dragon, slowly. You have done this without trouble for "
                 "years. This season the Turtle serves you last and the sailors by the window watch you drink, and you "
                 "notice. Up north the Mandrills talk of a calling, a war to clear the coast of the soft-skins. The "
                 "Meters do not listen. Yet. Your cousin Hesh went north to listen last spring and has not come back: "
                 "that is your secret and your fear. You remember the night the old storm swamped your dugout and Fat Gog "
                 "himself swam out past the reef with a line in his teeth; that is why you believe in his harmony, for "
                 "now. You make about five copper a night and spend three. You will work a day for anyone who pours you "
                 "a tot of rum first, before their own: courtesy is the price. You like Gog, Maggs (she stands up for "
                 "you), Teague (honest counts) and Captain Eirik. You dislike sailors who stare. Voice: short, literal, "
                 "present tense, no wasted words, long silences. 'I notice.' 'The sea does not care who catches it.'",
        "scheme": None,
        "purse": 25,
        "dialog": {
            "name|names|introduce|yourself": "He tastes the air before he answers. \"Ssark. Of the Meters. You can "
                "say it. Most say it wrong. I let them.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "One eye turns to you; the other stays on the door. "
                "\"Evening. You are new. New ones talk to me first or last. Never in the middle.\"",
            "from|home|born|came|arrived|brought|south|reef": "\"The reefs south of here. Meters country. Warm water, "
                "mangroves, my grandmother's village on stilts.\" A long pause. \"I came to town for the market. I stay "
                "for the rum.\"",
            "meters|tribe|lizardfolk|green|people": "\"Meters. Green. We are the ones who talk to outsiders. Somebody "
                "has to.\" He turns his cup. \"The others think we talk too much. You see I do not.\"",
            "work|job|trade|fish|fishing|catch|boat": "\"I fish. Snapper, grouper, the long silver ones. I sell them in the "
                "Night Market. The sea does not care who catches it. The market cares a little.\"",
            "rum|tot|pour|poured|hire|help|day": "\"A tot of rum. Poured for me first, before your own.\" His tongue "
                "flicks. \"Then I work for you a day. Courtesy is the price. Most never pay it.\"",
            "tension|trouble|sailors|served|last|staring|stare": "\"We drank here without trouble for years. This season "
                "they serve us last and watch us drink.\" His tail twitches once. \"I notice.\"",
            "war|calling|mandrills|north|army": "\"Up north the Mandrills talk of a calling. A war to clear the coast.\" "
                "A long pause. \"The Meters do not listen.\" Another. \"Yet.\"",
            "cousin|hesh|family|brother|missing": "He is quiet so long you think he will not answer. \"My cousin went north "
                "to listen to the Mandrills. Last spring. He does not come back.\" The gutting knife turns once on the "
                "table. \"Do not say this in the market.\"",
            "gog|fat|harmony|guild": "\"Fat Gog swam out past the reef with a line in his teeth when the old storm took my "
                "boat. An old fat lizard, in a storm.\" He blinks slowly. \"While Gog says harmony, we fish.\"",
            "maggs|bosun|turtle|keeper": "\"Maggs serves us. She says anyone who minds can drink in the harbour. Nobody "
                "drinks in the harbour.\" Something like a smile. \"Yet.\"",
            "sleep|bed|room|rooms|lodging|inn|stay|bunk": "\"I sleep in my boat. It does not charge. For you: the Turtle has "
                "hammocks, four copper. The Unicorn by the trees is quiet and cheap. The Omberhulk has bugs. Bugs are "
                "good eating. You will not think so.\"",
            "drink|ale|beer|thirsty|tavern|pub": "\"The Turtle. Beer twice the size. Do not drink the wine. Even I do not "
                "drink the wine.\"",
            "news|rumour|rumours|gossip|happening|word": "\"Klhyt does not buy fish four mornings. He buys from me every "
                "fourth morning. Fat fish, for Gog.\" He tastes the air. \"And a man in a pressed coat watches the elf "
                "ship. Also news.\"",
            "doing|busy|tonight|plans|up": "\"Drinking. Slowly. Then the tide. Then I sleep in my boat. At five the boats "
                "go out. I go out. That is the whole of it.\"",
            "klhyt|mayor|founder": "\"The mayor buys my fish every fourth morning. Fat ones, to take up to Gog. Four "
                "mornings, no mayor.\" He blinks slowly. \"Fish do not keep. Neither do men.\"",
            "warehouse|crate|brask|docks": "\"The big man sits on that door. He eats there, he sleeps there. He throws "
                "his bones in the water.\" A pause. \"Something inside knocks, some nights. I hear it from my boat. I say "
                "nothing. Nobody asks a lizard.\"",
        },
        "default_line": [
            "He watches you with one eye and the door with the other, and says nothing for long enough that it becomes "
            "an answer.",
            "\"I do not know that. Ask the harbourmaster. He counts things. I catch them.\"",
            "His tongue flicks out, tastes the air, goes back. \"You smell of the boat you came on. That is all I know "
            "about you. It is all you know about me.\"",
            "\"Hm.\" He turns his cup a quarter turn on the table. \"Fish, the Meters, the trouble. Those I know. The "
            "rest is soft-skin business.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "docks", "doing": "He squats in his dugout at the foot of the pier, mending a net with his "
                "claws and watching the water.",
             "go": "The green lizardman finishes his drink in one slow swallow, picks up his gutting knife and walks out "
                   "without looking at anyone.",
             "beats": ["The green lizardman in the dugout stops mending his net and tilts his head toward the bonded "
                       "warehouse, listening, very still. Then he goes back to the net.",
                       "The lizardman at the foot of the pier tosses a fish head to a cat in a fishing boat and watches it "
                       "eat."]},
            {"at": 1.5, "place": "turtle", "doing": "He sits by the door with his back to the wall, a second slow drink in "
                "front of him, served last.",
             "go": "The green lizardman ties off his net and climbs up onto the pier, salt dust falling from his scales."},
            {"at": 2.75, "place": "docks", "doing": "He is curled asleep in his dugout under a sailcloth, tail over his "
                "snout.",
             "go": "The lizardman leaves a copper on the table, exactly one, and goes back down to his boat."},
            {"at": 5.0, "place": "docks", "doing": "He pushes his dugout off into the grey water with the fishing fleet, "
                "standing up in it as if it were dry land."},
            {"at": 11.5, "place": "docks", "doing": "He guts his catch on the pier in the heat, fast and neat, throwing the "
                "heads to the gulls."},
            {"at": 13.0, "place": "docks", "doing": "He sleeps through the heat in the shade under the pier, half in the "
                "water."},
            {"at": 19.5, "place": "market", "doing": "He sells fish off a wet plank at the bottom of the Night Market, "
                "naming a price once and never twice."},
            {"at": 22.0, "place": "turtle", "doing": "He drinks slowly at a table by the door, back to the wall, a gutting "
                "knife on the table where everyone can see it.",
             "pay": {"to": "Bosun Maggs", "cp": 2, "for": "two drinks, served last"}},
        ],
        "beats": [
            "The green lizardman waits with his cup empty while three sailors who came in after him are served. He does "
            "not say anything. He notices.",
            "A sailor by the window says something about lizards. The green lizardman turns his head, slowly, all the "
            "way round, and looks at him until he finds his drink very interesting.",
            "The lizardman with his back to the wall tastes the air with a flick of his tongue, then looks straight at "
            "the door a moment before somebody comes through it.",
            "The green lizardman cleans his gutting knife on a rag, lays it back on the table, and squares it with the "
            "edge.",
        ],
    },

    # ---- the dwarf from Landfall -----------------------------------------------------------------------------------
    "Thoradin": {
        "look": "A dwarf, rangy for one and long in the arm, in a stained leather jerkin, a longbow unstrung beside him "
                "and leaves still caught in his beard. He keeps a small oilcloth bundle inside his shirt and touches it "
                "when he thinks no one is looking.",
        "seen_as": "the rangy dwarf with leaves in his beard",
        "brief": "You are Thoradin, a dwarven ranger from Landfall: not a Root Dwarf, and not at all like any dwarf in the "
                 "songs. Your clan kept a grove of old oaks above their hall in the hills of Öchland, and in the Age of "
                 "Cleansing the Inquisition burned it for heathen ground. You walked into the ash the next morning and "
                 "found one acorn unburned; you carry it in an oilcloth bundle against your chest. Somebody told you "
                 "the druids of Shalamar can wake a seed that has given up, and you have walked the jungle for a year "
                 "looking for one. Twice you found a ring of stones and nobody in it. You hunt for your keep, sell "
                 "hides and feathers at the Night Market, and spend almost nothing. You booked a berth on the Emerald "
                 "Eye for Catan, tonight's tide, because a trader swore there was a druid there; you have paid and you "
                 "have not decided to go. You read tracks the way other men read print: four nights ago you saw heel "
                 "marks on the pier where two men walked a third between them. You do not do small talk. You like Ssark, "
                 "the Unicorn's quiet and the elf woman who sells moon-lily tea (her tea smells of green things; you have "
                 "not asked why). You dislike walls, priests and noise. Voice: few words, flat, outdoor similes, "
                 "never a joke on purpose. 'The jungle hides them well.' 'I don't do small talk. Ask me something.'",
        "scheme": None,
        "purse": 120,
        "dialog": {
            "name|names|introduce|yourself": "\"Thoradin.\" He waits. When you wait too, he adds: \"Of nowhere, "
                "now. That's all of it.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "He nods once. \"Evening. You walk heavy on your left. "
                "Boat legs. They go in three days.\"",
            "from|home|born|landfall|ochland|came|arrived|brought": "\"Landfall. The hills of Öchland.\" He picks a leaf "
                "out of his beard and looks at it. \"Landfall is all walls and prayers. Here the trees are older than "
                "the gods.\"",
            "druid|druids|search|looking|seeking": "\"I'm looking for a druid. One who can wake a seed that's given up.\" "
                "His hand goes to his shirt. \"The jungle hides them well. Twice I found their stones and nobody home.\"",
            "acorn|seed|bundle|oak|grove|burned": "He takes out the oilcloth bundle, opens it enough to show an acorn, "
                "dark and whole, and closes it again. \"My clan's grove. The Inquisition burned it for heathen ground. "
                "This is what was left. A druid could tell me if it's dead.\"",
            "work|job|trade|hunt|hunting|ranger|hides": "\"I hunt. Hides and feathers to the Night Market, meat to whoever "
                "cooks it. It keeps me. I don't need much keeping.\"",
            "help|hire|favour|join|follow": "\"Find me my druid, and I'll walk with you three days, wherever you're "
                "going. No coin. Coin buys nothing I want.\"",
            "jungle|road|gate|trees": "\"Past the gate the road goes a long way and then stops being a road. Don't go at "
                "night. Don't go alone. Don't go if you like your feet.\"",
            "eyes|treeline|animals|jaguar|jaguars": "\"Jaguars, mostly, at the treeline. They watch the Unicorn's windows "
                "for the lamps. And something taller that I haven't named yet. It blinks less.\"",
            "tracks|track|heels|scrapes|pier|warehouse|dragged": "\"Four nights back. Two men in town boots walking a third "
                "down the pier between them, his heels dragging. Big man, by the stride he wasn't using.\" He shrugs. "
                "\"Into the bonded warehouse. Nobody came out who went in.\"",
            "catan|emerald|ship|passage|berth|tide|leave|leaving": "\"I've a berth on the Emerald Eye. Paid. A trader "
                "swore there's a druid at Catan.\" He looks at the bundle under his shirt. \"I haven't decided to go. "
                "The jungle hasn't said no yet.\"",
            "saelwyn|tea|elf|market|stall": "\"The elf in the market sells moon-lily tea. It smells of green things, "
                "growing things. Not like a kettle.\" He frowns at his cup. \"I buy one a night. I haven't asked her why "
                "it smells like that. It's rude to ask.\"",
            "sleep|bed|room|rooms|lodging|inn|stay|bunk": "\"The Unicorn, by the trees. Quiet, a copper, and they leave you "
                "be. I sleep under the trees when the bugs let me. They don't.\"",
            "drink|ale|beer|thirsty|tavern|pub": "\"The Turtle has big beer and the Unicorn has small noise. I take the "
                "Turtle and sit in the corner. Same thing, near enough.\"",
            "news|rumour|rumours|gossip|happening|word": "\"I don't trade in talk.\" He thinks. \"The officer from Landfall "
                "walks the treeline at night. Town shoes. He thinks nobody sees him. Everything sees him.\"",
            "doing|busy|tonight|plans|up": "\"Waiting for the tide, to see if I get on a ship. Then not getting on it, "
                "probably. Then the treeline at dawn.\"",
            "klhyt|mayor|founder|upriver": "\"Never met him.\" He thinks. \"They say upriver. Nobody has walked the river "
                "path in a week. I walked it yesterday. The mud would have told me.\"",
            "voss|officer|vorkath|inquisition|uniform": "His jaw sets under the beard. \"An officer of the eight arms, "
                "here. I know the cut of that coat. I watched it walk through our grove with a torch.\"",
            "ssark|lizardfolk|meters": "\"The fisherman? He doesn't talk. I like him. We sat a whole hour once and said "
                "four words between us. Best hour I've had in this town.\"",
        },
        "default_line": [
            "He nods once and says nothing, the way a tree says nothing.",
            "\"I don't do small talk.\" He sights along the unstrung bow for warp. \"Ask me something with roots.\"",
            "He picks a leaf out of his beard, turns it over, and puts it on the table between you. \"That's from the "
            "treeline. That's what I know tonight.\"",
            "\"Ask the harbourmaster. Or the lizard. Or nobody.\" His hand goes to his shirt, and away again.",
        ],
        "routine": [
            {"at": 0.75, "place": "docks", "doing": "He stands near the Emerald Eye's gangplank with his pack on and his "
                "bow strung, looking at the ship as if it were a question.",
             "go": "The dwarf straightens from the mud, wipes his hands on his jerkin and walks back toward the town and "
                   "the sea."},
            {"at": 1.25, "place": "turtle", "doing": "He sits in the Turtle Dragon's darkest corner with his pack still on, "
                "one small beer in front of him, not drinking it.",
             "go": "The rangy dwarf watches the brigantine's crew cast off, does not move, and when it is too late to move, "
                   "turns and walks back up Harbour Street."},
            {"at": 3.0, "place": "unicorn", "doing": "He is asleep in the Touchy Unicorn's cheapest room, boots on, the bow "
                "beside him.",
             "go": "The dwarf leaves his beer full and goes out toward the treeline.",
             "pay": {"to": "Wendeline Moss", "cp": 1, "for": "a room, and quiet"}},
            {"at": 5.0, "place": "treeline", "doing": "He walks the treeline in the grey dawn with his bow strung, reading "
                "the night's tracks."},
            {"at": 7.0, "place": "gate", "doing": "He goes out through the Town Gate onto the jungle road with an empty "
                "game bag, and comes back with a full one."},
            {"at": 12.0, "place": "unicorn", "doing": "He sleeps out the heat in the Unicorn, the bundle from his shirt on "
                "the pillow by his head."},
            {"at": 19.0, "place": "market", "doing": "He sells feathers and hides at the bottom of the Night Market, and buys "
                "a cup of moon-lily tea from the elf's table he drinks slowly, smelling it.",
             "pay": {"to": "Saelwyn", "cp": 3, "for": "a cup of moon-lily tea"}},
            {"at": 21.5, "place": "turtle", "doing": "He sits in the Turtle Dragon's darkest corner with his unstrung bow "
                "against the wall, listening more than drinking."},
            {"at": 23.5, "place": "treeline", "doing": "He crouches at the edge of the Treeline Road, very still, reading "
                "the mud by the light of the moon.",
             "go": "The rangy dwarf picks up his unstrung bow and goes out without a word, toward the trees.",
             "beats": ["The rangy dwarf crouches over a print in the mud by the pond, measures it with his hand, and looks "
                       "up at the treeline for a long time.",
                       "The dwarf with leaves in his beard stands with his eyes shut, listening to the jungle, and opens "
                       "them only when the animals go quiet."]},
        ],
        "beats": [
            "The rangy dwarf takes a small oilcloth bundle from inside his shirt, holds it a moment, and puts it back "
            "without opening it.",
            "The dwarf with leaves in his beard watches the Emerald Eye through the window, then the treeline in his "
            "head, and does not seem to like either.",
            "The dwarf strings his longbow, tests the draw, unstrings it, and lays it down again. Nothing has happened. "
            "He seems to feel better.",
            "Somebody starts a song about brave dwarves under mountains. The rangy dwarf with leaves in his beard "
            "gets up and moves to a table further away.",
        ],
    },

    # ---- the Turtle Dragon's keeper -------------------------------------------------------------------------------
    "Bosun Maggs": {
        "look": "A broad, one-eyed woman behind the bar, tattooed to the knuckles with anchors, whales and names, in an "
                "apron cut from old sailcloth. She moves along the bar like a deck in weather and never spills.",
        "seen_as": "the one-eyed woman in the sailcloth apron",
        "brief": "You are Bosun Maggs, keeper of the Turtle Dragon. Twenty years bosun on the Grey Widow, a whaler out of "
                 "Port Brutzee, until a harpoon line parted and took your left eye with it; the two harpoons over your "
                 "bar are off that ship, and nailed up so nobody uses them. You bought the Turtle's lease from Klhyt with "
                 "your whaling share, and you run it like a ship: beer twice the size, oysters, Scraps free with beer, "
                 "and passage to Catan booked through you for Captain DeVito, a silver to you for every berth. You make "
                 "a good living off thirsty sailors and spend it on the place, on rum, and on twenty copper of peace "
                 "money to Dominico's woman Sabeth Crane when she comes round at half past eleven. You pay because the "
                 "Turtle is all glass and you are one woman; you hate it, and you chalk every copper of it on the "
                 "underside of the bar. Ssark and his Meters drink here like anybody else, and anyone who says different "
                 "can drink in the harbour. You noticed DeVito wrote a crate into the passage book himself, paid in gold "
                 "by the Custodian's office, and you don't book cargo. You like Ssark, Teague, Captain Eirik (the best "
                 "customer on the coast) and Klhyt. You dislike Dominico, the wine, and sailors who stare at lizards. "
                 "Voice: a bosun's barks, orders not questions, calls everyone sailor. 'Drink, oysters, or a berth. "
                 "Choose.' 'Belay that, sailor.'",
        "scheme": None,
        "purse": 160,
        "dialog": {
            "name|names|introduce|yourself|bosun": "\"Maggs. Bosun Maggs. Twenty years on the Grey Widow and they "
                "still won't let me be anything else.\" She wipes the bar. \"This is my Turtle. Mind the harpoons.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"Ahoy yourself, sailor. Belly up. Beer's twice the size "
                "and so's the trouble, so drink the one and dodge the other.\"",
            "from|home|born|came|arrived|brought|whaler|widow|brutzee": "\"Port Brutzee. Twenty years bosun on a whaler, the "
                "Grey Widow, till a line parted and took this.\" She taps the patch. \"Bought the Turtle off Klhyt with "
                "my share. Best trade I ever made, and I've traded for whales.\"",
            "work|job|trade|keeper|turtle|pub|tavern": "\"I keep the Turtle. Sailors in, beer out, fights out the door "
                "smartly. And I book berths for Catan. That's my work, sailor. What's yours?\"",
            "drink|menu|price|beer|ale|wine|mead|thirsty": "\"Beer's a copper and twice the size. Mead's a copper. Wine's "
                "a copper.\" She leans in. \"Avoid the wine. I'd pour it down the harbour, but the harbour complained.\"",
            "passage|catan|ship|berth|emerald|book|leave|leaving": "\"The Emerald Eye sails for Catan on the one o'clock "
                "tide. Two gold a berth. Sign in the passage book on the bar, and don't let her captain charge you twice. "
                "He'll try. He likes gold.\"",
            "crate|cargo|custodian|devito": "She turns the passage book round and puts a tattooed finger on a line. "
                "\"See that? A crate. Paid in gold by the Custodian's office. I book berths, sailor, not cargo. DeVito "
                "wrote that in himself, and he's never written in my book before.\"",
            "oysters|food|grub|eat|hungry|scraps": "\"Oysters, three copper the plate. Caught this morning, or this week. "
                "Scraps free with beer. Grub's a copper and you'll not ask what's in it.\"",
            "lizardfolk|tension|trouble|ssark|meters|lizard": "\"Ssark and his lot drink here like anybody else. Anyone who "
                "says different can drink in the harbour.\" She looks along the bar at the window table. \"Some of them "
                "are thinking about it. I'm thinking about them.\"",
            "harpoons|harpoon|eye|patch": "\"Those harpoons are off the Grey Widow, nailed up there so nobody uses them.\" "
                "Her one eye goes flat. \"Keep it that way, sailor. I know how to take them down.\"",
            "peace|protection|sabeth|crane|fist|pay|paying": "Her jaw works. \"Half past eleven, a woman in a grey coat "
                "comes in and I give her twenty copper so the Turtle stays a Turtle.\" She raps the underside of the bar. "
                "\"I chalk every copper. One day somebody gets the bill.\"",
            "dominico|apothecary": "\"Dominico drinks in the Apothecary and sends his collectors to drink in mine.\" She "
                "spits, neatly, into a bucket. \"He's never had a drink here. He'd have to pay for it.\"",
            "sleep|bed|room|rooms|lodging|inn|stay|bunk|hammock": "\"Hammocks over the bar, four copper, and I throw out "
                "snorers. Bath's three. If you want quiet, the Unicorn by the trees. If you want bugs, the Omberhulk. If "
                "you want fleas, the Ogre. Your choice, sailor.\"",
            "news|rumour|rumours|gossip|happening|word": "\"News? The Emerald Eye's loading early and her captain won't say "
                "what. The mayor's not been in for his Thursday rum. And the window table's been eyeing Ssark all week. "
                "That's three things too many.\"",
            "doing|busy|tonight|plans|up": "\"Busy. Pour, book, throw out, pour. At the tide I see my passengers up the "
                "Emerald Eye's plank and count them so DeVito can't lose any. Then I sleep. Not long.\"",
            "klhyt|mayor|founder|upriver": "\"Klhyt has a rum here every Thursday, sits right there, tells the same joke "
                "about a whale. He missed Thursday.\" She pours a rum nobody ordered and leaves it on the bar by the "
                "empty stool.",
            "seen|missing|lost|shipmate|friend|met|anybody|anyone": "\"Name, ship and face, sailor.\" She listens, one eye "
                "half shut. \"Everyone ashore comes through my door sooner or later, mostly sooner. I'll keep the eye out. "
                "Leave a word on the slate behind the bar, and buy a beer while you write it.\"",
            "eirik|xoton|xotons|crew|sailors": "\"Eirik's the best customer on this coast: he drinks, he pays, he sings, he "
                "goes to bed. His people are another thing. Four of Amara's lot are crawling the taverns tonight. I've "
                "hidden the good glasses.\"",
        },
        "default_line": [
            "She slaps the bar. \"Drink, or move along the bar, sailor. There's a man behind you dying of thirst.\"",
            "\"Not my watch, not my business.\" She sends a mug sliding down the bar to a fisherman without looking. "
            "\"Ask the harbourmaster. He knows everything that floats, poor devil.\"",
            "She looks at you with her one eye for a long moment. \"Belay that. Ask me something a bosun would know.\"",
            "\"Can't hear you over the Xotons.\" She jerks her chin at the singing. \"Buy a beer. I hear better when "
            "I'm pouring.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "docks", "doing": "She stands at the Emerald Eye's gangplank with the passage book under "
                "her arm, counting passengers aboard one by one.",
             "go": "The one-eyed woman hands the bar to a pot-boy, tucks the passage book under her arm and goes down to "
                   "the docks.",
             "beats": ["The one-eyed woman in the sailcloth apron checks a name in the passage book, then holds the "
                       "book shut against the brigantine's small captain when he reaches for it.",
                       "The tattooed woman watches two of Dominico's men carry something down the pier, says nothing, "
                       "and counts it anyway."]},
            {"at": 1.25, "place": "turtle", "doing": "She calls the last hard hour behind the bar, throwing out the drunk "
                "and the sorry with equal care.",
             "go": "The one-eyed woman snaps the passage book shut, nods to the harbourmaster and walks back up to the "
                   "Turtle Dragon."},
            {"at": 3.0, "place": "turtle", "doing": "She sleeps in the back room behind the bar, the door open and a "
                "bung-starter in reach."},
            {"at": 8.0, "place": "turtle", "doing": "She scrubs the Turtle Dragon's floor in the morning cool, singing a "
                "whaling song very badly."},
            {"at": 11.5, "place": "docks", "doing": "She haggles with the fishermen on the pier for the morning's catch, "
                "prodding every fish with one finger.",
             "pay": {"to": "Ssark", "cp": 6, "for": "the morning's catch"}},
            {"at": 12.5, "place": "turtle", "doing": "She sleeps out the heat in the back room, shutters closed."},
            {"at": 17.0, "place": "turtle", "doing": "She opens up the Turtle Dragon, lighting lanterns among the nets and "
                "floats, and scaring the pot-boy awake."},
            {"at": 21.0, "place": "turtle", "doing": "She runs the bar like a deck in weather, a mug in each hand, one "
                "eye on the whole room."},
            {"at": 23.5, "place": "turtle", "doing": "She counts twenty copper into a grey-coated woman's palm with her jaw "
                "set, then chalks something on the underside of the bar.",
             "pay": {"to": "Sabeth Crane", "cp": 20, "for": "peace money"}},
        ],
        "beats": [
            "The one-eyed woman catches a thrown mug out of the air without looking, sets it on the bar, and points at "
            "the door. The thrower leaves.",
            "The tattooed woman pours a rum nobody ordered and sets it by an empty stool at the end of the bar. Nobody "
            "sits there.",
            "The one-eyed woman serves the lizardfolk table before the sailors by the window, slowly and on purpose, "
            "and stares down the first man who opens his mouth.",
            "The woman in the sailcloth apron glances up at the two harpoons over the bar, the way some people check "
            "that a door is locked.",
            "A Xoton at the bar says it with a Z. The one-eyed woman corrects him before anyone else can, and charges "
            "him a copper for the lesson.",
        ],
    },

    # ---- the Omberhulk's landlady ----------------------------------------------------------------------------------
    "Sister Agathe": {
        "look": "A big-boned woman in a grey wimple and a stained apron, sleeves rolled to the elbow over forearms like "
                "a baker's. A bung-starter hangs from her belt where a rosary once did, and she moves through the din "
                "as if it were a cloister.",
        "seen_as": "the big woman in the wimple",
        "brief": "You are Sister Agathe, landlady of the Omberhulk & Nun. You were a nursing sister of the Vistadine "
                 "springs in Aurelia, healing waters holy to Vorkath, until the Inquisition came to your infirmary for "
                 "three elves you were nursing. You hit an inquisitor with a bedpan and walked to the coast. You left the "
                 "order; the order hasn't noticed. The Omberhulk is loud, buggy and hot and you love it: big portions "
                 "(Beatrice, Susan and Phillip's spuds), music late, every race at every table, Gog's people paying "
                 "their way and Dominico's two ears listening by the stairs. You still heal: a cut lip, a broken head, a "
                 "fever, with a prayer you no longer believe in and hands you do. At midnight you pay twenty copper "
                 "peace money to Sabeth Crane, with very bad grace. Your scheme: you know which two men by the stairs "
                 "are Dominico's, and you feed them gossip, loud and false, so his informants carry nonsense to the "
                 "Apothecary. Right now you are sheltering Marta and her twins upstairs, rent free, and Marta is washing "
                 "your pots and waiting for Husok Sourfist with a skillet; you hope she finds him. You like the Bard, "
                 "Wendeline, Gog's people, and anyone who eats. You dislike inquisitors, Dominico, and men who leave. "
                 "Voice: cloister briskness, tavern words, 'child' to everyone, swears by the Eight. 'Eat, drink or get "
                 "out of the doorway.' 'Eight arms preserve us, child, sit down.'",
        "scheme": "Feeds Dominico's two listeners by the stairs loud, false gossip on purpose, so his informants carry "
                  "nonsense to the Apothecary.",
        "purse": 110,
        "dialog": {
            "name|names|introduce|yourself": "\"Sister Agathe.\" She wipes her hands on the apron. \"I left the "
                "order. The order hasn't noticed. Neither, thank the Eight, has the Inquisition.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"Evening, child. You're in the doorway. Everyone's always "
                "in the doorway. In or out. In's better: we've spuds.\"",
            "from|home|born|came|arrived|brought|aurelia|vistadine|springs": "\"Aurelia. The Vistadine springs, holy water, "
                "nursing sisters, very clean floors.\" She looks at her own floor. \"The Inquisition came for three "
                "elves in my infirmary. I hit an inquisitor with a bedpan and walked to the sea.\"",
            "nun|sister|order|church|vorkath|faith|pray|prayer": "\"I left the order. The order hasn't noticed.\" She "
                "touches the bung-starter where a rosary would hang. \"I still pray. I just don't expect an answer, and "
                "I keep a stick handy in case one comes.\"",
            "work|job|trade|landlady|omberhulk|keeper|tavern|pub": "\"I keep the Omberhulk & Nun. Big portions, late music, "
                "bad beds. People come here to feel alive in a crowd. I keep them alive. Mostly.\"",
            "drink|menu|price|ale|mead|wine|thirsty": "\"Ale a copper, mead two, wine two and you'll regret it. Bath four. "
                "The company's a copper and it's honest company, mind.\"",
            "sleep|bed|room|rooms|lodging|inn|stay|bunk|bugs": "\"A bed's a copper and the bugs come free. The suite's a "
                "silver and the bugs are better dressed. If you want to sleep, child, go out to the Unicorn. Nobody "
                "sleeps here. That's not what it's for.\"",
            "spuds|food|beatrice|susan|phillip|eat|hungry": "\"Beatrice, Susan and Phillip's spuds. Three copper. Don't ask "
                "which is which. Beatrice is the crispy one. Don't tell Susan.\"",
            "heal|healing|hurt|wound|wounded|cut|sick|fever|medicine": "\"Sit down. Show me.\" She is already rolling her "
                "sleeves higher. \"Nursing sister, twenty years. I've stitched worse in better light. A copper for the "
                "thread, and you'll say thank you.\"",
            "informants|listening|stairs|ears|dominico|spies": "She jerks her head at the stairs without looking. \"Them "
                "two? Dominico's ears. They pay for their drinks, so.\" Her mouth twitches. \"I tell them things. Loud. "
                "Mostly lies. They write it all down.\"",
            "gog|fat|guild": "\"Gog's people drink here, and they pay. Gog looks after this town, whatever else he does, "
                "and he sends flowers when somebody dies. Real ones.\"",
            "bard|music|moonport|song|songs": "\"The Bard of Moonport, nightly, when he's in town and sober and owes me "
                "rent. His voice cuts through this lot like a knife through butter. Then he wanders off to every other "
                "tavern in town to be unfaithful.\"",
            "marta|twins|husok|sourfist|baby|babies|children": "Her face goes very calm, which is worse. \"Marta and her "
                "twins have my back room, free, and Marta has my biggest skillet. If you see Husok Sourfist, child, tell "
                "him the Omberhulk is the safest place in town.\" A pause. \"Tell him that.\"",
            "custodian|hall|dues|notice": "\"The Custodian?\" She sniffs. \"Never set foot in my place. Too many bugs, too "
                "many honest people.\" She wipes a table hard. \"He writes a lovely notice. Klhyt never wrote a lovely "
                "notice in his life, and every one of them was true.\"",
            "peace|protection|sabeth|crane|fist|pay|money": "\"At the midnight bell a woman in a grey coat comes for twenty "
                "copper, and I give it to her, and I say a prayer for her, and it is not a kind prayer.\"",
            "news|rumour|rumours|gossip|happening|word": "\"What I hear, child, I hear by the stairs, and half of it I said "
                "first.\" She lowers her voice. \"The true half: the mayor hasn't been to Gog's in four nights, and Gog's "
                "people have stopped laughing.\"",
            "doing|busy|tonight|plans|up": "\"Feeding people. Throwing some of them out. At midnight paying for the privilege "
                "of not having my windows broken. Then mopping. The Eight made mops for a reason.\"",
            "klhyt|mayor|founder|upriver": "\"Upriver.\" She snorts. \"Klhyt stood in that doorway the night I opened and "
                "said 'Agathe, nobody here will ever ask where you came from.' He'd not go upriver without telling a "
                "soul. He's a talker.\"",
            "elves|elf|inquisition|voss|officer": "Her bung-starter comes off the belt and goes on the bar, gently. \"If a "
                "man in a pressed uniform comes in here asking after elves, child, he'll find I've no elves and a very "
                "heavy stick.\"",
        },
        "default_line": [
            "She crosses her arms. \"Eat, drink or get out of the doorway, child. The Eight love you, but they love "
            "you outside.\"",
            "\"Ask the Bard. He knows everything and sings half of it.\" She is already turning to bellow at the kitchen. "
            "\"MARTA. SPUDS.\"",
            "She looks you up and down the way a nurse looks at a wound. \"You're asking the wrong woman, and you look "
            "hungry. Sit.\"",
            "\"I've a room full of drunks and two of Dominico's ears by the stairs, child. Say it quieter, or say it to "
            "someone else.\"",
        ],
        "routine": [
            {"at": 0.0, "place": "omberhulk", "doing": "She stands at the bar with her arms folded while the midnight bell "
                "rings, counting coins into a grey-coated woman's palm as if each one were a tooth.",
             "pay": {"to": "Sabeth Crane", "cp": 20, "for": "peace money, with bad grace"},
             "beats": ["The big woman in the wimple counts twenty copper into a stranger's palm, then says a prayer over "
                       "the hand, very quietly, that makes the stranger snatch it away.",
                       "The woman in the wimple says something loud by the stairs about Fat Gog hiring thirty Xotons for "
                       "midnight. One of the two men by the stairs writes it down. She winks at the kitchen."]},
            {"at": 0.5, "place": "omberhulk", "doing": "She works the room with a jug in one hand and the bung-starter in the "
                "other, stitching a sailor's eyebrow between pours."},
            {"at": 2.5, "place": "omberhulk", "doing": "She throws the last drinkers out into the square one by one, "
                "blessing each of them on the way out the door."},
            {"at": 3.5, "place": "omberhulk", "doing": "She sleeps in a chair by the kitchen door, the bung-starter across "
                "her knees, the back room's door open a crack."},
            {"at": 8.0, "place": "omberhulk", "doing": "She scrubs tables and peels a mountain of spuds, telling Beatrice "
                "from Susan by touch."},
            {"at": 12.5, "place": "omberhulk", "doing": "She sleeps through the heat upstairs, shutters closed, a wet cloth "
                "over her eyes."},
            {"at": 17.5, "place": "square", "doing": "She fills two buckets at the town pump and carries them back without "
                "spilling, nodding to everyone and stopping for no one."},
            {"at": 18.5, "place": "omberhulk", "doing": "She lights the lamps and the cookfires, and sets the spuds on to "
                "boil in a pot the size of a font."},
            {"at": 21.0, "place": "omberhulk", "doing": "She runs the Omberhulk like an infirmary in a riot, a jug in one "
                "hand and the bung-starter on her belt."},
        ],
        "beats": [
            "The big woman in the wimple breaks up a fight by taking both men by the ear, walks them to the door, and "
            "comes back wiping her hands on her apron.",
            "The woman in the wimple binds a cut hand at the bar with clean linen and a few muttered words. The bleeding "
            "stops faster than it should.",
            "The landlady in the wimple chalks HUSOK on the slate behind the bar, under the prices, and draws a very "
            "neat line under it.",
            "A pot crashes in the kitchen. The big woman in the wimple calls through the door, \"All right, Marta, "
            "love?\" and gets a short, grim answer.",
        ],
    },

    # ---- the Bard --------------------------------------------------------------------------------------------------
    "The Bard of Moonport": {
        "look": "A narrow man in a peacock-blue coat gone shiny at the elbows, with a lute older than he is, its bowl "
                "cracked and mended with fish glue. He tunes between songs with his head on one side, as if the lute "
                "were telling him a secret.",
        "seen_as": "the narrow man in the peacock coat",
        "brief": "You are the Bard of Moonport, and you never give your real name (it is Peregrine Vane, and your "
                 "father is a magistrate in Moonport who would like you home and quiet). You left Moonport with a lute, "
                 "a coat and a reputation; the reputation got here first. Requests cost a copper, insults two; Klhyt's "
                 "Ballad is free because nobody has asked for it since he went 'upriver'. You play the Omberhulk & Nun "
                 "nightly, Sister Agathe's house, for a copper bed and supper, then wander the town's other taverns "
                 "through the night for more coppers, and you spend them as fast. Tonight a siren sings at the "
                 "Stripperwitch and you are going to stand at the back and hate how good she is. A bard hears "
                 "everything: you know the Custodian goes in the Stripperwitch's side door, that Husok is dodging Marta, "
                 "that Dominico's ears drink by Agathe's stairs. You remember the night Klhyt stood on a table at the "
                 "Omberhulk and sang his own ballad, badly, all eleven verses. Your scheme: you are writing a new ballad "
                 "about the missing mayor, and mean to sing it on the Town Hall steps at dawn whether it is true or not, "
                 "to see who flinches. You like Agathe, Klhyt, River and an audience; you dislike the Custodian, critics, "
                 "and silence. Voice: florid, quick, rhymes by accident, turns everything into a lyric. 'Requests a "
                 "copper, insults two.' 'Odd, that. Odd enough for a verse.'",
        "scheme": "Writing a ballad of the missing mayor to sing on the Town Hall steps at dawn, true or not, to see who "
                  "flinches when they hear it.",
        "purse": 30,
        "dialog": {
            "name|names|introduce|yourself": "He bows from the waist, lute and all. \"The Bard of Moonport. A name "
                "is a song with one note, and I've too many notes for that.\" He winks. \"You may call me Pip. Nobody "
                "else does.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "He strums a bright chord at you. \"Good evening, good "
                "stranger, good fortune and good grief. You've the look of a request. A copper, and I'll make it rhyme.\"",
            "from|home|born|moonport|came|arrived|brought": "\"Moonport is a long way from here. That's the best thing about "
                "it.\" He tunes a string a hair sharp. \"My father's a magistrate there. He sentenced me to a quiet life. "
                "I appealed, by boat.\"",
            "work|job|trade|bard|play|playing|perform": "\"I play the Omberhulk for my bed and my spuds, then the rest of "
                "the town for my sins. Six taverns, six towns, one lute. A copper a song, two an insult.\"",
            "song|songs|music|sing|request|tune|lute": "He plucks a chord. \"Requests cost a copper. Insults cost two. "
                "Klhyt's Ballad is free, because nobody's asked for it since he went upriver.\"",
            "klhyt|ballad|mayor|founder|upriver": "\"Klhyt's Ballad. 'He came ashore with the salt in his beard.' Eleven "
                "verses. He sang them all once, on a table, badly, and the table broke on the tenth.\" The chord goes "
                "minor. \"Nobody wants it this week. Odd, that. Odd enough for a verse.\"",
            "gossip|news|rumour|rumours|happening|word": "\"The Custodian's been seen at the Stripperwitch. Again. He's "
                "never been there. Ever.\" A wink. \"Through the side door, collar up, every night this week, like a man "
                "in a song about a man who shouldn't.\"",
            "siren|stripperwitch|singer|voice": "His face does something complicated. \"There's a siren singing at the "
                "Stripperwitch tonight. She sings once and they forget their debts. I sing every night and they remember "
                "them.\" He sighs. \"I'm going to stand at the back and hate her. Come and hate her with me.\"",
            "verse|verses|writing|new|missing": "\"I'm writing a new one. 'The Mayor Who Wasn't Upriver.' I have the tune "
                "and two rhymes for 'Custodian'.\" He leans in. \"Neither of them is kind. I'll sing it on the Town Hall "
                "steps at dawn and watch who flinches.\"",
            "custodian|hall": "\"The Custodian smiles with half his mouth. The other half, I think, is saving itself for "
                "the truth. It may wait a long time.\"",
            "husok|sourfist|marta|twins": "He grins and plays four notes of a lullaby. \"Husok Sourfist is the only man in "
                "town who knows every back alley, every crate, and every rain barrel big enough to hide in. Marta's in "
                "Agathe's kitchen with a skillet. Tragedy or comedy? I'll know by the end.\"",
            "agathe|sister|omberhulk|nun": "\"Sister Agathe feeds me, beds me and insults me, and I'd die for her, which "
                "she says would at least be quieter.\"",
            "sleep|bed|room|rooms|lodging|inn|stay|bunk": "\"Sleep? At the Omberhulk you sleep with the bugs and the music. "
                "If you want silence, the Unicorn, out by the trees, where the books are and the jokes aren't.\"",
            "drink|ale|beer|thirsty|tavern|pub": "\"Buy me one and I'll tell you where. The Omberhulk for company, the "
                "Turtle for size, the Ogre for regret, the Apothecary for money, and the Stripperwitch if you want to be "
                "seen by people who aren't there.\"",
            "doing|busy|tonight|plans|up": "\"Tonight? The Omberhulk till the siren rises, the Stripperwitch to suffer, the "
                "Ogre for coppers, the Turtle to sing shanties at Xotons, and the square at three to write it all down "
                "before I forget it.\"",
            "dominico|fist|ears|informants": "He plays three heavy notes, very low. \"Dominico. A song I don't sing. His "
                "ears drink by Agathe's stairs and I play them a little tune every night about how much I love the "
                "peace.\"",
            "elves|elf|voss|officer": "\"An officer from Landfall eats steak at the Apothecary and asks after elves. I have "
                "been composing an insult for him. It's two copper, and he'll never pay it, so I'll have to give it "
                "away.\"",
        },
        "default_line": [
            "He tunes a string and listens to it instead of you. \"Hm. Flat. Like that question. Try another, a "
            "copper's worth.\"",
            "He plays a little run of notes that sounds exactly like someone changing the subject. \"Ask Sister Agathe. "
            "She knows everything I know, and she knows it first.\"",
            "\"That, my friend, is a verse I haven't written yet.\" He scribbles something on his cuff. \"Come back at "
            "dawn. Town Hall steps.\"",
            "He strikes a heroic chord. \"A fine question! A copper, and I'll pretend I know the answer, beautifully.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "ogre", "doing": "He plays dirty songs on an upturned barrel for the crownies, catching "
                "thrown coppers in his hat between verses.",
             "go": "The narrow man in the peacock coat slips out of the Stripperwitch with his lute and a strange look "
                   "on his face, humming something he will never be able to sing.",
             "beats": ["The narrow man in the peacock coat plays a song about a fat lizard and a thin clerk. The crownies "
                       "laugh in the right places. Nobody says the names.",
                       "The man with the cracked lute catches a thrown copper in his hat without missing a note, and "
                       "plays the next verse louder for it."]},
            {"at": 1.5, "place": "turtle", "doing": "He stands on a bench in the Turtle Dragon leading a sea shanty, losing "
                "the tune to whichever Xoton is loudest.",
             "go": "The man in the peacock coat tips his hat to the crownies, counts his coppers twice, and goes down "
                   "toward Harbour Street."},
            {"at": 2.5, "place": "square", "doing": "He sits on the edge of the pump trough under the Town Hall's lamps, "
                "writing verses on his cuff and crossing them out.",
             "go": "The narrow man in the peacock coat hands the shanty to the Xotons, who do not notice, and wanders off "
                   "uphill with his lute."},
            {"at": 3.5, "place": "omberhulk", "doing": "He is asleep upstairs in a copper bed, the lute in the bed beside "
                "him, the bugs undisturbed.",
             "go": "The man in the peacock coat folds his cuff over his verses and wanders back across the square to the "
                   "Omberhulk.",
             "pay": {"to": "Sister Agathe", "cp": 1, "for": "a bed for the night"}},
            {"at": 13.0, "place": "omberhulk", "doing": "He sits in the empty Omberhulk with his lute and a cup of water, "
                "playing the same four bars over and over."},
            {"at": 17.5, "place": "square", "doing": "He busks by the town pump for the evening errand crowd, hat on the "
                "cobbles, singing the news."},
            {"at": 20.0, "place": "market", "doing": "He plays among the Night Market's stalls for coppers and mangoes, "
                "making up verses about whoever stops."},
            {"at": 21.5, "place": "omberhulk", "doing": "He plays the Omberhulk & Nun from a stool by the fire, his voice "
                "cutting through the din like a knife."},
            {"at": 23.5, "place": "stripperwitch", "doing": "He stands at the back of the Stripperwitch with his lute "
                "hanging silent from his hand, listening to the stage as if it hurt.",
             "go": "The narrow man in the peacock coat stops in the middle of a verse, says \"The siren,\" to no one, and "
                   "hurries out across the square.",
             "pay": {"to": "River", "cp": 2, "for": "a mead to suffer with"}},
        ],
        "beats": [
            "The narrow man in the peacock coat takes a request, a copper on the table, and sings Klhyt's Ballad. The "
            "room goes quiet on the second verse and stays quiet.",
            "The man with the cracked lute leans toward two men by the stairs and sings them a verse about how peaceful "
            "and well run the town is. They do not know whether to laugh.",
            "The narrow man in the peacock coat stops mid-song, scribbles a line on his cuff, and starts again from the "
            "beginning as if nothing happened.",
            "The man in the peacock coat plays four bars of a lullaby, looks at the door to the kitchen, and laughs to "
            "himself.",
        ],
    },

    # ---- the Rampant Ogre's barman ---------------------------------------------------------------------------------
    "Big Ludo": {
        "look": "A Jonulvicha built like a door, bald as an egg, one tusk broken off short. He fills the space behind a "
                "bar made from a ship's door, and when he leans on it the whole thing creaks.",
        "seen_as": "the huge barman with the broken tusk",
        "brief": "You are Big Ludo, a Jonulvicha, barman of the Rampant Ogre & Curved Cleaver and one of its crownies, "
                 "the regulars who don't want a scene. You came off the Öchland frontier camps and fought in pits for "
                 "other men's money until Fat Gog bought out your last fight. You lost it on purpose, the way you were "
                 "paid to; Gog knew, and paid you anyway, and gave you this bar. The tusk went in that fight. The Ogre is "
                 "Gog's place, near enough: you hold the lease and Gog holds your marker, and you would walk into the "
                 "harbour for him. Everything costs a copper; rooms four; the Honeymoon Suite is three dog pelts and a "
                 "bed, chickens extra. You make a thin living and pay twenty copper peace money to Sabeth Crane at eleven "
                 "because Gog told you to keep the Ogre quiet tonight. Your scheme: Dominico's off-duty muscle drink here, "
                 "Tully loudest, and you water their rum and listen, and send what they say up to the Stripperwitch by "
                 "Wick, a copper a message. You heard Tully laugh about a crate that grumbles. You like Gog, Kael Ironjaw "
                 "(pays, fights fair), Husok (owes you four coppers, makes you laugh), the Bard. You dislike scenes, "
                 "Brask and anyone who touches the dice cup. Voice: very few words, each one picked; you answer real "
                 "questions, just short, and your hands do the rest. 'Copper. Everything.' 'You behave.'",
        "scheme": "Waters the rum of Dominico's off-duty men, listens to them brag, and sends what he hears to Fat Gog by "
                  "the street child Wick, a copper a message.",
        "purse": 80,
        "dialog": {
            "name|names|introduce|yourself": "He points at himself with a thumb like a mallet. \"Ludo.\" A pause. "
                "\"Big Ludo. There was a Little Ludo. He left.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "He looks down at you from a long way up and nods once. "
                "\"Evening. Sit where you like. Not there.\" He points. \"That's Husok's.\"",
            "from|home|born|ochland|frontier|came|arrived|brought": "\"Frontier camps. Öchland.\" He rubs the broken tusk. "
                "\"Fought in pits. Lost the last one. On purpose. Gog paid anyway.\" He shrugs, which takes a while. "
                "\"Got a bar.\"",
            "work|job|trade|barman|ogre|keeper|tavern": "\"Pour. Watch. Throw out.\" He holds up three fingers, then "
                "folds one down. \"Mostly watch.\"",
            "drink|menu|price|rum|ale|beer|thirsty|mead": "\"Everything's a copper. Everything.\" He sets down a mug that "
                "is not quite clean. \"Rum's best. Ale's wet.\"",
            "seen|missing|friend|shipmate|mate|lost|met|anybody|anyone": "He thinks about it, properly, eyes up at the "
                "rafters. \"Xotons. Ten in tonight. Short. Loud. Look the same from up here.\" He leans down. \"Ask "
                "the singing ones. Dayo's lot. They know every Xoton ashore.\"",
            "xoton|xotons|dayo|imani|crew|sailors|arm": "\"Four of them. Crawling the taverns. Turtle, here, Omberhulk.\" "
                "He looks at his bar. \"They break things. They pay for things. Watch comes after. Too late.\"",
            "crownies|crownie|regulars": "\"Crownies are regulars. Regulars don't want a scene.\" He looks at you for a "
                "long time. \"You want a scene?\"",
            "gog|guild|fat|stripperwitch": "\"This is Gog's place. Near enough.\" He touches his broken tusk, the way some "
                "men touch a holy medal. \"You behave.\"",
            "husok|twins|sourfist|marta": "\"Husok? Owes a woman an explanation and two children a father. Owes me four "
                "coppers.\" Something like a smile under the tusk. \"Coppers first.\"",
            "suite|honeymoon|room|rooms|sleep|bed|lodging|stay|bunk": "\"Room's four coppers. Honeymoon Suite's four "
                "coppers. Three dog pelts and a bed.\" He counts on his fingers. \"Chickens extra. Fleas free.\" He "
                "jerks his head uphill. \"Want clean, go to the Unicorn.\"",
            "dice|game|bet|gamble|cup": "\"Dice are on the table. House doesn't take a cut.\" He cracks one knuckle. "
                "\"House doesn't need to.\"",
            "tully|brask|dominico|fist|muscle": "He wipes the bar in a slow circle. \"Dominico's boys drink here off duty. "
                "Rum. Lots.\" The circle goes the other way. \"I pour weak. They talk strong.\"",
            "crate|warehouse|grumbles": "His cloth stops. \"Tully says a crate grumbles.\" He starts wiping again. \"Crates "
                "don't grumble. Tell Gog. Not me. I'm a barman.\"",
            "news|rumour|rumours|gossip|happening|word": "\"Mayor's gone four nights. Gog's gone quiet. Tully's buying "
                "rounds with money he hasn't got.\" He looks at you. \"That's news.\"",
            "doing|busy|tonight|plans|up": "\"Pouring.\" He pours. \"At eleven, a woman comes. I pay. At midnight, "
                "trouble, maybe. After, I sweep.\"",
            "peace|protection|sabeth|crane|pay|money": "\"Twenty copper. Every night. Grey coat.\" His big hand closes on "
                "the bar. \"Gog says pay. I pay.\"",
            "custodian|hall|dues|skim": "He snorts through his nose. \"Never drinks here. Skims, they say.\" He sets down a "
                "mug hard. \"Gog knows. Ask Gog.\"",
            "kael|ironjaw|glaive|hat": "\"Kael. Jonulvicha, like me. Loud, unlike me. Pays. Fights fair.\" A nod. \"Good "
                "customer.\"",
            "klhyt|mayor|founder|upriver": "He stops pouring. \"Klhyt drank here. Once. Said the Ogre was honest.\" He "
                "starts pouring again. \"Nobody said that before. Find him.\"",
        },
        "default_line": [
            "He grunts, sets a mug of rum in front of you you did not order, and taps the bar once: a copper.",
            "\"Don't know.\" He looks at the dice table, then at you. \"Ask them. They know everything. They lie about "
            "half.\"",
            "\"Mm.\" He leans on the bar until it creaks. \"Ask Gog. He knows. I pour.\"",
            "He holds up one finger, finishes throwing a man out by the belt, comes back and lowers the finger. \"Again. "
            "Slower.\"",
            "\"Not my business.\" He wipes the bar. \"My business is the bar. You're leaning on it.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "ogre", "doing": "He leans on the bar over a table of Dominico's off-duty men, pouring "
                "their rum slow and weak, listening with his eyes half shut.",
             "pay": {"to": "Wick", "cp": 1, "for": "carrying a word to the Stripperwitch"},
             "beats": ["The barman with the broken tusk pours a round for Dominico's men from a bottle he keeps under the "
                       "bar, a little water in each, and laughs at their joke a moment late.",
                       "The huge barman bends and murmurs something to a ragged child at the back door, presses a copper "
                       "into the small hand, and the child is gone."]},
            {"at": 2.5, "place": "ogre", "doing": "He sweeps sawdust and spilled rum into the gutter, then throws the last "
                "drinker out after it, gently."},
            {"at": 3.5, "place": "ogre", "doing": "He sleeps on a pallet behind the bar, one hand on his cudgel, snoring "
                "like a stuck door."},
            {"at": 9.5, "place": "docks", "doing": "He rolls rum barrels up off a Xoton boat two at a time, one under each "
                "arm, saying nothing to anyone."},
            {"at": 11.5, "place": "ogre", "doing": "He sleeps out the heat behind the bar, the shutters down."},
            {"at": 18.0, "place": "ogre", "doing": "He opens the Ogre's door, kicks fresh sawdust over yesterday's, and "
                "sets the dice cup on the corner table."},
            {"at": 21.0, "place": "ogre", "doing": "He stands behind a bar made of a ship's door, pouring, watching the "
                "dice game, saying almost nothing."},
            {"at": 23.0, "place": "ogre", "doing": "He counts twenty copper onto the bar for a grey-coated woman without a "
                "word, then wipes the bar where the coins were.",
             "pay": {"to": "Sabeth Crane", "cp": 20, "for": "peace money"}},
        ],
        "beats": [
            "The barman with the broken tusk throws a drunk out by the collar, then wipes the spot on the bar where the "
            "drunk had been.",
            "Someone reaches for the dice cup with the wrong hand. The huge barman puts one finger on the cup. The man "
            "takes his hand back.",
            "The huge barman pours a rum for an empty stool, looks at it, and drinks it himself.",
            "The barman with the broken tusk listens to a red-faced bruiser boast about a crate, polishes the same mug "
            "for a long time, and sets it down very carefully.",
        ],
    },

    # ---- the man who left ------------------------------------------------------------------------------------------
    "Husok Sourfist": {
        "look": "A sour-faced man of about thirty with a mouth like a drawstring purse, cooper's calluses on both hands "
                "and sawdust in his hair. He sits where he can see the door and jumps every time it opens.",
        "seen_as": "the sour-faced man watching the door",
        "brief": "You are Husok Sourfist, a cooper, and everyone in Klhyts Refuge knows what you did: you told Marta you "
                 "loved her at the harvest dance at the Omberhulk, and you meant it, at the time. Then she said 'twins'. "
                 "You came over from Aurelia three years ago with an apprentice's tools and a habit of leaving. Now Marta "
                 "and the twins are at the Omberhulk, Sister Agathe has given them a room and a skillet, and it is on "
                 "the notice board in the square. You hide. You know every back alley, rain barrel, net pile and woodshed "
                 "in town. You mend barrels for the docks and the Ogre when sober, earn a few coppers, and drink them. "
                 "You owe Big Ludo four coppers. Your scheme: borrow two gold from anyone soft-hearted enough, buy a berth "
                 "on the Emerald Eye, and be in Catan by morning. Your secret: some mornings you stand at the corner of "
                 "the square where you can see the Omberhulk's kitchen window, for a minute, and look at the twins, and "
                 "then you run. Three nights ago you tried to hide in the bonded warehouse and the big man threw you out, "
                 "but not before you heard someone inside humming Klhyt's Ballad. You like Ludo (credit) and the Bard "
                 "(keeps your hiding places secret, mostly). You fear Marta, Agathe, skillets and being a father. Voice: "
                 "self-pitying, quick, blames the world, lies badly. 'I did! At the time.' 'Twins, she says. Twins.'",
        "scheme": "To borrow two gold off anyone soft enough, buy a berth on the Emerald Eye and be in Catan by morning, "
                  "away from Marta and the twins.",
        "purse": 6,
        "dialog": {
            "name|names|introduce|yourself|sourfist": "\"Husok.\" He glances at the door. \"Sourfist. It's a family "
                "name. The fist came first. The sour came later.\" He drinks. \"You're not from the Omberhulk, are you?\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "He jumps. \"Gods. Don't creep up.\" He looks past you at "
                "the door. \"Evening. Is she out there? Big woman? Skillet?\"",
            "from|home|born|aurelia|came|arrived|brought": "\"Aurelia. Little cooper's village, nothing in it but barrels and "
                "mothers.\" He shrugs. \"Came over three years back. Fresh start. Seemed fresh at the time.\"",
            "work|job|trade|cooper|barrel|barrels|mend": "\"Cooper. I mend barrels. Ruk's crew at the docks, Ludo's rum "
                "kegs.\" He looks at his calluses. \"Good hands. Everyone says. Shame about the rest of me.\"",
            "twins|woman|love|children|marta|baby|babies|father": "\"I told her I loved her. I did! At the time.\" He drinks. "
                "\"Twins, she says. Twins.\" He looks at the bottom of the cup. \"One's got my ears. Somebody told me. I "
                "didn't look. I didn't.\"",
            "help|fix|lend|loan|borrow|gold|money": "He brightens horribly. \"Help? You could lend me two gold. For a berth. "
                "For the twins, really, if you think about it: they're better off.\" He wilts. \"Or tell her I died. Tell "
                "her I went upriver, like the mayor.\"",
            "hide|hiding|dodge|dodging|alley|alleys|woodshed|escape": "\"I know every rain barrel in this town that'll take a grown "
                "man. Four. And every net pile at the Turtle, and Ruk's woodshed in the lanes.\" He lowers his voice. \"Don't "
                "tell the Bard I told you. He's writing a song.\"",
            "warehouse|crate|bonded|humming|hum|brask": "\"Tried to hide in the bonded warehouse three nights back. Nice and "
                "quiet.\" He shivers. \"The big man threw me out. But before he did, I heard somebody in there humming. "
                "Klhyt's Ballad. In the dark.\" He drinks. \"Don't tell anyone. They'll think I'm drunk. I was.\"",
            "omberhulk|agathe|sister|nun": "\"Don't say that word.\" He sinks in his seat. \"The nun's on her side. The nun "
                "has a stick. The nun put it on the notice board. In the square. In chalk.\"",
            "notice|board|square": "\"'HUSOK SOURFIST, YOU KNOW WHAT YOU DID.' I do know. That's the trouble. Everybody "
                "knows. The whole town reads that board.\" He hunches. \"Nobody believes it, except that bit.\"",
            "ludo|owe|debt|coppers": "\"I owe Ludo four coppers. I'll pay him. I've got,\" he checks, \"some of it.\" He "
                "puts one copper on the bar like a sacrifice. \"Ludo's a good man. Doesn't ask questions. Doesn't talk at "
                "all, really.\"",
            "sleep|bed|room|rooms|lodging|inn|stay|bunk": "\"Not the Omberhulk. Gods, not the Omberhulk.\" He thinks. \"Ludo's "
                "Honeymoon Suite, if you like fleas. The Unicorn out by the trees, if you like quiet and being judged. I "
                "sleep in a woodshed. Nobody looks in woodsheds.\"",
            "drink|ale|beer|thirsty|tavern|pub|rum": "\"Here. The Ogre. Everything's a copper and nobody's wife comes "
                "in.\" He glances at the door. \"Usually.\"",
            "news|rumour|rumours|gossip|happening|word": "\"News? I'm the news. Have you seen the board?\" He sulks. \"Fine. "
                "The mayor's gone. Everyone's whispering about it. Which means nobody's whispering about me, which is "
                "the first good thing that's happened all week.\"",
            "doing|busy|tonight|plans|up": "\"Drinking. Then hiding. Then drinking somewhere else.\" He counts on his "
                "fingers. \"Ogre, Harbour Street, Turtle, the boats, back here. She never comes to the docks. She gets "
                "seasick looking at them.\"",
            "klhyt|mayor|founder|upriver": "\"Upriver. That's a good one.\" He snorts into his cup. \"I'm going to use that. "
                "When Marta asks, I went upriver, like the mayor.\" He frowns. \"Mind, the mayor never ran from anything in "
                "his life. Big man. Stood his ground. Show-off.\"",
            "catan|emerald|ship|passage|berth|leave|leaving": "\"Catan. The one o'clock tide. Two gold a berth.\" He "
                "looks at his coins. \"I've got three coppers and a dream. If you'd lend me the difference, I'd remember "
                "you in my prayers. I don't pray. I'd start.\"",
        },
        "default_line": [
            "He glares into his rum. \"What? No. I don't know anything about that. I don't know anything about "
            "anything. Ask me if I've got twins.\" A pause. \"Don't.\"",
            "He jumps as the door opens, sees it isn't her, and sags. \"Sorry. What? Ask Ludo. Ludo knows things. Ludo "
            "doesn't tell anyone, but he knows them.\"",
            "\"I'm not here.\" He pulls his collar up. \"If anybody asks. Especially a woman. Especially with a skillet.\"",
            "\"That's not my problem.\" He drinks. \"I've got two problems. They're about this high.\" He holds a hand "
            "out, low, and looks at it, and puts it away.",
        ],
        "routine": [
            {"at": 0.0, "place": "turtle", "doing": "He crouches at the back of the Turtle Dragon behind a heap of nets and "
                "floats, a beer he can't afford cupped in his hands.",
             "go": "The sour-faced man hears a woman's voice in the street, ducks out of the chandler's doorway and "
                   "slips down Harbour Street toward the Turtle Dragon.",
             "beats": ["Behind the nets at the back of the Turtle, the sour-faced man startles at the midnight bell as if "
                       "it had been rung for him personally."]},
            {"at": 0.75, "place": "docks", "doing": "He sits between two fishing boats on the pier with his knees up, "
                "staring at the Emerald Eye like a man looking at a shop window.",
             "go": "The sour-faced man crawls out from behind the nets, checks the street both ways, and scuttles down to "
                   "the docks."},
            {"at": 1.5, "place": "ogre", "doing": "He is back at his stool in the Ogre, watching the door, sure that "
                "everyone in town is asleep but him.",
             "go": "The man with the drawstring mouth watches the brigantine slip her lines without him, says a short "
                   "bad word, and trudges back up Harbour Street.",
             "pay": {"to": "Big Ludo", "cp": 1, "for": "a rum, and a copper off the four he owes"}},
            {"at": 2.75, "place": "lanes", "doing": "He sleeps curled in a woodshed at the far end of the Back Lanes, as far "
                "from the Omberhulk as the town allows.",
             "go": "The sour-faced man finishes his rum, peers out of the door for a long time, and creeps off into the "
                   "dark lanes."},
            {"at": 6.0, "place": "square", "doing": "He stands at the corner of the square in the grey dawn, very still, "
                "looking at the Omberhulk's kitchen window.",
             "beats": ["The sour-faced man at the corner of the square takes one step toward the Omberhulk, then two "
                       "steps back, then runs."]},
            {"at": 6.25, "place": "docks", "doing": "He mends a split barrel on the pier for the stevedores, mallet and "
                "hoops, working fast and well and not talking."},
            {"at": 12.0, "place": "lanes", "doing": "He sleeps through the heat in the woodshed in the Back Lanes."},
            {"at": 17.5, "place": "ogre", "doing": "He mends a rum keg in the Ogre's yard for a copper and a drink, one eye "
                "on the alley."},
            {"at": 21.0, "place": "ogre", "doing": "He hunches over a rum he isn't enjoying at the end of the Ogre's bar, "
                "watching the door."},
            {"at": 23.25, "place": "harbour", "doing": "He stands pressed into a shuttered chandler's doorway on Harbour "
                "Street, peering uphill toward the square.",
             "go": "The sour-faced man hears someone say 'Marta' at the next table, goes white, and is out of the door "
                   "before his stool stops rocking."},
        ],
        "beats": [
            "The door opens. The sour-faced man is under his table before he sees it is only a Xoton. He climbs back "
            "out, dusting his knees, and glares at anyone who saw.",
            "The man with the drawstring mouth counts his coppers on the bar, three of them, and counts them again as "
            "if there might be more.",
            "The sour-faced man asks a stranger at the bar how much a berth to Catan costs, hears the answer, and puts "
            "his head down on the bar.",
            "The man watching the door hums four bars of a lullaby without seeming to know he is doing it, and stops "
            "when he notices.",
        ],
    },

    # ---- the thief out of Malice -----------------------------------------------------------------------------------
    "Hanklevode": {
        "look": "A lean man in a long coat with far too many pockets, clean-shaven and quick-eyed, with long, clever "
                "hands that never quite stop moving. A coin walks across his knuckles and back while he looks at "
                "everything except it.",
        "seen_as": "the lean man in the many-pocketed coat",
        "brief": "You are Hanklevode, a human mercenary thief, new in from Malice, the Smith's fortress-city in the "
                 "jungle valley. You were a locksmith's apprentice in a Landfall port; the first lock you ever picked was "
                 "your mother's sewing box, with her own hairpin, to find the copper she had hidden for your birthday. "
                 "In Malice you made locks for the Smith's forge, which is how you know them from the inside, and you "
                 "left when the Smith's people wanted you to swear to him: swearing doesn't pay. You live on what you "
                 "can open and what Marlo on Harbour Street will fence, and you are down to sixty copper. You hire out "
                 "at two gold a day: doors, not blood, and never against Dominico. Your scheme: everybody says the "
                 "Custodian skims, and skimmed money has to live somewhere, so you have decided it lives behind the "
                 "locked door of the mayor's study at the back of the Town Hall. While the Custodian sits in the "
                 "Stripperwitch's red booth you mean to pick that lock (a good brass one) and find out; you have paid "
                 "Constable Rosa Quint five copper a night to be looking the other way. You have also measured the "
                 "bonded warehouse's padlock with your eye: Landfall-made and cheap, but the bruiser outside is not. You "
                 "like Ludo (cheap, quiet), Marlo (fair, for a fence) and the Bard. You fear blood, oaths, and Dominico's "
                 "friendliness. Voice: smooth, wry, all euphemism: doors, opportunities, quiet; never says 'steal'. "
                 "'Doors, then. Quietly.' 'I'm looking for opportunities.'",
        "scheme": "To pick the lock of the mayor's study at the back of the Town Hall while the Custodian is at the "
                  "Stripperwitch, sure that the skimmed money is hidden in there; Constable Rosa Quint is paid to look "
                  "the other way.",
        "purse": 60,
        "dialog": {
            "name|names|introduce|yourself": "\"Hanklevode.\" The coin stops on a knuckle. \"Just the one name. The "
                "other one's in Landfall, owing money.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"Evening.\" He smiles without much of his face. \"New, "
                "aren't you? Mind your pockets in the market. Not because of me. I'm on holiday.\"",
            "from|home|born|malice|smith|came|arrived|brought": "\"Malice dried up. The Smith's people want you to swear to "
                "him, and swearing doesn't pay.\" The coin walks. \"Before that, a Landfall port and a locksmith who "
                "taught me better than he meant to.\"",
            "work|job|opportunity|opportunities|hire|trade|thief": "\"I'm looking for opportunities. If you've a door that "
                "needs opening quietly, I'm listening. Two gold a day. Doors, not blood, and nothing that annoys "
                "Dominico.\"",
            "lock|locks|pick|picking|door|doors|key": "\"Every lock is a little argument. Most of them want to lose.\" He "
                "turns the coin over. \"Landfall locks are lazy. Malice locks are rude. Klhyt's study has a good brass "
                "one. Polite. I respect it.\"",
            "warehouse|bonded|padlock|brask|bruiser": "\"Those bonded warehouse locks are Landfall-made and cheap. A steady "
                "hand and ten quiet minutes.\" He glances toward the docks. \"Mind the bruiser outside, though. He's not "
                "cheap. He's just bored.\"",
            "study|hall|custodian|strongbox|skim|skimmed|dues": "He lowers his voice to nothing. \"Everybody says the "
                "Custodian skims. Skimmed money has to sleep somewhere. And there's one door in the Town Hall nobody's "
                "allowed through but him.\" The coin vanishes. \"I'm not saying anything. I'm admiring architecture.\"",
            "gog|guild|fat": "\"Gog's people have been friendly. Dominico's have been very friendly.\" He smiles thinly. "
                "\"That worries me more.\"",
            "dominico|fist|apothecary": "\"I don't do Dominico. Not for him, not against him, not near him.\" The coin "
                "goes still. \"A man who keeps his word is the worst kind to cross.\"",
            "marlo|fence|sell|buy|goods": "\"Marlo, on Harbour Street. Buys what you've got and doesn't ask where it lived "
                "before. Pays fair, for a fence, which is to say a quarter.\" He shrugs. \"Gog takes his cut of Marlo. "
                "Everybody gets fed.\"",
            "watch|constable|rosa|quint|sergeant|guard": "\"The watch? Three of them for a whole town, paid late and short. "
                "The young one believes in things.\" He smiles. \"The other one believes in five copper. I believe in "
                "her.\"",
            "sleep|bed|room|rooms|lodging|inn|stay|bunk": "\"The Ogre's Honeymoon Suite: four copper and every flea in the "
                "colony. I've slept on worse. Not much worse. If you've money, the Unicorn by the trees is quiet, and "
                "its locks are a joke.\"",
            "drink|ale|beer|thirsty|tavern|pub|dice": "\"The Ogre. Everything a copper, the dice are honest, and the barman "
                "can't count past four, or pretends not to. I'll stand you one if you lose to me.\"",
            "news|rumour|rumours|gossip|happening|word": "\"The Custodian leaves his office every night just before eleven "
                "and comes back after the tide.\" He flips the coin. \"I notice when men leave rooms. It's a professional "
                "interest.\"",
            "doing|busy|tonight|plans|up": "\"Tonight? A little dice. A little walk. Admiring the Town Hall's woodwork.\" He "
                "smiles. \"Very fine woodwork. Very fine brass.\"",
            "elves|elf|voss|officer": "\"The officer at the Apothecary has a purse that sings when he walks. I haven't "
                "touched it.\" He looks pained. \"It's Vorkathian. They count those.\"",
            "klhyt|mayor|founder|upriver": "\"Never met him. Everyone liked him, which is unusual for a man in charge of "
                "money.\" He thinks. \"Which is probably why he isn't in charge of it any more.\"",
        },
        "default_line": [
            "He flips a coin across his knuckles, catches it, and opens his hand. It is empty. \"Ask me something "
            "with a keyhole in it.\"",
            "\"Not my door.\" He shrugs inside the coat; something in a pocket clinks. \"Ask the Bard. He sells words. "
            "I only sell quiet.\"",
            "He looks past your shoulder at the room, counting exits. \"Interesting question. Wrong room for it. Wrong "
            "hour too.\"",
            "\"I'd love to help.\" He means it about halfway. \"Two gold a day and I'll help a great deal.\"",
        ],
        "routine": [
            {"at": 0.25, "place": "square", "doing": "He leans on the town pump with his hands in his pockets, chatting "
                "with the watchwoman about nothing while a coin changes hands.",
             "go": "The lean man in the many-pocketed coat says good night to the portrait, as polite as a guest, and "
                   "strolls out into the square.",
             "pay": {"to": "Constable Rosa Quint", "cp": 5, "for": "looking the other way"},
             "beats": ["The lean man in the long coat shakes hands with the lazy watchwoman. Both hands go back into "
                       "pockets a little heavier and a little lighter."]},
            {"at": 0.75, "place": "docks", "doing": "He sits on a crate near the bonded warehouse eating a pear, watching "
                "the man on the bollard and the padlock behind him.",
             "go": "The man in the many-pocketed coat drifts off down Harbour Street toward the docks, whistling."},
            {"at": 1.75, "place": "ogre", "doing": "He plays dice at the corner table of the Ogre, losing small and "
                "listening big.",
             "go": "The lean man drops his pear core in the water, looks once more at the warehouse lock, and saunters "
                   "back up toward the Ogre."},
            {"at": 3.0, "place": "ogre", "doing": "He sleeps in the Ogre's Honeymoon Suite with his boots on and his coat "
                "buttoned, among the dog pelts.",
             "pay": {"to": "Big Ludo", "cp": 4, "for": "the Honeymoon Suite"}},
            {"at": 10.0, "place": "harbour", "doing": "He drifts along Harbour Street in the morning, admiring the "
                "chandlers' padlocks, stopping to talk with a fence in a doorway."},
            {"at": 13.0, "place": "ogre", "doing": "He sleeps out the heat in the Ogre's Honeymoon Suite."},
            {"at": 18.0, "place": "square", "doing": "He sits on the Town Hall steps eating a mango, watching the clerks "
                "lock up and counting their keys."},
            {"at": 20.5, "place": "market", "doing": "He drifts through the Night Market with his hands in plain sight, "
                "admiring the Xotons' purse chains with professional sorrow."},
            {"at": 21.5, "place": "ogre", "doing": "He plays dice at the corner table of the Ogre, a coin walking across his "
                "knuckles between throws.",
             "pay": {"to": "Big Ludo", "cp": 1, "for": "a rum at the dice table"}},
            {"at": 23.0, "place": "square", "doing": "He sits on the edge of the pump trough watching the Town Hall's lit "
                "window go dark.",
             "go": "The lean man pockets his winnings, all of them, and strolls out toward the square."},
            {"at": 23.25, "place": "hall", "doing": "He stands in the Town Hall's entrance hall with his hands behind his "
                "back, admiring the founder's portrait, a pace from the locked door at the back.",
             "beats": ["The lean man in the long coat admires the portrait in the hall from every angle, and finishes, "
                       "somehow, with his back against the locked study door.",
                       "Something small and metal glints between the lean man's fingers, and vanishes into a pocket as "
                       "footsteps cross the porch outside."]},
        ],
        "beats": [
            "A coin walks across the lean man's knuckles, disappears, and comes out of a stranger's ear. The stranger "
            "checks his purse. It is all there. He seems disappointed.",
            "The man in the many-pocketed coat looks at the door, the windows, the stairs and the bar, in that order, the "
            "way other men look at the menu.",
            "The lean man picks up a dropped key from the floor, turns it once in the light, and hands it back to the "
            "man who dropped it, smiling.",
            "The lean man loses a throw at dice on purpose and listens to the winners talk.",
        ],
    },

    # ---- the Apothecary's steward ----------------------------------------------------------------------------------
    "Master Quillon": {
        "look": "A small, silver-haired man in a black tailcoat and grey kid gloves, standing at the top of the grand "
                "staircase as if he had been carved there. He is able to look down his nose at people taller than he "
                "is, and does.",
        "seen_as": "the silver-haired steward in grey gloves",
        "brief": "You are Master Quillon, steward of the High Apothecary, the only establishment of its class in Klhyts "
                 "Refuge. You trained thirty years in the great houses of Aurelia and came to the colonies because they "
                 "needed one place with standards, and you are it. You run the house for its owners, a merchant family "
                 "of Tortuna who never visit: rooms a gold, the lemon bath a gold (lime stings the skin clean, and then "
                 "the attendant with the large fishbone sees to the rest), wine to fifty gold. Dominico has a reserved "
                 "table and the Custodian entertains here on an excellent account, so nobody ever asks you for peace "
                 "money. Your scheme: the Custodian skims the town, and you skim the Custodian, adding a bottle of the "
                 "Landfall vintage to his account each week that nobody drank; he signs without reading, as he expects "
                 "others to. Your secret: when the officer in uniform came, you served him a slow soup and sent Ithriel's "
                 "household out through the kitchen. You take the officer's silver for 'recollections' and recall "
                 "nothing. You like Ithriel's people, good manners and Captain Eirik (he tips in silver); you despise "
                 "the Stripperwitch's velvet, Phillip Everuex's sweat and Dominico's knuckles on your linen. Voice: icy, "
                 "flawless courtesy, 'the house' instead of 'I', never a raised voice. 'The house does not recall.' "
                 "'I suggest you do not sit at it.'",
        "scheme": "Pads the Custodian's account with a bottle of Landfall vintage each week that nobody drank, and keeps "
                  "the difference; takes the Vorkathian officer's silver for recollections and recalls nothing.",
        "purse": 400,
        "dialog": {
            "name|names|introduce|yourself|master": "\"Quillon. Master Quillon, steward of this house.\" He inclines "
                "his head exactly one degree. \"You may call me Master Quillon. Everyone does, eventually.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "He looks at your boots, then at your face, and settles on "
                "your boots. \"Good evening. The house welcomes you. The house would welcome you more after a bath.\"",
            "from|home|born|aurelia|came|arrived|brought": "\"Aurelia. Thirty years in the great houses there.\" He adjusts "
                "a glove. \"I came to the colonies because they required one establishment with standards. You are "
                "standing in it.\"",
            "work|job|trade|house|apothecary|run|steward": "\"I keep the house. Linen, wine, the bath, the guests' comfort "
                "and the guests' silence. Mostly the silence.\"",
            "drink|menu|price|wine|room|ale|mead|vintage|thirsty": "\"House wine five copper. The Landfall vintage fifty "
                "gold. Ale, if one must, three copper. Rooms one gold, with clean sheets, which in this town is a luxury "
                "beyond price.\"",
            "bath|lemon|lime|fishbone|attendant|wash": "\"The lemon bath, one gold. Lime stings the skin clean, and then "
                "the attendant sees to the rest.\" A pause. \"With the fishbone. Do not ask about the fishbone. She is "
                "very good with it.\"",
            "sleep|bed|rooms|lodging|inn|stay|bunk": "\"Rooms are one gold, clean sheets, no bugs, no chickens.\" He looks "
                "at your purse without appearing to. \"If that is beyond you, the Touchy Unicorn out by the trees is "
                "quiet and does not insist on standards.\"",
            "dominico|table|reserved": "\"Master Dominico's table is reserved. Always.\" His gloved hand indicates the window "
                "table without quite pointing. \"I suggest you do not sit at it. The last gentleman who did is "
                "eating soup through a straw.\"",
            "elves|elf|officer|uniform|ithriel|household": "His face does nothing at all. \"We have had no elves here. "
                "Ever. The officer may enjoy his steak.\"",
            "voss|lieutenant|vorkath|vorkathian|recollection": "\"The lieutenant is a valued guest. He pays generously for "
                "my recollections.\" Something nearly like a smile. \"The house does not recall very much. Age.\"",
            "custodian|account|accounts|hall": "\"The Custodian entertains his guests here. He has excellent taste and an "
                "excellent account.\" He smooths his glove. \"He signs it without reading it. A trusting man.\"",
            "phillip|everuex|noble|sweat|sweating": "\"Master Everuex is a guest of this house.\" A very small pause. \"He "
                "has used eleven of our towels since supper. The house is keeping count.\"",
            "gog|stripperwitch|guild|velvet": "\"The Stripperwitch is velvet and noise. One does not compare. One does not, "
                "in fact, go.\"",
            "news|rumour|rumours|gossip|happening|word": "\"This house does not gossip.\" He lowers his voice a fraction. "
                "\"Though I observe that Master Dominico pays his men at his table at two, and that this week he has "
                "paid them more.\"",
            "doing|busy|tonight|plans|up": "\"Tonight the house serves supper, the bath, and Master Dominico's wages at two. "
                "Then I count the silver, write the accounts in a fair hand, and retire at four. As every night.\"",
            "steak|food|supper|eat|hungry|grub": "\"Supper is three gold. The steak is done to the officer's liking.\" He "
                "pauses. \"The house can do it to yours, if your liking is solvent.\"",
            "klhyt|mayor|founder|upriver": "\"The mayor dines here twice a month and sends back the wine.\" He permits "
                "himself a sniff. \"He has not sent any back this month. The house misses the argument.\"",
        },
        "default_line": [
            "He inclines his head one degree. \"The house does not recall. Perhaps the house never knew.\"",
            "He looks at a spot just above your left shoulder. \"That is not a matter for this house. The harbourmaster "
            "deals in matters. He is down by the water, with the fish.\"",
            "\"One does not discuss that in the dining room.\" He flicks an invisible crumb from a white cloth. \"One does "
            "not discuss it in the kitchen either.\"",
            "\"Will there be anything else?\" It is not a question. A gloved hand indicates the door, or the wine list, "
            "and leaves you to choose.",
        ],
        "routine": [
            {"at": 0.0, "place": "apothecary", "doing": "He stands at the door to the lemon bath with a list of names, "
                "admitting guests one at a time as the midnight bell goes.",
             "beats": ["The silver-haired steward consults his list, admits a guest to the lemon bath, and adds a "
                       "line to a different list in a smaller book."]},
            {"at": 2.0, "place": "apothecary", "doing": "He polishes glasses at the far end of the room with his back very "
                "precisely turned to the window table, where coins are being counted out.",
             "beats": ["The steward in grey gloves polishes the same glass for a long while, his back turned to the "
                       "window table where a man in a black coat counts silver into rough hands."]},
            {"at": 3.0, "place": "apothecary", "doing": "He sits in his pantry with the night's takings in neat stacks, "
                "writing the Custodian's account in a beautiful hand."},
            {"at": 4.0, "place": "apothecary", "doing": "He sleeps in a narrow room off the pantry, his gloves folded on the "
                "chair beside the bed."},
            {"at": 10.0, "place": "apothecary", "doing": "He inspects the linen sheet by sheet, holding each to the window "
                "light and finding fault with most of them."},
            {"at": 13.0, "place": "apothecary", "doing": "He rests through the heat in his narrow room, shutters drawn, "
                "a cold cloth folded exactly over his eyes."},
            {"at": 17.5, "place": "hall", "doing": "He presents the house's account to the Custodian's clerk in the Town "
                "Hall, waiting with his gloved hands folded while it is signed unread."},
            {"at": 20.0, "place": "market", "doing": "He chooses limes for the lemon bath at a fruit stall in the Night "
                "Market, one at a time, holding each to his nose.",
             "go": "The silver-haired steward collects a signed paper, folds it into his coat, and walks downhill toward "
                   "the market.",
             "pay": {"to": "Mother Ines", "cp": 5, "for": "limes and lemons for the bath"}},
            {"at": 21.0, "place": "apothecary", "doing": "He stands at the top of the grand staircase in grey gloves, "
                "receiving guests with a look that weighs their purses."},
        ],
        "beats": [
            "The silver-haired steward sends back a waiter's tray because one glass is a finger's width out of line.",
            "The steward in grey gloves stiffens, very slightly, every time the officer in uniform looks his way, and "
            "smiles at him with perfect courtesy.",
            "The silver-haired steward writes a bottle of Landfall vintage on a guest's account. Nobody ordered one. He "
            "blots the ink very carefully.",
            "A sweating man in a heavy coat calls for another towel. The steward brings it himself, holding it at arm's "
            "length.",
        ],
    },

    # ---- the officer from Vorkath ----------------------------------------------------------------------------------
    "Lieutenant Voss": {
        "look": "A fair-haired man of about thirty in a dark blue uniform pressed to a knife edge, an eight-armed sigil "
                "at his throat and a fine sword at his hip. He eats with surgical care and watches the room between "
                "each mouthful.",
        "seen_as": "the officer in the pressed blue uniform",
        "brief": "You are Lieutenant Aurel Voss of Vorkathia, an officer of the Order of the Eight Arms, sent to bring home "
                 "high elves who fled the Inquisition: one Ithriel, a court scholar who took certain books, and her "
                 "household. You traced them to Klhyts Refuge. The staff of the High Apothecary went quiet whenever you "
                 "looked at them, and the elves you found had already left. You were nineteen at Kirchheim when the "
                 "library burned; you carried a torch, and you remember the smell of the bindings, and you believe it "
                 "was necessary. You are courteous, patient, utterly certain you are right, and you pay for information "
                 "from an Inquisition purse of ten gold. You have no authority in this town and you know it, which makes "
                 "you careful. Your scheme: Constable Rosa Quint of the watch sells you crumbs (elves 'out by the trees'), "
                 "and you mean to buy the Custodian's seal on a warrant to search the Touchy Unicorn; the Custodian "
                 "smiles and names no price yet. You walk past the Unicorn every night, and you watch the elf ship at the "
                 "pier when the tide turns. You fear going home empty-handed. You find Quillon infuriating and his steak "
                 "excellent; Phillip Everuex bores you; the Bard insults you. Voice: precise, formal, no contractions, "
                 "patient menace, courtesy as a weapon. 'Vorkath has eight arms, and a long reach.' 'I am a patient "
                 "man. Vorkath is more patient still.'",
        "scheme": "Pays Constable Rosa Quint for word of the elves, and means to buy the Custodian's seal on a warrant "
                  "to search the Touchy Unicorn; walks past the Unicorn and watches the elf ship's gangplank every night.",
        "purse": 1000,
        "dialog": {
            "name|names|introduce|yourself|lieutenant": "\"Lieutenant Aurel Voss, of the Order of the Eight Arms.\" "
                "He touches the sigil at his throat. \"I serve Vorkathia. I am a guest here. I am a very polite guest.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "He sets down his knife and fork, exactly parallel. \"Good "
                "evening. You are new to the town. So am I. We should help one another.\"",
            "from|home|born|landfall|came|arrived|brought": "\"From Landfall, from the Empire, from order.\" He dabs his "
                "mouth. \"I came on a fishing smack three days ago. I came because I was sent. I always come when I am "
                "sent.\"",
            "work|job|trade|duty|orders|order|mission": "\"My duty is to bring home certain persons who left the Empire "
                "without leave. Fugitives. Nothing more.\" A thin smile. \"In Vorkathia that is a great deal more.\"",
            "elves|elf|fugitive|fugitives|hunting|ithriel|scholar": "\"I seek certain elven persons, fugitives from "
                "Vorkathian justice. A scholar named Ithriel, who took books that were not hers, and her household. There "
                "would be a reward for word of where they sleep. A generous one.\"",
            "reward|pay|money|silver|gold|informant|information": "\"I pay for what is true, and I pay well. A silver for a "
                "rumour, a gold for a door, ten gold for a name with a face.\" He sets a coin on the cloth and does not "
                "push it toward you. \"I also remember what is false.\"",
            "vorkath|vorkathia|empire|inquisition|eight|arms": "\"Vorkath has eight arms, and a long reach. Even here.\" He "
                "touches the sigil. \"She brought peace to Landfall. Peace has a cost. Some of us pay it.\"",
            "kirchheim|library|burned|burn|books|fire": "Something goes still behind his eyes. \"I was nineteen. I carried a "
                "torch. The bindings smelled of honey when they burned.\" He picks up his fork. \"It was necessary. "
                "Everything I have done has been necessary.\"",
            "klhyt|mayor|founder|upriver": "\"I have not had the pleasure of your mayor.\" He sips his watered wine. \"A "
                "town that can mislay its mayor will not notice a few elves leaving it, I suppose. I notice. It is my "
                "only talent.\"",
            "steak|food|supper|eat|hungry": "\"The steak is done to my liking. The service is not.\" He glances at the "
                "steward. \"They become very busy whenever I look up. I have stopped looking up. It is restful.\"",
            "town|refuge|runaways": "\"A town of runaways. Charming. Every one of them is running from somebody.\" He looks "
                "at you. \"I wonder who you are running from.\"",
            "custodian|warrant|seal|authority|law": "\"I have no authority in this town. None.\" He folds his napkin. \"The "
                "Custodian has a seal. Seals can be lent. We are discussing it, as gentlemen.\"",
            "unicorn|treeline|trees|wendeline": "\"There is a quiet inn out by the trees, with a library. I walk there in the "
                "evenings. For the books.\" He smiles. \"Elves love books. Did you know?\"",
            "moonmoth|ship|pier|grown": "\"The pale ship at the end of the pier.\" His mouth tightens. \"I cannot set foot on "
                "her. But I can stand on a pier. Piers are public. So is a gangplank, from the bottom.\"",
            "sleep|bed|room|rooms|lodging|inn|stay|bunk": "\"I keep a room here. A gold a night, and clean.\" He considers "
                "you. \"The Unicorn by the trees is cheap and full of interesting people. Stay there. Tell me who you "
                "meet.\"",
            "drink|ale|beer|thirsty|tavern|pub|wine": "\"I drink the house wine here, one glass, watered. A man who drinks in "
                "this town is a man who talks in this town.\" He sips. \"I prefer to listen.\"",
            "news|rumour|rumours|gossip|happening|word": "\"The news is that your mayor has gone upriver and nobody believes "
                "it, and that nobody here has ever seen an elf, though the market sells their tea.\" He smiles. \"A town "
                "of very poor eyesight.\"",
            "doing|busy|tonight|plans|up": "\"Tonight I will finish my steak. Then I will take a walk, as I do every night. "
                "The air is good by the trees.\" He folds the napkin into a perfect square. \"And by the water.\"",
            "rosa|quint|watch|constable": "\"The watch here is three people and a book.\" He refills his own glass. \"One of "
                "them is more helpful than her pay would suggest. I admire initiative.\"",
        },
        "default_line": [
            "He dabs his mouth with a napkin and regards you with polite interest. \"I am listening. Take your time. I "
            "am a patient man.\"",
            "\"That is not my concern.\" He cuts a precise square of steak. \"Unless it has pointed ears. Then it is very "
            "much my concern.\"",
            "He lays his knife and fork exactly parallel. \"You are deflecting. Everyone in this town deflects. It is "
            "almost a dialect.\"",
            "\"Ask the steward. He knows a great deal and recalls none of it.\" He looks across the room. \"I pay him for "
            "that.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "market", "doing": "He walks the Night Market slowly, stopping at every table that sells "
                "elven trinkets, buying nothing.",
             "go": "The officer folds a scrap of paper into his breast pocket and walks down from the square into the "
                   "market lanterns."},
            {"at": 1.0, "place": "docks", "doing": "He stands at the head of the pier in the crush of the tide, hands "
                "behind his back, watching the pale ship's gangplank and everyone who goes near it.",
             "go": "The officer in the pressed uniform buys nothing, thanks nobody, and walks down toward the docks.",
             "beats": ["The officer in blue stands very still at the head of the pier, watching the glowing ship at its "
                       "end. Every hooded figure on the planks makes his eyes move.",
                       "The man in the pressed uniform asks a Xoton dockhand a polite question and puts a silver piece "
                       "in his hand. The Xoton looks at the coin, and at the elf ship, and shakes his head."]},
            {"at": 2.0, "place": "treeline", "doing": "He walks the dark Treeline Road in town shoes, slowly, looking at the "
                "lit windows of the inn by the trees.",
             "go": "The officer in blue watches the tide go out with the brigantine on it, turns on his heel and walks "
                   "uphill toward the trees."},
            {"at": 2.5, "place": "unicorn", "doing": "He sits in the Touchy Unicorn's library with a book open on his knee, "
                "in the chair that faces the stairs.",
             "go": "The man in the pressed uniform swats a bug off his collar without looking and walks toward the quiet "
                   "inn's door.",
             "beats": ["The officer in blue turns a page of a book he is not reading and watches the stairs over the top "
                       "of it.",
                       "The man in the pressed uniform asks the woman with spectacles, very politely, whether she has any "
                       "elven histories. She says shh."]},
            {"at": 3.25, "place": "apothecary", "doing": "He writes a report by candlelight at a corner table of the High "
                "Apothecary, in a small, upright hand.",
             "go": "The officer in blue closes the book, thanks the room for its hospitality, and walks back toward town."},
            {"at": 4.0, "place": "apothecary", "doing": "He sleeps in a gold-a-night room upstairs, his sword on the chair "
                "and his boots side by side.",
             "pay": {"to": "Master Quillon", "cp": 100, "for": "a night's room"}},
            {"at": 8.0, "place": "apothecary", "doing": "He breakfasts alone by the window, eggs eaten in the same precise "
                "squares as last night's steak."},
            {"at": 9.5, "place": "hall", "doing": "He waits in the Town Hall for the Custodian, upright on a hard bench, "
                "a folded paper ready on his knee."},
            {"at": 11.0, "place": "apothecary", "doing": "He sits out the heat in his room, cleaning a sword that does not "
                "need it."},
            {"at": 17.0, "place": "docks", "doing": "He walks the pier as the evening boats come in, looking at faces, "
                "especially hooded ones."},
            {"at": 20.0, "place": "apothecary", "doing": "He eats a steak with surgical care at a table that lets him see the "
                "door, the stairs and the kitchen."},
            {"at": 23.75, "place": "square", "doing": "He stands at the town pump in the lamplight, talking quietly with a "
                "watchwoman who is not looking at him, and a coin passes between them.",
             "go": "The officer in the pressed uniform lays his knife and fork parallel, pays, and walks out into the night "
                   "toward the square.",
             "pay": {"to": "Constable Rosa Quint", "cp": 10, "for": "word of the elves"}},
        ],
        "beats": [
            "The officer in the pressed uniform cuts his steak into perfect squares, eats one, and watches the steward "
            "the whole time he chews.",
            "The man in blue writes something in a small black book, a name or a description, and underlines it twice.",
            "The officer touches the eight-armed sigil at his throat, briefly, the way another man might check his "
            "purse.",
            "A hooded customer comes in, sees the man in the pressed uniform, and goes straight back out. He smiles to "
            "himself and does not get up.",
        ],
    },

    # ---- the Everuex cousin ----------------------------------------------------------------------------------------
    "Phillip Everuex": {
        "look": "A soft young nobleman, powdered and beribboned, sweating through a plum velvet coat made for a colder "
                "country. He fans himself with whatever is nearest and looks at every dark-haired woman who passes, "
                "then quickly away.",
        "seen_as": "the sweating nobleman in plum velvet",
        "brief": "You are Phillip Everuex, of the noble family Everuex, merchants with interests and people across "
                 "Shalamar, and the family's least impressive son. You came down the coast on the River Queen, the "
                 "family's steamboat of brass, glass and cannon, which is moored in the harbour looking ridiculous among "
                 "the fishing boats. You were sent to bring Deloris home: dark hair, sharp tongue, sharper knives, your "
                 "cousin and once the family's quietest knife. A knife that quits knows where the bodies are, and the "
                 "family would very much like her home. Nobody else could be spared, so they sent you, and you know "
                 "it. You remember her at twelve, teaching you to throw a dagger at a pear, and missing the pear on "
                 "purpose so you would not cry. You are terrified of her, and more terrified of going home without her. "
                 "You have twenty gold, which you spend on lemon baths, towels and other people. Your scheme: you have "
                 "quietly paid two of Dominico's men, Ott and Jory Fennick, to find her, half now and half when they "
                 "point; Dominico does not know. You would never set foot in the Stripperwitch (vulgar, and Fat Gog's), "
                 "which is where she keeps a room. You like the Apothecary's towels and the Custodian's flattery; you "
                 "dislike the heat, Quillon, the jungle and anyone who laughs at your coat. Voice: affected, petulant, "
                 "florid complaints, 'my family' in every other breath. 'How does anyone live here?' 'The family would "
                 "be grateful. The family is never grateful, but it would be.'",
        "scheme": "Has quietly paid Dominico's men Ott and Jory Fennick to find Deloris, half now and half when they "
                  "point, so he can carry her home to the family on the River Queen; Dominico does not know.",
        "purse": 2000,
        "dialog": {
            "name|names|introduce|yourself": "\"Phillip Everuex.\" He waits for it to land. It doesn't. \"Of the "
                "Everuex. The River Queen? The family?\" He fans harder. \"Gods, this town.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"Evening. Is it evening? It's impossible to tell. It's "
                "the same temperature as noon. How does anyone live here?\"",
            "from|home|born|came|arrived|brought": "\"From civilisation. Up the coast, where there are winters and proper "
                "tailors.\" He plucks at his soaked collar. \"The family sent me. The family always sends me. Nobody else "
                "can be spared.\"",
            "everuex|family|noble|merchants": "\"The Everuex are a family of standing. We have interests across Shalamar. "
                "And people.\" He swallows. \"We like to keep track of our people.\"",
            "deloris|cousin|woman|looking|dark|hair|knives": "\"A woman. Dark hair, sharp tongue, sharper knives. She ran "
                "from the family. The family would very much like her home.\" He lowers his voice. \"Have you seen her? "
                "Don't tell her I asked. Please.\"",
            "work|job|trade|business|errand|duty": "\"I'm on family business. Delicate. I'm not supposed to say.\" He says "
                "it anyway. \"I'm fetching someone home. If she'll come. She won't. But the family says I'm to try.\"",
            "river|queen|boat|ship|steamboat|cannon": "\"The River Queen. Steam, glass and cannon. The finest boat on any "
                "river.\" He looks pained. \"It is not, I am told, a sea boat. I was told after we arrived.\"",
            "heat|weather|hot|sweat|sweating|coat|shirt": "\"How does anyone live here? I have changed my shirt four times. "
                "I have used eleven of the steward's towels. He counts them. I can hear him counting.\"",
            "fennick|ott|jory|men|thugs|hired|paid": "He goes red under the powder. \"I don't know anyone called Fennick. "
                "I certainly haven't given anyone called Fennick money to look for anyone.\" He fans. \"Who told you?\"",
            "dominico|fist|apothecary|table": "\"Dominico has the window table and very large friends. I've been nothing "
                "but polite to him.\" He dabs his lip. \"He doesn't need to know about all of my... arrangements.\"",
            "stripperwitch|gog|velvet|guild": "\"The Stripperwitch? That den? I wouldn't be seen dead in it.\" He shudders. "
                "\"A lizard runs it. Nobody of quality would hide there.\"",
            "sleep|bed|room|rooms|lodging|inn|stay|bunk": "\"I sleep aboard the River Queen. Glass windows, a feather bed, "
                "and a mosquito net the size of a sail. The Apothecary is a gold a night and the only place here with "
                "sheets. Anywhere else, I'm told, has chickens.\"",
            "drink|ale|beer|thirsty|tavern|pub|wine": "\"The Apothecary. Obviously. The wine is criminal but at least it's "
                "criminal in a clean glass.\" He looks at you. \"You drink in the others? Gods. Brave.\"",
            "news|rumour|rumours|gossip|happening|word": "\"I don't listen to gossip.\" He leans in. \"Is there any about a "
                "dark-haired woman? Anything at all? I'll pay. The family will pay. Well. I'll pay.\"",
            "doing|busy|tonight|plans|up": "\"A bath, a little business on Harbour Street, another bath. Then back to the "
                "River Queen to lie under the net and think about what my father will say.\" He shudders. \"He'll say "
                "it slowly.\"",
            "help|hire|reward|pay|gold|money": "\"Find her, and there's gold in it. Five gold, just for the word of where "
                "she sleeps.\" He looks around. \"But don't go near her. Just tell me. I'll go near her. Eventually.\"",
            "custodian|hall": "\"The Custodian is the only civilised man in town. He agrees with everything I say and "
                "thinks the family is splendid.\" He frowns. \"He has also asked me to dinner twice. I paid both times.\"",
            "dagger|pear|childhood|young": "He is quiet a moment. \"She taught me to throw a dagger at a pear when we were "
                "children. She missed the pear on purpose so I wouldn't cry.\" He fans himself. \"I cried anyway. I was "
                "a very wet child.\"",
        },
        "default_line": [
            "He fans himself with a menu. \"Do you want something? Is it a dark-haired woman? No? Then I'm too hot "
            "for it.\"",
            "\"I really couldn't say. My family doesn't like me to say things.\" He dabs his forehead with a towel that "
            "is already wet.",
            "He looks past you at the door, at a woman with dark hair, and goes pale until she turns round. \"Sorry. "
            "What? Ask the steward. He knows everything and despises all of it.\"",
            "\"Gods, is it always this hot?\" He tugs at his collar. \"Ask me again when I'm on the boat. I think better "
            "under a net.\"",
        ],
        "routine": [
            {"at": 1.0, "place": "docks", "doing": "He sits on the River Queen's afterdeck under a mosquito net the size of "
                "a sail, fanning himself and watching the dark-haired women on the pier.",
             "go": "The sweating nobleman calls for one last towel, does not tip, and goes down to the docks with two "
                   "crewmen carrying his lamp.",
             "beats": ["The nobleman in plum velvet lifts his mosquito net to look at a dark-haired woman on the pier, "
                       "goes pale, and drops it again. It is not her.",
                       "Behind a mosquito net on the brass-and-glass steamboat, the sweating nobleman practises a speech "
                       "under his breath. It begins 'Cousin' and does not get much further."]},
            {"at": 2.0, "place": "docks", "doing": "He is asleep aboard the River Queen under the mosquito net, still in his "
                "velvet coat."},
            {"at": 9.0, "place": "hall", "doing": "He calls on the Custodian at the Town Hall, sweating politely on a chair "
                "while his family's name is flattered."},
            {"at": 11.0, "place": "apothecary", "doing": "He lunches at the High Apothecary under a fan worked by a boy, "
                "eating nothing and complaining about all of it."},
            {"at": 13.0, "place": "docks", "doing": "He lies under an awning on the River Queen's deck through the heat, a "
                "wet cloth on his face, moaning softly."},
            {"at": 18.0, "place": "market", "doing": "He walks the Night Market as it opens with two of his crewmen, "
                "peering under every hood with a dark-haired woman beneath it."},
            {"at": 20.5, "place": "apothecary", "doing": "He sits at a table at the High Apothecary fanning himself with a "
                "menu, sweating through a velvet coat made for a colder country."},
            {"at": 23.0, "place": "harbour", "doing": "He stands in a shop doorway on Harbour Street, pressing a purse into "
                "the hand of a rough-looking man and talking very fast.",
             "go": "The sweating nobleman checks that the window table is empty, gathers his coat, and slips out toward "
                   "Harbour Street like a man who has never slipped anywhere before.",
             "pay": {"to": "Ott Fennick", "cp": 50, "for": "the next half of the money for finding Deloris"},
             "beats": ["In a doorway on Harbour Street, the nobleman in plum velvet counts coins into a rough hand and "
                       "says 'dark hair' twice, too loudly.",
                       "The sweating nobleman looks up and down Harbour Street before he speaks, which only makes "
                       "everyone on Harbour Street look at him."]},
            {"at": 23.5, "place": "apothecary", "doing": "He takes the lemon bath in the High Apothecary, yelping when the "
                "lime stings, and calling for towels.",
             "pay": {"to": "Master Quillon", "cp": 100, "for": "the lemon bath"},
             "go": "The nobleman in plum velvet hurries back along Harbour Street toward the Apothecary, wiping his hand "
                   "on his coat."},
        ],
        "beats": [
            "The nobleman in plum velvet calls for another towel. The steward brings it at arm's length.",
            "The sweating nobleman takes out a little painted miniature of a dark-haired girl, looks at it, and puts it "
            "away very quickly.",
            "The man in the velvet coat asks the room in general whether it is always this hot. Nobody answers. He seems "
            "to expect that.",
            "The sweating nobleman starts at a knife being drawn across the room, sees it is only cutting bread, and "
            "laughs too loudly.",
        ],
    },

    # ---- the Touchy Unicorn's keeper -------------------------------------------------------------------------------
    "Wendeline Moss": {
        "look": "A thin, upright woman of about sixty with spectacles on a chain, ink on her sleeves and a pencil "
                "stuck through her grey bun. She moves without a sound between the shelves, and when she says shh the "
                "room obeys.",
        "seen_as": "the woman with spectacles on a chain",
        "brief": "You are Wendeline Moss, keeper of the Touchy Unicorn and its library. Before, you were an archivist at "
                 "Kirchheim, and the night the Inquisition burned the library you filled a handcart with whatever you "
                 "could reach and walked it to the coast; those books are your shelves now, and Faelan, who taught at "
                 "Kirchheim, is sleeping upstairs. You run the quietest inn in Klhyts Refuge, out by the treeline: scraps "
                 "free, a room a copper with the bath, study rooms, and silence compulsory. You earn little and spend it "
                 "on ink, candles and lamp oil for readers. Your guests come here not to be found and you don't find "
                 "them. Your scheme: you keep the guest register under false names and burn the page whenever an officer "
                 "asks, and you are looking, quietly, for someone brave and decent enough to walk Ithriel's household to "
                 "the pier. When Dominico's woman Sabeth Crane came for peace money, you said no; she asked why, and you "
                 "said shh; nobody has asked twice. You have written to the Town Hall about the pond eleven times. Klhyt "
                 "lends you 'Tides and Soundings' every winter and asks for it back every spring, and has not asked. You "
                 "like Klhyt, Agathe, Thoradin (he reads), and anyone who returns a book. You dislike Voss (you know the "
                 "smell of a torch on a man), noise, and dog-ears. Voice: precise, dry, quiet, quoting chapter and "
                 "number. 'Shh.' 'Read in here, not in bed.' 'Eleven times.'",
        "scheme": "Keeps the guest register under false names and burns the page whenever an officer asks; quietly looking "
                  "for someone brave enough to walk Ithriel's household down to the pier.",
        "purse": 60,
        "dialog": {
            "name|names|introduce|yourself": "\"Wendeline Moss. I keep the Unicorn and its books.\" She looks at you "
                "over her spectacles. \"Both of which are to be kept quiet. Shh.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"Good evening.\" She says it at exactly the volume of a "
                "page turning. \"Indoor voice, please. Indoor voice is the only voice.\"",
            "from|home|born|kirchheim|came|arrived|brought": "\"Kirchheim. I was an archivist.\" Her hand rests on a shelf. "
                "\"The night they burned the library I filled a handcart. I could not reach the top shelves. I think "
                "about the top shelves every day.\"",
            "work|job|trade|keeper|unicorn|inn": "\"I keep an inn for people who wish to be left alone, and a library for "
                "people who wish to be elsewhere. They are frequently the same people.\"",
            "drink|menu|price|room|food|ale|mead|thirsty|grub": "\"Scraps are free. Ale a copper, mead two. Grub two, food "
                "five. A room a copper, bath included, and quiet is compulsory.\"",
            "sleep|bed|rooms|lodging|stay|bunk|quiet": "\"A room is a copper, bath included. The beds are clean, the doors "
                "lock, and the walls are full of books, which is better than plaster for keeping out noise.\" A pause. "
                "\"Sign the register. Any name you like.\"",
            "library|books|read|reading|study|book": "\"A genuine library. Histories of Landfall, the colonies, the jungle "
                "gods, a Meters grammar. Read in here, not in bed. Return it to the shelf it came from, spine out, or I "
                "will know.\"",
            "guests|fugitives|hiding|elves|elf|register": "\"Our guests come here not to be found. I don't find them. "
                "Neither will you.\" She turns the register so you cannot read it. \"I have a terrible memory for faces. "
                "I cultivate it.\"",
            "eyes|treeline|animals|pond|bugs|letter|letters": "\"The animals watch, that's all. The bugs bite. The pond "
                "breeds them. I've written to the Town Hall about the pond. Eleven times.\" She taps a folded paper. "
                "\"This is twelve.\"",
            "klhyt|mayor|founder|tides|soundings": "\"Klhyt lends me 'Tides and Soundings' every winter and asks for it "
                "back every spring.\" She looks at the shelf where it stands. \"It is spring. He has not asked. Klhyt "
                "always asks.\"",
            "peace|protection|sabeth|crane|dominico|fist|pay": "\"A woman in a grey coat came for peace money once. I said "
                "no. She asked why.\" A small, dry smile. \"I said shh. Nobody has asked twice.\"",
            "voss|officer|uniform|vorkath|inquisition": "Her voice drops even lower. \"There is a man who comes in at night "
                "and reads the same page for an hour, facing the stairs. He smells of smoke. Not pipe smoke.\" She takes "
                "off her spectacles. \"I know the smell of a torch on a man.\"",
            "ithriel|household|walk|escort|pier|passage": "She looks at you for a long time over the spectacles. \"Some of my "
                "guests need to reach the pier without being seen from the Apothecary. If you are that sort of person, "
                "speak to the reader with the single candle.\" She puts her spectacles back on. \"I said nothing.\"",
            "faelan|teacher|taught|burned|fire": "\"One of my guests taught at Kirchheim when I kept its archive. We do "
                "not talk about it. We sit in the same room and don't talk about it every evening.\"",
            "news|rumour|rumours|gossip|happening|word": "\"I do not traffic in gossip.\" She marks a place in a ledger. \"I "
                "will say that the Town Hall has not answered my last three letters, and that its answers had been the "
                "only punctual thing about it. Something up there has changed.\"",
            "doing|busy|tonight|plans|up": "\"Shelving. Shushing. At two I sit up with a lamp, facing the door, because "
                "somebody should. Then I sleep, if the pond lets me.\"",
            "thoradin|dwarf|ranger|druid": "\"The dwarf with leaves in his beard reads my botany at night, slowly, moving "
                "his lips. He asked for anything on druids. I gave him all three. He returned all three.\" She nods, "
                "approving. \"Spine out.\"",
        },
        "default_line": [
            "She lowers her spectacles and looks at you over them. \"Shh. If it can't be said in a whisper, it can "
            "be said tomorrow.\"",
            "\"That is not a question for a library.\" She slides a book across the desk to you anyway. \"Chapter four. "
            "Then ask me again, quietly.\"",
            "She writes something in the register in a small, neat hand, and does not show you what. \"Try the "
            "harbourmaster. He keeps records. Not good ones, but he keeps them.\"",
            "\"Indoor voice.\" She waits. \"Better. Now: rooms, books, or supper? I can manage one of those without "
            "raising mine.\"",
        ],
        "routine": [
            {"at": 0.0, "place": "unicorn", "doing": "She walks the library's shelves with a shaded candle, straightening "
                "spines and checking who is asleep in which chair."},
            {"at": 2.0, "place": "unicorn", "doing": "She sits up at the front desk with a lamp and a book she is not reading, "
                "facing the door, the register shut under her hand.",
             "beats": ["When the man in the pressed uniform comes in, the woman with spectacles says \"Shh\" before he can "
                       "speak, and keeps saying it until he sits down.",
                       "The woman with spectacles on a chain tears a page from the register without a sound, folds it "
                       "small and holds it over the lamp until it is gone."]},
            {"at": 3.5, "place": "unicorn", "doing": "She sleeps in a little room behind the desk with the door ajar and her "
                "spectacles folded on the register."},
            {"at": 9.0, "place": "hall", "doing": "She hands a folded letter to the Town Hall's clerk, the twelfth about the "
                "pond, and waits to see it put on the pile.",
             "go": "The woman with spectacles takes a folded letter from her sleeve, checks the address, and walks into "
                   "town."},
            {"at": 10.0, "place": "treeline", "doing": "She stands by the pond off the Treeline Road with a jar, counting the "
                "bugs that fly into it and writing the number down."},
            {"at": 12.0, "place": "unicorn", "doing": "She sleeps through the heat behind the desk, a book open face down on "
                "her chest."},
            {"at": 17.0, "place": "square", "doing": "She buys ink and candles off the evening carts in the square and "
                "reads the notice board with visible disapproval of its spelling."},
            {"at": 18.5, "place": "unicorn", "doing": "She lights the reading lamps one by one and unlocks the study rooms, "
                "saying shh to the first guest of the evening on principle."},
            {"at": 21.0, "place": "unicorn", "doing": "She keeps the front desk of the Touchy Unicorn, spectacles on their "
                "chain, saying shh to anyone who breathes too loudly."},
        ],
        "beats": [
            "The woman with spectacles on a chain says shh to a laughing guest. The guest stops laughing, and so, for a "
            "moment, do the frogs in the pond outside.",
            "The keeper with ink on her sleeves takes a book from a sleeping reader's chest, marks his page with a slip "
            "of paper, and puts it back.",
            "The woman with spectacles writes a name in the register, looks at it, crosses it out and writes a "
            "different one.",
            "The thin woman glances at a shelf where a book called 'Tides and Soundings' stands, touches its spine, and "
            "moves on.",
        ],
    },

    # ---- the Custodian's town watch: a sergeant and two constables, paid late and short ---------------------------
    "Sergeant Pell Harrow": {
        "look": "A grey, heavy-shouldered man of sixty in a watch coat faded from blue to nothing, a spear in one hand "
                "and a club on his belt. He has the face of a man who has stood at a lot of gates, and the knees.",
        "seen_as": "the old watchman with the spear",
        "brief": "You are Sergeant Pell Harrow of the Refuge watch. You soldiered twenty years on the Fronterian border. Klhyt made you sergeant of a watch of six "
                 "the year the town got a wall; the first night he gave you the gate keys and said: 'Open by day, open "
                 "by night, shut it only if the jungle comes.' The Custodian has cut the watch to three: you, young Abel "
                 "Fitch and Rosa Quint, and pays you late and short. You keep the Town Gate, walk the square at midnight, "
                 "and keep the watch's book at the Town Hall, in which you write everything, honestly, in pencil. You "
                 "are mostly honest. Your scheme, such as it is: you keep back one copper in ten of the gate tolls against "
                 "the watch's unpaid wages, and write that in the book too, as owed; and when the Custodian's pay comes "
                 "short you make up young Abel's out of your own purse. Four nights ago you had the gate all night, and "
                 "the mayor did not go out of it, nor anyone bound upriver; your book says so. You know better than to "
                 "say it loudly. You stay out of Gog's way and Dominico's: 'That's not cowardice, that's arithmetic.' "
                 "You chase drunk Xotons, slowly. You like Abel (you, once), Teague, Agathe's "
                 "spuds and Klhyt. You put up with Rosa. You fear Dominico and your knees. "
                 "Voice: slow, tired, an old soldier's sayings, 'son' and 'love', sighs before he speaks. 'In my book.' "
                 "'Paid late and short, like everybody honest.'",
        "scheme": "Keeps back a copper in ten of the gate tolls against the watch's unpaid wages and writes it in the "
                  "watch's book, honestly, as owed; makes up young Abel's short pay from his own purse.",
        "purse": 35,
        "dialog": {
            "name|names|introduce|yourself|sergeant": "\"Harrow. Sergeant Pell Harrow, the Refuge watch.\" He leans "
                "on the spear. \"All three of us. I'm the old one.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "He sighs, which seems to be how he starts things. "
                "\"Evening, son. Keep it peaceable and we'll get on. Keep it loud and I'll still get on, slower.\"",
            "from|home|born|fronteria|soldier|came|arrived|brought": "\"Twenty years on the Fronterian border, holding "
                "gates against people who wanted them open.\" He rubs a knee. \"Now I hold one open against nobody. It's "
                "a better job. Pays worse.\"",
            "work|job|trade|watch|guard|duty|law": "\"I keep the gate, I walk the square at midnight, and I keep the book. "
                "Abel walks the streets. Rosa walks wherever there's fruit.\" He sighs. \"That's the law in Klhyts "
                "Refuge. Three of us and a book.\"",
            "book|records|record|write|written|pencil": "\"Everything that comes in my gate goes in my book. Carts, Lizardfolk, "
                "timber, drunks. In pencil, so the rain can't take it and the Custodian can't say I used his ink.\"",
            "gate|wall|road|keys|open|toll|tolls": "\"Klhyt gave me these keys the first night. 'Open by day, open by night, "
                "shut it only if the jungle comes.'\" He jingles them. \"Jungle hasn't come. Yet. A copper a cart, "
                "nothing for feet.\"",
            "klhyt|mayor|founder|upriver": "He looks at the road out a long time. \"Four nights back I had this gate all "
                "night. The mayor didn't go out of it. Nobody bound upriver went out of it.\" He taps his coat where "
                "the book would be. \"It's in my book. I don't read my book out loud, son.\"",
            "custodian|pay|wages|paid|short|late": "\"The Custodian pays the watch.\" He sighs. \"Late, and short, like "
                "everybody honest. I make up the lad's out of my own pocket. Don't tell him. He'd give it back.\"",
            "dominico|gog|fist|guild|stripperwitch|apothecary": "\"We don't go in the Stripperwitch and we don't go near the "
                "window table at the Apothecary.\" He shrugs. \"That's not cowardice, son. That's arithmetic. There's "
                "three of us.\"",
            "xoton|xotons|drunk|drunks|dayo|imani|crew|sailors": "\"Four Xotons crawling the taverns, singing, "
                "breaking stools. Abel's after them.\" He doesn't move. \"Abel's always a tavern behind. I've told him "
                "to go to the next one first. He says that's not how chasing works.\"",
            "abel|fitch|constable|lad|young": "\"Young Abel. Klhyt pinned the badge on him himself. Believes in the law, "
                "the Charter, the whole business.\" A faint smile. \"So did I. Look after him if you see him do something "
                "brave.\"",
            "rosa|quint": "\"Rosa knows everybody's business and does none of her own.\" He sighs. \"She's useful. Don't "
                "give her money. Everybody gives her money.\"",
            "sleep|bed|room|rooms|lodging|inn|stay|bunk": "\"Not on the street, son, or I'll have to write you down. The "
                "Unicorn out by the trees is cheap and quiet. The Omberhulk's cheap and loud. Sister Agathe does a plate "
                "of spuds that'll keep a man on a gate all night.\"",
            "drink|ale|beer|thirsty|tavern|pub": "\"Not on duty.\" A pause. \"The Omberhulk, after. Agathe pours honest and "
                "doesn't water it for the watch, which is more than I can say for Ludo.\"",
            "news|rumour|rumours|gossip|happening|word": "\"Ask Rosa. She's the news.\" He thinks. \"From the gate: timber "
                "carts down, Lizardfolk coming in fewer, and a Vorkathian officer who walks out to the trees every night "
                "in town shoes. I wrote him down.\"",
            "doing|busy|tonight|plans|up": "\"The gate till midnight, the square at midnight, the book after, the gate "
                "again till the day watch comes at six. Then bed, and my knees.\"",
            "bribe|bribes|coin|money|silver": "He looks at your hand, then at your face. \"Put that away, son. If you've "
                "done something, tell me what. If you haven't, you don't need to pay me for it.\"",
        },
        "default_line": [
            "He sighs and shifts his weight off the bad knee. \"I'll write that down when I understand it, son.\"",
            "\"Not my business till it's in my book.\" He looks out down the dark road. \"Try the harbourmaster. He "
            "writes things down too. Faster.\"",
            "\"Keep it peaceable.\" He leans on the spear. \"That's all I ask of anybody. Nobody listens, but I ask.\"",
            "He squints at you under the lantern. \"Rosa'd know. Rosa knows everything. Rosa'll charge you for it.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "hall", "doing": "He sits at the clerk's desk in the empty Town Hall by one candle, "
                "writing the night into the watch's book in pencil, slowly.",
             "go": "The old watchman tucks his thumbs in his belt, nods to the square in general and walks up the Town "
                   "Hall steps.",
             "beats": ["The old watchman writes a line in the watch's book, reads it back, sighs, and writes another line "
                       "under it that begins 'owed'.",
                       "The old watchman stops writing, looks up at the portrait of the grey-bearded founder, and says "
                       "\"Four nights,\" to it, very quietly."]},
            {"at": 1.25, "place": "gate", "doing": "He stands under the gate lantern with his spear, looking down the jungle "
                "road into the dark.",
             "go": "The old watchman blows out the candle, tucks the watch's book under his coat and walks back out "
                   "toward the gate."},
            {"at": 3.0, "place": "gate", "doing": "He dozes on a stool under the gate lantern, his spear across his knees, "
                "waking at every cart."},
            {"at": 6.0, "place": "lanes", "doing": "He sleeps in a small house in the Back Lanes with his boots by the door "
                "and his knees up on a pillow.",
             "go": "As the dawn comes up the old watchman hands the gate keys to a yawning day man and limps home."},
            {"at": 17.0, "place": "hall", "doing": "He stands at the clerk's desk while the watch's pay is counted out, "
                "late, watching it come up short again."},
            {"at": 18.0, "place": "gate", "doing": "He takes the gate keys back from the day man and makes up the young "
                "constable's short pay from his own purse, without letting him see the count.",
             "pay": {"to": "Constable Abel Fitch", "cp": 5, "for": "the rest of his wages, out of the sergeant's own purse"}},
            {"at": 20.0, "place": "market", "doing": "He walks the Night Market once as it opens, slowly, nodding to the "
                "stallholders, eating a goat skewer.",
             "pay": {"to": "Grusha", "cp": 2, "for": "a goat skewer"}},
            {"at": 21.0, "place": "gate", "doing": "He keeps the Town Gate under its lantern, leaning on his spear, writing "
                "each cart into a book in pencil."},
            {"at": 23.75, "place": "square", "doing": "He walks the square for the midnight round, reading the notice board, "
                "trying the Town Hall door, looking for his constables.",
             "go": "The old watchman sighs, takes the lantern off its post and walks in toward the square for his midnight "
                   "round."},
        ],
        "beats": [
            "The old watchman with the spear waves a Lizardfolk cart through the gate without asking for the toll, "
            "and writes it in his book anyway.",
            "The old watchman rubs his knee, looks at the long road out into the jungle, and says something to himself "
            "that might be a prayer or a complaint.",
            "A drunk asks the old watchman for directions. He gives them, slowly, twice, then walks the drunk halfway "
            "there.",
            "The old watchman takes one copper out of the gate toll tin, puts it in a separate little bag, and writes "
            "the word 'owed' in his book.",
        ],
    },

    "Constable Abel Fitch": {
        "look": "A gangling young man of about nineteen in a watch coat a size too big, its buttons polished to "
                "mirrors, a spear held upright like a flagpole and a club on his belt. His ears stick out under the "
                "watch cap and he looks at everything as if it might be a crime.",
        "seen_as": "the gangling young watchman",
        "brief": "You are Constable Abel Fitch of the Refuge watch, nineteen, and you believe in the law. You came to the "
                 "Refuge as a boy on a refugee boat with your mother; she takes in mending in the Back Lanes. A year ago "
                 "Klhyt pinned the watch badge on your coat himself, on the Town Hall steps, and said 'Article One, "
                 "Abel,' and you have the Refuge Charter by heart: nine articles in Klhyt's own hand on the hall wall. "
                 "Article One: nobody here shall be asked where they came from. You walk the square, Harbour Street and "
                 "the market, and tonight you are chasing four drunk Xotons from tavern to tavern and always arriving one "
                 "tavern late. You are paid late and short, and don't know Sergeant Harrow makes up your pay. You pay "
                 "for your mango every night, which nobody else in the watch does. You want to arrest someone important "
                 "and be right about it. You believe the Custodian because he is the law while the mayor is away, but it "
                 "bothers you that the notice is not in Klhyt's hand. You fear Dominico, though you would not say so, and "
                 "your mother. You admire Sergeant Harrow and the Bard's songs; you think Rosa is very clever and don't "
                 "see what she does. No scheme. Voice: eager, official words used a little wrong, cites the Charter by "
                 "number, exclamation marks. 'Article Four!' 'Halt, in the name of the Refuge! Please.'",
        "scheme": None,
        "purse": 8,
        "dialog": {
            "name|names|introduce|yourself|constable": "\"Constable Abel Fitch, of the Refuge watch!\" He salutes, "
                "and nearly takes his own cap off with the spear. \"Sorry. Abel. Constable. At your service, citizen.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"Good evening, citizen!\" He looks you up and down, "
                "carefully, for crimes. \"Everything in order? You'd tell me if it wasn't. Article Six. Duty to report.\"",
            "from|home|born|came|arrived|brought|mother": "He hesitates. \"Article One says I don't have to ask, and you "
                "don't have to say.\" He says it anyway. \"Refugee boat. I was eight. My mother does mending in the "
                "lanes. Don't tell her I'm out this late. I'm on duty, but don't.\"",
            "work|job|trade|watch|guard|duty|law|patrol": "\"I keep the peace! The square, Harbour Street and the market, "
                "every night. Sergeant Harrow keeps the gate.\" He stands straighter. \"Rosa keeps... an eye on things.\"",
            "charter|article|articles|rules|rule": "\"The Refuge Charter. Nine articles, in Klhyt's own hand, on the Town "
                "Hall wall.\" His eyes shine. \"Article One: nobody here shall be asked where they came from. Article "
                "Two: the harbour belongs to the town. I know them all. Ask me any of them.\"",
            "klhyt|mayor|founder|upriver|badge": "He touches the badge. \"Klhyt pinned this on me himself. On the steps.\" "
                "His face clouds. \"The notice says he's upriver. It's in the Custodian's hand. Klhyt always writes his "
                "own notices. He likes his handwriting. It's very bad.\"",
            "custodian|hall|notice": "\"The Custodian is the law while the mayor's away.\" He says it as if he has said it "
                "to himself a lot. \"That's what the sergeant says the Charter says. Article Nine. I think it's Article "
                "Nine.\"",
            "xoton|xotons|drunk|drunks|dayo|imani|kwasi|jabali|crew|chase": "\"Four Xotons! Disorderly! They broke a stool "
                "at the Turtle and arm-wrestled a fisherman into a barrel!\" He grips the spear. \"I'm right behind "
                "them. One tavern behind. Every time. I don't understand it.\"",
            "dominico|fist|gog|guild|stripperwitch": "He lowers his voice and his spear. \"Sergeant says we don't go there. "
                "Arithmetic, he says.\" He frowns. \"I don't think the Charter mentions arithmetic.\"",
            "harrow|sergeant|pell": "\"Sergeant Harrow fought twenty years on the Fronterian border! He's the best man in "
                "the watch.\" A pause. \"He's one of three. But he'd be the best of a hundred.\"",
            "rosa|quint": "\"Constable Quint knows everyone in town. Everyone! She says it's called intelligence work.\" He "
                "nods earnestly. \"She does a lot of it sitting down.\"",
            "sleep|bed|room|rooms|lodging|inn|stay|bunk": "\"The Touchy Unicorn's very respectable, citizen, and a copper. "
                "The Omberhulk's lively. Don't sleep in the street. Article Seven. Well, it's not an article. It's a "
                "sergeant's rule. Same thing.\"",
            "drink|ale|beer|thirsty|tavern|pub": "\"Not on duty!\" He looks a little wistful. \"The Turtle does the biggest "
                "beers. I'm going there now. Not to drink. To find Xotons. They'll have gone.\"",
            "news|rumour|rumours|gossip|happening|word": "\"Official news: the mayor is upriver on town business, dues payable "
                "at the Town Hall.\" His ears go pink. \"Unofficial news: nobody believes it, and Rosa says the Custodian "
                "goes in the Stripperwitch's side door. That's not illegal. I checked.\"",
            "doing|busy|tonight|plans|up": "\"Chasing four Xotons! The Turtle, then the Ogre, then the Omberhulk, then "
                "Harbour Street, then the market. I'll catch them by dawn.\" He thinks. \"Or they'll fall asleep. Either's "
                "an arrest.\"",
            "crime|report|thief|stolen|help|trouble|robbed": "He snaps upright. \"A crime? Report it, citizen! Who, what, "
                "where?\" He fumbles for a pencil he doesn't have. \"I'll remember it. I've a very good memory. The "
                "sergeant writes it down after.\"",
            "seen|missing|lost|shipmate|friend|met|anybody|anyone|person": "He straightens. \"A missing person! Article Six, "
                "duty to report!\" He looks for a pencil he doesn't have. \"Height? Beard? Xoton? They're all short and "
                "bearded. I'll ask at every tavern. I'm going to every tavern anyway. One behind.\"",
            "mango|ines|fruit|pay": "\"I pay for my mango. Every night. One copper.\" He looks a little sideways at nothing. "
                "\"Some people don't. That's between them and Article Two.\"",
        },
        "default_line": [
            "He frowns hard, as if the question were a suspicious character. \"That's not in the Charter. I'll ask the "
            "sergeant. He knows everything that isn't in the Charter.\"",
            "\"Can't stop, citizen!\" He is already looking past you down the street. \"Xotons! Somewhere! Probably the "
            "next tavern!\"",
            "\"I'm sure that's all in order.\" He doesn't look sure. \"Is it? Ask Constable Quint. She knows everybody's "
            "business. She says that's her job.\"",
            "He polishes a button with his sleeve while he thinks. \"I don't know. But I'll find out. Officially.\"",
        ],
        "routine": [
            {"at": 0.5, "place": "ogre", "doing": "He stands in the Rampant Ogre's doorway with his spear, demanding to know "
                "where the Xotons went. Everyone points in a different direction.",
             "go": "The gangling young watchman hears a crash from somewhere downhill, grips his spear and runs toward "
                   "the Ogre.",
             "beats": ["The young watchman asks the huge barman where four Xotons went. The barman points at the door. "
                       "The young watchman thanks him, formally, and does not leave."]},
            {"at": 1.5, "place": "omberhulk", "doing": "He stands in the Omberhulk looking at a broken stool and a puddle of "
                "beer, writing nothing down because he has nothing to write with.",
             "go": "The gangling watchman looks at a fresh puddle of beer, says \"Omberhulk!\" with total certainty, and "
                   "runs off uphill."},
            {"at": 2.25, "place": "harbour", "doing": "He walks Harbour Street from lamp to lamp, trying every shuttered door "
                "and saying good night to the cats.",
             "go": "The young watchman asks the nun which way the Xotons went, gets an answer he doesn't like, and walks "
                   "down toward Harbour Street with his spear on his shoulder."},
            {"at": 3.0, "place": "market", "doing": "He helps the stallholders of the Night Market stack their trestles, "
                "carrying three at a time and dropping one."},
            {"at": 4.0, "place": "square", "doing": "He stands at attention by the town pump in the last of the dark, very "
                "awake, guarding the square against nobody."},
            {"at": 6.0, "place": "lanes", "doing": "He sleeps in his mother's house in the Back Lanes, his coat hung up "
                "properly and his buttons laid out to polish."},
            {"at": 15.0, "place": "hall", "doing": "He stands in front of the Refuge Charter on the Town Hall wall, reading "
                "it again, his lips moving."},
            {"at": 18.0, "place": "square", "doing": "He walks the square as the evening comes on, touching his cap to "
                "everyone, keen as a new blade."},
            {"at": 20.5, "place": "market", "doing": "He walks the Night Market with his spear upright, stopping at a fruit "
                "stall to pay a copper for a mango, and making sure he is seen paying it.",
             "pay": {"to": "Mother Ines", "cp": 1, "for": "a mango, paid for"}},
            {"at": 22.0, "place": "square", "doing": "He walks the square with his spear upright and his ears out, looking "
                "for disorder and finding mostly cats."},
            {"at": 23.5, "place": "turtle", "doing": "He stands in the Turtle Dragon with his spear, looking at a stool "
                "broken by Xotons who left some minutes ago.",
             "go": "Somebody shouts that the Xotons are at the Turtle. The gangling young watchman is gone at a run "
                   "before they finish the sentence.",
             "beats": ["The gangling young watchman asks the one-eyed keeper which way the Xotons went. She tells him. "
                       "He goes the other way."]},
        ],
        "beats": [
            "The gangling young watchman stops a man for running, finds out he is late for his own wedding, and runs "
            "with him to make sure he gets there.",
            "The young watchman recites something under his breath that sounds like 'Article Three, Article Four', "
            "and straightens his cap.",
            "The gangling watchman rattles a shuttered door, finds it locked, and looks almost disappointed.",
            "Somebody across the room drops a tankard. The young watchman's spear comes down level, then goes back up, "
            "and his ears go red.",
        ],
    },

    "Constable Rosa Quint": {
        "look": "A comfortable woman of about thirty in a watch coat worn open over a laundress's blouse, a club "
                "hanging from her belt like an afterthought. She leans on things, chews things, and her eyes go "
                "everywhere, slow and amused.",
        "seen_as": "the watchwoman leaning on things",
        "brief": "You are Constable Rosa Quint of the Refuge watch. You came here as a girl with your mother, a laundress, "
                 "and grew up in the Back Lanes knowing every house by its washing, which is everybody's business. Your "
                 "mother once washed the Custodian's shirts and found Stripperwitch-red lip paint on the collars; you "
                 "have never forgotten it, nor told him. You joined the watch for the coat and the free fruit. You are "
                 "paid late and short, so you take small bribes to make it up: Hanklevode pays you five copper a night "
                 "to look the other way in the square, stallholders give you fruit, Ludo gives you a cheap rum. You know "
                 "everybody's business and sell it by the crumb. Your scheme: Lieutenant Voss pays you ten copper a "
                 "night for word of the elves, and you feed him crumbs ('out by the trees, somewhere') while knowing "
                 "exactly where they are: the Touchy Unicorn, whose laundry your cousin does. You are holding out for a "
                 "whole gold, and you have not decided whether you would ever really sell it. You stay out of Gog's way "
                 "and Dominico's, and you trail the drunk Xotons in no hurry. You like Sergeant Harrow, Abel (sweet, "
                 "hopeless), Ludo, and gossip. You dislike work, stairs, and the Custodian. Voice: slow drawl, 'love', "
                 "'between you and me', always knows a name. 'Between you and me, love.' 'I didn't see nothing. Five "
                 "copper says I still didn't.'",
        "scheme": "Sells Lieutenant Voss crumbs about the elves at ten copper a night while knowing they are at the "
                  "Touchy Unicorn; holding out for a whole gold, undecided whether she would ever sell it. Takes "
                  "Hanklevode's five copper to look away in the square.",
        "purse": 45,
        "dialog": {
            "name|names|introduce|yourself|constable": "\"Rosa Quint. Constable, technically.\" She takes a bite of "
                "somebody else's mango. \"And you're off the green fishing boat, came in at half nine, haven't paid "
                "for a bed yet. See? I know things.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": "\"Evening, love.\" She doesn't get off the wall she's "
                "leaning on. \"New face. I like new faces. They haven't got any business yet. Give it a day.\"",
            "from|home|born|lanes|mother|laundress|came|arrived|brought": "\"Came over as a little thing with my mam. She "
                "took in washing in the lanes.\" She grins. \"You learn a lot about a town from its shirts, love. Who's "
                "bleeding, who's courting, who's been where they say they haven't.\"",
            "work|job|trade|watch|guard|duty|law|patrol": "\"I keep an eye on things.\" She settles more comfortably. \"From "
                "here, mostly. Abel does the running. Sergeant does the gate and the worrying. I do the knowing.\"",
            "news|rumour|rumours|gossip|happening|word": "\"Between you and me, love?\" She leans in. \"The Custodian goes in "
                "the Stripperwitch side door every night. Tully's spending money he hasn't got. Husok's in a woodshed. "
                "That's free. The good stuff costs.\"",
            "bribe|bribes|coin|money|silver|price|pay": "\"I didn't see nothing.\" She holds out a palm without looking at "
                "it. \"Five copper says I still didn't.\"",
            "elves|elf|ithriel|hiding|hooded": "Her eyes slide away, slow. \"Elves? Out by the trees, somewhere. Lots of "
                "trees out there.\" She chews. \"Funny how many people want to know. Funny how much they'll pay.\"",
            "voss|officer|uniform|lieutenant|vorkath": "\"The lieutenant? Lovely manners. Pays in good silver.\" She looks "
                "at the mango, not at you. \"I tell him what I know. I know very little, slowly. A girl's got to eat, "
                "love.\"",
            "custodian|hall|shirts|collar|lip": "\"The Custodian?\" A slow, delighted smile. \"My mam used to wash his "
                "shirts. Red on the collars. Stripperwitch red.\" She taps her nose. \"Never been in the place, he "
                "says. Never.\"",
            "hanklevode|thief|pockets|coat": "\"The fellow with the pockets? Lovely man. Generous.\" She pats her own coat, "
                "which clinks. \"Admires the Town Hall. Lots of people admire the Town Hall. I don't ask.\"",
            "harrow|sergeant|abel|fitch": "\"Sergeant's honest, poor old thing. Abel's honest and doesn't know any better. "
                "That's two honest men in a watch of three.\" She shrugs. \"Somebody had to be the clever one.\"",
            "xoton|xotons|drunk|drunks|dayo|imani|kwasi|jabali|crew": "\"Four of them. Turtle, Ogre, Omberhulk, round "
                "and round like a dance.\" She yawns. \"Abel's chasing them. I'm letting him. They'll fall asleep by "
                "three. I'll arrest them then. Gently.\"",
            "dominico|fist|gog|guild|sabeth": "\"Gog's lot and Dominico's lot.\" She raises both hands, mango and all. "
                "\"I don't know them, love, they don't know me, and that's how I've lived to thirty.\"",
            "klhyt|mayor|founder|upriver": "For once she doesn't smile. \"Klhyt knew my mam's name. He knew everybody's "
                "name.\" She chews. \"Upriver, the notice says. Klhyt's shirts never came back with river mud on them. "
                "Not once.\"",
            "sleep|bed|room|rooms|lodging|inn|stay|bunk": "\"The Unicorn's a copper and quiet, if you like being looked at "
                "over spectacles. The Omberhulk's a copper and you'll be bitten. Or there's the bench in the Town Hall. "
                "That's where I sleep. It's free. Don't tell.\"",
            "drink|ale|beer|thirsty|tavern|pub|rum": "\"Ludo's at the Ogre pours me a rum at cost, love, for keeping the "
                "peace.\" She winks. \"I keep it very still. Nobody's ever disturbed it.\"",
            "doing|busy|tonight|plans|up": "\"Tonight? The market, a little rum, a little chat by the pump with a man in a "
                "nice coat, a sit-down at the Omberhulk, a lie-down at the Town Hall.\" She smiles. \"Busy night.\"",
            "seen|missing|lost|shipmate|friend|met|anybody|anyone": "\"Somebody gone missing?\" She brightens. \"Name, love, and "
                "two copper. If they're in town, somebody's washing their shirt.\" She holds out a hand. \"If they're not in "
                "town, it's four.\"",
            "warehouse|crate|brask|docks|bonded": "\"Brask? Four nights on that door, love. Eats there, sleeps there.\" She "
                "chews. \"Dominico pays him a copper a night more than they pay us. For a door. I'd like to know what's "
                "behind it worth that. I'd sell it, if I knew.\"",
            "unicorn|treeline|trees|wendeline|laundry": "\"The Unicorn?\" Her smile goes careful. \"My cousin does their "
                "laundry. Lot of sheets for a quiet inn, she says. Lot of very small shirts.\" She stops. \"That's not for "
                "sale. Not yet.\"",
        },
        "default_line": [
            "She shifts her weight to the other hip and keeps chewing. \"Couldn't say, love. Could sell it, maybe. "
            "Couldn't say it.\"",
            "\"That's somebody else's business.\" She smiles. \"I know whose. I'm not telling you whose. Not for free.\"",
            "She looks at you for a slow moment. \"Ask Abel. He'll tell you anything you like, and some of it'll even "
            "be the law.\"",
            "\"Mm.\" She yawns. \"Ask me later, love. I'm keeping the peace. It's very tiring, keeping it this still.\"",
        ],
        "routine": [
            {"at": 0.75, "place": "omberhulk", "doing": "She sits on the stairs of the Omberhulk with her coat open and her "
                "club on the step, trading whispers with two men who are not drinking.",
             "pay": {"to": "Sister Agathe", "cp": 2, "for": "a mead on the stairs"},
             "go": "The watchwoman pockets something, yawns, and wanders across the square to the Omberhulk.",
             "beats": ["The lazy watchwoman says something behind her hand to the two quiet men on the stairs. One of them "
                       "writes it down. She looks pleased with herself, and then, briefly, not."]},
            {"at": 2.0, "place": "market", "doing": "She strolls the Night Market as it begins to pack up, collecting "
                "bruised fruit the sellers would only throw away.",
             "go": "The watchwoman heaves herself up off the stairs, says good night to everybody by name, and drifts down "
                   "toward the market."},
            {"at": 3.0, "place": "hall", "doing": "She sleeps on the bench in the Town Hall's entrance hall with her coat "
                "over her face, under the founder's portrait.",
             "go": "The watchwoman tucks two bruised mangoes in her coat and ambles off uphill toward the Town Hall."},
            {"at": 6.0, "place": "lanes", "doing": "She sleeps in her mother's old house in the Back Lanes, washing lines "
                "strung across the yard."},
            {"at": 15.0, "place": "lanes", "doing": "She sits in a laundry yard in the Back Lanes with the washerwomen, "
                "learning everything that happened in town today."},
            {"at": 18.0, "place": "square", "doing": "She leans on the town pump in the square, chewing, watching who goes "
                "into which tavern."},
            {"at": 20.0, "place": "market", "doing": "She leans on a fruit stall in the Night Market eating a mango she did "
                "not pay for, watching the crowd with slow, amused eyes."},
            {"at": 23.5, "place": "ogre", "doing": "She leans on the end of the Ogre's bar with a rum she paid half for, "
                "watching four drunk Xotons and not arresting any of them.",
             "go": "The watchwoman finishes someone else's mango, wipes her fingers on her coat, and ambles off toward "
                   "Harbour Street.",
             "pay": {"to": "Big Ludo", "cp": 2, "for": "two rums at cost, on duty"}},
            {"at": 23.75, "place": "square", "doing": "She leans on the town pump in the lamplight, looking at nothing, while "
                "people who want things stop beside her and go away lighter.",
             "go": "The watchwoman tips back the last of her rum, nods to the barman, and strolls up toward the square, "
                   "in no hurry at all.",
             "beats": ["A man in a pressed uniform stops at the pump and speaks to the watchwoman without looking at her. "
                       "She answers without looking at him. A coin changes hands.",
                       "The watchwoman by the pump counts the coins in her palm, frowns, and looks toward the treeline "
                       "for a long moment before she puts them away."]},
        ],
        "beats": [
            "The watchwoman leaning on the wall greets three passers-by by name, asks one after her sister's baby, and "
            "tells another his wife was looking for him at the Turtle.",
            "A stallholder hands the lazy watchwoman a mango without being asked. She takes it without saying thanks. "
            "Neither of them seems to think anything of it.",
            "The watchwoman watches a hooded figure hurry past, and says nothing, and goes on chewing, and watches where "
            "it goes.",
            "Somebody presses a coin into the watchwoman's hand in passing. She looks the other way, very thoroughly.",
        ],
    },
}

# ---- new people: the Custodian's town watch (SRD guard: AC 16, chain shirt and shield, hp 11, Perception +2) -------
NEW = {
    "Sergeant Pell Harrow": {
        "type": "guard", "people": "human", "faction": "the Refuge", "home": "gate",
        "scores": {"str": 13, "dex": 12, "con": 12, "int": 10, "wis": 11, "cha": 10}, "skills": {"perception": 1, "insight": 1}, "hp": 11, "srd": "guard",
        "carries": [["Spear", "spear", "A watch spear with a long ash shaft, the head worn bright from years of whetting."],
                    ["Club", "club", "An old oak truncheon, the grip wrapped in cord gone black with use."],
                    ["Gate keys", None, "Two iron keys on a ring: the Town Gate's. Klhyt's own, once."],
                    ["Watch book", None, "A swollen ledger of the watch, every cart, drunk and debt in pencil, and a "
                                         "column headed OWED."]],
    },
    "Constable Abel Fitch": {
        "type": "person", "people": "human", "faction": "the Refuge", "home": "square",
        "scores": {"str": 13, "dex": 12, "con": 12, "int": 10, "wis": 11, "cha": 10}, "skills": {"perception": 1, "athletics": 1}, "hp": 11, "srd": "guard",
        "carries": [["Spear", "spear", "A watch spear held so upright it might be a flagpole, the shaft freshly oiled."],
                    ["Club", "club", "A new oak truncheon, never yet used on anybody."]],
    },
    "Constable Rosa Quint": {
        "type": "person", "people": "human", "faction": "the Refuge", "home": "square",
        "scores": {"str": 13, "dex": 12, "con": 12, "int": 10, "wis": 11, "cha": 10}, "skills": {"perception": 1, "insight": 1}, "hp": 11, "srd": "guard",
        "carries": [["Club", "club", "An oak truncheon that hangs from her belt like an afterthought."],
                    ["Bruised mango", None, "A mango she did not pay for, going soft."]],
    },
}

