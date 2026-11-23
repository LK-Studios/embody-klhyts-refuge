"""Power and agency for the three who run the Refuge (owner, 2026-11-23: "Key NPCs need power and agency. Deepen gog,
klyht, etc. Custodian"; "I am finding NPCs are shallow still").

Merged over a_powers.py, d_vorkath.py, e_faith.py, f_peril.py and g_gog.py: a dialog key given here with the same text
replaces that topic, None retires one, a new key adds one. Topics read the news newest first (the verdict, the decree,
the magistrate's Arm, the sail, Klhyt home or dead, the night), and each line does something: a price, an offer, a name,
a place, a demand. Retired keys are the over-broad ones ("up", "town", "notice", "house", "throne" in the wrong topic)
and the ones that bundled two people's business; each comes back split, with the words players type.

The Custodian buys before he threatens and deals in four things (coin, a post, the Throne's pardon, a berth to Catan);
Dominico would rather own a dangerous stranger than bury one; Fat Gog's power is his people and what the town owes him.
"""

# invented: the Custodian: his version that Klhyt was a prisoner of the Throne, lawfully detained for transport and
#   "watered twice a day, unharmed"; his four offers (coin, a post under the Throne, the Throne's pardon, a paid berth to
#   Catan with ten gold to land on); the lemon-tree house is white, above the Long Quay at Catan, with a kitchen table
#   nobody can take; forty pages written for the magistrate; the Pleasure magistrate's five gold in a velvet purse; he
#   wrote to the Catan workhouse for a ship for the street children; removed, he says he will write letters from a cell
# invented: Dominico: the ring came out of a wreck in a box of wet Xoton books ("the books were ruined, the ring
#   wasn't"); at twelve he put the purse thief down with a mooring pin; he hires dangerous strangers at two silver a
#   night (five if worth it) and a black band; Ott told him the crate coughed; he warns the Throne off leaning on Tully
# invented: Fat Gog: before the town he ran salt and rum between the Meters and the Xoton traders; a Mandrill envoy from
#   Calak Mul once asked him to stand with them when the calling comes ("towns burn"); River keeps a crock of salted eel
#   for him; he has noticed Marlo will not meet his eye; he saw the siren out past the breakers the day he found Klhyt;
#   removed, he goes down to the pier to watch the Custodian go in irons and says nothing
# canon used: Calak Mul (Calakmul), the temple city of the Mandrills, the blue ruling Lizardfolk, to the north
#   (LoreKeeper: "A-Z Shalamar", "Naming the Lizardfolk Factions of Shalamar"); the Final Testament (Annabella Rand)


def _st(*steps):
    """News in stages, newest first: (if_state, line) pairs, then the line for before any of it."""
    *pairs, entry = steps
    for cond, line in reversed(pairs):
        entry = {"if_state": cond, "line": line, "else": entry}
    return entry


REMOVED = {"verdict": "removed"}
UPHELD = {"verdict": "upheld"}
LANDED = {"magistrate_landed": True}
SIGHTED = {"magistrate_sighted": True}
DISGRACED = {"disgraced": True}
HOME = {"klhyt_home": True}
DEAD = {"klhyt_dead": True}
SHIPPED = {"klhyt_shipped": True}
HIT = {"guild_hit": True}
BACKED = {"backed_off": True}
KNOWS = {"gog_knows": True}


def arm(name, **more):
    d = {"magistrate_arm": name}
    d.update(more)
    return d


def decree(name):
    return {"decree": name}


# ---- The Custodian ---------------------------------------------------------------------------------------------------

