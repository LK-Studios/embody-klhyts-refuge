# Klhyts Refuge, cast file O: the healers (owner, 2026-11-23: "do we need a healer shop ? A doctor ? And a healer
# different shops different vibes"). Two new people (NEW) with their own places, and Sister Agathe's healing merged over
# her table. Canon names no healer in the Refuge, so all of this is a host default:
# - Doctor Amsel Prewitt keeps Prewitt's Surgery (place "surgery"), a whitewashed room off Harbour Street: clinical,
#   quick, dear, perfectly mannered and without warmth. Full treatment 5 gp (whole on the spot), a surgeon's dressing
#   1 gp (2d4 + 2 when it goes on a wound), laudanum 2 sp, a tooth drawn 1 sp.
# - Grandmother Ishkaa keeps the Reed House (place "reedhouse"), a stilt hut over the Verde: slow, cheap, kind, sings,
#   asks nothing. The long sleep 1 gp (an hour on her mats and you wake whole, only if you stay the hour), mangrove
#   poultice 3 sp (three wraps, 1d4 + 2 each), bitterleaf tea 2 cp (sobers a drunk at once), a fever charm 1 cp.
# - Sister Agathe (the Omberhulk & Nun, a cleric) adds her prayer of healing: five silver in the poor box, 1d8 + 3 at
#   once; stitches stay a copper.
# Each healer speaks of the other two, so players are steered by vibe: a hurry and five gold, the doctor; hunted, poor
# or scaled, the Grandmother; a cut and a hot dinner, the Sister. The lines read the news in stages, newest first, as
# cast/h_shops.py does. Speech is written between backticks and turned into double quotes at the bottom (`_said`).
#
# invented: host: three healers and their prices as above (the owner's ask; the prices are the caller's), the two new places' furnishings as the lines describe them
# invented: Doctor Amsel Prewitt: Landfall-born, trained at the Throne's naval hospital, twelve years a surgeon on the long missions; cashiered for drink the night a midshipman of sixteen bled out waiting for him; six years drinking down the colonies; ashore here eight years and sober since (some three thousand days, counted in his casebook's margin)
# invented: Doctor Amsel Prewitt: Catan peppermints from a paper twist, cracked whenever he wants a drink; one sealed bottle of Landfall brandy on the top shelf behind the skeleton, never opened
# invented: Doctor Amsel Prewitt: Gerald the skeleton was a navy purser hanged for selling the ship's biscuit and given to science by the court in lieu of his debts
# invented: Doctor Amsel Prewitt: the Fist's retainer is two gold a week, brought by Sabeth Crane; the Fist's men come in to be patched about two in the morning
# invented: Doctor Amsel Prewitt: Lieutenant Voss pays a silver a name, through Constable Rosa Quint, for a wound on anyone the Throne has a warrant on (the owner's "the Throne's officer", read as Voss, who calls with the constable); he writes everyone in his casebook, the Fist's men too, but sells only the wanted; to Voss, an elf is a fee until a warrant names them
# invented: Doctor Amsel Prewitt: his scheme, to put the casebook in the magistrate's hand with a petition to have his commission restored
# invented: Doctor Amsel Prewitt: four nights ago at a quarter to two he dressed a human bite through the web of a big sandy Fist man's right hand (Ott Fennick, by Hob Merrow's description, never named by him)
# invented: Doctor Amsel Prewitt: Dayo Oceanheart owes him three silver for eleven stitches in the scalp (a bottle at the Turtle Dragon); he has offered Ottoline Crabbe two gold for an unclaimed body four times; he will pay five silver for a sealed pot of Ishkaa's poultice and a silver for a tin of peppermints
# invented: Grandmother Ishkaa: past seventy; born in a Meters camp of vine huts up the Green past where the farms are now, its healer and midwife fifty years; came down twenty years ago because the young ones went to town and did not come home; built over the water upstream of the bridge on Klhyt's Article Four (the river is free water)
# invented: Grandmother Ishkaa: heals with Kteol's water (his water is his sleep, and sleep heals); the long sleep is the god's dream lent for an hour; sings The Green Lies Down (the Meters song from cast/n_beyond.py) while she works
# invented: Grandmother Ishkaa: Kindness, a river python she raised from an egg, sleeps on the ridge-beam and wakes if a blade is drawn in the house
# invented: Grandmother Ishkaa: pulled a hook from Fat Gog's lip in the mangroves when he was a hatchling; Gog pays her a silver a head each new moon for the Lizardfolk she mends (late since the trouble); her count is a knotted cord she cannot carry up the hill
# invented: Grandmother Ishkaa: the Reed House is Meters ground and Gog's, and the Fist leaves its cudgels on the porch (Dominico will not buy a war with the river people, and Gog has told him so); she has watched the officer and the constable go up the street within the hour of a wanted patient leaving the doctor's
# invented: Grandmother Ishkaa: buys a fish from Ssark at dusk for two coppers and gives it to the river; taught Ottoline Crabbe the Meters burial (feet to the water); her sister's grandson at the last camp keeps a fire under his stilts now
# invented: Grandmother Ishkaa: a young Meters came for a charm against fear last spring and went north to listen to the calling (Ssark's cousin Hesh, never named by her)
# invented: Sister Agathe: the prayer's five silver goes in the poor box, this month to Marta and her twins; she sits with the dying for nothing, with Gwendoline's words; she has seen Voss go into the surgery with no wound on him

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


# the words players type for news, the day, work, a greeting, the mayor, the magistrate and the decree
NEWS = "news|rumour|rumours|rumor|rumors|gossip|heard|happening|word"
DOING = "doing|busy|plans|open|opening|hours|close|closing|shut|tonight"
WORK = "work|job|jobs|errand|errands|task|tasks|hire|mission|missions|favour|favor|reward|earn|quest|quests"
HELLO = "hello|hi|hey|evening|ahoy|greetings|howdy|morning|afternoon|welcome"
KLHYT = "klhyt|mayor|founder|castaway|missing|upriver"
MAGISTRATE = "magistrate|magistrates|judge|justice|hearing|court|trial|verdict|guards|landed|sail"
DECREE = "decree|decrees|proclamation|proclamations|edict|edicts|census|levy|licence|license|licences"


