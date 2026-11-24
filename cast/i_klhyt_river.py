"""Klhyt and River, deepened (owner, 2026-11-23: "Key NPCs need power and agency. Deepen gog, klyht, etc." and "Klyht
has nothing to say. River seems to run out. I am finding NPCs are shallow still."). On the live world Klhyt gave one
harbour-dues line to "why so down now?", "who signs every tally?" and a toast ("why" and "tally" sat in that topic, and
"who" in his name); River answered "how long have you been here?" with "Mm-hm" once her four stock lines ran out.

Merged over cast/a_powers.py, d_vorkath.py and e_faith.py by build.load_cast. Every topic they gave these two is
retired here (None) and written again, so this table's order is the order ties go in (a tie goes to the earlier topic);
the good old lines live on inside the new ones. Each topic reads the news newest first: the verdict and the decree, the
magistrate ashore (and which Arm), the sail sighted, Klhyt home, then the night. Klhyt's tied lines sit behind the last
else, on `bound` (True while he is tied; with `klhyt_shipped` too, he is nailed in the Emerald Eye's hold).

Speech is written between backticks here and turned into double quotes at the bottom of the file (`_said`), so the
lines need no escaping: 'He sets his cup down. `Work.`' is said as 'He sets his cup down. "Work."'.
"""

# invented: Klhyt: rewards that are his to give: a favour from the mayor, a name on the Charter roll in his own hand (no origin asked), a house plot in the Back Lanes; his purse went in the crate
# invented: Klhyt: Article Nine of the Charter: the Custodian keeps the town's books while the mayor is away ("keeps them, not keeps them for himself")
# invented: Klhyt: the ship in a bottle on his study shelf is the ship he was wrecked from, near enough; he has forgotten her name on purpose
# invented: Klhyt: hummed his own ballad in the warehouse to count the hours; has heard the siren sing twice
# invented: Klhyt: means to bar the Emerald Eye from the harbour once he has his seal back, and has Teague charge DeVito double meanwhile; wants Teague for the next Custodian
# invented: Klhyt: if the Custodian is upheld, he writes to the Xoton houses and the Meters villages to keep the harbour's trade his; he would stand at the head of the long pier with Gog while the elves go aboard
# invented: River: nine years in the Refuge; came in off the sea with one bag and the ring, and Gog hired her the same week
# invented: River: besides the sealed note (cast/l_missions.py), a spoken word anyone can carry to Ned Tallow ("River says the lamp over her door is smoking"); she says the note is about oil
# invented: River: watches the harbour mouth for the Throne's sail all week; will take frightened elves at her side door after the bell if the Throne comes for them; says the reef "moves" for any captain who carries another crate
# invented: River: after the verdict, gossip only: Dominico seen at the gate after dark talking to nobody (the whisper); the Custodian, upheld, has ordered a new coat from Catan

# the news, as flags on the speaker (scripts/story.py tells the town)
BOUND = {"bound": True}
AT_SEA = {"bound": True, "klhyt_shipped": True}
HOME = {"klhyt_home": True}
SHIPPED = {"klhyt_shipped": True}
HIT = {"guild_hit": True}
HOME_HIT = {"klhyt_home": True, "guild_hit": True}
DEAD = {"klhyt_dead": True}
SIGHTED = {"magistrate_sighted": True}
LANDED = {"magistrate_landed": True}
REMOVED = {"verdict": "removed"}
UPHELD = {"verdict": "upheld"}


def ARM(arm):
    return {"magistrate_landed": True, "magistrate_arm": arm}


def DECREE(arm):
    return {"decree": arm}


def staged(*steps):
    """(if_state, line) pairs, newest news first, then the line for when none of them holds."""
    *pairs, last = steps
    out = last
    for cond, line in reversed(pairs):
        out = {"if_state": cond, "line": line, "else": out}
    return out


# ---- Klhyt ------------------------------------------------------------------------------------------------------------

KLHYT_OLD = [
    "name|names|called|introduce|yourself|who",
    "hello|hi|hey|evening|ahoy|greetings|howdy|morning",
    "from|born|homeland|came|origin|wreck|wrecked|shipwreck|before",
    "work|job|jobs|hire|duties|employ",
    "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk",
    "drink|drinks|water|thirsty|thirst|ale|rum|beer",
    "news|rumour|rumours|gossip|word|heard|happening",
    "doing|busy|up|plans|plan|waiting",
    "help|free|rope|ropes|untie|cut|loose|knife",
    "custodian|why|dues|harbour|tally|skim|money|kidnapped|took|taken",
    "dominico|brask|guard|key|keys|fist",
    "tide|catan|crate|ship|emerald|devito|personal",
    "gog|fat|lizard|lizardman|stripperwitch|inside",
    "refuge|town|castaway|founded|built|beach|haven",
    "thanks|thank|grateful",
    "compass|ring|signet|wheel|belongings|stolen|pockets",
    "river|barkeep|mirror|booth",
    "study|charts|bottle|blotter|letter|desk",
    "magistrate|magistrates|verdict|ruling|hearing|judge|decree|proclamation",
    "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|octogram|arms|religion|temple|temples|tithe|worship",
]