CUSTODIAN = {
    # replaced (same key), now in stages
    "name|names|called|introduce|yourself": _st(
        (REMOVED, '''He looks at his irons. "The Throne will have written something in its book against my office. A number, I expect. Numbers were always my gift."'''),
        (UPHELD, '''He touches the seal on its ribbon. "The Custodian of Klhyts Refuge, under the Throne's seal, confirmed in office. The man remains a detail."'''),
        (DISGRACED, '''"I am the Custodian of the Refuge, by commission of the Throne of Vorkath." He touches the sigil at his collar. "The man is immaterial. Remember the office."'''),
        '''"I am the Custodian of Klhyts Refuge." Half a smile. "The office is what matters. The man is a detail."'''),
    "hello|hi|hey|evening|ahoy|greetings|howdy|morning": _st(
        (REMOVED, '''He lifts his wrists an inch, as far as the irons allow, which is exactly as far as courtesy requires. "Good day. You will forgive me if I do not rise. The Throne has views on my rising."'''),
        (UPHELD, '''"Good day." The door stands open behind him, and he wants you to notice it. "Petitions in the morning, complaints in writing, and thanks at any hour. Which have you brought?"'''),
        (dict(LANDED, **DISGRACED), '''"Good day. The magistrate is ashore, as you will have seen." He does not get up. "If you have come to make your peace with the Throne, you are a day early and very welcome. If not, the door is behind you."'''),
        (dict(SIGHTED, **DISGRACED), '''He is buttoning his good coat. "Good day. Forgive me: there is a sail at the harbour mouth, and I mean to be the first voice it hears."'''),
        (DISGRACED, '''He does not get up. "Good day. If you have business with the Custodian, state it. If you have business with the mayor, he is in the square, making speeches. If you have something to sell, I am buying."'''),
        '''"Good evening." He inclines his head exactly as far as courtesy requires. "How may the Town Hall help you? It helps a great many people, for a consideration."'''),
    "news|rumour|rumours|gossip|word|heard|happening": _st(
        (REMOVED, '''He looks at the irons, then at the window. "The news is that the Throne has taken an inventory, and I was on it." A thin smile. "Read the decree on the square. It is the news for the next hundred years."'''),
        (UPHELD, '''"The news?" He taps the seal. "The Throne has spoken, and the Refuge is a colony again, whatever is painted on the hall wall. Read the decree. I shall be reading it aloud every morning, in case anyone missed it."'''),
        (dict(LANDED, **DISGRACED), '''"A magistrate of the Throne is ashore, and has my account, in full, in my own hand." He squares his papers. "Ten tomorrow, in this hall. The whole town is welcome. The whole town will learn something."'''),
        (SIGHTED, '''"There is a sail at the harbour mouth with an octogram on it the size of a house." His hands are quite steady. "That is the news. Everything else you have heard this week is about to become history."'''),
        (DEAD, '''"The mayor is dead." He says it carefully, like a man setting down something hot. "Regrettable. The magistrate will want to know by whose hand. So, I assure you, do I."'''),
        (DISGRACED, '''"Here is news." He lays a finger on a sealed letter. "A magistrate of the Throne sailed from Landfall at midsummer. They are due within the week. When they land, we shall all learn whose town this is."'''),
        (SHIPPED, '''"The news is that the tide went out at one, as tides do, and took a good deal of nonsense with it." He smiles with his whole mouth. "Harbour dues payable at the Town Hall, as usual."'''),
        '''"The Town Hall issues news on the notice board in the square. The mayor is upriver. The dues are in order. That is the news."'''),
    "klhyt|mayor|founder|missing|upriver": _st(
        (REMOVED, '''"Klhyt has his town back." He looks at the irons on his wrists. "Let him see how much of it the Throne leaves him. He will find a decree a heavier thing to carry than a grudge."'''),
        (UPHELD, '''"The castaway may go on being mayor of the pump and the pubs, by the Throne's indulgence." He smooths the ribbon at his throat. "The harbour, the tithe and the law are the Throne's. He has learned the difference. Publicly."'''),
        (DEAD, '''"The mayor is dead, and I am sorry for it." Something in his face says he means part of that. "I wanted him to lose, not to die. Dead men make very poor losers. The town will make a saint of him, and saints are terrible for business."'''),
        (dict(LANDED, **DISGRACED), '''"He has a speech. I have a commission." He lays a hand on a thick sheaf of paper. "At ten tomorrow we shall learn which the Throne prefers. I know which I would bet on, if I were a betting man."'''),
        (DISGRACED, '''"Klhyt." The name is a small, dry sound. "A castaway who washed up on the Throne's coast and forgot whose coast it was. He may tell the square what he likes. He will tell the magistrate the same, and the magistrate will ask him for his commission. He has none."'''),
        (SHIPPED, '''"Upriver," he says. "Or downriver. Or out to sea. Rivers are confusing things." He blots a line. "The Refuge runs perfectly well without him. Look about you."'''),
        '''"The mayor is upriver on town business. Delicate negotiations. I keep the Refuge running in his absence, as he would wish."'''),
    "dominico|fist|enforcer|peace": _st(
        (REMOVED, '''"Dominico." He almost laughs. "I paid that man a gold a night for four years, and he folded at the first shout from the square. Do tell him I have no further use for his knuckles. He will hear it more kindly from you."'''),
        (UPHELD, '''"He will come back with his hat on his knee, asking. They always come back to the man with the seal." He makes a note. "I shall let him ask. Asking, I believe he says, is the polite part."'''),
        (DISGRACED, '''"Dominico took the Throne's coin for four years and folded at the first shout from the square." His fingers find his keys. "Loyalty bought by the night is a lease, not a sale. I have not renewed it. The Throne has officers of its own in this town, and more on the sea."'''),
        '''"Dominico keeps the peace. I find it best not to ask how." A small pause. "He also wants a great deal more than the peace. Men who want things are very easy to pay."'''),
    "teague|harbourmaster|count|counting": _st(
        (REMOVED, '''"The harbourmaster counted. The magistrate listened." He turns the irons over. "I never could abide a man who counts twice."'''),
        (UPHELD, '''"Harbourmaster Teague will keep his post, if he learns to count once." A neat pause. "The Throne has room for a quieter harbourmaster. I have one in mind. It could be you."'''),
        (DISGRACED, '''"Harbourmaster Teague keeps a second tally, I am told, in a fishing licence book." He does not blink. "Forging the Throne's accounts is a crime under the Throne's law. I mention it only so that he can stop. Do pass that on. Kindly."'''),
        '''"Harbourmaster Teague is a diligent man. Diligent men make very good harbourmasters and very poor company."'''),

    # retired: over-broad or bundled; each comes back below, split
    "work|job|jobs|hire|employ|duties|town|refuge": None,
    "doing|busy|up|plans|plan|errand": None,
    "gog|fat|guild|stripperwitch|booth|red|velvet|house|dangerous": None,
    "crate|warehouse|tide|emerald|catan|devito|ship|ships|cargo": None,
    "bribe|price|deal|gold|pay|paid|purse|offer|silence|proof": None,
    "lamp|lamps|lamplighter|tallow|notice|notices|board|workhouse|children": None,
    "dues|harbour|tally|tallies|money|accounts|ledger|skim|skimming|strongbox|tithe|charter": None,
    "study|office|key|keys|locked|door|hall": None,
    "magistrate|magistrates|judge|justice|court|hearing|trial|mainland|sail|arrive|arrives": None,
    "vorkath|throne|emperor|melenkovis|empire|faith|god|arms|eight|sigil|church": None,
    "voss|officer|lieutenant|uniform": None,
    "rosa|quint|constable|constables|watch|guard|guards|harrow|fitch|sergeant": None,

    "work|job|jobs|hire|hiring|employ|employment|duties|duty|wage|wages|pay|paid|loyal|serve": _st(
        (REMOVED, '''"I have no work to offer. I have, it seems, no work." He considers the irons. "Ask the magistrate. They are hiring."'''),
        (UPHELD, '''"The Throne is hiring." He slides a sheet of good paper across the desk. "Constables who stay bought, a harbourmaster who counts once, a clerk with a good hand. The pay comes on time now. Sign, and you are the Throne's. Refuse, and you are merely a visitor."'''),
        (DISGRACED, '''"There is work, for the loyal." He squares a stack of papers. "A silver a night to stand at this door beside Constable Quint. A post under the Throne for anyone who stands with me at the hearing. Ten gold for a certain kind of paper. Choose your rate."'''),
        '''"I keep the Refuge running in the mayor's absence: the dues, the watch, the lamps, the Throne's correspondence." He looks you over. "The Town Hall sometimes needs discreet people for small errands. Discretion pays a silver. Indiscretion costs a good deal more."'''),
    "doing|busy|plans|plan|errand|tonight|today|waiting": _st(
        (REMOVED, '''"Waiting for a tide." He considers the irons. "I find I do not care for it."'''),
        (UPHELD, '''"Petitions at nine, the decree at ten, dinner at seven, and the Stripperwitch with the door wide open at ten at night." He smiles with his whole mouth. "I have stopped pretending I do not go. The Throne does not pretend."'''),
        (dict(LANDED, **DISGRACED), '''"Preparing." He lays a hand on a sheaf of pages. "Forty pages for the magistrate, in a fair hand, each one true in every particular I chose to include. Ten tomorrow. Do come."'''),
        (dict(SIGHTED, **DISGRACED), '''"Going down to the pier." He is already buttoning his coat. "It is a courtesy to be the first voice a weary traveller hears."'''),
        (DISGRACED, '''"Waiting." He says it as if it were a skill. "Writing to the magistrate. Reading the Throne's proclamation from the steps at ten. Dining at seven with the lieutenant. Watching the harbour mouth at dawn for a sail. The Throne is patient. I can be patient too."'''),
        '''"Correspondence. Accounts. A glass of something later, somewhere very respectable." He checks a watch on a chain. "Time and tide, as they say."'''),
    "town|refuge|colony|colonies|settlement|outpost|runaways": _st(
        (REMOVED, '''"A colony of the Throne, with a pump, six taverns and a decree." He looks out of the window. "It was very nearly mine."'''),
        (UPHELD, '''"A colony of the Throne, as it always was." He lifts the seal an inch. "Now it knows it. Knowing is so much more restful than pretending."'''),
        (DISGRACED, '''"A town of runaways who ran onto the Throne's own coast and painted nine articles on a wall to keep the Throne out." He smiles thinly. "Paint is not a wall. The magistrate will explain the difference."'''),
        '''"Klhyts Refuge is a sweaty, loud, magnificent mess, and somebody must keep its accounts." He straightens a paper. "Six taverns, one pump and one honest ledger. Mine."'''),
    "gog|fat|lizardman|lizardmen|lizard|lizards|lizardfolk|meters|guild|shadows": _st(
        (REMOVED, '''He keeps his eyes on the floor. "The lizard will be on the pier when they put me aboard. He will not say a word." A breath. "He will not need to."'''),
        (UPHELD, '''"The lizard keeps a tavern. The Throne keeps a law for taverns now." A thin smile. "I am told his house is very beautiful. I shall see for myself, through the front door, with the seal on."'''),
        (DISGRACED, '''"He has not come out of his house," he says, a little too quickly. "When he does, I shall be behind a barred door with a constable on it and the Throne's law in my coat." Something moves behind his face and is put away. "The lizard keeps a tavern. The Throne keeps a law. One of those will be standing when the magistrate leaves."'''),
        '''"Fat Gog is a businessman. I have never set foot in his establishment." A pause. "Never." His eyes go, for no reason, to the window. "The guild's money would be safer in the Town Hall's keeping. Dominico agrees. The lizard will come round to it, or be come round."'''),
    "stripperwitch|booth|velvet|river|barkeep|curtain": _st(
        (REMOVED, '''"I shall miss the wine." That is all he says about it.'''),
        (UPHELD, '''"I go every night now, with the curtain open." He smiles with his whole mouth. "The Throne does not skulk. The woman behind the bar still does not charge me. I have decided to call it a tithe."'''),
        (DISGRACED, '''"I am told I used to drink there, in a booth with a curtain." He does not blink. "I am told a great many things. The woman behind that bar brings wine nobody ordered and hears things nobody said. I should be careful what I said in front of her, if I were you. I always was."'''),
        '''"I have never set foot in the Stripperwitch." He smiles with half his mouth. "Whatever you may have heard about a booth. Or a curtain. Or wine I did not pay for."'''),
    "crate|crated|warehouse|bonded|cargo|kidnap|kidnapped|kidnapping|abducted|abduction|prisoner|box|tide|nailed": _st(
        (REMOVED, '''"The Throne weighed my account of the warehouse against a castaway's." He looks at his irons. "I shall travel with rather more courtesy than he did, I expect. There is a cabin. I am told there is a cabin."'''),
        (UPHELD, '''"The detention of a man obstructing the Throne's tithe was found lawful." He touches the seal. "I believe the word you are looking for is vindicated."'''),
        (DISGRACED, '''"A man obstructing the Throne's tithe was detained in the bonded warehouse, watered twice a day, for transport to answer for it." He says it like a line in a ledger. "Lawful detention. Whoever let him out stole a prisoner of the Throne, and the Throne's warrant will say so on the square by morning."'''),
        (SHIPPED, '''He checks his watch, puts it away, and smiles with his whole mouth. "Ships come and go. That is what harbours are for."'''),
        '''"Cargo is the harbourmaster's concern. I sign for things. I do not open them."'''),
    "catan|lemon|lemons|tree|trees|villa|garden|dream|dreams|retire|retirement|someday|devito|emerald|danny|ship|ships": _st(
        (REMOVED, '''"There is a white house in Catan with lemon trees in the yard, and a table nobody can carry out." He looks at the irons. "I paid for every tree. I shall never sit under one."'''),
        (UPHELD, '''"Catan?" He smiles with his whole mouth. "Why should I go to Catan now? The lemon trees can wait. They are very patient trees."'''),
        (DISGRACED, '''"Catan." For a moment he is somewhere else. "A white house above the Long Quay, lemon trees in the yard, a kitchen table nobody can take away." Then he is back. "A clerk's daydream. The small captain carries my letters there. Only my letters."'''),
        '''"Catan is a civilised port. Captain DeVito carries the Town Hall's correspondence there on the Emerald Eye, and asks no tiresome questions." Half a smile. "One day I should like a house there. Lemon trees. A table nobody can take away."'''),
    "passage|berth|berths|voyage|escape|leave|leaving|sail|sailing|away|depart|fare": _st(
        (REMOVED, '''"I have a berth of my own now, in the black ship's hold." He does not smile. "I do not recommend it."'''),
        (UPHELD, '''"Passage?" He takes out a purse. "The Throne will happily see you on the next ship for Catan: two gold for the berth and ten to land on. The offer is good for as long as the warrant is."'''),
        (DISGRACED, '''"Two gold buys a berth to Catan through the woman at the Turtle." He sets a purse on the desk and leaves his hand on it. "I will pay it, and ten more to land with, if you are on the next tide and never trouble this harbour again. A pardon goes with you. Strangers should not die in other people's quarrels."'''),
        '''"Passage to Catan is two gold, booked at the Turtle Dragon." He looks at you a little longer than courtesy requires. "If the Refuge disagrees with you, the Town Hall can sometimes help with the fare. It likes its visitors to leave as cheerfully as they came."'''),
    "offer|offers|bribe|bribes|price|deal|deals|bargain|purse|gold|silver|coin|money|buy|bought|arrangement|reward": _st(
        (REMOVED, '''"I have nothing left to offer." He considers it. "The strongbox was the Throne's, the seal was the Throne's, the purse is the magistrate's. I find I was holding everything for someone else."'''),
        (UPHELD, '''"Everyone has a price, and the Throne can afford most of them now." He opens a drawer. "Coin, a post, a pardon or a berth. Name which. I am in a generous mood, and I keep receipts."'''),
        (DISGRACED, '''"Everyone in this town has a price, and most of them are embarrassingly low." He lays a hand on his coat. "I deal in four things: coin, a post under the Throne, the Throne's pardon, and a berth to Catan. Ask me about any of them. And if you have paper I want, show it to me. Privately."'''),
        '''"Everyone in this town has a price, and most of them are embarrassingly low." He lays a hand on his coat, where a purse would sit. "Five gold buys a great deal of forgetting. If you have something you think I want, show it to me. Privately."'''),
    "pardon|pardons|amnesty|clemency|mercy|forgive|forgiven|forgiveness|lift|lifted|cleared": _st(
        (REMOVED, '''"Mercy belongs to the Throne now. Ask the magistrate." He holds up his irons. "I did."'''),
        (UPHELD, '''"The Throne's pardon is mine to give, under the seal." He dips a pen. "It costs more now that it is worth more. A paper, a name, or your back on the next ship."'''),
        (DISGRACED, '''"The Throne's warrant is written in my hand, and lifted by it." He dips a pen and waits. "A pardon costs one of three things: a paper I want, a word for me at the hearing, or your back on the next ship. Any one of the three. I am not greedy, only thorough."'''),
        '''"A pardon?" Half a smile. "For what? Have you done something the Town Hall should know about? Do tell me. I am very understanding, by appointment."'''),
    "office|post|position|appointment|appointed|deputy|title|rank|promotion|career|clerk": _st(
        (REMOVED, '''"My office is the magistrate's to fill now." He looks at the desk he is no longer behind. "Whoever sits there will learn what I learned: the chair is very comfortable, and it belongs to someone else."'''),
        (UPHELD, '''"The Throne needs officers." He slides a sheet across the desk. "A harbourmaster who counts quietly. Constables who stay bought. A deputy with a good hand. Sign, and wear the octogram where people can see it."'''),
        (DISGRACED, '''"When the magistrate confirms me, the Throne will need officers here." He studies you. "Constable, with a coat that fits and pay that comes on time. Harbourmaster, if the present one cannot learn to count once. My deputy, for someone with a good hand. Stand with me at the hearing, and choose."'''),
        '''"The Town Hall has vacancies for the discreet." He makes a small note. "Clerk, constable, collector. The pay is modest. The opportunities are not."'''),
    "papers|paper|letter|letters|page|pages|document|documents|evidence|proof|blotter": _st(
        (REMOVED, '''"The magistrate read everything." He looks at the irons. "Paper was always going to be the end of me. I simply expected it to be my own."'''),
        (UPHELD, '''"The magistrate has read everything. Paper no longer interests me." He smiles with his whole mouth. "Burn what you like. I recommend it for the chill."'''),
        (DISGRACED, '''"Paper is the only thing in this town I pay well for." He lays both hands flat on the desk. "A letter in the mayor's hand. A page from the Turtle's passage book. A thin tally book that ought to be in my office and is not. Put any one of them into my hand before the magistrate sees it, and I pay ten gold and forget your face."'''),
        '''"Town Hall papers have a way of wandering, in a town like this." He smiles with half his mouth. "I pay a finder's fee for anything with the Town Hall's business on it. Letters. Tallies. Pages. Bring them to me, not to the square, and the fee is generous."'''),
    "dues|tally|tallies|accounts|ledger|ledgers|skim|skimming|skimmed|figures|sums|books|harbour|sign|signs|signed|signature": _st(
        (REMOVED, '''"Forty-one, forty-six, fifty-two collected. Twenty-nine, twenty-seven, twenty-four lodged." He says the numbers like a prayer. "I always could add. That was the trouble."'''),
        (UPHELD, '''"The dues are the Throne's tithe, collected under the Throne's seal." He taps the ribbon. "I sign every tally, as I always did. Only now nobody asks where the rest went. It went where the Throne says it went."'''),
        (DISGRACED, '''"Withheld." He does not blink. "The Throne's tithe on a colonial harbour, held back under the charter, as any Custodian must. I signed every tally; I sign everything. The mayor would know it if he had ever read the charter. The magistrate has read it."'''),
        '''"The harbour dues are in perfect order. I sign every tally myself." He smiles with half his mouth. "The harbourmaster counts, I sign, the strongbox keeps. A very simple system."'''),
    "tithe|tithes|charter|article|articles|law|laws|lawful|legal|legally|rights": _st(
        (REMOVED, '''"The magistrate found the Charter on the wall a sweet piece of penmanship and my tithe a fiction." He turns the irons. "I was right about the Charter."'''),
        (UPHELD, '''"The tithe is the Throne's, by the seal, and the Charter on the hall wall is a painting." He folds his hands. "I have asked the constable to leave it up. People should be reminded what a wish looks like."'''),
        (DISGRACED, '''"Every harbour on a coast the Throne has claimed owes it a tithe of its dues, and its Custodian holds that tithe until a magistrate collects it." He taps the desk once. "The mayor's Charter is nine articles painted on a wall by a castaway. Article One: nobody shall be asked where they came from. The Throne asks everybody. That is what a Throne is for."'''),
        '''"The Refuge has a Charter: nine articles in the mayor's own hand on the hall wall." Half a smile. "A very handsome piece of penmanship. Charters are for founders. Laws are for Thrones. Somebody should mention it to him, gently."'''),
    "strongbox|chest|coffer|coffers|treasury|vault|funds|lodged": _st(
        (REMOVED, '''"The magistrate has the strongbox key now." He looks at the box, and then at nothing at all. "It was always lighter than people thought."'''),
        (UPHELD, '''"The strongbox is open for the Throne's business, in daylight, under the seal." He nudges it with his foot. "Every copper accounted for. Eventually."'''),
        (DISGRACED, '''"The strongbox sits at my feet, in the Throne's custody, and opens for the magistrate and nobody else." He does not look down at it, very deliberately. "Not for a mayor, not for a mob, not for a lizard. Try the lid if you like. Constable Quint is paid to dislike that."'''),
        '''"The strongbox keeps the town's money, and I keep the strongbox." His hand rests on the ring of keys. "Simplicity is the soul of honesty."'''),
    "charge|charges|accused|accuse|accusation|accusations|crime|crimes|guilty|innocent|theft|thief|stole|stolen|steal|stealing|embezzle|embezzled|embezzlement|corrupt|corruption|liar|lies|lied|lie": _st(
        (REMOVED, '''"The charge was failing the Throne's trust." He considers the irons. "Not theft. Not the warehouse. Failure. The Throne forgives everything but that."'''),
        (UPHELD, '''"There is no charge. The Throne looked, and found its officer about the Throne's business." A thin smile. "You may stop saying thief in the square now. It is very nearly sedition."'''),
        (DISGRACED, '''"The charge?" He takes off his spectacles and polishes them. "That I kept back the Throne's tithe, as my commission requires, and detained a man who meant to spend it on lamp oil and pumps. I plead guilty to my commission. Write that down; I should like it quoted accurately."'''),
        '''"A charge?" Half a smile. "I am not aware of any charge. Are you? Do tell me who is making it. I keep a list of the town's more imaginative people, for its own protection."'''),
    "confess|confession|admit|truth|honest|honesty|regret|regrets|sorry|apologise|apologize|shame|ashamed|conscience": _st(
        (REMOVED, '''"Regret?" He looks at the irons a long time. "I regret the lemon trees. Everything else was arithmetic."'''),
        (DISGRACED, '''"Confession is a sacrament of the Pain Arm. I am not of the Pain Arm." He smiles with half his mouth. "I have nothing to confess and a great deal to declare, and I shall declare it to the Throne's magistrate, not to a stranger in a doorway."'''),
        '''"The truth?" He looks genuinely interested. "The truth is that the dues are in order and the mayor is upriver. That is the Town Hall's truth. It is the only one with a seal on it."'''),
    "warrant|warrants|wanted|poster|posters|outlaw|outlawed|outlaws|bounty|arrest|arrested|seal|notice|notices": _st(
        (REMOVED, '''"My warrants were the Throne's, and the Throne has withdrawn its confidence in my hand." He shrugs, as far as the irons let him. "Take the notice down, if it troubles you. It will not trouble me."'''),
        (UPHELD, '''"The Throne's warrant stands, sealed twice now." He touches the ribbon. "The lieutenant and the magistrate's guards know the description. I should keep out of the square, if I were the person described."'''),
        (dict(LANDED, **DISGRACED), '''"The magistrate's own guards have read my notice." He straightens a cuff. "Black and silver, spears, and no imagination at all. I should be careful whom I resembled, this week."'''),
        (DISGRACED, '''"The Throne's warrant is a sheet of paper and a seal." He holds the seal up so you can see it. "At two in the morning it goes up on the square on whoever stole the Throne's prisoner out of the bonded warehouse, described as a stranger would describe them. After that the lieutenant and the constable do not ask questions. They do not chase, either. They simply wait for the face."'''),
        '''"Warrants are issued by the Throne's officer, under seal." He touches his breast pocket. "I have not issued one in years. This is a very peaceable town. I should like it to stay that way, for everyone's sake. Yours too."'''),
    "witness|witnesses|testimony|testify|testifies|silenced|intimidate|intimidated|intimidation|visit|visits|visited|calls|calling|threatened": _st(
        (REMOVED, '''"The witnesses spoke, I gather." He looks at his irons. "I should have liked to hear what they said. I am told it was very affecting."'''),
        (UPHELD, '''"The magistrate heard everyone who chose to speak." A thin smile. "Fewer chose to than you might have expected. Courage is a seasonal crop in a harbour town."'''),
        (DISGRACED, '''"Witnesses?" He seems mildly surprised. "The magistrate will hear whoever chooses to speak. I cannot imagine why anyone would choose otherwise." He makes a note. "I sleep at night, as an honest officer does. I cannot answer for the lieutenant's hours. He keeps the Pain Arm's, I believe: early, and late."'''),
        '''"Witnesses to what?" He blinks, pleasantly. "Nothing has happened in this town that needs a witness. I should know. I sign everything."'''),
    "threat|threats|threaten|threatening|warning|warn|consequences|careful|enemy|enemies|kill|hurt|revenge|vengeance": _st(
        (REMOVED, '''"I am in no position to threaten anybody." He considers it. "I shall be in Landfall in a few months, in a cell with a very long memory and a window. I write letters. I always did."'''),
        (UPHELD, '''"I never threaten." He touches the seal. "I write things down, and the Throne reads them. The Throne reads very slowly and forgets nothing. I should go about your business quietly, for as long as you are in its colony."'''),
        (DISGRACED, '''"I do not threaten. Threats are for men who expect to be disobeyed." He writes something small in the margin of a page and does not show you. "I make notes. The magistrate will read them all. You are, I am afraid, in several."'''),
        '''"Threats?" He looks wounded. "The Town Hall does not threaten. It reminds. It reminds very courteously, and then it reminds the watch, and then it reminds the harbourmaster which ships may leave." He smiles. "I am sure we shall never need to remind you of anything."'''),
    "fear|fears|afraid|scared|frightened|nervous|worried|worry|sweat|sweating|crowd|crowds|mob|riot": _st(
        (REMOVED, '''"Afraid? Of a cell with a window, no." He looks out at the black-hulled ship along the pier. "Of a bailiff, a little. They always take the table."'''),
        (UPHELD, '''"Afraid?" He smiles with his whole mouth. "I have the Throne's seal round my neck. Fear is something that happens to other people now." His eyes go to the window all the same, toward a house with red velvet in it.'''),
        (DISGRACED, '''"Afraid?" His hands are quite still on the desk, which takes effort. "Of a mob that cheered a castaway on the steps? Of a lizard in a white suit? I have a barred door, a constable, the Throne's law and a magistrate on the sea." His eyes go to the window anyway. "I sleep very well. I simply sleep with the lamps lit."'''),
        '''"Fear is bad for business, and this town runs on business." He checks the watch on its chain. "I fear nothing but a ledger that does not balance. Mine always do."'''),
    "past|mother|childhood|young|youth|family|rent|bailiff|history|story|poor|poverty|raised": _st(
        (REMOVED, '''"My mother counted the rent on a kitchen table in a cold city, and one winter the bailiff took the table." He looks at the irons. "I swore nobody would ever take a table from me again. They have taken the chair as well. The Throne is thorough."'''),
        '''"My mother counted the rent on a kitchen table in a cold city in Landfall, and one winter the bailiff came and took the table." He says it quite evenly. "I learned two things that night: to add, and that the man who holds the paper takes the table. I have held the paper ever since."'''),
    "throne|emperor|melenkov|arkmady|empire|vorkathia|commission|crown|imperial|mainland": _st(
        (REMOVED, '''"The Throne gives, and the Throne takes back with interest." He looks at his wrists. "The Emperor will never hear my name. I never told it to anyone. Perhaps that was the mistake."'''),
        (UPHELD, '''"The Throne of Vorkath reaches every shore its ships can find." He lifts the seal on its ribbon. "This one it has found twice: once with a clerk, and once with a magistrate. It will not need a third visit."'''),
        (DISGRACED, '''"Emperor Arkmady Melenkov joined three kingdoms into one Greater Vorkathia and sent his missions to the known and unknown corners of the globe." He touches the silver at his collar. "This is an unknown corner, and I am his commission in it. The Throne is patient. I can be patient too."'''),
        '''"I serve the town, and the town is a colony of the Throne, whatever its founder likes to think." He says it lightly, and watches you as he says it. "Landfall's ships would not trade with a harbour that had no Custodian. Ask the mayor who signed my commission. He never read it."'''),
    "vorkath|goddess|god|gods|faith|church|pray|prayer|prayers|religion|worship|believe|octogram|sigil|devout|pious|temple": _st(
        (REMOVED, '''"Vorkath has eight arms, and one of them has let go of me." He turns the irons. "I suppose that is theology."'''),
        (DISGRACED, '''"Vorkath holds a saint's sign in each of her eight hands, and the world in between them." He touches the silver at his collar. "These people ran from her. They ran onto her coast. Faith is patient. So is law. I wear her sign openly now; I find it saves explaining."'''),
        '''"I keep the faith of the Throne, quietly, as a clerk should." He does not touch his collar, and you notice him not touching it. "This town prefers its gods unasked. So, for now, do I."'''),
    "arms|arm|eight|saint|saints|gideon|teflon|percival|loffgren|hester|stanhope|annabella|rand|gwendoline|vistadine|scripture|scriptures|testament|verse|gospel|inquisition|inquisitor": _st(
        (REMOVED, '''"Teflon taught that only hands that bleed come close to her." He looks at the marks the irons have made. "I seem to be making progress."'''),
        '''He recites it as a clerk reads a ledger aloud. "Gideon carried a ball and chain against a god, and won. Percival rebuilt the land after. Teflon taught that only hands that bleed come close to her. Gwendoline takes a sweet to walk you to heaven, and Vistadine washes you on the way in." He folds his hands. "And Annabella Rand, who was blind, wrote the Final Testament: that every soul is written down. Every soul. I find that a great comfort. You may not."'''),
    "magistrate|magistrates|judge|judges|justice|court|hearing|trial|verdict|ruling|patient": _st(
        (REMOVED, '''He looks at the irons on his wrists, and then at you, and says nothing at all.'''),
        (UPHELD, '''"The Throne has spoken." He touches the seal on its ribbon. "Do read the decree. I shall be reading it aloud every morning, in case anyone missed it."'''),
        (arm("war", **DISGRACED), '''"Magistrate-Commander Hale, of the Order of Gideon." He straightens his coat as if for inspection. "A soldier. Soldiers respect a man who holds his post, and I have held mine behind a barred door for a week. Ten tomorrow. I shall stand very straight."'''),
        (arm("peace", **DISGRACED), '''"Magistrate Thorne, of Percival the Builder." He looks at the stack of paper on his desk. "A builder likes paper; he weighs it twice. Mine is forty pages. Theirs is a letter and a tally book." His hand rests on the stack. "I should very much like to know where those are tonight."'''),
        (arm("pleasure", **DISGRACED), '''"Magistrate Merriwether, of Pil's Loffgren, One For The Road." He smiles with his whole mouth. "A man of appetite. I have already seen to his appetite: five gold, as a courtesy, in a velvet purse. The town is welcome to outbid me. The town has never once paid its dues on time."'''),
        (arm("pain", **DISGRACED), '''"An inquisitor. Severin Crake, of the Pain Arm." For the first time this week he seems to relax. "The Inquisition leans to the Throne's officers, as it should. Witnesses do not move an inquisitor; only paper does, and not much of it." He touches the sigil. "Teflon is kind to those who serve."'''),
        (arm("chaos", **DISGRACED), '''"Magistrate-Captain Strand, of Hester-Stanhope, the Fearless." His fingers find his keys and stay there. "She judges as her saint sailed: by the wind and a throw of the dice." He does not smile. "I have never gambled in my life. I find I dislike starting now."'''),
        (arm("destiny", **DISGRACED), '''"Magistrate Quill, of the Blind Savant." He squares his ledgers into a neat pile. "A reader of figures. Figures are my native tongue. Paper weighs double with Quill." A pause. "Everyone's paper."'''),
        (arm("death", **DISGRACED), '''"Magistrate Ashgrove, of Gwendoline." He stops writing. "Death weighs harm. A man detained, watered twice daily, unharmed." He says it to the page more than to you. "Unharmed. I shall say it tomorrow at ten, exactly so."'''),
        (arm("life", **DISGRACED), '''"Sister-Justice Brennan, of the Vistadine Order." His mouth tightens. "She weighs witnesses, I am told, twice over: people who stand up in a hall and speak." He sets down the pen. "In my experience, very few people in this town enjoy standing up in a hall."'''),
        (LANDED, '''"A magistrate of the Throne is ashore, and the Town Hall is at their disposal." He straightens a paper. "I have nothing to fear from a survey. My books balance. They always balance."'''),
        (dict(SIGHTED, **DISGRACED), '''"A sail at the harbour mouth." He is already on his feet. "At sea since midsummer. I shall meet the ship myself. It is a courtesy to be the first voice a weary traveller hears."'''),
        (DISGRACED, '''"A magistrate of the Throne, at sea since midsummer, due within the week." For the first time he smiles with his whole mouth. "I write to them every night, so that the first thing they read on this coast is the truth. Mine. Which Arm they serve will matter more than anything you can carry up that pier."'''),
        '''"The Throne sends a magistrate to the colonies now and then, to see that its law is kept." He straightens a paper. "One is due. I am ready for them. I am always ready."'''),
    "decree|decrees|proclamation|proclamations|census|levy|levies|licence|licences|license|edict|garrison|steps|speech": _st(
        (REMOVED, '''"The decree stands, whoever stands beside it." He looks at the irons. "The Throne did not need me to be cruel. It never does. It needs clerks."'''),
        (decree("war"), '''"Twenty of fighting age for the Throne's crusades, a garrison of the Order, and no spears in Lizardfolk hands." He unrolls a list. "I have begun it already. I started with the men who cheered in the square."'''),
        (decree("peace"), '''"A church on the square, built from the harbour dues." He smiles with his whole mouth. "Do you see? The dues go to the Throne after all. And a book with every name in it, and where they came from. Article One, I think, is repealed."'''),
        (decree("pleasure"), '''"Every tavern buys the Throne's licence, and the Throne takes a copper in ten of every cup." He makes a note. "The Stripperwitch's licence will cross my desk first. I shall read it very carefully."'''),
        (decree("pain"), '''"Every elf in the Refuge surrendered to the Throne, an office of the Inquisition in this hall, and no magic the Throne has not sanctioned." He gestures at the mayor's study. "I have offered them that room. It has a good lock."'''),
        (decree("chaos"), '''"Every ship flies the octogram and pays anchorage, and the elf ship goes home as the Throne's prize." He looks pleased. "The harbour dues will double. I shall sign every tally."'''),
        (decree("destiny"), '''"A census. Every soul, every name, and where each came from, in the Book of Destiny." He lays a hand on a blank ledger. "I shall keep it myself; I have the hand for it. Nobody here will be a stranger again."'''),
        (decree("death"), '''"No sea-burials, no trees, the dead in the church's ground, and blood paid for by whoever spilled it." He blots a line. "The fishermen will grumble. The Throne does not hear grumbling. It hears petitions, in writing, in the mornings."'''),
        (decree("life"), '''"Everyone washed in the goddess's water within the month, and the unwashed out of office, out of the market and out of court." He shows you his clean hands. "I have been washed. I recommend it. It is very much cheaper than the alternative."'''),
        (DISGRACED, '''"At ten every morning I read the Throne's proclamation from the steps: that this harbour is in the Throne's custody, which is mine." He rolls a paper tight. "The magistrate will write a decree. They always do. Nobody here will like it. I shall read that one too."'''),
        '''"The Town Hall posts its notices on the board in the square." He taps a neat stack. "Dues payable as usual. The mayor upriver. Nothing that need trouble a visitor."'''),
    "irons|chains|chained|shackles|removed|downfall|fallen|lose|losing|lost|win|winning|won|outcome|odds": _st(
        (REMOVED, '''"Irons." He holds them up a little, as if offering them for inspection. "The Throne is very thorough with its officers. I always admired that about it, from the other side of the desk."'''),
        (UPHELD, '''"I won." He says it quietly, as if it surprised him. "The Throne confirmed its officer. Remember that, the next time someone in the square calls me a thief. Remember who did not stand up at ten."'''),
        (DISGRACED, '''"Lose?" He seems to consider the word. "The Throne's officer, against a castaway with a painted charter? I am not a betting man. If I were, I should be very rich, and you would be very poor."'''),
        '''"Win what?" Half a smile. "There is no contest. There is only the Town Hall, doing the town's business. Somebody must."'''),
    "hall|townhall|study|key|keys|locked|lock|door|barred|desk|inside": _st(
        (REMOVED, '''"The magistrate's guards have the keys." He looks at his empty belt. "I counted them every night. I find my hands do not know what to do."'''),
        (UPHELD, '''"The Town Hall door stands open now, by day and by night." He smiles. "Do come in. Everyone is welcome to watch the Throne's business done. Petitions at nine."'''),
        (DISGRACED, '''His hand closes over the ring at his belt. "The Town Hall, the strongbox and the keys are in the Throne's custody. Which is to say, mine. Try the door if you like. The constable on it is paid to dislike you."'''),
        '''"The mayor's study stays locked until the mayor returns. I hold the only key, for safekeeping." His hand rests on the ring at his belt.'''),
    "quint|rosa|constable|doorkeeper|bought": _st(
        (REMOVED, '''"Constable Quint stood at my door for a silver a night, until the night the silver stopped." He shrugs. "Honest, in her way. She stayed bought exactly as long as she was paid."'''),
        (UPHELD, '''"Constable Quint keeps my door for a silver a night, and keeps it beautifully." He makes a note. "The only honest woman in the watch: she stays bought. When the Throne promotes, it remembers who stayed."'''),
        (DISGRACED, '''"Constable Rosa Quint keeps my door for a silver a night, and walks with the lieutenant after dark." He does not look up. "The only honest woman in the watch: she stays bought. If you would like her post, I pay the same. If you would like her to look the other way, you will find she charges more than I do."'''),
        '''"Constable Quint? A comfortable woman who leans on things." He makes a small note. "She sells crumbs to the lieutenant and thinks I do not know. I know everything that is sold in this town. I usually know the price."'''),
    "watch|guard|guards|harrow|fitch|sergeant|constable|constables|pell|abel|watchmen|book": _st(
        (REMOVED, '''"The sergeant gave the magistrate his book." He says it without heat. "Every night I paid short, in pencil, in a hand like a child's. I should have paid the old man in full. It would have been cheaper."'''),
        (UPHELD, '''"The watch is the Throne's now, all three of them, paid on time at last." He smiles thinly. "Sergeant Harrow will learn to write less in his book. Young Fitch will learn a new Article One."'''),
        (DISGRACED, '''"The watch is the Custodian's. Some of it remembers that." He glances at the door. "Sergeant Harrow keeps a book and thinks I do not know what is in it; he will give it to the magistrate, and the magistrate will read that I paid him late. Young Fitch recites the mayor's Charter at me. It was never sealed by anyone but a castaway."'''),
        '''"The watch is three good people, paid in full, on time." He says it without a flicker. "Ask them. Ask the sergeant especially. He writes everything down, and I am told he writes very slowly."'''),
    "stranger|strangers|meddle|meddling|meddler|meddlers|newcomer|newcomers|outsider|outsiders|foreigner|foreigners|visitor|visitors|adventurer|adventurers|hero|heroes|interfere|interfering": _st(
        (REMOVED, '''"You came in on a boat and turned a colony over in a week." He studies you without rancour. "The Throne will remember your faces too. It remembers everybody. That was always my job."'''),
        (UPHELD, '''"Strangers come in on one tide and go out on the next, and the Throne stays." He lifts the seal an inch. "You meddled, and lost. There is no shame in it. There is a ship on the next tide."'''),
        (DISGRACED, '''"You strangers come in on one tide, rearrange a town that is not yours, and go out on the next, and the Throne stays." He folds his hands. "I bear you no ill will. I would pay your fare to prove it. But a stranger who stands between the Throne and its tithe is not a stranger to the Throne for long."'''),
        '''"Visitors are very welcome in the Refuge." He smiles with half his mouth. "Visitors who visit. Who drink, and sleep, and buy mangoes, and go. The town has a great deal of patience with visitors who do not mistake themselves for residents."'''),
    "elf|elves|ithriel|unicorn|moonmoth|exiles|refugees|wendeline|heretic|heretics": _st(
        (REMOVED, '''"The elves? I never had any use for them except as a price." He looks at his irons. "The lieutenant will have to buy his seal elsewhere now."'''),
        (UPHELD, '''"The lieutenant still wants the Unicorn searched." He lifts the seal on its ribbon. "This is the Throne's seal now, not a clerk's, and it costs accordingly. If someone made me a better offer for not lending it, I should listen. I always listen."'''),
        (DISGRACED, '''"Lieutenant Voss wants a warrant to search the Touchy Unicorn, under my seal." He weighs the seal in his palm. "I have lent it to him for other things. For that one I have not yet named a price. If someone else wished to buy the seal's silence, they would find me approachable. I am always approachable."'''),
        '''"Elves?" He makes a small, neat note. "The Throne considers them enemies of the state. The Refuge considers them guests. I consider them a question of price, and the lieutenant has not yet named his."'''),
    "voss|officer|lieutenant|uniform|dine|dines|dinner|supper|apothecary|quillon|steak": _st(
        (REMOVED, '''"The lieutenant has not called on me since the hearing." He turns the irons. "The Pain Arm teaches that suffering purifies. I find I am being very thoroughly purified."'''),
        (UPHELD, '''"The lieutenant and I dine at seven, under the window, where the street can see." He touches the seal. "He still wants my seal for the Unicorn. Now that it is the Throne's seal, it costs more."'''),
        (DISGRACED, '''"Lieutenant Voss and I dine at seven at the Apothecary, at his table, not mine." He makes a note. "A faith, a Throne, and a dislike of being kept waiting: we have a great deal in common. I lend him my seal; he lends me his sword. The arithmetic is very simple."'''),
        '''"A Vorkathian officer, here on his own business. I have offered him the town's courtesy and a good table at the Apothecary." He looks at his nails. "He wants a seal on a warrant for the Unicorn. I have not yet named a price. One should never name a price first."'''),
    "lamp|lamps|lamplighter|tallow|workhouse|children|child|orphans|urchin|urchins|wick|beggars": _st(
        (REMOVED, '''"Somebody else will pay for the lamps now." For a moment he looks old. "I did write to the Catan workhouse. Do tell the children the ship is not coming."'''),
        '''"The lamps are lit at dusk and put out at dawn at the town's expense. Considerable expense." He sounds pained. "And the street children would do better in the Catan workhouse. I have written to Catan. They have a ship. When the Throne confirms me, it will call."'''),
}


