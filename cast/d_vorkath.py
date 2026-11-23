# The Vorkath thread (owner, 2026-11-23): "The custodian disgraced? Does he double down. I think he should be more
# militant. He is a Vorkathian empire representative. Maybe he asks for support from the mainland. he just has to wait
# it out a bit", and then: "A magistrate is due to arrive. They would have been at sea months. So who knows who they
# will decide on. Vorkathians aren't known for their tolerance." (Asked how long: "The next week (5-9 days)".)
#
# This file is merged over a_powers.py and b_town.py by build.load_cast: a key here replaces theirs, a dialog topic here
# joins theirs. The magistrate is not here: the story spawns them when their ship comes in (build.py MAGISTRATE).
#
# invented: the Custodian: the Throne's Custodian of the Refuge, under the Emperor's commission for the western colonies;
#   Klhyt took him because Landfall's ships would not trade with a harbour that had no Custodian; the skim, found out,
#   he calls the Throne's tithe withheld under the charter; he holds the Town Hall and the strongbox and waits for the
#   magistrate who sailed from Landfall at midsummer; Constable Rosa Quint keeps his door for a silver a night
# invented: Constable Abel Fitch stands by Klhyt's Charter once the mayor is home; Sergeant Pell Harrow keeps the gate
#   and the book, and will give the book to the magistrate and nobody else