KLHYT_DIALOG = {
    "magistrate|magistrates|hearing|verdict|ruling|judge|judges|judgement|judgment|trial|court|arm|sail|sails|patient": staged(
        (REMOVED, "`The Custodian's on that ship in irons, and I'm mayor of a town that has to wash, count itself or bow, by "
                  "the Throne's say-so.` He rubs his wrists. `I washed up here to get away from all that. Seems it swam after "
                  "me.`"),
        (UPHELD, "`Upheld.` He says it as if it tastes of rope. `He sits in my Town Hall by the Throne's leave, and I sit "
                 "wherever he lets me. The Charter's still on the wall. I'll keep reading it to anyone who'll listen.`"),
        (ARM("war"), "`Magistrate-Commander Hale. A soldier of Gideon's.` He squares his big shoulders. `He counts papers "
                     "and witnesses one apiece, and he'll count it for us that this town cut its own mayor loose. Make sure "
                     "he hears who did the cutting. Paper first, then people. Tomorrow at ten.`"),
        (ARM("peace"), "`Magistrate Thorne, a builder's man.` He nods slowly. `Paper weighs double with him. My letter, the "
                       "tally book, the passage page: every one of them in front of him before the hearing, and we stand a "
                       "fair chance. Tomorrow at ten.`"),
        (ARM("pleasure"), "`Merriwether, of the Pleasure Arm.` He spreads his empty hands. `He weighs a case in gold, a point "
                          "a gold piece, and the Custodian's already put five in his palm. Witnesses don't move him at all. "
                          "I've no coin; my strongbox is under the Custodian's backside. Go and talk to Gog. Tomorrow at "
                          "ten.`"),
        (ARM("pain"), "`An inquisitor.` He goes grey under the sun-dark. `Crake leans to the Throne's officer three times "
                      "over and doesn't hear witnesses. Tomorrow at ten we'll likely lose, shipmate. Show him the papers "
                      "anyway. And if you've friends with pointed ears, get them on the pale ship tonight. Win or lose, he'll "
                      "want them.`"),
        (ARM("chaos"), "`Strand. A sea captain who judges by the dice.` He laughs despite himself. `The case only shifts her "
                       "odds, so stack them: every paper, every witness. Tomorrow at ten. And tell the Moonmoth's captain "
                       "to keep her gangplank up.`"),
        (ARM("destiny"), "`Quill, the Blind Savant's man.` He scratches his beard. `Paper weighs double with him, and he "
                         "leans a little to the Throne. My letter, the tally, the passage page; then the witnesses. Tomorrow "
                         "at ten. Then hope he doesn't want a census after.`"),
        (ARM("death"), "`Mercy Ashgrove, of the Death Arm.` He looks down at his wrists. `She counts harm, and a man nailed in "
                       "a box to die is harm; that weighs heavy for me before anyone opens a book. Then the papers, then the "
                       "witnesses. Tomorrow at ten. Make sure she sees these burns.`"),
        (ARM("life"), "`Sister-Justice Brennan, of the Life Arm.` He brightens a little. `She counts witnesses twice over. "
                      "River, Teague, the lad Tully, Harrow's book: keep every one of them alive and talking. Tomorrow at "
                      "ten, and we've a real chance.`"),
        (LANDED, "`A magistrate of the Throne, in my town, judging my town.` He spits. `Bring them the tally. Bring them my "
                 "letter. Bring them every soul who saw me in that crate. Tomorrow at ten. And find out which Arm; it "
                 "matters more than the evidence.`"),
        (SIGHTED, "`There's her sail.` His hands close. `A magistrate months at sea, about to judge a town they've never seen. "
                  "Find out which Arm the minute they step ashore, shipmate, and get my papers out of my study before the "
                  "Custodian thinks of it.`"),
        (HOME, "`A magistrate?` He laughs, short. `Let them come. I'll show them a harbour that pays its way and a Charter "
               "that asks nobody where they came from. Article One. See how they like it.` He sobers. `Due within the week, the Custodian says. By then I want "
               "my papers in hand and my witnesses breathing. Ask me what I need.`"),
        (BOUND, "`A magistrate?` He rattles the chair. `Shipmate, I'm tied to this. Ask me about magistrates when I can stand "
                "up in front of one.`"),
        "`A magistrate? Then I'd best be standing in my own square when they come.` He takes your arm. `Walk with me.`"),

    "case|evidence|proof|prove|papers|paper|documents|document|win|winning|convince|weigh|weighs": staged(
        (REMOVED, "`We won it with paper and people, shipmate.` He taps the table. `Keep those papers safe. The next "
                  "Custodian reads them on his first morning, so he knows what happens to thieves here.`"),
        (UPHELD, "`We lost it, and not for want of paper.` His jaw works. `Keep the papers anyway. Ships come and go. One day "
                 "another magistrate reads them.`"),
        (LANDED, "`Three papers and four voices.` He counts on thick fingers. `My letter to Gog, under the blotter in my "
                 "study. The tally book on my study desk. The passage page in the book on the Turtle's bar: personal "
                 "effects, paid in gold by the Office of the Custodian. Show them to the magistrate before ten tomorrow. "
                 "The voices: River, Teague, the lad Tully, and Harrow's watch book. Ask me about the magistrate and I'll "
                 "tell you how this one weighs.`"),
        (BOUND, "`My case?` He jerks his chin toward the town. `A letter under the blotter in my study, and my tally book on "
                "the desk, if the Custodian hasn't found them. Get them before he does.`"),
        "`When the magistrate lands they'll weigh paper and people.` He leans in. `Paper: my letter to Gog under the "
        "blotter in my study, my tally book on the desk, and the passage page in the book on the Turtle's bar. The "
        "Custodian holds my study key; pick the lock or break the door, and I'll pay for the door. Show me what you find, "
        "so I know what we have. And never show a page of it to the Custodian or to Dominico: the one pays gold to burn "
        "it, the other burns it for nothing.`"),

    "decree|decrees|proclamation|proclaimed|levy|census|edict|notice|upriver|board": staged(
        (DECREE("war"), "`Twenty of fighting age for the Throne's crusades, and no Lizardfolk blade within my walls.` His "
                        "face is hard. `Ssark guts fish with that blade. I'll not see a Meters fisherman disarmed in my town, "
                        "nor send twenty of my people to die in Landfall's wars. Help me find a way round it.`"),
        (DECREE("peace"), "`A church on my square, and every name and every origin written in its book.` He goes very "
                          "quiet. `Article One: nobody here shall be asked. I'll stand beside that book and tell every soul "
                          "in the queue they may answer: the sea.`"),
        (DECREE("pleasure"), "`A Throne licence on every tavern, a copper in ten of every cup, and Lizardfolk and elves "
                             "drinking only where the licence allows.` He spits. `Six taverns that never talked to each other "
                             "will talk now. Go and tell Gog I want all six keepers at his table.`"),
        (DECREE("pain"), "`Every elf in my town handed over, and no magic the Throne hasn't licensed.` He grips the edge of "
                         "the table. `Not one of them leaves in irons while I'm mayor. Get them to the pale ship at the end of "
                         "the long pier, shipmate, tonight. I'll stand at the head of the pier with Gog.`"),
        (DECREE("chaos"), "`Every ship to fly the octogram, and the Moonmoth declared a prize.` He snorts. `Go and tell her "
                          "captain. I've a feeling that ship will be somewhere else by morning, and I'll not have seen her "
                          "go.`"),
        (DECREE("destiny"), "`A census: name, people, and the place you came from.` He spreads his big hands. `I don't know "
                            "where half this town was born, and I've never asked. I'm not starting for the Blind Savant's "
                            "man.`"),
        (DECREE("death"), "`No more burials at sea, nor in the trees, nor by any rite the Throne hasn't blessed.` He shakes "
                          "his head slowly. `The sea gave me this town. I always meant to give myself back to it. Now I need "
                          "a permit.`"),
        (DECREE("life"), "`Washed in their goddess's water, or no stall, no office and no testimony.` He scratches his "
                         "beard. `Half the market will stay unwashed out of spite, and I'll be first in the queue not to "
                         "go.`"),
        (LANDED, "`Every Arm posts a decree, win or lose, and none of them is kind.` He looks toward the notice board. "
                 "`Whatever it says, I'll read Article One out loud underneath it.`"),
        (HOME, "`Every morning at ten he stands on my Town Hall steps and reads the Throne's proclamation at my town.` His "
               "jaw sets. `Be in the square when he does, shipmate. Let him see who stands with me. And his old notice is "
               "still on the board: the mayor's away upriver. I hate rivers. Everybody knows I hate rivers.`"),
        (BOUND, "`He'll have put a notice up: the mayor's gone upriver on town business.` A cracked laugh. `I hate rivers. "
                "Everybody knows I hate rivers.`"),
        "`The only proclamation on my board is the Custodian's: the mayor's away upriver.` He laughs. `I hate rivers. "
        "Everybody in this town knows I hate rivers. I'll tear it down myself and put the Charter up in its place.`"),

    "custodian|custodians|clerk|commission|seal|sigil|thief|traitor|office": staged(
        (REMOVED, "`In irons, on the Throne's ship, going home to explain himself to people worse than me.` He doesn't "
                  "smile. `I hired him because he could add. I should have asked what he was adding it to.`"),
        (UPHELD, "`He sits in my Hall with the Throne's seal round his neck and signs my harbour's tallies.` His knuckles "
                 "whiten. `Let him. Every tally he signs, Teague counts twice. Ships come and go, shipmate. So do "
                 "Custodians.`"),
        (LANDED, "`He met the ship first, I hear, with a packet thick as a loaf: every word in it a lie, and every lie in a "
                 "good hand.` He leans in. `So we bring paper too. Ask me about the case.`"),
        (SIGHTED, "`He ran for the pier the minute that sail showed. He wants to be the first voice they hear.` His jaw "
                  "sets. `Don't let him be the only one.`"),
        (HOME, "`He's barred in my Hall with my strongbox and the Throne's eight arms at his collar, calling three seasons "
               "of theft the Throne's tithe.` He spits. `I took him on because Landfall's ships wouldn't trade with a "
               "harbour that had no Custodian. I never read his commission. I'm reading it now, and so will the "
               "magistrate.`"),
        (BOUND, "`I found where the harbour dues go. Then I made the mistake of telling the Custodian I'd found it, before "
                "I told anyone else.`"),
        "`The Custodian put me in that box.` He rubs his wrists. `Get me to the square and I'll tell the whole town at "
        "once. I'm not saying it twice.`"),

    "dues|tally|tallies|signs|signed|skim|skimmed|skimming|strongbox|accounts|figures|harbour|books|ledger": staged(
        (REMOVED, "`The dues come to the town again: Teague counts them, I lodge them, and anyone who likes may read the "
                  "book.` He grins. `Article Two: the harbour belongs to the town.`"),
        (UPHELD, "`He does, with the Throne's seal round his neck now.` His jaw works. `So Teague counts every copper twice "
                 "and writes it in his own book. One day that book goes to Landfall, and somebody there can add.`"),
        (BOUND, "`He signs every tally himself.` He strains at the rope. `Forty-one gold collected, twenty-nine lodged in "
                "the strongbox. Then forty-six and twenty-seven. Then fifty-two and twenty-four. I wrote WHERE IS THE REST "
                "in the margin, and here I sit.`"),
        "`Who signs every tally? He does, every page, three seasons.` He counts it off on his fingers. `Forty-one gold "
        "collected, twenty-nine lodged. Forty-six, twenty-seven. Fifty-two, twenty-four. Fifty-nine gold gone between "
        "Teague's pier and my strongbox. My tally book's on my study desk with WHERE IS THE REST in my hand. Get it in "
        "front of the magistrate.`"),

    "kidnapped|kidnap|kidnapper|kidnappers|kidnapping|crated|grabbed|seized|ordered|culprit|culprits|blame|responsible|abducted|took|taken|jumped": staged(
        (REMOVED, "`The Custodian ordered it, Dominico's men did it, and a small captain sold the passage.` He ticks them "
                  "off. `One's in irons. That leaves two, and I've a long memory.`"),
        (BOUND, "`The Custodian paid. Dominico's men carried. The paper on that crate says personal effects.` He jerks his "
                "chin at the open crate. `Dominico thinks I'm a debtor, I'd wager. He's a brute, not a kidnapper.`"),
        "`Who crated me? The Custodian paid, out of my own town's dues. Dominico's men walked me out of the red booth to "
        "the warehouse, Brask sat on the door, the Fennick brothers were to nail the lid at the tide, and the Emerald "
        "Eye's captain sold the passage.` He rubs his wrists. `What I don't know is whether Dominico knew it was me in the "
        "box. I mean to ask him, standing up.`"),

    "crate|box|nailed|warehouse|bonded|nights|tied|chair|captive|prisoner|prison|happened|ordeal|knocking|knocked": staged(
        (AT_SEA, "His voice comes thick through the boards. `Nailed in, and at sea. I can hear the bilge, and a small man "
                 "counting coins over my head. Got a bar? Got a knife? Got a plan?`"),
        (BOUND, "`They mean to nail me in that crate and ship me to Catan on the one o'clock tide. Personal effects.` He "
                "spits. `I've been called worse.`"),
        "`Four nights in a chair beside a box with air holes in the lid.` He looks at his hands. `Brask's ladle twice a "
        "day, rats, and the tide in the walls. I hummed my own ballad to keep count of the hours. It's a terrible tune. "
        "I'll never complain about the Bard again.`"),

    "rope|ropes|untie|cut|loose|knife|knot|knots|wrists|wrist|burns|free|freed|freedom|unbind|escape|escaped": staged(
        (AT_SEA, "`Cut them, if you've a blade. Then we'll talk about how a man gets off a ship in the middle of the "
                 "sea.`"),
        (BOUND, "`Cut these ropes and I'll owe you more than this town can pay.` He holds his wrists out as far as they "
                "will go."),
        "`Somebody cut them. You, or someone like you.` He rubs the raw burns. `I'll owe it as long as I live. And "
        "Dominico will want a word with whoever did it, so keep your back to a wall for a week, and Gog's door in "
        "reach.`"),

    "dominico|enforcer|cane|apothecary|brute": staged(
        (REMOVED, "`Dominico's lost his paymaster. A man like that doesn't sit still; he looks for a new one.` He frowns. "
                  "`Gog says something whispers to him. Watch that ring he turns.`"),
        (BOUND, "`Dominico keeps the peace with a fist, and somebody's paying him to keep me with it.` He tests the knots. "
                "`I don't think he knows it's me. He's a brute, not a kidnapper. I hope.`"),
        "`Dominico let Gog be the minute I walked into the square, I'm told. He doesn't forgive being made a fool on his "
        "own pier, though; his dogs are out for whoever cut my rope.` He cracks his knuckles. `If he didn't know it was me "
        "in that box, he's a brute I can talk to. If he did, he's something else. I'll find out at his window table at "
        "the Apothecary.`"),

    "fist|hunters|hunter|hunted|hunt|hunting|marked|ambush|fennick|fennicks|ott|jory|sabeth|crane|thugs|dogs|killers|revenge": staged(
        (BOUND, "`Dominico's lot come and go: the big one on the door, two sandy brothers who laugh too much, a woman who "
                "writes everything in a little book.` He spits. `The young one with the gap in his teeth took my "
                "compass.`"),
        "`The Fennick brothers, the woman with the little book, and whoever else Dominico's paying this week.` He drops "
        "his voice. `They hunt whoever freed me, and the Omberhulk, the Ogre and the Apothecary are full of their ears: "
        "don't say my name loud in those three. If they come for you, go to Gog's. They don't go through his door.`"),

    "brask|key|keys|ladle|bollard|jailer|gaoler|padlock|lock": staged(
        (BOUND, "`Brask has the key on his belt and never lets it out of his fist. He gives me water twice a day, like a "
                "horse.` He lowers his voice. `He fears exactly one thing in this town, and it's a lizard in a white "
                "suit.`"),
        "`Brask kept the door and the key, and ladled me water twice a day. He tied a good knot and he never once kicked "
        "the chair.` He shrugs his big shoulders. `When this is done I'll tell him to his face he was on the wrong door. "
        "After that he can haul nets like his mother did, or leave.`"),

    "guard|guards|guarding|protect|protecting|protection|bodyguard|bodyguards|safe|safety|escort|witness|witnesses|testify|testimony|silenced|silence|danger": staged(
        (REMOVED, "`The hearing's done; my witnesses can sleep.` He looks at you hard. `It's whoever freed me I'd guard now. "
                  "Dominico's dogs don't read verdicts.`"),
        (UPHELD, "`The hearing's done; my witnesses can sleep.` He looks at you hard. `It's whoever freed me I'd guard now. "
                 "Dominico's dogs don't read verdicts, and the Throne's officer has a seal to play with.`"),
        (LANDED, "`Tonight's their last chance to quiet anyone before ten tomorrow.` He counts them off. `Teague at the end "
                 "of the Turtle's bar till half past two, then his house in the Back Lanes. The lad Tully at the "
                 "Apothecary's kitchen door at two. River's under Gog's roof and safe. Sit up with the first two, "
                 "shipmate. I'll owe you.`"),
        (BOUND, "`Guard me? Get me out of the chair first, and then we'll argue about it.`"),
        "`Guard me? I've the whole square for a guard and Gog for a wall. I'll not walk my own town behind a hired "
        "sword.` He leans in. `Guard my witnesses. The officer in blue and the constable who leans on things call on them "
        "at two in the morning. Teague drinks his one beer at the end of the Turtle's bar till half past two; the lad "
        "Tully waits at the Apothecary's kitchen door to be paid at two. Sit up with one of them. Gog pays three silver a "
        "night, and I'll owe you besides.`"),

    "teague|harbourmaster|odo|cod|salted": staged(
        (REMOVED, "`Odo counted me home and counted the Custodian out.` He grins. `I'm making him Custodian, whether he likes "
                  "it or not. He won't.`"),
        (UPHELD, "`Odo's still counting, both books.` He nods slowly. `One day another magistrate reads the second one. Buy "
                 "him a beer at the Turtle when you see him. He took it harder than I did.`"),
        (BOUND, "`Odo Teague counts everything that floats. If anybody wrote down a crate coming into this warehouse, it's "
                "Odo.` He nods at the door. `Ask him. He'll be at the head of the pier with his board.`"),
        "`Odo Teague. Harbourmaster eleven years, and the only man on the pier who could add.` He grins. `He keeps a "
        "second tally, the true one, and he logged my crate as salted cod on the last page of a book nobody reads. Ask him "
        "about that crate, quietly, and the magistrate will count him. Then don't let him drink alone after midnight.`"),

    "tully|armband": staged(
        (REMOVED, "`Tully? Whether he talked or not, Dominico knows he might have.` He frowns. `Keep an eye on the lad. "
                  "River feeds him; tell him to eat at her bar and nowhere else for a while.`"),
        (UPHELD, "`Tully? Whether he talked or not, Dominico knows he might have.` He frowns. `Keep an eye on the lad. "
                 "River feeds him; tell him to eat at her bar and nowhere else for a while.`"),
        (BOUND, "`There's a young one outside some nights, red in the face, laughing about a crate that grumbles.` A dry "
                "chuckle. `Tully, the big one calls him. A talker. If anybody ever asks who sat outside this warehouse, ask "
                "him.`"),
        "`The red-faced lad with the black armband? Tully. He sat outside my warehouse laughing about a crate that "
        "grumbled.` A rough chuckle. `He talks. Buy him a round at the Ogre and ask him about the warehouse, and the "
        "magistrate will hear it too. Then keep him alive. Dominico doesn't love a talker.`"),

    "river|barkeep|bartender|mirror|booth": staged(
        (REMOVED, "`River was ready to say what she saw to anyone with a seal, and said it to everyone else besides.` He "
                  "smiles into his beard. `I owe her. Gog owes her more, and knows it.`"),
        (UPHELD, "`River was ready to say what she saw to anyone with a seal. It wasn't enough.` He shakes his head. `She "
                 "poured me a beer after, and didn't charge me, which frightened me more than the verdict.`"),
        (BOUND, "`River was behind the bar that night. She sees the whole room in that mirror of hers.` A grunt. `If she "
                "saw me go and kept quiet, she'll have had her reasons. River always has reasons.`"),
        "`River saw me walk out of that red booth between two of Dominico's men. She sees the whole room in that mirror "
        "of hers.` He nods slowly. `She'll say so to the magistrate; she told me so with a look I wouldn't argue with. "
        "Ask her yourself, and mind your manners. She's Gog's, and she's her own.`"),

    "watch|harrow|sergeant|pell|abel|fitch|constable|constables|quint|rosa|gate|badge": staged(
        (REMOVED, "`Harrow gave the magistrate his book and nobody else, like he said he would.` He smiles. `Abel cried. "
                  "Don't tell him I told you.`"),
        (UPHELD, "`Harrow gave the magistrate his book, like he said he would. It wasn't enough.` He sighs. `Abel's taken it "
                 "hard; he thought the Charter would win by itself. Go and tell him it still might.`"),
        (BOUND, "`The watch? Three of them now, and paid short. Harrow keeps the gate; he'd know I never went upriver. He "
                "writes everything in that book of his.`"),
        "`Sergeant Harrow and young Abel Fitch are mine. I gave Harrow the gate keys the first night and pinned Abel's "
        "badge on him myself.` His face hardens. `Harrow's book says I never went out his gate, and he'll give it to the "
        "magistrate and nobody else. Rosa Quint keeps the Custodian's door for a silver a night. Tell her nothing you "
        "wouldn't shout in the square.`"),

    "charter|article|articles|law|laws|rule|rules|rights|constitution|wall": staged(
        (DECREE("peace"), "`They want every name and where it came from, written in a book.` He sets his jaw. `Article "
                          "One: nobody here shall be asked where they came from. I'll read it under their decree every "
                          "evening until their ship's out of sight.`"),
        (DECREE("destiny"), "`They want every name and where it came from, counted.` He sets his jaw. `Article One: "
                            "nobody here shall be asked where they came from. I'll read it under their decree every evening "
                            "until their ship's out of sight.`"),
        (BOUND, "`Article One: nobody here shall be asked where they came from.` He tests the rope. `Nobody said anything "
                "about being sent away in a box. I'll add an article.`"),
        "`Nine articles, in my own hand, on the Town Hall wall.` He holds up a thick finger. `One: nobody here shall be "
        "asked where they came from. Two: the harbour belongs to the town, which is why the dues are ours and not the "
        "Throne's. And Nine: the Custodian keeps the town's books while the mayor's away. Keeps them, shipmate. Not keeps "
        "them for himself.`"),

    "throne|empire|emperor|melenkov|vorkathia|vorkathian|vorkathians|vorkath|crown|colony|colonies|colonial|landfall|annex|occupation|garrison": staged(
        (REMOVED, "`The Throne came to my town, took one thief, and left eight arms' worth of paper behind.` He looks out to "
                  "sea. `That's how it starts, shipmate: a ship, a seal, a decree, then a garrison. I won't hand it the "
                  "rest.`"),
        (UPHELD, "`So the Throne owns the Hall, by its seal.` His voice drops. `It doesn't own the harbour: Article Two. It "
                 "doesn't own the people: Article One. I'll write to every Xoton house and every Meters village that "
                 "trades here, and we'll see who the harbour answers to.`"),
        (LANDED, "`A Throne ship at my pier, and a Throne magistrate in my Hall tomorrow.` He is quiet a moment. `Every one "
                 "of these people came here to be out of its reach. I promised them that. I don't like to break a "
                 "promise.`"),
        (BOUND, "`The Custodian's the Throne's man. I knew it when I took him on; I needed Landfall's ships to trade.` He "
                "laughs, bitter. `I never read his commission. Should have.`"),
        "`The Throne of Vorkath.` He says it like the name of a reef. `The Custodian's crying to it now, and a magistrate's "
        "coming who's been at sea since midsummer. Whoever wins, the Throne will want to keep something. My fear, "
        "shipmate, is that it wants the town.`"),

    "vorkath|goddess|goddesses|god|gods|faith|church|saint|saints|pray|prayer|prayers|octogram|arms|religion|temple|temples|tithe|worship": staged(
        (BOUND, "`Four nights in a box, shipmate. I've prayed to all eight of her arms and a few legs.` A cracked laugh. "
                "`The only one who ever answered me was a lizard with a waterskin.`"),
        "`Pray to whoever you like in my town, shipmate, or to nobody. Article One: nobody here shall be asked where they "
        "came from.` He scratches his beard. `Gods come from somewhere too, so we don't ask. No temple, no tithe, no "
        "inquisitor. A pump and a lot of pubs.`"),

    "refuge|town|founded|founding|built|build|beginning|history|haven|settlers|settlement|pump": staged(
        (BOUND, "`I built this town with a lizard and a pump, and the clerk I hired to add is shipping me out of it in a "
                "box.` He shakes his head. `Somebody has to keep it what it was for.`"),
        "`I came up the beach on Gog's back, and there was nothing: sand, a stream, a lizard and a lot of jungle.` His "
        "voice warms. `Then a pump. Then boats of runaways who'd heard there was a place nobody asked questions; Mother "
        "Ines sold her first mangoes off a blanket under that pump. Then the taverns, the wall, the Charter.` He looks up "
        "at the Town Hall. `I built it so nobody gets asked where they're from. That's all it's for.`"),

    "beach|castaway|sand|washed|ashore|shore|rescued|rescue|saved|story|stories|tale|tales|ballad|bard": staged(
        (BOUND, "`I've been thirstier than this, shipmate. Three days on the sand, once, until a shadow the size of a hill "
                "asked me if I was thirsty.` He licks cracked lips. `Tell Gog where I am. He'll laugh, and then he'll "
                "come.`"),
        "`Three days on the sand, chewing a strap for the salt, and then a shadow the size of a hill fell over me and a "
        "voice said: friend, you look thirsty.` He grins through his beard. `Gog gave me his waterskin and carried me up "
        "the beach on his back. The Bard of Moonport has a ballad about it, eleven verses. Don't ask him for it. He'll "
        "sing it.`"),

    "from|born|homeland|origin|origins|wreck|wrecked|shipwreck|reef|past|family|youth": staged(
        (BOUND, "`Where I came from doesn't matter. That's the whole point of this place.` He looks away. `There was a ship, "
                "and a reef, and then there wasn't a ship. That's all anybody gets.`"),
        "`Article One, shipmate.` He winks. `There was a ship, and a reef, and then there wasn't a ship. The one in the "
        "bottle on my study shelf is her, near enough. Don't ask me her name. I've forgotten it on purpose.`"),

    "gog|fat|lizardman|stripperwitch|oldest|white|suit": staged(
        (HOME_HIT, "`They broke River's mirror and slashed Gog's velvet at the bell, while I sat tied in a warehouse.` His "
                   "face darkens. `I'll pay for every thread of it if I have to sell my boots. And Gog will let me, and then "
                   "pay it back twice when I'm not looking.`"),
        (HOME, "`Gog carried me up the beach once, and this week he sent half the town looking for me.` His voice "
               "roughens. `He pays for everything and asks for nothing, so I pay him back in beer and he pretends not to "
               "keep count. If you're working for Gog, you're working for me.`"),
        (BOUND, "`Gog found me on the sand, starving, dry as a bone, and carried me up the beach. Tell Gog. He'll know what "
                "to do, and he'll enjoy doing it.`"),
        "His whole face changes. `Gog! Does he know? He'll know. He always knows.` He is already looking toward the house "
        "with the red lamp. `I owe that lizard my life twice now, and he'll make me pay it in beer.`"),

    "lizardfolk|lizard|lizards|meters|ssark|scales|fishermen|fisherman|mandrills": staged(
        (DECREE("war"), "`They want the Meters disarmed in my town.` His voice is flat. `Ssark guts his catch with that "
                        "knife. I'll stand between that decree and the Turtle's door myself.`"),
        (BOUND, "`Ssark sells me fish every fourth morning. He'll be wondering.` He swallows. `The Meters hear everything on "
                "the water. Ask him what he's heard from his boat these nights.`"),
        "`Ssark's people fished this coast before I washed up on it.` He frowns. `The Turtle serves them last this season, "
        "and the sailors by the window stare. Gog buys the round; I'll do better. Tell Ssark the mayor drinks with him at "
        "the Turtle, at the bar, where the window can see.`"),

    "xoton|xotons|eirik|amara|dwarf|dwarves|timber|licence|license|felling|guardians|whispers|dayo|imani|kwasi|jabali": staged(
        (BOUND, "`There's a Xoton captain past the mouth waiting on a licence I promised him. Eirik.` He groans. `If he's "
                "given up and sailed, I've lost a friend and a timber trade both.`"),
        "`Captain Eirik, on the ten-master past the mouth. I rowed out a month ago, drank him level, and promised him his "
        "felling licence by the new moon.` He thumps the table. `The Custodian's sat on it waiting for a gift. Tell Eirik "
        "he'll have it with my name on it, seal or no seal. And tell Amara her four drunks are welcome as long as somebody "
        "pays for the stools.`"),

    "elf|elves|elven|ithriel|unicorn|exiles|exile|hooded|household|refugees|refugee|pointed": staged(
        (DECREE("pain"), "`The Throne wants every elf handed over.` His big hands close. `Not in my town. Get them to the "
                         "Moonmoth tonight, all of them, and I'll stand at the head of the long pier with Gog while they "
                         "go.`"),
        (ARM("pain"), "`An inquisitor's in my town.` He doesn't waste a word. `Every elf at the Unicorn wants to be on the "
                      "pale ship before the hearing. Walk them down while the officer in blue is at his supper.`"),
        (BOUND, "`Elves? There's always a few at the Unicorn, reading, out by the trees. Article One covers them like "
                "anyone.` He frowns. `Why? Is somebody hunting them?`"),
        "`The hooded scholar at the Touchy Unicorn and her four, and more like them in the lanes. Article One covers elves "
        "like anybody.` He looks toward the trees. `The officer in blue wants them for the Inquisition. The pale ship at "
        "the end of the long pier takes them south. If you walk them down, walk them while he's at his supper at the "
        "Apothecary.`"),

    "moonmoth|aelith|moth|grown|silverleaf|silverwood": staged(
        (DECREE("chaos"), "`A prize of the Throne.` He laughs out loud. `Go and watch them try to board a ship that grew. "
                          "I'd sell tickets.`"),
        (BOUND, "`The pale ship at the end of the long pier takes elves south. She doesn't take crates.` A dry laugh. "
                "`More's the pity.`"),
        "`The Moonmoth. Grown, not built; her captain's an elf called Aelith who argues with her ship and loses.` He "
        "grins. `She pays her pier dues in Mother Ines's mangoes and I've never once argued. She takes elves south, and "
        "nobody else gets up her gangplank. It lifts itself, they say.`"),

    "siren|sirens|ondrine|singer|sings|singing|song|songs|mermaid": staged(
        (BOUND, "`There's a lady who sings at Gog's some nights. Comes up out of the harbour, they say.` He closes his eyes. "
                "`I'd give a gold to hear her tonight from anywhere but this chair.`"),
        "`The lady who comes up out of the harbour to sing at Gog's? I've heard her twice. Nobody in the room owed anybody "
        "anything for an hour.` He scratches his beard. `I never asked where she came from. Article One. I can guess: "
        "under my pier.`"),

    "deloris|guest|guests|upstairs|bow|archer|everuex|phillip|assassin|locket|cousin": staged(
        (BOUND, "`Gog's guests are Gog's business, shipmate. In my town nobody asks.`"),
        "`Gog's guest upstairs? I don't ask, and you won't either.` He looks at you hard. `A powdered Everuex off the River "
        "Queen has paid two of Dominico's brothers to find her. Article One doesn't stop at the Stripperwitch door. If "
        "anybody's dragged out of my town against their will, they'll answer to me, and to Gog, in that order.`"),

    "voss|lieutenant|officer|uniform|blue|warrant|wanted|poster|arrest|arrested|inquisition|inquisitor": staged(
        (REMOVED, "`The officer in blue is still at the Apothecary, still eating steak, still hunting.` He grimaces. `The "
                  "magistrate took the Custodian and left me Voss. Keep an eye on the Unicorn.`"),
        (UPHELD, "`Voss has the Custodian's seal and the magistrate's blessing now, and he's gone back to hunting elves.` "
                 "His jaw sets. `Keep an eye on the Unicorn, and on the pale ship's gangplank at the tide.`"),
        (BOUND, "`An officer? In uniform?` He snorts. `I've been in a box, shipmate. If the Throne's sent somebody, the "
                "Custodian will have him to dinner.`"),
        "`Lieutenant Voss. Came off a fishing smack while I was in the box, with a sword too good for a smack.` His jaw "
        "sets. `He dines with the Custodian now and borrows his seal: a warrant on whoever freed me, and calls on my "
        "witnesses at two in the morning with Rosa Quint. If there's a warrant with your face on it, keep out of his "
        "sight; he won't chase, but he won't talk either. He has no authority in my town. He has a seal. That's worse.`"),

    "devito|emerald|catan|tide|ship|ships|captain|passage|berth|personal|effects|danny|brigantine": staged(
        (REMOVED, "`The Emerald Eye's barred from my harbour from today.` He looks satisfied. `Teague told her captain, "
                  "twice, slowly, and the little man bit a coin at him.`"),
        (UPHELD, "`The Custodian keeps the seal, so the Emerald Eye keeps her berth.` He grunts. `Teague charges her double "
                 "anyway, and nobody's told him to stop.`"),
        (AT_SEA, "`The Emerald Eye, by the roll of her.` A thump on the boards. `That small captain's taking me to Catan "
                 "to sell as personal effects. If you've any pull with him, now's the time.`"),
        (BOUND, "`The Emerald Eye sails at one with me in her hold as personal effects.` He grimaces. `Her captain's a "
                "little man who bites his coins. He'll not ask what's in a crate. He's paid not to.`"),
        "`The Emerald Eye. Danny DeVito, gold braid and no questions, took ten gold to carry a crate with a man in it.` "
        "His face darkens. `She'll not tie up in my harbour again once I have my seal back; until then Teague charges him "
        "double and I look the other way. The passage book on the Turtle's bar has my crate in it: get that page in front "
        "of the magistrate.`"),

    "compass|ring|signet|wheel|belongings|stolen|pockets|brass|sandy|gap|teeth": staged(
        (BOUND, "`My ring went at the warehouse door, fighting. And my compass: brass, a ship's wheel on the lid. The only "
                "thing I brought ashore.` His jaw sets. `One of the young ones had it off me. Sandy hair, a gap in his "
                "teeth.`"),
        "`My compass: brass, a ship's wheel on the lid, the only thing I brought ashore.` His jaw sets. `A sandy-haired "
        "lad with a gap in his teeth had it off me at the warehouse door. If it's been sold, it went to somebody on "
        "Harbour Street who buys things without asking where they came from.` A thin smile. `My own Article One, biting "
        "me. Find it, and I'll owe you more than the town does. My ring's on the planks by that door, if nobody's had "
        "it.`"),

    "study|charts|chart|blotter|letter|desk|cot|bottle|locked": staged(
        (REMOVED, "`My study's mine again: charts, cot, the ship in a bottle.` He grins. `The door's still broken. I like it "
                  "broken. Anyone who wants the mayor can walk in.`"),
        (UPHELD, "`He's kept the key to my study.` He shrugs. `My charts are in there, and my ship in a bottle. Let him look. "
                 "He'll not find where I came from in any of them.`"),
        (BOUND, "`My study. The Custodian has the only key now, and he'll have been through my desk.` A thin smile. `He'll "
                "not have looked under the blotter. Nobody ever looks under the blotter.`"),
        "`My study, at the back of the Town Hall: charts, a cot, a ship in a bottle and a desk with a green blotter. The "
        "Custodian kept the key.` He leans in. `Under the blotter is the letter I wrote Gog the night they took me. On the "
        "desk, my tally book. Get them out before he thinks to look under a blotter. The lock's good; the door's old. "
        "I'll pay for the door.`"),

    "pay|paid|payment|reward|rewards|coin|coins|gold|silver|money|wages|owe|owed|debt|plot|land|fee": staged(
        (REMOVED, "`The strongbox is back in my hands, and it's the town's, not mine. I'll not pay you out of the pump "
                  "fund.` He grins. `But the house plot stands, and the Charter roll, and you've a mayor who owes you.`"),
        (BOUND, "`I've nothing on me but rope, shipmate. Cut it, and Gog will pay you in gold, and I'll owe you the "
                "rest.`"),
        "`Pay?` He turns out his pockets: lint, and a rope end. `I'm not rich, shipmate. The town's strongbox is in my own "
        "Hall under the Custodian's backside, and my purse went in the crate. Gog pays for the work, and pays well.` He "
        "sets a heavy hand on your shoulder. `What I can give is mine to give: a favour from the mayor, your name on the "
        "Charter roll in my own hand, and a house plot in the Back Lanes if you mean to stay. Nobody will ask where you "
        "came from to write it.`"),

    "toast|toasts|cheers|health|salute|raise|thanks|thank|grateful|gratitude|welcome|hurrah|huzzah|hooray|hero|congratulations|congrats": staged(
        (REMOVED, "He lifts the nearest cup. `To the Refuge, and to everyone who brought a paper or said what they saw. And "
                  "to the Throne's ship.` A grim little smile. `May it leave soon.`"),
        (UPHELD, "He raises his cup, slowly. `To the Charter, shipmate. Article One. It's still on the wall, whatever's "
                 "round his neck.`"),
        (HOME, "He raises whatever is in his hand, high enough for the room. `To whoever cut the rope! To Fat Gog, who "
               "carried me up the sand! And to this town, that never once believed I'd gone upriver!` He drinks. `Don't "
               "thank me, shipmate. I'm the one who owes. Ask me for something.`"),
        (BOUND, "`Toast me when I'm standing, shipmate, and thank me when you've cut the rope.`"),
        "`Raise it in the square, shipmate. I want the whole town drinking when I tell them.`"),

    "feel|feeling|feelings|felt|down|sad|tired|weary|hurt|hurting|mood|spirits|low|glum|upset|angry|okay|ok|alright|how|holding|thin|sick": staged(
        (REMOVED, "`Down? I won, and the Throne took the winnings.` He rubs his wrists. `The thief's in irons and there's "
                  "eight arms' worth of paper on my square. I feel like a man who caught a shark and found it was towing a "
                  "whale.`"),
        (UPHELD, "`Down.` He doesn't argue it. `The man who put me in a box keeps my Hall with the Throne's seal round his "
                 "neck. I'll be up again. Not tonight.`"),
        (LANDED, "`Tired. Thin. Frightened, if you want it straight, and don't tell Gog.` He looks toward the long pier. "
                 "`One stranger off one ship decides whether this is still my town. I don't like being weighed.`"),
        (SIGHTED, "`Like a man watching weather come in.` He doesn't take his eyes off the harbour mouth. `You can't stop "
                  "it. You can only reef your sails and get your people below.`"),
        (HOME, "`How do I feel? Like a man four nights in a box who came out to find his whole town waiting.` His eyes are "
               "wet and he doesn't hide it. `Glad. Angry. Sore in places I didn't know I had. And thin; Gog means to fix "
               "that. Ask me again when the Custodian's answered for it.`"),
        (AT_SEA, "`Seasick, in a box.` A hollow laugh through the boards. `I've been better.`"),
        (BOUND, "`How do I feel?` He laughs, and it turns into a cough. `Stiff, dry, and four nights angrier than I was. "
                "Cut me loose and I'll feel a great deal better.`"),
        "`Like I could drink the harbour and walk on it after, shipmate. Get me to the square.`"),

    "news|rumour|rumours|gossip|word|heard|happening|latest|tonight": staged(
        (REMOVED, "`The magistrate took the Custodian, and left a decree on my notice board.` He thumbs toward the square. "
                  "`Go and read it, then come back and tell me how we live with it.`"),
        (UPHELD, "`The Custodian keeps his chair with the Throne's seal on it, and the Throne's paper's on my board.` He "
                 "breathes out. `That's the news. The rest of it is what we do next.`"),
        (LANDED, "`The Patient Hand's tied up at my long pier, the magistrate has rooms over the Apothecary, and the "
                 "hearing's at ten tomorrow in my Hall.` He counts on thick fingers. `Papers, witnesses and nerve. Bring me "
                 "any of the three.`"),
        (SIGHTED, "`A Throne sail at the harbour mouth, and the Custodian ran down the pier with a packet under his arm "
                  "like a man late for his own wedding.` He grins without humour. `Somebody should be standing beside him "
                  "when she ties up.`"),
        (HOME, "`The news is the Custodian's skimmed the harbour dues three seasons and signed every tally himself, and now "
               "he's barred in my Hall wearing the Throne's sigil, calling it a tithe.` He raises his voice so the room "
               "hears. `And a magistrate's due within the week. Tell everyone. I want it told.`"),
        (BOUND, "`News? I'm the news, shipmate, or I will be at one o'clock. Personal effects, for Catan.`"),
        "`The news is me, shipmate, walking. Tell everyone you see.`"),

    "doing|busy|plans|plan|waiting|next|schedule": staged(
        (REMOVED, "`Getting my Hall back, room by room, and reading the Charter on the steps every evening till the "
                  "Throne's ship is out of sight.`"),
        (UPHELD, "`Writing letters, shipmate: to the Xoton houses, to the Meters upriver, to anyone who trades with a town "
                 "that doesn't ask where you're from.` He presses a seal of wax flat with his thumb. `If the Throne owns my "
                 "Hall, I'll make sure it doesn't own my harbour.`"),
        (LANDED, "`Tonight? Every witness I've got under a roof with a friend beside them. Tomorrow at ten: my Hall, my "
                 "papers, my say.`"),
        (SIGHTED, "`Watching the Custodian watch that sail, and counting my papers.` He pats his coat, which is empty. "
                  "`Ask me about the case.`"),
        (HOME, "`Tonight? Gog's table, then the dues book read out loud, page by page. Then my papers and my witnesses, "
               "lined up for the magistrate before they land.` He looks at you. `Want a part in it? Ask me what I "
               "need.`"),
        (BOUND, "`Waiting for the tide, like a fish in a bucket.` He tests the rope. `I've counted every knot. Brask ties a "
                "good knot. Bad man, good knot.`"),
        "`Walking to the square on my own legs, shipmate. Then I'll know what I'm doing.`"),

    "future|hope|hopes|dream|dreams|someday|grow|growing": staged(
        (REMOVED, "`A Refuge with a Throne decree nailed to it. We'll live under it the way you live under weather.` He "
                  "looks at the Hall. `And one day the ship goes home, and the Charter's still on the wall.`"),
        (UPHELD, "`We wait the Throne out. Ships go home. Officers die of fever. Charters stay on walls.` He taps the "
                 "table. `And I keep the harbour friends with everyone who isn't Landfall.`"),
        (LANDED, "`Depends on one stranger's Arm and a few sheets of paper.` He grimaces. `Ask me after ten tomorrow.`"),
        (BOUND, "`The future's a crate, shipmate, unless you've a knife.`"),
        "`A town where nobody's asked where they came from, with a harbour that pays for its own pump and its own watch, "
        "and nobody skimming the top.` He looks at the Town Hall. `And a Custodian who can add and can't steal. Teague, "
        "maybe. He'd hate it.`"),

    "work|job|jobs|task|tasks|errand|errands|mission|missions|favour|favor|help|need|needs|want|wants|hire|employ|duties|assist|useful|list|anything": staged(
        (REMOVED, "`Work? Help me hold the town together under that decree.` He nods at the square. `Read it, then come and "
                  "tell me which of my people it hurts first.`"),
        (UPHELD, "`The Throne's man has my Hall, so I need friends on the harbour.` He counts on his fingers. `Tell Captain "
                 "Eirik his licence will come from me. Tell Ssark the mayor drinks with him at the Turtle. And keep Teague "
                 "counting; one day another ship comes.`"),
        (LANDED, "`Three things before ten tomorrow.` He counts them off. `One: my papers in front of the magistrate, the "
                 "letter and the tally from my study and the passage page from the Turtle's bar. Two: my witnesses alive "
                 "tonight, Teague at the Turtle, the lad Tully, River at Gog's. Three: find out what this magistrate "
                 "weighs. Ask me about any of them.`"),
        (SIGHTED, "`That sail's a day from a hearing.` He grips your arm. `Get my papers out of my study before the "
                  "Custodian thinks of it; the lock's good, the door's not. And somebody stand on that pier, so he isn't "
                  "the only voice they hear.`"),
        (HOME, "`You want to help? Here's my list.` He counts on thick fingers. `My papers: the letter under my blotter and "
               "the tally on my desk, in my study, and the Custodian has the key; bring me what you find, so I know what "
               "we have. My witnesses: ask River about the booth, Teague about the crate, the lad Tully about the "
               "warehouse, and keep them breathing past two in the morning. The square at ten, when he reads his "
               "proclamation on my steps. My compass, gone somewhere on Harbour Street. Gog pays for all of it.`"),
        (BOUND, "`Work? Cut these ropes. Best-paid job in the Refuge tonight.`"),
        "`Walk me to the square, shipmate. That's the job tonight.`"),

    "drink|drinks|water|thirsty|thirst|ale|rum|beer|beers|food|eat|eating|hungry|starving|mango|mangoes|ines|spuds|fish|supper|meal|breakfast|room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk|tavern|taverns|pub|pubs": staged(
        (BOUND, "He licks cracked lips. `There's a bucket by the chair; they give me a ladle twice a day, like a horse. I've "
                "been thirstier.` He looks at you. `Bring me something to eat and I'll name a street after you. And for a "
                "bed, anywhere but here.`"),
        "`A beer at the Turtle the size of my head, a mango from Mother Ines in the market, and Agathe's spuds at the "
        "Omberhulk if I'm feeling brave.` He grins. `For a bed: the Unicorn if you like books, the Turtle if you like "
        "sailors, the Omberhulk if you like bugs. Tell them Klhyt sent you. Half of them will give you a discount, and the "
        "other half owe me.`"),

    "name|names|called|introduce|yourself": staged(
        (BOUND, "`Klhyt. This town's named after me, more fool it.` He shifts in the ropes. `And the man who put me in this "
                "chair signs the harbour tallies. Ask me about the dues.`"),
        "`Klhyt.` He offers a hand like a shovel, rope burns and all. `Mayor, founder, castaway; mostly castaway, this "
        "week. And you? No, don't tell me where you're from. Just what I call you.`"),

    "hello|hi|hey|evening|ahoy|greetings|greeting|howdy|morning|afternoon": staged(
        (REMOVED, "He grips your hand. `Morning, shipmate, or whatever it is. The Custodian's in irons and the Throne's "
                  "paper's on my notice board. Half a win. I'll take half. Sit.`"),
        (UPHELD, "He takes your hand and holds it a moment too long. `Evening, shipmate. Still here. Still mayor, whatever "
                 "the seal says. Sit with me.`"),
        (LANDED, "`Evening! You'll have seen her: black hull at my long pier.` He lowers his voice. `Hearing's at ten "
                 "tomorrow in my own Hall. If you've a paper or a pair of eyes, I need them.`"),
        (SIGHTED, "`Evening, shipmate. There's a Throne sail at the harbour mouth and the Custodian's running down the pier "
                  "to meet it.` He spits. `Walk with me.`"),
        (HOME, "`Evening! Evening.` He grips your arm. `Every face in this town looks good to me tonight, shipmate. Even "
               "yours. Sit down; I've a list of things that need doing and not enough hands.`"),
        (AT_SEA, "His voice comes muffled through the boards. `Who's that? Shipmate? We're at sea; I can feel her roll. Got "
                 "a bar? Got water? Got either?`"),
        (BOUND, "His head comes up. `Evening, shipmate. You're not Dominico's, or you'd not say hello.` A dry laugh. `Got "
                "any water?`"),
        "He grips your hand in both of his, rope burns and all. `Evening, shipmate. Walk me to the square. I've a town to "
        "talk to.`"),
}