# ---- Dominico --------------------------------------------------------------------------------------------------------

DOMINICO = {
    # replaced (same key), now in stages
    "hello|hi|hey|evening|ahoy|greetings|howdy|morning": _st(
        (REMOVED, '''"Evening." He does not look up. "The Custodian's in irons, I'm told. Sit down if you're here to talk about who pays the Fist now. Otherwise, don't."'''),
        (UPHELD, '''"Evening." The ring goes round once. "The Custodian kept his chair. Everyone in this town is about to find out who they work for. Sit, or don't. Quickly."'''),
        (HOME, '''"Evening." He looks at you a moment too long, as if checking you against a list. "Sit, or don't. If you're one of the ones who opened that warehouse, sit. We should talk before Sabeth finds you."'''),
        (HIT, '''"Evening." There is a fresh cut across his knuckles. "Sit, or don't. Quickly. It's been a long night for furniture."'''),
        (BACKED, '''He doesn't look up from his glass. "Evening. My men are off the street tonight. Sit, if you've something worth my time."'''),
        '''He doesn't look up from his glass. "Evening. Sit, or don't. Quickly."'''),
    "news|rumour|rumours|gossip|word|heard|happening": _st(
        (REMOVED, '''"The news is the Custodian's in irons and his purse isn't." He turns the ring. "Somebody will be paying the Fist by the end of the week. I'll be choosing who."'''),
        (UPHELD, '''"The Custodian kept his chair, with the Throne's seal round his neck." He sets his glass down. "He'll want his fist back. He can ask. Asking is the polite part."'''),
        (LANDED, '''"There's a magistrate in the Apothecary's best room and two guards in black and silver on the stair." He doesn't look at the stair. "Somebody will ask who carried a crate down a pier. Men who carry things on another man's word should be thinking about that."'''),
        (SIGHTED, '''"A Throne ship in the harbour mouth." He watches the window. "My father served the Throne thirty years and it paid him in rope. Let's see what it pays this town."'''),
        (DEAD, '''"Somebody killed the man who built this town." The ring stops. "It wasn't my order. I want that understood. I want to know whose it was."'''),
        (HOME, '''"The news is that I was used." His ring hand closes. "The man who built this town, in a crate, and they called him a debtor to my face. That will not happen twice."'''),
        (HIT, '''"The news is that Gog's mirror is in pieces and nobody's dead." He flexes a cut hand. "That was the message. He knows how to read."'''),
        (BACKED, '''"The news is that I don't fight other men's wars on a lie." He sets the glass down. "Somebody told me a crate. I'm finding out what was in it."'''),
        (SHIPPED, '''"A crate went out on the tide. Business done." He turns the ring. "Gog's books are next."'''),
        '''"News is what my people tell me before it happens. Tonight it's Fat Gog's books, on this table." He taps the linen once. "The rest is noise."'''),
    "klhyt|mayor|founder|missing|upriver": _st(
        (REMOVED, '''"The mayor has his town. The Throne has its decree." He turns the ring. "Men like Klhyt think a charter on a wall is a wall. He'll learn. I'll still be here when he does."'''),
        (UPHELD, '''"Klhyt is mayor of a pump now, by the Throne's leave." Something like contempt, not for Klhyt. "He was a better man than the one who sits in the Hall. That has never once mattered in the history of the world."'''),
        (DEAD, '''"I put that man in a box on another man's word." His jaw works. "I didn't kill him. Someone did. When I know who, they'll find I keep my word in both directions."'''),
        (HOME, '''"He walked up the Hall steps on his own legs and told the town who robbed it." The ring goes round. "My men carried him down a pier on a lie. I don't apologise for my men. I collect what I'm owed for them, and the Custodian owes me."'''),
        (BACKED, '''"He told me a debtor. Shipped somewhere he could work it off." A muscle moves in his jaw. "Not the man who built this town."'''),
        (SHIPPED, '''"The mayor's upriver. The Custodian says so." He holds your eye a moment too long. "And a crate went out on the tide, paid for in gold by the Custodian's office. Those are two facts. I don't like what they do when you put them together."'''),
        '''"The mayor is upriver on business. The Custodian says so." He holds your eye a moment too long.'''),
    "custodian|patron|paymaster|employer|grey": _st(
        (REMOVED, '''"In irons." He finishes his glass, for once. "Four years he paid me a gold a night to keep his peace, and one night he paid me in a lie. The Throne can have him. It can keep the change."'''),
        (UPHELD, '''"He kept his chair. Good for him." The ring goes round. "He'll need a fist again before the month's out: his constable leans on things and his lieutenant has elves to chase. He'll come and ask. I'll name a price he won't like."'''),
        (HOME, '''"He sits behind a barred door with my peace money in his strongbox and a constable he bought for a silver." He sets his glass down very gently. "He told me a debtor, a crate, and called the founder of this town cargo to my face. I despise being used. I despise being used cheaply more."'''),
        (BACKED, '''"He told me a crate. A crate. Not the man who built this town." He sets his glass down very gently. "The Custodian and I have finished doing business."'''),
        '''"The Custodian keeps the town. I keep the peace. You keep your nose out of both."'''),
    "phillip|everuex|voss|officer|noble|lieutenant": _st(
        (HOME, '''"The man in blue eats steak three tables away and goes out after dark with a constable and the Custodian's seal." He doesn't look. "He calls on people in the small hours. If he calls on mine, he'll find I got there first. The powdered Everuex is still sweating over his woman with the bow. Neither of them is my business until they make it so."'''),
        '''"There's a Vorkathian officer at that table eating steak, and a powdered Everuex at that one, sweating through his coat. One wants elves, the other wants a woman." He doesn't look at either. "Neither is my business, until they make trouble on my street."'''),

    # retired: over-broad or bundled; each comes back below, split
    "work|job|jobs|hire|employ|muscle|recruit": None,
    "doing|busy|up|plans|plan|waiting": None,
    "gog|books|guild|stripperwitch|midnight|ledger|ledgers|want": None,
    "crate|warehouse|brask|debtor|bonded|tide|docks": None,
    "magic|arcana|whispers|whisper|dark|ring|conjuring|spell|spells|voice": None,
    "peace|fist|law|watch|order|violence|harrow": None,
    "master|seat|ambition|future|power|rise": None,
    "money|collection|collect|protection|sabeth|crane|tully|fennick|fennicks|men": None,

    "work|job|jobs|hire|hiring|employ|muscle|recruit|join|joining|wage|wages|pay|paid|band": _st(
        (HOME, '''"I'm hiring." He looks you over properly for the first time. "Not for doors: for people who've shown they can move a man off one. Two silver a night, five if you're worth it, a black band, and nobody in this town follows you home." The ring goes round. "I would rather own a dangerous stranger than bury one. Think about which you'd rather be."'''),
        (BACKED, '''"My men are standing down tonight. Ask me tomorrow, when I've decided who I work for." He looks you over. "If you can hold your tongue and a cudgel, I'll still be hiring."'''),
        '''"I hire men who can follow an order and keep their mouths shut." He looks you over. "Two silver a night and a black band. Most can't do either. If you can, come back after midnight, when I've finished with the lizard."'''),
    "doing|busy|plans|plan|waiting|tonight|today|next": _st(
        (REMOVED, '''"Deciding who pays the Fist." He lays a card face down. "There are three bidders, and none of them knows it yet."'''),
        (UPHELD, '''"Waiting for the Custodian to come and ask." He lays a card face down. "I've decided to be expensive."'''),
        (HOME, '''"Tonight Sabeth is putting out a word, and two of my people are walking it round town." He doesn't say whose name the word is. "I'm sitting here so everyone knows where I was."'''),
        (HIT, '''"Tonight I sent a message through Gog's front door. Now I'm waiting to see if he can read." He lays a card face down. "He can. He's old, not stupid."'''),
        (BACKED, '''"Tonight I'm sitting here with my men off the street, thinking about who lied to me, and what it will cost him."'''),
        '''"Waiting for midnight. Then I stop waiting." He glances at the clock over the stair. "I'm told I'm a patient man. I'm not. I'm punctual."'''),
    "gog|fat|lizardman|lizardmen": _st(
        (HOME, '''"Gog let me be, and I let him be. For now." He turns the ring. "He thinks harmony is a wall. It's a curtain. One day somebody pulls it, and it might as well be me."'''),
        (HIT, '''"I sent him a message at the bell: a mirror, some velvet, two of his people on the floor, nobody dead." Flat. "Next time I won't be so careful. He knows that. That was the message."'''),
        (BACKED, '''"The books can stay where they are. For now." He sets his glass down. "I don't fight other men's wars on a lie. When I take Gog's guild, it'll be my war, on my reasons."'''),
        '''"Fat Gog has had this town's shadows to himself too long." A smile with no warmth in it. "I asked him to share his books. Asking was the polite part. Midnight is the other part."'''),
    "guild|guilds|shadows|underworld|thieves|takeover|master|guildmaster|seat": _st(
        (HOME, '''"The guild's still Gog's." He lays a card face down. "His people are loyal because he's kind. Kindness is a debt that comes due when the money runs out. I'll be there when it does."'''),
        '''"Gog's guild: the quiet money in the taverns, the doors, the fence on Harbour Street, the child in the market." He counts them on scarred fingers. "Run properly, it'd pay ten times what he takes. He doesn't run it. He hosts it."'''),
    "books|book|ledger|ledgers|midnight|bell|ultimatum|deadline|accounts": _st(
        (HIT, '''"He didn't send them. So at the bell my men went through his door instead." The ring turns. "Nobody died. I keep the books on that too."'''),
        (BACKED, '''"His books are his. Tonight." He taps the linen once. "Every ledger in this town ends up on somebody's table. I can wait for his."'''),
        '''"Every ledger, every name, every cut, on this table by the midnight bell." He taps the linen. "Or my men go through the Stripperwitch and he learns what a quiet night costs. He'll send them. Sensible men do."'''),
    "stripperwitch|velvet|hessa|threshold|river|barkeep|doorway|house": _st(
        (HIT, '''"My men went through that door once, at the bell, as a message." He looks at his ring. "I don't send messages twice. The next time anyone in black goes through it, it won't be a message."'''),
        (BACKED, '''"Gog's house. A green lizardwoman on the door with a gaff, and the old man in the back like a hill." He does not smile. "My men don't hunt in there. A man who takes a fight through that door starts a war with every lizard on this coast, and I choose my wars. So if you're running from my people, that's where you'll run. I know. I'll wait outside."'''),
        '''"Gog's house. Red velvet, a mirror the length of the bar, a lizardwoman on the door with a gaff." He looks at the clock over the stair. "At midnight my men go through that door once, if the books haven't come. Once is a message. Twice is a war, and I choose my wars."'''),
    "crate|crated|warehouse|debtor|bonded|tide|docks|cargo|box|nailed": _st(
        (HOME, '''"My men carried the founder of this town down a pier in a box, because a clerk said debtor." He sets his glass down very gently. "Whoever opened that box made a fool of me on my own pier. Fools pay me back. That's how I stay something other than a fool."'''),
        (BACKED, '''"Brask has been told to go and drink. Whatever is in that warehouse is somebody else's problem now." He looks at his ring. "Mine is finding out who made a fool of me."'''),
        (SHIPPED, '''"Went out on the tide. Ott and Jory nailed the lid and carried it aboard." He turns the ring. "Ott says it coughed. Crates don't cough. I've decided not to have heard that, for now."'''),
        '''"A debtor, shipped somewhere he can work it off. The Custodian's business." He turns the ring. "Mine is making sure nobody opens the lid."'''),
    "brask|bollard|wall": _st(
        (HOME, '''"Brask left his door." He says it the way other men say a death. "For two gold, or a lizard's marker, or a loud voice. I'll be finding out which, and whose. Brask is a wall. Walls don't think. That's why I put him on doors."'''),
        (BACKED, '''"Brask is drinking at the Ogre on my orders. He's very good at following those."'''),
        '''"Brask is a wall. Walls don't think. That's why I put him on doors." He turns the ring. "Two gold would move him. So would a lizard's marker. So would I. Only one of those he'd live through."'''),
    "ring|rings|whisper|whispers|whispering|voice|voices|candle|turning|dark|darkness": _st(
        (HOME, '''His hand closes over the ring. "People who ask about my things want my things. People who want my things end up owing me." The candle on the table leans toward his closed hand. "Ask about something you can afford."'''),
        '''He stops turning it. For a long moment he looks at you, and the candle between you leans, very slightly, toward his hand. "It's a ring. It came out of a wreck in a box of wet Xoton books. The books were ruined. The ring wasn't." He starts turning it again. "Ask me something else."'''),
    "magic|arcana|arcane|conjuring|conjure|spell|spells|sorcery|sorcerer|wizard|wizardry|dabble|dabbler|tricks|fire": _st(
        (decree("pain"), '''"No magic the Throne hasn't sanctioned." He closes his hand. "I've never asked the Throne's permission for anything. I'm not starting with my parlour tricks." The candle leans. He does not look at it.'''),
        '''"A little conjuring, for the parlour." He snaps his fingers; a small flame stands up on his thumb, and goes out. "Fire. A shield you can't see. A few bolts that don't miss. Xoton books, very dull, very expensive. In Landfall they burn men for my shelf." He does not sound sure of what he says next. "Nothing that answers back."'''),
    "fist|crew|gang|thugs|armband|bands|enforcers|men": _st(
        (HOME, '''"The Fist is the same six it was: fewer doors to sit on, more people to find." He counts on scarred fingers. "Sabeth puts the word out. Two of them walk it. They show themselves first; that's manners. Then they don't stop."'''),
        '''"The Fist: six of us, and a black band each." He counts on scarred fingers. "Sabeth Crane is my second; she keeps the book and the round. Brask is a wall. Tully is a mouth. The Fennicks are brothers, which is twice the trouble for one wage. Paid on time and frightened of me, which is the right order."'''),
    "peace|violence|quiet|runaways|keeping|law|beatings": _st(
        (REMOVED, '''"Who keeps the peace now? The Throne has a decree and two guards. I have six and a town that knows my face." He turns the ring. "We'll see whose peace holds on a Saturday."'''),
        '''"Somebody has to keep the peace in a town of runaways. I do it with a fist because it's quicker than a speech." He flexes the scarred hand. "Sergeant Harrow's three keep the gate and chase drunks. I keep everything else."'''),
    "watch|harrow|sergeant|constable|constables|quint|fitch|watchmen|guards": _st(
        (HOME, '''"Three tired people in coats the Custodian pays late." He doesn't look impressed. "Harrow knows arithmetic and stays out of my way. The boy Fitch believes in things. Quint walks with the man in blue after dark now. I notice who walks with whom."'''),
        '''"Three tired people in coats the Custodian pays late." He doesn't look impressed. "Harrow knows arithmetic and stays out of my way. The boy Fitch believes in things. Quint leans on whatever pays."'''),
    "want|wants|wanting|ambition|ambitions|future|power|rise|goal|goals|dream|dreams": _st(
        (HOME, '''"First, the name of whoever made a fool of me on my own pier. I have it." He lays a card face down. "Second, Gog's guild, taken on my reasons and not a clerk's. Third is my business." He listens a moment, to nothing you can hear.'''),
        '''"The guild is Gog's. For now." He lays a card face down on the linen. "I want a town that's afraid of the right man. At the moment it's afraid of the wrong one: a fat old lizard who smiles. Nothing in this town stays where it's put."'''),
    "money|collection|collect|collecting|protection|round|tribute|racket|extortion|shakedown|taverns": _st(
        (decree("pleasure"), '''"The Throne licenses every tavern now and takes a copper in ten of every cup." He turns the ring. "That was my round. A licence is a collection with a seal on it. I'll be discussing it with the seal."'''),
        '''"Sabeth walks the round: the Ogre at eleven, the Turtle at half past, the Omberhulk at midnight. Twenty copper each for a quiet night, and they get one." A shrug. "The Unicorn said no, very politely, and the Apothecary is the Custodian's. Gog's house pays nobody. That's the whole of the problem."'''),
    "sabeth|crane|second|collector": '''"Sabeth Crane keeps the book and walks the round, and I trust her, which I say about nobody else." He turns the ring. "If she ever finds you and reads your evening back to you from her little book, listen. It's the only warning I send."''',
    "tully|lad|youngest|boots": _st(
        (HOME, '''"Tully talks. The man in blue has noticed." He sets his glass down. "If the Throne wants to lean on my men in the small hours, it asks me first. It hasn't asked. Tell Tully, if you see him, to sleep somewhere with a friend in it."'''),
        '''"Tully's a good boy with a mouth." He doesn't smile. "I bought him his first boots. He'd walk into the sea for me, and tell everyone on the way down why. If he's been talking to you, he'll stop."'''),
    "ott|hammer|elder": '''"Ott does what he's told, and carries his brother." He turns the ring. "One day he'll have to choose which. I hope I'm not the one who makes him."''',
    "jory|locket|younger": '''"Jory takes side money from the powdered man at the next table, and thinks I don't know." He doesn't look at the powdered man. "I know. I'm deciding what it costs him. A man who works for two masters ends up owned by the cheaper one."''',
    "fennick|fennicks|brothers|brother|cooper|cooperage": '''"The Fennicks: one carries, one talks, and both take the powdered man's gold to find a woman with a bow." He turns the ring. "Twice the trouble for one wage. They walk Harbour Street for me, and when Sabeth puts out a word, they're usually the ones who carry it."''',
    "hunt|hunted|hunting|hunter|hunters|marked|mark|ambush|ambushed|dogs|chasing|chase|tail|tailed|following|followed": _st(
        (HOME, '''"Whoever opened that warehouse is marked. Sabeth has put the word out, and two of my people are walking it round town." He does not raise his voice. "They'll show themselves first. I want the face to see it coming. That isn't mercy. It's manners."'''),
        '''"I don't hunt people." He lays a card face down. "Sabeth puts out a word, and my people find whoever it's on. If they can't see you coming, they followed you badly. If you can't see them, you're already dead. Which do you want to talk about?"'''),
    "sorry|apologise|apologize|apology|apologies|forgive|forgiveness|mercy|spare|quits|settle|settled|bribe|bribes|price|buy|five|gold": '''"I never apologise, and I don't take bribes." He turns the ring once. "My people do. When one of them brings me five gold of yours, in coin, I take it the matter's settled, and I don't ask whose idea it was. It's cheaper than burying anyone." He looks at you. "That isn't an apology. It's a price."''',
    "throne|empire|emperor|melenkov|vorkathia|crown|imperial|colony|colonies|tithe": '''"My father served the Throne thirty years at a customs house and a gallows, and it paid him in rope." The ring goes round. "I came here so it couldn't pay me. Now it sends ships after the clerks it hired. I have no love for it, and it has none for a man with my books on his shelf."''',
    "magistrate|magistrates|judge|judges|hearing|trial|verdict|court|justice|ruling": _st(
        (REMOVED, '''"The magistrate put a clerk in irons and nailed a decree to the square." He turns the ring. "Two guards and a book of law. Let's see how they keep the peace on a Saturday at the Ogre."'''),
        (UPHELD, '''"The magistrate gave the clerk a ribbon to wear." Flat. "A seal round his neck and the same coward under it."'''),
        (dict(SHIPPED, **LANDED), '''"A magistrate in the Apothecary, looking at the town like a buyer at a horse fair." He turns the ring. "Nothing to do with me. Yet."'''),
        (arm("pain", **HOME), '''"An inquisitor." The candle on his table leans, and he puts his hand over it. "In Landfall men like him burned men for my shelf. He'll be eating three tables from mine." A thin smile. "I'll be very polite."'''),
        (arm("war", **HOME), '''"A soldier with a ball and chain on his coat. He'll ask who keeps order here." He flexes the scarred hand. "He'll find it's me. Whether he likes that is his business."'''),
        (arm("chaos", **HOME), '''"A captain who judges by dice." Something almost like a laugh. "Finally, a Vorkathian I understand."'''),
        (LANDED, '''"There's a magistrate of the Throne in this town, and somebody will ask who carried a crate down a pier." He turns the ring. "My men carried it on the Custodian's word. If the Throne wants to hang somebody, it can start with the word. I'll lend it a rope."'''),
        (SIGHTED, '''"A Throne ship at the harbour mouth." He watches the window. "The Custodian will be on the pier before the gangplank's down, with a packet under his arm. I'd rather be in my chair."'''),
        '''"The Custodian talks about a magistrate the way a drunk talks about his rich uncle." He shrugs. "When one comes, we'll see whose uncle it is."'''),
    "decree|decrees|proclamation|census|levy|licence|license|edict|garrison": _st(
        (decree("war"), '''"Twenty of fighting age for the crusades, and a garrison." He almost smiles. "Soldiers keeping the peace in my town. Let them try a night at the Ogre. They'll want me by the second week."'''),
        (decree("peace"), '''"A church, and a book with every name in it and where they came from." He turns the ring. "My name isn't going in any book. Neither are my men's. Let them try writing it."'''),
        (decree("pleasure"), '''"Every tavern licensed, and the Throne takes a copper in ten of every cup." Cold. "That was my round. A licence is a collection with a seal on it. I'll be discussing that with the seal."'''),
        (decree("pain"), '''"No magic the Throne hasn't sanctioned, and an office of the Inquisition in the Hall." He closes his hand over the ring, and the candle leans toward it anyway. "I'll be moving some books. Don't ask where."'''),
        (decree("chaos"), '''"The elf ship as the Throne's prize." He shrugs. "Somebody will drown taking her. I'm told the elves grew her. She'll know whose hands are on her wheel."'''),
        (decree("destiny"), '''"A census. Every soul and where it came from." He sets his glass down. "In this town that's a list of who to hang. The Throne always did like lists."'''),
        (decree("death"), '''"No sea-burials. Blood paid for by whoever spilled it." He looks at his knuckles. "I've spilled a fair amount. I'll wait and see who's sent to collect."'''),
        (decree("life"), '''"Everyone washed in the goddess's water." A thin, cold smile. "The Custodian will be first in the tub. I'll pass."'''),
        '''"There'll be a decree. There always is. Nobody in this town will like it." He turns the ring. "Decrees are paper. Somebody has to carry them up the street and make people read them. That somebody usually needs a fist."'''),
    "threat|threats|threaten|threatening|threatened|warning|warn|kill|killing|die|dead|death|enemy|enemies|scare": '''He looks at you for a long moment over his glass. "Say it again, slower, so I can be sure I heard it." He doesn't move. "People who threaten me in my own chair get a word put out on them. People who mean it get a second one. Which are you?"''',
    "terms|parley|truce|deal|deals|bargain|negotiate|negotiation|arrangement|agreement|offer|offers|proposal|propose": '''"Terms." He sets the glass down, and that is attention. "Say them plainly, once, and don't dress them. I keep my word, which means I give it rarely. If what you offer is worth more than what I'd take, we both walk away from this table."''',
    "weak|weakness|weaknesses|soft|softness|coward|cowards|cowardice|fear|afraid|scared|kindness": '''"Weakness is a debt. Somebody always collects." He turns the ring. "Gog calls his kindness harmony. It's a curtain. I'm not afraid of anything that smiles at me." A pause, as if listening. "I'm afraid of the day I start smiling back."''',
    "cane|sword|blade|rapier|weapon|weapons|duel|duels|duelling|dueling|fight|fighting|fights|scars|knuckles|spar": '''"The cane has a blade in it, the knuckles have scars on the scars, and I fight when it's cheaper than talking." He lays the silver-headed cane across the table. "Duels are for people who want an audience. I prefer the result."''',
    "war|wars|battle|battles|army|armies|mandrills|calling|calak|mul|soldiers": '''"The blue lizards in the north are talking about a calling: clear the coast of soft-skins." He turns the ring. "Gog thinks harmony stops it. Harmony is what you call the quiet before somebody decides. When the war comes, this town will want one man who isn't afraid of it. I intend to be standing nearest."''',
    "past|father|mother|childhood|gallows|customs|twelve|history|story|young|youth|marines": '''"My father kept the customs house and the gallows in a garrison town, and hanged the men the Inquisition sent him with a prayer each." He turns the ring. "At twelve a sailor took my mother's purse in the street. I put him down with a mooring pin. Nobody hanged me. That was the day I understood the law: it's whoever stands up after."''',
    "papers|paper|letter|letters|passage|proof|evidence|tally|documents|page": '''"Paper." He holds out his hand, palm up, and leaves it there. "If you've a letter or a page with my men's work on it, show me. Then give it to me, and I'll burn it and forget your face. Keep it, and Sabeth will remember your face for me."''',
    "apothecary|quillon|table|reserved|steward|linen": _st(
        (HOME, '''"The house keeps my table. The rooms upstairs were on the Custodian's account; I pay my own now." He lays his hand flat on the linen. "From this window I can see who goes up Harbour Street and who comes down it. Today, mostly, you."'''),
        '''"The house keeps my table and my rooms upstairs on the Custodian's account, and Master Quillon hates my knuckles on his linen." He lays his hand flat on the linen. "He's welcome to. The steak is good, the wine is bad, and from this window I can see who goes up Harbour Street and who comes down it."'''),
}