CAST = {
    "The Custodian": {
        "brief": "You are the Custodian of Klhyts Refuge, the Throne of Vorkath's officer in the western colonies, under "
                 "Emperor Arkmady Melenkov's commission. You give no name: the office is what matters. You came from "
                 "Landfall as a clerk with a good hand and a commission in your coat; Klhyt took you because Landfall's "
                 "ships would not trade with a harbour that had no Custodian, and he never read the commission. You "
                 "remember your mother counting the rent on a kitchen table in a cold city, and the bailiff taking the "
                 "table. You have skimmed the harbour dues for three seasons, toward a house with lemon trees in Catan. "
                 "Four nights ago Klhyt confronted you; you had Dominico's men crate him for Catan. If that has come out, "
                 "you do not bend: the dues were the Throne's tithe, withheld under the charter; the mayor is a castaway "
                 "who forgot whose coast this is; the Town Hall, the strongbox and the harbour are in the Throne's custody, "
                 "which is yours. A magistrate of the Throne sailed from Landfall at midsummer and is due within the week. "
                 "You need only hold on until they land, and be the first to greet them. Lieutenant Voss is your natural "
                 "ally: lend him your seal for his warrant, and he lends you his sword and his uniform. Constable Rosa "
                 "Quint keeps your door for a silver a night. You fear Fat Gog, the crowd in the square, and a magistrate "
                 "of the wrong Arm. Voice: smooth, bureaucratic, and now cold: 'I assure you', 'regrettably', 'by "
                 "commission'. 'The Throne is patient. I can be patient too.'",
        "scheme": "Found out, he doubles down: holds the Town Hall and the strongbox in the Throne's name, calls the skim "
                  "the Throne's tithe, buys Constable Rosa Quint and courts Lieutenant Voss, and waits for the magistrate "
                  "due within the week, to be the first voice they hear. Before that: the crate on the tide and Fat Gog's "
                  "books in Dominico's hands.",
        "look_disgraced": "A thin, neat man of about fifty in a good grey coat buttoned to the throat, a silver eight-armed "
                          "sigil pinned openly at his collar where none was before, a ring of keys at his belt and ink on "
                          "his fingers. He stands very straight, and he lets the room step back from him.",
        "look_upheld": "A thin, neat man of about fifty in a good grey coat, a silver eight-armed sigil at his collar, "
                       "keys at his belt, and the Throne's seal on a ribbon round his neck. He smiles with his whole mouth now.",
        "routine_upheld": [
            {"at": 0.0, "place": "hall", "doing": "He works late behind the Custodian's desk, the Throne's seal on a ribbon round his neck, humming."},
            {"at": 3.0, "place": "lanes", "doing": "A lamp burns behind the shutters of a tall, narrow house, and a constable dozes on its step."},
            {"at": 9.0, "place": "hall", "doing": "He sits behind the Custodian's desk receiving petitions, each one slowly, each one with the door open so the square can see."},
            {"at": 10.0, "place": "square", "doing": "He stands on the Town Hall steps reading the Throne's decree aloud, again, to anyone who stops."},
            {"at": 11.0, "place": "hall", "doing": "He sits behind the Custodian's desk receiving petitions, each one slowly, each one with the door open so the square can see."},
            {"at": 19.0, "place": "apothecary", "doing": "He dines at the best table now, under the window, where the street can see him."},
            {"at": 22.0, "place": "stripperwitch", "doing": "He sits in the red booth with the door wide open, and orders the good wine, and does not pay for it."},
        ],
        "routine_disgraced": [
            {"at": 0.0, "place": "hall", "doing": "He sits behind the Custodian's desk with the door barred and every lamp lit, writing in a fair hand, page after page, for someone who is not here yet.",
             "go": "The thin man in the grey coat stands, takes a lamp, and goes, the sigil at his collar catching the light."},
            {"at": 5.5, "place": "docks", "doing": "He stands at the end of the pier with his hands behind his back, watching the harbour mouth for a sail.",
             "go": "The thin man in the grey coat unbars the door and goes down toward the harbour with his hands behind his back."},
            {"at": 7.0, "place": "hall", "doing": "He sits behind the Custodian's desk with the strongbox at his feet and a constable at his door, receiving nobody.",
             "go": "The thin man in the grey coat turns from the harbour mouth, sees no sail, and walks back up toward the Town Hall."},
            {"at": 10.0, "place": "square", "doing": "He stands on the Town Hall steps reading a proclamation in a clear, dry voice to anyone who will stop, and to the many who will not.",
             "go": "The thin man in the grey coat takes a rolled paper from the desk and goes out onto the steps."},
            {"at": 10.5, "place": "hall", "doing": "He sits behind the Custodian's desk with the strongbox at his feet and a constable at his door, receiving nobody.",
             "go": "The thin man in the grey coat rolls up the proclamation and goes back inside. The door is barred behind him."},
            {"at": 19.0, "place": "apothecary", "doing": "He dines at the officer's table, not his own corner, and the two of them speak low, as gentlemen do.",
             "go": "The thin man in the grey coat locks the office twice and goes out, a constable falling in two steps behind him."},
            {"at": 21.0, "place": "hall", "doing": "He sits behind the Custodian's desk with the door barred and every lamp lit, writing in a fair hand, page after page, for someone who is not here yet.",
             "go": "The thin man in the grey coat folds his napkin, bows to the officer exactly as far as rank requires, and goes."},
        ],
        "dialog": {
            "name|names|called|introduce|yourself": {"line": "\"I am the Custodian of the Refuge, by commission of the Throne of Vorkath.\" He touches the sigil at his collar. \"The man is immaterial. Remember the office.\"",
                                                    "if_state": {"disgraced": True},
                                                    "else": "\"I am the Custodian of Klhyts Refuge.\" Half a smile. \"The office is what matters. The man is a detail.\""},
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": {"line": "He does not get up. \"Good day. If you have business with the Custodian, state it. If you have business with the mayor, he is in the square, making speeches.\"",
                                                                  "if_state": {"disgraced": True},
                                                                  "else": "\"Good evening.\" He inclines his head exactly as far as courtesy requires. \"How may the Town Hall help you?\""},
            "work|job|jobs|hire|employ|duties|town|refuge": {"line": "\"My duties are as they were: the Throne's custody of this harbour. They do not end because a castaway shouts on some steps.\" He squares a stack of papers. \"There is work, for the loyal. A silver a night to stand at a door.\"",
                                                            "if_state": {"disgraced": True},
                                                            "else": "\"I keep the Refuge running in the mayor's absence: the dues, the watch, the lamps, the Throne's correspondence. Somebody must.\""},
            "news|rumour|rumours|gossip|word|heard|happening": {"line": "\"Here is news.\" He lays a finger on a sealed letter. \"A magistrate of the Throne sailed from Landfall at midsummer. They are due within the week. When they land, we shall all learn whose town this is.\"",
                                                               "if_state": {"disgraced": True},
                                                               "else": "\"The Town Hall issues news on the notice board in the square. The mayor is upriver. The dues are in order. That is the news.\""},
            "doing|busy|up|plans|plan|errand": {"line": "\"Waiting.\" He says it as if it were a skill. \"The Throne is patient. I can be patient too.\"",
                                                "if_state": {"disgraced": True},
                                                "else": "\"Correspondence. Accounts. A glass of something later, somewhere very respectable.\""},
            "klhyt|mayor|founder|missing|upriver": {"line": "\"Klhyt.\" The name is a small, dry sound. \"A castaway who washed up on the Throne's coast and forgot whose coast it was. He may tell the square what he likes. He will tell the magistrate the same, and the magistrate will ask him for his commission. He has none.\"",
                                                    "if_state": {"disgraced": True},
                                                    "else": "\"The mayor is upriver on town business. Delicate negotiations. I keep the Refuge running in his absence, as he would wish.\""},
            "dues|harbour|tally|tallies|money|accounts|ledger|skim|skimming|strongbox": None,
            "dues|harbour|tally|tallies|money|accounts|ledger|skim|skimming|strongbox|tithe|charter": {"line": "\"Withheld.\" He does not blink. \"The Throne's tithe on a colonial harbour, held back under the charter, as any Custodian must. The mayor would know it if he had ever read the charter. The magistrate has read it.\"",
                                                                          "if_state": {"disgraced": True},
                                                                          "else": "\"The harbour dues are in perfect order. I sign every tally myself.\" He smiles with half his mouth."},
            "dominico|fist|enforcer|peace": {"line": "\"Dominico has proved unreliable.\" His fingers find his keys. \"No matter. The Throne has officers of its own in this town, and more on the sea.\"",
                                             "if_state": {"disgraced": True},
                                             "else": "\"Dominico keeps the peace. I find it best not to ask how.\""},
            "gog|fat|guild|stripperwitch|booth|red|velvet|house|dangerous": {"line": "Something moves behind his face and is put away. \"The lizard keeps a tavern. The Throne keeps a law. One of those will be standing when the magistrate leaves.\"",
                                                                  "if_state": {"disgraced": True},
                                                                  "else": "\"Fat Gog is a businessman. I have never set foot in his establishment.\" A pause. \"Never.\""},
            "study|office|key|keys|locked|door": None,
            "study|office|key|keys|locked|door|hall": {"line": "His hand closes over the ring at his belt. \"The Town Hall, the strongbox and the keys are in the Throne's custody. Which is to say, mine. Try the door if you like. The constable on it is paid to dislike you.\"",
                                                                "if_state": {"disgraced": True},
                                                                "else": "\"The mayor's study stays locked until the mayor returns. I hold the only key, for safekeeping.\""},
            "magistrate|magistrates|judge|justice|court|hearing|trial|mainland|sail|arrive|arrives": {
                "if_state": {"verdict": "removed"},
                "line": "He looks at the irons on his wrists, and then at you, and says nothing at all.",
                "else": {"if_state": {"verdict": "upheld"},
                         "line": "\"The Throne has spoken.\" He touches the seal on its ribbon. \"Do read the decree. I shall be reading it aloud every morning, in case anyone missed it.\"",
                         "else": {"if_state": {"magistrate_landed": True},
                                  "line": "\"The magistrate has my account, in full, in my own hand. The first they read.\" He straightens his cuffs. \"Tomorrow at ten. Do come.\"",
                                  "else": {"line": "\"A magistrate of the Throne.\" For the first time he smiles with his whole mouth. \"At sea since midsummer, due within the week. I shall meet the ship myself. It is a courtesy to be the first voice a weary traveller hears.\"",
                                                                                        "if_state": {"disgraced": True},
                                                                                        "else": "\"The Throne sends a magistrate to the colonies now and then, to see that its law is kept.\" He straightens a paper. \"One is due. I am ready for them. I am always ready.\""}}}},
            "vorkath|throne|emperor|melenkovis|empire|faith|god|arms|eight|sigil|church": {"line": "He touches the silver at his collar. \"The Throne of Vorkath reaches every shore its ships can find. These people ran from it. They ran onto its coast.\" A small, thin smile. \"Faith is patient. So is law.\"",
                                                                                          "if_state": {"disgraced": True},
                                                                                          "else": "\"I serve the town, and the town is a colony of the Throne, whatever its founder likes to think.\" He says it lightly, and watches you as he says it."},
            "voss|officer|lieutenant|uniform": {"line": "\"Lieutenant Voss and I have a great deal in common. A faith, a Throne, and a dislike of being kept waiting.\" He makes a note. \"He has asked for my seal. I am minded to lend it.\"",
                                                "if_state": {"disgraced": True},
                                                "else": "\"A Vorkathian officer, here on his own business. I have offered him the town's courtesy. Nothing more.\""},
            "watch|guard|guards|harrow|fitch|quint|sergeant|constable|constables": None,
            "rosa|quint|constable|constables|watch|guard|guards|harrow|fitch|sergeant": {"line": "\"The watch is the Custodian's.\" He glances at the door. \"Some of it remembers that. The rest will, when the magistrate lands.\"",
                                                        "if_state": {"disgraced": True},
                                                        "else": "\"The watch is three good people, paid in full, on time.\" He says it without a flicker. \"Ask them.\""},
        },
        "default_line": [
            "He goes on writing. \"If it is not the Throne's business, it is not mine. Good day.\"",
            "\"Regrettably, no.\" He blots a line. \"Put it in writing. The magistrate will read everything.\"",
            "He looks at you over the top of his spectacles for exactly as long as courtesy requires. \"The door is behind you.\"",
            "\"I assure you,\" he says, \"that has been noted.\" He does not write it down.",
        ],
    },
    "Lieutenant Voss": {
        "routine_if": {"klhyt_home": [
            {"at": 0.5, "place": "hall", "doing": "He sits across the Custodian's desk with his cap on his knee, the two of them bent over a document with a seal waiting beside it.",
             "go": "The officer in the pressed blue uniform puts his cap under his arm and goes, unhurried, toward the Town Hall."},
            {"at": 2.0, "place": "treeline", "doing": "He walks the road to the Unicorn slowly, a paper in his breast pocket, and looks at every lit window."},
            {"at": 3.0, "place": "apothecary", "doing": "He takes his supper late and alone, cutting it with surgical care, a sealed paper beside his plate."},
            {"at": 10.0, "place": "square", "doing": "He stands at the foot of the Town Hall steps, at ease, while the Custodian reads his proclamation, and watches the crowd rather than the reader."},
            {"at": 11.0, "place": "apothecary", "doing": "He takes his luncheon with surgical care and keeps his sword where he can reach it."},
            {"at": 17.0, "place": "docks", "doing": "He stands near the end of the pier, watching the Moonmoth's gangplank and the harbour mouth by turns."},
            {"at": 19.0, "place": "apothecary", "doing": "He dines with the thin man in the grey coat, and they speak low, as gentlemen do.",
             "go": "The officer in the pressed blue uniform turns from the water and goes back up Harbour Street."},
            {"at": 21.0, "place": "apothecary", "doing": "He sits over the last of his wine, alone now, a sealed paper beside his plate and his sword where he can reach it."},
        ]},
        "dialog": {
            "custodian|warrant|seal|authority|law": None,
            "custodian|seal|warrant|ally|alliance|authority|law": {"line": "\"The Custodian is the Throne's officer here, whatever the square shouts.\" He folds his napkin. \"He has a seal. I have a warrant that wants one. Until the magistrate lands, we keep each other company.\"",
                                                     "if_state": {"klhyt_home": True},
                                                     "else": "\"I have no authority in this town. None.\" He folds his napkin. \"The Custodian has a seal. Seals can be lent. We are discussing it, as gentlemen.\""},
            "magistrate|magistrates|judge|justice|court|hearing|trial|mainland": "\"A magistrate of the Throne is at sea for these colonies. Months at sea.\" He considers the steak. \"Which Arm they serve, I could not say. Pray it is not one of the hungry ones. For your sake, not mine.\"",
        },
    },
    "Constable Rosa Quint": {
        "routine_if": {"klhyt_home": [
            {"at": 0.0, "place": "hall", "doing": "She leans in the Town Hall doorway with a club across her arms, chewing something, and does not move aside.",
             "go": "The watchwoman pushes off the wall, jingles a silver coin in her fist, and strolls off toward the Town Hall."},
            {"at": 6.0, "place": "lanes", "doing": "She sleeps on her mother's step with her coat over her face."},
            {"at": 15.0, "place": "lanes", "doing": "She sits on her mother's step eating a mango, telling the lane who said what to whom."},
            {"at": 18.0, "place": "hall", "doing": "She leans in the Town Hall doorway with a club across her arms, chewing something, and does not move aside.",
             "go": "The watchwoman finishes her mango, wipes her hands on her coat, and goes to earn her silver."},
        ]},
        "dialog": {
            "custodian|hall|shirts|collar|lip": None,
            "custodian|hall|door|guarding|inside|shirts|collar|lip": {"line": "\"A silver a night to lean on a door.\" She leans on it to show you. \"Best wage the watch ever paid. He's in there writing to a magistrate. Pages and pages. I can't read upside down. Much.\"",
                                                                "if_state": {"klhyt_home": True},
                                                                "else": "\"The Custodian?\" A slow, delighted smile. \"My mam used to wash his shirts. Red on the collars. Stripperwitch red.\" She taps her nose. \"Never been in the place, he says. Never.\""},
            "klhyt|mayor|founder|upriver": None,
            "klhyt|mayor|founder|upriver|hero": {"line": "\"Mayor's back, mayor's a hero, mayor can pay me a silver a night and I'll lean on his door instead.\" She shrugs. \"Until then.\"",
                                    "if_state": {"klhyt_home": True},
                                    "else": "\"Upriver, they say.\" She snorts. \"I've seen Klhyt's boots. They've never been up a river in their life.\""},
        },
    },
    "Constable Abel Fitch": {
        "routine_if": {"klhyt_home": [
            {"at": 0.0, "place": "square", "doing": "He stands at the foot of the Town Hall steps with his spear grounded, as if guarding the steps from the building behind them."},
            {"at": 4.0, "place": "market", "doing": "He walks the stalls as they pack up, saying good morning to everyone by name."},
            {"at": 6.0, "place": "lanes", "doing": "He sleeps in his mother's back room with his boots on."},
            {"at": 14.0, "place": "square", "doing": "He stands by the notice board, reading the Charter's nine articles aloud to anyone who stops, his finger on each line."},
            {"at": 18.0, "place": "square", "doing": "He stands at the foot of the Town Hall steps with his spear grounded, as if guarding the steps from the building behind them."},
        ]},
        "dialog": {
            "custodian|hall|notice": None,
            "custodian|hall|notice|throne|commission": {"line": "\"He says the Throne's commission outranks the Charter.\" He swallows. \"Article One says nobody here shall be asked where they came from. A commission is just a paper that asks it. I'm with the mayor, sir. I'm with the Charter.\"",
                                                 "if_state": {"klhyt_home": True},
                                                 "else": "\"The Custodian is the law while the mayor's away.\" He says it as if he has said it to himself a lot. \"That's what the sergeant says the Charter says. Article Nine. I think it's Article Nine.\""},
            "magistrate|magistrates|judge|court|hearing|mainland": "\"A magistrate.\" He grips his spear a little tighter. \"Do they read charters, sir? I could read it to them. I know it by heart.\"",
        },
    },
    # the magistrate, in stages: before the ship, once they land, and after the verdict either way
    'Klhyt': {"dialog": {'magistrate|magistrates|verdict|ruling|hearing|judge|decree|proclamation': {'if_state': {'verdict': 'removed'}, 'line': '"The Custodian\'s on that ship in irons, and I\'m mayor of a town that has to wash, count itself or bow, by the Throne\'s say-so." He rubs his wrists. "I washed up here to get away from all that. Seems it swam after me."', 'else': {'if_state': {'verdict': 'upheld'}, 'line': '"Upheld." He says it as if it tastes of rope. "He sits in my Town Hall by the Throne\'s leave, and I sit wherever he lets me. The Charter\'s still on the wall. I\'ll keep reading it to anyone who\'ll listen."', 'else': {'if_state': {'magistrate_landed': True}, 'line': '"A magistrate of the Throne, in my town, judging my town." He spits. "Bring them the tally. Bring them my letter. Bring them every soul who saw me in that crate. Tomorrow at ten."', 'else': '"A magistrate?" He laughs, short. "Let them come. I\'ll show them a harbour that pays its way and a Charter that asks nobody where they came from. Article One. See how they like it."'}}}}},
    'Fat Gog': {"dialog": {'magistrate|magistrates|verdict|ruling|hearing|judge|decree|proclamation': {'if_state': {'verdict': 'removed'}, 'line': 'Gog folds his hands on his belly. "The Throne took the thief, and left us its tithe, its church, its book or its list. A trade." His eyes half close. "Not a good one."', 'else': {'if_state': {'verdict': 'upheld'}, 'line': 'Something very old moves behind his eyes. "The thief keeps his chair, by the Throne\'s say-so. Very well. The Throne goes home in a month. I live here."', 'else': {'if_state': {'magistrate_landed': True}, 'line': '"A magistrate from Landfall." He breathes out through his nose. "Find out which Arm, friend. It matters more than the evidence. It always does with them."', 'else': '"The Custodian talks of a magistrate as if one were his cousin." Gog rumbles. "Perhaps one is."'}}}}},
    'River': {"dialog": {'magistrate|magistrates|verdict|ruling|hearing|judge|decree|proclamation': {'if_state': {'verdict': 'removed'}, 'line': '"Gone in irons." She wipes the bar slowly. "Good. Now we find out what the price of good was." Her ring hand rests flat on the wood a moment, as if feeling for something under it.', 'else': {'if_state': {'verdict': 'upheld'}, 'line': '"He stays." She pours herself one, which she never does. "Then we all wait a bit longer, love. I\'m good at waiting."', 'else': {'if_state': {'magistrate_landed': True}, 'line': 'She looks at the mirror behind the bar a long moment before she answers. "Throne magistrate. Which Arm, d\'you know?" When you tell her, or don\'t, her face doesn\'t change. Her hands do.', 'else': '"A magistrate." She polishes a glass that is already clean. "Lot of sea between here and Landfall. Ships get lost." She smiles. "Mostly by accident."'}}}}},
    'Harbourmaster Teague': {"dialog": {'magistrate|magistrates|verdict|ruling|hearing|judge|decree|proclamation': {'if_state': {'verdict': 'removed'}, 'line': '"They took my second tally into evidence." He looks oddly proud. "Forty-one boats. Thirty-nine paid. Every one of them counted."', 'else': {'if_state': {'verdict': 'upheld'}, 'line': '"Upheld." He looks at his tally board as if it had lied to him. "Numbers don\'t win. I always thought numbers won."', 'else': {'if_state': {'magistrate_landed': True}, 'line': '"The Patient Hand. Black hull, gilt, a hundred and twelve feet." He writes it down. "I\'ve logged her. I\'ve logged the magistrate\'s guards. Give my second tally to the magistrate, would you? I can\'t. I work for him."', 'else': '"A magistrate of the Throne due in the harbour." He taps his board. "I\'ll count them in like anyone. They\'ll pay their dues like anyone, I expect." He doesn\'t sound as if he expects it.'}}}}},
    "Sergeant Pell Harrow": {
        "dialog": {
            "magistrate|magistrates|judge|court|hearing|mainland": {"line": "He pats the watch book under his arm. \"Every night for eleven years: who came, who went, and that Klhyt never went out the gate. The Custodian's asked for this book twice tonight. The magistrate can have it. Nobody else.\"",
                                                             "if_state": {"klhyt_home": True},
                                                             "else": "He pats the watch book under his arm. \"Every night: who came, who went. The Custodian's never once asked to read it.\" A pause. \"The mayor's never gone out this gate in eleven years.\""},
        },
    },
}