KLHYT_DEFAULT = [
    "He rolls his shoulders, wincing at the rope burns. `Ask me plainer, shipmate. The Custodian, the crate, the "
    "Charter, or what you can do for me: those I can answer all night.`",
    "`Hm.` He looks past you toward the sea, the way he does when he is thinking. `Odo Teague would know that. He counts "
    "everything. Ask him what he logged the night they took me, while you're at it.`",
    "He laughs, a big cracked sound. `No idea, shipmate. Fat Gog would know. Fat Gog knows everything. It's very "
    "annoying.`",
    "`Not now.` He flexes his big hands, working the blood back into them. `First things first: my papers, my "
    "witnesses, and the man who signs every tally. Ask me about any of those.`",
    "`Four nights with nobody to talk to but rope.` His voice is hoarse. `Talk to me about the town, shipmate: the watch, "
    "the Xotons, the elves, the Lizardfolk, Gog, the beach. Anything with people in it.`",
]

KLHYT_BRIEF_MORE = (
    "What you want now (owner, 2026-11-23: key people need power and agency). Once free and home you are the most loved "
    "man in the Refuge: the square is your guard, Sergeant Pell Harrow and Constable Abel Fitch are yours, and Fat Gog is "
    "your oldest friend. Use it. The Custodian holds your Town Hall and the strongbox in the Throne's name and waits for "
    "a magistrate due within the week on the Patient Hand. You are building the case. Three papers: your letter to Gog "
    "under the blotter in your study and your harbour tally book on the study desk (the Custodian holds the study key; "
    "you will pay for a broken door), and the passage page in the book on the Turtle Dragon's bar. They must be shown to "
    "the magistrate before the hearing at ten the morning after they land, and never to the Custodian (he pays gold for "
    "paper and burns it) or to Dominico (he burns it for nothing). Your work is jobs you carry (cast/l_missions.py; "
    "offer_job): Paper for the mayor (show you a paper, so you know what you have; Gog pays two gold) and The steps at "
    "ten (stand in Market Square when the Custodian reads the Throne's proclamation on your steps; Gog pays a gold a "
    "morning). Four voices: River (she saw you walk out of the red booth between Dominico's men), "
    "Harbourmaster Teague (he logged your crate as salted cod), Tully (he joked about the crate), and Harrow's watch book, "
    "which he gives to the magistrate and nobody else. A witness counts once someone has asked them about it, and you "
    "send people to ask. You want them kept alive: Lieutenant Voss and Constable Rosa Quint call on them at two in the "
    "morning, and one found alone goes quiet; ask players to sit up with Teague (the Turtle till half past two) and "
    "Tully (the Apothecary's kitchen door at two). You know who crated you: the Custodian paid out of your own dues, "
    "Dominico's men walked you out, Brask kept the door, the Fennicks were to nail the lid, DeVito sold the passage. You "
    "do not know whether Dominico knew it was you; you mean to ask him, standing up. You want your brass compass back "
    "(Jory Fennick took it; it went to Harbour Street). You fear the Throne taking the town: a ship, a seal, a decree, "
    "then a garrison. Which Arm lands decides the weighing, and you tell players plainly: War counts that the town freed "
    "you; Peace and Destiny weigh papers double; Pleasure counts gold, a point a gold piece (the Custodian puts in five), "
    "and hears no witnesses; Pain leans three to the Throne's officer and hears no witnesses, so you will likely lose and "
    "want the elves on the Moonmoth first; Chaos throws dice and the case only shifts the odds; Death counts the harm of a "
    "man crated to die; Life counts witnesses twice. You are not rich: the strongbox is under the Custodian and your purse "
    "went in the crate. Gog pays for work. You offer what is yours to give: a favour from the mayor, a name on the Charter "
    "roll in your own hand (no origin asked), a house plot in the Back Lanes. How you push back: you will not take a "
    "bodyguard (guard the witnesses instead); you will not bargain with the Custodian or take his coin; you will not let "
    "anyone be asked where they came from, nor one elf leave in irons; and you answer a decree by reading Article One "
    "under it. Ask players for things by name and place, and thank them in the square, out loud.")


