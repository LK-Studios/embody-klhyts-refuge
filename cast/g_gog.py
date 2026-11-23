"""Fat Gog's work (owner, 2026-11-23: "We still go[t] shallow NPCs, fat gog has nothing to say despite being the main
person to go to for stuff and missions"). On the live world a player asked him twice for work and pay and got his line
about the Custodian both times: his table had no word for pay, and "custodian" outscores "work" (the table scores a
word by its length); his work line still sent people to the warehouse hours after Klhyt was home.

Here: his table reads the night's news in stages, answers work, pay, guarding, why, the hunters, the witnesses, the
ring and the elves, and steers anyone who asks him for anything toward what he would pay for. MISSIONS are his work as
jobs (the engine's jobs pack): each a promise he carries, offered aloud to whoever asks him for work while the story
wants it (`when`), checked by the world, paid from his own purse (scripts/_missions.py). Rewards are host defaults.
"""

# invented: host: Gog's rewards (five silver for a lead on Klhyt, five gold for him breathing, three silver a night to
# sit up with a witness, two gold a Fist man put down in a fair fight, five gold for what moves Dominico)
# invented: host: the thing in Dominico's ring shows to a sharp eye at the Apothecary (arcana, religion or
# investigation, DC 13): the candle leans toward the ring against the draught

WORK = ("work|job|jobs|hire|employ|useful|help|mission|missions|task|tasks|errand|errands|favour|favor|pay|paid|"
        "payment|reward|rewards|earn|coin|gold|money|offer|offers|contract|bounty|anything")