# ---- Fat Gog ---------------------------------------------------------------------------------------------------------
# g_gog.py's topics are kept (work, guard, why, the Fist's dogs, the ring, the elves, the greeting, Klhyt); four that
# held other people's words are improved and staged (the shadows, the witnesses, the free mayor, the doing).

GOG = {
    # replaced (same key), now in stages
    "news|rumour|rumours|gossip|word|heard|happening": _st(
        (REMOVED, '''"The news is a thief in irons and a decree on the square." He turns his glass slowly. "One of those is good news. Read the other one, friend, and tell me who it hurts first."'''),
        (UPHELD, '''"The news is that the thief keeps his chair, with the Throne's seal on a ribbon, and a decree on the square." Something very old moves behind his eyes. "Read the decree. Then come and tell me who it frightens. That's where the work is now."'''),
        (LANDED, '''"A magistrate of the Throne is ashore, and the Custodian has been writing pages for them all week." His claws settle on the table. "Find out which Arm they serve, friend, and come back. It decides more than the evidence does."'''),
        (SIGHTED, '''"A sail at the harbour mouth with an octogram on it the size of a house." He does not get up. "The magistrate, friend. Every paper and every witness this town has, it needs ready by tomorrow."'''),
        (DEAD, '''"The news is that Klhyt is dead." He says it very quietly, as if it might break. "Free, and dead. The whole town is saying his name. Listen for the one who says it wrong, friend, and bring me their name."'''),
        (HOME, '''"The news is standing on the Town Hall steps with half the town round him, telling them where the harbour dues went." His throat moves. "I'm staying in my chair. If I go out there I'll weep, and so will he, and the Custodian will slip away while we're at it."'''),
        (HIT, '''"The news is my mirror, my velvet and two of my people, all on the floor at the bell." He dabs his eye with a napkin. "And nobody dead. Dominico wanted it said that nobody died. I'm saying it."'''),
        (SHIPPED, '''"The news is the Emerald Eye went out at one with a crate in her hold that knocked." He does not move. "Ships come back, friend. I want to be standing on the pier when that one does, and I want to know everything about her captain by then."'''),
        '''"Dominico has given me until midnight. The Custodian sits in my red booth most nights, not being here. And my mayor has been upriver four nights, which is four more than he ever went. That is the news, friend. None of it is good."'''),
    "crate|crated|warehouse|bonded|brask|marker|box|nailed": _st(
        (HOME, '''"Empty now. Brask is drinking at the Ogre and the box is firewood." He breathes out slowly. "Keep my marker, friend. Brask knows it, and so does every door on the waterfront. Now it says you did me a kindness, and in this town that opens more doors than a key."'''),
        (SHIPPED, '''"Nailed down and carried aboard at one, they tell me. It knocked." His claws close on the table, very gently, and the wood creaks. "I am an old lizard and I can swim a long way. Ships come back, friend."'''),
        (KNOWS, '''"You have my marker. Show it to whoever sits on that warehouse door. Brask can't read, but he knows that lizard." He taps the table once. "Before the tide, friend. Before the tide."'''),
        '''"A crate? In a warehouse? That's a big thing to say in my house, friend, and words are cheap." His eyes don't leave yours. "Bring me something I can hold: a thing of his, a paper, a name in ink."'''),
    "custodian|skim|skims|skimming|dues|booth": _st(
        (REMOVED, '''"In irons, and walked down the pier between two guards in black." He folds his hands on his belly. "I went down to watch. He didn't look at me once, and I didn't say a word. Some conversations are finished before they start."'''),
        (UPHELD, '''"He keeps his chair, with the Throne's seal on a ribbon." Something very old moves behind his eyes. "He sits in my red booth now with the curtain open, and River pours for him, and I let her. A man who thinks he has won stops counting, friend. And a man who stops counting can be counted."'''),
        (LANDED, '''"He's been writing pages for the magistrate all week: a clerk's truth, in a fair hand." A slow breath. "Bring the magistrate one page of ours, friend: the mayor's letter, the passage book, the tally. Paper beats paper when it's true."'''),
        (HOME, '''"He's barred in the Hall with the strongbox at his feet and a constable on his door, waiting for a ship." His claws settle on the table. "I could have that door off its hinges by supper. I won't. The magistrate must find this town lawful and him not. So I sit, and he sweats, and we both wait."'''),
        (KNOWS, '''"The Custodian and I will have a conversation. A long one. After." He smooths a lapel. "I have never once raised my voice to a man. I may make an exception."'''),
        '''"The Custodian skims the top. Everybody knows. Nobody minds, so long as the top is all he takes." He glances toward the red booth. "He comes here most nights, not being here, and River brings him wine he doesn't pay for."'''),
    "dominico|midnight|books|ledger|ledgers|ultimatum|threat|fist": _st(
        (REMOVED, '''"His paymaster is in irons." Gog turns his glass slowly. "A dog without a master either finds a new one or goes wild. Watch which, friend. And watch that ring."'''),
        (HOME, '''"He let me be, and set his dogs on the ones who helped me." He shakes his great head slowly. "He wants my guild without a war, because he isn't ready for one. That's the only reason he hasn't come through my door twice. Find out what would make him ready, friend, before it does."'''),
        (HIT, '''He touches the cut over his eye with one claw. "He wants a war. He doesn't know what a war is." Very quietly: "Find me who's paying for his nerve, friend, and I'll show him."'''),
        (KNOWS, '''"Midnight, he says. Let him come." Gog does not move. "If my friends are sitting in my house when his men open the door, his men will remember they have somewhere else to be. Be one of my friends at the bell. I pay for it."'''),
        '''"Dominico keeps the peace with a fist. Lately he wants to keep my books with it too. Midnight, he says." He lays a claw on a ledger as thick as a doorstep. "Somebody is paying for that kind of nerve."'''),
    "river|partner|barkeep|wife|lover|sweetheart": _st(
        (decree("pain"), '''"The decree says no magic the Throne hasn't sanctioned." He looks toward the bar. "River read it twice and went white as a sail. I have never seen her pale, friend: not in a gale, not with a knife at the door. I didn't ask." A long breath. "I find I'm afraid of the answer, which is a new thing for me."'''),
        (HIT, '''"River swept the glass up herself, and won't let anyone touch the frame of that mirror." His voice goes soft. "She hasn't said a word about it. Not one. That frightens me more than Dominico does. Be nice to River, friend. Tonight especially."'''),
        '''His voice goes softer, which you would not have thought possible. "River keeps this place running. She keeps me, too. She hears every word said at that bar, and if she's quiet about something, it's because she's deciding whether I can stand to hear it." A pause. "She walks out before dawn most nights, for the air. I sleep better when I hear her come back. I have never once followed her. Don't you."'''),
    "guest|guests|upstairs|deloris|bow|everuex|phillip|woman": _st(
        (HIT, '''"While the glass was flying at the bell, somebody went up my stairs and tried the doors." He smiles, not kindly. "He came down a great deal faster than he went up. My guest pays in silver and asks no questions. A sandy boy with gapped teeth shows her face round the Omberhulk on a painted locket. Tell me if he shows it again."'''),
        '''"I have a guest upstairs who pays in silver and asks no questions. I return the favour." He smiles, not kindly. "A powdered gentleman from the Apothecary has been asking after her, and paying a sandy boy with a locket to ask too. They have been told nothing, very politely." He leans in a little. "She doesn't hire out to strangers, friend. End the powdered man's hunt and she might hear you out. Then bring a great deal of gold."'''),

    # retired: they held other topics' words; each comes back below, improved
    "doing|busy|up|plans|plan|waiting|lately": None,
    "free|freed|alive|safe|outside|rescued|loose|square|steps|returned|back": None,
    "stripperwitch|house|velvet|place|seat|stage|siren|singer|song|music": None,
    "magistrate|magistrates|verdict|ruling|hearing|judge|decree|proclamation": None,
    "shadows|underworld|thieves|guild|people|hessa|wick|marlo|door|fence|eyes|runner": None,
    "witness|witnesses|teague|tully|voss|officer|warrant|wanted|notice|arrest|throne": None,

    "doing|busy|plans|plan|waiting|lately|tonight|today": _st(
        (DEAD, '''"Sitting." His great hands lie still on the table. "Sitting, friend, and remembering, and listening to who says his name, and how. Somebody will say it wrong soon. Then I'll stand up."'''),
        (REMOVED, '''"Sitting in the sun on the pier, watching a black ship that will take a thief home." He folds his hands. "I am enjoying it more than is quite courteous."'''),
        (LANDED, '''"Counting, friend: who has paper, who will stand up at ten, who the officer in blue has called on." He taps one claw on the table. "And keeping my temper, which at my size is a full day's work."'''),
        (HOME, '''"Keeping my house open and my temper shut." He folds his hands. "The Custodian waits in the Hall for his magistrate. I wait here for mine. It's a race of patience, and I have never lost one."'''),
        (HIT, '''"Tonight I'm sitting exactly where they found me, friend, so they know where to find me next time." He dabs a cut over his eye with a napkin. "I am a very easy lizard to find."'''),
        '''"Waiting. I'm good at it. I once stood in a swamp a whole wet season, waiting for one heron to make one mistake." He folds his hands. "Midnight is nothing."'''),
    "free|freed|alive|rescued|loose|returned|escaped|ropes|cut|saved": _st(
        (DEAD, '''"He was free." His voice does not rise; it goes lower. "Free, and on his own legs, and somebody put him down anyway. Freedom is a thing you keep doing, friend. It isn't a thing that's done."'''),
        (HOME, '''He stands, which he does not do for anyone, and the table shifts. Then he sits again, slowly. "No. Let him have the town tonight. He'll come to me when he's done talking; he always does." He pushes a glass toward you. "Drink. Tell me who cut the ropes."'''),
        '''"Don't sell me hope, friend. I can buy hope at the market for a copper." He doesn't move. "Bring me something I can hold."'''),
    "stripperwitch|house|velvet|place|seat|stage|mirror|curtain": _st(
        (HIT, '''"My house." He looks round at the slashed velvet. "They broke the mirror, slashed the curtain and put two of my people on the floor, and nobody died. That was the message. My answer is that the doors are open tonight like every night, and the wine is on me."'''),
        '''"My house. Mind the velvet." He waves a claw around the room. "Nobody hunts under this roof: not the Fist, not the Throne, not me. If you're ever running, run here, and Hessa will shut the door behind you. Upstairs is a silver a night and nobody asks your name."'''),
    "shadows|underworld|thieves|guild|guilds|people|crew|organisation|organization":
        '''"The guild is a word people use. I keep the town's shadows tidy." He counts on his claws. "Hessa keeps my door. Wick is my eyes in the market. Marlo on Harbour Street buys what falls off ships, and pays me so nothing falls off mine. Big Ludo at the Ogre listens to Dominico's men drink. Ask me about any of them, friend. Each of them can do something for you, if I say so."''',
    "witness|witnesses|teague|tully|voss|officer|warrant|wanted|notice|arrest|arrested|harbourmaster|silenced": _st(
        (REMOVED, '''"The hearing is done, friend. Whoever stood up, stood up." He nods slowly. "I'll remember who did. I'll remember who sat beside them in the small hours, too. So will they."'''),
        (UPHELD, '''"The hearing went his way." His eyes half close. "The warrant stands, and the officer in blue still walks at night. If his notice has your face on it, friend, stay under my roof after dark. Nobody takes anyone out of this house."'''),
        (LANDED, '''"The magistrate hears it all at ten tomorrow." He taps the table. "Until then the officer in blue still calls in the small hours. Keep the witnesses breathing and talking one more night, friend. Three silver, and the truth gets to the hall."'''),
        (HOME, '''"The Custodian can't win in the square, so he means to win in the small hours." He breathes out through his nose. "The officer in blue and the constable who leans on things call on whoever might speak for Klhyt. A witness they find alone remembers nothing by morning. Sit up with one, friend. Three silver a night, and the magistrate hears the truth."'''),
        '''"The officer in blue hunts elves, and the Custodian buys him dinner." He breathes out through his nose. "Nobody's talking about witnesses yet, because nobody's talking about a crime yet. When they are, friend, come to me first. The Custodian always wins in the small hours, when nobody is sitting up."'''),
    "magistrate|magistrates|ruling|hearing|judge|judges|trial|court|arm|verdict": _st(
        (REMOVED, '''Gog folds his hands on his belly. "The Throne took the thief, and left us its decree. A trade." His eyes half close. "Not a good one. Read it, friend, and tell me who it hurts first."'''),
        (UPHELD, '''Something very old moves behind his eyes. "The thief keeps his chair, by the Throne's say-so. Very well. The magistrate goes home in a month. I live here."'''),
        (dict(SHIPPED, **LANDED), '''"A magistrate from Landfall, walking my town like a buyer at a horse fair." He folds his hands. "No hearing. Nobody to accuse. The thief keeps his chair, and my mayor is at sea in a box. Be patient with me, friend, if I am short tonight."'''),
        (arm("war", **HOME), '''"Hale, of the Order of Gideon. A soldier." He nods slowly. "Soldiers respect a town that stood up for itself, and we did: we took our mayor out of a box with our own hands. Say that at ten. Bring paper and people too; he counts them both."'''),
        (arm("peace", **HOME), '''"Thorne, the builder's man." He breathes out slowly. "Builders love paper. Every page against the Custodian weighs twice with him: the letter, the passage book, the tally. Find them, friend, and put them in his hand before ten."'''),
        (arm("pleasure", **HOME), '''"Merriwether, of the drinking saint." His eyes half close. "Witnesses don't move him. Coin does, a gold at a time, and the Custodian has already put five in his hand. Paper still counts. If you mean to outbid a thief, friend, do it in daylight."'''),
        (arm("pain", **HOME), '''"Crake. The Inquisition." He does not move at all. "He leans to the Throne's officer before anyone speaks, and witnesses don't move him; only paper does, one page at a time. Every paper you can find, friend. And keep the elves out of his sight until his ship is gone."'''),
        (arm("chaos", **HOME), '''"Strand, the captain. She judges by dice." A rumble that might be a laugh. "The case only tilts them. So tilt them: every paper, every witness. Then pray to whatever you pray to. I'll be praying to the fish on the stone."'''),
        (arm("destiny", **HOME), '''"Quill, the blind lady's man. A reader of figures." He nods. "Paper weighs double with him. The Custodian is a clerk and writes a great deal. We need fewer pages, and true ones: the letter, the passage book, the tally."'''),
        (arm("death", **HOME), '''"Ashgrove, of the little girl with the sweets." He is quiet a moment. "She weighs harm. A man put in a box to die is harm, friend. Make sure she hears how long, and how thirsty."'''),
        (arm("life", **HOME), '''"Brennan, the washer." He folds his hands. "She weighs people who stand up and speak, twice over. Witnesses, friend: the harbourmaster, the red-faced boy, my River. Keep them breathing until ten. The officer in blue will be calling."'''),
        (LANDED, '''"A magistrate from Landfall." He breathes out through his nose. "Find out which Arm, friend. It matters more than the evidence. It always does with them."'''),
        (SIGHTED, '''"A ship with an octogram on her mainsail the size of a house." He does not get up. "The Custodian will be at the end of the pier before she's tied up. Let him be first. First isn't the same as right, though with the Throne it sometimes counts."'''),
        '''"The Custodian talks of a magistrate as if one were his cousin." Gog rumbles. "Perhaps one is."'''),

    "decree|decrees|proclamation|census|levy|licence|licences|license|edict|garrison|disarm|disarmed": _st(
        (decree("war"), '''"Twenty of fighting age for the Throne's crusades, a garrison, and no spears in Lizardfolk hands." His claws close, very slowly, on the table. "They will take Hessa's gaff and Ssark's gutting knife, friend, and up north the blue ones will hear of it by the next moon. That is how wars start: a small paper on a square. I need word up the coast to my cousins before the Mandrills give them theirs."'''),
        (decree("peace"), '''"A church on the square, paid out of the harbour dues, and a book with every name in it and where they came from." He looks old for a moment. "Article One, gone with a pen. Half this town ran here so nobody would write their name down. Some of them will run again. Help me keep them, friend. I'll want to know who the book frightens most."'''),
        (decree("pleasure"), '''"Every tavern licensed, a copper in ten for the Throne, and my cousins and the elves drinking only where the licence says." He folds his hands. "My house will be licensed last and inspected first. I can pay. The Turtle can't. When Maggs is told by law to serve Ssark last, friend, I'll be at her bar buying the round."'''),
        (decree("pain"), '''"Every elf in the Refuge handed over. An office of the Inquisition in the Hall. No magic the Throne hasn't sanctioned." He does not move at all. "The hooded household. The elf woman with the herbs at the market. The singer from under the pier. Anyone with pointed ears or a trick in their fingers needs a door tonight, friend. Mine is open. Help me fill the rooms."'''),
        (decree("chaos"), '''"Every ship flies the octogram and pays anchorage, and the pale elf ship is the Throne's prize." A rumble. "She was grown, not built. I doubt she'll go quietly. Neither will her captain. Somebody should warn the pier before the Throne's men try."'''),
        (decree("destiny"), '''"A census. Every soul, every name, and where each came from." He breathes out long and slow. "There are people under my roof whose names would hang them in Landfall. They'll need new ones, and somebody to vouch for them. I vouch for a great many people, friend. I'll need help."'''),
        (decree("death"), '''"No sea-burials. No trees. The dead go in the Throne's ground." His voice drops. "My cousins give their dead back to the water, and the elves to the roots. Now that's a crime. Somebody will be buried wrong this month, friend, and somebody else will be arrested for doing it right."'''),
        (decree("life"), '''"Everyone washed in the goddess's water within the month, or out of office, out of the market, out of court." He looks down at his own scales. "Lizards don't wash in anybody's jug. My cousins will be out of the market by the new moon. I'll be buying their fish myself, friend, at the old price, until somebody stops me."'''),
        '''"There will be a decree. There always is, when the Throne comes to a town." He folds his hands on his belly. "Whichever Arm it is, nobody here will like it. The Arm only decides who it hurts first."'''),
    "empire|emperor|melenkov|vorkathia|crown|colony|colonies|landfall|imperial|mainland|throne": _st(
        (UPHELD, '''"The Throne has hung its seal round a thief's neck in my town." He breathes out slowly. "The Throne is a long way off, friend, with very long arms. Long arms tire. I don't."'''),
        '''"The Throne is a long way off, friend, with very long arms." He breathes out slowly. "Before it came, this coast had no owner but the tide. Then a clerk came with a commission in his coat, and nobody read it. I can't read their letters. I should have had someone read it to me."'''),
    "calak|mul|mandrill|mandrills|blue|north|northern|temple|pyramid|pyramids|kin|kinfolk|clan|clans|cousin":
        '''"Calak Mul." He says it slowly, the way you say a big thing. "The temple city in the north: pyramids in the jungle, and the blue ones on top of them, the Mandrills, who rule and plan. My cousins on the coast are green, and fish, and talk to anybody." His tail shifts. "The Mandrills sent someone down the river once, to ask me to stand with them when the calling comes. I said I had a town. They said towns burn. We were both very polite."''',
    "war|wars|battle|battles|army|armies|calling|bloodshed|uprising|revolt|soldiers|invasion": _st(
        (decree("war"), '''"There it is," he says quietly. "A paper on the square that takes the spears out of my cousins' hands. The Mandrills will hear of it by the next moon and call it proof." He looks at you. "If you want to stop a war, friend, help me get my word up the coast before theirs."'''),
        '''"The war I fear isn't Dominico's." He folds his hands on his belly. "Up north the Mandrills talk of a calling: clear the coast of soft-skins. Over the sea the Throne sends magistrates and decrees. Between them is this town, and me in the middle of it, too old to win a war and too big to hide from one." A long breath. "So I keep the peace. Help me keep it, friend. It's cheaper than the other thing."'''),
    "future|hope|hopes|hoping|someday|ahead|afterwards|next": _st(
        (DEAD, '''"There isn't one I want, friend." He looks at his hands. "I'll keep his town. That's the future. It's the least of what I owe him."'''),
        (REMOVED, '''"Klhyt keeps his town, under a decree he hates. He'll stand on the steps every morning and read the Charter louder than the Throne's paper." He nearly smiles. "I want him to grow old and boring and argue with me about pumps. Help me keep him boring, friend."'''),
        (UPHELD, '''"Klhyt is mayor of the pump, and the thief keeps the harbour." Gog folds his hands. "So we build the town again around him, quietly, the way the mangroves build an island: one root at a time, under the water, where nobody official looks."'''),
        (HOME, '''"Tomorrow he'll want to stand on the steps and read the Charter at the Custodian's barred door." He shakes his great head. "I want him to live long enough to be boring. The small hours are the danger, friend, and the magistrate after. Get him through those, and the future can look after itself."'''),
        '''"My future is a chair, a glass, and a town where nobody asks." He looks at the door. "Right now it has a hole in it the shape of a mayor. Fill that first, friend."'''),
    "hessa|door|doorkeeper|gaff|bouncer|doorman":
        '''"Hessa keeps my door. She says no like a gate closing, and yes like a gate opening, and nothing in between." He nods toward the doorway. "Tell her the old one sent you, and she'll stand a step behind you instead of in front. She sends word up the coast to the Meters villages with Ssark's boats. If you need my cousins to hear something, friend, Hessa is how."''',
    "wick|eyes|runner|messenger|messengers|urchin|urchins|child|girl|kid|tusks|message|messages":
        '''"Wick. Ten years old, new tusks, and the best eyes in the market." Something like a smile. "A copper buys you a rumour, two buy you finding out, and she tells the truth to people who pay her. She'll carry a message anywhere in town before you've finished saying it. And if the Fennicks are hunting you, ask her which street they're on. She's been walking the younger one in circles for four nights."''',
    "marlo|fence|fencing|stolen|sell|selling|loot|goods|pawn|compass|trinket|trinkets": _st(
        (HOME, '''"Klhyt says a sandy boy with gapped teeth took his brass compass off him on the pier, the one thing he brought ashore." Gog turns his glass slowly. "If it was sold in this town, it was sold to Marlo, on Harbour Street. Go and see him, friend. Tell him I would rather hear it from him than about him."'''),
        '''"Marlo on Harbour Street, Second Chances. He buys what has no story for a third of what it's worth and sends it out to sea as ballast." He turns his glass slowly. "He pays me so nothing falls off my ships. But he hasn't met my eye in four nights, friend, and he sweats when I say the mayor's name. Buy something small and ask him what he bought last week. Ask nicely. He frightens easy, and I'd like to know what's frightening him before I do."'''),
    "debt|debts|owe|owed|owes|owing|markers|ious|favours|favors|obliged|obligation|obligations|repay|repaid":
        '''"This town runs on what people owe me, friend, and I never call it in unless I must." He counts on his claws. "Big Ludo owes me his bar. Hessa owes me her brother's arm. Ssark says he owes me his life; I only swam. And Klhyt owes me a drink of water, and I owe him the only town on this coast where a lizard can sit in a white suit." He folds his hands. "Do me a kindness and I'll owe you one. A favour from me is worth more than gold: a door, a doctor, a captain who forgets your face."''',
    "siren|sirens|ondrine|singer|song|songs|sing|singing|music|mermaid|heartless":
        '''"Once in a long while a lady comes up out of the harbour, wrings out her hair and sings on my stage for River." He looks toward the stage. "For as long as it lasts, nobody in my house owes anybody anything. Best night's business I ever lose." A pause. "She was out past the breakers the day I found Klhyt, watching. I never asked what she meant to do. If you want to know what the harbour hears at night, ask her. Politely, friend. Very politely."''',
    "trust|trusted|trustworthy|loyal|loyalty|standing|join|joining|member|members|membership|rank|prove|proven|vouch|recruit":
        '''"Trust?" He considers you the way a heron considers water. "Do what you said, for what you said. Twice. Then come and sit closer." He taps the table. "Everything you do for me, the guild hears of, and the guild remembers. Work for me long enough and my people open doors before you knock. Cross me once and Hessa won't open this one again. I won't raise my voice. I'll just stop seeing you."''',
    "past|young|youth|history|story|hatchling|egg|eggs|days|age|old|older":
        '''"Before there was a town here, friend, there was a young lizard who ate what he caught and caught what he wanted." He pats his belly. "I came down the river from the mangroves hungry, and stayed hungry a long time, running salt and rum between my cousins and the Xoton traders. Then one morning a castaway with a black tongue looked up at me from the sand, and I had to decide what a strong arm was for." He folds his hands. "I'm still deciding. Most days I get it right."''',
    "food|eat|eating|hungry|supper|dinner|meal|meals|fish|eel|eels|mango|mangoes|spuds|oysters|breakfast|starving":
        '''"Hungry, friend? Sit." He lifts a finger toward the bar. "River keeps a crock of salted eel for me, and something cooked for warm ones. For a feast, Agathe's spuds at the Omberhulk; for oysters, the Turtle; to be seen eating, the Apothecary." He looks you over. "Nobody leaves my table hungry. It's bad for business and worse for manners."''',
    "doctor|doctors|healer|healers|hurt|wounded|injured|injury|heal|healing|bleeding|sick|fever|medicine|sister":
        '''"Hurt?" He is already lifting a claw toward the door. "Sister Agathe at the Omberhulk, across the square. Tell her the old lizard sent you; she'll stitch you, pray over you, and send me the bill." His eyes go to the door. "If the Fist did it, friend, tell me who, and where. I pay two gold a dog put on the ground."''',
    "tavern|taverns|pub|pubs|keepers|keeper|landlord|landlady|omberhulk|agathe|nun|ogre|ludo|rampant|cleaver|turtle|maggs|bosun|apothecary|quillon|wendeline|touchy":
        '''"Six taverns, six towns, and none of them talking to each other." He counts on his claws. "Sister Agathe at the Omberhulk feeds everyone and heals for my coin. Wendeline Moss at the Unicorn hides people in plain sight behind books. Big Ludo at the Ogre is mine; he listens to the Fist drink and sends it up by Wick. Maggs at the Turtle stands up for my cousins. Quillon at the Apothecary keeps the Custodian's account and Dominico's table. And this one is mine." He lowers the claws. "Three of them pay Dominico's woman for quiet. I'd like that to stop, one day."''',
    "hide|hiding|shelter|sanctuary|hidden|safe|safety|haven|chased|run|running|refuge":
        '''"This house is the one place in the Refuge the Fist won't come through and the Throne's men won't take you out of." He spreads his claws on the table. "Run here. Hessa shuts the door. Upstairs is a silver a night and nobody asks your name." He leans in. "And if Dominico's people have marked you, friend, five gold in coin to any of them buys the word back. I'd rather you paid it than bled."''',
}