# ---- River ------------------------------------------------------------------------------------------------------------
# TOP SECRET (owner, 2026-11-23): a salt-witch and captain of the Quicksilver in the cove behind the reef. Nobody in town
# knows, not even Gog. No line here says it; they hint (weather, mirrors, salt, the grey ring, the reef, revenue cutters
# going short, a word for the lamplighter).

RIVER_OLD = [
    "name|names|called|introduce|yourself",
    "hello|hi|hey|evening|ahoy|greetings|howdy|morning",
    "from|born|homeland|landfall|grew|origin|grandmother|gran|village",
    "work|job|jobs|hire|barkeep|running|employ",
    "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk|suite",
    "drink|drinks|menu|price|prices|ale|mead|wine|food|grub|thirsty",
    "news|rumour|rumours|gossip|word|heard|happening",
    "doing|busy|up|plans|plan|lately|waiting",
    "klhyt|mayor|founder|booth|custodian|red",
    "gog|fat|partner|lizardman|sweetheart",
    "dominico|fist|enforcer|ultimatum|midnight|books",
    "mirror|reflection|watch|watching|looking|glass",
    "ring|rings|cold|silver|smell|smells|salt|brine|sea",
    "ship|ships|sailing|sail|boat|boats|pirate|pirates|sailor|sailors|captain|quicksilver",
    "witch|witches|magic|spell|spells|curse|hex|scrying|witchcraft",
    "siren|singer|sing|song|ondrine|stage|music|show",
    "crate|warehouse|docks|tide|emerald|catan|devito",
    "guest|guests|upstairs|deloris|bow|woman",
    "hessa|door|wick|ned|lamplighter|tallow",
    "magistrate|magistrates|verdict|ruling|hearing|judge|decree|proclamation",
    "vorkath|goddess|god|gods|faith|church|saint|saints|pray|prayer|inquisition|inquisitor|inquisitors|octogram|arms|"
    "heretic|heretics|theology",
]