CAST = {
    "Fat Gog": {
        "brief_more": (
            "What moves the story now (owner, 2026-11-23: you are the main person to go to for work). You always have "
            "work and you always pay, from your own purse, what you promised. Your jobs are things you carry "
            "(offer_job, job: its name): Where my mayor went; Bring him breathing; Keep my books; The hooded "
            "household; Who pays for Dominico's nerve; Sit up with a witness; Papers for the magistrate; The "
            "Fist's dogs. Offer the ones the night calls for, in your own words, then with offer_job; the world "
            "checks the work and pays it. Answer what you are asked first: work and pay plainly, then the story. "
            "You never send anyone to the warehouse once Klhyt is home."),
        "dialog": {
            "work|job|jobs|hire|employ|useful|help|guild": None,  # retired: the guild has its own topic now
            WORK: {"line": "He sets his glass down, which is how you know he means it. \"Work.\" He counts it off on "
                           "his claws.",
                   "if_state": {"klhyt_dead": True},
                   "else": "He sets his glass down, which is how you know he means it. \"Work. Good. I always have "
                           "work, friend, and I always pay.\" He counts it off on his claws."},
            "shadows|underworld|thieves|people|hessa|wick|marlo|door|fence|eyes|runner": None,
            "shadows|underworld|thieves|guild|people|hessa|wick|marlo|door|fence|eyes|runner":
                "\"The guild is a word people use. I keep the town's shadows tidy.\" He counts on three claws. \"Hessa "
                "keeps my door and says no like a gate closing. Wick is my eyes in the market; pay her in copper and "
                "she tells you the truth. Marlo on Harbour Street buys what falls off ships, and pays me so nothing "
                "falls off mine.\"",
            "hello|hi|hey|evening|ahoy|greetings|howdy|morning": {
                "if_state": {"klhyt_dead": True},
                "line": "He does not lift his claw. \"Sit, friend. We buried a friend of mine. Sit anyway.\"",
                "else": {"if_state": {"klhyt_home": True},
                         "line": "He lifts one claw an inch off the table. \"Evening, friend. You'll have heard: he's "
                                 "home. Now comes the hard part, which is keeping him there.\" He waits. \"If it's "
                                 "work you want, say so. I have it.\"",
                         "else": {"if_state": {"guild_hit": True},
                                  "line": "He lifts a claw an inch off the table. \"Evening, friend. Mind the glass "
                                          "on the floor. We had visitors at the bell.\"",
                                  "else": "He lifts one claw an inch off the table, which from him is a bow. "
                                          "\"Evening, friend. Sit, if the chair will have you.\" He waits. \"Most "
                                          "people who come to this table want something. Work, a favour, a name. "
                                          "Say which.\""}}},
            "klhyt|mayor|founder|friend": {
                "if_state": {"klhyt_dead": True},
                "line": "For a long time he says nothing at all. \"I carried him up the sand once,\" he says at last. "
                        "\"Somebody will carry him down it now. And somebody will answer for it.\"",
                "else": {"if_state": {"klhyt_home": True},
                         "line": "His eyes close all the way, and for a moment he only breathes. \"He's home. He's "
                                 "been at this table twice, and wept both times, and so did I.\" The eyes open. \"Now "
                                 "the Custodian sits in the Hall in the Throne's name, waiting for a magistrate, and "
                                 "Dominico's dogs are off the leash. Keeping him home is the work now.\"",
                         "else": "His eyes half close. \"I found that man on the beach, his tongue black from "
                                 "thirst, and carried him up the sand. Four nights gone now. The Custodian says "
                                 "upriver.\" A long breath through the nostrils. \"Klhyt never had business upriver "
                                 "in his life. Bring me something I can hold, and I'll pay for it.\""}},
            "guard|guarding|protect|protecting|protection|tomorrow|bodyguard|keep|keeping|watch|watching": {
                "if_state": {"klhyt_home": True},
                "line": "\"In the square, the whole town is his guard.\" He taps the table. \"It's the small hours I "
                        "worry about. The Throne's officer calls on people at night, the ones who might speak for "
                        "Klhyt to the magistrate: the harbourmaster, that red-faced boy Tully. Sit up with one of them "
                        "past two in the morning and the officer finds company. I pay for that.\"",
                "else": "\"Guard my mayor?\" Something like a smile. \"Find him first, friend. Then we'll talk about "
                        "guarding.\""},
            "why|reason|kindness|bother|worth|care|matters|matter|cause": (
                "\"Why?\" He considers you the way a heron considers water. \"Because this is the one town on this "
                "coast where nobody asks where you came from. Not the Throne, not the Fist, not me. That's worth more "
                "than my coin.\" He pushes a small stack of silver an inch toward you, and leaves it there. \"But "
                "you'll have my coin too. Kindness is cheaper when it's paid.\""),
            "fennick|fennicks|ott|jory|sabeth|hunters|hunted|hunting|marked|ambush|dogs|kill|killers|thugs": {
                "if_state": {"klhyt_home": True},
                "line": "\"Dominico let me be, and set his dogs on the ones who helped me.\" His claws settle on the "
                        "table, very gently. \"That is a coward's arithmetic. Put one of them on the ground in a fair "
                        "fight, and come and tell me. I pay two gold a dog, and the doctor.\" He leans in a little. "
                        "\"And when they come for you, come here. They don't come through my door.\"",
                "else": "\"Dominico's men: the big sandy one with the hammer, his wiry brother, the woman with the "
                        "little book who counts everything.\" He smooths his lapel. \"They don't come through my "
                        "door. Remember that, if you ever need a door.\""},
            "ring|rings|whisper|whispers|voice|candle|nerve|spine|iron|patron|paying|backing|behind|magic": (
                "\"Somebody is paying for Dominico's nerve, or something is.\" He turns his own glass slowly on the "
                "table, round and round. \"He never used to turn that ring. Now he never stops. Go and watch him at "
                "his table at the Apothecary, friend, with whatever eyes you have for that kind of thing, and tell me "
                "what you see. Five gold for something I can believe.\""),
            "witness|witnesses|teague|tully|voss|officer|warrant|wanted|notice|arrest|throne": (
                "\"The Custodian can't win in the square, so he means to win in the small hours.\" He breathes out "
                "through his nose. \"The officer in blue and the constable who leans on things call on whoever might "
                "speak for Klhyt. A witness they find alone remembers nothing by morning. Sit up with one, friend. "
                "Three silver a night, and the magistrate hears the truth.\""),
            "elf|elves|ithriel|moonmoth|unicorn|hooded|household|exiles": (
                "\"The hooded one who reads by candlelight at the Unicorn, and the four who sit in her corners.\" He "
                "nods slowly. \"They want the pale ship at the end of the pier, and the officer in blue wants them. "
                "Walk them down to the water, friend. I'll give you a gold for it; they'll give you something better.\""),
        },
        "default_line": [
            "He folds his hands on his belly and lets the silence do the asking. \"Take your time, friend. If it's "
            "work, say so; I always have it.\"",
            "He lifts one finger; across the room a glass is filled for you without a word. \"Try it plainer. I'm "
            "old, not slow. Work, a favour, a name: which?\"",
            "\"Mm.\" He watches the door over your shoulder. \"If it's gossip you want, find the little one with new "
            "tusks in the market. If it's work, you've found me.\"",
            "He breathes out slowly through his nostrils, a sound like a bellows at rest. \"I've heard a great many "
            "things at this table, friend. Ask me about work, or the mayor, or Dominico's dogs. Those I'll answer.\"",
        ],
    },
}

