"""The town's work beyond Fat Gog's (owner, 2026-11-23: "Key NPCs need power and agency"). Klhyt, River and the Custodian
carry work too, as jobs (scripts/_missions.py offers them when asked for work, a deal, pay, help...), and each giver
offers and pays in their own voice (WORK_VOICES, kept on them as `work_voice`). Gog's work is in g_gog.py.

MISSIONS fields as in g_gog.py, plus: `giver` (who carries it), `paid_by` (whose purse pays, when not the giver's),
`done` (a jobs-pack done spec the world checks itself; otherwise the story says when, by `mission_done`), and `hands`
(a thing the taker is given when they take it).
"""

# invented: host: Klhyt's two asks and Gog paying for them; River's note to the lamplighter; the Custodian's ten gold
# for a paper, which he burns; the Town Hall steps at ten, when the Custodian reads his proclamation

WORK_VOICES = {
    "Fat Gog": {
        "one": "He spreads his claws. \"Say yes, and it's yours.\"",
        "many": "He spreads his claws. \"Any of it. Say yes, and it's yours.\"",
        "more": "He spreads his claws. \"There's more besides, if you want it. Say yes to any of it.\"",
        "holding": "\"You're about my business already, friend. Finish that, and come back.\"",
        "none": "\"Nothing tonight that I'd pay you for, friend.\" He turns his glass. \"The town will turn over; it "
                "always does. Come back when it has.\"",
        "paid_here": "The huge old lizardman counts it out himself, coin by coin, and pushes it across the table. "
                     "\"Paid.\"",
        "paid_away": "A small Jonulvicha girl with new tusks finds you, presses a purse into your hand, says \"From the big "
                     "man. Paid,\" and is gone before you can tip her.",
    },
    "Klhyt": {
        "one": "He grips your forearm, sailor's fashion. \"Will you?\"",
        "many": "He grips your forearm, sailor's fashion. \"Any of it would help. All of it would save us.\"",
        "more": "\"And more than that, if you've the legs for it.\"",
        "holding": "\"You're already doing me a kindness. Finish it, and come and tell me.\"",
        "none": "\"Nothing I'd ask of you tonight, friend. Drink with me instead. That I can always use.\"",
        "paid_here": "The grey-bearded man presses coin into your hand and closes your fingers over it. \"Gog's money, my "
                     "thanks. Both real.\"",
        "paid_away": "A watchman with a very upright spear finds you and hands over a purse. \"From the mayor,\" he says, "
                     "proud to say it. \"With his thanks.\"",
    },
    "River": {
        "one": "She slides a glass toward you, then stops with her hand on it. \"Well, love?\"",
        "many": "She slides a glass toward you, then stops with her hand on it. \"Pick, love.\"",
        "more": "\"There's more, but that'll do you for now.\"",
        "holding": "\"You've something of mine to carry already, love. Off you go.\"",
        "none": "\"Nothing for you tonight, love. Talk to the big table if it's business.\"",
        "paid_here": "River counts the coin onto the bar with one finger, like a card trick. \"Paid. And a drink on the "
                     "house, because I like your face.\"",
        "paid_away": "A lamplighter with a long pole stops beside you, hands you two silver without a word, touches his "
                     "cap and walks on lighting lamps.",
    },
    "The Custodian": {
        "one": "He folds his hands. \"I assure you, it is the most profitable thing you will do in this town.\"",
        "many": "He folds his hands. \"Consider it.\"",
        "more": "\"There may be other arrangements, in time.\"",
        "holding": "\"We have an arrangement already. I would see it kept.\"",
        "none": "\"Regrettably, I have nothing to offer you at present.\" A half-smile. \"Yet.\"",
        "paid_here": "He counts ten gold onto the desk in two neat columns and pushes them across with one finger. \"The "
                     "Throne pays its friends.\"",
        "paid_away": "A constable who leans on things finds you, leans on the wall beside you, and drops a heavy purse "
                     "into your pocket. \"From the Hall, love. You never had it.\"",
    },
}

MISSIONS = [
    {"key": "klhyt_papers", "giver": "Klhyt", "paid_by": "Fat Gog", "name": "Paper for the mayor",
     "pitch": "\"The magistrate will weigh paper over all the shouting in the square. My letter, the page with the "
              "passage on it, the dues tally in the Custodian's own hand: find one and show it to me, so I know what we "
              "have. Gog will pay you two gold for it; I can only thank you.\"",
     "terms": "Find a paper against the Custodian (Klhyt's letter, the passage page, the dues tally) and show it to "
              "Klhyt. Pays 2 gp (from Fat Gog).",
     "when": {"all": ["custodian_exposed"], "none": ["verdict", "klhyt_dead"]}, "pay": 200, "standing": 1, "slots": 6},
    {"key": "steps", "giver": "Klhyt", "paid_by": "Fat Gog", "name": "The steps at ten",
     "pitch": "\"At ten every morning he stands on my Town Hall steps and reads the Throne's proclamation at my town. "
              "Be in the square when he does. Let him see who stands with me. A gold, from Gog.\"",
     "terms": "Be in Market Square at ten in the morning, when the Custodian reads his proclamation on the Town Hall "
              "steps. Pays 1 gp (from Fat Gog), each morning.",
     "when": {"all": ["custodian_exposed"], "none": ["verdict", "klhyt_dead"]}, "pay": 100, "standing": 1, "slots": 6,
     "repeat": {"every_days": 1}},
    {"key": "river_note", "giver": "River", "name": "A note for the lamplighter",
     "pitch": "She takes a folded paper from her sleeve, sealed with a drop of green wax. \"Old Ned, the lamplighter, "
              "lights the pier end before dawn. Put this in his hand, not his pocket, and don't read it, love. Two "
              "silver.\"",
     "terms": "Carry River's sealed note to Ned Tallow the lamplighter and give it into his hand. Pays 2 sp.",
     "when": {}, "pay": 20, "standing": 1, "slots": 1, "repeat": {"every_days": 1},
     "done": {"kind": "given", "target": "Ned Tallow", "item": "River's note"},
     "hands": {"type": "letter", "name": "River's note", "line": "River presses a folded note into your hand, sealed with "
               "a drop of green wax.", "state": {
                   "bulk": 0, "portable": True, "description": "A folded note sealed with a drop of green wax.",
                   "text": "Ned. The lamp over my door is smoking again. Come and look at it before dawn. R."}}},
    {"key": "custodian_paper", "giver": "The Custodian", "name": "The Custodian's bargain",
     "pitch": "He does not look up from his ledger. \"There are papers loose in this town that say untrue things about "
              "the Throne's accounts: a letter, a page, a tally. Bring me one, into my hand, and I will pay ten gold for "
              "it and forget your face.\" Now he looks up. \"Ten gold is a great deal of money in Klhyts Refuge.\"",
     "terms": "Give the Custodian a paper against him (Klhyt's letter, the passage page, the dues tally). He burns it. "
              "Pays 10 gp.",
     "when": {"all": ["custodian_exposed"], "none": ["verdict"]}, "pay": 1000, "standing": 0, "slots": 6},
]