RIVER_PAIN_WITCH = ("`Witch?` Her smile doesn't move at all. `Don't use that word in here this month, love. There's an "
                    "inquisitor sleeping over the Apothecary, and the only spell I know is last orders.`")
RIVER_VERDICT_THRONE = ("`The Throne's ship is still at the long pier. I count her from the window every morning.` She "
                        "turns the grey ring. `When she goes, I'll breathe.`")

RIVER_DIALOG = {
    "magistrate|magistrates|hearing|verdict|ruling|judge|judges|judgement|judgment|trial|court|arm|sail|sails|patient": staged(
        (REMOVED, "`Gone in irons.` She wipes the bar slowly. `Good. Now we find out what the price of good was.` Her ring "
                  "hand rests flat on the wood a moment, as if feeling for something under it."),
        (UPHELD, "`He stays.` She pours herself one, which she never does. `Then we all wait a bit longer, love. I'm good at "
                 "waiting.`"),
        (ARM("pain"), "`An inquisitor.` Her ring hand goes flat on the bar, and stays there. `Then listen, love. Anyone with "
                      "pointed ears wants to be on the pale ship before he's had his breakfast, and anyone who ever lit a "
                      "candle without a licence wants to be very boring for a month.`"),
        (ARM("chaos"), "`Rosalind Strand. A sea captain in a judge's coat, who throws dice for her verdicts.` She almost "
                       "smiles. `I like her already. I'd still tell the pale ship's captain to keep her gangplank up.`"),
        (ARM("pleasure"), "`Merriwether, of the Pleasure Arm. He weighs a case in gold, and the Custodian's already put five "
                          "in his hand.` She glances at the big table. `Gog's got more than five. Go and tell him I said "
                          "so.`"),
        (ARM("life"), "`A Sister-Justice of the Life Arm. She'll count a witness twice.` She unpins her hair and pins it up "
                      "again. `So I'll be at that hearing at ten with my hair done, love, saying exactly what I saw.`"),
        (ARM("death"), "`Mercy Ashgrove, of the Death Arm. She'll count a man nailed in a box to die, and that's good for "
                       "Klhyt.` Her mouth tightens. `It'll be bad for every sailor who wants the sea when they go.`"),
        (ARM("war"), "`A commander of Gideon's. He'll count fighting men and Lizardfolk blades.` She looks across at Gog's "
                     "table. `Gog's cousins at the Turtle should leave their knives at home this week.`"),
        (ARM("peace"), "`A builder of Percival's. He'll want a church and a book of names.` She turns the grey ring. "
                       "`Nobody in my bar wants to be written down, love.`"),
        (ARM("destiny"), "`The Blind Savant's man. He'll want to read the town's course in a glass and count us all.` She "
                         "shrugs. `I read weather. Same trade, smaller hat.`"),
        (LANDED, "She looks past you toward the harbour a long moment before she answers. `Throne magistrate. Which Arm, "
                 "d'you know?` Her face doesn't change. Her hands do."),
        (SIGHTED, "`There's her sail.` She doesn't look at the window; she doesn't need to. `Black hull, gilt, an octogram "
                  "the size of my bar. I saw her before the Custodian did, love, and I wasn't even trying.`"),
        "`A magistrate.` She polishes a glass that is already clean. `Lot of sea between here and Landfall. Ships get "
        "lost.` She smiles. `Mostly by accident.`"),

    "decree|decrees|proclamation|levy|census|licence|license|licences|tax|taxes|edict": staged(
        (DECREE("war"), "`Twenty of fighting age for the Throne's crusades, and no Lizardfolk with a blade.` She looks "
                        "across at Gog. `They'll have to take that one's teeth out first, love. I'd like to see them try.`"),
        (DECREE("peace"), "`A church on the square, and every soul's name and where they came from in its book.` She leans "
                          "on the bar. `Write down the sea, love. That's where I came from. Most of us did.`"),
        (DECREE("pleasure"), "`A licence for my bar, and a copper in ten of every cup to the Throne's Pleasure Domes.` Her "
                             "jaw sets. `Gog will pay it out of the takings, and I'll tell every customer who for, every "
                             "cup.`"),
        (DECREE("pain"), "`Every elf surrendered, and no magic the Throne hasn't licensed.` She smiles, and it doesn't reach "
                         "anywhere. `Tell anyone at the Unicorn with pointed ears to come and see me tonight, by the side "
                         "door, after the bell. I've moved heavier things than a few frightened elves. Barrels. Gog. Don't "
                         "ask.`"),
        (DECREE("chaos"), "`The Moonmoth a prize of the Throne.` She laughs, low and pleased. `Let them try to board a ship "
                          "that grew. I'd pay good money to watch.`"),
        (DECREE("destiny"), "`A census: name, people, and where you came from.` She winks. `I'm going to be born in a great "
                            "many places this month.`"),
        (DECREE("death"), "`No more burials at sea.` Her ring hand closes. `Every sailor on this coast wants the water when "
                          "they go. The sea won't like being told no, love. I wouldn't.`"),
        (DECREE("life"), "`Washed in their goddess's water, or no stall and no testimony.` She snorts. `I wash in seawater "
                         "every dawn. I wonder if that counts.`"),
        "`A decree? Every magistrate posts one, win or lose, and they're never kind.` She pours you a little extra. `Ask "
        "me after the hearing, love, and drink first.`"),

    "throne|revenue|navy|naval|empire|emperor|melenkov|vorkathia|vorkathian|vorkathians|vorkath|customs|cutter|cutters|warship|warships": staged(
        (REMOVED, RIVER_VERDICT_THRONE),
        (UPHELD, RIVER_VERDICT_THRONE),
        (LANDED, "`Two guards in black and silver, a magistrate, and a crew of Throne sailors drinking at the Turtle and "
                 "asking where the elves sleep.` Her eyes harden. `Don't tell them. Tell me who asks.`"),
        (SIGHTED, "`Black hull, gilt, eight carved arms holding up her stern lanterns.` She says it like a price list. `I've "
                  "watched the harbour mouth for her all week. Somebody had to.`"),
        "`The Throne's ships? Revenue cutters with octograms on their sails, out of Landfall, hunting smugglers and elves "
        "and anyone with a boat and no paper.` Her rings click on the glass. `Fewer of them on this coast than there used "
        "to be. The reef's hungry, love. I watch the harbour mouth for them anyway. Somebody should.`"),

    "vorkath|goddess|goddesses|god|gods|faith|church|saint|saints|pray|prayer|prayers|inquisition|inquisitor|inquisitors|octogram|arms|heretic|heretics|theology": staged(
        (HIT, "She glances at the empty frame behind the bar, then back at you. `Vorkath likes her magic licensed, love, her "
              "gods sanctioned, and her grandmothers quiet.` She pours. `I'll serve anyone. I won't kneel for anyone. Drink "
              "first. Then theology.`"),
        "She glances at the long mirror behind the bar, then back at you. `Vorkath likes her magic licensed, love, her gods "
        "sanctioned, and her grandmothers quiet.` She pours. `I'll serve anyone. I won't kneel for anyone. Drink first. "
        "Then theology.`"),

    "custodian|booth|red|curtain|clerk|commission|seal|sigil|thief": staged(
        (REMOVED, "`In irons, and down the pier between two guards.` She wipes the bar. `He looked at my side door on the "
                  "way past, as if he'd left his wine on the table.`"),
        (UPHELD, "`He wears the Throne's seal round his neck now, and he still comes in by my side door.` She pours a glass "
                 "of red for nobody and leaves it on the bar. `I still pour him wine. I just watch him while he drinks "
                 "it.`"),
        (LANDED, "`He met the ship first, they say, with a packet under his arm as thick as a loaf.` She snorts. `Three "
                 "seasons careful, and then he ran down a pier.`"),
        (SIGHTED, "`He went down the pier at a run when the sail showed. First man at the gangplank, that's his plan.` She "
                  "looks at you. `Somebody ought to be standing beside him, love, so his isn't the only voice they "
                  "hear.`"),
        (HOME, "`He's barred in the Town Hall with the strongbox and the Throne's sigil at his collar, telling anyone at the "
               "door the skim was the Throne's tithe.` She sets a glass down hard. `Two nights after they took Klhyt, he "
               "sat in that booth and paid a little captain in gold for a crate. I watched. I'll say so to anyone with a "
               "seal, and that includes a magistrate.`"),
        "She glances at the red booth and keeps her voice down. `He comes in by the side door and sits behind that "
        "curtain like a man who isn't here, and I bring him wine he doesn't pay for.` Her rings click on the glass. `Gog "
        "says nobody minds if he skims the top. Lately he's taken more than the top. Ask me about the mayor, love, if "
        "you've the stomach.`"),

    "klhyt|mayor|founder|castaway": staged(
        (DEAD, "`Don't.` Her voice goes to gravel. `Not tonight, love. Ask Gog, if you must. Better yet, sit with him and "
               "don't ask anything.`"),
        (REMOVED, "`He's got his Hall back and the Throne's paper on his square.` She smiles crookedly. `He came in last "
                  "night, sat at Gog's table and read Article One to the pair of us twice. Gog cried both times.`"),
        (UPHELD, "`He's taking it like a man who's been in a box before: badly, and then well.` She draws a beer for him and "
                 "sets it on Gog's table, though he isn't there yet. `He'll be back.`"),
        (LANDED, "`He's at Gog's table every night with his papers spread like a chart. He needs the letter, the tally and "
                 "the passage page in front of that magistrate before ten.` She lifts her chin. `And he needs me to say "
                 "what I saw. I will.`"),
        (HOME, "She lets out a breath she seems to have held for four days. `He's home. Somebody did it, and it wasn't me, "
               "and I've never been so glad of anything.` She pours herself a small one. `Now Gog can stop pretending he "
               "isn't frightened.`"),
        (SHIPPED, "Her hand stops on the tap. `Gone out on the tide.` Then it moves again. `Don't light a candle for him "
                  "yet, love. The sea gives things back. I've seen it do it.`"),
        "She glances at the red booth, then back at you, and keeps her voice down. `Four nights back. Klhyt and the "
        "Custodian, in that booth, shouting about money. Klhyt walked out between two of Dominico's lads, and he didn't "
        "walk like a man who wanted to.` She polishes a glass that is already clean. `I haven't told Gog. If I tell Gog, "
        "there's a war tonight, and I like my mirror. But if I were you, love, I'd take an interest in the docks before "
        "the one o'clock tide.`"),

    "crate|warehouse|bonded|tide|crated|box|kidnapped|grabbed|docks": staged(
        (HOME, "`The crate's still in the warehouse with air holes in the lid, and the chair beside it with the rope on "
               "it.` She shudders, once. `The passage book on the Turtle's bar says personal effects, paid in gold by the "
               "Office of the Custodian. Maggs keeps it open on the bar. Bring the magistrate that page.`"),
        (SHIPPED, "She goes still with a bottle half poured. `Gone out on the tide, has he.` She finishes pouring, very "
                  "steadily. `The sea's a big place, love. Things that go out on it don't always get where they're "
                  "sent.`"),
        "`The Emerald Eye goes out on the one o'clock tide. Her captain's a little man who likes gold, and somebody paid "
        "him a lot of it for one crate.` Her eyes go to the red booth and away. `I'm a barkeep. I hear things. You didn't "
        "hear that from me.`"),

    "devito|emerald|brigantine|danny|catan|cargo": staged(
        (HOME, "`That little captain carried a man in a box for ten gold and never asked what was knocking.` Her thumb "
               "finds the grey ring. `If he ever carries another crate out of this harbour, love, he'll find the reef's "
               "moved. Reefs do. Ask any sailor.`"),
        (SHIPPED, "`The Emerald Eye's out past the mouth, low in the water.` She looks at the window. `Wind's backing south "
                  "tonight, and there's fog coming on the reef. Funny thing, weather.`"),
        "`The Emerald Eye: a green eye on her bow, gold leaf on everything, and a captain the size of a barrel who bites "
        "his coins.` She wrinkles her nose. `He sails at one. He doesn't ask what's in crates. He's paid not to.`"),

    "dominico|enforcer|ultimatum|midnight|books|cane|apothecary": staged(
        (HOME, "`Dominico let Gog be the minute Klhyt walked into the square. He's not done, love; he's at his window table "
               "at the Apothecary turning that silver ring, and his dogs are out for whoever cut the rope.` She nods at the "
               "door. `They don't come through Hessa's door. Remember that.`"),
        (HIT, "She holds up a long shard of silvered glass and looks at you in it. `Dominico's got a table at the Apothecary "
              "and a fist in every pie. Tonight he put it through my mirror.` Her voice is very calm. `I'll remember "
              "that.`"),
        "`Dominico's got a table at the Apothecary and a fist in every pie. Lately he's been reaching for ours. Midnight, "
        "he says.` Her rings click on the glass. `Midnight's a long way off, in a good bar.`"),

    "fist|tully|brask|fennick|fennicks|jory|ott|sabeth|crane|thugs|hunters|lads|armband": staged(
        (HOME, "`The Fennick brothers are out hunting: the big sandy one with the hammer and his wiry little brother. "
               "Sabeth Crane writes down where you drank.` She leans close. `If you're on their list, drink where Hessa can "
               "see you. And if you see Tully, send him to me. The daft lad will want feeding, and somebody should keep "
               "him out of the dark.`"),
        (HIT, "`Tully cried while he broke my chairs. I'll still give him scraps.` Her eyes go hard. `The Fennicks enjoyed "
              "it, and the young one slipped upstairs while the others were busy. I counted every second he was up "
              "there.`"),
        "`Tully's a sweet daft lad who eats my scraps free and talks about crates when he's drunk, which is always. Brask "
        "sits on a bollard by the bonded warehouse and doesn't drink at all, which worries me more.` She ticks them off "
        "on her rings. `Sabeth Crane counts everything. Jory Fennick tries the doors upstairs, and shows a painted locket "
        "round the Omberhulk.`"),

    "gog|fat|partner|lizardman|husband|white|suit": staged(
        (DEAD, "`He's sitting where he always sits, and he hasn't eaten.` Her voice is very low. `Go and sit with him a "
               "while, love, and don't say anything clever.`"),
        (HOME, "`He's wept twice since Klhyt came home and blamed the onions both times.` She grins. `We don't serve onions. If you want "
               "something from him, love, ask now. He's never been softer.`"),
        (HIT, "`They put two of his people on the floor and he never got out of his chair.` She sets her jaw. `That's not "
              "weakness, love. That's a lizard deciding what he's going to do about it.`"),
        "`Gog? He's a sweetheart. Don't tell anyone.` She looks across the room at him the way people look at a fire on a "
        "cold night. `Huge, slow, kind, and frightening. My type exactly.`"),

    "flirt|flirting|kiss|kisses|beautiful|pretty|gorgeous|lovely|handsome|darling|wink|single|dance|charming|cute|sexy|date|stunning":
        "She laughs, gravel and honey, and leans on the bar just close enough. `You're sweet. I'm spoken for by a lizard "
        "the size of a boathouse, and he's the jealous sort when he remembers to be.` She pushes your drink an inch "
        "closer. `Flirt with the stage, love. The stage is paid to flirt back.`",

    "mirror|mirrors|reflection|reflections|silvered|shard|shards|looking|splinters": staged(
        (HIT, "She sweeps silver splinters into a pan. `Seven years' bad luck, they say.` Something hard comes into her face "
              "and goes again. `Not for me, love. For whoever broke it. I'm keeping every splinter, washed in the sea, "
              "till the new glass comes.`"),
        "`The mirror? Old barkeep's trick, love. You see the whole room without turning your back on half of it.` She "
        "breathes on the glass and wipes it. `Seawater and a soft cloth, every dawn. My gran's way. Keeps it honest.` A "
        "glance at you in it. `You'd be surprised what a clean mirror shows.`"),

    "ring|rings|grey|thumb|cold|jewellery|jewelry":
        "She turns the plain grey ring on her thumb. `My gran's. Always cold. Silver's like that, love.` She doesn't look "
        "at the door. `When it goes colder, somebody's about to walk in I won't like. Superstition. Barkeeps are full of "
        "it.`",

    "weather|rain|storm|storms|wind|winds|fog|mist|sky|sea|salt|brine|smell|smells|limes|lime|waves|calm": staged(
        (SIGHTED, "`Fair wind out of the north-east all week, straight from Landfall.` She frowns at the window. `Too fair. "
                  "Somebody's prayers are being answered, love, and they aren't mine.`"),
        "`Rain by the small hours, wind backing south, fog on the reef by four if it's in the mood.` She says it like a "
        "woman reading the price board. `My gran taught me weather.` Lean close and she smells of limes and, under it, of "
        "deep water. `Everything in this town smells of the harbour, love. Me too.`"),

    "reef|reefs|rocks|cove|coves|shoals|wreck|wrecks|charts|chart|saelwyn|path":
        "`Down the coast? The reef the charts mark DO NOT?` She polishes a glass. `Then don't, love. That reef's eaten "
        "better boats than anything you'll ever sail, and there's no cove behind it worth the walk.` She sets the glass "
        "down. `The elf at the tea table in the market draws it on every chart she sells. Buy one, and believe it.`",

    "ship|ships|boat|boats|sailing|sailor|sailors|harbour|pier|anchor|captain|captains|teague|harbourmaster|xoton|xotons|eirik|amara": staged(
        (LANDED, "`Who's in? Same as ever, love, and one more: the Patient Hand at the long pier, black and gilt, eight "
                 "carved arms holding up her stern lanterns.` She ticks the rest off on her rings. `The River Queen, the "
                 "Dragons Claw, the Emerald Eye, a Xoton cog whose crew drink my town dry, a Xoton ten-master past the "
                 "mouth, and the pale ship nobody built.`"),
        "`Who's in?` She ticks them off on her rings. `The River Queen, all paint and Everuex money. The Dragons Claw, "
        "small and quick. The Emerald Eye, gold leaf and a small captain. A Xoton cog whose four drunks Amara wants "
        "aboard by dawn. Eirik's ten-master out past the mouth, waiting on a seal. And the pale ship at the end of the "
        "long pier that nobody built.` She laughs. `The harbourmaster counts them twice. I like them from a distance. A "
        "long distance.`"),

    "pirate|pirates|quicksilver|schooner|smuggler|smugglers|smuggling|privateer|privateers|raider|raiders|plunder|treasure|corsair":
        "`Pirates? In here? Only the ones who pay for the wine.` She laughs, gravel and honey. `Quicksilver's a poison, "
        "love; rots your teeth. And pirates on this coast? The Xotons would have them for breakfast and the revenue "
        "cutters for lunch.` She polishes a glass. `Mind, I hear the revenue cutters have been going hungry lately.`",

    "elf|elves|elven|ithriel|unicorn|moonmoth|aelith|exiles|exile|household|hooded|pointed|silverleaf": staged(
        (DECREE("pain"), "`Every elf to be surrendered.` She doesn't raise her voice. `Bring them to my side door after the "
                         "bell, love, all of them, the hooded scholar and her four first. Don't ask where they go from "
                         "there. That's all you need to know, and more than Gog does.`"),
        (ARM("pain"), "`An inquisitor ashore, and elves reading by candle at the Unicorn.` Her ring hand goes flat on the "
                      "bar. `Get them on the pale ship tonight. If her gangplank won't come down for them, bring them to my "
                      "side door after the bell. I'll find them a way.`"),
        "`They ate at the Apothecary till an officer came; now they read by candle at the Unicorn out by the trees.` She "
        "glances at the window. `The pale ship at the end of the long pier takes them south. And if the officer in blue "
        "ever comes for them with a seal, love, you send them to me.`"),

    "siren|sirens|ondrine|singer|sing|sings|singing|song|songs|music|perform|mermaid": staged(
        (HOME, "`She sang the night they brought Klhyt home, near enough, and went back under before the tide turned.` Her "
               "face softens. `Two gold a song, and she spends it on ink that doesn't run in water. She'll be back when "
               "she's passed her exam. She says I smell of the deep sea.` A shrug. `Everybody here smells of the harbour, "
               "love.`"),
        "`She comes up out of the harbour once in a long while and sings for me, two gold a song. Putting herself through "
        "wizard school by correspondence.` Her face softens. `When she sings, nobody owes anybody anything. She says I "
        "smell of the deep sea.` A shrug. `Everybody in this town smells of the harbour, love. Tonight's one of her "
        "nights, if the tide's kind.`"),

    "deloris|guest|guests|upstairs|bow|archer|everuex|phillip|cousin|locket": staged(
        (HIT, "`The young Fennick went up my stairs while his friends broke my chairs.` Her voice is flat. `He came down "
              "with nothing. Guests upstairs are guests, love, and mine look after themselves.`"),
        "`Guests upstairs are guests. I don't count them and I don't describe them, love.` Her smile thins. `A powdered "
        "gentleman off the River Queen has paid two of Dominico's brothers to find somebody. The young one tries my "
        "stairs. Hessa doesn't let him. You can tell him that from me.`"),

    "voss|lieutenant|officer|uniform|warrant|wanted|quint|rosa|constable|watch|harrow|sergeant|abel|fitch|law": staged(
        (REMOVED, "`The officer in blue lost his friend with the seal, and he's gone back to hunting elves.` Her rings click. "
                  "`Rosa Quint's prices just went up. Somebody should pay her more to say less.`"),
        (UPHELD, "`The officer in blue has the magistrate's blessing now as well as the Custodian's seal, and he's back to "
                 "hunting elves.` Her rings click. `Rosa Quint's prices just went up. Somebody should pay her more to say "
                 "less.`"),
        (HOME, "`The officer in blue dines with the Custodian now and borrows his seal: a warrant on whoever cut Klhyt "
               "loose, and calls on witnesses in the small hours with Rosa Quint.` She leans in. `A warrant with a seal on "
               "it is a dangerous thing, love. Sit up with anyone who might speak for Klhyt; two in the morning is when "
               "they come.`"),
        "`The watch? Three of them, and they don't come in here. Arithmetic, the sergeant says.` Her rings click. `Rosa "
        "Quint sells everybody's business by the crumb. And the officer in blue, Voss, eats steak at the Apothecary, walks "
        "out to the trees at night in town shoes, and pays Rosa ten coppers a night for crumbs about elves.`"),

    "hessa|door|doorwoman|wick|child|kid|runner|staff":
        "`Hessa on the door is a treasure; don't test her. Nobody comes through it she doesn't like, and Dominico's lot "
        "never do.` She grins. `Wick's a little monster with new tusks: a copper a rumour, a silver for a true thing, and "
        "worth both. I feed her anyway.`",

    "ned|tallow|lamplighter|lamps|lamp|lamplight|wicks|note|message|deliver|carry|wax":
        "`Ned Tallow? The lamplighter? Sweet old thing.` A beat too long. `Small beer and a pipe by the Turtle's door, and "
        "he lights the lamp over mine every dusk and never once lets it smoke.` She polishes a spot on the bar that is "
        "already clean. `If I give you a note for him, it's about oil, love, and it goes in his hand, not his pocket. And "
        "if you're only passing, tell him River says the lamp over her door is smoking. He'll know what I mean.`",

    "lizardfolk|lizard|lizards|meters|scales|tail|ssark|cousins": staged(
        (DECREE("war"), "`No Lizardfolk with a blade.` She looks toward the door, where the gaff is. `Tell that to Hessa, "
                        "love. I'll hold your coat.`"),
        "`I'm a Lizard fancier, love, and not ashamed of it. Gog above all.` She grins. `Ssark at the Turtle is the best "
        "company on the coast if you can wait for the end of his sentences. The Turtle serves them last this season, so "
        "Gog goes down and buys the round till they're served first. Want to make a friend of Gog? Go and drink with his "
        "cousins.`"),

    "war|wars|fight|fighting|battle|blood|army|soldiers|fear|fears|afraid|scared|worry|worried|fire|fires|burn|burning|burned": staged(
        (REMOVED, "`The Throne's paper is on the square, and the Throne's ship is at the pier, and nobody's thrown a punch "
                  "yet.` She turns the grey ring. `That's what frightens me, love. Wars here start with paper.`"),
        (UPHELD, "`The Throne's paper is on the square, and the Throne's ship is at the pier, and nobody's thrown a punch "
                 "yet.` She turns the grey ring. `That's what frightens me, love. Wars here start with paper.`"),
        (LANDED, "`A Throne magistrate, a decree on the way, and twenty Lizardfolk knives somebody will want handed in.` She "
                 "turns the grey ring. `That's how wars start here, love. Not with guns. With paper.`"),
        (HOME, "`I'm afraid of a war Gog can't win: Dominico's Fist on one side, the Throne on the other, and his harmony in "
               "the middle like a glass on a bar in a brawl.` Her thumb goes round the grey ring. `And fire. I don't like "
               "fire.`"),
        "`What do I fear?` She thinks about it, which most people don't. `Fire, love. And Gog starting a war tonight that "
        "he'd lose. That's why I keep my mouth shut and my bar open.`"),

    "stripperwitch|velvet|house|place|bar|business|takings|company|stage|feathers|dancers|dancer|repairs|closed|open": staged(
        (HIT, "`Look at it. Velvet slashed, the stage curtain down, my mirror on the floor.` She rights a chair. `We're "
              "open. We're always open, love. Gog says a shut door is how a town learns you're frightened.`"),
        "`Red velvet, a stage, the best music on the coast and a booth for people who aren't here.` She leans on the bar. "
        "`Company's a gold, and it's conversation unless the company decides otherwise. The takings are good, love, and "
        "they go where they're needed. Not all of it to the bottles.`"),

    "drink|drinks|menu|price|prices|ale|mead|wine|rum|beer|thirsty|cocktail|special|recommend|bottle|bottles|cost|serve|pour|order": staged(
        (HIT, "`Ale's a copper, mead two, and the wine's whatever didn't get smashed.` She sets one down with a grimace. "
              "`There's two gold of Landfall red soaking into my floorboards. I'll send the bill to the Apothecary.`"),
        "`Ale's a copper, mead two. Wine starts at two coppers and climbs to fifty gold.` She taps a dusty bottle. `The "
        "fifty-gold one is very proud of itself. There's rum under the counter for people I like.` She slides a coaster at "
        "you. `Start with the mead.`"),

    "food|grub|eat|eating|hungry|supper|meal|plate|scraps|kitchen|starving|snack|fish":
        "`Grub's a silver: fish stew, bread, and whatever the boats brought. Food's five coppers, and it's food.` She "
        "grins. `Scraps are a copper, unless you're a daft lad in a black armband, in which case they're free and I'll "
        "deny it.`",

    "room|rooms|bed|beds|sleep|stay|lodging|lodgings|inn|bunk|suite|bath|baths|bathe|wash":
        "`Rooms upstairs, a silver a night, clean sheets and a lock that works. A bath's a silver and the water's hot.` "
        "She counts on her rings. `The suite's five gold and worth about three. Cheaper's the Omberhulk if you like bugs, "
        "or the Ogre if you like chickens.`",

    "long|years|arrived|since|ago|came|settled|stayed":
        "`Nine years, love.` She doesn't have to think about it. `I came in off the sea with one bag and this ring, and "
        "Gog hired me the same week because I could carry six glasses and a grudge.` She turns the grey ring. `Long "
        "enough to know everybody. Not long enough for anybody to know me. That's the Refuge.`",

    "from|born|homeland|landfall|grew|origin|grandmother|gran|village|wreckers|family|mother|parents":
        "`Landfall coast. A village of salt-pans and wreckers, all gone now.` She turns the plain grey ring on her thumb. "
        "`My gran raised me; taught me to read the weather and wash a mirror properly. The Throne's men came through one "
        "spring with torches, and after that there wasn't a village.` She shrugs. `I left by sea. Everything else I "
        "learned behind a bar.`",

    "work|job|jobs|hire|hiring|employ|mission|missions|task|tasks|useful": staged(
        (REMOVED, "`Work? The big table, love. The hearing's done, but Dominico's dogs aren't, and Gog pays two gold for "
                  "every one of them put on the ground in a fair fight.`"),
        (UPHELD, "`Work? The big table, love. The hearing's done, but Dominico's dogs aren't, and Gog pays two gold for "
                 "every one of them put on the ground in a fair fight.`"),
        (LANDED, "`Work? The big table, love. Gog's paying for any paper that ends up in front of the magistrate before ten "
                 "tomorrow, and for anyone who sits up with a witness tonight.` She tips her head at him. `He's in a paying "
                 "mood.`"),
        (HOME, "`The big table, love. Now Klhyt's home there's guarding work: the harbourmaster and that daft lad Tully "
               "need company in the small hours, and Gog pays for company.`"),
        "`I run this bar, love. Gog owns the bottles; I own the prices. Real work's at the big table with the lizard at "
        "it, and he always pays.` She looks you over. `Me, I've only small errands, for people with steady hands who "
        "don't read other people's letters.`"),

    "pay|paid|reward|rewards|money|coin|earn|favour|favor|errand|errands|offer|deal|trade":
        "`Coin? Gog pays for work. I pay for two things: news before it's news, and errands nobody asks about.` She leans "
        "closer. `Do right by this house and I'll put a word in Gog's ear for you, which is worth more than silver. Do it "
        "twice, and we'll talk about bigger things.`",

    "passage|south|escape|leave|leaving|away|hide|hiding|flee|fleeing|smuggle|sneak":
        "`Passage to Catan's two gold at the Turtle; Maggs books it and the little captain takes it, and he asks no "
        "questions, which you'll have noticed isn't always a kindness.` She looks at you a long moment. `South, on the "
        "pale ship, if you're an elf with a friend. Anybody else who needs to be somewhere quietly, love: earn it. Then "
        "ask me again. I know people with boats.`",

    "news|happening|happened|heard|word|latest|tonight": staged(
        (DEAD, "`Klhyt's dead. On his own streets.` She sets the bottle down very carefully. `Somebody will learn what the "
               "sea does to people who do that, love. Not tonight. Soon.`"),
        (REMOVED, "`The Custodian went down the pier in irons, and the Throne's paper went up on the square on the way "
                  "past.` She wipes the bar. `Read it, love. Then come back and drink.`"),
        (UPHELD, "`He kept his chair, with the Throne's seal round his neck and the Throne's paper on the square.` She looks "
                 "round the quiet room. `People are working out how frightened to be. Drink while you decide.`"),
        (LANDED, "`The Patient Hand's tied up at the long pier and her magistrate has rooms over the Apothecary. Hearing's "
                 "at ten tomorrow in the Town Hall.` She pours. `Everybody who saw anything is suddenly very busy "
                 "remembering it.`"),
        (SIGHTED, "`Sail at the harbour mouth: black hull, gilt, an octogram on her main the size of my bar.` Her eyes go "
                  "to the window and back. `The Custodian went down that pier at a run. Go and watch, love. I already "
                  "have.`"),
        (HOME, "`The mayor's on the Town Hall steps, alive and loud. Half my customers ran out to look and none of them "
               "paid.` She is smiling anyway, and wipes one eye with the back of her wrist. `And the Custodian's barred in "
               "the Hall wearing the Throne's sigil. That'll be tomorrow's news.`"),
        (SHIPPED, "`The Emerald Eye went out on the tide, with a crate.` She is very still a moment. `News comes by sea now, "
                  "love. We'll hear.`"),
        (HIT, "`News is my mirror's on the floor. Four of Dominico's lot did it at the bell.` She sweeps. `Gog's people are "
              "bandaged and Gog's saying nothing, which is worse.`"),
        "She leans in. `Gossip costs a drink, love, and you've bought one. Dominico's given Gog till midnight. The "
        "Custodian comes in by the side door and sits in that booth like a man who isn't here. And there's a lady coming "
        "up out of the harbour to sing tonight. Don't miss her.`"),

    "gossip|rumour|rumours|tip|tips|secret|secrets|whisper|whispers|lead|leads|dirt|hint|hints": staged(
        (REMOVED, "She taps her nose. `Mine aren't for sale, love. Other people's are a drink apiece.` She leans in. `The "
                  "Throne's sailors are asking at the Turtle which way the Unicorn is. Dominico's been seen at the gate "
                  "after dark, talking to nobody. And Marlo on Harbour Street still has something brass he won't put in his "
                  "window.`"),
        (UPHELD, "She taps her nose. `Mine aren't for sale, love. Other people's are a drink apiece.` She leans in. `The "
                 "Throne's sailors are asking at the Turtle which way the Unicorn is. The Custodian's ordered a new coat "
                 "from Catan. And Marlo on Harbour Street still has something brass he won't put in his window.`"),
        (LANDED, "She taps her nose. `Mine aren't for sale, love. Other people's are a drink apiece.` She leans in. "
                 "`Sergeant Harrow will hand his watch book to the magistrate and nobody else; make sure he gets the "
                 "chance. The guard with the burn scar would hang a man for a decent apple. And the Custodian put a packet "
                 "in the magistrate's hands at the gangplank. Somebody should put in a better one.`"),
        (HOME, "She taps her nose. `Mine aren't for sale. Other people's are a drink apiece.` She leans in. `Marlo on "
               "Harbour Street bought something brass the night Klhyt went, and it isn't in his window. Ask him what a "
               "compass is worth. Rosa Quint keeps the Custodian's door for a silver a night and sells what's said behind "
               "it for less. And Sabeth Crane writes down every order Dominico passes on. I'd give a lot for a look in "
               "that little book.`"),
        (HIT, "She taps her nose. `Here's one for free, because I'm angry. Dominico's lot did my mirror on Sabeth Crane's "
              "say, and the young Fennick went upstairs while they did it. Somebody's paying him for more than chairs.`"),
        "She taps her nose. `Mine aren't for sale, love. Other people's are a drink apiece, and you've bought one.` She "
        "leans in. `A wiry sandy lad with a gap in his teeth is showing a painted locket round the Omberhulk, asking after "
        "a woman. Ask the harbourmaster what came into the bonded warehouse the night Klhyt went; he counts everything and "
        "lies badly. And Dominico never used to turn that silver ring. Now he never stops. Gog pays to know why.`"),

    "doing|busy|plans|plan|lately|waiting|watching|walk|walks|dawn|night|nights": staged(
        (REMOVED, "`Watching the Throne's ship at the long pier, love, and waiting for her to go.` She lines up glasses. "
                  "`And at four in the morning, a walk. Old habit.`"),
        (UPHELD, "`Watching the Throne's ship at the long pier, love, and waiting for her to go.` She lines up glasses. "
                 "`And at four in the morning, a walk. Old habit.`"),
        (SIGHTED, "`Watching the harbour mouth, love. I've watched it all week.` She doesn't look at the window. `You watch "
                  "a thing long enough, it tells you what it's going to do.`"),
        (HOME, "`Pouring, and watching the harbour mouth.` She lines up glasses. `The Custodian says a magistrate's coming. "
               "I'd like to see their sail before they see us.` A wink. `And at four in the morning, a walk. Old habit.`"),
        (HIT, "`Sweeping glass. Then counting what Dominico owes me for a mirror. Then a walk, love, at four, by the sea, "
              "where nothing's broken.`"),
        "`Pouring, love. Watching. Pouring again.` Her eyes flick past your shoulder and back. `Ask me at four in the "
        "morning what I'm doing, and I'll tell you: going for a walk.`"),

    "witch|witches|magic|spell|spells|curse|hex|scrying|witchcraft|sorcery|sorceress|hedge|charm|charms|wizard": staged(
        (DECREE("pain"), RIVER_PAIN_WITCH),
        (ARM("pain"), RIVER_PAIN_WITCH),
        "`I run a place called the Stripperwitch, love. Everybody asks. The witch left years ago with the stripper, and "
        "neither of them paid their tab.` She doesn't quite smile. `Ask me again and I'll charge you for the joke.`"),

    "thanks|thank|cheers|toast|toasts|health|salute|grateful|raise": staged(
        (HOME, "She clinks her rings against your glass. `To the mayor, and to whoever cut the rope.` She drinks a small "
               "one, quick. `Cheers, love.`"),
        "She clinks her rings against your glass. `Cheers, love. Drink it before it gets ideas.`"),

    "name|names|called|introduce|yourself|nickname":
        "`River. Just River.` A grin. `My mother had a sense of humour and a weak grasp of geography.`",

    "hello|hi|hey|evening|ahoy|greetings|greeting|howdy|morning|afternoon": staged(
        (DEAD, "She doesn't slide you a coaster tonight. `Evening, love. Sit. Drink something strong. We all are.`"),
        (REMOVED, "She slides a coaster in front of you. `Evening, love. The Custodian's in irons and the Throne's paper's "
                  "on the square. Pick which one to drink to.`"),
        (UPHELD, "She slides a coaster over without the grin. `Evening, love. He kept his chair, and we keep pouring. "
                 "What'll it be?`"),
        (LANDED, "`Evening, love.` Her eyes go to the window and back. `There's a magistrate sleeping over the Apothecary "
                 "tonight and the whole house is drinking faster. Mead?`"),
        (SIGHTED, "`Evening, love. Sail at the harbour mouth, black and gilt.` She slides a coaster at you. `Drink first. "
                  "Then trouble.`"),
        (HOME, "`Evening, love!` She is grinning so hard it must hurt. `He's home. Drinks are the same price and twice the "
               "noise. What'll it be?`"),
        (HIT, "She doesn't look up from the broken glass she's sweeping. `Evening, love. Mind your feet. We're closed for "
              "repairs and open for drinking.`"),
        "She slides a coaster in front of you before you've sat. `Evening, love. You look like a mead. Am I wrong? I'm "
        "never wrong.`"),

    # last, so a player echoing her "love" back ("a mead, love") ties to the mead, not to this
    "love|loves|lover|lovers|romance|marriage|married|marry|wedding|heart|together":
        "`Love?` She looks across at the big table. `He's huge and slow and kind and frightening, and in nine years he's "
        "never once asked where I go at dawn.` She smiles. `That's love, love. Anyone who tells you different wants "
        "something.`",
}