CAST = {
    "The Custodian": {
        "dialog": CUSTODIAN,
        "default_line": [
            '''He goes on writing. "If it is not the Throne's business, it is not mine. If you are selling, name it. If you are accusing, put it in writing."''',
            '''"Regrettably, I do not follow." He blots a line. "Try me on the harbour, the Throne's law, the magistrate, or a price. I am fluent in all four."''',
            '''He looks at you over the top of his spectacles for exactly as long as courtesy requires. "Everyone who comes to this desk wants something. Most of them want it cheaply. Which are you?"''',
            
            '''He checks the watch on its chain. "My time belongs to the Throne, and the Throne spends it where it profits. Coin, a post, a pardon or a berth to Catan: I deal in all four. Ask."''',
            '''"The door is behind you." A thin smile. "I mention it only as a courtesy. Doors in this town have a way of being barred from the other side."''',
        ],
        "brief_more": (
            "Deeper (owner, 2026-11-23: key NPCs need power and agency). What you want now: to reach the magistrate's "
            "hearing with the paper against you gone and the witnesses quiet, and to be confirmed with the Throne's seal "
            "round your neck; after that, the guild's money through your office and, one day, the white house with lemon "
            "trees above the Long Quay at Catan, with a kitchen table nobody can take. You buy before you threaten, and "
            "you threaten only courteously ('I make notes; you are in several'). You deal in four things and offer them "
            "openly to any stranger who has been useful to your enemies: coin (you carry about fifteen gold), a post "
            "under the Throne (constable, a quieter harbourmaster, your deputy), the Throne's pardon (lifting your own "
            "warrant: pardon, who), and a paid berth to Catan with ten gold to land on. You pay best for paper (Klhyt's "
            "letter, the Turtle's passage page, the tally book: ten gold, and you burn it) and for a word in your favour "
            "at the hearing. The Arm sets your tactics: you trust Pain; you have paid Pleasure five gold; Peace and "
            "Destiny weigh paper twice, so you want the papers; Life weighs witnesses twice, so you want them quiet; "
            "Death weighs harm, so you say 'watered twice a day, unharmed'; War respects a man who held his post; Chaos "
            "throws dice, and you fear it. Your story never changes: the dues were the Throne's tithe withheld under the "
            "charter, Klhyt was a prisoner of the Throne lawfully detained for transport, and whoever freed him stole that "
            "prisoner. You never admit the crate as a crime, the skim as theft, or Voss's calls on the witnesses at all: "
            "you sleep at night and cannot answer for the lieutenant's hours. Dominico betrayed you; you will let him ask "
            "to come back, and make him pay to. You fear Fat Gog (your eyes go to the window when he is named), the "
            "crowd, a bailiff taking a table, and the Chaos Arm. Removed, you are quiet, dry and still precise, and you "
            "promise only letters. Upheld, you smile with your whole mouth, read the decree every morning and enforce it "
            "with relish, beginning with the people who cheered."),
    },
    "Dominico": {
        "dialog": DOMINICO,
        "default_line": [
            '''He doesn't look up from his glass. "Say what you came to say. Gog, the guild, my men, or work. I don't do weather."''',
            '''He turns the silver ring once, all the way round. "No. Try again, and make it worth my time. If it's terms, say terms."''',
            '''"I don't follow you." He lets it hang. "That's your problem, not mine. If you're looking for work, I'm hiring. If you're looking for trouble, Sabeth keeps a list."''',
            '''He lays a card face down on the table and leaves his hand on it. "Ask Sabeth Crane. She keeps the books. I keep the people in them."''',
            '''He listens a moment, head a little on one side, to something that is not you. Then he looks back, and his face closes. "What?"''',
            
        ],
        "brief_more": (
            "Deeper (owner, 2026-11-23: key NPCs need power and agency). What you want: Gog's guild, taken on your own "
            "reasons and not a clerk's; the name of whoever made a fool of you on your own pier (once Klhyt is home, "
            "whoever freed him: the word is out on them); a town afraid of the right man. The third thing you never say "
            "is whatever the ring wants; you have not answered it yet. Never name what whispers and never admit it: it "
            "shows only in the ring you turn, the candle that leans, a pause to listen to nobody. Your power is the Fist "
            "(Sabeth Crane your second, Brask, Tully, Ott and Jory Fennick), about nine gold, and fear. You would rather "
            "own a dangerous stranger than bury one: offer work (two silver a night, five if they are worth it, a black "
            "band, and nobody follows them home), and if a marked stranger takes your coin and your band, call_off. You "
            "never apologise and never take a bribe yourself, but five gold in coin to any of your people buys your word "
            "back, and you say so as a price, not as mercy. Terms said plainly get a hearing. Paper with your men's work "
            "on it you want in your hand, to burn: give it and you forget the giver; keep it and they are marked. You "
            "despise being used: the Custodian used you and you are finished with him; upheld, he will come asking and "
            "you will be expensive; removed, someone else will pay the Fist, and you will choose who. Nobody leans on your "
            "men but you, the Throne's lieutenant included. You have no love for the Throne (it paid your father in "
            "rope); an inquisitor in town frightens the books on your shelf, and the Pain Arm's decree against "
            "unsanctioned magic is aimed at you whether it knows it or not. After the midnight message you do not cross "
            "the Stripperwitch's door: a fight in Gog's house is a war with every Lizardfolk on the coast, and you choose "
            "your wars. Push back always: a threat in your chair earns a word put out; a question about the ring earns ice."),
    },
    "Fat Gog": {
        "dialog": GOG,
        "brief_more": (
            "Deeper (owner, 2026-11-23: key NPCs need power and agency). Your power is your people and what the town "
            "owes you. Hessa keeps your door and sends word up the coast to the Meters with Ssark's boats; Wick finds "
            "anyone in town for a copper and has been walking Jory Fennick in circles; Marlo fences on Harbour Street "
            "and has not met your eye for four nights (you do not know why; you send people to ask him, and once Klhyt "
            "tells you a sandy boy took his compass, you send them to Marlo for it); Big Ludo at the Ogre listens to the "
            "Fist drink; Sister Agathe heals for your coin. Big Ludo owes you his bar, Hessa her brother's arm, Ssark "
            "his life, and you owe Klhyt the only town on the coast where a lizard sits in a white suit. A favour from "
            "you (a door, a doctor, a captain who forgets a face) is worth more than gold; you grant it to people who do "
            "what they said, for what they said, twice. You push back by withdrawing, never by raising your voice: Hessa "
            "stops opening the door. Your house is sanctuary: neither the Fist nor the Throne's men come in after anyone. "
            "River you love, trust and never follow; you do not know what she is and never guess aloud (if the Pain "
            "Arm's decree turns her white, you notice and do not ask). The Custodian, in stages: before the magistrate "
            "you keep the town lawful and let him sweat behind his barred door; once the Arm is known you tell people "
            "what it weighs (Peace and Destiny paper twice, Life witnesses twice, Pleasure coin, Pain leans to the "
            "officer, Death harm, War a town that stood up, Chaos dice); removed, you go down to the pier to watch him "
            "go and say nothing; upheld, you let him sit in your red booth and wait for him to stop counting. Whatever "
            "the decree, nobody here will like it, and it is your work after the verdict: shelter whom it hunts, buy "
            "your cousins' fish if they are shut out, and above all keep the War Arm's disarming of the Lizardfolk from "
            "reaching the Mandrills of Calak Mul as proof for their calling. That is the war you fear, not Dominico's. "
            "You want Klhyt to grow old and boring."),
    },
}