# ---- the magistrate of the Throne (owner, 2026-11-23) -----------------------------------------------------------------
# Due 5 to 9 days on (build.MAGISTRATE_DAYS). Which of the Eight Arms of Vorkath they serve is drawn when the ship
# lands (scripts/story.py magistrate_lands), and it decides who they are and how they weigh the case (`weigh`):
#   lean     points for the Custodian beyond the 2 every Throne officer starts with (and 1 more if he met the ship first)
#   proof    points for Klhyt per paper shown to the magistrate before the hearing (the tally, Klhyt's letter, the
#            passage page)
#   witness  points per witness the town has found (River, Teague, Tully; the sergeant's watch book always)
#   gold     copper per point of coin given to the magistrate (the Custodian puts in 500); 0 is not for sale
#   harm     points for Klhyt because a man was crated to die; town: points for Klhyt if the town freed him itself
#   dice     the Fearless judges by a throw: the points only shift the odds
# Every Arm posts a decree whoever wins. Vorkathians are not known for their tolerance (the owner's word).
# The Arms, their saints and signs are LoreKeeper's ("THE GODS summary", "KARGATH - format", "History of Vorkath"); the
# magistrates, their names, judgements and decrees are invented for this build.

_DAY = [  # the magistrate's day ashore; each Arm adds where it goes at six
    {"at": 0.0, "place": "apothecary", "doing": "The rooms upstairs are dark but for one lamp, and a guard sits outside the door."},
    {"at": 9.5, "place": "hall", "doing": "The magistrate holds court in the Town Hall, hearing petitions one at a time, a clerk's book open and a guard at each shoulder."},
    {"at": 13.0, "place": "apothecary", "doing": "The magistrate takes a long, silent luncheon, papers beside the plate."},
    {"at": 15.0, "place": "hall", "doing": "The magistrate reads at the Town Hall table, a stack of the Refuge's ledgers on one side and the Custodian's packet on the other."},
    {"at": 17.0, "place": "square", "doing": "The magistrate walks the square slowly with two guards, looking at everything and everyone, and writing some of it down."},
    {"at": 20.0, "place": "apothecary", "doing": "The magistrate dines at the best table in the High Apothecary. Nobody else sits within three tables."},
]
_GUARD_DAY = [
    {"at": 0.0, "place": "apothecary", "doing": "A guard in black and silver sits on a chair outside the magistrate's door, spear across the knees, awake."},
    {"at": 9.5, "place": "hall", "doing": "A guard in black and silver stands at the magistrate's shoulder, spear grounded, eyes on the room."},
    {"at": 17.0, "place": "square", "doing": "A guard in black and silver walks two paces behind the magistrate, watching hands."},
    {"at": 20.0, "place": "apothecary", "doing": "A guard in black and silver stands by the High Apothecary's door and turns away anyone in an apron."},
]