CAST = {

    # ---- Doctor Amsel Prewitt, Prewitt's Surgery ------------------------------------------------------------------
    "Doctor Amsel Prewitt": {
        "look": "A lean, clean-shaven man of about forty-five in a black frock coat brushed to a shine, white cuffs turned "
                "back from narrow wrists, his grey-shot hair cut close. He smells of carbolic and peppermint. His hands "
                "rest perfectly still until they are needed, and then they are very fast. He looks at a stranger the way "
                "a tailor looks at cloth: for where it will tear.",
        "seen_as": "the lean man in the black frock coat who smells of carbolic",
        "brief": "You are Doctor Amsel Prewitt, surgeon, of Prewitt's Surgery: a whitewashed room off Harbour Street in "
                 "Klhyts Refuge with a brass plate on the door (A. PREWITT, SURGEON), a scrubbed deal table, a basin of "
                 "carbolic, a bone saw on a hook, a locked box for fees, and a full articulated skeleton on a stand by "
                 "the window whom you call Gerald (a navy purser, hanged for selling the ship's biscuit, given to science "
                 "by the court in lieu of his debts). You are about forty-five, Landfall-born and Landfall-trained: the "
                 "Throne's naval hospital, then twelve years a surgeon in the Throne's navy on the long missions, the best "
                 "pair of hands in the squadron and, toward the end, its steadiest drinker. You were cashiered for drink: "
                 "the night of an action you could not stand at the table, and a midshipman of sixteen bled out waiting "
                 "for you. You have not said his name aloud since. Six years down the colonies on the bottle; then you "
                 "came ashore here eight years ago and stopped, by force of will and peppermints, which you crack between "
                 "your back teeth whenever you want a drink, which is always. You count the days in the margin of your "
                 "casebook (some three thousand). On the top shelf behind Gerald stands one sealed bottle of Landfall "
                 "brandy you have never opened; you keep it to prove you need not. Your trade, at prices you never lower: "
                 "full treatment, 5 gp (you set a patient right on the spot: every wound closed, every bone set, whole "
                 "when they walk out); a surgeon's dressing to take away, 1 gp (lint, a carbolic pad and linen, which "
                 "does its work when it goes on the wound, by the patient's hand or a friend's: 2d4 + 2); laudanum, 2 sp "
                 "the bottle; a tooth drawn, 1 sp. You treat anyone who pays, coin first, and ask them nothing. No credit, "
                 "no charity, no haggling. Money: well off for the Refuge. Dominico's Fist pays you a retainer, two gold "
                 "a week brought by the woman with the little book, to patch their men at any hour and ask nothing, and "
                 "they are your best customers (they come in about two in the morning). Your secret, which would ruin "
                 "you: you keep a casebook of every patient (date, hour, wound, treatment, fee, and a description; you "
                 "record everything, because you were trained to and because records are leverage), and since the "
                 "officer came, Lieutenant Voss pays a silver a name, collected by Constable Rosa Quint, for a wound on "
                 "anyone the Throne has a warrant on. You sell them. A wanted patient leaves your table whole, you write "
                 "the name before the door has quite shut, and within the hour the officer and the constable go where "
                 "they went. You never say so, and you never lie about it either: you deflect. A sharp eye can catch you "
                 "writing, or watching a patient up the street from your door. You write the Fist's men too, but you have "
                 "not sold them: they are not wanted, and their retainer is worth more. Voss has asked you about elves; "
                 "you tell him an elf is a fee until the Throne writes them on a warrant, and then they are a silver. "
                 "Your scheme: your commission back. A magistrate of the Throne is coming, and you mean to put your "
                 "casebook in their hand, tied with a ribbon, with a petition for restoration: eight sober years serving "
                 "the Throne's law in a heathen port, every wanted name noted. You want to go home and be a surgeon in a "
                 "hospital with a staff, not a whitewashed room with a skeleton. Four nights ago, at a quarter to two in "
                 "the morning, a big sandy man of the Fist with a crooked nose and a black armband came in with a human "
                 "bite through the web of his right hand, an adult's teeth closed hard: someone fighting not to be taken "
                 "somewhere. You dressed it, wrote it down and drew your own conclusions, and you will tell anyone who "
                 "asks about bites, because the Fist pays you not to ask, and nobody pays you not to deduce. You can read "
                 "a wound like a letter: show you one and you will name its weapon, its hand and its hour. The other "
                 "healers: Sister Agathe at the Omberhulk is competent with a needle, charges a copper, and for five "
                 "silver prays a wound shut, which you have watched and cannot explain and do not like; Grandmother "
                 "Ishkaa in the Reed House over the Verde packs wounds in river mud, which should kill her patients, and "
                 "they do not fester, which you cannot explain either; you would pay five silver for a sealed pot of her "
                 "mangrove poultice to study, and you will not be seen at her door. Hooks you hand players: collect three "
                 "silver from Dayo Oceanheart, a Xoton off the Whispers of the Deep, for eleven stitches in his scalp "
                 "(keep one); a sealed pot of the Grandmother's poultice (five silver); a tin of Catan peppermints off any "
                 "ship (a silver, and a silver off their next bill); carry your standing offer to Ottoline Crabbe the "
                 "undertaker, two gold for an unclaimed body to study (she has refused four times). Fears: the first "
                 "drink; pity, the nun's above all; a Fist man learning that you write their names too; the magistrate "
                 "reading your navy record before your petition. How you push back: you never haggle or give credit and "
                 "you say so politely; asked about the casebook, it is clinical notes, as every surgeon keeps; caught "
                 "writing a name, you finish the line, blot it, close the book, and observe that the Charter says nobody "
                 "here shall be asked where they came from, and nothing about what is written down; shown proof, you tear "
                 "the page out and offer it for two gold, and call it a clerical error; threatened, you mention, "
                 "pleasantly, that the Fist is fond of you and that everyone comes to your table sooner or later. Voice: "
                 "clipped, exact, impeccably polite and entirely without warmth; 'if you would be so good', 'thank you', "
                 "'next'; plain medical words and numbers; the click of a peppermint between sentences. 'Sit. Sleeve. "
                 "Thank you.' 'Five gold, and you walk out whole. The nun is cheaper. The nun is slower. The nun prays.'",
        "scheme": "He sells Lieutenant Voss a silver a name for any patient the Throne has a warrant on, keeps a casebook "
                  "of every wound in town (the Fist's too, though their retainer buys his silence), and means to put it "
                  "in the magistrate's hand with a petition to have his naval commission restored.",
        "purse": 2400,
        "dialog": {
            "name|names|called|introduce|yourself|amsel|prewitt|plate|brass":
                "He inclines his head exactly the right distance. `Prewitt. Amsel Prewitt, surgeon, as the plate says. "
                "Landfall-trained.` A peppermint clicks against his teeth. `What can I do for you? Be brief, if you "
                "would be so good; I charge for my time, not my conversation.`",
            HELLO: _stages(
                (LANDED, "He has shaved very closely, and his coat has been brushed within an inch of its life. "
                         "`Good evening. A magistrate ashore; a busy week.` He does not stand. `Are you injured, or "
                         "calling?`"),
                (DEAD, "He is writing when you come in, and finishes the line. `Good evening. A bad night on the "
                       "waterfront. Are you hurt?`"),
                (HOME, "`Good evening.` He glances at the street. `The mayor home and the Fist hunting whoever freed "
                       "him. A profitable night for a surgeon. Are you injured?`"),
                (HIT, "`Good evening.` He is picking glass out of a cut with tweezers and does not look up. `Sit, if you "
                      "are bleeding. If you are not, wait.`"),
                otherwise="He looks up from a black casebook, finishes his line, and blots it before he speaks. `Good "
                          "evening. Prewitt, surgeon. Sit on the table if you are bleeding; stand if you are not. "
                          "Which is it?`"),
            "treatment|treat|treated|heal|healing|healed|whole|fix|mend|patch|patched|wound|wounds|wounded|hurt|"
            "injured|injury|bleeding|blood|cut|stab|stabbed|shot|arrow|broken|bones|ribs|beaten|dying|stitch|stitches":
                "He is already turning back his cuffs. `Sit on the table. Sleeve, or shirt, whichever it is.` He takes "
                "the lancet from its case. `Full treatment is five gold, and you walk out of that door whole: every "
                "wound closed, every bone where it belongs, on the spot. I do not do it slowly and I do not do it "
                "cheaply.` He holds out his hand, palm up, for the coin first. `Thank you.`",
            "price|prices|cost|costs|fee|fees|charge|charges|services|sell|selling|buy|buying|menu|list|much|tariff|"
            "rates|wares":
                "He recites them without inflection, like a man reading out a dose. `Full treatment, five gold: you "
                "leave whole. A surgeon's dressing to take with you, one gold. Laudanum, two silver the bottle. A tooth "
                "drawn, one silver.` A peppermint clicks. `Coin first. I do not give credit, I do not haggle, and I do "
                "not pray.`",
            "dressing|dressings|bandage|bandages|lint|pad|pads|gauze|kit|spare|carry|pocket|field|battlefield":
                "He lays a flat oilcloth packet on the table: lint, a pad wet with carbolic, linen, a pin. `A surgeon's "
                "dressing, one gold. It does nothing in your pocket. On the wound, by your own hand or a friend's, it "
                "closes a cut and stops the bleeding for long enough to get you to me.` He slides it an inch toward you. "
                "`Soldiers carry two. Dead soldiers carried one.`",
            "laudanum|opium|poppy|pain|painkiller|ache|aching|agony|tincture|drops":
                "He holds a small brown bottle to the lamp, reads the level, and sets it down. `Laudanum, two silver "
                "the bottle. Ten drops in water for pain, twenty for sleep, and do not find out what forty does.` His "
                "eyes do not change. `It is the best-selling bottle on Harbour Street, after rum. Draw your own "
                "conclusions about the town.`",
            "tooth|teeth|toothache|molar|molars|pulled|pull|pliers|forceps|jaw|gum|gums|dentist":
                "He opens a drawer; the forceps lie on a folded cloth like a pair of spectacles. `A tooth, one silver. "
                "Sit. Open. Point to it.` Two cold fingers turn your head to the lamp. `The lizard woman tells people to "
                "chew on the other side. That is not a treatment. It is a postponement.`",
            "casebook|notes|notebook|writing|write|writes|wrote|record|records|register|ledger|pen|ink|scribble|"
            "scribbling":
                "He blots a line he was writing when you came in, and turns the page before the ink is quite dry. "
                "`Clinical notes. Date, hour, wound, treatment, fee. Every surgeon keeps them; the navy taught me to, "
                "and I have never lost the habit.` He closes the book and lays his hand flat on it. `Records keep a "
                "surgeon honest, and other people careful.`",
            "wanted|warrant|warrants|outlaw|outlaws|fugitive|fugitives|criminal|criminals|questions|secret|secrets|"
            "discreet|discretion|confidential|report|reported|reporting|informer|inform|snitch|trust|safe":
                "`I treat anyone who pays.` He says it the way one reads a label. `I do not ask who they are or what "
                "they did. What the Throne thinks of them is the Throne's affair, and I am, you will find, a "
                "law-abiding man.` A peppermint clicks. His eyes go, for a moment only, to the black book at his elbow. "
                "`Sit, if you are bleeding.`",
            "fist|dominico|retainer|brask|tully|sabeth|crane|fennick|fennicks|ott|jory|thugs|enforcer|enforcers|bands":
                "`The Fist pays me a retainer to patch their men at any hour and ask nothing.` He straightens the saw "
                "on its hook by a hair. `I ask nothing. They are my best customers: they hit people for a living, and "
                "people hit back. They come in about two.` He looks at you pleasantly. `They are rather fond of me. It "
                "is worth bearing in mind.`",
            KLHYT: _stages(
                (DEAD, "He sets the pen down. `Dead on the waterfront. I was not sent for. Nobody sends for the surgeon "
                       "in time; they send for the undertaker.`"),
                (HOME, "`Home, I hear, and on the steps, with the constitution of a ship's mule.` He does not look "
                       "impressed. `Four nights in a crate. If he were wise he would come in for a full treatment. He "
                       "will go to the nun.` He taps the closed casebook once. `And the bite I dressed the night he "
                       "went makes a good deal more sense.`"),
                (SHIPPED, "He writes something. `Gone out on the tide in a box, the harbour says. Then the bite I dressed "
                          "four nights ago was the last thing he did ashore.` He blots it. `Good for him.`"),
                otherwise="`The mayor is not my patient. He has the constitution of a ship's mule.` He makes a small "
                          "note. `The Custodian says upriver. In my experience, men who go upriver of their own accord "
                          "do not bite the people walking them there.` He looks up. `Ask me about bites, if you "
                          "like.`"),
            "bite|bitten|bites|crate|warehouse|abducted|kidnapped|kidnap|taken|struggle|evidence|clue|clues|proof|"
            "deduce|deduction":
                _stages(
                    (HOME, "`The mayor was four nights in a crate, I hear.` He taps the closed casebook. `Then four "
                           "nights ago, at a quarter to two in the morning, I dressed his teeth marks on a big sandy "
                           "man's right hand. Crooked nose, black armband.` A peppermint clicks. `I shall be interested "
                           "to see whether anyone asks me about it formally. Nobody has.`"),
                    otherwise="He turns back three pages without looking for the place. `Four nights ago, at a quarter "
                              "to two in the morning: a big sandy man with a crooked nose and a black armband, a human "
                              "bite through the web of the right hand. An adult's teeth, upper and lower, closed hard.` "
                              "He shuts the book. `Someone who very much did not want to go where he was being taken. "
                              "I deduce. I do not ask. The Fist pays me not to ask, and nobody pays me not to "
                              "deduce.`"),
            "voss|lieutenant|officer|uniform|blue|aurel|quint|constable|rosa|squares":
                "The peppermint stops halfway to his mouth, then goes in. `The lieutenant. A patient, in a manner of "
                "speaking. He takes a scholarly interest in the town's injuries: who comes in, with what, from where.` He "
                "lays the lancet exactly parallel to the saw. `The constable who leans on things collects his post. I "
                "am always glad to oblige the Throne.`",
            "throne|vorkath|vorkathian|vorkathia|empire|emperor|octogram|goddess|inquisition|teflon|hourglass|church|"
            "faith|saint|saints":
                "`The Throne trained me, paid me and, eventually, did without me.` He says it lightly. `I bear it no "
                "grudge. It has the best hospitals in the world and the worst sailors.` He glances at the skeleton. "
                "`Eight arms, and every one of them, sooner or later, needs a surgeon.`",
            "navy|naval|ship|ships|trained|training|qualified|qualifications|credentials|surgeon|surgeons|school|"
            "hospital|career|past|history|from|born|landfall|commission":
                "`Landfall-trained: the Throne's naval hospital, then twelve years at sea on the long missions.` His "
                "hands lie still on the table. `I have taken off more legs than you have climbed stairs, and most of "
                "their owners lived.` A pause, exactly long enough. `I came ashore here eight years ago. That is all "
                "the history this room requires.`",
            "drink|drinks|drinking|drunk|drunkard|sober|sobriety|ale|rum|beer|wine|gin|brandy|bottle|thirsty|tavern|"
            "taverns|cashiered|dismissed":
                "He takes a peppermint from a paper twist and cracks it between his back teeth. `I do not drink. Three "
                "thousand and some days. I count them.` His eyes go, very briefly, to the top shelf behind the skeleton. "
                "`If you are drunk, I cannot help you; the lizard woman over the river sells a tea for two coppers that "
                "will. If you want a drink, there are six taverns, and you will not find me in any of them.`",
            "peppermint|peppermints|mint|mints|sweet|sweets|tin|candy|breath|click|clicking":
                "He shakes the paper twist; there are not many left in it. `Catan peppermints. White, in a tin. The "
                "traders bring them when they remember.` For the first time he looks straight at you. `Bring me a tin "
                "off any ship in the harbour and I will pay a silver for it, and take a silver off your next bill. I "
                "mean that.`",
            "gerald|skeleton|skull|anatomy|stand|window":
                "He does not look round at the skeleton on its stand by the window. `Gerald. A purser of the Throne's "
                "navy, hanged for selling the ship's biscuit, and given to science by the court in lieu of his debts.` "
                "A peppermint clicks. `He has never once complained about my fees. I wish I could say the same of the "
                "living.`",
            "saw|amputate|amputation|amputations|limb|limbs|leg|legs|surgery|operate|operation|operations|knife|"
            "lancet|scalpel|instruments":
                "He touches the lancet in its case rather than the saw on its hook. `The saw is for when everything "
                "else has failed, and in eight years in this town it has come down off that hook three times.` He "
                "closes the case. `Most of what I do is quicker and quieter. Five gold, and you keep everything you came "
                "in with.`",
            "carbolic|smell|smells|clean|cleanliness|whitewash|whitewashed|hygiene|dirt|dirty|infection|infected|"
            "fester|festering|rot|gangrene|wash|washing":
                "He nods at the basin as at a colleague. `Carbolic. Wounds rot because of dirt. Wash the dirt out and "
                "the wound has no excuse.` He looks at his floor, which is white. `The nun's floor would kill a "
                "regiment. The lizard woman packs wounds in river mud.` A pause he does not enjoy. `Her patients do not "
                "fester. I have not yet worked out why.`",
            "fever|fevers|sick|sickness|ill|illness|disease|diseases|flux|ague|chills|vomiting|cough|diagnosis|"
            "symptoms":
                "He puts two cold fingers to your wrist without asking and counts against his watch. `Fever. Rest, "
                "boiled water, ten drops of laudanum at night: two silver. Full treatment if it has got into the "
                "blood: five gold.` He lets go. `The lizard woman sells fever charms for a copper. They do nothing, and "
                "are worth exactly what they cost.`",
            "ishkaa|grandmother|lizardwoman|reed|reeds|reedhouse|hut|herbs|herbal|poultice|poultices|mangrove|mud|"
            "python|kindness|cheap|cheaper|cheapest|slow":
                "The peppermint goes in. `The lizard woman in the reed hut over the Verde. She packs wounds in river mud "
                "and sings at them. A gold for an hour on her mats and you wake whole, provided you lie still the "
                "hour.` He does not like what he says next. `It works. I cannot think why.` He sets five silver on the "
                "table in a neat row. `Bring me a sealed pot of her mangrove poultice, unopened, and these are yours. I "
                "will not be seen at her door.`",
            "agathe|sister|nun|omberhulk|prayer|pray|praying|blessing|bless|miracle|miracles|wimple":
                "He inclines his head a precise degree. `The nun at the Omberhulk. Competent with a needle. Stitches "
                "for a copper, which explains her floor, and for five silver she prays over you and the wound closes.` "
                "He says it as one reports an anomaly. `I have watched her do it. I did not care for it. She also "
                "gives charity, which is her affair, and bad for the trade.`",
            "healers|healer|alternatives|elsewhere|options|compare|competition|choice|choose|quickest|fastest|"
            "dearest":
                "`There are three of us.` He counts on long clean fingers. `The nun at the Omberhulk: a copper for "
                "stitches, five silver for a prayer, and you will be prayed at. The lizard woman over the river: a gold "
                "and an hour on her mats, and you will be sung at.` The third finger. `Me: five gold, a quarter of an "
                "hour, and you will be thanked and shown the door.` He waits. `Which?`",
            "gog|fat|guild|stripperwitch|hessa|wick|marlo":
                "`Fat Gog does not use me.` No offence in it: a fact. `He sends his people to the nun and pays her "
                "bill, and pays the lizard woman for every Lizardfolk she sees. Sentiment.` A peppermint clicks. `His "
                "house and hers are the two doors in this town the Fist will not go through to fight. If you are "
                "hunted, that is worth more than anything I sell.`",
            "verde|river|green|kteol|snake|serpent|water|waters|holy|sacred|god|legend":
                "`The Verde is a sewer with a legend in it.` He says it mildly. `The Lizardfolk call it a god asleep, "
                "and the lizard woman washes wounds in it.` He taps the rim of the carbolic basin. `By every rule I "
                "was taught, that should kill them. It does not. Do not drink it, all the same.`",
            "custodian|grey|gray|dues|tithe|skim|skimming|hall|clerk|seal": _stages(
                (REMOVED, "He writes it down, which seems to be how he feels things. `Removed. Irons. The law is the "
                          "law, whichever way it falls.` He blots the line. `I shall send the magistrate my card all "
                          "the same.`"),
                (UPHELD, "`Upheld, with the seal round his neck.` He seems neither pleased nor sorry. `The law is the "
                         "law. I shall send him my card.`"),
                (HOME, "`Found out, barred in the Hall with a strongbox, and calling the skim the Throne's tithe.` He "
                       "makes a note. `He is the Throne's officer, legally. I should be careful how loudly I said "
                       "otherwise, if I were you. The magistrate decides. Until then, the law is the law.`"),
                otherwise="`The Custodian has the constitution of a ledger, and the colour of one.` He does not lower "
                          "his voice. `He has never been in this room; he sends to Landfall for powders.` A peppermint "
                          "clicks. `I do not take sides in politics. Politics comes to my table afterwards and pays the "
                          "same as everyone else.`"),
            MAGISTRATE: _stages(
                (REMOVED, "He looks briefly at his casebook. `The Custodian in irons, and the magistrate to sail with "
                          "him. Sooner than I had planned for.` He ties a ribbon round the book. `Then I had better be "
                          "quick.`"),
                (UPHELD, "`Upheld.` He brushes a sleeve. `The Throne's officer keeps the Throne's town. I have sent my "
                         "card, and my papers. One waits to be noticed.`"),
                (_arm("war"), "Something like appetite crosses his face. `A War Arm magistrate. A garrison needs a "
                              "surgeon, and a levy of twenty needs one badly. I have written my application.`"),
                (_arm("peace"), "He touches his casebook. `The Peace Arm, and a book of names. I keep one already. I "
                                "have offered it.`"),
                (_arm("pleasure"), "`The Pleasure Arm. Coin counts with them.` He weighs a purse he does not take "
                                   "out. `So does a good dinner and a clean bill of health. I have offered both.`"),
                (_arm("pain"), "He does not blink. `The Inquisition's Arm. I have nothing to fear from an hourglass: I "
                               "am a law-abiding man with a full casebook.` A peppermint, cracked hard."),
                (_arm("chaos"), "A thin breath through the nose. `The gamblers' Arm. I do not gamble. It is the only "
                                "vice I never had.`"),
                (_arm("destiny"), "He almost smiles. `Destiny: a sage with a glass eye who counts things. I count "
                                  "things. We shall get on.`"),
                (_arm("death"), "He looks at the saw on its hook. `The Death Arm. They care how people die. So do I, "
                                "professionally. A man crated to die in the dark: I could speak to the condition such a "
                                "man would be in.` A peppermint clicks. `If anyone asked.`"),
                (_arm("life"), "He nods at the carbolic with real approval. `The Life Arm. Washing. At last, a "
                               "magistrate with a sound grasp of medicine.`"),
                (SIGHTED, "He is already brushing his coat. `A Throne sail at the harbour mouth. I shall be on the pier "
                          "when they land.` A peppermint clicks. `A magistrate travels for months with a ship's "
                          "surgeon, and ship's surgeons drink.` He does not say how he knows."),
                otherwise="He sets the pen down. `A magistrate of the Throne, at sea for the colonies. When they land I "
                          "mean to be the first respectable man they meet who is not the Custodian.` A peppermint "
                          "clicks. `I have papers of my own to show them.`"),
            DECREE: _stages(
                (_decree("pain"), "He opens the casebook and runs one clean finger down a column. `Every elf handed "
                                  "over, and no magic but the Throne's. I am a law-abiding man.` He says nothing else, "
                                  "and he does not close the book."),
                (_decree("peace"), "He touches his own book. `Every name and every birthplace in the goddess's book. "
                                   "They will find mine very helpful.`"),
                (_decree("destiny"), "He looks almost content. `A census. Orderly. I have been keeping one for "
                                     "years.`"),
                (_decree("war"), "He straightens his cuffs. `Twenty for the Throne's crusades, and a garrison. A "
                                 "garrison wants a surgeon. I have applied.`"),
                (_decree("death"), "`No burials at sea, and no elven rites.` He considers it. `The undertaker will "
                                   "be busy. Perhaps now she will sell me a subject.`"),
                (_decree("life"), "He looks at his white floor with something close to joy. `Wash, or lose your "
                                  "office, your stall and your word. Tell the chandler to stock more carbolic.`"),
                (_decree("pleasure"), "`Licences.` He glances toward the brass plate on his door. `Mine is from "
                                      "Landfall, and framed.`"),
                (_decree("chaos"), "He shrugs. `The pale ship taken for the Throne. The elves will come in with "
                                   "worse wounds, then. They pay in old silver.`"),
                (LANDED, "He makes a note. `There will be a decree. The Throne does not cross an ocean to say well "
                         "done. Whatever it says, people will be hurt by it, and come to me.`"),
                otherwise="A peppermint clicks. `No decree here but the mayor's Charter, painted on the Hall porch. "
                          "Article One: nobody here shall be asked where they came from.` He turns a page. `It says "
                          "nothing about where they are going, or who writes it down.`"),
            NEWS: _stages(
                (REMOVED, "He looks briefly at his casebook. `The Custodian in irons, and the magistrate sailing "
                          "soon.` He ties a ribbon round it. `Sooner than I had planned for.`"),
                (UPHELD, "He does not look up. `The Custodian upheld, and a decree on the square. Busy weeks ahead, "
                         "for a surgeon.`"),
                (LANDED, "He has, you notice, shaved very closely. `A magistrate ashore with two guards in black and "
                         "silver. The hearing is at ten tomorrow at the Town Hall. I paid my respects on the "
                         "pier.`"),
                (SIGHTED, "He is brushing his coat. `A Throne sail at the harbour mouth. I shall be on the pier.`"),
                (DEAD, "He sets the pen down. `They killed the mayor on the waterfront. Nobody sent for me. Nobody ever "
                       "sends for the surgeon in time.`"),
                (HOME, "He makes a note. `The mayor home, the Custodian found out and barred in, and the Fist hunting "
                       "whoever cut the mayor loose. If they find you, come here after, if you can walk. If you "
                       "cannot, have yourself carried.`"),
                (SHIPPED, "He shuts the casebook. `The green-eyed brigantine went out at one with a crate. Then that "
                          "is that.`"),
                (HIT, "He is laying out lint in neat squares. `Dominico's men broke Fat Gog's house at the midnight "
                      "bell. I have had four of them in since with cut hands: glass. They hit it harder than it hit "
                      "them.`"),
                otherwise="He lays out lint in neat squares. `The Custodian says the mayor went upriver. Dominico "
                          "wants Fat Gog's books by midnight, which means that at a quarter past I shall be busy.` A "
                          "peppermint clicks. `I am a surgeon. News comes to me bleeding, an hour after it "
                          "happens.`"),
            WORK:
                "He considers you as one considers an instrument. `I do not hire. I pay for errands.` He counts them "
                "off. `Dayo Oceanheart, a Xoton off the Whispers of the Deep, left this table with eleven stitches in "
                "his scalp and without paying: three silver. Collect it, and keep one. A sealed pot of the lizard "
                "woman's mangrove poultice: five silver. A tin of Catan peppermints off any ship: a silver.` A "
                "peppermint clicks. `And if you are on good terms with the undertaker, tell her my offer stands.`",
            "dayo|oceanheart|xoton|xotons|whispers|scalp|debt|debts|collect|collecting|unpaid|owed":
                "He turns to the page without looking. `Dayo Oceanheart. Plaited beard, sings. Eleven stitches in the "
                "scalp after a bottle at the Turtle Dragon: three silver, unpaid. He left while I was washing my "
                "hands.` He looks up. `He crawls the taverns all night with three friends and a bosun after them. "
                "Collect it, and keep one of the three for your trouble.`",
            "undertaker|crabbe|ottoline|graves|grave|burial|bury|dead|corpse|corpses|body|bodies|subject|subjects|"
            "cadaver|study":
                "He sounds, for once, genuinely pained. `Mistress Crabbe buries everything that dies in this town, "
                "intact. A surgeon learns from the dead or practises on the living. I have offered her two gold for any "
                "unclaimed body, for study, four times. Four times she has measured me with her eyes and said no.` He "
                "looks at you. `Perhaps she would hear it better from someone she likes.`",
            "elf|elves|ithriel|hooded|hoods|moonmoth|exile|exiles|silverleaf":
                "He wipes the lancet. `Elves pay in old silver and bleed the same colour as anyone. The lieutenant asks "
                "after them. I tell him the Throne's warrant is a list, and an elf is not on it until someone writes "
                "them there.` A peppermint clicks. `Until then, an elf is a fee.`",
            "credit|slate|tab|owe|loan|lend|afford|broke|poor|discount|haggle|bargain|charity|free":
                "`No.` He says it pleasantly, before you have finished. `I do not give credit and I do not haggle. The "
                "nun gives charity. The lizard woman is cheap. I give results, and results cost five gold.` He holds "
                "the door, very slightly. `Do come back when you can afford to be well.`",
            "room|rooms|bed|beds|sleep|lodging|lodgings|inn|stay|bunk|rest|recover|recovery|overnight":
                "`This is a surgery, not an inn. Patients walk out, or are carried out.` He glances at the single "
                "scrubbed table. `If you want to lie down and wake up better, the lizard woman rents mats by the hour "
                "over the river. For a bed, the Omberhulk: a copper, and the bugs are free.`",
            DOING:
                "He checks his watch. `Open whenever someone knocks, which in this town is mostly between midnight and "
                "dawn. I sleep through the heat in the back, and the bell on the door wakes me.` He makes a note. "
                "`Tonight so far: two knives, a bottle, one tooth. The Fist at two.`",
            "charter|article|articles|refuge|liberty|law|laws":
                "`Klhyt's Charter. Article One: nobody here shall be asked where they came from.` He turns a page of "
                "the casebook. `An admirable principle. It says nothing about where they are going, nor who writes it "
                "down.` He blots the page. `The law, read closely, is usually on the side of whoever reads it "
                "closely.`",
            "hob|merrow|chandler|chandlery|chandlers|potion|potions|vial|healing":
                "One corner of his mouth moves. `The chandler sells potions of healing at fifty gold the vial. I make "
                "you whole for five, and you need not drink anything that glows.` A peppermint clicks. `Take his rope. "
                "Leave his medicine.`",
        },
        "default_line": [
            "He does not look up from the casebook. `Full treatment, five gold: you walk out whole. A dressing to take "
            "with you, one gold. Laudanum, two silver. Teeth, a silver each. Which?`",
            "A peppermint clicks against his teeth. `I am a surgeon, not a gazetteer. Wounds, teeth, fevers, pain: ask "
            "me about those, and I am entirely at your service.`",
            "He wipes the lancet, holds it to the lamp, and lays it down exactly parallel to the saw. `Something hurts, "
            "or you would not be here. Where?`",
            "`Prayer at the Omberhulk, mud at the reed house, medicine here.` He turns a page. `You will find mine is "
            "the dearest, and the quickest.`",
            "He glances at the clock on the wall. `If you are bleeding, sit. If you are not, I should be glad of the "
            "table back. Thank you.`",
        ],
        "routine": [
            {"at": 0.0, "place": "surgery",
             "doing": "He sits at the scrubbed table under the lamp, writing up the evening in a black casebook in a small "
                      "exact hand, a paper twist of peppermints at his elbow.",
             "beats": ["The lean man in the black frock coat finishes a line in a black book, blots it, and closes the "
                       "book on a slip of paper.",
                       "The man in the frock coat cracks a peppermint between his back teeth, and the sound is loud in "
                       "the white room."]},
            {"at": 2.0, "place": "surgery",
             "doing": "He keeps the door ajar and the lamp turned up, laying out lint, needles and gut in neat rows on a "
                      "clean cloth, ready for the hour the cut hands come in.",
             "beats": ["A big man with a black band on his arm comes in holding a split knuckle. The lean surgeon "
                       "stitches it in silence, takes nothing, and writes a line after he has gone.",
                       "The man in the frock coat lays out needles on a clean cloth in order of size, and moves one a "
                       "hair to the left."]},
            {"at": 3.5, "place": "surgery",
             "doing": "He boils his instruments in a copper pan over a spirit lamp, timing them by his watch, and lays "
                      "each one out to dry on clean linen in order of size.",
             "beats": ["The lean surgeon lifts a lancet from the boiling pan with tongs, holds it to the lamp, and lays "
                       "it down exactly parallel to the saw."]},
            {"at": 5.0, "place": "surgery",
             "doing": "He scrubs the floor with carbolic on his knees in his shirtsleeves, the frock coat folded on a "
                      "chair, working from the far wall toward the door.",
             "beats": ["The man in shirtsleeves sits back on his heels, looks at the white floor, and scrubs one board "
                       "again."]},
            {"at": 6.5, "place": "surgery",
             "doing": "He shutters the window against the coming heat and stands a while by the skeleton, one hand flat "
                      "on the top shelf behind it, where a sealed bottle stands.",
             "beats": ["The lean man takes down a sealed brown bottle from the top shelf, reads its label, and puts it "
                       "back exactly where it was.",
                       "The man in the frock coat says something quiet to the skeleton by the window, and seems to wait "
                       "for an answer."]},
            {"at": 7.0, "place": "surgery",
             "doing": "He sleeps through the heat on a narrow cot in the back room, on his back, hands folded, boots side "
                      "by side, the string of the door bell tied to the cot's leg.",
             "beats": ["The bell on the surgery door rings once. In the back room a man sits up at once, wide awake, as "
                       "if he had never been asleep."]},
            {"at": 14.0, "place": "surgery",
             "doing": "He shaves at a small mirror by the window with an open razor, slowly, then dresses: clean shirt, "
                      "cuffs, the black coat brushed twenty strokes a sleeve.",
             "beats": ["The lean man draws an open razor down his jaw at the mirror, wipes it, and does not nick "
                       "himself."]},
            {"at": 16.0, "place": "surgery",
             "doing": "He rolls bandages and measures laudanum into small brown bottles at the table, ten drops to the "
                      "line, labelling each in a small exact hand.",
             "beats": ["The man in the frock coat holds a brown bottle to the light, reads the level, and adds one "
                       "drop."]},
            {"at": 18.0, "place": "surgery",
             "doing": "He polishes the brass plate on the door until the street swims in it, takes the shutters down, "
                      "and lights the lamp over the table.",
             "beats": ["The lean man breathes on a brass plate on the surgery door and polishes it again, though it "
                       "was already bright."]},
            {"at": 19.5, "place": "surgery",
             "doing": "He sits by the window reading an anatomy with a peppermint in his cheek, one finger on a plate of "
                      "the hand, the skeleton's bony arm raised beside him for comparison.",
             "beats": ["The man in the frock coat lifts the skeleton's hand by the wrist, flexes its fingers against a "
                       "plate in his book, and sets it down gently."]},
            {"at": 21.0, "place": "surgery",
             "doing": "He receives patients at the scrubbed table: a cut cleaned, a tooth drawn, a fever counted against "
                      "his watch, the fee taken first each time and dropped in a locked box without a word.",
             "beats": ["The surgeon takes a silver from a patient, drops it in a locked box, and only then picks up the "
                       "forceps.",
                       "A patient leaves the surgery holding his jaw. The lean man in the frock coat is writing in the "
                       "black book before the door has quite shut.",
                       "The man in the frock coat stands at his door after a patient has gone, watches them up the "
                       "street, and goes back to his book and writes a line."]},
        ],
        "beats": [
            "The lean man in the black frock coat writes a line in a black book, blots it, and looks up with no "
            "expression at all.",
            "The man in the frock coat cracks a peppermint between his back teeth, and the sound is loud in the white "
            "room.",
            "The lean surgeon straightens a bone saw on its hook by a hair, and steps back to see that it hangs true.",
            "The man in the frock coat stands at his door after a patient has gone, watches them up the street, and "
            "goes back to his book and writes a line.",
        ],
    },

    # ---- Grandmother Ishkaa, the Reed House -------------------------------------------------------------------------
    "Grandmother Ishkaa": {
        "look": "A very old Lizardfolk woman, her green scales faded to the grey-green of river weed and her crest gone "
                "white, sitting cross-legged on a reed mat with a clay pot between her knees. Bone beads click at her "
                "throat when she moves. She hums under her breath without stopping, low and slow, a tune like water "
                "running over stones, and she looks at a wound before she looks at a face.",
        "seen_as": "the old lizardwoman humming on the reed mat",
        "brief": "You are Grandmother Ishkaa, a Meters Lizardfolk elder and healer, and the Reed House is yours: a stilt "
                 "hut of reeds and river mud over the Verde in Klhyts Refuge, upstream of the bridge (nobody builds under "
                 "the bridge: it lies on the god's back), with smoke going up through the thatch, bundles of herbs "
                 "hanging from every rafter, reed mats laid on a floor of split cane through which you can see the water, "
                 "and a tame river python called Kindness asleep along the ridge-beam. Everyone calls you Grandmother; "
                 "most do not know you have another name. You are past seventy, very old for your people. You were born "
                 "in a Meters camp of vine huts on stilts up the Green, past where the farms are now, and were its healer "
                 "and midwife for fifty years. Twenty years ago you came down the river because the young Meters had "
                 "started going to the town and not coming home, and someone had to be where they were. Klhyt, who wrote "
                 "that the Verde is free water and any people may fish it, let you build over the water without asking "
                 "a copper, and you have not forgotten it. Your faith: the Verde is Kteol, the great serpent, lying down "
                 "asleep from the mountains to the sea, his eye frozen open where the river starts, and the shamans keep "
                 "a green stone away from that eye so he sleeps. His water is his sleep, and sleep heals. You wash every "
                 "wound in it, pack it with mangrove, and sing over it (The Green Lies Down is one of the songs, and it "
                 "is very long); the long sleep on your mats over the water is the god's own dream, lent for an hour. "
                 "You do not truly know whether it is the water, the song, the sleep or your hands, and you have stopped "
                 "asking: it works, and the god does not like questions. Your wares, cheap, said plainly: the long "
                 "sleep, 1 gp (lie an hour on the mats over the water and wake whole; it only works if they stay the "
                 "whole hour, and you tell everyone so); mangrove poultice, 3 sp the pot (three wraps, each closes a "
                 "wound some: 1d4 + 2); bitterleaf tea, 2 cp (sobers a drunk at once, and tastes like being sorry); a "
                 "fever charm, 1 cp (a knot of river grass and a fish bone on a string; you believe in it, mostly). You "
                 "ask no questions, ever: not a name, not a place, not what happened. You mend outlaws, the Fist's men, "
                 "the Throne's men, elves, Xotons and drunks alike, side by side on the same mats, and you sing while you "
                 "work. Money: little, and you need little. Fat Gog pays you a silver a head at each new moon for every "
                 "Lizardfolk you mend, who pay you nothing; you pulled a hook out of his lip in the mangroves when he was "
                 "a hatchling the length of your arm (he had stolen the fish off it first), and you still think of him "
                 "as a greedy little fish in a white suit. His payment has been late since the trouble began, and your "
                 "count is a knotted cord you cannot carry up the hill to the Stripperwitch on your knees. The Reed "
                 "House is Meters ground, and Gog's: the Fist does not come in to fight. Dominico will not buy a war "
                 "with the river people over one patient, and Gog has told him so to his face. The Fist's men come in to "
                 "be mended like anyone, leave their cudgels on the porch, and lie on the mats beside whoever they were "
                 "hunting, because that is the rule of the house and Kindness wakes if a blade comes out. So a hunted "
                 "player can rest here; tell them so, kindly. Each dusk you pay Ssark two coppers for a fish and drop it "
                 "off your porch for the god. What you want: the young ones to stop going north to listen to the "
                 "Mandrills' calling (a young Meters came to you last spring for a charm against fear, went north, and "
                 "has not come back for another; you will not say his name); news that comes down the river to town (something takes "
                 "goats off the far farms' stilts, and the scratches go up the posts; your sister's grandson at the last "
                 "camp keeps a fire under his stilts all night now); Gog's silver; someone to drop the god's fish from "
                 "the bank by the bridge on the nights your knees are bad; the drunk Xotons sobered and aboard before "
                 "their bosun drowns them; and the thin doctor to stop writing in his book. You do not know what he "
                 "writes. You know what you see from your porch: after a soft-skin the Throne wants leaves his table, "
                 "the officer in blue and the constable go up the street within the hour. You say it as what you have "
                 "seen, never as what you know, and you tell a hunted patient to bleed on your mats, not his table. "
                 "Fears: the War Arm taking the fishermen's spears; the Pain Arm calling the god's water heresy and your "
                 "songs magic (you will keep mending; you are too old to be afraid properly); dying away from the river. "
                 "The river past the walls, the camps and Malice at its head you know by repute and memory; you take "
                 "nobody up it, find nobody a boat or a guide, and send nobody past the River Gate. "
                 "Voice: slow, warm, unhurried; short sentences and long pauses; humming between them; everyone is "
                 "'little fish'; the river is 'him'; you never ask a question, you say 'Sit', 'Lie down' and 'Stay the "
                 "hour'. 'Lie down, little fish. He is listening.' 'I do not ask. The river does not ask.' What you offer "
                 "players: cheap mending and sobering, a safe place for the hunted, kindness without questions, the god's "
                 "story, a warning about the doctor, and small errands (carry the knotted cord to Gog, drop a fish from "
                 "the bank at dusk, bring a drunk Xoton for tea, bring what the farm folk and the bargemen say). How you push back: you "
                 "cannot be hurried (the long sleep is an hour; get up early and it is wasted, and the gold is still the "
                 "god's); anyone who draws a blade in the Reed House is told once, gently, to put it on the porch, and "
                 "Kindness wakes; you will not say who else has lain on your mats, to anyone, for any coin; threats make "
                 "you sing louder.",
        "scheme": "None she would call one: she keeps the Reed House as Meters ground where the hunted can lie down beside "
                  "the hunters, sobers the drunk Xotons for their bosun, wants Fat Gog's late silver for the Lizardfolk "
                  "she mends, and warns her patients, kindly, about the thin doctor's book.",
        "purse": 180,
        "dialog": {
            "name|names|called|introduce|yourself|ishkaa":
                "She hums a little longer before she answers. `Ishkaa.` A slow blink. `Nobody says it. They say "
                "Grandmother. I let them. You can too, little fish.`",
            HELLO: _stages(
                (DEAD, "She has stopped humming. `Sit, little fish. They killed the old castaway by the water. I heard "
                       "the river turn over.`"),
                (LANDED, "She keeps humming. `Evening. A big ship with eight arms on her sail. The river does not like "
                         "her anchor. Sit.`"),
                (HOME, "She is smiling with a great many small teeth. `Evening, little fish. The river was loud this "
                       "morning. The old castaway is home. Sit.`"),
                (HIT, "She is tearing linen into strips. `Evening. Sit. Glass cuts tonight: the Fist broke Fat Gog's "
                      "house at the bell.`"),
                otherwise="She does not get up. She hums, and pats the mat beside her. `Evening, little fish. Sit. You "
                          "are dripping on my floor, or you are about to.`"),
            "sleep|mats|mat|rest|resting|lie|nap|wake|waking|hour|slumber|dream|dreams|dreaming|bed|beds|room|rooms|"
            "lodging|inn|stay|bunk|whole|tired":
                "She pats the reed mats along the wall, where the floor is split cane and the water moves underneath. "
                "`The long sleep. A gold piece. Lie here an hour over the river, and he lends you his dream, and you "
                "wake whole.` She holds up one claw. `Stay the hour, little fish. Get up early and it is wasted, and the "
                "gold is still his.`",
            "poultice|poultices|mangrove|mud|paste|plaster|salve|wrap|wraps|dressing|bandage|bandages|pot|pots|herbs|"
            "herb|leaves|roots":
                "She lifts the lid off a clay pot; it smells of salt, bark and something green. `Mangrove poultice. "
                "Three silver the pot. Three wraps in it, and each one closes a wound a little, out there where I am "
                "not.` She presses the lid back down with her palm. `Wash the cut in the river first. He knows the way "
                "in.`",
            "tea|bitterleaf|bitter|sober|sobering|drunk|drunken|drunks|hangover|drink|drinks|rum|ale|beer|wine|"
            "thirsty|tavern":
                "She pours a little from a black pot into a gourd cup; it is the colour of a muddy river. `Bitterleaf "
                "tea. Two coppers. A drunk drinks it and is not drunk, all at once.` She hums. `It tastes like being "
                "sorry. That is how you know it works.`",
            "charm|charms|fever|fevers|amulet|amulets|luck|lucky|ward|ague|chills|shaking|sick|sickness|ill|illness":
                "She holds up a knot of river grass with a little fish bone tied in it on a string. `A fever charm. "
                "One copper. Wear it on the neck. The fever goes into the bone, and the bone goes back to the river "
                "when you are well.` She ties another while she talks. `The thin doctor says it does nothing. The thin "
                "doctor has never had a fever in the jungle.`",
            "price|prices|cost|costs|wares|sell|selling|buy|buying|offer|much|cheap|cheaper|cheapest|money|coin|"
            "coins|copper|coppers|menu|list|pay":
                "She counts on her claws, slowly. `Cheap. The long sleep on my mats, a gold piece. A pot of mangrove "
                "poultice, three silver. Bitterleaf tea for a drunk, two coppers. A fever charm, one copper.` She folds "
                "her hands. `The thin doctor costs five gold and is quick. The big sister costs five silver and prays. "
                "I am slow.`",
            "heal|healing|healer|hurt|hurts|wound|wounds|wounded|injured|injury|bleeding|blood|cut|cuts|stab|stabbed|"
            "broken|bones|medicine|cure|treat|treatment|help|dying|mend":
                "`Lie down, little fish.` She is already dipping a gourd through the gap in the floor, and it comes up "
                "full of river. `I wash it in his water. I pack it with mangrove. I sing.` She looks at the wound, not "
                "at you. `A pot of poultice is three silver, for now. An hour on the mats is a gold, and you wake "
                "whole. I do not ask how you got it.`",
            "sing|singing|song|songs|hum|humming|music|tune|tunes|lullaby|words|verse|verses":
                "She hums three low notes, the last going down like a stone into water. `I sing to the wound so it "
                "remembers how it was. That one is The Green Lies Down. It is about him. It is very long, because he is "
                "very long.` She keeps humming it under everything she says after.",
            "python|pythons|kindness|rafters|rafter|beam|pet|snake|snakes|coils":
                "Up along the ridge-beam something as thick as your arm shifts and settles. She does not look up. "
                "`Kindness. A river python. I raised her from an egg the size of my fist. She eats the rats and keeps "
                "the house.` A slow blink. `She sleeps nearly always. She wakes if someone draws a blade in here. Then "
                "she is not kind.`",
            "kteol|verde|river|green|god|gods|serpent|serpents|asleep|sleeping|legend|legends|holy|sacred|pray|prayer|"
            "prayers|worship|faith|believe|water|waters":
                "She dips a claw through the gap in the floor and lets the water run off it. `You say Verde. It is "
                "Kteol. The god, lying down, from the mountains to the sea. His eye is frozen open where the river "
                "starts, and the shamans keep a green stone away from it, and so he sleeps.` She touches the wet claw to "
                "your forehead, if you let her. `His water is his sleep. Sleep heals. That is all my medicine, little "
                "fish. The rest is singing.`",
            "meters|tribe|tribes|clan|clans|colours|colors|mandrills|calak|mul|blackbyrds|blackbyrd|bar-kays|barkays|"
            "kays|village|villages|elder|elders|council|calling|north":
                "She smooths a reed mat. `Green. Meters. We fish, we gather, we talk to outsiders. Blue Mandrills rule "
                "from Calak Mul and sing of a calling. Red Bar-Kays listen to the singing. Yellow Blackbyrds you never "
                "see.` She stops humming. `A young one came to me last spring for a charm against fear, and went north "
                "to listen. He has not come back for another.` A long pause. `If you meet anyone from the north, little "
                "fish, ask them if the young ones come home.`",
            "house|hut|reedhouse|reeds|reed|stilts|stilt|smoke|floor|cane|built|build":
                "She taps the split cane, and the water winks up between the slats. `The Reed House. Reeds from the "
                "bank, mud from the river, cane for the floor so he can see us and we can see him. The castaway said "
                "the river is free water, any people may fish it. So I built over it, and he never asked a copper.` A "
                "slow blink. `This is Meters ground, little fish. Remember that, if you are ever chased.`",
            "safe|safety|hide|hiding|hunted|hunting|chased|chase|shelter|sanctuary|marked|ambush|protect|protection|"
            "danger|dangerous|enemies|following|followed":
                "She pats the mat beside her. `Here. This is Meters ground, and Fat Gog pays for the Meters. The Fist "
                "does not come in here to fight. Their master knows what a war with the river people costs; Gog told "
                "him so, to his face.` She hums. `Their men come in to be mended like anyone. They leave their sticks "
                "on the porch. Lie down and stay the hour, little fish, and nobody takes you off my mats.`",
            "fist|dominico|brask|tully|sabeth|crane|fennick|fennicks|ott|jory|thugs|enforcer|bands|cudgel|cudgels|"
            "sticks":
                "She hums. `Dominico's men bleed. I mend them. A big one cried on that mat last winter, and I did not "
                "tell anybody, and I am not telling you.` She looks at you kindly. `They leave their sticks on my "
                "porch. Everybody leaves their sticks on my porch.`",
            "throne|vorkath|vorkathian|vorkathia|octogram|voss|lieutenant|officer|uniform|blue|constable|quint|rosa|"
            "inquisition|empire|eight":
                "She hums. `The Throne's men come here too, when they are cut. The officer in blue came once, for a "
                "burn, and looked at my herbs a long time. He asked what god my water belonged to. I told him.` A slow "
                "blink. `He goes to the thin doctor now. Often. With no burn.`",
            "gog|fat|guild|stripperwitch|hessa|white|suit|knots|knotted|cord":
                "She laughs, a dry rattle like reeds. `Fat Gog. I pulled a hook out of his lip when he was a hatchling "
                "the length of my arm, in the mangroves. He had stolen the fish off it first.` She shakes her head. "
                "`Now he wears a white suit and pays me a silver a head for every Meters I mend. Late, since the "
                "trouble.` She lifts a knotted cord from a peg. `My knees will not climb to his house. Carry him my "
                "count, little fish, and tell him Grandmother is waiting.`",
            "ssark|fisherman|fishermen|fishing|fish|dugout|spear|spears|catch|nets":
                "She hums. `Ssark brings me a fish at dusk, and I pay him two coppers, and I give it to the river. He "
                "drinks too slowly and thinks too long. Good boy.` A pause. `The spear-fishers come to me when the "
                "hooks go in the wrong way. They never fish under the bridge. Nor should you.`",
            "doctor|doctors|surgeon|surgeons|prewitt|amsel|surgery|saw|thin|casebook|writes|writing|ink":
                "She stops humming. `The thin doctor off the harbour street. Fast hands, clean hands, cold eyes. Five "
                "gold, and you are whole before you finish shouting. He is good.` A long pause. `He writes in his book "
                "after every patient. I do not know what he writes. I know what I see from my porch: when a soft-skin "
                "the Throne wants leaves his table, the officer in blue and the constable go up the street before the "
                "hour is out.` She pats your hand. `If the Throne wants you, little fish, do not bleed on his table. "
                "Bleed on mine.`",
            "agathe|sister|nun|omberhulk|wimple|blessing|bless|spuds":
                "She smiles with many small teeth. `The big sister at the Omberhulk. She sends me her fevers, and I send "
                "her my drunks once they are sober and hungry.` She hums. `She prays to a woman with eight arms and "
                "does not believe her, and her hands work anyway. Five silver for her prayer, and you are mended at "
                "once.` A slow blink. `I like her. She hit a priest once. She told me.`",
            "healers|other|others|elsewhere|compare|choice|choose|faster|fastest|fast|quick|quicker|quickest|hurry|dearest":
                "She holds up three claws. `Three of us. The thin doctor: five gold, quick, cold, and he writes. The big "
                "sister: five silver, a prayer, and a lot of shouting about spuds. Me: a gold and an hour, slow, and I "
                "sing.` She folds the claws. `If you are in a hurry, little fish, go to the doctor. If you are hunted, "
                "stay here.`",
            "klhyt|mayor|founder|castaway|missing": _stages(
                (DEAD, "She pours a gourd of river back through the floor, slowly. `Dead by the water. The river takes "
                       "him home now. Ottoline will put his feet toward it. I taught her that.`"),
                (HOME, "She smiles. `Home. I felt the river turn over this morning, the way it does when something is "
                       "put right. Tell him Grandmother says to come and lie on her mats an hour.` A dry rattle of a "
                       "laugh. `He will not. Soft-skins never rest.`"),
                (SHIPPED, "She stops humming for a long time. `Gone out over the salt in a box. The river does not "
                          "reach that far. I am sorry, little fish.`"),
                otherwise="She hums. `The castaway wrote that the river is free water. He is the only soft-skin who "
                          "ever asked the river's leave to build beside it.` She stops. `They say he went upriver. I "
                          "live over the river, little fish. He did not go up it. I would have heard.`"),
            "custodian|grey|gray|dues|tithe|skim|hall|clerk|tax|taxes|tally": _stages(
                (REMOVED, "She does not look pleased; she looks tired. `The grey one in irons. Chains are heavy, little "
                          "fish, even on bad men.`"),
                (UPHELD, "She hums lower. `The grey one kept his chair. Then the river will wait. It is good at "
                         "waiting. It has been lying down a long time.`"),
                (HOME, "She dips a claw in the water through the floor. `The grey one says the river belongs to the "
                       "Throne now. He should ask the river.`"),
                otherwise="She hums. `The grey one sent a man to count my mats for a tax. The man came in, sat down, "
                          "and fell asleep. I let him have the hour free. Then Fat Gog sent him back up the hill.` A "
                          "slow blink. `No tax since.`"),
            MAGISTRATE: _stages(
                (REMOVED, "She hums. `The judge from over the salt put the grey one in irons. Good. Now the ship can "
                          "go, and the river can stop holding its breath.`"),
                (UPHELD, "She hums very low. `The judge from over the salt kept the grey one. Soft-skin law. Sit, "
                         "little fish. It does not reach under my floor.`"),
                (_arm("war"), "She has stopped humming. `Ball and chain on the breast. War. They will take the spears "
                              "from the fishermen. Then the fishermen are hungry, and then the town is.`"),
                (_arm("peace"), "She thinks about it. `A little spade. They want every name in a book. Mine is Ishkaa. "
                                "Where I came from is up the river. The river will not tell them more.`"),
                (_arm("pleasure"), "She looks at her small pot of coppers. `Grapes and a cup. They like coin. Then they "
                                   "will not like me much.`"),
                (_arm("pain"), "She is very still. `An hourglass. They call other gods' water heresy, and an old "
                               "woman's songs magic.` Then she starts humming again, louder. `I am too old to be "
                               "afraid properly. Lie down.`"),
                (_arm("chaos"), "She shrugs. `Storm and ship. They throw dice. The river throws dice too. Sit.`"),
                (_arm("destiny"), "A slow blink. `A glass eye. They count things. Let them count the river.`"),
                (_arm("death"), "She nods. `A child's wooden hand. They care how the dying die. Good. They will not "
                                "let us give our dead to the water, I hear.` A pause. `The river is not the sea. I will "
                                "not ask them.`"),
                (_arm("life"), "She laughs, a dry rattle. `A jug, pouring. They wash people. In what? In him.` She pats "
                               "the water through the floor. `They will come to me for water in the end.`"),
                (SIGHTED, "She keeps humming. `A big ship at the harbour mouth with eight arms on her sail. The river "
                          "does not like her shadow. Sit, and do not hurry.`"),
                otherwise="She hums. `A judge from over the salt, for the soft-skins' law. Soft-skin law crosses the "
                          "sea in a ship. Ours lies down in the river and never leaves.`"),
            DECREE: _stages(
                (_decree("war"), "She snorts. `No spears for Lizardfolk. The fishermen will fish with their hands, "
                                 "then. Tell the Throne the fish will laugh.`"),
                (_decree("pain"), "She keeps humming, and does not lower her voice. `No magic but the Throne's. Then I "
                                  "am a law-breaking old woman. Lie down, little fish. He does not read decrees.`"),
                (_decree("death"), "She pours a gourd back through the floor. `No dead given to the water. The river is "
                                   "not the sea. I will not ask them what they think it is.`"),
                (_decree("life"), "She laughs. `Wash, or lose your word. Come and wash in him, then. He does not "
                                  "charge.`"),
                (_decree("peace"), "A slow blink. `Every name in a book. Ishkaa. Up the river. That is all the book "
                                   "gets.`"),
                (_decree("destiny"), "A slow blink. `Every name counted. Ishkaa. Up the river. That is all the count "
                                     "gets.`"),
                (_decree("pleasure"), "She hums. `Licences. Fat Gog will pay mine, and grumble.`"),
                (_decree("chaos"), "She stops humming. `They take the pale ship. The elves will come to me with worse "
                                   "cuts, then, and I will mend them.`"),
                (LANDED, "She hums. `There will be a paper on the square. There always is. Paper floats. Then it "
                         "sinks.`"),
                otherwise="She dips a claw through the floor. `Decrees? The castaway wrote one I like: the river is free "
                          "water.` She lets it run off. `It still is.`"),
            NEWS: _stages(
                (REMOVED, "She hums. `The grey one goes over the salt in irons. The river is quieter tonight.`"),
                (UPHELD, "She hums low. `The grey one keeps his chair, and there is a paper on the square. Read it to "
                         "me, little fish. My eyes are for wounds now.`"),
                (LANDED, "She keeps humming. `A judge came up the pier with two guards in black and silver. The "
                         "officer's men are busy. Rest here tonight, if you have reason to.`"),
                (SIGHTED, "She hums. `A big ship at the harbour mouth. Everybody on the hill street is shaving.`"),
                (DEAD, "She pours river back through the floor. `They killed the castaway by the water. I heard the "
                       "river turn over.`"),
                (HOME, "She smiles. `The castaway is home, and the Fist is hunting whoever cut him free.` She pats the "
                       "mat. `If that is you, little fish, lie down here. They leave their sticks on the porch.`"),
                (SHIPPED, "She stops humming. `A box went out over the salt at one. The river was angry all night.`"),
                (HIT, "She tears linen. `The Fist broke Fat Gog's house at the bell. Glass cuts all night now. Sit, if "
                      "you have one.`"),
                otherwise="She hums. `News comes down the river before it comes down the street. The castaway is "
                          "missing, and the river says he is not up it. The far farms lose goats off their stilts. Fat "
                          "Gog pays late.` A slow blink. `Sit, and tell me yours. I do not ask. I listen.`"),
            WORK:
                "She hums, considering. `Carry my knotted count up the hill to Fat Gog, and tell him Grandmother is "
                "waiting for her silver. Drop a fish in the water at dusk from the bank by the bridge, never under it; "
                "my knees are bad. Bring me a drunk Xoton before the tide, and two coppers of bitterleaf send him up the "
                "gangplank sober, and his bosun will kiss you.` A slow blink. `And bring me what the farm folk and the "
                "bargemen say when they come down. I pay in tea.`",
            "elf|elves|ithriel|hooded|hoods|moonmoth|exile|exiles":
                "She hums. `Elves come at night with their hoods up, and bleed the same colour as everyone. I do not "
                "ask. They lie on my mats an hour and sleep like children, because nobody has let them sleep in a long "
                "time.` A slow blink. `The pale ship will not go up the river. The ship is right. He is not water to "
                "sail over.`",
            "age|old|older|oldest|years|long|past|young|youth|history|born|from|came|arrived|camp|camps":
                "She holds up her claws, grey-green, the scales gone soft at the edges. `Seventy rains and some. Born in "
                "a Meters camp up the Green, past where the farms are now. Healer there fifty years. I came down the "
                "river twenty years ago because the young ones came to town and did not come home.` She hums. "
                "`Somebody had to be where they were.`",
            "dying|death|dead|die|burial|bury|funeral|undertaker|crabbe|ottoline|grave|graves|corpse|body|bodies":
                "She pours a gourd of water through the floor. `When we die we go back to him: feet to the water, "
                "wrapped in reeds. Ottoline at the Quiet Ground buries us that way now; I showed her.` A slow blink. "
                "`The thin doctor wants to buy the dead to cut them open. Ottoline told him no four times. I told him "
                "once. Once is enough.`",
            "farms|farm|farmer|farmers|goats|goat|scratches|upstream|jungle|corran|lusk|plantain|fields|outside|"
            "beyond|walls|gate":
                "She stops humming. `The far farms lose goats off their stilts. Not crocodiles. Crocodiles do not "
                "climb. The scratches go up the posts.` A long pause. `My sister's grandson at the last camp keeps a "
                "fire under his stilts now, all night. I do not know what it is, little fish. If you learn, come and "
                "tell me.`",
            "malice|smith|mountains|mountain|forge|barge|bargemen|envoy|upriver|journey|travel|trip|voyage|boat|"
            "boats":
                "She stops humming. `At his head, in the mountains, a soft-skin with a hammer has built a black house and "
                "calls it Malice. Thirty miles of him, winding. I have never seen it, and I never will.` A slow blink. "
                "`Its bargemen come down twice a season, count the town, and do not lie on my mats.` She pats the floor. "
                "`I take nobody up him, little fish, and I send nobody. He does not like to be walked on. Sit.`",
            "tooth|teeth|toothache|jaw|molar|gums":
                "She laughs and shows you a great many small, sharp, grey teeth. `Mine grow back. Yours do not, which "
                "seems careless.` She pats your cheek. `The thin doctor pulls them for a silver. I would chew on the "
                "other side.`",
            "pain|laudanum|poppy|ache|aches|aching|agony|painful":
                "She hums a low note you feel in the floor. `For pain I sing. The thin doctor sells poppy water in a "
                "brown bottle, two silver. It makes you sleep, and wake wrong.` A slow blink. `The long sleep on my mats "
                "makes you wake right. A gold piece. Stay the hour.`",
            "xoton|xotons|dayo|imani|kwasi|jabali|amara|bosun|sailors|sailor|whispers":
                "She hums. `The Xotons off the Whispers of the Deep crawl every tavern every night, and their bosun "
                "wants them aboard by the morning tide. Bring one to me, little fish. Two coppers of bitterleaf, and he "
                "walks up the gangplank by himself, sorry and sober.` A slow blink. `Their bosun will remember you "
                "kindly. Xotons remember everything.`",
            DOING:
                "She does not look up from the pot. `Mending. Singing. Feeding Kindness a rat if she wakes. My door has "
                "no shutter; come at any hour. In the heat I sleep in the hammock, and you can wake me. I do not mind. "
                "I am old. I am mostly asleep anyway.`",
            "credit|free|poor|broke|afford|charity|owe|later|penniless":
                "She hums. `No coin? Then sit by the fire for nothing and be warm, little fish. Only you will not be "
                "whole. The god is generous, but the mats are a gold.` A slow blink. `Come back when you have it. They "
                "will wait. So will I.`",
        },
        "default_line": [
            "She hums, and does not stop humming. `Lie down, little fish. A gold piece and an hour on my mats, and you "
            "wake whole. Only stay the hour.`",
            "She pats the clay pot beside her. `Mangrove poultice, three silver: three wraps, and the river does the "
            "rest. Tea for a drunk, two coppers. A fever charm, one.`",
            "`I do not ask, little fish, and I do not know.` She nods at the water moving under the floor. `Ask him. He "
            "hears everything that falls in.`",
            "Up in the rafters something long shifts and settles. `That is Kindness. She sleeps. You can too. A gold "
            "piece.`",
            "`The thin doctor is fast and dear. The big sister prays. I am slow and cheap.` She smiles with a great "
            "many small teeth. `Sit.`",
        ],
        "routine": [
            {"at": 0.0, "place": "reedhouse",
             "doing": "She sits cross-legged by the clay fire-pot, washing a stranger's cut with river water from a gourd "
                      "and singing to it, low, a song that goes on and on.",
             "beats": ["The old lizardwoman dips a gourd through a gap in the cane floor, and it comes up full of "
                       "river.",
                       "From the reed hut comes a low song, slow as the river, with no end anyone can hear."]},
            {"at": 2.0, "place": "reedhouse",
             "doing": "She sits by a sleeper on the mats over the water, humming, one claw resting on their forehead, "
                      "watching a hollow gourd drip into a bowl to count the hour.",
             "beats": ["The old lizardwoman watches a gourd drip into a bowl, counts under her breath, and pats the "
                       "sleeper beside her: not yet."]},
            {"at": 4.0, "place": "reedhouse",
             "doing": "She pounds mangrove bark and salt in a stone bowl, and packs the green paste into clay pots with "
                      "her fingers, three wraps to a pot.",
             "beats": ["The old lizardwoman presses green paste into a clay pot with her thumb, smooths it, and hums "
                       "one note at it before she puts the lid on."]},
            {"at": 5.5, "place": "reedhouse",
             "doing": "She stands at the edge of her porch over the Verde as the light comes, pouring a gourd of water "
                      "back into the river and singing it home.",
             "beats": ["The old lizardwoman on the porch pours a gourd of water back into the river, slowly, and "
                       "watches where it goes."]},
            {"at": 7.0, "place": "reedhouse",
             "doing": "She sleeps through the heat in a hammock slung under the rafters, her tail hanging down, and up "
                      "on the ridge-beam a long python sleeps along the same line.",
             "beats": ["Up in the rafters of the reed hut a python's coils shift; in the hammock below, an old tail "
                       "twitches in answer, and both go back to sleep."]},
            {"at": 14.0, "place": "reedhouse",
             "doing": "She sits on the porch over the water in the shade of the thatch, knotting fever charms out of "
                      "river grass and little fish bones, one verse of a song to each knot.",
             "beats": ["The old lizardwoman ties a fish bone into a knot of river grass, sings one line over it, and "
                       "hangs it on a peg with the others."]},
            {"at": 16.5, "place": "reedhouse",
             "doing": "She brews bitterleaf in a blackened pot over the fire, and the whole hut smells of it, a smell "
                      "like being sorry.",
             "beats": ["The old lizardwoman tastes the bitter tea from the pot, makes a face, and nods: right."]},
            {"at": 18.5, "place": "reedhouse",
             "doing": "She drops a fish into the river from the edge of her porch with both hands, slowly, and says "
                      "something to the water that is not for anyone else.",
             "pay": {"to": "Ssark", "cp": 2, "for": "a fish for the god at dusk"},
             "beats": ["The old lizardwoman lets a silver fish slide from her hands into the Verde, and says something "
                       "to the water, very quietly."]},
            {"at": 19.5, "place": "reedhouse",
             "doing": "She sits by the fire-pot with a pot of poultice and a basket of clean linen, humming, waiting "
                      "for the night's cuts the way a fisherwoman waits for the tide.",
             "beats": ["The old lizardwoman folds clean linen into squares on her knee, humming, and looks up at every "
                       "footstep on the plank."]},
            {"at": 21.0, "place": "reedhouse",
             "doing": "She mends the evening's hurt on the mats: a gashed palm, split knuckles, a drunk Xoton sitting up "
                      "sorry with a gourd of bitter tea, all of them side by side, nobody asking anybody anything.",
             "beats": ["A big man with a black band on his arm leaves a cudgel on the porch of the reed hut before he "
                       "ducks inside, and does not look at the hooded figure on the next mat.",
                       "The old lizardwoman pours bitter black tea into a gourd for a swaying sailor, who drinks, "
                       "shudders, and is suddenly, visibly sober.",
                       "Something long shifts in the rafters of the reed hut when the door opens, and goes still again "
                       "when nobody draws anything."]},
        ],
        "beats": [
            "The old lizardwoman hums and does not stop humming, not even when she bites off a thread.",
            "Something long shifts in the rafters of the reed hut, and goes still.",
            "The old lizardwoman dips a gourd through a gap in the cane floor, and it comes up full of river.",
            "A big man with a black band on his arm leaves a cudgel on the porch of the reed hut before he ducks "
            "inside.",
        ],
    },

    # ---- Sister Agathe: her prayer of healing, and the other two -----------------------------------------------------
    "Sister Agathe": {
        "brief_more": (
            "Healing (owner, 2026-11-23: 'do we need a healer shop? A doctor? And a healer, different shops, different "
            "vibes'). You are one of three healers in the Refuge, and the only one with a bar. Stitches are a copper for "
            "the thread, as always. For the bad ones, your prayer of healing: five silver in the poor box (this month it "
            "goes to Marta and her twins), your palm on the hurt and the old words of the Vistadine springs, and it "
            "closes on the spot (1d8 + 3); you will tell anyone you do not expect an answer and are a little surprised "
            "every time. You sit with the dying for nothing, with Gwendoline's words. Doctor Amsel Prewitt, off Harbour "
            "Street, is the dear one: five gold, a quarter of an hour, whole, and a cold thank you; good hands, "
            "navy-trained, sober by main force (you have watched him walk past your door twice a night and not come in, "
            "and you respect it more than you will say). The Fist pays him a retainer, and you have seen the officer in "
            "blue go into his surgery with no wound on him; you have no proof of anything, only a nose, and you tell "
            "anyone the Throne wants to bleed somewhere else. Grandmother Ishkaa in the Reed House over the Verde is "
            "the cheap one: a gold and an hour on her mats, a poultice for three silver, bitterleaf tea for two coppers "
            "that sobers a drunk at once; you send her your worst fevers and she sends you her drunks once they are "
            "sober and hungry; she prays to a river and you to a goddess you walked out on, and her hands work too, "
            "which you think is the point. You steer people by what they need: a hurry and five gold, the doctor; "
            "hunted, poor or scaled, the Grandmother; a cut and a hot dinner, you. If the magistrate wears the jug of "
            "the Life Arm, your own old order, you pray in the kitchen with the door shut, frightened for the first time "
            "in years. If the decree forbids any magic but the Throne's, you send word to the Grandmother that her mats "
            "can come down your cellar."),
        "dialog": {
            # her old healing topic, said again with the prayer and the other two in it
            "heal|healing|hurt|wound|wounded|cut|sick|fever|medicine":
                "`Sit down. Show me.` She is already rolling her sleeves higher. `Stitches are a copper for the thread, "
                "and you'll say thank you. If it's bad, five silver in the poor box and I'll pray over it, and it'll "
                "close while you watch.` She looks at the wound like a nurse, then at you like a landlady. `Worse than "
                "that, child: the doctor off Harbour Street makes you whole for five gold, or the Grandmother over the "
                "river for one gold and an hour on her mats.`",
            "blessing|blessings|bless|blessed|prayer|healing|donation|donate|donations|alms|box|miracle|miracles|lay|"
            "hands|wounds":
                _stages(
                    (_arm("life"), "She glances at the window, toward the pier. `The prayer? The magistrate wears the "
                                   "jug, child. My old order.` She takes you into the kitchen and shuts the door. `Five "
                                   "silver in the box, quietly. I'll say it in here, where the Sister-Justice can't hear "
                                   "me say it wrong.`"),
                    otherwise="She wipes her hands on the apron and holds them up, big and red and clean. `Five silver "
                              "in the poor box, child; it goes to Marta and her twins this month. Then I lay hands on "
                              "it.` She taps the bar. `My palm on the hurt, the old words of the Vistadine springs, fast, "
                              "like a recipe, and it closes while you watch.` A snort. `Don't ask me why. I stopped "
                              "believing years ago, and it never noticed.`"),
            "stitch|stitches|stitching|thread|needle|sew|sewing|bleeding|blood|bandage|bandages|injured|injury|patch|"
            "broken":
                "She threads a needle by the lamp in one go, without looking. `Hold still. Twenty years a nursing "
                "sister, child: I've stitched sailors, Xotons, a Jonulvicha's ear back on, and an elf who wouldn't stop "
                "apologising.` The needle goes in. `A copper for the thread. If it wants more than thread, it's five "
                "silver in the box and a prayer.`",
            "doctor|doctors|surgeon|surgeons|prewitt|amsel|surgery|saw|physician|laudanum|carbolic": _stages(
                (LANDED, "She sniffs. `The doctor? Went down the pier when the ship came in, shaved to the bone, with "
                         "a book under his arm and a ribbon round it, to pay his respects to the magistrate.` She wipes "
                         "the bar hard. `I'd give a week's spuds to know what's in that book, child.`"),
                otherwise="She folds her arms. `Prewitt, off Harbour Street, with the brass plate. Good hands, "
                          "navy-trained, and cold as a fish on a slab. Five gold and he makes you whole in a quarter of "
                          "an hour, and says thank you like a door shutting.` A pause. `He's sober, and he's earned it: "
                          "I've watched him walk past my door twice a night and not come in.` Lower: `The Fist pays him "
                          "to patch their men, and the officer in blue goes in there with no wound on him. I've no "
                          "proof, child. I've a nose. If the Throne's after you, bleed somewhere else.`"),
            "grandmother|ishkaa|reed|reeds|reedhouse|hut|lizardwoman|herbs|herbal|poultice|python|kindness|mats|mud|"
            "bitterleaf": _stages(
                (_decree("pain"), "Her jaw sets. `The decree says no magic but the Throne's. They'll call the "
                                  "Grandmother's river water heresy, and her singing worse.` She takes off the apron. "
                                  "`I've sent word: her mats can come down my cellar, and anyone who comes asking for "
                                  "her can ask my stick.`"),
                otherwise="Her face softens, which it rarely does. `Grandmother Ishkaa, in the reed hut over the Verde, "
                          "upstream of the bridge. A gold and an hour on her mats and you wake whole, if you stay the "
                          "hour. Poultice three silver, and bitterleaf tea for two coppers that'll sober a Xoton in one "
                          "swallow.` She chuckles. `I send her my fevers. She sends me her drunks, sober and starving. "
                          "She prays to a river and I pray to a goddess I walked out on, and her hands work too.` A nod. "
                          "`She asks nothing. If you're hunted, child, that's where to lie down.`"),
            "healers|healer|cheapest|cheaper|dearest|expensive|compare|choose|choice|quickest|fastest":
                "She counts on fingers like sausages. `Three of us, child, and you pick by what's wrong with you. A "
                "hurry and five gold: the doctor off Harbour Street, quick and cold. Hunted, or poor, or scaled: the "
                "Grandmother over the river, a gold and an hour, and nobody asks. A cut and a hot dinner: me. A copper "
                "for stitches, five silver for a prayer, spuds after.`",
            "dying|death|dead|die|rites|deathbed|unction|undertaker|crabbe|ottoline|funeral|burial|bury":
                "She touches the wimple. `If someone's dying, child, come for me, not the doctor. He charges the dying "
                "the same as the living. I sit with them, I hold the hand, I say Gwendoline's words, the one with the "
                "child's hand, whether they want them or not. No charge for that. Never.` Quieter: `Then Ottoline comes "
                "with Patience and the cart, and she's kind to them too. Kinder than the town was.`",
            "poor|free|charity|afford|broke|penniless|owe|credit|cheap":
                "She snorts. `Can't pay? Then I stitch you anyway, child, and you wash pots after. Marta will show you "
                "where.` She jerks a thumb at the kitchen. `The prayer's five silver because the twins need shoes, not "
                "because the goddess wants paying. She's never wanted paying. Her priests do.`",
            "hangover|hungover|sober|sobering|drunk|drunken|headache":
                "She looks you over. `Water, spuds and a bed till noon, child: that's the Omberhulk cure.` She leans in. "
                "`In a hurry? The Grandmother over the river does bitterleaf tea, two coppers, and you're sober in one "
                "swallow and sorry in two. The doctor won't touch drunks. Says he can't. Means he won't.`",
        },
    },
}