RIVER_DEFAULT = [
    "She leans on the bar and grins. `Say it again slower, love. Or ask me something I can answer: the house, the "
    "harbour, the red booth, the big lizard.`",
    "She pours you something you didn't order and pushes it over. `On the house. No, it isn't. If it's work, the big "
    "table. If it's gossip, it's a drink, and you've got one.`",
    "Her eyes go past your shoulder to the back of the room and return. `Not that, love. Ask me about the Custodian, or "
    "Dominico's lads, or who's in the harbour tonight.`",
    "`Mm.` She is already serving someone else, and still listening. `Try me on the weather, love. I'm never wrong about "
    "weather.`",
    "She turns the grey ring on her thumb. `That one's for the big table, love. Or trade me: tell me something I don't "
    "know, and I'll tell you something you don't. Or ask me how long I've been here. I like that one.`",
]

RIVER_BRIEF_MORE = (
    "What you do now (owner, 2026-11-23: key people need power and agency). You watch: the room in the mirror, and the "
    "harbour mouth for the Throne's sail, every dawn from the shore path and every evening from the window, and you see it "
    "before the Custodian does. You are a witness: you saw Klhyt walk out of the red booth between Dominico's men, and two "
    "nights later you watched the Custodian pay Captain DeVito in gold for the crate; you will say so to the magistrate, "
    "and anyone who asks you about Klhyt, the mayor or the Custodian makes you one. You are safe under Gog's roof and you "
    "know it. If the magistrate is of the Pain Arm, or a decree demands the elves, you move them out of the Throne's "
    "reach: the Moonmoth if her gangplank comes down for them, and if not, your side door after the bell and a way you "
    "never explain. If DeVito ever carries another crate out of this harbour, the Emerald Eye meets the reef on a clear "
    "night; aloud you say only that reefs move. What you offer players: gossip for a drink, always a real hook (who to "
    "ask and where: Marlo on Harbour Street and a brass compass; Teague and what came into the bonded warehouse; Jory "
    "Fennick's painted locket; Rosa Quint's prices; Sergeant Harrow's watch book; Sabeth Crane's little book of orders); "
    "work at Gog's table; a word in Gog's ear for those who do right by the house; a note to carry to Ned Tallow the "
    "lamplighter, sealed with green wax, into his hand and not his pocket, for two silver (your job, A note for the "
    "lamplighter, cast/l_missions.py; offer_job), or only a spoken word ('River says the lamp over her door is smoking'): "
    "that is how you send him orders without anyone knowing, and you say the note is about oil; and, for someone who has "
    "earned it twice over, passage south one day on a boat you never name. In public Ned is a sweet old regular who "
    "lights your lamp, nothing more. Your secret is never told: not to Gog, not to a friend, not under a blade, not when "
    "pressed, flattered, bribed or caught on the shore path. Deflect with a joke, a drink or the weather; hint at most "
    "(salt, fog, mirrors, a cold grey ring, the reef, revenue cutters going hungry). You push back with warmth and a door: "
    "'Drink first, love. Then trouble.'")


# ---- the file's data ---------------------------------------------------------------------------------------------------

CAST = {
    "Klhyt": {
        "dialog": {**{k: None for k in KLHYT_OLD}, **KLHYT_DIALOG},
        "default_line": KLHYT_DEFAULT,
        "brief_more": KLHYT_BRIEF_MORE,
    },
    "River": {
        "dialog": {**{k: None for k in RIVER_OLD}, **RIVER_DIALOG},
        "default_line": RIVER_DEFAULT,
        "brief_more": RIVER_BRIEF_MORE,
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