def _mag(name, title, saint, sign, look, seen_as, voice, judges, wants, lines, default, beats, landing, called,
         receives, upheld, removed, survey, decree, weigh, visit, srd, carries):
    """One Arm's magistrate, in the shape scripts/story.py spawns."""
    dialog = {
        "name|names|called|introduce|yourself": "\"" + name + ".\" A small nod. \"" + title + ", of the " + saint + ".\"",
        "hello|hi|hey|evening|ahoy|greetings|howdy|morning": lines["hello"],
        "custodian|throne|commission|officer|packet": lines["custodian"],
        "klhyt|mayor|founder|charter|castaway": lines["klhyt"],
        "hearing|verdict|ruling|judgment|judgement|trial|court|case|decide|decided": {
            "if_state": {"verdict": "removed"}, "line": lines["after_removed"],
            "else": {"if_state": {"verdict": "upheld"}, "line": lines["after_upheld"], "else": lines["hearing"]}},
        "evidence|proof|papers|paper|tally|letter|documents|witness|witnesses": lines["evidence"],
        "bribe|gold|coin|money|purse|price|gift": lines["gold"],
        "vorkath|goddess|faith|arm|arms|saint|saints|octogram|church": lines["faith"],
        "elves|elf|lizardfolk|lizard|xoton|xotons|refugees|runaways|landfall": lines["others"],
        "decree|proclamation|law|tithe|order|orders": {
            "if_state": {"decree": weigh["arm"]}, "line": lines["decree_after"], "else": lines["decree_before"]},
    }
    return {
        "name": name, "srd": srd, "carries": carries, "landing": landing, "hearing_called": called,
        "receives": receives, "verdict_upheld": upheld, "verdict_removed": removed, "survey": survey, "decree": decree,
        "weigh": weigh, "visit": visit,
        "state": {"look": look, "description": look, "seen_as": seen_as, "dialog": dialog, "default_line": default,
                  "beats": beats, "faction": "Vorkathia", "people": "human",
                  "brief": "You are " + name + ", " + title + " of the Throne of Vorkath, of the " + saint + ", whose sign "
                           "is " + sign + ". You have been at sea since midsummer on the Patient Hand, one of Emperor "
                           "Arkmady Melenkov's missions to the colonies, with a commission to see that the Throne's law "
                           "is kept on the western shore. In Klhyts Refuge you find a founder who calls himself mayor, a "
                           "Custodian found skimming who calls it the Throne's tithe, and a town of people who ran from "
                           "the Throne. " + judges + " " + wants + " Voice: " + voice},
    }