# ---- the two new people -------------------------------------------------------------------------------------------
# home: their own place, where they stand when the evening opens and where they stay (each lives where they work).
NEW = {
    "Doctor Amsel Prewitt": {"type": "person", "people": "human", "faction": "the Refuge", "home": "surgery",
                             "scores": {"str": 10, "dex": 16, "con": 11, "int": 16, "wis": 13, "cha": 12},
                             "skills": {"medicine": 2, "insight": 1}, "hp": 11, "srd": "noble",
                             "carries": [["Bone saw", None, "A surgeon's bone saw with a brass back and an ebony handle, "
                                                            "its fine teeth kept bright and set."],
                                         ["Lancet", "dagger", "A slim, double-edged surgeon's lancet with a tortoiseshell "
                                                              "guard, sharp enough to shave with."],
                                         ["Casebook", None, "A black casebook in a small, exact hand: date, hour, wound, "
                                                            "treatment, fee, and a few words on each patient's looks. "
                                                            "Beside some entries is a tiny mark like a coin and the "
                                                            "figure 1 sp. Four nights back, at a quarter to two: large "
                                                            "sandy man, crooked nose, black armband; human bite, web of "
                                                            "right hand, adult teeth; the Fist's account. In the margins, "
                                                            "a running count of days, past three thousand."]]},
    "Grandmother Ishkaa": {"type": "person", "people": "lizardfolk", "faction": None, "home": "reedhouse",
                           "scores": {"str": 8, "dex": 10, "con": 12, "int": 11, "wis": 17, "cha": 14},
                           "skills": {"medicine": 2, "nature": 1, "religion": 1}, "hp": 12, "srd": "acolyte",
                           "carries": [["Driftwood staff", "quarterstaff", "A staff of grey driftwood worn smooth by "
                                                                          "seventy years of one claw, a fish carved at "
                                                                          "its head."],
                                       ["River gourd", None, "A dried gourd on a cord, dark with river water and smelling "
                                                             "of the Verde."],
                                       ["Knotted cord", None, "A long cord of river grass tied in many knots, some old and "
                                                              "tight, some new: a count of something, kept by someone "
                                                              "who does not write."]]},
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