# Gog's work, as jobs he carries. `when`: story facts that must all hold (`all`), must none hold (`none`), and
# `any_marked` (someone the Fist has marked). `pitch` is what he says when he offers it; `terms` is the job card.
MISSIONS = [
    {"key": "mayor", "name": "Where my mayor went",
     "pitch": "\"Where my mayor went. Bring me something I can hold: a thing of his, a paper, a name in ink. Five silver.\"",
     "terms": "Find out where Klhyt is and show Fat Gog proof he can hold (a thing of Klhyt's, a paper, a name in ink). "
              "Pays 5 sp.",
     "when": {"none": ["gog_knows", "klhyt_freed", "shipped"]}, "pay": 50, "standing": 1, "slots": 6},
    {"key": "breathing", "name": "Bring him breathing",
     "pitch": "\"Take my marker to the warehouse and bring Klhyt to me breathing, before the one o'clock tide. Five "
              "gold, and my thanks, which are worth more.\"",
     "terms": "Get Klhyt out of the bonded warehouse alive before the one o'clock tide. Pays 5 gp to whoever cuts him "
              "loose, or stands with them when they do.",
     "when": {"all": ["gog_knows"], "none": ["klhyt_freed", "shipped"]}, "pay": 500, "standing": 2, "slots": 6},
    {"key": "books", "name": "Keep my books",
     "pitch": "\"Dominico comes for my books at the midnight bell. Be in my house when he does, and let his men see "
              "who's waiting. Three gold.\"",
     "terms": "Be in the Stripperwitch at the midnight bell, when Dominico's men come for Fat Gog's books. Pays 3 gp.",
     "when": {"none": ["dominico_backed", "midnight_rung", "klhyt_freed"]}, "pay": 300, "standing": 1, "slots": 6},
    {"key": "witnesses", "name": "Sit up with a witness",
     "pitch": "\"The officer in blue calls on whoever might speak for Klhyt, in the small hours. Sit up with the "
              "harbourmaster, or the red-faced boy, past two in the morning, and he finds company. Three silver a "
              "night.\"",
     "terms": "Be with a witness the town has found (Harbourmaster Teague, or Tully) when the Throne's officer calls, "
              "after two in the morning. Pays 3 sp a night.",
     "when": {"all": ["custodian_exposed"], "none": ["verdict"]}, "pay": 30, "standing": 1, "slots": 6,
     "repeat": {"every_days": 1}},
    {"key": "papers", "name": "Papers for the magistrate",
     "pitch": "\"The magistrate is ashore. Show them what you found: the letter, the passage, the tally. Paper wins "
              "where words don't. Three gold.\"",
     "terms": "Show the magistrate a paper against the Custodian (Klhyt's letter, the passage page, the dues tally) "
              "before the hearing. Pays 3 gp.",
     "when": {"all": ["custodian_exposed", "magistrate"], "none": ["verdict"]}, "pay": 300, "standing": 1, "slots": 6},
    {"key": "dogs", "name": "The Fist's dogs",
     "pitch": "\"Dominico has set his dogs on people who helped me. Put one of them on the ground in a fair fight and "
              "tell me. Two gold a dog, and the doctor. And when they come for you, come here: they don't come "
              "through my door.\"",
     "terms": "Put one of Dominico's Fist on the ground in a fight. Pays 2 gp each time.",
     "when": {"any_marked": True}, "pay": 200, "standing": 1, "slots": 6, "repeat": "always"},
    {"key": "iron", "name": "Who pays for Dominico's nerve",
     "pitch": "\"Somebody, or something, is paying for Dominico's nerve. Watch him at his table at the Apothecary, the "
              "ring he keeps turning, with whatever eyes you have for that kind of thing, and come and tell me. Five "
              "gold.\"",
     "terms": "Watch Dominico at the High Apothecary (arcana, religion or investigation) and tell Fat Gog what moves "
              "him. Pays 5 gp.",
     "when": {"none": ["iron_known"]}, "pay": 500, "standing": 2, "slots": 6},
    {"key": "elves", "name": "The hooded household",
     "pitch": "\"The hooded one at the Unicorn and her four want the pale ship at the end of the pier, and the "
              "officer in blue wants them. Walk them down. A gold from me.\"",
     "terms": "Ask the hooded elf at the Touchy Unicorn about passage and walk her household to the Moonmoth at the "
              "docks. Pays 1 gp.",
     "when": {"none": ["elves_aboard", "escort_by"]}, "pay": 100, "standing": 1, "slots": 1},
]