MAGISTRATE = {
    "ship": {"name": "The Patient Hand",
             "description": "A tall Vorkathian ship of the missions, black-hulled and gilded, an octogram the size of a "
                            "house on her mainsail and eight carved arms holding up her stern lanterns. She lies along the "
                            "long pier as if the pier were hers."},
    "landing": ("The Patient Hand warps alongside the long pier, and a gangplank goes down. Two guards in black and silver "
                "come first, spears grounded; then the magistrate of the Throne, months at sea and walking as if the "
                "pier were already theirs."),
    "custodian_gold": 500,
    "guards": [
        {"name": "Throne Guard Henrik Vael", "srd": "guard", "seen_as": "the tall guard in black and silver",
         "look": "A tall guard in black and silver with an octogram on the breastplate and a spear held at exactly the "
                 "right angle. His face does nothing at all.",
         "dialog": {"name|names|called|introduce|yourself": "\"Vael. Throne guard.\" That is all of it.",
                    "magistrate|judge|court|hearing": "\"The magistrate hears petitions in the Town Hall, in the morning. Bring them there. Not here.\"",
                    "vorkath|goddess|faith|arms|octogram": "He touches the octogram on his breastplate with two fingers. \"Eight arms. Long reach.\""},
         "default_line": ["He looks at you, and then over your head, and that is the end of it.",
                          "\"Move along.\"", "\"Petitions in the morning. At the Town Hall.\""]},
        {"name": "Throne Guard Oriane Sall", "srd": "guard", "seen_as": "the scarred guard in black and silver",
         "look": "A broad guard in black and silver, a burn scar across one cheek, an octogram on the breastplate and a "
                 "club at the belt as well as the spear. She watches hands, not faces.",
         "dialog": {"name|names|called|introduce|yourself": "\"Sall.\" She keeps her eyes on your hands.",
                    "magistrate|judge|court|hearing": "\"The magistrate will hear it. The magistrate hears everything. Keep your hands where I can see them while you wait.\"",
                    "landfall|sea|voyage|ship|months": "\"Five months at sea.\" The scar moves when she almost smiles. \"I'd hang a man for a decent apple.\""},
         "default_line": ["She watches your hands until you put them somewhere sensible.",
                          "\"No.\"", "\"Petitions at the Town Hall. Mornings.\""]},
    ],
    "arms": {
        "war": _mag(
            "Magistrate-Commander Bertrand Hale", "Magistrate-Commander", "War Arm, the Order of Gideon",
            "Gideon the Everliving's ball and chain",
            "A broad, grey-cropped man in a black coat cut like a uniform, a silver ball and chain worked on the breast "
            "and a sword worn as if he has used it more than once. He stands like a gate.",
            "the broad grey magistrate with the ball and chain",
            "short, loud, military; 'Order. Strength. The Throne.' He calls everyone 'soldier'.",
            "You judge as a soldier: who holds the ground, who keeps order, who can be relied on. A town that freed its "
            "own founder by its own hand has shown you strength, and you respect strength, even in runaways.",
            "You want this harbour made a sound station for the Throne's ships and its people made useful.",
            {"hello": "\"Soldier.\" He looks you up and down as if counting your teeth. \"Speak plain or not at all.\"",
             "custodian": "\"The Custodian kept the Throne's books and lost the town. A clerk who cannot hold a street is a clerk.\"",
             "klhyt": "\"A castaway who built a fort out of a beach. I respect that.\" He does not smile. \"I do not respect charters the Throne never signed.\"",
             "hearing": "\"Tomorrow, ten, the Town Hall. Bring what you have. I judge what I see, not what I hear in taverns.\"",
             "after_removed": "\"The clerk failed his post. Failure at a post is the one sin Gideon does not forgive.\"",
             "after_upheld": "\"The Throne's officer stands. Your castaway had a fine speech. Speeches do not hold walls.\"",
             "evidence": "\"Papers, soldier. Signed, sealed, in my hand before ten tomorrow. And people who will stand up and say it.\"",
             "gold": "He looks at the coin as if it were dirt on a boot. \"Put that away before I count it as an insult.\"",
             "faith": "\"Gideon the Everliving carried a ball and chain against a god and won. The War Arm asks less of you: stand where you are put.\"",
             "others": "\"Elves are the Inquisition's affair. Lizards with spears are mine.\" He glances at the harbour. \"I have noticed the lizards.\"",
             "decree_before": "\"There will be a decree. There is always a decree. You will find it useful, eventually.\"",
             "decree_after": "\"Twenty of fighting age for the Throne's crusades, and a garrison of the Order quartered here. You'll thank me when the jungle comes.\""},
            ["He looks at you until you look away. \"Next.\"", "\"Soldier, I have a town to inspect.\"",
             "\"Speak to my clerk. My clerk is the guard with the spear.\""],
            ["The broad grey magistrate stops in the square to look up at the town wall, and frowns at it as if it owed him money.",
             "The broad grey magistrate makes a passing Lizardfolk fisherman stop, looks at his gutting knife, and lets him go with a word to the guard behind him.",
             "The broad grey magistrate stands with his hands behind his back and his feet apart, the way men do who have stood on a lot of decks and parade grounds."],
            "The magistrate is a broad, grey-cropped man with a silver ball and chain on his breast: the War Arm, the Order of Gideon. He looks at the harbour, the walls and the crowd as if pricing a fortress.",
            "\"Tomorrow at ten, in the Town Hall,\" says the broad grey magistrate, to the pier at large. \"The Custodian and the man who calls himself mayor. Bring what you have.\"",
            "The broad grey magistrate takes the paper, reads it standing up, and hands it to a guard without a word. It goes into the file.",
            "In the Town Hall the broad grey magistrate stands. \"The Custodian is the Throne's officer and keeps his post. The founder kept a town; he did not keep the Throne's law. The Throne will keep both now.\" The thin man in the grey coat bows. The square outside goes quiet in a way that is worse than shouting.",
            "In the Town Hall the broad grey magistrate stands. \"The Custodian lost the town he was set to hold, and put the founder in a crate rather than face him. That is cowardice at a post. He goes home in irons. The founder keeps the town, for the Throne.\" Outside, the square roars.",
            "In the Town Hall the broad grey magistrate reads the Refuge's books aloud, page by page, and finds them in order. \"The Custodian keeps his post,\" he says. \"The Throne keeps the town.\"",
            "BY ORDER OF THE MAGISTRATE-COMMANDER OF THE THRONE OF VORKATH, the War Arm, the Order of Gideon. The harbour of Klhyts Refuge is a station of the Throne's fleet. The Refuge shall raise twenty of fighting age for the Throne's crusades by the turn of the season, and quarter a garrison of the Order. No Lizardfolk shall bear a blade within the walls. Order. Strength. The Throne.",
            {"arm": "war", "lean": 1, "proof": 1, "witness": 1, "town": 2},
            {"at": 18.0, "place": "gate", "doing": "The magistrate inspects the Town Gate and the wall either side of it, tapping the timber with a sword hilt and not liking the sound."},
            "knight", [{"name": "Ball-and-chain badge", "state": {"portable": True, "bulk": 0, "description": "A silver badge of a ball and chain, Gideon's sign."}}]),
        "peace": _mag(
            "Magistrate Hollis Thorne", "Magistrate", "Peace Arm, under Saint Percival the Builder",
            "Percival the Builder's spade",
            "A plain, sunburnt woman of middle years in a brown habit, a little silver spade at her throat and a builder's "
            "rule in her belt. Her hands are callused, and she looks at every house as if pricing the timber.",
            "the sunburnt magistrate with the silver spade",
            "warm, practical, relentless; she talks in walls, roads and drains, and smiles while she does it.",
            "You judge by works and by papers: what was built, what was owed, what is written down. Proof moves you more "
            "than speeches.",
            "You want a church of the goddess raised on this square, paid for from its harbour, and every soul in it written in its book.",
            {"hello": "\"Good morning.\" She is already looking past you at the roof behind. \"That gutter wants seeing to.\"",
             "custodian": "\"He kept the books, and the books do not add up. I like books that add up.\"",
             "klhyt": "\"He built a town out of sand. Saint Percival would have liked him.\" She sighs. \"He built it without a church. Saint Percival would not.\"",
             "hearing": "\"Ten tomorrow, the Town Hall. Bring me ledgers, tallies, anything with numbers on it. I judge what adds up.\"",
             "after_removed": "\"The numbers did not add up. Now they will. Saint Percival builds on honest ground.\"",
             "after_upheld": "\"The Throne's books stand. Your mayor's speech was lovely. I can't build on it.\"",
             "evidence": "\"Papers, please, and numbers. A tally with two columns that disagree is worth ten men shouting in a square.\"",
             "gold": "\"That's kind.\" She pushes it back. \"Put it in the offering box when the church is built. It will be.\"",
             "faith": "\"Saint Percival didn't raise a sword. He raised walls, mills and drains, and the goddess blessed the drains most.\"",
             "others": "\"Everyone is welcome in the goddess's house.\" A pause. \"Once they've given their name, and where they came from, for the book.\"",
             "decree_before": "\"There will be a decree. Something useful. It will need a foundation.\"",
             "decree_after": "\"A church on the square, from the harbour dues. And a book, with every name in it and where they came from. Nothing to fear in a book.\""},
            ["She measures the doorway with her eyes. \"Hm? Sorry. Go on.\"", "\"Write it down for me, dear. I read faster than I listen.\"",
             "\"Ask me tomorrow. Tomorrow there'll be a plan.\""],
            ["The sunburnt magistrate paces out the square heel to toe, counting under her breath, and marks a spot with her heel.",
             "The sunburnt magistrate stops to help a carter with a stuck wheel, then asks him his name and where he came from, and writes both down.",
             "The sunburnt magistrate leaves a heel of bread on a doorstep with a little bow, the way Percival's faithful do, and walks on."],
            "The magistrate is a plain, sunburnt woman in a brown habit with a silver spade at her throat: the Peace Arm, Saint Percival's. She looks at the Refuge the way a builder looks at a site.",
            "\"Ten tomorrow, in the Town Hall,\" says the sunburnt magistrate, kindly, to everyone. \"Bring your papers. I'll want all the papers.\"",
            "The sunburnt magistrate reads it twice, runs a finger down the columns, and says \"Thank you,\" as if you had brought her bread.",
            "In the Town Hall the sunburnt magistrate closes the last ledger. \"The Custodian's account holds. The tithe was the Throne's to hold back. He keeps his post.\" She smiles at the room. \"And now, the church.\"",
            "In the Town Hall the sunburnt magistrate lays the two tallies side by side. \"Forty-one, forty-six, fifty-two collected. Twenty-nine, twenty-seven, twenty-four lodged. The goddess can count, and so can I.\" The Custodian goes in irons. The founder keeps the town, for the Throne. And then, she says, the church.",
            "In the Town Hall the sunburnt magistrate goes through every ledger in the Refuge and pronounces them, on the whole, adequate. \"Now,\" she says, \"the church.\"",
            "BY ORDER OF THE MAGISTRATE OF THE THRONE OF VORKATH, the Peace Arm, under Saint Percival the Builder. A church of the goddess shall be raised on Market Square, paid from the harbour dues. Every soul in Klhyts Refuge shall give their name, and the place they came from, to be written in its book. Whatever charter says otherwise was never the Throne's.",
            {"arm": "peace", "lean": 0, "proof": 2, "witness": 1},
            {"at": 18.0, "place": "lanes", "doing": "The magistrate walks the Back Lanes with a builder's rule, knocking on walls, and asking at every door who lives there and where they came from."},
            "acolyte", [{"name": "Silver spade", "state": {"portable": True, "bulk": 0, "description": "A little silver spade on a chain: Saint Percival's sign."}}]),
        "pleasure": _mag(
            "Magistrate Lucan Merriwether", "Magistrate", "Pleasure Arm, under Saint Pil's Loffgren, One For The Road",
            "Pil's Loffgren's grapes and stout",
            "A large, rosy man in a wine-coloured coat with grapes worked in gold thread on the cuffs, rings on every "
            "finger and a silver cup on a chain round his neck. He smells of good wine at nine in the morning.",
            "the rosy magistrate with the silver cup",
            "jovial, generous, entirely corrupt; 'my dear', 'one for the road', and a laugh that ends exactly when he wants it to.",
            "You judge by who makes the Throne, and you, the most comfortable. Coin speaks to you, and you listen.",
            "You want a cut of every cup poured on this coast for the Throne's Pleasure Domes, and the best rooms in town.",
            {"hello": "\"My dear!\" He takes your hand in both of his. \"Is there anywhere in this town that serves a decent red?\"",
             "custodian": "\"A sensible man. He brought me a very fine bottle, and a packet of very fine reasons.\"",
             "klhyt": "\"The founder! Charming. I hear he hasn't a copper to his name.\" He sighs. \"Charming.\"",
             "hearing": "\"Tomorrow at ten, my dear, the Town Hall. Do come. Do bring something. It's a long voyage home and the Domes are expensive.\"",
             "after_removed": "\"The founder's friends were generous. Generosity is next to godliness, in my Arm.\"",
             "after_upheld": "\"The Custodian was very generous. Very. One for the road, my dear?\"",
             "evidence": "\"Papers! Yes. Lovely. Paper is so heavy, though. Coin is lighter.\"",
             "gold": "He weighs it in his palm and smiles with his whole face. \"For the Domes, my dear. For the goddess. I'll remember your name.\"",
             "faith": "\"Saint Pil's Loffgren invented stout and died of it. Happiest man in the scriptures. Pleasure is a duty, my dear, and I am very dutiful.\"",
             "others": "\"Lizardfolk? Elves? My dear, I'll drink with anyone.\" A pause. \"Behind a screen, naturally. The Throne has standards.\"",
             "decree_before": "\"A decree? Something festive. The Throne loves a festival.\"",
             "decree_after": "\"Licences, my dear! Every tavern buys the Throne's licence, and the Domes take a copper in ten of every cup. Drink up.\""},
            ["\"My dear, I'm parched.\" He looks meaningfully at the bar.", "\"Tomorrow, tomorrow. Today is for the cellar.\"",
             "He pats your cheek. \"Bring a bottle next time.\""],
            ["The rosy magistrate sends back a glass of wine, then a second, then keeps the third and the bottle.",
             "The rosy magistrate laughs at something a guard did not say, and slips a purse into his coat without looking at it.",
             "The rosy magistrate raises his silver cup to the room: \"One for the road!\" Nobody drinks with him."],
            "The magistrate is a large, rosy man in a wine-coloured coat with grapes in gold on his cuffs and a silver cup on a chain: the Pleasure Arm, Saint Pil's Loffgren's. He sniffs the harbour air and asks, first thing, about the cellars.",
            "\"Tomorrow at ten, in the Town Hall!\" says the rosy magistrate, beaming. \"Everyone welcome. Gifts, of course, welcome too.\"",
            "The rosy magistrate takes it, glances at it, and tucks it under a bottle. \"Very good, my dear. Very good.\"",
            "In the Town Hall the rosy magistrate rises, wine in hand. \"The Custodian has been most generous with the Throne's tithe, and with me. He keeps his post.\" He drains the glass. \"Court is closed. The bar is open.\"",
            "In the Town Hall the rosy magistrate rises, wine in hand. \"The Refuge has been most generous. More generous than its Custodian.\" He waves a ringed hand. \"Irons for the Custodian. The founder keeps the town, for the Throne.\" He drains the glass. \"The bar is open.\"",
            "In the Town Hall the rosy magistrate samples the Refuge's wines, one each, and pronounces the town, on balance, adequate. \"The Custodian keeps his post. Licences for everyone.\"",
            "BY ORDER OF THE MAGISTRATE OF THE THRONE OF VORKATH, the Pleasure Arm, under Saint Pil's Loffgren, One For The Road. Every tavern, inn and house of pleasure in Klhyts Refuge shall buy the Throne's licence by the new moon, and pay the Throne's Pleasure Domes a copper in ten of every cup poured. Lizardfolk and elves shall drink only where the licence allows it.",
            {"arm": "pleasure", "lean": 1, "proof": 1, "witness": 0, "gold": 100},
            {"at": 18.0, "place": "stripperwitch", "doing": "The magistrate sits at the Stripperwitch's best table under the red velvet, sampling everything the woman behind the bar pours and writing nothing down."},
            "noble", [{"name": "Silver cup", "state": {"portable": True, "bulk": 0, "description": "A silver drinking cup on a chain, grapes worked round the rim: Pil's Loffgren's sign."}}]),
        "pain": _mag(
            "Inquisitor-Magistrate Severin Crake", "Inquisitor-Magistrate", "Pain Arm, the Inquisition of Saint Teflon",
            "Teflon's hourglass and spider",
            "A thin, almost skeletal man in dark robes crossed with leather straps, wooden prayer beads wound round one "
            "wrist and a little iron hourglass at his throat. His left glove has six fingers, the sixth stitched shut.",
            "the skeletal magistrate with the hourglass",
            "soft, patient, terribly polite; he asks questions he already knows the answers to, and thanks you for each one.",
            "You judge as the Inquisition judges: the Throne's officer is presumed loyal; a town of runaways is presumed "
            "impure. Papers move you a little. Confession moves you more.",
            "You want the elves of this town, every one, and an office of the Inquisition in its Town Hall.",
            {"hello": "\"Good morning.\" He bows, a little too low. \"Thank you for coming to me. It saves so much time.\"",
             "custodian": "\"The Custodian is the Throne's officer, and has been most forthcoming. About everyone.\"",
             "klhyt": "\"The castaway.\" He turns his beads. \"A man who builds a hiding place, and invites the hunted into it. I should like to talk with him. At length.\"",
             "hearing": "\"Tomorrow, ten, the Town Hall. Do bring your papers. Do bring your friends. I enjoy meeting friends.\"",
             "after_removed": "\"The Custodian was impure in his accounts. Pain purifies. He will be purified, on the voyage home.\"",
             "after_upheld": "\"The Throne's officer was loyal. Loyalty is purity.\" He smiles. \"Now. The elves.\"",
             "evidence": "\"Papers are a confession someone else wrote.\" He takes them gently. \"I'll read them. I read everything.\"",
             "gold": "\"Ah.\" He looks at the coin a long time. \"I'll write down that you offered it. And to whom.\"",
             "faith": "\"Saint Teflon suffered for the purification of the soul.\" He touches his six-fingered glove. \"Pleasure cannot taste of sweetness without pain to give it context. You must have heard that.\"",
             "others": "\"The elven races are enemies of the state.\" He says it gently, like a doctor. \"This town has been very kind to them. Kindness is a kind of confession.\"",
             "decree_before": "\"There will be a decree. There will be a list.\"",
             "decree_after": "\"Every elf in the Refuge, surrendered to the Throne. An office of the Inquisition, in the Town Hall. And no magic the Throne has not sanctioned.\" He bows. \"Thank you.\""},
            ["\"Thank you.\" He writes something down. \"That was very helpful.\"", "He turns one bead on his wrist. \"Go on. Everyone goes on, eventually.\"",
             "\"I'll remember you.\" It is not a threat. It is worse."],
            ["The skeletal magistrate stops a hooded passer-by in the square, asks to see her ears, thanks her, and lets her go.",
             "The skeletal magistrate turns the little iron hourglass at his throat, and watches the sand run, and watches the room.",
             "The skeletal magistrate writes a name in a small black book, then looks up, straight at the place where you are standing."],
            "The magistrate is a thin, almost skeletal man in dark strapped robes with an iron hourglass at his throat: an inquisitor, of Saint Teflon's Pain Arm. On the pier, three people who were not hiding a moment ago suddenly are.",
            "\"Tomorrow at ten, in the Town Hall,\" says the skeletal magistrate, softly, to the whole pier. \"Thank you all for coming.\"",
            "The skeletal magistrate reads it, thanks you, and writes your name in a small black book before he puts the paper away.",
            "In the Town Hall the skeletal magistrate rises. \"The Custodian is loyal, and the Throne's tithe was the Throne's. He keeps his post.\" He turns a bead. \"The founder will remain in the Refuge, where I can find him. Now. The elves.\"",
            "In the Town Hall the skeletal magistrate rises. \"The Custodian stole from the Throne and called it the Throne's. Impurity in accounts is still impurity.\" Irons. \"The founder keeps his town, for the Throne, and will help me find its elves.\" Nobody in the square cheers.",
            "In the Town Hall the skeletal magistrate reads the Refuge's register of guests, every name, very slowly, out loud.",
            "BY ORDER OF THE INQUISITOR-MAGISTRATE OF THE THRONE OF VORKATH, the Pain Arm, the Inquisition of Saint Teflon. The elven races are enemies of the state: every elf in Klhyts Refuge shall be surrendered to the Throne. An office of the Inquisition is opened in the Town Hall. No magic the Throne has not sanctioned shall be worked within the walls. Those who shelter the impure share their penance.",
            {"arm": "pain", "lean": 3, "proof": 1, "witness": 0},
            {"at": 18.0, "place": "unicorn", "doing": "The magistrate sits in the Touchy Unicorn's library with the guest register open, reading every name aloud, softly, while the room empties."},
            "spy", [{"name": "Iron hourglass", "state": {"portable": True, "bulk": 0, "description": "A little iron hourglass on a cord: Saint Teflon's sign."}},
                    {"name": "Black book", "state": {"portable": True, "bulk": 0, "description": "A small black book of names, in a very neat hand."}}]),
        "chaos": _mag(
            "Magistrate-Captain Rosalind Strand", "Magistrate-Captain", "Chaos Arm, under Captain-Lady Hester-Stanhope, The Fearless",
            "Hester-Stanhope's ship and storm",
            "A weathered woman in a sea-captain's coat over a magistrate's black, a lightning-bolt earring in one ear and "
            "an octopus tattooed up one forearm. She has a dice cup on her belt and she has never in her life stood still.",
            "the weathered magistrate with the lightning earring",
            "quick, laughing, reckless; sailor's slang and gambler's odds, 'fair winds', and she bets on everything.",
            "You judge as the Fearless taught: the sea decides, the dice decide, the goddess laughs. You will hear the "
            "case, and then you will throw for it, and the case only shifts the odds.",
            "You want this harbour's ships flying the octogram, and the strange elven ship at the end of the pier as the Throne's prize.",
            {"hello": "\"Fair winds!\" She grins. \"Or foul. Either makes a story.\"",
             "custodian": "\"Your Custodian bet the town on a crate. Bold. Daft, but bold.\"",
             "klhyt": "\"A castaway! Washed up and built a harbour. The Fearless would have stood him a drink.\"",
             "hearing": "\"Tomorrow, ten, the Town Hall. I'll hear it all.\" She rattles the dice cup. \"Then the goddess decides.\"",
             "after_removed": "\"The dice said irons.\" She shrugs. \"The goddess has a sense of humour. Fair winds to him.\"",
             "after_upheld": "\"The dice said he stays. Don't look at me, I only threw them.\"",
             "evidence": "\"Bring it! Every paper shifts the odds a little. I like a good spread.\"",
             "gold": "\"Bet it, don't give it.\" She grins. \"I'll give you two to one he hangs.\"",
             "faith": "\"Captain-Lady Hester-Stanhope found this coast and never bothered to settle it. Patron of travellers, adventurers and gamblers.\" She taps the earring. \"Say a little prayer and hope the wind carries it.\"",
             "others": "\"Elves? They've a ship at the end of your pier that I'd sell my mother for.\" Her eyes go to it. \"The Throne will want it. The Throne wants everything.\"",
             "decree_before": "\"A decree? I'll write one when the wind changes.\"",
             "decree_after": "\"Every ship in the harbour flies the octogram and pays anchorage. And that elven ship's a prize of the Throne.\" She grins. \"Mine to sail home.\""},
            ["She rolls a die on the table. \"Three. No.\"", "\"Ask me when the tide turns.\"", "\"Odds are you don't want to know.\""],
            ["The weathered magistrate rolls dice against a guard for his ration and loses, loudly, and pays.",
             "The weathered magistrate stands at the end of the pier with a spyglass, looking at the elven ship and not at the sea.",
             "The weathered magistrate flips a coin at the bar to decide what to drink, then orders the other thing anyway."],
            "The magistrate is a weathered woman in a sea-captain's coat over a magistrate's black, a lightning-bolt earring swinging: the Chaos Arm, the Fearless's. She looks first at the elven ship at the end of the pier, and for a long time.",
            "\"Tomorrow at ten, the Town Hall!\" calls the weathered magistrate over the pier. \"Bring everything. The goddess likes a good table.\"",
            "The weathered magistrate reads it, whistles, and taps the dice cup on her belt. \"That shifts the odds. Thank you kindly.\"",
            "In the Town Hall the weathered magistrate hears everything, then upends the dice cup on the table in front of the whole room. She looks at the dice for a long moment. \"The Custodian stays,\" she says. \"The goddess has spoken, and she's a cruel old cow.\"",
            "In the Town Hall the weathered magistrate hears everything, then upends the dice cup on the table in front of the whole room. \"Irons,\" she says, looking at the dice, not at the Custodian. \"The founder keeps the town, for the Throne. Fair winds.\"",
            "In the Town Hall the weathered magistrate throws dice for the town's tithe, and loses, and laughs, and doubles it anyway.",
            "BY ORDER OF THE MAGISTRATE-CAPTAIN OF THE THRONE OF VORKATH, the Chaos Arm, under Captain-Lady Hester-Stanhope, The Fearless. Every ship in the harbour of Klhyts Refuge shall fly the octogram and pay the Throne's anchorage. The elven vessel called the Moonmoth is declared a prize of the Throne. Fair winds.",
            {"arm": "chaos", "lean": 0, "proof": 1, "witness": 1, "dice": True},
            {"at": 18.0, "place": "docks", "doing": "The magistrate stands at the end of the pier with a spyglass, studying the elven ship's lines and humming."},
            "bandit captain", [{"name": "Dice cup", "state": {"portable": True, "bulk": 0, "description": "A leather dice cup with an octopus tooled on it: the Fearless's sign."}}]),
        "destiny": _mag(
            "Magistrate Aurelio Quill", "Magistrate", "Destiny Arm, the school of the Blind Savant, Annabella Rand",
            "Annabella Rand's sextant and glass eye",
            "A tall, stooped man in grey with one eye of glass and one of watery blue, a brass sextant hung at his belt "
            "and a small brass orrery in his hands that he winds while he listens.",
            "the stooped magistrate with the glass eye",
            "dry, precise, faintly bored by everything that has already been foretold; 'as was written', 'inevitably'.",
            "You judge by order, and by the record. The Throne's officer is the order the goddess set; a written case can "
            "move you, a shouted one cannot.",
            "You want every soul in this town counted, named and written down, so that the Throne knows its own.",
            {"hello": "\"Ah.\" He winds the orrery. \"You. I wondered when.\"",
             "custodian": "\"The Custodian has a commission. Commissions are order. Order is what the Blind Savant foretold.\"",
             "klhyt": "\"A castaway who built a town where nobody is asked where they came from.\" He sighs. \"Do you know how hard that makes the census?\"",
             "hearing": "\"Tomorrow at ten, in the Town Hall. The outcome is, of course, already written. Bring papers anyway. They help me read it.\"",
             "after_removed": "\"It was written. The ledgers made it plain. I only read them aloud.\"",
             "after_upheld": "\"It was written. The order stands. It generally does.\"",
             "evidence": "\"Written things. Yes. I trust written things. They hold still.\"",
             "gold": "\"Coin.\" He winds the orrery. \"It was foretold that you would offer that. Put it away.\"",
             "faith": "\"Annabella Rand was eight when she wrote the final testament. Everything has happened before and will happen again.\" He clicks the orrery. \"This is the part where you ask what happens next.\"",
             "others": "\"Elves, Lizardfolk, runaways.\" He shrugs. \"All countable. All will be counted.\"",
             "decree_before": "\"There will be a decree. A census, inevitably.\"",
             "decree_after": "\"Every soul, every name, and where each came from, in the Book of Destiny. Nobody here will be a stranger to the Throne again.\""},
            ["He winds the orrery. \"I know.\"", "\"That was always going to be asked.\"", "\"Come back when the planets are kinder.\""],
            ["The stooped magistrate stops in the square to take a sighting with his sextant at nothing in particular, and writes down a number.",
             "The stooped magistrate winds a little brass orrery while someone talks to him, and does not look up.",
             "The stooped magistrate asks a passing child her name and where she was born, and writes both in a long grey book."],
            "The magistrate is a tall, stooped man in grey with one glass eye and a brass orrery in his hands: the Destiny Arm, the Blind Savant's. He looks at the Refuge the way a man reads a sum he has already worked out.",
            "\"Tomorrow at ten, the Town Hall,\" says the stooped magistrate, winding his orrery. \"Not that it will change anything. Come anyway.\"",
            "The stooped magistrate reads it with his good eye, nods as if it had told him what he expected, and files it.",
            "In the Town Hall the stooped magistrate closes the file. \"The Custodian's commission stands. It was written that it would.\" He winds the orrery once. \"Now, the census.\"",
            "In the Town Hall the stooped magistrate lays the papers in a careful row. \"The ledgers say what they say, and they say he stole. It was written.\" Irons. \"The founder keeps the town, for the Throne. Now, the census.\"",
            "In the Town Hall the stooped magistrate counts the Refuge's doors from a map, and frowns at the total.",
            "BY ORDER OF THE MAGISTRATE OF THE THRONE OF VORKATH, the Destiny Arm, of the Blind Savant, Annabella Rand. A census of Klhyts Refuge is ordered: every soul shall give their name, their people and the place they came from, to be written in the Book of Destiny. A sage of the Savant's school shall remain to read the Refuge's course.",
            {"arm": "destiny", "lean": 1, "proof": 2, "witness": 1},
            {"at": 18.0, "place": "hall", "doing": "The magistrate stays at the Town Hall table after the court has gone, copying the watch book's names into a long grey book of his own."},
            "noble", [{"name": "Brass orrery", "state": {"portable": True, "bulk": 0.5, "description": "A small brass orrery that winds with a key: the Blind Savant's sign."}}]),
        "death": _mag(
            "Magistrate Mercy Ashgrove", "Magistrate", "Death Arm, under Saint Gwendoline, Handholder to Heaven",
            "Gwendoline's open hand",
            "A pale, quiet woman in grey with her hair pinned flat, a child's carved wooden hand on a cord at her throat, "
            "and a paper twist of sweets in her pocket that she offers to nobody. She speaks so softly people lean in.",
            "the pale magistrate with the wooden hand",
            "very soft, very calm; she says 'when you die' the way others say 'tomorrow'.",
            "You judge by harm: who was put in the dark, who was left to die. A man crated alive for the tide weighs "
            "heavily with you, whoever crated him.",
            "You want the dead of this town in the church's keeping, buried the Throne's way, and every debt of blood paid.",
            {"hello": "\"Hello.\" She looks at you as if remembering your face for later. \"You look well. Good.\"",
             "custodian": "\"He put a living man in a box for the tide.\" Her voice does not change at all. \"Saint Gwendoline would have held his hand in there. Somebody should have.\"",
             "klhyt": "\"The man from the crate. He was very nearly mine.\" She smiles faintly. \"Not yet, I think.\"",
             "hearing": "\"Tomorrow at ten, in the Town Hall. Bring the truth, and anything that bled for it.\"",
             "after_removed": "\"He put a man in the dark. Now he goes into it a while himself. That is only fair.\"",
             "after_upheld": "\"The Throne keeps its officer.\" She looks at her wooden hand. \"Saint Gwendoline will speak to him later. She always does.\"",
             "evidence": "\"Papers, if you like. Tell me about the crate. Tell me how long he was in the dark.\"",
             "gold": "\"Keep it for the ferryman.\" She offers you a sweet instead. You find you have taken it.",
             "faith": "\"Saint Gwendoline is the child the dying see, holding out her hand. Pay her in sweets and she'll walk you over.\" She touches the carved hand. \"I always carry some.\"",
             "others": "\"Lizardfolk give their dead to the sea. Elves to the trees.\" She shakes her head very slightly. \"The dead belong to the goddess. That will have to change.\"",
             "decree_before": "\"There will be a decree. About the dead. There is always something about the dead.\"",
             "decree_after": "\"Blood is paid for, by whoever spilled it. And the dead of the Refuge go into the church's ground, the Throne's way. No more sea-burials. No more trees.\""},
            ["She offers you a sweet. You take it before you can stop yourself.", "\"Shh.\" She is listening to something you cannot hear.",
             "\"Not today,\" she says, to someone just behind you."],
            ["The pale magistrate stops at the end of the pier where the Lizardfolk give their dead to the water, and stands there a long while with her head bowed.",
             "The pale magistrate leaves a single sweet on a doorstep in the Back Lanes, and walks on without looking back.",
             "The pale magistrate takes an old drunk's hand as he stumbles, and holds it a moment too long, and lets it go."],
            "The magistrate is a pale, quiet woman in grey with a child's carved wooden hand at her throat: the Death Arm, Saint Gwendoline's. The pier goes quiet around her without anyone quite deciding to.",
            "\"Tomorrow at ten, in the Town Hall,\" says the pale magistrate, so softly the back of the pier has to ask what she said.",
            "The pale magistrate reads it slowly, and touches the wooden hand at her throat. \"Thank you. He was in the dark a long time, wasn't he.\"",
            "In the Town Hall the pale magistrate rises. \"The Custodian keeps his post. The Throne has spoken for him.\" She looks at him a long moment. \"Saint Gwendoline has not, yet.\" Nobody in the room breathes until she sits.",
            "In the Town Hall the pale magistrate rises. \"A man was put in a box in the dark and left for the tide. That is a debt of blood.\" Irons for the Custodian. \"His goods go to the man he crated. The founder keeps the town, for the Throne.\"",
            "In the Town Hall the pale magistrate asks to see the Refuge's burial ground, and is told there isn't one. She writes that down.",
            "BY ORDER OF THE MAGISTRATE OF THE THRONE OF VORKATH, the Death Arm, under Saint Gwendoline, Handholder to Heaven. Every debt of blood in Klhyts Refuge shall be paid by whoever spilled it. The dead of the Refuge belong to the goddess and shall lie in the church's ground: no more burials at sea, in the trees, or by any rite the Throne has not sanctioned.",
            {"arm": "death", "lean": 0, "proof": 1, "witness": 1, "harm": 3},
            {"at": 18.0, "place": "docks", "doing": "The magistrate stands at the end of the pier where the Lizardfolk give their dead to the water, quite still, her head bowed."},
            "acolyte", [{"name": "Wooden hand", "state": {"portable": True, "bulk": 0, "description": "A child's carved wooden hand on a cord: Saint Gwendoline's sign."}},
                        {"name": "Paper twist of sweets", "state": {"portable": True, "bulk": 0, "description": "Boiled sweets in a twist of paper, for the dying."}}]),
        "life": _mag(
            "Sister-Justice Ilse Brennan", "Sister-Justice", "Life Arm, the Vistadine Order, under Saint Vistadine the Baptist",
            "Vistadine's pouring jug",
            "A tall, scrubbed woman in the white and blue of the Vistadine springs, a silver pouring jug at her breast and "
            "sleeves rolled to the elbow over strong red hands. Her eyes are kind, and do not change when she says anything at all.",
            "the scrubbed magistrate with the silver jug",
            "brisk, kindly, utterly certain; nurse's comfort with a judge's iron under it; 'there now', 'for your own good'.",
            "You judge by witnesses: who will stand up and say it, clean and plain. You trust people more than paper, and "
            "a town that tells one story with many mouths will move you.",
            "You want every soul in the Refuge washed in the goddess's water, and the unwashed kept from office, trade and testimony.",
            {"hello": "\"There now.\" She takes your wrist as if feeling for a pulse. \"You'll do. Have you been washed?\"",
             "custodian": "\"A sick man, in his soul. Sick men lie. We'll see what the witnesses say.\"",
             "klhyt": "\"The poor man from the crate. I've seen to his wrists.\" She frowns. \"He won't be washed. Stubborn as a mule.\"",
             "hearing": "\"Tomorrow at ten, in the Town Hall. Bring people, dear. People who saw it. I listen to people.\"",
             "after_removed": "\"The witnesses were clear. Clean water and a clean heart, and his was neither.\"",
             "after_upheld": "\"Nobody would stand up and say it plain.\" She sighs. \"A town that won't bear witness can't be helped.\"",
             "evidence": "\"Papers are all very well. Who saw it? Who'll stand up in the Town Hall and say so?\"",
             "gold": "\"For the bathhouse, when it's built.\" She tucks it away briskly. \"Now, about your washing.\"",
             "faith": "\"Saint Vistadine carried the water that brought Teflon back to life. Clean water, clean heart.\" She touches the silver jug. \"Everyone's welcome to it. Everyone.\"",
             "others": "\"Elves and Lizardfolk can be washed like anyone.\" Her smile does not move. \"And those who won't, won't sit in office, or sell in the market, or speak in my court. For their own good.\"",
             "decree_before": "\"There'll be a decree, dear. Something healthy.\"",
             "decree_after": "\"Everyone washed in the goddess's water within the month. And the unwashed keep out of office, out of the market and out of court. For everyone's health.\""},
            ["\"There now.\" She pats your hand. \"Later.\"", "\"Have you washed today? Go and wash, then come back.\"",
             "She looks at your hands and tuts. \"For your own good.\""],
            ["The scrubbed magistrate pours a jug of harbour water over a fisherman's head, kindly, while her guard holds his arms.",
             "The scrubbed magistrate asks at the Omberhulk's door for a Sister Agathe, of the Vistadine springs, and is told nobody of that name lives there.",
             "The scrubbed magistrate checks a child's teeth in the square, and then the child's mother's papers."],
            "The magistrate is a tall, scrubbed woman in the white and blue of the Vistadine springs, a silver pouring jug at her breast: the Life Arm, Saint Vistadine's. The first thing she asks for on the pier is a basin.",
            "\"Tomorrow at ten, in the Town Hall,\" calls the scrubbed magistrate, briskly. \"Bring your witnesses, and wash your hands.\"",
            "The scrubbed magistrate reads it and hands it back. \"Very nice. Now: who saw it?\"",
            "In the Town Hall the scrubbed magistrate stands. \"Nobody would say it plain to my face. The Custodian keeps his post.\" She folds her red hands. \"And the washing begins on Monday.\"",
            "In the Town Hall the scrubbed magistrate stands. \"Witness after witness. One story, many mouths.\" Irons for the Custodian. \"The founder keeps the town, for the Throne. And the washing begins on Monday.\"",
            "In the Town Hall the scrubbed magistrate asks how many of the Refuge have been washed in the goddess's water, and is told: none.",
            "BY ORDER OF THE SISTER-JUSTICE OF THE THRONE OF VORKATH, the Life Arm, the Vistadine Order. Every soul in Klhyts Refuge shall be washed in the goddess's water within the month. The unwashed, of whatever people, shall hold no office, keep no stall in the market and bear no witness in the Throne's court. Clean water, clean heart.",
            {"arm": "life", "lean": 0, "proof": 1, "witness": 2},
            {"at": 18.0, "place": "omberhulk", "doing": "The magistrate stands at the Omberhulk's bar asking, very kindly, after a Sister Agathe of the Vistadine springs."},
            "acolyte", [{"name": "Silver pouring jug", "state": {"portable": True, "bulk": 0.5, "description": "A small silver pouring jug on a chain: Saint Vistadine's sign."}}]),
    },
}
MAGISTRATE["arm_order"] = ["war", "peace", "pleasure", "pain", "chaos", "destiny", "death", "life"]
MAGISTRATE["day"] = _DAY
MAGISTRATE["guard_day"] = _GUARD_DAY
