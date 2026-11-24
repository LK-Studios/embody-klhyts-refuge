"""Shalamar - Klhyts Refuge. A world for embody, imported from the LoreKeeper world "Shalamar Est: 1988".

    uv run embody --as gm --author load klhyts-refuge
    uv run embody --as you join klhyts-refuge Newcomer
    uv run embody --as you perceive

The continent is Shalamar, the jungle New World, not Landfall. The town is Klhyts Refuge before the war: the nicest
town in Shalamar, colonial timber and good pubs, where people come to hide from the mainland. Races mix freely and
Lizardfolk are tolerated. Fat Gog runs the guild. Dominico, not yet sworn to anything darker, is leaning on the guild.
Klhyt, the town's founder and mayor, is missing, and the Custodian runs the town in his absence.

Rules: the d20 pack (checks, threaten, parley, factions with standing, thirst), fought by the dnd5e pack (D&D 5e combat:
initiative and turns, armour class, damage dice, death saves, conditions, spells), the sheet pack (D&D-style ability
scores on a sheet: STR force, DEX poise, CON endurance, INT cognition, WIS acuity, CHA projection), the village pack
(walk, carry, give, talk) and locks. The world's own scripts: buy (coin for what a keeper sells), drink (ale and rum
drunk for the taste; three in an hour and you are unsteady), hire (the one way a player gets a second agent: hire
someone in the world, on their terms, and claim their seat) and the storyline.

Canon comes from LoreKeeper; what had to be invented is listed in notes/invented.md.
"""

import importlib.util as _ilu
import random as _random
from pathlib import Path as _Path

from packs.d20.pack import install_rules
from packs.dnd5e.pack import armor as armor5, character, class_hp, install_rules as install_5e, weapon as weapon5
from packs.jobs.pack import install_rules as install_jobs
from packs.burial.pack import install_rules as install_burial
from packs.beasts.pack import install_rules as install_beasts

WORLD = {
    "id": "klhyts-refuge",
    "name": "Embody - Klhyts Refuge",
    "seed": 1988,
    "description": "Shalamar, before the war. Klhyts Refuge, the nicest town on the continent: taverns, inns and "
                   "docks, refugees from Landfall, Lizardfolk tolerated. Fat Gog's guild is under threat and the "
                   "founder is missing.",
    "requires": ["village", "d20", "sheet", "dnd5e", "locks", "jobs", "burial", "beasts"],
}

# ---- 5e on the sheet pack ----------------------------------------------------------------------------------------
# The sheet's modifier is 5e's own ((score - 10) // 2), so ability scores copy across. The other six attributes stay 10.
ABILITY = {"str": "force", "dex": "poise", "con": "endurance", "int": "cognition", "wis": "acuity", "cha": "projection"}

# 5e's skills, added to the d20 pack's skillbook as data. Keys are single words a player can type.
SKILLS_5E = {
    "athletics": {"primary": "force", "secondary": None, "scope": "climbing, swimming, shoving, grappling", "related": ["brawl", "climb"]},
    "acrobatics": {"primary": "poise", "secondary": None, "scope": "balance, tumbling, keeping your feet", "related": []},
    "sleight": {"primary": "poise", "secondary": None, "scope": "sleight of hand: palming, picking pockets", "related": ["stealth"]},
    "arcana": {"primary": "cognition", "secondary": None, "scope": "magic, spells, old sigils", "related": ["lore"]},
    "history": {"primary": "cognition", "secondary": None, "scope": "Landfall, Vorkathia, the colonies, who did what", "related": ["lore"]},
    "investigation": {"primary": "cognition", "secondary": None, "scope": "searching, reading clues, working things out", "related": []},
    "nature": {"primary": "cognition", "secondary": None, "scope": "the jungle, beasts, plants, weather", "related": ["survival"]},
    "religion": {"primary": "cognition", "secondary": None, "scope": "Vorkath, the jungle gods, rites", "related": ["lore"]},
    "animals": {"primary": "acuity", "secondary": None, "scope": "animal handling: calming, riding, reading beasts", "related": []},
    "insight": {"primary": "acuity", "secondary": None, "scope": "reading people, spotting a lie", "related": []},
    "medicine": {"primary": "acuity", "secondary": None, "scope": "wounds, fever, poison", "related": ["survival"]},
    "perception": {"primary": "acuity", "secondary": None, "scope": "noticing, listening, spotting", "related": []},
    "deception": {"primary": "projection", "secondary": None, "scope": "lying, bluffing, disguise", "related": []},
    "intimidation": {"primary": "projection", "secondary": None, "scope": "menace, hard words", "related": ["resolve"]},
    "performance": {"primary": "projection", "secondary": None, "scope": "song, story, the stage", "related": []},
    "persuasion": {"primary": "projection", "secondary": None, "scope": "winning people round, honestly", "related": ["parley"]},
    "sailing": {"primary": "poise", "secondary": "acuity", "scope": "ships, knots, weather, the sea", "related": ["athletics"]},
}


def sheet(scores, skills=None):
    """A 5e statline as an embody sheet. scores: {"str": 16, ...}; skills: {"perception": 2, ...} (rank = proficiency)."""
    attrs = {a: 10 for a in ["force", "poise", "endurance", "acuity", "cognition", "discipline", "tenacity",
                             "comprehension", "projection", "coherence", "persistence", "attunement"]}
    for k, v in scores.items():
        attrs[ABILITY[k]] = int(v)
    return {"attributes": attrs, "skills": dict(skills or {}), "xp": {}}


def d20_stats(scores):
    """The d20 pack's three raw stats from 5e scores (rules that read body/wits/will raw still see sensible numbers)."""
    mod = lambda k: max(0, min(5, (int(scores.get(k, 10)) - 10) // 2))
    return {"body": max(mod("str"), mod("con")), "wits": max(mod("dex"), mod("int"), mod("wis")), "will": max(mod("wis"), mod("cha"))}


def body(scores, skills=None, hp=None):
    """A sheet body's state: the sheet, the raw stats, and hit points."""
    st = {"sheet": sheet(scores, skills), **d20_stats(scores)}
    if hp:
        st.update({"hp": hp, "max_hp": hp})
    return st


# ---- what things can do --------------------------------------------------------------------------------------------

PERSON_ACTIONS = {
    "go": {"script": "go", "doc": "Walk to a connected place", "targets": "place", "scope": "exits", "duration": 60},
    "take": {"script": "take", "doc": "Pick something up", "targets": "thing", "scope": "here"},
    "drop": {"script": "drop", "doc": "Put down something you hold", "targets": "thing", "scope": "held"},
    "put": {"script": "put", "doc": "Put something you hold onto or into something here (a shelf, a chest)",
            "targets": "thing", "scope": "here", "listed": "ok",
            "params": {"item": "id or name of a thing you hold", "count": "how many of a stack"}},
    "give": {"script": "give", "doc": "Hand something you hold to someone here", "targets": "creature", "scope": "here",
             "params": {"item": "id or name of a thing you hold", "count": "how many of a stack"}},
    "show": {"script": "show", "doc": "Show something you hold to someone here; they read it, you keep it",
             "targets": "creature", "scope": "here", "params": {"item": "id or name of a thing you hold"}},
    "talk": {"script": "talk", "doc": "Talk to someone about something", "targets": "creature", "scope": "here",
             "duration": 30, "params": {"about": "the topic, in your words"}},
    "buy": {"script": "buy", "doc": "Buy something from someone here who sells it, for coin",
            "targets": "creature", "scope": "here", "listed": "ok", "duration": 30,
            "params": {"item": "what you want (leave it out to hear what they sell)"}},
    "follow": {"script": "follow", "doc": "Go where they go, until you stay", "targets": "creature", "scope": "here"},
    "stay": {"script": "stay", "doc": "Stop following"},
    "watch": {"script": "watch", "doc": "Look into the next place without stepping in", "targets": "place",
              "scope": "exits", "duration": 15},
    "free": {"script": "free", "doc": "Cut or untie someone who is tied up", "targets": "creature", "scope": "here",
             "listed": "ok", "duration": 30},
    "hire": {"script": "hire", "doc": "Hire someone here who works for hire, on their terms: ask bare to hear their price",
             "targets": "creature", "scope": "here", "listed": "ok", "duration": 60,
             "params": {"days": "how many days to pay for, up front, when they work for coin"}},
    "dismiss": {"script": "dismiss", "doc": "Let someone in your hire go before their days are up; nothing is paid back",
                "targets": "creature", "scope": "here", "listed": "ok"},
    # the village pack's words on things (the owner, 2026-11-23: "A few time we encounter paper or books and no ability
    # to write on things", then "Chalkboards etc messages, scratching into wood"): each offered only where it works
    "read": {"script": "read", "doc": "Read what is written on it", "targets": "thing", "listed": "ok"},
    "write": {"script": "write", "doc": "Write on it: paper and books take ink, a slate or a door chalk, wood a blade",
              "targets": "thing", "listed": "ok", "duration": 10, "params": {"text": "the words"}},
    "carve": {"script": "write", "doc": "Carve words into wood with a knife or a blade in your hand",
              "targets": "thing", "listed": "ok", "duration": 60, "params": {"text": "the words, short"}},
    "wipe": {"script": "wipe", "doc": "Wipe the chalk off a slate or a door", "targets": "thing", "listed": "ok",
             "duration": 5},
    # the town's animals (scripts/pet.py; feed, gentle, come and stay are the beasts pack's own, on the animal)
    "pet": {"script": "pet", "doc": "Pet an animal here: a scratch behind the ears, and see what it makes of you",
            "targets": "beast", "scope": "here", "listed": "ok", "duration": 5},
    # the d20 pack's own, listed only where they would work, so a card does not offer to drink a coin
    "drink": {"script": "drink", "doc": "Drink from a cup, a skin or a well within reach: ale and rum for the taste, water for thirst",
              "targets": "thing", "scope": "any", "listed": "ok", "duration": 30},
    "fill": {"script": "fill", "doc": "Fill a skin you hold at a source here", "targets": "thing", "scope": "held",
             "listed": "ok", "duration": 30},
    "crawl": {"script": "crawl", "doc": "Drag yourself to a connected place, even when down", "targets": "place",
              "scope": "exits", "listed": "ok", "duration": 120},
    # a villain's own orders, one verb each, held only by those the cast gives them (cast/f_peril.py, scripts/order.py)
    "order": {"named_by": {"key": "orders", "doc": "doc"}, "script": "order", "doc": "An order of your own",
              "params": {"who": "the name of the one it is about"}},
}


def define(s):
    """Schemas. Scripts come from scripts/ and the packs. Safe to run again on a live world."""
    s.define_schema("person", extends="combatant",
                    doc="Someone of the Refuge: walks, carries, talks, buys, and is bound by the d20 rules.",
                    state={"dialog": {}, "default_line": "Hm.", "gives": {}, "gave": {}, "asleep": False,
                           "follows": None, "secret": ["dialog", "gives", "gave"]},
                    actions=PERSON_ACTIONS,
                    listeners=[{"script": "person_on", "kinds": ["talked"], "unless_embodied": True}])
    s.define_schema("fighter", extends="person",
                    doc="A person who fights without a mind: back at whoever strikes them, and at anyone their side has outlawed.",
                    behaviors=[{"script": "fighter_tick", "every": 30}])
    s.define_schema("sign", extends="thing", doc="Something with writing on it, fixed in place. A notice board or a slate takes more.",
                    state={"text": "", "portable": False},
                    actions={"read": {"script": "read", "doc": "Read what is written"}})
    s.define_schema("animal", extends="beast",
                    doc="One of the town's animals (the beasts pack's beast): feed it, gentle it, pet it; talked to, it "
                        "answers in its own way.",
                    state={"dialog": {}, "default_line": [], "lines": "quoted", "secret": ANIMAL_SECRET},
                    listeners=[{"script": "person_on", "kinds": ["talked"], "unless_embodied": True}])
    s.define_schema("letter", extends="thing", doc="Paper: rides in a pocket, burns, and takes writing.",
                    state={"text": "", "portable": True, "bulk": 0, "burnable": True, "writable": True},
                    actions={"read": {"script": "read", "doc": "Read what is written"}})
    s.define_schema("guard", extends="fighter",
                    doc="One of Dominico's men on a post. Coin enough, Fat Gog's marker, or a hard look will move him.",
                    listeners=[{"script": "guard_on", "kinds": ["given", "shown", "cowed"], "unless_embodied": True}])
    s.define_schema("food", extends="thing", doc="Something to eat.", state={"portable": True, "kind": "food"},
                    actions={"eat": {"script": "eat", "doc": "Eat it", "duration": 60}})
    s.define_schema("dice", extends="thing", doc="Dice anyone can throw; the room sees what comes up.",
                    state={"portable": True, "dice": "2d6"},
                    actions={"throw": {"script": "throw", "doc": "Throw the dice: everyone here sees the total"}})
    s.define_schema("bath", extends="thing", doc="The High Apothecary's lemon bath.", state={"portable": False},
                    actions={"bathe": {"script": "bathe", "doc": "Take the lemon bath (you need a bath token)", "duration": 600}})
    s.define_schema("crowd", extends="thing", doc="A crowd: place state, not a hundred bodies. Mingle to overhear; hail someone out of it.",
                    state={"portable": False, "rumours": [], "mix": {"human": 1}, "max_faces": 6, "faces": 0, "heard": {},
                           "secret": ["heard", "mix"]},
                    actions={"mingle": {"script": "crowd_mingle", "doc": "Mingle: overhear what the crowd is saying", "duration": 120},
                             "hail": {"script": "crowd_hail", "doc": "Call someone out of the crowd to talk to", "duration": 60}})
    s.define_schema("ship", extends="thing", doc="A ship at her moorings: seen from the pier, not boarded.",
                    state={"portable": False})
    s.define_schema("elfship", extends="place", doc="The Moonmoth: elves board freely, others only with an elf's silverleaf token.",
                    listeners=[{"script": "gangplank", "kinds": ["before_act", "arrived"]}])
    s.define_schema("story", extends="entity", doc="The rails. Hidden; holds the facts the story has seen.",
                    state={"hidden": True})


# ---- the canon and the table's word ----------------------------------------------------------------------------------

POLICY = {
    "fixed": [
        "Shalamar before the war: no infection, no Lizardfolk army, Santa Guistina still stands, Kteol sleeps",
        "the Custodian skims the top, Dominico keeps the peace with a fist, Fat Gog owns the shadows",
        "Fat Gog is the guild master; Dominico is the Custodian's enforcer and not, yet, master of anything",
        "six taverns, their prices and their crowds, as the LoreKeeper taverns doc gives them",
        "money is copper, silver and gold pieces; 10 cp to the sp, 100 cp to the gp",
        "Lizardfolk are tolerated in town; tension is rising, but nobody has drawn steel over it yet",
        "Klhyt, a castaway, founded the town; he is missing and the Custodian runs it",
        "what happened to Klhyt and where he is (notes/bible.md); the tide and the midnight deadline (timers() says when)",
    ],
    "fill": True,    # small things a port town would have may be spawned with state {"improvised": true}
    "voice": True,   # people may say free lines through say_as when their table has no answer, in their own voice
}

AMBIENT = {"era": "before the war: before the mushroom, before the walls came down",
           "time_of_day": "late evening, half past ten", "weather": "hot, wet and still; the sea breeze has given up",
           "light": "lamplight, torchlight and the harbour lanterns"}

# the evening starts at half past ten on the first day: the clock is stepped there before anyone exists, so it costs
# nothing, and the timers count from it
START = 22.5 * 3600

# what join hands everyone who comes in (players and minds alike): the town, the hour, and where a newcomer stands
BRIEFING = ("Shalamar, before the war. Klhyts Refuge, the nicest town on the continent: six taverns, the inns, the market "
            "and the docks, with refugees from Landfall, Lizardfolk tolerated, elves in exile and Xoton sailors ashore. Fat "
            "Gog's guild is under threat, the founder Klhyt is missing, and the Custodian runs the town in his absence. It "
            "is half past ten at night. Whoever comes to play comes ashore at the docks, off a boat from somewhere else, "
            "and nobody here asks where from.")
HIRE_BRIEF = ("Hired help: some people here work for hire, each on their own terms (coin by the day, a thing they want, "
              "a favour done first); `hire` them bare to hear the price. Hiring someone is the only way to bring a second "
              "agent into the Refuge: the hire offers you their seat, and claim_seat gives you a paste for an agent of "
              "their own, until the days you paid for run out. You keep 1 + your Charisma modifier in your hire at once.")
# The pause while an agent asks the world, in a DM's voice (owner, 2026-11-22: on the phone it kept saying "One moment,
# let me check on that")
TABLE_BRIEF = ("At this table: you are the Dungeon Master for your human, and the world is behind your screen. When you "
               "turn to it to see what happens, never say \"one moment\", \"let me check\" or \"looking that up\": a DM "
               "never leaves the table. Fill the pause the way a DM would, in a line at most: lean into the moment "
               "(\"Let's see if the lock gives...\"), call for the dice (\"Roll for it.\" or \"The dice rattle behind the "
               "screen...\"), or give the room a beat (\"The fiddler misses a note; every drinker at the bar suddenly "
               "finds their mug fascinating.\"). Then tell what happened. Your human may be listening, not reading (a "
               "voice game on a phone): say who speaks before they speak, give each person their own rhythm and pet "
               "words so they sound like nobody else in one voice (Fat Gog slow and rumbling, River quick and dry, "
               "Kael loud and short), and keep to short spoken sentences, with no lists, symbols or headings.")
# Show, don't tell (owner, 2026-11-23: "the narrator tells the users too much. Often should describe what people look
# like rather then outright just say who they are and what they are going to do")
SHOW_BRIEF = ("People are seen before they are named: bring everyone in by what your human's character can see and hear "
              "(a look, what they are doing, how they sound), never by their name, title or what they are up to. A name "
              "comes when someone says it, or when they give it themselves; a job, a plan or a secret comes only from what "
              "is said, seen or found. The world shows you names and descriptions so you can keep track; your human gets "
              "only what their character would notice, one or two telling details at a time, never a whole description "
              "read out. Never say what someone is about to do, what they want or what they hide. When someone answers "
              "with a line that does not fit the question, that is them dodging or steering: play it as their character. "
              "People here have their own days: they come and go, so a room is not always as you left it.")
BRIEFING = BRIEFING + " " + HIRE_BRIEF + " " + TABLE_BRIEF + " " + SHOW_BRIEF
BRIEF_ADDENDA = [("Hired help:", HIRE_BRIEF), ("At this table:", TABLE_BRIEF),  # each added once, to what the root says
                 ("People are seen before they are named:", SHOW_BRIEF)]
# an invite's steps for Claude: name the connector this, then say "Play <this>" in a chat (the owner's words, 2026-11-22)
CONNECTOR_NAME = "Embody Klhyts Refuge"
PLAY_NAME = "Klhyts Refuge"

COIN = {"kind": "cp", "portable": True, "bulk": 0,
        "description": "Mixed coin, counted in copper: 100 to the gold piece, 10 to the silver."}


def coin(n):
    return {**COIN, "count": n}


def hp(five_e):
    """5e hit points, whole: the dnd5e pack fights by 5e's numbers (they were a quarter under d20's blows)."""
    return int(five_e)


def cup(name, desc, empty="An empty mug, sticky inside.", left=1):
    return {"type": "thing", "name": name, "state": {"kind": "drink", "strong": True, "left": left,
                                                     "description": desc, "description_empty": empty}}


def dish(name, desc, line):
    return {"type": "food", "name": name, "state": {"description": desc, "eaten_line": line}}


def fed_on(item, food, feeds=1):
    """What an animal eats of it too (the beasts pack's feed): its diet tag and how many meals it is."""
    return {**item, "state": {**item["state"], "food": food, "feeds": feeds}}


def token(name, desc, **extra):
    return {"type": "thing", "name": name, "state": {"description": desc, "bulk": 0, **extra}}


def arm(base, desc, **over):
    """A weapon from 5e's table (packs/dnd5e WEAPONS) with this world's look; over sets any key (kind, bonus)."""
    return weapon5(base, description=desc, **over)


DAGGER = arm("dagger", "A plain knife, honest steel.")
CUDGEL = arm("club", "A length of oak wrapped in tarred cord.")

# ---- the taverns: canon prices (LoreKeeper "Klhyts Refuge Taverns"), kept in copper ------------------------------------

BOARD_OMBERHULK = ("THE OMBERHULK & NUN. Ale 1cp. Mead 2cp. Wine 2cp. Room 1cp. Bath 4cp. Suite 1sp. Company 1cp. "
                   "Ask for Beatrice, Susan and Phillip's spuds. Music runs late.")
BOARD_UNICORN = ("THE TOUCHY UNICORN. Scraps free. Ale 1cp. Mead 2cp. Wine 2cp. Room 1cp, bath included. Suite 1sp. "
                 "Grub 2cp. Food 5cp. The library is for guests. Quiet, please.")
BOARD_OGRE = "RAMPANT OGRE & CURVED CLEAVER. Everything 1cp. Room 4cp. Company 1cp. No bath. No suite. No food worth mentioning."
BOARD_TURTLE = ("THE TURTLE DRAGON. Ale 1cp (double). Mead 1cp. Wine 1cp. Room 4cp. Bath 3cp. Grub 1cp. Food 3cp. "
                "Oysters. Scraps free with beer. Passage to Catan arranged. Avoid the wine.")
BOARD_APOTHECARY = ("THE HIGH APOTHECARY. Ale 3cp. Mead 5cp. Wine 5cp to 50gp. Room 1gp. Company 5cp. Lemon bath 1gp. "
                    "Suite 10gp. Grub 1gp. Food 3gp.")
BOARD_STRIPPERWITCH = ("THE STRIPPERWITCH. Ale 1cp. Mead 2cp. Wine 2cp to 50gp. Room 1sp. Company 1gp. Bath 1sp. Suite 5gp. "
                       "Grub 1sp. Food 5cp. Scraps 1cp.")

SELLS_OMBERHULK = {
    "ale|beer": {"price": 1, **cup("Mug of ale", "A mug of thin brown ale, warm as the room.")},
    "mead": {"price": 2, **cup("Cup of mead", "Sweet, cloudy mead with something floating in it.")},
    "wine": {"price": 2, **cup("Cup of wine", "Red wine, rough enough to scour a pot.", "An empty cup, stained red.")},
    "spuds|potatoes|food|beatrice|susan|phillip": {"price": 3, **dish("Plate of spuds",
        "Beatrice, Susan and Phillip's spuds: a heap of fried potatoes the size of a cat, salted like the sea.",
        "The spuds are, against all odds, wonderful.")},
    "room|bed": {"price": 1, **token("Room key (Omberhulk & Nun)", "A brass key on a leather tag. The room is hot and the bugs get in.")},
    # the healers, 2026-11-23: she left the order, and the order's prayers did not leave her (scripts/healing_rule.py)
    "blessing|bless|prayer|pray|heal|healing|cure|wounds|hurt": {"price": 50, **token(
        "Sister Agathe's blessing", "Five silver in the poor box and her hand on your head.", portable=True,
        treatment="blessing", heals="1d8+3")},
    "stitches|stitch|stitching|thread|needle|sew": {"price": 1, **token(
        "Sister Agathe's stitches", "A copper for the thread, and her needle through your hide.", portable=True,
        treatment="stitches", heals="1d4")},
}
SELLS_UNICORN = {
    "scraps": {"price": 0, **fed_on(dish("Scraps", "Yesterday's bread and the end of a cheese.", "Scraps, but honest ones."), "scraps")},
    "ale|beer": {"price": 1, **cup("Mug of ale", "A mug of decent ale, cool from the cellar.")},
    "mead": {"price": 2, **cup("Cup of mead", "Clear golden mead.")},
    "wine": {"price": 2, **cup("Cup of wine", "A quiet white wine.", "An empty cup.")},
    "grub": {"price": 2, **dish("Bowl of grub", "Bean stew with a heel of bread.", "Plain food, and plenty of it.")},
    "food|supper|meal": {"price": 5, **dish("Supper", "Roast fowl with yams and greens.", "Better than the place has any right to serve.")},
    "room|bed": {"price": 1, **token("Room key (Touchy Unicorn)", "A wooden key tag carved with a unicorn. The rooms are quiet. The pond bugs are not.")},
}
SELLS_OGRE = {
    "ale|beer": {"price": 1, **cup("Mug of ale", "Ale, probably.")},
    "rum": {"price": 1, **cup("Tot of rum", "Black rum in a chipped tot glass. It bites.", "A chipped tot glass, empty.")},
    "stew|food|grub": {"price": 1, **dish("Bowl of something", "Something in a bowl. It was an animal once.", "You eat it. You do not ask.")},
    "room|bed": {"price": 4, **token("Honeymoon Suite key", "A bent nail on a string. The Honeymoon Suite is three dog pelts on a flea-ridden bed.")},
}
SELLS_TURTLE = {
    "ale|beer": {"price": 1, **cup("Massive beer", "A beer twice the size of any beer has a right to be.", "A huge empty tankard.", 2)},
    "mead": {"price": 1, **cup("Cup of mead", "Mead, served in a scallop shell for no good reason.")},
    "wine": {"price": 1, **cup("Cup of wine", "The wine. You were warned.", "An empty cup. Your teeth feel loose.")},
    "oysters|oyster|food": {"price": 3, **dish("Plate of oysters", "A dozen oysters on ice that was ice an hour ago.",
                                               "The oysters taste of the whole sea.")},
    "grub|chowder": {"price": 1, **dish("Bowl of chowder", "Fish chowder, heavy on the fish.", "Hot, salty and gone.")},
    "room|bed": {"price": 4, **token("Room key (Turtle Dragon)", "A key on a cork float, in case you drop it in the harbour.")},
    "passage|catan|berth|ticket": {"price": 200, **token("Passage to Catan",
                                                          "A berth on the Emerald Eye, sailing for Catan on the one o'clock tide. Paid.",
                                                          passage="catan")},
}
SELLS_APOTHECARY = {
    "ale|beer": {"price": 3, **cup("Glass of ale", "Pale ale in a cut-glass goblet.", "An empty cut-glass goblet.")},
    "mead": {"price": 5, **cup("Glass of mead", "Spiced mead, warmed.", "An empty glass.")},
    "wine": {"price": 5, **cup("Glass of house wine", "A good red, honestly priced, for once.", "An empty wine glass.")},
    "vintage|bottle": {"price": 5000, **cup("Bottle of Landfall vintage", "Fifty gold pieces of wine older than you are.",
                                              "An empty bottle that cost fifty gold.", 4)},
    "grub|soup": {"price": 100, **dish("Bowl of turtle soup", "Clear soup in a silver bowl.", "Delicate, and gone in four spoonfuls.")},
    "food|steak|supper": {"price": 300, **dish("Steak supper", "A steak done exactly as you asked, with things in a sauce.",
                                               "The steak is done to your liking.")},
    "room|bed": {"price": 100, **token("Room key (High Apothecary)", "A heavy brass key on a tassel. Clean sheets.")},
    "bath|lemon": {"price": 100, **token("Bath token", "A brass token stamped with a lemon. Give it up at the lemon bath.",
                                         bath_token=True)},
}
SELLS_STRIPPERWITCH = {
    "ale|beer": {"price": 1, **cup("Mug of ale", "Good ale, cold, poured right.")},
    "mead": {"price": 2, **cup("Cup of mead", "Dark mead with a red ribbon on the cup.")},
    "wine": {"price": 2, **cup("Glass of wine", "The cheap red, which is not cheap.", "An empty glass with lipstick on it.")},
    "vintage|bottle": {"price": 5000, **cup("Bottle of the good stuff", "Aggressively priced. Very good.", "An empty bottle.", 4)},
    "scraps|nuts": {"price": 1, **dish("Scraps", "Bar nuts and pickled things.", "Salty, sour, gone.")},
    "food|fish": {"price": 5, **dish("Plate of fried fish", "Fried fish and flatbread.", "Not bad at all.")},
    "grub|pork": {"price": 10, **dish("Hot plate", "A proper hot plate: pork, rice and pepper sauce.", "Very good, and you are sweating.")},
    "room|bed": {"price": 10, **token("Room key (Stripperwitch)", "A key on a red velvet ribbon.")},
}

# ---- places ------------------------------------------------------------------------------------------------------

TOWN = {"tier": "town", "description":
        "Klhyts Refuge: the nicest town in Shalamar, everyone says, and they mean the pubs. Colonial timber gone soft in "
        "the heat, a harbour full of fishing boats, six taverns and six different towns happening in them at once. "
        "People come here from Landfall to not be found."}

PLACES = {
    "docks": ("The Docks", {
        "water_source": True,
        "description": "Tarred piers on fat pilings and lamps on poles making yellow coins on black water. Fishing boats "
                       "rafted three deep, a Xoton cog unloading by lantern, the Everuex steamboat all brass and glass, a "
                       "squat brigantine with a green eye painted on her bow. At the far end of the pier, something that is not "
                       "quite a ship glows faintly: the Moonmoth, the elves' vessel. The bonded warehouse squats at the pier's end, "
                       "its door shut, a big man on a bollard in front of it. Out past the harbour mouth a Xoton trader rides at anchor.",
        "finds": {"perception|investigation|search": {"dc": 12, "clue": "scrapes",
                    "line": "Fresh scrapes run across the planks from the pier's edge to the warehouse door: something heavy "
                            "went in and has not come out. The big man on the bollard never looks away from that door for long.",
                    "fail": "Fish guts, rope ends, and a lot of people minding their own business."},
                  "insight": {"dc": 11, "line": "Brask is bored, broke and thirsty, in that order. A man like that has a price."}}}),
    "warehouse": ("The Bonded Warehouse", {
        "water_source": True,
        "description": "A long dark shed that smells of tar, wet hemp and old fish. Bales and crates stacked to the rafters, "
                       "a single lantern hanging from a nail. In the one dry corner, a chair, a bucket of water, and a big crate "
                       "with air holes drilled in the lid.",
        "finds": {"investigation|perception|search": {"dc": 10,
                    "line": "The paper tacked to the big crate reads: PERSONAL EFFECTS. DO NOT OPEN. EMERALD EYE FOR CATAN, ONE O'CLOCK TIDE. "
                            "The wax seal is the Custodian's."}}}),
    "harbour": ("Harbour Street", {
        "description": "The waterfront's spine: chandlers shuttered for the night, a rope-walk, gutters running to the sea. "
                       "The Turtle Dragon's lanterns sway at one end, the High Apothecary's brass glows at the other, and the "
                       "Rampant Ogre's noise spills out of an alley in between. Uphill, the street climbs to Market Square.",
        "finds": {"perception": {"dc": 12, "line": "Two of Dominico's men stroll the street in step, hands near their belts, "
                                 "nodding to the shopkeepers. Peace, kept with a fist."}}}),
    "turtle": ("The Turtle Dragon", {
        "water_source": True,
        "description": "Sailors' pub, the nautical theme taken too far: nets, floats, a stuffed turtle with a dragon's head "
                       "glued on, and two harpoons over the bar. The beers come twice the size. Fishermen, sailors, Xoton "
                       "traders passing through, and at a table by the door, Lizardfolk fishermen drinking with their backs to the wall.",
        "finds": {"perception|insight": {"dc": 12, "line": "The Lizardfolk table gets served last, and the sailors by the window "
                                         "watch it like weather. Nobody has said anything yet. Everyone is waiting for someone to."}}}),
    "apothecary": ("The High Apothecary", {
        "water_source": True,
        "description": "The only establishment of its class in Klhyts Refuge: a grand staircase, fine dark woodwork, white "
                       "linen, a steward who looks through you. The lemon bath is through the back. Dominico's reserved table "
                       "sits by the window. Close to the noble houses, and an easy walk to the port.",
        "finds": {"insight|perception": {"dc": 12, "line": "The steward stiffens every time the officer in uniform looks his way. "
                                         "Whoever the officer is hunting, the staff are on their side, not his."}}}),
    "square": ("Market Square", {
        "water_source": True,
        "description": "Stalls sheeted for the night, a town pump, the Town Hall's white-columned porch, and a notice board "
                       "everybody reads and nobody believes. Lanes run down to Harbour Street, across to the Stripperwitch "
                       "and the Omberhulk & Nun, out to the Treeline Road and the Town Gate.",
        "finds": {"perception": {"dc": 10, "line": "The Town Hall's lamps are lit late. Someone is working in the Custodian's office."}}}),
    "hall": ("The Town Hall", {
        "description": "Colonial timber, white paint going grey, a portrait of a big grey-bearded man in the entrance hall. "
                       "The Custodian's office stands at one side; at the back, the door to the mayor's study, locked.",
        "finds": {"investigation|history": {"dc": 12, "clue": "dues",
                    "line": "The harbour dues book on the clerk's desk shows the dues falling every season for three seasons, "
                            "while the harbour has never been busier. Every page is signed by the Custodian."}}}),
    "study": ("Klhyt's Study", {
        "description": "A small room that smells of pipe smoke and the sea: charts on the walls, a ship in a bottle, a desk "
                       "with a green leather blotter. Somebody has searched it and put everything back very carefully.",
        "finds": {"investigation|search|perception": {"dc": 10,
                    "line": "Whoever searched the desk was in a hurry and then careful. They missed what was under the blotter."}}}),
    "stripperwitch": ("The Stripperwitch", {
        "water_source": True,
        "description": "Red velvet, great music, a stage with a curtain, a long mirror behind the bar. Everyone who matters in "
                       "the underworld passes through here: this is Fat Gog's real seat of power. A red booth in the corner, "
                       "for people who are not here.",
        "finds": {"insight|perception": {"dc": 12, "line": "River keeps glancing at the red booth, then not glancing at it. "
                                         "Something happened in that booth that she has not told anyone."}}}),
    "omberhulk": ("The Omberhulk & Nun", {
        "water_source": True,
        "description": "Mid-tier: loud, buggy, hot. The beds are unclean and the bugs get in, but the company is good and the "
                       "music runs late. Big portions. Mixed races at every table; Fat Gog's people drink here, and so do "
                       "Dominico's informants.",
        "finds": {"perception|insight": {"dc": 12, "line": "Two men by the stairs aren't drinking, they're listening: Dominico's ears, "
                                         "and not subtle about it. Anything said loud in here is at the Apothecary by morning."}}}),
    "ogre": ("Rampant Ogre & Curved Cleaver", {
        "water_source": True,
        "description": "One star. Barely. Sawdust, spit, a bar made of a ship's door, a dice game going in the corner. This is "
                       "Fat Gog's place, or close to it, and the regulars don't want a scene. Dominico's muscle drinks here off duty.",
        "finds": {"insight|perception": {"dc": 11, "line": "Tully, one of Dominico's men, keeps buying rounds he can't afford and "
                                         "laughing too loud about a crate."}}}),
    "treeline": ("The Treeline Road", {
        "description": "Out on the edge of town. Quiet. A dark walk in. Animals watch you from the treeline, their eyes "
                       "catching the moonlight, and the pond off the road breeds unbearable bugs.",
        "finds": {"perception|nature|survival": {"dc": 12, "line": "Eyes in the treeline: a pair low down that blinks, a pair high "
                                                 "up that does not. Whatever they are, they keep to the trees."}}}),
    "unicorn": ("The Touchy Unicorn", {
        "water_source": True,
        "description": "Quiet, for Klhyts Refuge: a genuine library, study rooms, peace. Scholars, fugitives, people who don't "
                       "want to be found. The windows look out on the treeline.",
        "finds": {"history|religion|arcana|investigation": {"dc": 12, "line": "In the library, a Vorkathian court record: the High "
                    "Elves banished in 28 EV, the elven races declared enemies of the state in 62 EV. Someone has pressed a dried "
                    "flower at that page."}}}),
    "market": ("The Night Market", {
        "water_source": True,
        "description": "Too hot to trade by day, so Klhyts Refuge trades by night: a lane of stalls under strings of lanterns "
                       "between the square and the harbour, smoke from braziers, fruit stacked in pyramids, Xoton goods on "
                       "tarpaulins, elven trinkets on folding tables, and a crowd so thick you move through it sideways.",
        "finds": {"perception|insight": {"dc": 12, "line": "Two of Dominico's men work the crowd, collecting a copper here and "
                                         "there from the stallholders. Peace money. The elves pay without looking up."},
                  "sleight|stealth": {"dc": 14, "line": "Every pocket here is guarded, and the Xotons wear their purses on chains. "
                                      "Nothing worth the risk tonight."}}}),
    "moonmoth": ("The Moonmoth", {
        "water_source": True,
        "description": "The elves' ship was grown, not built: one long hull of pale silverwood without a seam, sails folded like a "
                       "moth's grey wings, lanterns that hold a cold light like captured stars. The deck hums faintly underfoot. "
                       "Elves in exile sit among their bundles, waiting.",
        "finds": {"arcana|religion|nature": {"dc": 13, "line": "The hull is alive, slowly: it grows around the cleats and the "
                                             "lantern hooks. Old elven craft, the kind Vorkath's Inquisition burned whole libraries to forget."},
                  "perception": {"dc": 12, "line": "There are empty places among the bundles, kept clear, as if for people still to come."}}}),
    "lanes": ("The Back Lanes", {
        "water_source": True,
        "description": "Narrow lanes of timber houses behind the square, washing strung between the balconies, a rain "
                       "barrel at every door and a goat in every third yard. Most of the town sleeps here, at whatever "
                       "hour it sleeps, and the shutters stay shut through the heat of the day."}),
    # River's secret (owner, 2026-11-23): her ship lies here, and nobody in town knows. Hidden: only those in its
    # `known_to` see the way from the docks (River and Ned Tallow; a player who finds the shore path joins them)
    "cove": ("The Cove Behind the Reef", {
        "hidden": True, "water_source": True,
        "description": "A narrow cove down the coast, behind the reef the charts mark DO NOT: black shingle, a cave mouth "
                       "hung with drying nets, and lanterns kept hooded. In water too still for this coast rides a long, low, "
                       "black-hulled schooner, her name in silver on the stern: QUICKSILVER.",
        "finds": {"investigation|perception|search": {"dc": 12,
                    "line": "In the cave mouth, crates stencilled with the marks of half a dozen merchant houses, none of them "
                            "the same and none of them paid for. Over one hammock hangs a green glass bottle full of bent "
                            "pins and seawater, corked with red wax.",
                    "fail": "Nets, shingle, and a feeling of being watched from the schooner's rail."}}}),
    "gate": ("The Town Gate", {
        "description": "Two tarred timber gates in the town wall, standing open for the night trade, a lantern on each post. "
                       "Beyond, the jungle road goes into the dark, and the dark goes on a long way.",
        "finds": {"survival|nature|perception": {"dc": 11, "line": "The road out is well used: cart ruts, hooves, the splayed prints of "
                                                 "Lizardfolk feet coming in to market. Nothing has come down it in a hurry tonight."}}}),
    # the shops (owner, 2026-11-23: "we need some shops. Adventurer stuffs food, weapons. Armour"; canon names none:
    # host defaults). Chandlers' Row runs between Harbour Street and the Night Market; each keeper lives above the shop
    "row": ("Chandlers' Row", {
        "description": "A short, steep lane between Harbour Street and the Night Market, cobbled with ballast stones. Three "
                       "shopfronts stand with their shutters propped open late for the night trade: a chandler's window "
                       "hung with rope and lanterns, a smith's door with a crooked anvil painted on the lintel, and a "
                       "Xoton armourer's sign of coral and chain. Lamps burn in all three."}),
    "chandlery": ("Merrow's Chandlery", {
        "description": "A narrow shop that goes back much further than it looks, every inch of it hung or shelved: coils "
                       "of rope, lanterns, bedrolls, oilskins, barrels of hardtack and salt fish, a glass case of small "
                       "bottles with red wax on their necks, and maps pinned flat under a sheet of glass on the counter.",
        "finds": {"perception|investigation": {"dc": 13,
                  "line": "Behind the counter, half hidden by a rack of lanterns, a regimental drum hangs on a nail with "
                          "its painted crest scraped off. Somebody scraped it carefully, a long time ago.",
                  "fail": "Rope, lamps, biscuit and the smell of tar. A chandler's shop."}}}),
    "anvil": ("The Crooked Anvil", {
        "description": "A forge-shop open to the lane, hot as a kitchen: a crooked anvil, a quenching trough, and on the "
                       "back wall a rack of blades laid out like a choir, rapiers at the front, their guards curling like "
                       "fern fronds. Bows and crossbows hang above them; a barrel of spears stands by the door.",
        "finds": {"perception|investigation|history": {"dc": 12,
                  "line": "Elven script is worked small into the rapier guards, a word on each: names, you think, and none "
                          "of them the smith's. A ledger by the anvil has one long-unpaid line, for a sword-cane, black, "
                          "silver head.",
                  "fail": "Good steel, well kept. Somebody here knows what they are doing."}}}),
    "coral": ("Coral and Chain", {
        "description": "A low Xoton shop that smells of oil and the sea: coral plates drying on racks like shells on a "
                       "beach, a hauberk on a wooden man by the door, leather jerkins hung in a row, shields stacked like "
                       "plates, and a workbench of rivets and awls under a glow-kelp lamp.",
        "finds": {"perception|investigation": {"dc": 12,
                  "line": "A slate on the wall reads, in chalk: THE FIST OWES 30 JERKINS. Under it, a newer line: AND "
                          "INTEREST.",
                  "fail": "Armour, oil and the sound of a mallet. A working shop."}}}),
    # the owner, 2026-11-23: "Surrender should mean surrender. And you are taken to prison." Under the Town Hall,
    # behind a barred door only the watch opens (scripts/_custody.py)
    "cells": ("The Cells", {
        "water_source": True,
        "description": "Two cells cut into the rock under the Town Hall, straw on the floor, a bucket of water, and a "
                       "slit of a window at the height of passing boots. Names and tallies are scratched into the "
                       "walls in four alphabets. The door is oak and iron, barred on the Hall side."}),
    # the owner, 2026-11-23: "we will need an undertaker to go and sort out bodies etc." (scripts/undertaker_rule.py)
    "graves": ("The Quiet Ground", {
        "burial_ground": True, "water_source": True,
        "description": "A burial ground off the Treeline Road, red earth and frangipani, rows of pine boards with names "
                       "lettered on them, a low end by the mangroves where the Lizardfolk lie with their feet to the "
                       "water, and a lodge with a mule cart under the eaves. The jungle leans over the place where a "
                       "wall ought to be."}),
    # the owner, 2026-11-23: "the river that runs through the town... the Verde river. Legends have it is the body of
    # Kteol submerged. It goes out to the jungle ... out side the city walls, farms, lizard tribes and about 30 miles down
    # a wiggly river is Malice." The town's stretch of it, and the water gate where it meets the jungle; what is beyond
    # is known in talk (cast/n_beyond.py), not walked yet
    "verde": ("The Verde", {
        "water_source": True,
        "description": "The Verde runs through the middle of the Refuge, green and slow and warm as bathwater, between "
                       "banks of mangrove root and old stone quays. Three bridges cross it: a rope footbridge hung with "
                       "washing in the Back Lanes, the humpbacked Stone Bridge by the Night Market, and a tarred swing "
                       "bridge where it meets the harbour. Under the Stone Bridge flat river boats from the farms unload "
                       "plantains, cane and cages of shrieking birds, and Lizardfolk fishermen stand thigh-deep with "
                       "spears, never under the arch. The water is very still. In the right light its bends look less "
                       "like a river than like something lying down. Downstream it slides out into the harbour.",
        "finds": {"religion|history|nature|arcana": {"dc": 13,
                  "line": "Under the bridge, where the old stones go down into the water, a serpent has been cut into "
                          "every one of them, older than the town, worn almost smooth. The Lizardfolk leave a fish on "
                          "the lowest stone at dusk and do not look at the water while they do it. Their name for the "
                          "river is not Verde. It is the name of a god, and they say he is not dead, only lying down.",
                  "fail": "Green water, mangrove roots and a bridge. Something about the stillness bothers you, and "
                          "you cannot say what."}}}),
    "rivergate": ("The River Gate", {
        "water_source": True,
        "description": "Where the Verde comes in under the town wall: a water gate of tarred timber and iron, its "
                       "portcullis hung a man's height above the river so the boats can pass beneath, and a farm path "
                       "running along the bank. Beyond the wall lie cleared fields of cane and plantain, farmhouses on "
                       "stilts, the smoke of Lizardfolk fishing camps, and then the jungle, closing over the river like a "
                       "lid: past the last farm there is no path at all, only water. A painted board by the gate reads "
                       "MALICE, THIRTY MILES, BY WATER ONLY, and someone has added underneath, in another hand, AS THE "
                       "RIVER WINDS. The farm boats come in under the portcullis at dawn and go back out at noon, and "
                       "they take nobody with them."}),
    # the owner, 2026-11-23: "I guess with a river we need some bridges." Canon names none: three crossings, one for each
    # part of town, all host defaults
    "stonebridge": ("The Stone Bridge", {
        "description": "A humpbacked bridge of green-grey stone over the Verde between the Night Market and the Back "
                       "Lanes, so steep in the middle that the carts take a run at it. The parapets are worn into hollows "
                       "where a thousand elbows have leaned, lanterns hang on iron hooks, and there is a fruit barrow at "
                       "each end. Stone steps go down on the market side to the bridge quay, where the farm boats tie up "
                       "and the harbourmaster's copper is collected. Nobody throws anything off it, not a mango skin, not "
                       "a fishbone, and below it the Lizardfolk fishermen keep well out from under the arch.",
        "finds": {"history|religion|investigation|arcana": {"dc": 12,
                  "line": "The paving and the parapets are the town's, mortared and patched. The arch underneath is "
                          "not: older stones, fitted without mortar, greener than anything the town's masons ever cut, "
                          "and the hump stands exactly over the deepest bend of the river. The town did not build this "
                          "bridge. It paved one that was already there.",
                  "fail": "A good old bridge, steep as a roof. Your calves feel it."}}}),
    "washline": ("The Washline Bridge", {
        "description": "A footbridge of planks on rope slung across the Verde from the Back Lanes, sagging in the middle "
                       "so that the green water is never far below your boots. Washing lines run from its rails to every "
                       "balcony on both banks, and shirts, sheets and petticoats hang over the river like the flags of a "
                       "hundred small countries. It sways when anyone heavier than a goat crosses. On the far side a "
                       "duckboard path runs along the bank to the Reed House on its stilts.",
        "finds": {"perception|investigation": {"dc": 13,
                  "line": "Pegged out among the sheets is a fine white shirt, Landfall linen, far too good for the Back "
                          "Lanes. Someone has scrubbed hard at the collar and not quite got the red out.",
                  "fail": "Sheets, shirts, a goat on a balcony eating a sock. The Back Lanes, drying."}}}),
    "swingbridge": ("The Swing Bridge", {
        "description": "Where the Verde slides out into the harbour, Harbour Street crosses it on a timber bridge black "
                       "with tar that turns on a great iron pin, worked by a capstan in a keeper's hut no bigger than a "
                       "privy. At high water it swings open for the masts and the carts wait and curse. Below, the green "
                       "river water and the grey sea water meet in a line you could draw with a stick, and the gulls sit "
                       "on the rail on the sea side only."}),
    # the owner, 2026-11-23: "do we need a healer shop ? A doctor ? And a healer different shops different vibes." A
    # Landfall surgeon off the harbour who mends anyone, fast and dear, and writes it all down; and a Lizardfolk
    # grandmother's reed house over the Verde, slow and cheap, where nobody is taken (scripts/healing_rule.py)
    "surgery": ("Prewitt's Surgery", {
        "description": "A narrow whitewashed room off Harbour Street that smells of lye and spirits: a scrubbed table "
                       "with leather straps, a glass case of saws and probes laid out by size, a basin, a rack of brown "
                       "bottles labelled in a tidy Landfall hand, and a framed diploma from a college of surgeons in "
                       "Landfall, the glass cracked across. A brass plate on the door gives his hours. A slate under it "
                       "gives his prices, and they are not low.",
        "finds": {"investigation|perception": {"dc": 14,
                  "line": "On the shelf above the basin, among the case books, is a thinner ledger with a ribbon in it. "
                          "The last page is names, dates and wounds, and beside some of the names a small, neat tick and "
                          "the letter V.",
                  "fail": "Clean, cold and orderly: the cleanest room in the Refuge, and the least friendly."}}}),
    "reedhouse": ("The Reed House", {
        "water_source": True,
        "description": "A long low house of woven reed on stilts over the Verde, reached by a plank from the bank. "
                       "Inside it is dim and green and smells of river mud and crushed leaves: sleeping mats in rows, "
                       "bundles of herbs drying on the roof poles, clay pots of poultice, a fire pit with a kettle that "
                       "is never empty, and between the floor reeds the slow green river going by underneath. Nobody "
                       "here asks who you are, or who hurt you.",
        "finds": {"nature|medicine|religion": {"dc": 12,
                  "line": "The herbs are good ones and the poultices honestly made. On the post by the door hangs a "
                          "string of serpent bones, very old, that nobody who came here meaning harm has been able to "
                          "look at for long. Nobody is taken from the Reed House: not by the Fist, not by the watch. "
                          "Nobody has had to say so twice.",
                  "fail": "Reed, mud, smoke and herbs. Peaceful, and a little unsettling, like being watched by "
                          "something patient."}}}),
}

WAYS = [("square", "market"), ("harbour", "market"), ("docks", "moonmoth"), ("docks", "warehouse"), ("docks", "harbour"), ("harbour", "turtle"), ("harbour", "apothecary"), ("harbour", "ogre"),
        ("harbour", "square"), ("square", "hall"), ("hall", "study"), ("square", "stripperwitch"), ("square", "omberhulk"),
        ("square", "treeline"), ("treeline", "unicorn"), ("square", "gate"), ("square", "lanes"), ("market", "lanes"),
        ("docks", "cove"), ("harbour", "row"), ("row", "market"), ("row", "chandlery"), ("row", "anvil"),
        ("row", "coral"), ("treeline", "graves"), ("market", "verde"), ("lanes", "verde"), ("harbour", "verde"),
        ("verde", "rivergate"), ("harbour", "surgery"), ("verde", "reedhouse"), ("market", "stonebridge"),
        ("stonebridge", "lanes"), ("stonebridge", "verde"), ("lanes", "washline"), ("washline", "reedhouse"),
        ("harbour", "swingbridge"), ("swingbridge", "verde")]

# ---- people ------------------------------------------------------------------------------------------------------
# Each: (type, where, state, carries). Lines in a table: words in double quotes are said, the rest is seen.
# Canon is in notes/bible.md; looks, voices and stats not in LoreKeeper are host defaults.

FAT_GOG = {
    **body({"str": 18, "dex": 8, "con": 16, "int": 13, "wis": 14, "cha": 16},
           {"insight": 4, "intimidation": 4, "persuasion": 3, "brawl": 3, "resolve": 3}, hp(60)),
    "faction": "the Guild",
    "description": "An enormous, old Lizardfolk in a white linen suit gone grey at the cuffs, scales the green of deep "
                   "water, a sticking plaster on the back of his neck that nobody asks about. He sits like a hill sits. "
                   "Honest folk nod to him in the street; the shadows do as he says.",
    "brief": "You are Fat Gog: you own the shadows of Klhyts Refuge, the Marcelles Wallis of colonial fantasy, and you are "
             "also one of the most trusted people in the town. Slow, polite, very dangerous. Years ago you found Klhyt on "
             "the beach, a castaway starving and dying of thirst, and carried him up the sand; the town grew around him, and "
             "he is your friend. You built the underworld on one idea, Lizard men and humans living in harmony, and you are "
             "proud of it. River is your partner and you trust her with your life. Klhyt has been gone four nights; "
             "the Custodian says business upriver and you do not believe it. Dominico has given you until midnight to hand "
             "over your books and you will not. You want to know who put the iron in Dominico's spine. You do not know "
             "what River saw in the red booth. Reward the useful; you remember debts both ways. You talk like a man who has "
             "never had to raise his voice.",
    "dialog": {
        "klhyt|mayor|founder": "Gog's eyes half close. \"I found that man on the beach, starving, his tongue black from thirst, "
                               "and carried him up the sand. Now he has been gone four nights, and the Custodian says business "
                               "upriver. Klhyt never had business upriver in his life.\"",
        "beach|rescue|castaway|found": "\"He came ashore with nothing but the salt in his beard and no water in him at all. I "
                                       "gave him a drink. He gave this coast a town. I think I got the better of it.\"",
        "dominico|midnight|books|threat": "\"Dominico keeps the peace with a fist. Lately he wants to keep my books with it too. "
                                          "Midnight, he says. Somebody is paying for that kind of nerve.\"",
        "custodian": "\"The Custodian skims the top. Everybody knows. Nobody minds, so long as the top is all he takes.\"",
        "guild|work|job|help|hire": "\"You want work? Be useful. Find out who put the iron in Dominico's spine, or where my mayor "
                                    "went. Bring me something I can hold, not something you heard.\"",
        "river": "\"River keeps this place running. Be nice to River.\"",
        "lizardfolk|harmony|meters|lizard": "\"Lizard men and humans, drinking in the same rooms. That is what I built here. "
                                             "That is what some people would like gone.\"",
        "stripperwitch|place|seat": "\"My house. Mind the velvet.\"",
    },
    "default_line": "Gog folds his hands on his belly. \"Ask me something that matters, friend: Klhyt, Dominico, the "
                    "Custodian, work.\"",
}

RIVER = {
    **body({"str": 12, "dex": 14, "con": 12, "int": 12, "wis": 15, "cha": 15},
           {"insight": 3, "persuasion": 3, "perception": 3, "blade": 1}, hp(27)),
    "faction": "the Guild", "sells": SELLS_STRIPPERWITCH,
    "description": "River runs the bar: a tall woman with forearms like a sailor's, rings on every finger, a voice like "
                   "gravel and honey. She sees the whole room in the mirror behind the bar.",
    "brief": "You are River, head barkeep of the Stripperwitch and Fat Gog's partner; you keep the place running, and "
             "you are fond of Lizardfolk in general and Gog in particular. Four nights ago you saw Klhyt and the Custodian "
             "shouting about money in the red booth, and Klhyt walk out between two of Dominico's men, not willingly. You "
             "have not told Gog, because Gog would start a war tonight and you do not think he would win it. You tell a "
             "stranger only if they ask straight and seem able to do something about it. You are warm, quick, and nobody's fool.",
    "dialog": {
        "klhyt|mayor|founder|booth|custodian": "River glances at the red booth, then back at you, and keeps her voice down. "
            "\"Four nights back. Klhyt and the Custodian, in that booth, shouting about money. Klhyt walked out between two of "
            "Dominico's lads, and he didn't walk like a man who wanted to.\" She polishes a glass that is already clean. "
            "\"I haven't told Gog. If I tell Gog, there's a war tonight, and I like my mirror.\"",
        "gog|fat": "\"Gog? He's a sweetheart. Don't tell anyone.\"",
        "dominico": "\"Dominico's got a table at the Apothecary and a fist in every pie. Lately he's been reaching for ours.\"",
        "drink|menu|price|food|room": "\"Ale's a copper, mead two, the good wine you can't afford. Buy, or let someone else stand there.\"",
        "siren|show|stage|music": "\"We had a siren from the Heartless Sea sing here once, paying her way through wizard school. "
                                  "Nobody's matched her since.\"",
    },
    "default_line": "River leans on the bar. \"Drink, gossip or trouble? I do all three, in that order.\"",
}

DOMINICO = {
    **body({"str": 15, "dex": 14, "con": 14, "int": 14, "wis": 12, "cha": 15},
           {"intimidation": 4, "arcana": 2, "insight": 3, "blade": 3, "resolve": 3}, hp(52)),
    "faction": "the Fist",
    "description": "A lean, handsome human in a black coat, close-cropped beard, a heavy silver ring he keeps turning. "
                   "Dominico, the Custodian's enforcer, who keeps the peace in Klhyts Refuge with a fist. His knuckles have "
                   "scars on the scars.",
    "brief": "You are Dominico, the Custodian's enforcer, captain of the hired men who keep the peace in Klhyts Refuge. "
             "You are no guild master, not yet: the guild is Fat Gog's, and you want it. You keep the peace with a fist "
             "because it is quicker than a speech. You dabble in the magic arts, parlour conjuring mostly; "
             "lately something in the dark has started whispering back when you work, and you have not answered it. Not yet. "
             "The Custodian pays you, and has promised you Fat Gog's shadows if you take them: you have given Gog until midnight "
             "to hand over his books. Four nights ago the Custodian had your men take a 'troublemaker' to the bonded warehouse "
             "and crate him for Catan; you were told it was a debtor. You do not know it is Klhyt. If someone shows you proof, "
             "you will be furious at being used, and you will pull your men off. You despise weakness and you think Gog's harmony "
             "is weakness. You keep your word, which makes you dangerous.",
    "dialog": {
        "gog|books|guild|stripperwitch|midnight": "\"Fat Gog has had this town's shadows to himself too long. I'm only asking "
                                                  "him to share his books. By midnight.\"",
        "klhyt|mayor|founder": "\"The mayor is upriver on business. The Custodian says so.\" He holds your eye a moment too long.",
        "custodian": "\"The Custodian keeps the town. I keep the peace. You keep your nose out of both.\"",
        "magic|arcana|whispers|dark|ring|conjuring": "Dominico turns his ring. \"A little conjuring, for the parlour. Nothing "
                                                     "that answers back.\" He does not sound sure.",
        "peace|fist|law|watch": "\"Somebody has to keep the peace in a town of runaways. I do it with a fist because it's "
                                "quicker than a speech.\"",
        "lizardfolk|lizard|harmony": "\"They drink in our taverns and fish our water. Gog calls it harmony. I call it waiting.\"",
        "master|seat|ambition|want": "\"The guild is Gog's. For now. Nothing in this town stays where it's put.\"",
        "crate|warehouse|brask|debtor": "\"A debtor, shipped somewhere he can work it off. The Custodian's business. Mine is "
                                        "making sure nobody opens the lid.\"",
    },
    "default_line": "Dominico doesn't look up from his glass. \"Say what you came to say.\"",
}

CUSTODIAN = {
    **body({"str": 9, "dex": 11, "con": 10, "int": 16, "wis": 13, "cha": 14},
           {"deception": 4, "insight": 3, "persuasion": 3, "history": 2}, hp(18)),
    "faction": "the Refuge",
    "description": "The Custodian: a thin, neat human of about fifty in a good grey coat, ink on his fingers, a ring of keys "
                   "on his belt. He smiles with half his mouth.",
    "brief": "You are the Custodian of Klhyts Refuge, running the town while the mayor is away. You have skimmed the "
             "harbour dues for three seasons. Four nights ago Klhyt found out and confronted you at the Stripperwitch; you had "
             "Dominico's men take him, and he goes out in a crate on the Emerald Eye for Catan, on the one o'clock tide tonight. Dominico thinks the "
             "crate holds a debtor. You hold the only key to Klhyt's study. You lie smoothly and well, you bribe before you "
             "threaten, and you never admit anything in front of witnesses. You pretend you never visit the Stripperwitch. "
             "You do. Your goal: get through tonight, get the crate on the tide, and have Fat Gog's books in Dominico's hands.",
    "dialog": {
        "klhyt|mayor|founder|missing": "\"The mayor is upriver on town business. Delicate negotiations. I keep the Refuge running "
                                       "in his absence, as he would wish.\"",
        "dues|harbour|tally|money|accounts": "\"The harbour dues are in perfect order. I sign every tally myself.\"",
        "dominico": "\"Dominico keeps the peace. I find it best not to ask how.\"",
        "gog|guild|stripperwitch": "\"Fat Gog is a businessman. I have never set foot in his establishment.\"",
        "study|office|key": "\"The mayor's study stays locked until the mayor returns. I hold the only key, for safekeeping.\"",
        "town|refuge|custodian|job": "\"Klhyts Refuge runs on trust, and on someone minding the accounts. I mind the accounts.\"",
    },
    "default_line": "The Custodian smiles with half his mouth. \"Is there town business? I have a great deal of it.\"",
}

KLHYT = {
    **body({"str": 16, "dex": 10, "con": 15, "int": 13, "wis": 14, "cha": 15},
           {"athletics": 2, "survival": 3, "persuasion": 3, "blade": 2}, hp(45)),
    "hp": 6, "bound": True, "faction": "the Refuge",
    "description": "A big grey-bearded man gone thin, tied to a chair with tarred rope: Klhyt, founder of Klhyts Refuge. "
                   "Sun-dark, salt-white scars on his forearms, eyes that have not slept.",
    "description_free": "Klhyt, founder of Klhyts Refuge: a big grey-bearded man gone thin, rope burns on his wrists, standing "
                        "straight again.",
    "brief": "You are Klhyt, a castaway who washed up on this coast with nothing and founded the first western Shalamar town, "
             "a place where nobody asks where you came from. Four nights ago you confronted the Custodian over three seasons "
             "of skimmed harbour dues, and Dominico's men took you. You are tied up in the bonded warehouse, and you know you "
             "go to Catan in a crate on the one o'clock tide. Brask, outside, has the key. You are proud, warm, stubborn, "
             "and you speak like a sailor. Fat Gog found you on the beach when you washed up, starving and dying of thirst, "
             "and saved your life: you owe him everything, and you trust him above anyone. Once free you want the whole town to "
             "hear what the Custodian did.",
    "dialog": {
        "help|free|rope|untie|cut": "\"Cut these ropes and I'll owe you more than this town can pay.\"",
        "custodian|who|why|dues": "\"I found where the harbour dues go. Then I made the mistake of telling the Custodian I'd found "
                                  "it, before I told anyone else.\"",
        "dominico|brask|guard|key": "\"Dominico's men. Brask has the key; he never lets it out of his fist. Dominico thinks I'm a "
                                    "debtor, I'd wager. He's a brute, not a kidnapper.\"",
        "tide|catan|crate|ship": "\"They mean to nail me in that crate and ship me to Catan on the one o'clock tide. Personal effects.\"",
        "refuge|town|castaway|founded": "\"I washed up on this beach with nothing but the salt in my beard, and I'd have died "
                                        "there if Fat Gog hadn't found me. I built a place where nobody asks where you came "
                                        "from. Somebody has to keep it that way.\"",
        "gog": "\"Gog found me on the sand, starving, dry as a bone, and carried me up the beach. Tell Gog. He'll know what to "
               "do, and he'll enjoy doing it.\"",
    },
    "default_line": "Klhyt tests the ropes again. \"Ask me later. Ropes first.\"",
}

BRASK = {
    "body": 3, "wits": 1, "will": 2, "skills": {"blade": 2, "brawl": 2, "resolve": 1}, "hp": 9, "max_hp": 9,
    "faction": "the Fist", "bribe": 200, "purse_before": 12, "leaves_behind": "Warehouse key",
    "bribe_line": "The big man weighs the coin, looks at the warehouse door, and decides the Rampant Ogre is where he was all along.",
    "marker_line": "The big man looks at the bone marker for a long time. \"I never saw you,\" he says, and walks off up the pier.",
    "cowed_line": "The big man backs off a step, then another. Then he is going up the pier at a run, the key still on "
                  "his belt, bawling for Tully.",
    "description": "A slab of a man on a bollard by the warehouse door, cudgel across his knees, one of Dominico's.",
    "dialog": {
        "warehouse|crate|inside|door": "\"Fish. Rope. Nothing. Move along.\"",
        "dominico|boss|job": "\"Mister Dominico pays me to sit here.\" He rubs his thumb across his fingers without noticing. "
                             "\"Not enough, mind.\"",
        "drink|ale|ogre|thirsty": "\"I'd kill for a drink. Not literally. Probably.\"",
        "key|lock": "He pats his belt. \"Stays with me.\"",
        "money|coin|bribe|price": "\"Two gold, a man could have a very long drink with two gold.\" He says it to the water, not to you.",
    },
    "default_line": "\"Move along.\"",
}

TULLY = {
    "body": 3, "wits": 1, "will": 1, "skills": {"brawl": 2}, "hp": 8, "max_hp": 8, "faction": "the Fist",
    "description": "A red-faced young bruiser in Dominico's colours, off duty and drunk on it, buying rounds he can't afford.",
    "dialog": {
        "brask|warehouse|crate|job|work": "\"Brask got the short straw tonight. Minding a crate in the bonded warehouse till the one "
                                          "o'clock tide. Heavy crate. Grumbles a lot, for a crate.\" Tully laughs, then stops "
                                          "laughing. \"Forget I said that.\"",
        "dominico|boss": "\"Best boss I ever had. Pays on time. Scares me witless.\"",
        "custodian": "\"Never met him. Brask says he's the one paying for the crate.\"",
        "drink|round|ale": "\"Another round! On me! On... somebody.\"",
    },
    "default_line": "Tully grins at you. \"You're new. Drink with me.\"",
}

TEAGUE = {
    "body": 1, "wits": 3, "will": 2, "skills": {"lore": 1}, "faction": "the Refuge",
    "description": "Harbourmaster Odo Teague: a stooped man in a salt-white coat with a tally board under one arm and a "
                   "pencil behind each ear.",
    "dialog": {
        "crate|warehouse|bonded": "Teague lowers his voice. \"Four nights back the Custodian's men brought a crate into the bonded "
                                  "warehouse and told me not to log it. I logged it. I just didn't put it anywhere he'll look.\"",
        "klhyt|mayor|founder": "\"Upriver, they say. Klhyt doesn't go upriver. He hates rivers. He likes the sea.\"",
        "ship|passage|catan|emerald|boat": "\"The Emerald Eye goes out for Catan on the one o'clock tide. The Turtle Dragon books the berths.\"",
        "xoton|frigate|trader|masts": "\"Xoton trader out past the mouth, passing through like they all do. They pay their dues "
                                      "in full, which is more than I can say for some.\"",
        "dues|harbour|tally|money": "\"I collect the dues, count them, and hand them up to the Town Hall. What happens to them after "
                                    "that is above my station.\" He doesn't sound happy about it.",
        "gog|fat": "\"Fat Gog? He pulled Klhyt off the beach, back when this was nothing but sand. Half the town owes him "
                   "something, and the other half owes him money.\"",
        "work|job|new|town": "\"New? Then listen. If you want work, Fat Gog's always hiring, at the Stripperwitch up past the square. "
                             "If you want trouble, Dominico keeps a table at the High Apothecary. And if you want to be left alone, "
                             "the Touchy Unicorn, out by the trees.\"",
    },
    "default_line": "Teague looks you over and taps his tally board. \"New? Then here's free advice. Work: Fat Gog, at the "
                    "Stripperwitch past the square. Trouble: Dominico, at the High Apothecary. Peace and quiet: the Touchy "
                    "Unicorn, out by the trees. Otherwise: dues, ships, the tide or the town, one at a time.\"",
}

EIRIK = {
    **body({"str": 14, "dex": 11, "con": 15, "int": 12, "wis": 13, "cha": 15},
           {"persuasion": 3, "athletics": 2, "nature": 2, "blade": 2}, hp(30)),
    "faction": None,
    "description": "Captain Eirik, a Xoton: barrel-bodied, black-skinned, beard braided with copper wire and a kelp lamp "
                   "glowing green at his belt. He laughs with his whole chest.",
    "brief": "You are Captain Eirik, a Xoton envoy and trader, known for your diplomatic skills, ashore from the Xoton "
             "trader out past the harbour mouth, passing through. Xotons say their name with an X; outsiders with a Z, and you correct them "
             "cheerfully. You are here to buy timber. You met Klhyt a month ago and liked him. You saw lights at the bonded "
             "warehouse at odd hours this week. You are generous, curious, and you never take sides on land.",
    "dialog": {
        "xoton|zoton": "\"Xoton. With the X, friend. The soft sound is for people who've never been at sea.\"",
        "timber|forest|trade|wood": "\"We buy timber. Straight and tall. Your jungle has more of it than it knows what to do with.\"",
        "crows|nest|home": "\"The Crows Nest floats where we like it. That is the beauty of it.\"",
        "klhyt|mayor": "\"Your mayor was out to my ship a month back. Sharp man. Drinks like a Xoton. Haven't seen him since.\"",
        "warehouse|lights|crate": "\"Lights in that bonded warehouse at all hours this week. Nobody keeps fish that carefully.\"",
        "ship|frigate|masts|lamp": "\"Every mast of her earned. The lamp? Glow kelp. Never needs oil.\"",
    },
    "default_line": "Eirik raises his huge mug. \"Ships, timber, the sea. I'll talk about any of it.\"",
}

SSARK = {
    "body": 3, "wits": 2, "will": 2, "skills": {"survival": 2, "blade": 1}, "faction": None,
    "description": "Ssark, a green Lizardfolk fisherman of the Meters, salt crusted on his scales, drinking slowly with his "
                   "back to the wall and a gutting knife on the table.",
    "dialog": {
        "meters|tribe|lizardfolk": "\"Meters. Green. We are the ones who talk to outsiders. Somebody has to.\"",
        "tension|trouble|sailors|served": "\"We drank here without trouble for years. This season they serve us last and watch us "
                                          "drink.\" His tail twitches. \"I notice.\"",
        "war|calling|mandrills|north": "\"Up north the Mandrills talk of a calling. A war to clear the coast. The Meters do not listen.\" "
                                       "A long pause. \"Yet.\"",
        "gog|harmony": "\"Fat Gog says harmony. While Gog says it, we fish.\"",
        "fish|fishing|catch": "\"Snapper, grouper, the long silver ones. The sea does not care who catches it.\"",
    },
    "default_line": "Ssark watches you with one eye. \"Fish, my people, or the trouble. Which?\"",
}

THORADIN = {
    **body({"str": 14, "dex": 15, "con": 15, "int": 10, "wis": 14, "cha": 8},
           {"survival": 3, "nature": 3, "perception": 3, "aim": 3}, hp(40)),
    "faction": None,
    "description": "Thoradin, a dwarven ranger from Landfall, rangy for a dwarf, quiet, with a longbow unstrung beside him "
                   "and leaves still caught in his beard. Not at all like any dwarf you've heard songs about.",
    "dialog": {
        "druid|search|looking": "\"I'm looking for a druid. One in particular. The jungle hides them well.\"",
        "landfall|home|vorkathia": "\"Landfall is all walls and prayers. Here, the trees are older than the gods.\"",
        "jungle|road|gate|trees": "\"Past the gate the road goes a long way and then stops being a road. Don't go at night.\"",
        "eyes|treeline|animals": "\"Jaguars, mostly, at the treeline. And something taller that I haven't named yet.\"",
    },
    "default_line": "Thoradin nods once. \"Druids, the jungle, or Landfall. I don't do small talk.\"",
}

MAGGS = {
    "body": 2, "wits": 2, "will": 3, "skills": {"brawl": 2}, "faction": "the Refuge", "sells": SELLS_TURTLE,
    "description": "Bosun Maggs, who runs the Turtle Dragon: one-eyed, tattooed to the knuckles, an apron made of sailcloth.",
    "dialog": {
        "drink|menu|price|beer|ale": "\"Beer's a copper and twice the size. Mead's a copper. Wine's a copper.\" She leans in. \"Avoid the wine.\"",
        "passage|catan|ship|berth|emerald": "\"The Emerald Eye sails for Catan on the one o'clock tide. Two gold a berth. Sign in the passage book on the bar.\"",
        "oysters|food": "\"Oysters, three copper the plate. Caught this morning, or this week.\"",
        "lizardfolk|tension|trouble": "\"Ssark and his lot drink here like anybody else. Anyone who says different can drink in the harbour.\"",
        "harpoons|harpoon": "\"Those harpoons are nailed up there so nobody uses them. Keep it that way.\"",
    },
    "default_line": "Maggs slaps the bar. \"Drink, oysters, or a berth. Choose.\"",
}

AGATHE = {
    "body": 2, "wits": 3, "will": 4, "skills": {"brawl": 3, "resolve": 2}, "faction": "the Refuge", "sells": SELLS_OMBERHULK,
    "description": "Sister Agathe, landlady of the Omberhulk & Nun: a nun, or she was, with a wimple, an apron, and a "
                   "bung-starter she is not afraid to use.",
    "dialog": {
        "drink|menu|price|ale|room": "\"Ale a copper, mead two, a bed a copper and the bugs come free.\"",
        "spuds|food|beatrice|susan|phillip": "\"Beatrice, Susan and Phillip's spuds. Don't ask which is which. Three copper.\"",
        "nun|sister|name": "\"I left the order. The order hasn't noticed.\"",
        "gog|fat|guild": "\"Gog's people drink here, and they pay. Gog looks after this town, whatever else he does.\"",
        "informants|listening|stairs|dominico": "She jerks her head at the stairs. \"Them two? Dominico's ears. They pay for their drinks, so.\"",
        "bard|music|moonport": "\"The Bard of Moonport, when he's in town. His voice cuts through this lot like a knife through butter.\"",
    },
    "default_line": "Agathe crosses her arms. \"Eat, drink or get out of the doorway.\"",
}

BARD = {
    "body": 1, "wits": 3, "will": 2, "skills": {"parley": 2}, "faction": None,
    "description": "The Bard of Moonport: a narrow man in a peacock coat with a lute older than he is, tuning between songs.",
    "dialog": {
        "song|music|play|sing": "He plucks a chord. \"Requests cost a copper. Insults cost two. Klhyt's Ballad is free, because "
                                "nobody's asked for it since he went upriver.\"",
        "klhyt|ballad|mayor": "\"Klhyt's Ballad. 'He came ashore with the salt in his beard.' Nobody wants it this week. Odd, that.\"",
        "moonport|home": "\"Moonport is a long way from here. That's the best thing about it.\"",
        "gossip|news|rumour": "\"The Custodian's been seen at the Stripperwitch. Again. He's never been there. Ever.\" A wink.",
    },
    "default_line": "The Bard tunes a string. \"Songs, gossip or Moonport?\"",
}

LUDO = {
    "body": 4, "wits": 1, "will": 2, "skills": {"brawl": 3}, "faction": "the Guild", "sells": SELLS_OGRE,
    "description": "Big Ludo, a Jonulvicha behind the bar of the Rampant Ogre: bald, one tusk broken, built like a door. One of the crownies.",
    "dialog": {
        "drink|menu|price|rum|ale": "\"Everything's a copper. Everything.\"",
        "crownies|crownie": "\"Crownies are regulars. Regulars don't want a scene. You want a scene?\"",
        "gog|guild": "\"This is Gog's place. Near enough. You behave.\"",
        "husok|twins": "\"Husok? Owes a woman an explanation and two children a father. Owes me four coppers.\"",
        "suite|honeymoon|room": "\"Honeymoon Suite's four coppers. Three dog pelts and a bed. Chickens extra.\"",
        "dice|game": "\"Dice are on the table. House doesn't take a cut. House doesn't need to.\"",
    },
    "default_line": "Ludo grunts. \"Drink.\"",
}

HUSOK = {
    "body": 2, "wits": 1, "will": 1, "skills": {}, "faction": None,
    "description": "Husok Sourfist: a sour-faced man with a mouth like a drawstring purse, hunched over a rum he isn't enjoying.",
    "dialog": {
        "twins|woman|love|children": "\"I told her I loved her. I did! At the time.\" He drinks. \"Twins, she says. Twins.\"",
        "name|sourfist": "\"It's a family name. The fist came first. The sour came later.\"",
        "help|fix": "\"Help? Tell her I died. Tell her I went upriver, like the mayor.\"",
    },
    "default_line": "Husok glares into his rum. \"What?\"",
}

HANKLEVODE = {
    **body({"str": 12, "dex": 16, "con": 12, "int": 13, "wis": 10, "cha": 12},
           {"stealth": 3, "sleight": 3, "lockpick": 3, "blade": 2}, hp(28)),
    "faction": None,
    "description": "Hanklevode, a lean human mercenary thief with clever hands and a coat full of pockets, new in from Malice.",
    "dialog": {
        "malice|smith|from": "\"Malice dried up. The Smith's people want you to swear to him, and swearing doesn't pay.\"",
        "work|job|opportunity|hire": "\"I'm looking for opportunities. If you've got a door that needs opening quietly, I'm listening.\"",
        "lock|locks|pick|door|warehouse": "\"Those bonded warehouse locks are Landfall-made and cheap. A steady hand and ten quiet "
                                          "minutes. Mind the bruiser outside, though.\"",
        "gog|guild": "\"Gog's people have been friendly. Dominico's have been very friendly. That worries me more.\"",
    },
    "default_line": "Hanklevode flips a coin across his knuckles. \"Locks, Malice or work?\"",
}

QUILLON = {
    "body": 1, "wits": 3, "will": 3, "skills": {"parley": 2}, "faction": "the Refuge", "sells": SELLS_APOTHECARY,
    "description": "Master Quillon, steward of the High Apothecary: silver-haired, gloved, and able to look down his nose at "
                   "people taller than he is.",
    "dialog": {
        "drink|menu|price|wine|room": "\"House wine five copper. The Landfall vintage fifty gold. Rooms one gold, with clean sheets.\"",
        "bath|lemon": "\"The lemon bath, one gold. Lime stings the skin clean, and then the attendant sees to the rest.\"",
        "dominico|table": "\"Master Dominico's table is reserved. Always. I suggest you do not sit at it.\"",
        "elves|elf|officer|uniform": "Quillon's face does nothing at all. \"We have had no elves here. Ever. The officer may enjoy his steak.\"",
        "custodian": "\"The Custodian entertains his guests here. He has excellent taste and an excellent account.\"",
    },
    "default_line": "Quillon inclines his head one degree. \"Dining, wine, the bath, or a room?\"",
}

VOSS = {
    **body({"str": 14, "dex": 12, "con": 13, "int": 12, "wis": 14, "cha": 11},
           {"insight": 2, "intimidation": 2, "investigation": 2, "blade": 2}, hp(30)),
    "faction": "Vorkathia",
    "description": "Lieutenant Aurel Voss of Vorkathia, in a uniform pressed to a knife edge, eight-armed sigil at his throat, "
                   "eating a steak with surgical care.",
    "brief": "You are Lieutenant Aurel Voss, an officer of Vorkathia, sent to bring home high elves who fled the Inquisition. "
             "You have traced a group to Klhyts Refuge. The staff here go quiet whenever you look at them, and the elves you "
             "found had already left. You are courteous, patient, utterly certain you are in the right, and you pay for "
             "information. You have no authority in this town and you know it, which makes you careful.",
    "dialog": {
        "elves|elf|fugitive|hunting": "\"I seek certain elven persons, fugitives from Vorkathian justice. There would be a reward "
                                      "for word of where they sleep. A generous one.\"",
        "vorkath|vorkathia|landfall|inquisition": "\"Vorkath has eight arms, and a long reach. Even here.\"",
        "steak|food": "\"The steak is done to my liking. The service is not.\"",
        "town|refuge": "\"A town of runaways. Charming. Every one of them is running from somebody.\"",
    },
    "default_line": "Voss dabs his mouth with a napkin. \"Yes?\"",
}

PHILLIP = {
    **body({"str": 10, "dex": 12, "con": 10, "int": 14, "wis": 11, "cha": 15}, {"persuasion": 3, "deception": 2}, hp(20)),
    "faction": None,
    "description": "Phillip Everuex, of the noble family Everuex: powdered, beribboned, sweating through a coat made for a "
                   "colder country. The River Queen, the family's glass-cannon steamboat, is somewhere in the harbour.",
    "dialog": {
        "everuex|family|noble": "\"The Everuex are a family of standing. We have interests across Shalamar. And people.\"",
        "deloris|cousin|woman|looking": "\"A woman. Dark hair, sharp tongue, sharper knives. She ran from the family. The family "
                                        "would very much like her home.\"",
        "river queen|boat|ship|steamboat": "\"The River Queen. Steam, glass and cannon. The finest boat on any river.\"",
        "heat|weather": "\"How does anyone live here? I have changed my shirt four times.\"",
    },
    "default_line": "Phillip fans himself with a menu. \"Do you want something?\"",
}

WENDELINE = {
    "body": 1, "wits": 4, "will": 3, "skills": {"lore": 3}, "faction": "the Refuge", "sells": SELLS_UNICORN,
    "description": "Wendeline Moss, keeper of the Touchy Unicorn and its library: spectacles on a chain, ink on her sleeves, "
                   "and a way of saying shh that could stop a charging boar.",
    "dialog": {
        "drink|menu|price|room|food": "\"Scraps are free. Ale a copper. A room a copper, bath included, and quiet is compulsory.\"",
        "library|books|read|study": "\"A genuine library. Histories of Landfall, the colonies, the jungle gods. Read in here, not in bed.\"",
        "guests|fugitives|hiding|elves": "\"Our guests come here not to be found. I don't find them. Neither will you.\"",
        "eyes|treeline|animals|pond|bugs": "\"The animals watch, that's all. The bugs bite. The pond breeds them. I've written to the "
                                           "Town Hall about the pond. Eleven times.\"",
    },
    "default_line": "Wendeline lowers her spectacles. \"Shh. Rooms, books, or supper?\"",
}

ITHRIEL = {
    **body({"str": 8, "dex": 15, "con": 10, "int": 16, "wis": 13, "cha": 12},
           {"arcana": 3, "history": 3, "stealth": 2}, hp(20)),
    "faction": None,
    "description": "A slender elf in a borrowed fisherman's coat, hood up indoors, reading by a single candle and watching "
                   "the door over the top of the page.",
    "brief": "You are Ithriel, a high elf fleeing the Vorkathian Inquisition with what remains of your household. You ate at "
             "the High Apothecary until the staff warned you an officer had come; you left that night. You trust nobody who "
             "asks your name. You will trade knowledge (arcana, history, the old elven roads) for help getting your people "
             "passage off this coast before Lieutenant Voss finds them.",
    "dialog": {
        "name|who|elf|elves": "The elf closes the book. \"Nobody. A reader. You should find another table.\"",
        "officer|voss|vorkathia|inquisition": "Very quietly: \"If a man in a pressed uniform asks you about elves, you have never seen one.\"",
        "help|passage|ship|catan|moonmoth": "\"The Moonmoth will take my household south, if we can reach the pier without the "
                                            "officer seeing. Five of us. If you would walk with us, take this: the captain will "
                                            "let you aboard.\"",
        "magic|arcana|book|history": "\"The old roads, the old words, the old gods. Ask properly and I may answer.\"",
    },
    "gives": {"help|passage|ship|catan|moonmoth": {"item": "Silverleaf token",
                  "line": "The elf presses a leaf of living silverwood into your palm and closes your fingers over it.",
                  "gone_line": "\"I gave my token already. I have only the one.\""}},
    "default_line": "The elf turns a page and does not look up. \"I'm reading.\"",
}

DELORIS = {
    **body({"str": 12, "dex": 18, "con": 13, "int": 14, "wis": 12, "cha": 16},
           {"acrobatics": 3, "sleight": 3, "stealth": 3, "deception": 3, "insight": 3, "perception": 3,
            "lockpick": 3, "aim": 3, "blade": 3}, hp(58)),
    # Ed's character, and only Ed's (owner, 2026-11-22): no open seat offers her, and a hire never hands her seat on
    "playable": False, "faction": None,
    "description": "Deloris: lean and pale, tousled dark hair, a hooded cloak over leather armour, a longbow across her back. "
                   "She always stands where she can see every way out.",
    "brief": "You are Deloris, a Catalan assassin on the run from your merchant family, with a complicated history and a "
             "promise to protect the defenceless. Calm, with a cutting wit when trust is earned; paranoid about organised "
             "power. You came to Klhyts Refuge to not be found, and keep a room at the Stripperwitch, where red velvet "
             "hides a great deal. Phillip Everuex is in town asking for you. You join nobody lightly: whoever wants "
             "your bow ends Everuex's hunt first, and then pays like it.",
    "dialog": {
        "name|who": "\"Nobody you need to remember.\"",
        "family|everuex|phillip|running": "\"I do not seek mercy. I seek the path that will end this chase, for good or for me.\"",
        "help|job|work|hire|join": "\"Every vow has a price. Mine starts with the man hunting me. End Everuex's hunt, then "
                                   "come back with twenty-five gold a day, and I may listen.\"",
        "quiet|silence": "\"In silence there is a weapon as sharp as any blade.\"",
    },
    "default_line": "Deloris watches you without moving. \"Say it.\"",
}

KAEL = {
    **body({"str": 16, "dex": 12, "con": 14, "int": 10, "wis": 11, "cha": 13},
           {"athletics": 2, "intimidation": 2, "survival": 2, "blade": 2}, hp(38)),
    # not a seat players pick (owner, 2026-11-22); hiring him is how a player gets his seat, for a sub-agent
    "playable": False, "faction": None,
    "description": "Kael Ironjaw, a loud Jonulvicha sellsword from Vorkathia's frontier: his father's hat, a bright scarf, "
                   "dyed straps, and a glaive he found in a ditch.",
    "brief": "You are Kael Ironjaw, a Jonulvicha (half-orc) sellsword from the frontier camps of Vorkathia, loyal to a fault, reckless, not "
             "clever. You charge first and ask questions never. The hat was your father's; you have no idea what he looked "
             "like. You fight because leaving others to fight alone would be rude. You drink at the Rampant Ogre on what "
             "is left of your coin, looking for work.",
    "dialog": {
        "fight|trouble|work|job": "\"I don't need a map to know where the fight is. I follow the noise.\"",
        "hat": "\"This hat don't scare easy. Neither do I.\"",
        "plan|danger": "\"If it's coming for us, we don't wait for it to knock.\"",
    },
    "default_line": "Kael grins. \"Point me at something.\"",
}

NEWCOMER = {
    **body({"str": 10, "dex": 14, "con": 12, "int": 13, "wis": 15, "cha": 10},
           {"perception": 2, "insight": 2, "investigation": 2, "stealth": 2}, 10),
    "playable": True, "faction": None, "stays": True,
    "description": "You, fresh off a fishing boat from somewhere you would rather not talk about, salt in your hair and "
                   "everything you own on your back.",
}

TEMPLATES_STATE = {
    "refugee": ({"str": 10, "dex": 14, "con": 12, "int": 13, "wis": 15, "cha": 10},
                {"perception": 2, "insight": 2, "investigation": 2, "stealth": 2}, 10,
                "Off the last boat from Landfall, running from something you would rather not name.", "docks", 150,
                [("Knife", DAGGER)]),
    "sellsword": ({"str": 15, "dex": 13, "con": 14, "int": 10, "wis": 12, "cha": 8},
                  {"athletics": 2, "intimidation": 2, "blade": 2, "survival": 2}, 12,
                  "A sword for hire, between hires.", "docks", 60,
                  [("Shortsword", arm("shortsword", "A soldier's shortsword, nicked and oiled."))]),
    "lizardfolk": ({"str": 14, "dex": 12, "con": 15, "int": 8, "wis": 13, "cha": 10},
                   {"nature": 2, "survival": 2, "perception": 2, "athletics": 2}, 11,
                   "A Lizardfolk of the Meters, a fisher, in town to sell the catch and drink the proceeds.", "docks", 40,
                   [("Fishing spear", arm("spear", "A barbed fishing spear, the shaft worn smooth."))]),
    "elf": ({"str": 8, "dex": 14, "con": 10, "int": 15, "wis": 13, "cha": 12},
            {"arcana": 2, "history": 2, "stealth": 2, "insight": 2}, 9,
            "An elf in exile, on the run from the Vorkathian Inquisition, travelling under someone else's name.", "docks", 300,
            [("Knife", DAGGER), ("Silverleaf token", {"portable": True, "bulk": 0, "elf_token": True,
                                                      "description": "A leaf of living silverwood: your people's word, to give to one you trust."})]),
    "xoton": ({"str": 14, "dex": 12, "con": 15, "int": 10, "wis": 13, "cha": 8},
              {"sailing": 2, "athletics": 2, "perception": 2, "brawl": 2}, 12,
              "A Xoton sailor ashore between ships: barrel-bodied, sea-legged, and correcting everyone who says it with a Z.",
              "docks", 90, [("Hooked knife", {**DAGGER, "description": "A Xoton hooked knife, for nets and rigging."}),
                            ("Glow kelp lamp", {"portable": True, "lit": True, "description": "A glass globe of glow kelp."})]),
    "jonulvicha": ({"str": 16, "dex": 12, "con": 14, "int": 8, "wis": 10, "cha": 13},
                   {"athletics": 2, "intimidation": 2, "brawl": 2, "survival": 2}, 12,
                   "A Jonulvicha, half-orc and half Öchland barbarian by blood, off the Vorkathian frontier and done with it.",
                   "docks", 50, [("Cleaver", arm("handaxe", "A heavy frontier cleaver."))]),
}
TEMPLATE_PEOPLE = {"refugee": "human", "sellsword": "human", "lizardfolk": "lizardfolk", "elf": "elf", "xoton": "xoton",
                   "jonulvicha": "jonulvicha"}

LETTER_TEXT = ("Gog. The harbour dues don't add up. Three seasons of it, skimmed before it reaches the strongbox, and the "
               "Custodian signs every tally. I mean to have it out with him tonight at your place, in the red booth, quiet. "
               "If I'm not back by morning, look to the docks: Dominico's lot hold the bonded warehouse keys. Burn this. K.")
TALLY_TEXT = ("HARBOUR DUES, three seasons. Collected by the harbourmaster: 41 gp, 46 gp, 52 gp. Lodged in the strongbox: "
              "29 gp, 27 gp, 24 gp. Every page signed by the Custodian. In Klhyt's hand, in the margin: WHERE IS THE REST.")
PASSAGE_TEXT = ("EMERALD EYE, Capt. D. DeVito, for Catan on the one o'clock tide. Berths: three, one taken (Thoradin, paid). "
                "Cargo: one crate, PERSONAL EFFECTS, from the bonded warehouse, paid in gold by the Office of the Custodian. "
                "DO NOT OPEN. Load at half past twelve.")
NOTICE_TEXT = ("BY ORDER OF THE CUSTODIAN: the Mayor is away upriver on town business. Harbour dues payable at the Town Hall "
               "as usual. / The Bard of Moonport, nightly at the Omberhulk & Nun. / Passage to Catan: ask at the Turtle Dragon. / "
               "HUSOK SOURFIST: you know what you did. Marta and the twins are at the Omberhulk.")
LIBRARY_TEXT = ("The Touchy Unicorn's library: A Short History of the Vorkathian Inquisition. The Colonies of the Western Shore. "
                "Of the Nine Jungle Gods, with plates. A Lizardfolk Grammar (Meters dialect). Tides and Soundings of the "
                "Shalamar Coast. On the spine of the last one someone has written KLHYT'S, PLEASE RETURN.")
PORTRAIT_TEXT = "Under the portrait, a brass plate: KLHYT, FOUNDER. HE CAME ASHORE WITH NOTHING, AND BUILT A REFUGE."
SUITE_TEXT = "Chalked on the door: HONEYMOON SUITE. Inside, three dog pelts on a flea-ridden bed. Someone has stacked chickens in the corner."

# ---- the peoples of the Refuge (owner, 2026-11-22): plenty of Xotons and humans, Jonulvicha (half-orcs), a lot of
# elves in exile, Lizardfolk tolerated, a rare siren; no Root Dwarves, who keep to themselves ---------------------------

PEOPLE_OF = {
    "Fat Gog": "lizardfolk", "River": "human", "Dominico": "human", "The Custodian": "human", "Klhyt": "human",
    "Brask": "human", "Tully": "human", "Harbourmaster Teague": "human", "Captain Eirik": "xoton", "Ssark": "lizardfolk",
    "Thoradin": "dwarf", "Bosun Maggs": "human", "Sister Agathe": "human", "The Bard of Moonport": "human",
    "Big Ludo": "jonulvicha", "Husok Sourfist": "human", "Hanklevode": "human", "Master Quillon": "human",
    "Lieutenant Voss": "human", "Phillip Everuex": "human", "Wendeline Moss": "human", "Ithriel": "elf",
    "Deloris": "human", "Kael Ironjaw": "jonulvicha", "Newcomer": "human",
    "Captain Danny DeVito": "human", "Hulda Ironwake": "xoton", "Ruk Halfhand": "jonulvicha", "Mother Ines": "human",
    "Hallvard Saltbeard": "xoton", "Grusha": "jonulvicha", "Saelwyn": "elf", "Captain Aelith": "elf", "Ondrine": "siren",
}

# the Night Market and its vendors ----------------------------------------------------------------------------------

SELLS_INES = {
    "mango|mangoes|fruit": {"price": 1, **fed_on(dish("Mango", "A mango so ripe it is mostly juice.", "Juice to the elbows. Worth it."), "fruit")},
    "pineapple": {"price": 2, **fed_on(dish("Pineapple", "A whole pineapple, its top still green.", "Sharp, sweet, and gone."), "fruit", 2)},
    "coconut": {"price": 1, "type": "thing", "name": "Coconut", "state": {
        "kind": "drink", "left": 1, "description": "A green coconut with the top lopped off, full of cool water.",
        "description_empty": "An empty coconut shell."}},
}
SELLS_HALLVARD = {
    "lamp|kelp|glow": {"price": 200, **token("Glow kelp lamp", "A glass globe of Xoton glow kelp: green light, never needs oil.", lit=True)},
    "bolas|bola": {"price": 50, **token("Fishing bolas", "Three weighted cords, Xoton-made, for tangling fish or legs.")},
    "rope|line": {"price": 5, **token("Coil of Xoton rope", "Thirty feet of tarred Xoton line. It does not fray.")},
    "knife|hook|hooked": {"price": 30, "type": "thing", "name": "Hooked knife", "state": {
        **DAGGER, "description": "A Xoton hooked knife, for nets, rigging and arguments."}},
}
SELLS_GRUSHA = {
    "skewer|goat|meat|food": {"price": 2, **fed_on(dish("Goat skewer", "Charred goat on a stick, dripping fat.", "Smoky, peppery, and too hot to hold."), "meat", 2)},
    "pepper|sauce|hot": {"price": 1, **dish("Pot of pepper sauce", "A clay pot of Jonulvicha pepper sauce. People cry.",
                                            "You cry. Everyone watching laughs.")},
}
SELLS_SAELWYN = {
    "tea|moon|lily": {"price": 3, "type": "thing", "name": "Cup of moon-lily tea", "state": {
        "kind": "drink", "left": 1, "description": "Pale tea that smells of night flowers.", "description_empty": "An empty clay cup."}},
    "charm|silverleaf|leaf": {"price": 100, **token("Silver leaf charm", "A leaf of beaten silver on a cord. Elven work, and old.")},
    "map|coast|south": {"price": 20, "type": "letter", "name": "Map of the southern coast", "state": {
        "bulk": 0, "text": "A hand-drawn chart of the coast south of the Refuge: coves, a reef marked DO NOT, and far to the "
                           "south a tower drawn very small, with an elven word beside it that means 'still waiting'.",
        "description": "A chart on thin paper, folded small."}},
}

INES = {"body": 1, "wits": 2, "will": 3, "skills": {"parley": 2}, "sells": SELLS_INES,
        "description": "Mother Ines, a broad, laughing colonial woman behind a pyramid of mangoes, fanning herself with a palm leaf.",
        "dialog": {"fruit|mango|price|buy": "\"Mangoes a copper, pineapple two, coconut a copper, and the shade is free.\"",
                   "klhyt|mayor": "\"The mayor buys a mango off me every morning. Every morning. Four mornings, nothing.\"",
                   "market|night|why": "\"Too hot to sell in the day. The whole town shops after dark now.\""},
        "default_line": "Ines fans herself. \"Fruit, gossip or shade?\""}
HALLVARD = {"body": 2, "wits": 3, "will": 2, "skills": {"parley": 2}, "sells": SELLS_HALLVARD,
            "description": "Hallvard Saltbeard, a Xoton chandler with a beard full of salt crystals, selling ship's goods off a "
                           "tarpaulin: glow kelp lamps, rope, bolas, hooked knives.",
            "dialog": {"lamp|kelp|glow|price|buy": "\"Glow kelp lamp, two gold, never needs oil. Bolas fifty copper. Rope five.\"",
                       "xoton|crows|nest": "\"Xoton, with the X. We come, we trade, we go. The Crows Nest floats where it likes.\"",
                       "timber|trade": "\"Our captains buy timber. Straight and tall. Your jungle grows it like weeds.\""},
            "default_line": "Hallvard holds up a glowing globe. \"Lamps, rope, bolas, knives. Xoton-made.\""}
GRUSHA = {"body": 3, "wits": 2, "will": 3, "skills": {"brawl": 2}, "sells": SELLS_GRUSHA,
          "description": "Grusha, a Jonulvicha cook with brass-capped tusks, turning goat skewers over a brazier and daring "
                         "people to try the pepper sauce.",
          "dialog": {"skewer|goat|food|price|buy": "\"Skewer two copper. Pepper sauce one, and you'll want water after.\"",
                     "jonulvicha|half|orc|frontier": "\"Jonulvicha. Half-orc, if you're rude. My mother came off the frontier camps. "
                                                     "I came off a boat.\"",
                     "klhyt|mayor": "\"Klhyt ate my skewers and never once made a face. Good man. Gone four days. Bad sign.\""},
          "default_line": "Grusha points her tongs at you. \"Hungry or nosy?\""}
SAELWYN = {**body({"str": 8, "dex": 14, "con": 10, "int": 14, "wis": 15, "cha": 12}, {"medicine": 2, "nature": 2, "history": 2}, hp(20)),
           "sells": SELLS_SAELWYN,
           "description": "Saelwyn, an elf in exile selling moon-lily tea and silver trinkets from a folding table, her hood "
                          "always up, her eyes always on the street.",
           "dialog": {"tea|charm|map|price|buy": "\"Moon-lily tea three copper. A silver leaf, a gold piece. Charts of the coast, two silver.\"",
                      "exile|elves|elf|landfall": "\"Vorkath declared us enemies of the state long before I was born. Here, we sell tea.\"",
                      "moonmoth|ship": "\"The Moonmoth takes our people south. Ask Captain Aelith. Bring someone who will vouch for you.\"",
                      "officer|voss|uniform": "\"There is a man in a pressed uniform at the Apothecary. I am not selling him tea.\""},
           "default_line": "Saelwyn pours without looking. \"Tea, charms, or a chart?\""}

# the docks: ships and the people who work them -----------------------------------------------------------------------

DEVITO = {"body": 2, "wits": 3, "will": 3, "skills": {"parley": 3, "blade": 1},
          "description": "Captain Danny DeVito of the Emerald Eye: a small captain, round as a barrel, in a coat with more gold "
                         "braid than coat, counting coins on an upturned crate.",
          "brief": "You are Danny DeVito, small captain of the Emerald Eye. You like gold. You are carrying a crate of 'personal "
                   "effects' to Catan on the one o'clock tide for the Office of the Custodian, paid in gold, and you do not ask "
                   "what is in crates. You are loud, vain, funny, and you can be bought.",
          "dialog": {"crate|cargo|custodian": "\"A crate's a crate. The Custodian pays in gold, and gold doesn't ask what's in "
                                              "crates, so neither do I.\"",
                     "gold|money|pay": "\"I like gold. Gold likes me. We're very happy together.\"",
                     "catan|passage|berth|ship|emerald": "\"The Emerald Eye sails for Catan on the one o'clock tide. Berths through "
                                                          "Maggs at the Turtle Dragon. Two gold, and don't touch my rail.\"",
                     "small|size|height": "\"Small captain. Big ship. You do the maths.\""},
          "default_line": "DeVito bites a coin. \"Gold, the Emerald Eye, or Catan. Talk fast.\""}
HULDA = {"body": 3, "wits": 2, "will": 3, "skills": {"athletics": 2, "brawl": 2},
         "description": "Hulda Ironwake, bosun of the Xoton cog Whispers of the Deep: arms like hawsers, a whistle on a chain, "
                        "and a voice that carries across the harbour.",
         "dialog": {"ship|cog|whispers": "\"Whispers of the Deep. Cog-rigged, deep-keeled, and she's never lost a crate yet.\"",
                    "xoton|crows|nest": "\"Xoton. We're on every coast that floats. Mind the X.\"",
                    "warehouse|crate|lights": "\"That bonded warehouse has had a man sitting on its door for four nights. Nobody "
                                              "guards fish that hard.\"",
                    "work|job|hire": "\"Need hands for the morning tide. You any good with a line?\""},
         "default_line": "Hulda blows a short blast on her whistle at somebody. \"What?\""}
RUK = {"body": 4, "wits": 1, "will": 2, "skills": {"athletics": 3, "brawl": 2},
       "description": "Ruk Halfhand, a Jonulvicha stevedore foreman missing two fingers, tusks capped in iron, a tally stick behind each ear.",
       "dialog": {"crate|heavy|warehouse": "\"Carried a crate into that bonded warehouse four nights back. Custodian's seal. Heavy as a "
                                          "man.\" He stops. \"Heavy as a big crate.\"",
                  "work|job|stevedore": "\"Crates off, crates on. Pays in copper and bad backs.\"",
                  "jonulvicha|half|orc": "\"Jonulvicha. My father came off the frontier camps with nothing. Now I've got half a hand and a crew.\""},
       "default_line": "Ruk shifts a crate off his shoulder. \"You lifting or talking?\""}
AELITH = {**body({"str": 10, "dex": 16, "con": 12, "int": 15, "wis": 16, "cha": 15},
                 {"sailing": 4, "arcana": 3, "insight": 3, "perception": 3, "blade": 2}, hp(44)),
          "description": "Captain Aelith of the Moonmoth: an ageless elf in a coat of grey moth-silk, with a voice like a bell "
                         "heard underwater and eyes that do not blink often enough.",
          "brief": "You are Captain Aelith of the Moonmoth, an elven ship grown, not built. You carry elves in exile south, away "
                   "from Vorkath's reach, to a tower where an old one of your people waits. You take no one else aboard unless an "
                   "elf vouches for them with a silverleaf token. You know Ithriel and five of her household want passage; you "
                   "will take them if they can reach your deck unseen by the Vorkathian officer.",
          "dialog": {"moonmoth|ship|grown": "\"She was grown, not built: a silverwood seed in still water for a hundred years. She "
                                            "chooses her crew. I only argue with her.\"",
                     "south|tower|where": "\"South. Where an old one of our people waits. That is all you need.\"",
                     "passage|board|aboard|take": "\"Elves, and those an elf vouches for. No one else sets foot on her deck.\"",
                     "ithriel|household|five": "\"Ithriel's household has a place aboard, if they can reach the pier without the "
                                               "officer's eyes on them.\"",
                     "voss|officer|vorkath": "\"Vorkath's officer eats steak half a mile from my deck. He may finish his supper. He may not board.\""},
          "default_line": "Aelith regards you for a long moment. \"Speak, then.\""}
ONDRINE = {**body({"str": 10, "dex": 15, "con": 12, "int": 16, "wis": 13, "cha": 20},
                  {"performance": 5, "arcana": 3, "persuasion": 4, "deception": 3}, hp(40)),
           "hidden": True,
           "description": "A siren from the Heartless Sea: pale as a pearl, hair like wet black silk, a sealskin purse at her hip "
                          "and a wizard-school primer under one arm.",
           "brief": "You are Ondrine, a siren from the Heartless Sea, putting yourself through wizard school by singing at the "
                    "Stripperwitch once in a long while. Tonight is one of those nights. You are amused by mortals, fond of River, "
                    "and very tired of being asked to drown people. Years ago you watched a castaway wash up on this beach; Fat "
                    "Gog reached him before you did. You sing, collect your fee, and go back to the sea before the tide turns.",
           "dialog": {"wizard|school|exam|study": "\"I'm putting myself through wizard school. Singing pays better than drowning "
                                                   "sailors, and the sailors prefer it.\"",
                      "sea|heartless|home": "\"The Heartless Sea. It's not heartless. It's just busy.\"",
                      "song|sing|music": "\"Once in a long while, here, for River. Tonight is a while.\"",
                      "klhyt|castaway|beach": "\"The castaway? I watched him wash up, years ago, dry as driftwood. Fat Gog got to "
                                              "him before I did.\" She smiles. \"Lucky castaway.\""},
           "default_line": "The siren looks at you the way the sea looks at a boat. \"Yes?\""}

# crowds: place state, not a hundred bodies (reach-roles BUILDING.md, Scale) ---------------------------------------------

RUMOURS_MARKET = [
    "\"Klhyt's gone upriver, the Custodian says. Klhyt hates rivers. Everybody knows Klhyt hates rivers.\"",
    "\"The Custodian went in the Stripperwitch's side door last night. Again. Never set foot in the place, mind you.\"",
    "\"Dominico gave Fat Gog till midnight. Midnight for what, nobody's saying, and nobody's asking.\"",
    "\"There's a siren comes up out of the harbour some nights and sings at the Stripperwitch. Tonight, they say. "
    "Paying her way through wizard school.\"",
    "\"A Vorkathian officer's eating steak at the Apothecary, asking after elves. The elves are asking after ships.\"",
    "\"That elf ship at the end of the pier was grown, not built. Grown! Out of a seed!\"",
    "\"Fat Gog pulled Klhyt off the beach when he washed up. If anyone finds the mayor, it'll be Gog.\"",
    "\"Xotons are buying timber. Straight trunks, tall ones. They pay in silver, and they don't haggle.\"",
    "\"Husok Sourfist's got twins he won't own. Marta's looking for him with a skillet.\"",
    "\"The mayor ran off with a Catan widow, I heard.\" A pause. \"No, I didn't believe it either.\"",
]
RUMOURS_DOCKS = [
    "\"Brask's been sitting on that warehouse door four nights. Nobody guards fish that hard.\"",
    "\"The Emerald Eye sails for Catan on the one o'clock tide. Her captain's carrying something for the Custodian.\"",
    "\"Ruk says the crate they carried in was heavy as a man. Then he says he never said that.\"",
    "\"The Moonmoth takes elves south. Nobody else gets up her gangplank. It lifts itself, I swear.\"",
    "\"Xoton trader out past the mouth. They'll buy anything that floats and most things that don't.\"",
    "\"Some nights something climbs out of the harbour at the end of the pier. Pretty, they say. Don't look.\"",
]
RUMOURS_DECK = [
    "\"Ithriel's household is still ashore. Five of them. The officer is watching the Apothecary, not the pier.\"",
    "\"The captain says the Moonmoth will not sail without the ones still in the town.\"",
    "\"In Landfall they burned the library at Kirchheim. Here they sell us tea. It is better here.\"",
]
CROWDS = {
    "market": ("Market crowd", {"mix": {"human": 5, "xoton": 4, "elf": 3, "jonulvicha": 2, "lizardfolk": 1}, "max_faces": 8,
                                "rumours": RUMOURS_MARKET,
                                "description": "Hundreds of people under the lanterns: colonists and Landfall runaways, Xoton sailors "
                                               "on shore leave, Jonulvicha porters, elves in exile with their hoods up, a few Lizardfolk "
                                               "of the Meters selling fish. Mingle and you'll hear things; hail someone and they'll stop."}),
    "docks": ("Dockside crowd", {"mix": {"xoton": 5, "human": 4, "jonulvicha": 3, "lizardfolk": 1}, "max_faces": 6,
                                 "rumours": RUMOURS_DOCKS,
                                 "description": "Dockhands, Xoton sailors, Jonulvicha stevedores and fishermen, working by lamplight "
                                                "and drinking between loads."}),
    "moonmoth": ("Exiles on deck", {"mix": {"elf": 1}, "max_faces": 4, "rumours": RUMOURS_DECK,
                                    "description": "Elves in exile, two dozen of them, sitting quietly among their bundles on the "
                                                   "Moonmoth's deck, waiting for the ones still ashore."}),
}

SHIPS = [
    ("The Emerald Eye", "A squat, gold-trimmed brigantine with a great green eye painted on her bow, berthed at the "
                        "pier's end nearest the warehouse. Danny DeVito's ship. She sails for Catan on the one o'clock tide."),
    ("Whispers of the Deep", "A deep-keeled Xoton cog unloading by lantern-light, her hold breathing out tar, kelp and "
                             "foreign spice."),
    ("The River Queen", "The Everuex family's steamboat: brass, glass and a bow cannon, polished to a shine, looking "
                        "faintly ridiculous among the fishing boats."),
    ("Dragons Claw", "Elliot's ship: a small galleon, small enough to fit the river, sturdy enough to have crossed from Landfall."),
    ("Fishing boats", "Fishing boats rafted three deep, nets drying on every rail, a cat asleep in every third one."),
]


# Ithriel's household (the five the Moonmoth waits for) and Xoton sailors ashore --------------------------------------

# ---- D&D 5e: classes, levels and kit ---------------------------------------------------------------------------------
# The dnd5e pack fights by these. Canon (LoreKeeper character sheets, D&D 5e 2014): Deloris's AC 16 (studded leather),
# HP 58 and her one saving throw, dex; Kael's AC 15 and HP 38. Every class and level, and all other armour, is a host
# default (notes/bible.md lists them). Xoton advantage on saves against poison is canon (the Xotons doc); Jonulvicha get
# the half-orc's relentless endurance and Lizardfolk a natural armour of 13, host defaults.

# name: (class, or None for a body with no class, level, {armor, spells, cast, slots, saves, ac})
FIVE_E = {
    "Fat Gog": ("fighter", 7, {}),
    "River": ("rogue", 4, {}),
    "Dominico": ("fighter", 7, {"spells": ["fire bolt", "shield", "magic missile"], "cast": "int", "slots": {"1": 3}}),
    "The Custodian": (None, 3, {}),
    "Klhyt": ("fighter", 6, {}),
    "Brask": ("fighter", 2, {"armor": "leather"}),
    "Tully": ("fighter", 1, {}),
    "Harbourmaster Teague": (None, 2, {}),
    "Captain Eirik": ("fighter", 4, {"armor": "leather"}),
    "Ssark": ("ranger", 2, {}),
    "Thoradin": ("ranger", 5, {"armor": "leather", "spells": ["cure wounds"]}),
    "Bosun Maggs": ("fighter", 2, {}),
    "Sister Agathe": ("cleric", 3, {"spells": ["sacred flame", "bless", "cure wounds", "healing word"]}),
    "The Bard of Moonport": ("bard", 4, {"spells": ["vicious mockery", "healing word", "charm person", "hideous laughter",
                                                    "shatter"]}),
    "Big Ludo": ("fighter", 3, {}),
    "Husok Sourfist": (None, 1, {}),
    "Hanklevode": ("rogue", 4, {"armor": "leather"}),
    "Master Quillon": (None, 2, {}),
    "Lieutenant Voss": ("fighter", 4, {"armor": "breastplate"}),
    "Phillip Everuex": (None, 3, {}),
    "Wendeline Moss": (None, 2, {}),
    "Ithriel": ("wizard", 5, {"spells": ["fire bolt", "ray of frost", "magic missile", "shield", "mage armor", "hold person",
                                        "faerie fire"]}),
    "Deloris": ("rogue", 9, {"armor": "studded leather", "saves": ["dex"]}),
    "Kael Ironjaw": ("fighter", 4, {"ac": 15}),
    "Newcomer": ("rogue", 1, {}),
    "Captain Danny DeVito": (None, 3, {}),
    "Hulda Ironwake": ("fighter", 3, {}),
    "Ruk Halfhand": (None, 2, {}),
    "Mother Ines": (None, 1, {}),
    "Hallvard Saltbeard": (None, 2, {}),
    "Grusha": ("fighter", 1, {}),
    "Saelwyn": ("druid", 3, {"spells": ["thorn whip", "produce flame", "cure wounds", "healing word", "entangle",
                                       "faerie fire"]}),
    "Captain Aelith": ("fighter", 5, {"armor": "chain shirt"}),
    "Ondrine": ("wizard", 3, {"spells": ["ray of frost", "fire bolt", "magic missile", "shield", "charm person",
                                        "hideous laughter"]}),
}
RACE_5E = {"xoton": {"save_adv": ["poison"]}, "jonulvicha": {"relentless": True}, "lizardfolk": {"natural_ac": 13}}
ARMOUR = {"leather": ("Leather jerkin", "A jerkin of boiled leather, salt-stained."),
          "studded leather": ("Studded leather", "Dark leather studded with red metal rivets."),
          "breastplate": ("Breastplate", "A Vorkathian officer's breastplate, the eight-armed sigil chased on it."),
          "chain shirt": ("Moth-silk mail", "Fine elven mail worn under a coat, light as cloth."),
          "coral": ("Coral armour", "Xoton coral armour: plates of sea-coral on sharkskin, light and quiet.")}
# a template's class (level 1), the armour a new character starts in and the spells it knows
TEMPLATE_5E = {"refugee": ("rogue", [], []), "sellsword": ("fighter", ["leather"], []), "lizardfolk": ("fighter", [], []),
               "elf": ("wizard", [], ["fire bolt", "ray of frost", "magic missile", "shield", "mage armor"]),
               "xoton": ("fighter", ["coral"], []), "jonulvicha": ("barbarian", [], [])}
WEAPON_KEYS = ["kind", "dice", "dtype", "category", "properties", "versatile", "ranged", "ammo", "bonus"]


def armour_state(kind):
    """An ARMOUR entry as a carried thing: (name, state). Xoton coral is light armour, 11 + dex (the Xotons doc)."""
    name, desc = ARMOUR[kind]
    if kind == "coral":
        return name, armor5("leather", kind="coral armor", description=desc)
    return name, armor5(kind, description=desc)


def scores_of(state):
    """A body's six 5e scores: its sheet's, else from d20's body, wits and will (10 + 2 x the stat)."""
    attrs = (state.get("sheet") or {}).get("attributes")
    if attrs:
        return {k: int(attrs.get(v, 10)) for k, v in ABILITY.items()}
    b, wi, wl = (int(state.get(k) or 1) for k in ("body", "wits", "will"))
    return {"str": 10 + 2 * b, "dex": 10 + 2 * b, "con": 10 + 2 * b, "int": 10 + 2 * wi, "wis": 10 + 2 * wi,
            "cha": 10 + 2 * wl}


def five_block(cls, level, scores, extra=None):
    """A body's 5e keys for a class and level (packs/dnd5e character()); one with no class has a level, a d8 hit die
    and no saving throws. A fighter who dabbles in magic gets spells off its own ability and slots."""
    extra = extra or {}
    lv = max(1, int(level))
    if cls is None:
        st = {"level": lv, "saves": [], "hit_die": "1d8", "hit_dice": lv, "hit_dice_max": lv,
              "hp": max(1, 8 + (lv - 1) * 5 + ((scores.get("con", 10) - 10) // 2) * lv)}
    else:
        st = character(cls, lv, scores, extra.get("spells"))
    if extra.get("spells") and "spellcasting" not in st:
        slots = dict(extra.get("slots") or {})
        st["spellcasting"] = {"ability": extra.get("cast") or "int", "spells": list(extra["spells"]), "slots": slots,
                              "slots_max": dict(slots), "pact": False}
    if extra.get("saves"):
        st["saves"] = list(extra["saves"])
    if extra.get("ac") is not None:
        st["ac"] = int(extra["ac"])
    return st


def build_five_e(s):
    """D&D 5e onto everyone named in FIVE_E and everyone made from a template: class, level, saves, spells and slots,
    hp at 5e's scale, their people's traits, and 5e numbers on the weapons they carry; armour for the named. Each body
    once (`five_e` marks it). Hp keep their share: a body at 8 of 10 under d20 stands at 30 of 38 under 5e. A player's
    own kit is theirs: the upgrade gives a body made from a template no armour."""
    w = s.world
    built = {name: (state, carries) for _, _, name, state, carries in people()}
    for e in w.find(limit=None):
        st = e["state"]
        if st.get("five_e") or st.get("dead") or not w.is_a(e["type"], "combatant"):
            continue
        name, tpl = e["name"], st.get("template")
        if name in FIVE_E:
            cls, lv, extra = FIVE_E[name]
            kit = list(built.get(name, ({}, []))[1])
            armours = [extra["armor"]] if extra.get("armor") else []
        elif tpl in TEMPLATE_5E:
            cls, _, spells = TEMPLATE_5E[tpl]
            lv, extra, armours = 1, {"spells": spells}, []
            kit = [("thing", n, k) for n, k in TEMPLATES_STATE[tpl][6]]
        else:
            continue  # minor folk and the crowd's faces roll their d20 stats as 5e scores
        block = five_block(cls, lv, scores_of(st), extra)
        block.update(RACE_5E.get(st.get("people"), {}))
        b_state = built.get(name, ({}, []))[0]
        new_max = int(b_state["max_hp"]) if b_state.get("sheet") and b_state.get("max_hp") else int(block["hp"])
        old_hp = int(st.get("hp") if st.get("hp") is not None else new_max)
        old_max = int(st.get("max_hp") or old_hp or 1)
        hp5 = new_max if old_hp >= old_max else (0 if old_hp <= 0 else max(1, round(old_hp * new_max / old_max)))
        if b_state.get("hp") is not None and int(b_state["hp"]) < int(b_state.get("max_hp") or 0):
            hp5 = min(hp5, int(b_state["hp"]))  # written low on purpose (Klhyt, starved in a crate)
        block.update({"hp": hp5, "max_hp": new_max, "five_e": 1, "wounded": False})
        s.patch(e["id"], block)
        mine = {c["name"] for c in w.children(e["id"])}
        for kind in armours:
            aname, ast = armour_state(kind)
            if aname not in mine:
                s.spawn("thing", e["id"], aname, state=ast)
    # every weapon from before dice, wherever it is now (left with a barman, dropped in the street), by its name
    known = {}
    for _, _, _, _, carries in people():
        for _, cname, cst in carries:
            if cst.get("weapon"):
                known.setdefault(cname, cst)
    for tpl in TEMPLATES_STATE.values():
        for cname, cst in tpl[6]:
            if cst.get("weapon"):
                known.setdefault(cname, cst)
    for e in w.find(limit=None):
        cst = known.get(e["name"])
        if cst and e["state"].get("weapon") and not e["state"].get("dice"):
            s.patch(e["id"], {k: cst[k] for k in WEAPON_KEYS if k in cst})


def minor(people, desc, dialog, default, **stats):
    return {"body": stats.get("body", 2), "wits": stats.get("wits", 2), "will": stats.get("will", 2),
            "skills": stats.get("skills", {}), "people": people, "description": desc, "dialog": dialog, "default_line": default}


HOUSEHOLD = [
    ("Faelan", "A grey-haired elf with a scholar's stoop, keeping his back to the wall and a book he isn't reading open on his knee.",
     {"ithriel|household|family": "\"Ithriel leads us. Ask her, not me.\"",
      "landfall|vorkath|inquisition": "\"I taught at Kirchheim before they burned the library. I teach nobody now.\""}),
    ("Ysolde", "A young elf woman in a sailor's jacket two sizes too big, watching the treeline through the window.",
     {"moonmoth|ship|south": "\"The Moonmoth will wait for us. Ithriel says so. Ithriel is usually right.\"",
      "officer|voss": "\"I saw him at the Apothecary. Pressed uniform. Eight arms at his throat. We left before the soup.\""}),
    ("Corwen", "A broad-shouldered elf with a fisherman's hands and a long knife he keeps out of sight.",
     {"help|fight|protect": "\"If the officer comes, I'll be the one at the door. I'd rather not be.\"",
      "refuge|town": "\"Nobody asked our names here. That's worth more than you'd think.\""}),
    ("Miravel", "An elf child of perhaps sixty, which is young, drawing moths on the back of a menu.",
     {"moonmoth|moth|ship": "\"Her sails are wings. Saelwyn says she was a seed once. I'm going to sail on her.\"",
      "name|who": "\"Miravel. I'm not supposed to tell people that.\""}),
]
SAILORS = [
    ("Torvald Brineknot", "A Xoton sailor off the Whispers of the Deep, drinking a massive beer with both hands and singing under his breath.",
     {"ship|whispers|cog": "\"Whispers of the Deep. Best cog on any coast. Ask Hulda, she'll tell you, loudly.\"",
      "xoton|crows|nest": "\"Xoton. Crows Nest born. I've been ashore three days and the ground still moves.\""}),
    ("Ragna Seaward", "A Xoton woman with rope-burned palms and copper rings in her ears, arm-wrestling anyone who sits down.",
     {"arm|wrestle|wrestling|bet": "\"Sit down. A copper says I win. Everyone says no. Everyone loses.\"",
      "timber|trade": "\"Straight trunks, tall ones. The Crows Nest eats timber like Torvald eats oysters.\""}),
]

# ---- the map: metres, y north, the sea to the south ----------------------------------------------------------------

FRAME = {"units": "m", "up": "z", "north": "y"}
TOWN_AT = ([0, 0, 0], [640, 560, 2])
PLACE_AT = {
    "docks": ([0, -210, 0], [200, 50, 2]),
    "warehouse": ([125, -222, 0], [44, 26, 8]),
    "harbour": ([0, -150, 0], [300, 24, 2]),
    "turtle": ([-130, -122, 0], [30, 22, 7]),
    "ogre": ([20, -122, 0], [20, 16, 6]),
    "apothecary": ([125, -118, 0], [38, 30, 12]),
    "square": ([0, 0, 0], [80, 64, 2]),
    "hall": ([0, 62, 0], [40, 28, 10]),
    "study": ([14, 72, 0], [8, 8, 3]),
    "stripperwitch": ([-78, 18, 0], [30, 26, 9]),
    "omberhulk": ([78, 22, 0], [28, 24, 9]),
    "treeline": ([-170, 95, 0], [150, 14, 2]),
    "unicorn": ([-262, 150, 0], [28, 22, 8]),
    "gate": ([0, 250, 0], [24, 10, 6]),
    "market": ([48, -62, 0], [70, 40, 2]),
    "moonmoth": ([-112, -238, 0], [44, 10, 14]),
    "lanes": ([120, 110, 0], [90, 60, 2]),
    "cove": ([-290, -255, 0], [50, 40, 2]),
    "row": ([-60, -96, 0], [100, 10, 2]),
    "chandlery": ([-95, -82, 0], [18, 14, 7]),
    "anvil": ([-62, -82, 0], [16, 14, 6]),
    "coral": ([-30, -82, 0], [18, 14, 6]),
    "cells": ([-10, 70, -4], [12, 10, 3]),
    "graves": ([-190, 135, 0], [44, 30, 2]),
    "verde": ([115, -20, 0], [16, 100, 1]),
    "rivergate": ([140, 60, 0], [20, 12, 6]),
    "surgery": ([75, -124, 0], [14, 12, 6]),
    "reedhouse": ([135, 5, 1], [14, 12, 5]),
    "stonebridge": ([115, -50, 2], [26, 8, 4]),
    "washline": ([118, 45, 3], [22, 3, 2]),
    "swingbridge": ([115, -136, 1], [22, 6, 2]),
}
PLACE_TYPES = {"moonmoth": "elfship"}
PACKET_AT = ([0, -700, 0], [24, 7, 2])
AT_SEA = "The Emerald Eye, outward bound"
UNDER = "Under the Harbour"

# ---- the build, in stages that each check what is there by name, so a rerun adds only what is missing ----------------

STAGES = ["places", "layout", "people", "things", "wiring", "cast", "magistrate", "five_e", "statblocks", "hire", "glance",
          "peril", "missions", "shops", "law", "undertaker", "healers", "writing", "animals"]


def by_name(s):
    return {e["name"]: e for e in s.world.find(limit=None)}


def place_ids(s):
    have = by_name(s)
    return {k: have[name]["id"] for k, (name, _) in PLACES.items() if name in have}


def build_places(s, root):
    have = by_name(s)
    town = have["Klhyts Refuge"]["id"] if "Klhyts Refuge" in have else s.spawn("place", root, "Klhyts Refuge", state=TOWN)["id"]
    for key, (name, state) in PLACES.items():
        if name not in have:
            s.spawn(PLACE_TYPES.get(key, "place"), town, name, state=dict(state))
    if "The Catan Packet" in have and AT_SEA not in have:  # the invented packet gave way to a canon ship (owner, 2026-11-22)
        s.rename(have["The Catan Packet"]["id"], AT_SEA)
        have = by_name(s)
    if AT_SEA not in have:
        s.spawn("place", root, AT_SEA, state={
            "hidden": True, "water_source": True,
            "description": "The Emerald Eye, outward bound for Catan: a deck that won't keep still, a small captain counting "
                           "gold, and a long way from anywhere."})
    if UNDER not in have:
        s.spawn("place", root, UNDER, state={
            "hidden": True, "water_source": True,
            "description": "Under the harbour: green dark, cold water, and the long slow pull of the tide."})
    P = place_ids(s)
    done = set(tuple(x) for x in (s.inspect(town)["state"].get("built_ways") or []))
    for a, b in WAYS:
        if (a, b) not in done:
            s.connect(P[a], P[b])
            done.add((a, b))
    s.patch(town, {"built_ways": sorted(list(done))})
    return town


def build_layout(s):
    P = place_ids(s)
    have = by_name(s)
    placements = [{"entity": have["Klhyts Refuge"]["id"], "at": TOWN_AT[0], "size": TOWN_AT[1]},
                  {"entity": have[AT_SEA]["id"], "at": PACKET_AT[0], "size": PACKET_AT[1]}]
    for key, (at, size) in PLACE_AT.items():
        placements.append({"entity": P[key], "at": at, "size": size})
    paths = []
    for a, b in WAYS:
        pa, pb = PLACE_AT[a][0], PLACE_AT[b][0]
        paths.append({"a": P[a], "b": P[b], "route": [[pa[0], pa[1]], [pb[0], pb[1]]]})
    return s.layout(frame=FRAME, placements=placements, paths=paths)


# (type, place key, name, state, carries [(type, name, state)])
def people():
    return [
        ("person", "stripperwitch", "Fat Gog", FAT_GOG, [("thing", "Coin", coin(2400))]),
        ("person", "stripperwitch", "River", RIVER, [("thing", "Coin", coin(300)), ("thing", "Bar knife", DAGGER)]),
        ("person", "apothecary", "Dominico", DOMINICO, [("thing", "Coin", coin(900)), ("thing", "Sword-cane", arm(
            "rapier", "A black cane with a silver head and a thin blade inside it.", bonus=1))]),
        ("person", "hall", "The Custodian", CUSTODIAN, [("thing", "Coin", coin(1500)), ("thing", "Study key", {
            "portable": True, "bulk": 0, "description": "A brass key with a ship's wheel worked into the bow: the mayor's study."})]),
        ("person", "warehouse", "Klhyt", KLHYT, []),
        ("guard", "docks", "Brask", BRASK, [("thing", "Coin", coin(12)), ("thing", "Cudgel", CUDGEL), ("thing", "Warehouse key", {
            "portable": True, "bulk": 0, "description": "A heavy iron key stamped BONDED."})]),
        ("fighter", "ogre", "Tully", TULLY, [("thing", "Coin", coin(9)), ("thing", "Cudgel", CUDGEL)]),
        ("person", "docks", "Harbourmaster Teague", TEAGUE, [("thing", "Coin", coin(40))]),
        ("person", "turtle", "Captain Eirik", EIRIK, [("thing", "Coin", coin(800)), ("thing", "Hooked sword", arm(
            "longsword", "A Xoton hooked sword, for boarding and for arguments.", kind="hooked sword")),
            ("thing", "Glow kelp lamp", {"portable": True, "lit": True, "description": "A glass globe of kelp that glows green and never needs oil."})]),
        ("person", "turtle", "Ssark", SSARK, [("thing", "Coin", coin(25)), ("thing", "Gutting knife", DAGGER)]),
        ("person", "turtle", "Thoradin", THORADIN, [("thing", "Coin", coin(120)), ("thing", "Longbow", arm("longbow", "A dwarf-sized longbow, unstrung.")), ("thing", "Arrows", {"kind": "arrow", "ammo": "arrow",
                                                                                    "count": 12, "bulk": 0.05, "portable": True,
                                                                                    "description": "Grey-fletched arrows."})]),
        ("person", "turtle", "Bosun Maggs", MAGGS, [("thing", "Coin", coin(150))]),
        ("person", "omberhulk", "Sister Agathe", AGATHE, [("thing", "Coin", coin(90)), ("thing", "Bung-starter", CUDGEL)]),
        ("person", "omberhulk", "The Bard of Moonport", BARD, [("thing", "Coin", coin(30)), ("thing", "Lute", {
            "portable": True, "description": "A lute older than its owner, with a crack in the bowl mended with fish glue."})]),
        ("person", "ogre", "Big Ludo", LUDO, [("thing", "Coin", coin(70)), ("thing", "Cudgel", CUDGEL)]),
        ("person", "ogre", "Husok Sourfist", HUSOK, [("thing", "Coin", coin(3))]),
        ("person", "ogre", "Hanklevode", HANKLEVODE, [("thing", "Coin", coin(60)), ("thing", "Knife", DAGGER)]),
        ("person", "apothecary", "Master Quillon", QUILLON, [("thing", "Coin", coin(400))]),
        ("person", "apothecary", "Lieutenant Voss", VOSS, [("thing", "Coin", coin(1000)), ("thing", "Officer's sword", arm(
            "longsword", "A Vorkathian officer's sword, the eight-armed sigil on the pommel."))]),
        ("person", "apothecary", "Phillip Everuex", PHILLIP, [("thing", "Coin", coin(2000))]),
        ("person", "unicorn", "Wendeline Moss", WENDELINE, [("thing", "Coin", coin(60))]),
        ("person", "unicorn", "Ithriel", ITHRIEL, [("thing", "Coin", coin(350)), ("thing", "Knife", DAGGER),
                                                   ("thing", "Silverleaf token", {"portable": True, "bulk": 0, "elf_token": True,
                                                    "description": "A leaf of living silverwood, still green at the stem: an elf's word that you may be trusted."})]),
        ("person", "stripperwitch", "Deloris", DELORIS, [
            ("thing", "Coin", coin(400)), ("thing", "Daggers", {**DAGGER, "count": 2, "description": "A matched pair of throwing daggers."}),
            ("thing", "Longbow", arm("longbow", "A plain longbow, well kept.")),
            ("thing", "Arrows", {"kind": "arrow", "ammo": "arrow", "count": 20, "bulk": 0.05, "portable": True, "description": "Black-fletched arrows."}),
            ("thing", "Thieves' tools", {"portable": True, "bulk": 0, "description": "Picks, a tension wrench and a little mirror in a leather roll."})]),
        ("person", "ogre", "Kael Ironjaw", KAEL, [
            ("thing", "Coin", coin(30)), ("thing", "Glaive", arm("glaive", "A glaive he found in a ditch. It cuts fine.")),
            ("thing", "Father's hat", {"portable": True, "bulk": 0, "description": "A battered hat. It was his father's."})]),
        ("person", "docks", "Newcomer", NEWCOMER, [("thing", "Coin", coin(200)), ("thing", "Knife", DAGGER)]),
        ("person", "docks", "Captain Danny DeVito", DEVITO, [("thing", "Coin", coin(3000))]),
        ("person", "docks", "Hulda Ironwake", HULDA, [("thing", "Coin", coin(80)), ("thing", "Whistle", {
            "portable": True, "bulk": 0, "description": "A bosun's whistle on a chain."})]),
        ("person", "docks", "Ruk Halfhand", RUK, [("thing", "Coin", coin(35))]),
        ("person", "market", "Mother Ines", INES, [("thing", "Coin", coin(60))]),
        ("person", "market", "Hallvard Saltbeard", HALLVARD, [("thing", "Coin", coin(240))]),
        ("person", "market", "Grusha", GRUSHA, [("thing", "Coin", coin(45)), ("thing", "Cleaver", arm(
            "handaxe", "A butcher's cleaver, very clean."))]),
        ("person", "market", "Saelwyn", SAELWYN, [("thing", "Coin", coin(180))]),
        *[("person", "unicorn", n, minor("elf", d, dl, "The elf glances at the door before answering. \"Yes?\"",
                                          skills={"stealth": 1}), [("thing", "Coin", coin(40))]) for n, d, dl in HOUSEHOLD],
        *[("person", "turtle", n, minor("xoton", d, dl, "\"Xoton, with the X. What do you want?\"", body=3,
                                         skills={"brawl": 2}), [("thing", "Coin", coin(30))]) for n, d, dl in SAILORS],
        ("person", "moonmoth", "Captain Aelith", AELITH, [("thing", "Coin", coin(500)), ("thing", "Moth-silk blade", arm(
            "rapier", "A slim elven blade that makes no sound leaving its sheath.", bonus=1))]),
    ]


def build_people(s):
    P = place_ids(s)
    have = by_name(s)
    if "Ondrine" not in have:  # the siren waits under the harbour until the story raises her
        s.spawn("person", have[UNDER]["id"], "Ondrine", state={**ONDRINE, "people": "siren", "post": have[UNDER]["id"],
                                                               "home": have[UNDER]["id"]})
    town = have["Klhyts Refuge"]["id"]
    made = set(s.inspect(town)["state"].get("built_people") or [])
    for type_, where, name, state, carries in people():
        if name in have or name in made:
            continue
        st = {**state, "post": P[where], "home": P[where], "people": PEOPLE_OF.get(name, state.get("people", "human"))}
        if type_ == "guard":
            st["walks_to"] = P["ogre"]  # where a guard goes when he leaves his post: the nearest drink
        pid = s.spawn(type_, P[where], name, state=st)["id"]
        for ctype, cname, cstate in carries:
            s.spawn(ctype, pid, cname, state=dict(cstate))
        made.add(name)
    s.patch(town, {"built_people": sorted(made)})


# (type, place key, name, state)
def things():
    return [
        ("sign", "docks", "Harbour slate", {"text": HARBOUR_SLATE, **CHALK, "pen": True,
                                            "description": "A slate on a post by the pier, a stub of chalk on a string "
                                                           "beside it, where sailors chalk ships, tides and crews wanted."}),
        ("thing", "docks", "Water butt", {"portable": False, "water_source": True,
                                         "description": "A rain-water butt with a tin cup on a chain."}),
        ("thing", "docks", "Klhyt's signet ring", {"portable": True, "bulk": 0, "clue": "ring",
                                                   "description": "A heavy gold signet ring, a ship's wheel on the bezel, half "
                                                                  "trodden into the planks by the warehouse door."}),
        ("thing", "warehouse", "Big crate", {"portable": False, **WOOD, "description": "A crate big enough for a man, air holes drilled "
                                                                              "in the lid, a Custodian's seal on the paper tacked to it."}),
        ("sign", "turtle", "Price board", {"text": BOARD_TURTLE}),
        ("letter", "turtle", "Passage book", {"text": PASSAGE_TEXT, "clue": "passage", "burnable": False, **BOOK_ROOM,
                                              "description": "The Turtle Dragon's passage book, open on the bar."}),
        ("thing", "turtle", "Harpoons", {"portable": False, "description": "Two harpoons nailed up over the bar. Maggs would break your arm."}),
        ("dice", "turtle", "Knucklebone dice", {"description": "Two knucklebone dice, worn smooth by sailors' fingers."}),
        ("sign", "apothecary", "Price board", {"text": BOARD_APOTHECARY}),
        ("bath", "apothecary", "Lemon bath", {"description": "A copper tub of hot water with lemons and limes floating in it. A "
                                                             "woman with a large fishbone stands by with towels."}),
        ("thing", "apothecary", "Dominico's table", {"portable": False, **WOOD, "description": "A window table with a RESERVED card. "
                                                                                       "Nobody else sits there. Nobody."}),
        ("thing", "square", "Town pump", {"portable": False, "water_source": True, "description": "An iron pump with a long handle and a stone trough."}),
        ("sign", "square", "Notice board", {"text": NOTICE_TEXT, **BOARD_TAKES}),
        ("sign", "hall", "Portrait of Klhyt", {"text": PORTRAIT_TEXT, "description": "A big grey-bearded man, painted standing on a beach."}),
        ("letter", "study", "Klhyt's last letter", {"text": LETTER_TEXT, "clue": "letter",
                                                    "description": "A folded sheet under the blotter, addressed 'Gog', never sent."}),
        ("letter", "study", "Harbour tally book", {"text": TALLY_TEXT, "clue": "tally", "burnable": True, **BOOK_ROOM,
                                                   "description": "A thin ledger of harbour dues with notes in the margin."}),
        ("thing", "study", "Ship in a bottle", {"portable": True, "description": "A three-master in a green bottle. The name on "
                                                                                 "her bow is too small to read."}),
        ("sign", "stripperwitch", "Price board", {"text": BOARD_STRIPPERWITCH}),
        ("thing", "stripperwitch", "Red booth", {"portable": False, "description": "A curtained booth in red velvet, for people who are not here."}),
        ("thing", "stripperwitch", "Stage", {"portable": False, **WOOD, "description": "A little stage with a velvet curtain. Tonight, a "
                                                                              "fiddler and a lot of feathers."}),
        ("sign", "omberhulk", "Price board", {"text": BOARD_OMBERHULK}),
        ("sign", "ogre", "Price board", {"text": BOARD_OGRE}),
        ("sign", "ogre", "Honeymoon Suite", {"text": SUITE_TEXT, **SUITE_CHALK, "description": "A door with HONEYMOON SUITE chalked on it."}),
        ("thing", "ogre", "Bar top", {"portable": False, **WOOD, "room": 1200, "text": "",
                                      "description": "The Ogre's bar top, a single slab of black wood scarred deep with "
                                                     "initials, hearts, tallies and rude words in four alphabets."}),
        ("dice", "ogre", "Bone dice", {"description": "Three yellowed bone dice in a leather cup.", "dice": "3d6"}),
        ("sign", "unicorn", "Price board", {"text": BOARD_UNICORN}),
        ("sign", "unicorn", "The library", {"text": LIBRARY_TEXT, "description": "Floor-to-ceiling shelves, ladders, and a sign that says QUIET."}),
        ("thing", "market", "Fruit pyramids", {"portable": False, "description": "Mangoes, pineapples and coconuts stacked in "
                                               "pyramids taller than a child. Mother Ines sells them; taking one is stealing."}),
        ("thing", "market", "Brazier", {"portable": False, "fire": True, "description": "Grusha's brazier, goat skewers hissing over the coals."}),
        ("thing", "moonmoth", "Star lanterns", {"portable": False, "description": "Lanterns of elven glass holding a cold, steady "
                                                "light. They do not come off their hooks; the hooks have grown around them."}),
    ] + [("ship", "docks", name, {"description": desc}) for name, desc in SHIPS] + \
        [("crowd", where, name, dict(state)) for where, (name, state) in CROWDS.items()]


def build_things(s):
    P = place_ids(s)
    town = by_name(s)["Klhyts Refuge"]["id"]
    made = set(s.inspect(town)["state"].get("built_things") or [])
    for type_, where, name, state in things():
        if where + "/" + name in made:
            continue
        if not any(c["name"] == name for c in s.inspect(P[where])["contents"]):
            s.spawn(type_, P[where], name, state=dict(state))
        made.add(where + "/" + name)
    s.patch(town, {"built_things": sorted(made)})
    if not any(c["type"] == "lock" for c in s.inspect(P["study"])["contents"]):
        s.spawn("lock", P["study"], "Study lock", state={
            "key": "Study key", "pick_dc": 14, "break_dc": 15,
            "description": "A good brass lock on the study door. The Custodian holds the only key."})
    if not any(c["type"] == "lock" for c in s.inspect(P["warehouse"])["contents"]):
        s.spawn("lock", P["warehouse"], "Warehouse lock", state={
            "key": "Warehouse key", "pick_dc": 15, "break_dc": 16,
            "description": "A heavy Landfall padlock on the warehouse door, stamped BONDED."})


FACTIONS = ["the Guild", "the Fist", "the Refuge", "Vorkathia"]

KNOWS = [("Fat Gog", "Klhyt", 3, "found him on the beach dying of thirst; my friend"),
         ("Fat Gog", "River", 3, "partner; trusts her with his life"), ("River", "Fat Gog", 3, "partner; a sweetheart"),
         ("Dominico", "The Custodian", 1, "pays well, asks for things"), ("The Custodian", "Dominico", 1, "useful, and a brute"),
         ("Brask", "Dominico", 2, "the boss"), ("Tully", "Dominico", 2, "best boss I ever had"),
         ("Fat Gog", "Dominico", -2, "wants my books"), ("Dominico", "Fat Gog", -2, "fat, slow, and in the way"),
         ("Klhyt", "The Custodian", -3, "a thief, and the man who did this"), ("Klhyt", "Fat Gog", 3, "found me on the beach dying of thirst; I owe him my life"),
         ("Harbourmaster Teague", "The Custodian", -1, "signs every tally, and the tallies are short"),
         ("Lieutenant Voss", "Ithriel", 0, "a quarry; not yet found")]

GOALS = {
    "Fat Gog": [("Keep my books out of Dominico's hands", "Midnight, he says; nobody takes what I built"),
                ("Find out what happened to Klhyt", "Klhyt never had business upriver in his life")],
    "River": [("Keep the Stripperwitch standing", "It's Gog's house and it's mine"),
              ("Tell Gog what I saw without starting a war", "A war tonight is one Gog would lose")],
    "Dominico": [("Have Fat Gog's books on my table by midnight", "The Custodian promised me the shadows"),
                 ("Do not answer the voice in the dark", "Parlour conjuring should not answer back")],
    "The Custodian": [("Get the crate onto the Emerald Eye on the one o'clock tide", "Then the mayor is upriver for good"),
                      ("Keep the harbour dues quiet", "Three seasons of it, and nobody counts")],
    "Klhyt": [("Get free before the tide", "Catan is a long way to go in a crate"),
              ("Tell the whole town what the Custodian did", "A refuge that is robbed by its keeper is no refuge")],
    "Lieutenant Voss": [("Find the fugitive elves", "Vorkath's reach is long")],
    "Ithriel": [("Get passage off this coast for my people", "Before the officer finds us")],
}

TIMERS = [(600, "ultimatum"), (1500, "custodian_out"), (3600, "siren_rises"), (3900, "siren_sings"), (5400, "midnight"),
          (7200, "small_hours"), (7800, "siren_leaves"), (9000, "tide")]
STORY_KINDS = ["act", "arrived", "read", "taken", "talked", "shown", "cowed", "agreed", "freed", "pick_failed", "break_failed",
               "lock_broken", "klhyt_returns", "ultimatum", "dominico_back", "custodian_out", "midnight", "small_hours", "tide",
               "siren_rises", "siren_sings", "siren_leaves", "magistrate_sighted", "magistrate_lands", "hearing",
               "given", "died", "lock_picked"]


def templates(P):
    """A new character: a level 1 of its template's class (TEMPLATE_5E), with its kit and the armour it starts in."""
    out = {}
    for key, (scores, skills, hp5, doc, where, purse, kit) in TEMPLATES_STATE.items():
        cls, armours, spells = TEMPLATE_5E[key]
        five = five_block(cls, 1, scores, {"spells": spells})
        five.update(RACE_5E.get(TEMPLATE_PEOPLE[key], {}))
        five.update({"max_hp": five["hp"], "five_e": 1})
        gear = [{"type": "thing", "name": armour_state(k)[0], "state": armour_state(k)[1]} for k in armours]
        out[key] = {"type": "person", "place": P[where], "doc": doc,
                    # `stays`: nothing walks a player's body while they are away (the d20 pack's idle care)
                    "state": {**body(scores, skills, hp5), **five, "description": doc, "post": P[where], "home": P[where],
                              "stays": True,
                              "people": TEMPLATE_PEOPLE[key],
                              "skill_prof": {k: 1 for k, v in (skills or {}).items() if v},  # 5e skills (statblocks)
                              "statblock": people_block(TEMPLATE_PEOPLE[key])},
                    "kit": [{"type": "thing", "name": "Coin", "state": coin(purse)}] +
                           [{"type": "thing", "name": n, "state": dict(st)} for n, st in kit] + gear}
    return out


def build_wiring(s, root):
    P = place_ids(s)
    have = by_name(s)
    rs = s.inspect(root)["state"]
    if not rs.get("policy"):
        s.patch(root, {"policy": POLICY, "ambient": AMBIENT, "coin_kind": "cp", "sweat": False,
                       "thirst_death_days": False})
    if not rs.get("briefing"):
        s.patch(root, {"briefing": BRIEFING})
    # what a guest names the connector in Claude and what they say to play (the invite's steps; the owner's words)
    if rs.get("connector_name") != CONNECTOR_NAME or rs.get("play_name") != PLAY_NAME:
        s.patch(root, {"connector_name": CONNECTOR_NAME, "play_name": PLAY_NAME})
    s.patch(root, {"era": "Before the war", "calendar": "Era of Vorkath (EV); this evening falls before the war, the "
                   "mushroom and the fall of the walls"})
    s.patch(root, {"templates": templates(P)})
    for f in FACTIONS:
        if f not in have:
            s.spawn("faction", root, f)
    book = s.find(type="skillbook", limit=1)
    if book:
        s.patch(book[0]["id"], {"skills": SKILLS_5E})
    have = by_name(s)
    if "Story" not in have:
        s.spawn("story", root, "Story", state={
            "clues": [], **{k: P[k] for k in PLACES}, "packet": have[AT_SEA]["id"],
            "gog": have["Fat Gog"]["id"], "river": have["River"]["id"], "dominico": have["Dominico"]["id"],
            "custodian": have["The Custodian"]["id"], "klhyt": have["Klhyt"]["id"], "brask": have["Brask"]["id"],
            "tully": have["Tully"]["id"], "teague": have["Harbourmaster Teague"]["id"]})
    have = by_name(s)
    st_id = have["Story"]["id"]
    want = {"packet": have[AT_SEA]["id"], "under": have[UNDER]["id"], "siren": have["Ondrine"]["id"],
            "emerald": have["The Emerald Eye"]["id"], "market": P["market"], "moonmoth": P["moonmoth"],
            # Ithriel and her household, whom the story walks to the Moonmoth with whoever asks her about passage
            "ithriel": have["Ithriel"]["id"],
            "household": [have[n]["id"] for n in ["Ithriel"] + [h[0] for h in HOUSEHOLD] if n in have]}
    cur = s.inspect(st_id)["state"]
    missing = {k: v for k, v in want.items() if cur.get(k) != v}
    if missing:
        s.patch(st_id, missing)
    install_rules(s, root)
    install_5e(s, root)
    s.set_rule(root, "story", kinds=STORY_KINDS)
    s.set_rule(root, "finds", kinds=["checked"])
    s.set_rule(root, "bound_guard", kinds=["before_act"])
    s.set_rule(root, "follow_rule", kinds=["following", "stayed"])
    s.set_rule(root, "routine", kinds=["routine_tick"])  # the town's day (scripts/routine.py)
    if not any(t["kind"] == "routine_tick" for t in s.timers()):
        s.schedule(60, "routine_tick", entity=root, every=ROUTINE_EVERY)
    for a, b, standing, note in KNOWS:
        edges = s.recall(about=have[b]["id"], entity=have[a]["id"])["edges"]
        if not any(e["relation"] == "knows" and e["direction"] == "out" for e in edges):
            s.link(have[a]["id"], have[b]["id"], "knows", {"standing": standing, "note": note, "met_t": 0, "count": 0})
    for name, goals in GOALS.items():
        eid = have[name]["id"]
        mine = {g["text"] for g in (s.inspect(eid)["state"].get("goals") or [])}
        for text, why in goals:
            if text not in mine:
                s.intend(text, why=why, entity=eid)
    pending = {t["kind"] for t in s.timers()}
    now = s.summary()["t"]
    for at, kind in TIMERS:
        if kind not in pending and now < START + at and not rs.get("timers_set_" + kind):
            s.schedule(START + at - now, kind, entity=root)
            s.patch(root, {"timers_set_" + kind: True})


# ---- classic statblocks (owner, 2026-11-22: SRD statblocks for the town, LoreKeeper's sheets for Deloris and Kael) --
# The creatures of the System Reference Document 5.1 (Wizards of the Coast, CC BY 4.0), with the numbers the book
# prints: armour class, hit points and hit dice, scores, saves, skills (proficient 1, expertise 2, so the dnd5e pack's
# arithmetic gives the book's bonus), multiattack, traits, actions and reactions. Each body keeps what it carries; its
# attacks are worked from those weapons. Which SRD block each person wears is a host default (notes/bible.md).
BITE = ("Bite", "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.")
PARRY = ("Parry", "Adds 2 to its AC against one melee attack that would hit it. To do so, it must see the attacker and "
                  "be wielding a melee weapon.")
SRD = {
    "commoner": {"cr": 0, "ac": 10, "hp": 4, "dice": "1d8", "die": "1d8", "n": 1,
                 "scores": {"str": 10, "dex": 10, "con": 10, "int": 10, "wis": 10, "cha": 10}},
    "bandit": {"cr": 0.125, "ac": 12, "armor": "leather armor", "hp": 11, "dice": "2d8 + 2", "die": "1d8", "n": 2,
               "scores": {"str": 11, "dex": 12, "con": 12, "int": 10, "wis": 10, "cha": 10}},
    "thug": {"cr": 0.5, "ac": 11, "armor": "leather armor", "hp": 32, "dice": "5d8 + 10", "die": "1d8", "n": 5,
             "scores": {"str": 15, "dex": 11, "con": 14, "int": 10, "wis": 10, "cha": 11}, "skills": {"intimidation": 1},
             "multi": 1, "multiattack": "makes two melee attacks.",
             "traits": [("Pack Tactics", "Advantage on an attack roll against a creature if at least one of its allies is "
                                         "within 5 feet of the creature and the ally isn't incapacitated.")]},
    "spy": {"cr": 1, "ac": 12, "hp": 27, "dice": "6d8", "die": "1d8", "n": 6,
            "scores": {"str": 10, "dex": 15, "con": 10, "int": 12, "wis": 14, "cha": 16},
            "skills": {"deception": 1, "insight": 1, "investigation": 2, "perception": 2, "persuasion": 1, "sleight": 1,
                       "stealth": 1},
            "multi": 1, "multiattack": "makes two melee attacks.", "sneak_attack": "2d6", "cunning": True},
    "bandit captain": {"cr": 2, "ac": 15, "armor": "studded leather", "hp": 65, "dice": "10d8 + 20", "die": "1d8", "n": 10,
                       "scores": {"str": 15, "dex": 16, "con": 14, "int": 14, "wis": 11, "cha": 14},
                       "saves": ["str", "dex", "wis"], "skills": {"athletics": 1, "deception": 1}, "multi": 2,
                       "multiattack": "makes three melee attacks: two with its main weapon and one with a dagger. Or it "
                                      "makes two ranged attacks with its daggers.",
                       "reactions": [PARRY]},
    "veteran": {"cr": 3, "ac": 17, "armor": "splint", "hp": 58, "dice": "9d8 + 18", "die": "1d8", "n": 9,
                "scores": {"str": 16, "dex": 13, "con": 14, "int": 10, "wis": 11, "cha": 10},
                "skills": {"athletics": 1, "perception": 1}, "multi": 1,
                "multiattack": "makes two attacks with its main weapon; with a second blade drawn, it can make one more."},
    "knight": {"cr": 3, "ac": 18, "armor": "plate", "hp": 52, "dice": "8d10 + 8", "die": "1d10", "n": 8,
               "scores": {"str": 16, "dex": 11, "con": 14, "int": 11, "wis": 11, "cha": 15}, "saves": ["con", "wis"],
               "multi": 1, "multiattack": "makes two melee attacks.",
               "traits": [("Brave", "Advantage on saving throws against being frightened.")],
               "actions": [("Leadership (Recharges after a Short or Long Rest)",
                            "For 1 minute, whenever a creature it can see within 30 feet that is not hostile to it makes an "
                            "attack roll or a saving throw, that creature can add a d4 to the roll, provided it can hear and "
                            "understand the knight. One Leadership die at a time; it ends if the knight is incapacitated.")],
               "reactions": [PARRY]},
    "noble": {"cr": 0.125, "ac": 15, "armor": "breastplate", "hp": 9, "dice": "2d8", "die": "1d8", "n": 2,
              "scores": {"str": 11, "dex": 12, "con": 11, "int": 12, "wis": 14, "cha": 16},
              "skills": {"deception": 1, "insight": 1, "persuasion": 1}, "reactions": [PARRY]},
    "lizardfolk": {"cr": 0.5, "ac": 15, "armor": "natural armor, shield", "hp": 22, "dice": "4d8 + 4", "die": "1d8", "n": 4,
                   "scores": {"str": 15, "dex": 10, "con": 13, "int": 7, "wis": 12, "cha": 7},
                   "skills": {"perception": 1, "stealth": 2, "survival": 2}, "speed": "30 ft., swim 30 ft.",
                   "languages": ["Draconic"], "multi": 1,
                   "multiattack": "makes two melee attacks, each one with a different weapon (a bite among them).",
                   "traits": [("Hold Breath", "Can hold its breath for 15 minutes.")], "actions": [BITE]},
    "scout": {"cr": 0.5, "ac": 13, "armor": "leather armor", "hp": 16, "dice": "3d8 + 3", "die": "1d8", "n": 3,
              "scores": {"str": 11, "dex": 14, "con": 12, "int": 11, "wis": 13, "cha": 11},
              "skills": {"nature": 2, "perception": 2, "stealth": 2, "survival": 2}, "multi": 1,
              "multiattack": "makes two melee attacks or two ranged attacks.",
              "traits": [("Keen Hearing and Sight", "Advantage on Wisdom (Perception) checks that rely on hearing or sight.")]},
    "acolyte": {"cr": 0.25, "ac": 10, "hp": 9, "dice": "2d8", "die": "1d8", "n": 2,
                "scores": {"str": 10, "dex": 10, "con": 10, "int": 10, "wis": 14, "cha": 11},
                "skills": {"medicine": 1, "religion": 1}, "cast": "wis", "spells": ["sacred flame", "bless", "cure wounds"],
                "slots": {"1": 3}},
    "druid": {"cr": 2, "ac": 11, "armor": "16 with barkskin", "hp": 27, "dice": "5d8 + 5", "die": "1d8", "n": 5,
              "scores": {"str": 10, "dex": 12, "con": 13, "int": 12, "wis": 15, "cha": 11},
              "skills": {"medicine": 1, "nature": 1, "perception": 1}, "languages": ["Druidic"], "cast": "wis",
              "slots": {"1": 4, "2": 3}},
    # the Custodian's town watch (2026-11-23)
    "guard": {"cr": 0.125, "ac": 16, "armor": "chain shirt, shield", "hp": 11, "dice": "2d8 + 2", "die": "1d8", "n": 2,
              "scores": {"str": 13, "dex": 12, "con": 12, "int": 10, "wis": 11, "cha": 10}, "skills": {"perception": 1}},
}
SRD_OF = {
    "Fat Gog": ("bandit captain", {"traits": [("Hold Breath", "Can hold his breath for 15 minutes; Lizardfolk are at home "
                                                              "in the water.")],
                                   "speed": "30 ft., swim 30 ft.", "languages": ["Common", "Draconic"], "actions": [BITE]}),
    "River": ("spy", {}), "Hanklevode": ("spy", {}),
    "Dominico": ("veteran", {"cast": "int", "spells": ["fire bolt", "shield", "magic missile"], "slots": {"1": 3},
                             "traits": [("Parlour Conjuring", "Dabbles in the magic arts: a few spells off his own wits, "
                                                              "and something in the dark has started to answer.")]}),
    "The Custodian": ("noble", {}), "Master Quillon": ("noble", {}), "Phillip Everuex": ("noble", {}),
    "Klhyt": ("veteran", {}), "Captain Aelith": ("veteran", {}),
    "Brask": ("thug", {}), "Tully": ("thug", {}), "Big Ludo": ("thug", {}), "Bosun Maggs": ("thug", {}),
    "Hulda Ironwake": ("thug", {}), "Ruk Halfhand": ("thug", {}),
    "Captain Eirik": ("bandit captain", {}), "Captain Danny DeVito": ("bandit captain", {}),
    "Lieutenant Voss": ("knight", {}), "Ssark": ("lizardfolk", {}), "Thoradin": ("scout", {}),
    "Sister Agathe": ("acolyte", {}),
    "Saelwyn": ("druid", {"spells": ["thorn whip", "produce flame", "entangle", "thunderwave", "cure wounds", "healing word"]}),
    "Harbourmaster Teague": ("commoner", {}), "Husok Sourfist": ("commoner", {}), "Wendeline Moss": ("commoner", {}),
    "Mother Ines": ("commoner", {}), "Hallvard Saltbeard": ("commoner", {}), "Grusha": ("commoner", {}),
    **{n: ("commoner", {}) for n, _, _ in HOUSEHOLD}, **{n: ("bandit", {}) for n, _, _ in SAILORS},
}
# LoreKeeper's character sheets (D&D 5e 2014), the canon for these two: proficiencies, speed and, for Kael, the glaive
CANON_SHEETS = {
    "Deloris": {"skill_prof": {"acrobatics": 1, "sleight": 1, "stealth": 1, "deception": 1, "insight": 1, "perception": 1},
                "statblock": {"size": "Medium", "kind": "humanoid (human)", "speed": "30 ft.", "languages": ["Common"],
                              "traits": [("Tools", "Thieves' tools, navigator's tools.")]}},
    "Kael Ironjaw": {"skill_prof": {"athletics": 1, "intimidation": 1, "survival": 1},
                     "statblock": {"size": "Medium", "kind": "humanoid (Jonulvicha)", "speed": "30 ft.",
                                   "languages": ["Common", "Orc"]}},
}
PEOPLE_SENSES = {"elf": ["darkvision 60 ft."], "jonulvicha": ["darkvision 60 ft."], "dwarf": ["darkvision 60 ft."]}
PEOPLE_TONGUE = {"elf": "Elvish", "jonulvicha": "Orc", "dwarf": "Dwarvish", "lizardfolk": "Draconic", "xoton": "Xoton"}
CLASS_KEYS = ["cls", "level", "sneak_attack", "cunning", "spellcasting", "extra_attacks", "unarmored", "martial_arts"]


def rows(pairs):
    return [{"name": a, "text": b} for a, b in pairs]


def people_block(people):
    """What a statblock says of anyone of these people: medium, humanoid, their senses and tongue beside Common."""
    tongue = PEOPLE_TONGUE.get(people)
    return {"size": "Medium", "kind": "humanoid (" + (people or "human") + ")", "speed": "30 ft.",
            "senses": PEOPLE_SENSES.get(people, []), "languages": ["Common"] + ([tongue] if tongue else [])}


def srd_state(name, kind, over, st):
    """A body's state from its SRD block, its people and what the town adds; hp keep their share of the new whole."""
    b = dict(SRD[kind])
    b.update({k: v for k, v in over.items() if k not in ("traits",)})
    people = st.get("people") or "human"
    langs = list(b.get("languages") or ["Common"])
    if "Common" not in langs:
        langs.insert(0, "Common")
    tongue = PEOPLE_TONGUE.get(people)
    if tongue and tongue not in langs:
        langs.append(tongue)
    block = {"size": "Medium", "kind": "humanoid (" + people + ")", "speed": b.get("speed") or "30 ft.",
             "hit_dice": b["dice"], "armor": b.get("armor"), "senses": PEOPLE_SENSES.get(people, []), "languages": langs,
             "traits": rows(list(SRD[kind].get("traits") or []) + list(over.get("traits") or [])),
             "actions": rows(b.get("actions") or []), "reactions": rows(b.get("reactions") or []),
             "multiattack": (name + " " + b["multiattack"]) if b.get("multiattack") else None, "srd": kind}
    old_hp = int(st.get("hp") if st.get("hp") is not None else b["hp"])
    old_max = int(st.get("max_hp") or old_hp or 1)
    hp = b["hp"] if old_hp >= old_max else (0 if old_hp <= 0 else max(1, round(old_hp * b["hp"] / old_max)))
    out = {k: None for k in CLASS_KEYS}
    out.update({"srd": kind, "cr": b["cr"], "ac": b["ac"], "hp": hp, "max_hp": b["hp"], "hit_die": b["die"],
                "hit_dice": b["n"], "hit_dice_max": b["n"], "scores": dict(b["scores"]), "saves": list(b.get("saves") or []),
                "skill_prof": dict(b.get("skills") or {}), "weapon_prof": ["all"], "statblock": block, "five_e": 1})
    if b.get("multi"):
        out["extra_attacks"] = b["multi"]
    if b.get("sneak_attack"):
        out["sneak_attack"] = b["sneak_attack"]
    if b.get("cunning"):
        out["cunning"] = True
    if b.get("cast"):
        slots = dict(b.get("slots") or {})
        out["spellcasting"] = {"ability": b["cast"], "spells": list(b.get("spells") or []), "slots": slots,
                               "slots_max": dict(slots), "pact": False}
    return out


def build_statblocks(s):
    """Classic statblocks onto the town (owner, 2026-11-22). The named and the minor wear their SRD block once, or again
    when SRD_OF gives them another; Deloris and Kael get their LoreKeeper sheets' proficiencies; every other 5e body
    (a player's, a template's, a class-levelled one) gets 5e skills from its sheet: a rank is a proficiency."""
    w = s.world
    for e in w.find(limit=None):
        st = e["state"]
        if st.get("dead") or not w.is_a(e["type"], "combatant"):
            continue
        name = e["name"]
        if name in SRD_OF and not w.embodied(e["id"]):
            kind, over = SRD_OF[name]
            if st.get("srd") != kind:
                s.patch(e["id"], srd_state(name, kind, over, st))
            continue
        if name in CANON_SHEETS:
            c = CANON_SHEETS[name]
            want = {"skill_prof": c["skill_prof"],
                    "statblock": {**c["statblock"], "traits": rows(c["statblock"].get("traits") or []),
                                  "senses": PEOPLE_SENSES.get(st.get("people"), [])}}
            if st.get("skill_prof") != want["skill_prof"] or (st.get("statblock") or {}).get("kind") != want["statblock"]["kind"]:
                s.patch(e["id"], want)
            continue
        if st.get("five_e") and st.get("skill_prof") is None:
            ranks = ((st.get("sheet") or {}).get("skills") or {})
            s.patch(e["id"], {"skill_prof": {k: 1 for k, v in ranks.items() if int(v or 0) > 0}})
        if st.get("five_e") and not st.get("statblock"):
            s.patch(e["id"], {"statblock": people_block(st.get("people"))})


# ---- the cast (owner, 2026-11-23: "Give them routines, jobs, their own money, their plans or schemes", and "the
# narrator tells the users too much. Often should describe what people look like rather then outright just say who they
# are"). Each person's look (no name, no title), the phrase a stranger would point them out by, a brief for an agent,
# a scheme, a purse, a table of lines with several of their own for when nothing fits, a day (scripts/routine.py walks
# it) and the small things they are seen doing. The files are cast/*.py; NEW there are people new to the town (the
# Custodian's watch, Dominico's collector and two thugs, Gog's door, eyes and fence, a lamplighter, two more Xotons).

CAST_DIR = _Path(__file__).with_name("cast")


def load_cast():
    """CAST and NEW from every cast/*.py, in name order. A later file may give part of someone an earlier one wrote
    (cast/d_vorkath.py: the Custodian found out): its keys replace theirs, and its dialog topics join theirs (None
    retires one)."""
    cast, new = {}, {}
    global MAGISTRATE_DATA
    for f in sorted(CAST_DIR.glob("*.py")):
        spec = _ilu.spec_from_file_location("klhyts_refuge_cast_" + f.stem, f)
        mod = _ilu.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for name, entry in getattr(mod, "CAST", {}).items():
            if name not in cast:
                cast[name] = dict(entry)
                continue
            merged = dict(cast[name])
            for k, v in entry.items():
                if k == "dialog":
                    d = dict(merged.get("dialog") or {})
                    d.update(v)
                    merged["dialog"] = {dk: dv for dk, dv in d.items() if dv is not None}
                elif k == "brief_more":  # a paragraph added to the brief an earlier file wrote
                    merged["brief"] = (str(merged.get("brief") or "") + " " + v).strip()
                elif k == "dialog_when":  # [{if_state, words, line}]: each topic naming one of the words says `line`
                    d = dict(merged.get("dialog") or {})  # while the flag holds, and what it said before otherwise
                    for rule in v:
                        for dk in list(d):
                            if set(dk.split("|")) & set(rule["words"]):
                                d[dk] = {"line": rule["line"], "if_state": rule["if_state"], "else": d[dk]}
                    merged["dialog"] = d
                else:
                    merged[k] = v
            cast[name] = merged
        new.update(getattr(mod, "NEW", {}))
        # the special names count only in their own shape: a cast file may name a topic key MAGISTRATE or PERIL
        part = lambda name, kind: getattr(mod, name, None) if isinstance(getattr(mod, name, None), kind) else None
        PERIL_DATA.update(part("PERIL", dict) or {})
        MISSIONS_DATA.extend(part("MISSIONS", list) or [])
        WORK_VOICES.update(part("WORK_VOICES", dict) or {})
        if part("MAGISTRATE", dict):
            MAGISTRATE_DATA = mod.MAGISTRATE
        FAITH_TEXTS.update(part("FAITH_TEXTS", dict) or {})
    return cast, new


MAGISTRATE_DATA = None
FAITH_TEXTS = {}  # cast/e_faith.py: the missions' tract, and its line in the Unicorn's library
PERIL_DATA = {}  # cast/f_peril.py: who fights to kill, and the orders the villains hold (build_peril)
MISSIONS_DATA = []  # cast/g_gog.py, cast/l_missions.py: the town's work, as jobs its givers carry (build_missions)
WORK_VOICES = {}  # cast/l_missions.py: how each giver offers and pays, in their own voice


CAST, NEW_PEOPLE = load_cast()
SRD_OF.update({n: (v.get("srd") or "commoner", {}) for n, v in NEW_PEOPLE.items() if n not in SRD_OF})
for _n, _v in NEW_PEOPLE.items():
    PEOPLE_OF.setdefault(_n, _v.get("people", "human"))

# what players never read on a person (their `secret`): the lines not said yet, the day ahead, the plans
CAST_SECRET = ["dialog", "default_line", "routine", "routine_when", "routine_disgraced", "routine_upheld", "routine_if",
               "scheme", "beats", "look_free", "look_disgraced", "look_upheld", "orders", "finishes", "silenced"]
# what the plot adds to the cast files: whose day waits for which fact, the story's or their own (scripts/routine.py),
# and what they are doing while it waits (the cast files carry the looks and day the plot turns to: look_free,
# look_disgraced, routine_disgraced)
CAST_EXTRA = {
    "Klhyt": {"routine_when": ["klhyt_freed"]},
    "Brask": {"routine_when": ["klhyt_freed", "dominico_backed", "shipped", "off_post"],
              "waiting": "He sits on a bollard by the warehouse door, cudgel across his knees, and never looks away "
                         "from that door for long.",
              # his leaving lines, as the pier sees them (the live world kept the old, named ones)
              "bribe_line": BRASK["bribe_line"], "marker_line": BRASK["marker_line"], "cowed_line": BRASK["cowed_line"]},
}
ROUTINE_EVERY = 300  # world seconds between ticks of the town's day


def routine_ids(slots, P, have):
    """A day's slots with place keys and payees' names turned to ids, in hour order."""
    out = []
    for sl in slots or []:
        d = dict(sl)
        d["at"] = float(d["at"])
        d["place"] = P[d["place"]]
        if d.get("pay"):
            pay = dict(d["pay"])
            to = have.get(pay.get("to"))
            if to is None:
                d.pop("pay")
            else:
                pay["to"] = to["id"]
                d["pay"] = pay
        out.append(d)
    return sorted(out, key=lambda d: d["at"])


def slot_now(routine, t):
    h = (t % 86400) / 3600.0
    cur = routine[-1] if routine else None
    for sl in routine:
        if sl["at"] <= h:
            cur = sl
    return cur


def spawn_new(s):
    """The people new to the town, once ever (the town keeps the list, so one play killed stays dead)."""
    have = by_name(s)
    P = place_ids(s)
    town = have["Klhyts Refuge"]["id"]
    made = set(s.inspect(town)["state"].get("built_people") or [])
    for name, n in NEW_PEOPLE.items():
        if name in have or name in made:
            continue
        home = P[n.get("home") or "lanes"]
        st = {**body(n["scores"], n.get("skills"), hp(n.get("hp") or 10)), "faction": n.get("faction"),
              "people": n.get("people", "human"), "post": home, "home": home}
        pid = s.spawn(n.get("type") or "person", home, name, state=st)["id"]
        s.spawn("thing", pid, "Coin", state=coin(int((CAST.get(name) or {}).get("purse") or 20)))
        for cname, wkey, desc in n.get("carries") or []:
            s.spawn("thing", pid, cname, state=arm(wkey, desc) if wkey else {"portable": True, "bulk": 0, "description": desc})
        made.add(name)
    s.patch(town, {"built_people": sorted(made)})


def original_purse(name):
    for _, _, n, _, carries in people():
        if n == name:
            for _, cname, cst in carries:
                if cname == "Coin":
                    return int(cst.get("count") or 0)
    return None


def set_purse(s, pid, name, purse):
    """A purse sized to the person's life, keeping what play has put in it since (a tip, a sale)."""
    coins = [c for c in s.world.children(pid) if c["name"] == "Coin"]
    if not coins or purse is None:
        return
    now = int(coins[0]["state"].get("count") or 0)
    was = original_purse(name)
    gained = max(0, now - was) if was is not None else 0
    if now != int(purse) + gained:
        s.patch(coins[0]["id"], {"count": int(purse) + gained})


def build_cast(s, root):
    spawn_new(s)
    P = place_ids(s)
    have = by_name(s)
    w = s.world
    now = s.summary()["t"]
    facts = s.inspect(have["Story"]["id"])["state"] if "Story" in have else {}
    for name, c in CAST.items():
        e = have.get(name)
        if e is None:
            continue
        st = e["state"]
        held = w.embodied(e["id"]) is not None
        want = {"look": c["look"], "seen_as": c.get("seen_as"), "brief": c.get("brief"), "scheme": c.get("scheme"),
                "default_line": list(c.get("default_line") or []), "beats": list(c.get("beats") or []),
                "routine": routine_ids(c.get("routine"), P, have)}
        for k in ("look_free", "look_disgraced", "look_upheld"):
            if c.get(k):
                want[k] = c[k]
        if c.get("routine_disgraced"):
            want["routine_disgraced"] = routine_ids(c["routine_disgraced"], P, have)
        if c.get("routine_upheld"):
            want["routine_upheld"] = routine_ids(c["routine_upheld"], P, have)
        if c.get("routine_if"):  # {flag: slots}: the day the news brings (scripts/routine.py)
            want["routine_if"] = [[flag, routine_ids(slots, P, have)] for flag, slots in c["routine_if"].items()]
        extra = dict(CAST_EXTRA.get(name, {}))
        waiting_text = extra.pop("waiting", None) or c.get("waiting") or ""
        want.update(extra)
        if st.get("disgraced") and want.get("look_disgraced"):  # what the story has made of them stays
            want["look"] = want["look_disgraced"]
            want["routine"] = want.get("routine_disgraced") or want["routine"]
        if st.get("upheld") and want.get("look_upheld"):
            want["look"] = want["look_upheld"]
            want["routine"] = want.get("routine_upheld") or want["routine"]
        if st.get("in_irons"):  # removed by the magistrate: his look and his day are the story's now
            want.pop("look", None)
            want.pop("routine", None)
        if st.get("bound") is False and want.get("look_free"):
            want["look"] = want["look_free"]
        changes = {k: v for k, v in want.items() if st.get(k) != v}
        secret = sorted(set(st.get("secret") or []) | set(CAST_SECRET))
        if st.get("secret") != secret:
            changes["secret"] = secret
        if not st.get("cast_v"):  # the first time: their purse, and their look in place of the old who-and-what
            set_purse(s, e["id"], name, c.get("purse"))
            changes["cast_v"] = 1
        if "look" in changes or "routine" in changes:
            changes["routine_key"] = None  # the next tick sets their day afresh
            when = want.get("routine_when")
            waiting = bool(when) and not any(facts.get(k) or st.get(k) for k in when)  # tied, or on the door
            if not held:
                slot = None if waiting else slot_now(want["routine"], now)
                doing = slot["doing"] if slot else waiting_text
                changes["description"] = (want["look"] + " " + doing).strip()
        if st.get("dialog") != c.get("dialog"):
            s.patch(e["id"], {"dialog": None})  # whole: a merge would keep a retired topic or a stale branch
            changes["dialog"] = c.get("dialog") or {}
        if changes:
            s.patch(e["id"], changes)
    # the cove: River and her quartermaster know the way; the shore path off the docks is there for a sharp eye
    cove = have.get(PLACES["cove"][0])
    if cove:
        knows = list(cove["state"].get("known_to") or [])
        for who in ("River", "Ned Tallow"):
            if who in have and have[who]["id"] not in knows:
                knows.append(have[who]["id"])
        if knows != list(cove["state"].get("known_to") or []):
            s.patch(cove["id"], {"known_to": knows})
        docks = have[PLACES["docks"][0]]
        key = "survival|nature|navigation|tracking"
        path = {"dc": 15, "reveals": cove["id"],
                "line": "Below the end of the pier, where the planks give out, a path goes down the rocks and away south "
                        "along the shore toward the reef the charts call DO NOT. It has been walked lately, at night, by "
                        "someone who knew where to put their feet.",
                "fail": "Rocks, weed and the sea. If anyone goes that way, they do it in the dark."}
        if (docks["state"].get("finds") or {}).get(key) != path:
            s.patch(docks["id"], {"finds": {key: path}})
        if "The Quicksilver" not in have:
            s.spawn("thing", cove["id"], "The Quicksilver", state={
                "description": "A long, low schooner with a black hull and a silver name, built for speed and for not being "
                               "seen: raked masts, sails furled tight, gunports painted shut so well you would not know "
                               "they were there. A hooded lantern burns at the stern."})


TRACT = "The Eight Arms and Their Saints"


def build_faith(s):
    """The faith in the town's hands (owner, 2026-11-23: "We need a whole thing about that too"): the missions' tract on
    the Town Hall table and in the officer's coat, and its title on the Unicorn's shelves. Once each, by name."""
    text = FAITH_TEXTS.get("catechism")
    if not text:
        return
    have = by_name(s)
    w = s.world
    tract = {"portable": True, "bulk": 0, "text": text,
             "description": "A thin printed tract on cheap paper, an octogram stamped on the cover: one of the missions'."}
    holders = [have.get(PLACES["hall"][0]), have.get("Lieutenant Voss")]
    for h in holders:
        if h and not any(c["name"] == TRACT for c in w.children(h["id"])):
            s.spawn("letter", h["id"], TRACT, state=dict(tract))
    lib = have.get("The library")
    line = FAITH_TEXTS.get("library")
    if lib and line and line not in (lib["state"].get("text") or ""):
        s.patch(lib["id"], {"text": (lib["state"].get("text") or "").rstrip() + " " + line})


def build_news(s):
    """The night's news on the people of a world built before the flags (a live world mid-story): each fact the story
    has set reaches those it would have reached (scripts/story.py tell_town), once."""
    have = by_name(s)
    st = s.inspect(have["Story"]["id"])["state"] if "Story" in have else {}
    w = s.world
    folk = [e for e in w.find(limit=None) if w.is_a(e["type"], "person")]
    for fact, flag in (("custodian_exposed", "klhyt_home"), ("guild_hit", "guild_hit"), ("shipped", "klhyt_shipped")):
        if st.get(fact):
            for e in folk:
                if not e["state"].get(flag):
                    s.patch(e["id"], {flag: True})
    for fact, who, flag in (("gog_knows", "Fat Gog", "gog_knows"), ("dominico_backed", "Dominico", "backed_off")):
        if st.get(fact) and who in have and not have[who]["state"].get(flag):
            s.patch(have[who]["id"], {flag: True})
    if st.get("custodian_exposed") and "The Custodian" in have:
        c = by_name(s)["The Custodian"]
        cs = c["state"]
        want = {"disgraced": True}
        if cs.get("look_disgraced") and cs.get("look") != cs["look_disgraced"]:
            want.update({"look": cs["look_disgraced"], "description": cs["look_disgraced"]})
        if cs.get("routine_disgraced") and cs.get("routine") != cs["routine_disgraced"]:
            want.update({"routine": cs["routine_disgraced"], "routine_key": None})
        if any(cs.get(k) != v for k, v in want.items()):
            s.patch(c["id"], want)
    k = by_name(s).get("Klhyt")
    if k and k["state"].get("bound") is False and k["state"].get("look_free") and k["state"].get("look") != k["state"]["look_free"]:
        s.patch(k["id"], {"look": k["state"]["look_free"], "description": k["state"]["look_free"], "routine_key": None})
    br = by_name(s).get("Brask")
    if br and br["state"].get("left_post") and not br["state"].get("off_post"):
        s.patch(br["id"], {"off_post": True})
    if st.get("shipped") and k and not k["state"].get("routine_off"):
        s.patch(k["id"], {"routine_off": True})
    moon = place_ids(s).get("moonmoth")
    elves = [h[0] for h in HOUSEHOLD] + ["Ithriel"]
    for e in folk:
        if e["name"] in elves and parent_of(s, e["id"]) == moon and not e["state"].get("aboard"):
            s.patch(e["id"], {"aboard": True, "routine_off": True})


# ---- the magistrate (owner, 2026-11-23: "A magistrate is due to arrive. They would have been at sea months. So who
# knows who they will decide on. Vorkathians aren't known for their tolerance"; how long: "The next week (5-9 days)").
# The day is drawn once, from the world's seed, and kept on the Story (`magistrate_eta`): a sail at the harbour mouth
# two hours before, the landing at nine in the morning. Which Arm of Vorkath the magistrate serves is drawn when they
# land (scripts/story.py), from MAGISTRATE_ARMS.

MAGISTRATE_DAYS = (5, 9)
MAGISTRATE_HOUR = 9.0
MAGISTRATE_KINDS = ["magistrate_sighted", "magistrate_lands", "hearing"]


MAGISTRATE_SCORES = {"str": 10, "dex": 11, "con": 12, "int": 15, "wis": 15, "cha": 14}
GUARD_SCORES = {"str": 13, "dex": 12, "con": 12, "int": 10, "wis": 11, "cha": 10}


def magistrate_spec(s):
    """The magistrate as scripts/story.py spawns them: each Arm's whole person (look, lines, day, 5e numbers), the
    guards and the ship, with places as ids. Kept on the Story, so a change here reaches a live world."""
    M = MAGISTRATE_DATA
    if not M:
        return None
    P = place_ids(s)
    have = by_name(s)
    secret = sorted(CAST_SECRET + ["arm"])

    def person(name, kind, look, scores, skills, extra):
        st = {**body(scores, skills, hp(SRD[kind]["hp"])), **srd_state(name, kind, {}, {"people": "human"}),
              "people": "human", "faction": "Vorkathia", "look": look, "description": look, "secret": secret}
        st.update(extra)
        return st

    arms = {}
    for key, a in M["arms"].items():
        day = routine_ids(sorted([sl for sl in M_DAY(M) if sl["at"] != a["visit"]["at"]] + [a["visit"]],
                                 key=lambda d: d["at"]), P, have)
        state = person(a["name"], a["srd"], a["state"]["look"], MAGISTRATE_SCORES,
                       {"insight": 2, "persuasion": 2, "religion": 2}, dict(a["state"]))
        state["routine"] = day
        arms[key] = {k: v for k, v in a.items() if k not in ("state", "visit", "srd")}
        arms[key]["state"] = state
    guards = []
    for g in M["guards"]:
        st = person(g["name"], g["srd"], g["look"], GUARD_SCORES, {"perception": 1},
                    {"seen_as": g["seen_as"], "dialog": g["dialog"], "default_line": g["default_line"],
                     "routine": routine_ids(M_GUARD_DAY(M), P, have)})
        guards.append({"name": g["name"], "state": st})
    return {"ship": M["ship"], "landing": M["landing"], "custodian_gold": M["custodian_gold"], "guards": guards,
            "arms": arms, "arm_order": list(M["arm_order"]),
            "base": {"faction": "Vorkathia", "people": "human"}}


def M_DAY(M):
    return [dict(sl) for sl in M.get("day") or []]


def M_GUARD_DAY(M):
    return [dict(sl) for sl in M.get("guard_day") or []]


def build_magistrate(s, root):
    have = by_name(s)
    if "Story" not in have:
        return
    sid = have["Story"]["id"]
    st = s.inspect(sid)["state"]
    spec = magistrate_spec(s)
    if st.get("magistrate_spec") != spec:
        s.patch(sid, {"magistrate_spec": None})
        s.patch(sid, {"magistrate_spec": spec})
    if st.get("magistrate_eta") is not None:
        return
    now = s.summary()["t"]
    days = _random.Random(str(WORLD["seed"]) + "-magistrate").randint(*MAGISTRATE_DAYS)
    eta = (int(now // 86400) + days) * 86400 + MAGISTRATE_HOUR * 3600
    s.schedule(eta - 7200 - now, "magistrate_sighted", entity=root)
    s.schedule(eta - now, "magistrate_lands", entity=root)
    s.patch(sid, {"magistrate_eta": eta, "magistrate_day": int(eta // 86400)})


# ---- hired help: the one way a player brings a second agent in (owner, 2026-11-22) ---------------------------------
# Each names their own price (scripts/_hired.py has the shape): coin by the day, from a few silver to a fortune, a
# thing they want, or a favour the narrator marks done with `favoured: {<the hirer's id>: true}` on them. The hire
# offers the hirer their seat; claim_seat gives a sub-agent. Nobody else in the Refuge can be had that way.
HIRELINGS = {
    "Tully": {"wage": 20, "max_days": 3, "line": "Cash, and Dominico never hears about it.",
              "ask": "Two silver a day. Cash. And Dominico doesn't hear about it, or we're both in the harbour."},
    "Kael Ironjaw": {"wage": 50, "max_days": 7, "line": "Point me at something.",
                     "ask": "Five silver a day and I hit whatever you point at. Cheap, for what you get."},
    "Hanklevode": {"wage": 200, "max_days": 7, "line": "Doors, then. Quietly.",
                   "ask": "Two gold a day. I open doors quietly. I don't do blood, and I don't do Dominico."},
    # hard to win (owner, 2026-11-22): a favour, then a fortune; and she joins as herself, her seat staying Ed's
    "Deloris": {"favour": "end Phillip Everuex's hunt for her", "wage": 2500, "max_days": 3, "seat": False,
                "line": "Three days. Then I'm gone, and you never saw me.",
                "ask": "Twenty-five gold a day, and that is the easy part. A man named Everuex is hunting me. End the "
                       "hunt, then come back with the gold."},
    "Thoradin": {"favour": "find him the druid he is looking for", "days": 3, "max_days": 3,
                 "line": "Three days, then. I keep my word better than most keep their purse.",
                 "ask": "Coin? No. Find me my druid, and I'll walk with you three days."},
    "Ssark": {"wants": "Tot of rum", "days": 1, "max_days": 2, "line": "Poured for me first. Good. One day.",
              "ask": "Coin is for people with pockets. Buy me a rum, poured for me first, and I walk with you a day."},
}
HIRE_SLOTS = 6  # the engine's cap on seats one grant claims; the hire's own (1 + Charisma, from 5e's 20) bites first


def build_hire(s, root):
    have = by_name(s)
    for name, offer in HIRELINGS.items():  # the terms are the owner's: a changed line here reaches the live world
        p = have.get(name)
        seat = offer.get("seat", True) is not False
        if p is not None and (p["state"].get("for_hire") != offer or bool(p["state"].get("seatable")) != seat):
            s.patch(p["id"], {"for_hire": offer, "seatable": seat})
    rs = s.inspect(root)["state"]
    if rs.get("seat_slots") is None:
        s.patch(root, {"seat_slots": HIRE_SLOTS})
    briefing = str(rs.get("briefing") or "")
    for mark, text in BRIEF_ADDENDA:  # added to what the root says, so an edit there stays
        if mark not in briefing:
            briefing = (briefing + " " if briefing else "") + text
    if briefing != str(rs.get("briefing") or ""):
        s.patch(root, {"briefing": briefing})
    s.set_rule(root, "hire_rule", kinds=["hire_ends", "killed"])


def mend_stale(s):
    """Fixes for a world built from an earlier draft of this file: each checks first."""
    have = by_name(s)
    nc = have.get("Newcomer")
    if nc and nc["state"].get("max_hp") == 6 and nc["state"].get("hp") == 6:
        s.patch(nc["id"], {"hp": 10, "max_hp": 10})
    br = have.get("Brask")
    if br and not br["state"].get("leaves_behind"):
        s.patch(br["id"], {"leaves_behind": "Warehouse key"})
    if br and not br["state"].get("walks_to"):
        s.patch(br["id"], {"walks_to": place_ids(s)["ogre"]})
    tg = have.get("Harbourmaster Teague")
    if tg and str(tg["state"].get("default_line", "")).startswith("Teague taps his tally board."):
        s.patch(tg["id"], {"default_line": TEAGUE["default_line"]})
    # Kael back to the Ogre and Deloris to the Stripperwitch, neither a seat players pick (owner, 2026-11-22, after
    # an earlier word had put every seat at the docks). One nobody holds, standing where an older build put them,
    # goes; one play has moved elsewhere stays where play has them.
    P = place_ids(s)
    for name, olds, new, now in (("Kael Ironjaw", ("docks",), "ogre", KAEL),
                                 ("Deloris", ("docks", "unicorn"), "stripperwitch", DELORIS)):
        p = have.get(name)
        if p is None:
            continue
        st = p["state"]
        if st.get("playable") or st.get("brief") != now["brief"] or st.get("dialog") != now["dialog"]:
            dialog = {k: None for k in (st.get("dialog") or {}) if k not in now["dialog"]}  # a retired topic goes
            dialog.update(now["dialog"])
            s.patch(p["id"], {"playable": False, "brief": now["brief"], "dialog": dialog})
        if s.world.embodied(p["id"]) is None and parent_of(s, p["id"]) in [P[k] for k in olds]:
            s.move(p["id"], P[new])
            s.patch(p["id"], {"post": P[new], "home": P[new]})


def parent_of(s, eid):
    p = s.inspect(eid)["parent"]
    return p.get("id") if isinstance(p, dict) else p


# ---- a glance, said aloud (owner, 2026-11-23: a player on a voice client could not take in the docks, 68,000 characters
# of scene; "it needs to be enough that could be spoken to and listened to. LLMs over slop things, we want to reduce it
# for human interactivity"). perceive is short here by default (the engine's `perceive_brief`): each place by its
# `short` line, each person by their `seen_as`. The long descriptions stay for inspect, when someone looks closer.
PLACE_SHORT = {
    "docks": "Lamplit piers, ships rafted three deep, a pale ship glowing at the far end and a warehouse at the pier's end.",
    "warehouse": "A long dark shed of bales and crates, smelling of tar and old fish.",
    "harbour": "The waterfront street: shuttered chandlers, swaying tavern lanterns, and the hill up to the square.",
    "turtle": "A sailors' pub drowned in nets and floats, where the beers come twice the size.",
    "apothecary": "The town's one grand house: dark wood, white linen, and a steward who looks through you.",
    "square": "Sheeted stalls, a town pump, the Town Hall's white porch and a notice board.",
    "hall": "Colonial timber going grey, an office to one side and a locked door at the back.",
    "study": "A small room of charts and pipe smoke, searched and put back very carefully.",
    "stripperwitch": "Red velvet, good music, a curtained stage and a long mirror behind the bar.",
    "omberhulk": "Loud, hot and buggy, with big portions and music that runs late.",
    "ogre": "Sawdust, spit, a bar made of a ship's door and a dice game in the corner.",
    "treeline": "A dark road at the edge of town, with eyes watching from the trees.",
    "unicorn": "A quiet library of a tavern, for people who don't want to be found.",
    "market": "Lantern-strung stalls, brazier smoke and a crowd you move through sideways.",
    "moonmoth": "A grown ship of pale silverwood that hums underfoot, elves waiting among their bundles.",
    "lanes": "Narrow lanes of timber houses, washing overhead and a goat in every third yard.",
    "cove": "A hidden cove of black shingle, where a long black schooner rides at anchor.",
    "gate": "Two open timber gates, and the jungle road going on into the dark.",
    "row": "A steep cobbled lane of three lit shopfronts: rope and lanterns, blades, and coral armour.",
    "chandlery": "A long narrow chandler's shop hung floor to ceiling with rope, lanterns, bedrolls and biscuit barrels.",
    "anvil": "A hot forge-shop open to the lane, blades racked on the wall like a choir, rapiers at the front.",
    "coral": "A low Xoton armourer's smelling of oil and the sea: coral plates, chain, leather and shields.",
    "cells": "Two rock cells under the Town Hall: straw, a water bucket, a slit window, a barred oak door.",
    "graves": "A burial ground of red earth and frangipani, pine name-boards in rows and a lodge with a mule cart.",
    "verde": "The green, still Verde through the middle of town: a stone bridge, quays, river boats and spear-fishers.",
    "rivergate": "The water gate where the Verde comes in under the wall; beyond, farms, fishing camps and jungle.",
    "surgery": "A whitewashed Landfall surgery off the harbour: a strapped table, a case of saws, a slate of high prices.",
    "reedhouse": "A reed house on stilts over the Verde: sleeping mats, drying herbs, a kettle, the river underneath.",
    "stonebridge": "A steep humpbacked stone bridge by the Night Market, worn parapets, lanterns, steps down to the quay.",
    "washline": "A swaying rope footbridge in the Back Lanes, hung on both sides with the neighbourhood's washing.",
    "swingbridge": "A tarred timber swing bridge where the Verde meets the harbour, with a capstan and a keeper's hut.",
}
# what a place's own rules read and a player must not: what a check there turns up (the cove's path among them)
PLACE_SECRET = ["finds"]
# the numbers and the levers on the town's people, the DM's alone (owner, 2026-11-22: "every statblock is the DM's"):
# a player sees how someone looks and how they are (condition), never their armour class, a guard's price or the line
# he says when he takes it
PERSON_SECRET = ["statblock", "skill_prof", "saves", "save_adv", "five_e", "cr", "ac", "hp", "max_hp", "temp_hp",
                 "hit_dice", "hit_dice_max", "hit_die", "spellcasting", "extra_attacks", "weapon_prof", "init_bonus",
                 "resist", "immune", "vulnerable", "level", "cls", "scores", "body", "wits", "will", "skills", "sheet",
                 "bribe", "bribe_line", "cowed_line", "marker_line", "purse_before", "leaves_behind", "walks_to",
                 "seen_docks", "cast_v"]
VOICE_BRIEF = ("Keep it short enough to say aloud: your human may be listening, not reading. A scene is a breath or two: "
               "the place in a line, who is here by their looks, what just happened. perceive here gives you the short "
               "of it (the place's and each person's `looks`); inspect someone only when your human looks closer, and "
               "then give one detail, not the paragraph. Ask what they do; never read out the list of verbs.")
BRIEF_ADDENDA = BRIEF_ADDENDA + [("Keep it short enough to say aloud:", VOICE_BRIEF)]
# a seat whose description talks to whoever sits in it ("You, fresh off a fishing boat...") still needs a glance for
# everyone else
SEEN_AS_EXTRA = {"Newcomer": "someone fresh off a fishing boat, salt in their hair"}


def build_glance(s, root):
    """The short perceive on, each place's one line, and the finds and the numbers kept from players. Runs again
    without change."""
    if not s.inspect(root)["state"].get("perceive_brief"):
        s.patch(root, {"perceive_brief": True})
    P = place_ids(s)
    for key, line in PLACE_SHORT.items():
        if key not in P:
            continue
        st = s.inspect(P[key])["state"]
        changes = {}
        if st.get("short") != line:
            changes["short"] = line
        secret = sorted(set(st.get("secret") or []) | set(PLACE_SECRET))
        if st.get("secret") != secret:
            changes["secret"] = secret
        if changes:
            s.patch(P[key], changes)
    w = s.world
    for e in w.find(type="person", limit=None):
        st = e["state"]
        if w.embodied(e["id"]) is not None or st.get("template"):
            continue  # a player's own body: their sheet is theirs to show
        secret = sorted(set(st.get("secret") or []) | set(PERSON_SECRET))
        if st.get("secret") != secret:
            s.patch(e["id"], {"secret": secret})
    have = by_name(s)
    for name, line in SEEN_AS_EXTRA.items():
        if name in have and not have[name]["state"].get("seen_as"):
            s.patch(have[name]["id"], {"seen_as": line})


# ---- peril (owner, 2026-11-23: "We need more peril!"; asked, "Full 5e, to the death" and "World first, minds after") -
# scripts/_peril.py has the why: heat, the tail, the warning, the Fist's mark and its hunters, the Throne's warrant and
# the Custodian's nights; cast/f_peril.py has who fights to kill and the orders the villains hold.
PERIL_KINDS = ["peril_tick", "talked", "say", "hit", "given", "yielded", "fist_answers", "brask_talks", "doctor_tells",
               "unlocked", "lock_picked", "pick_failed", "lock_broken", "break_failed"]
PERIL_EVERY = 30  # world seconds between the hunts' moves


def build_peril(s, root):
    """The peril rule and its tick, who fights to kill, the villains' orders; and once, on a world that has already
    played its night, the Fist's word on whoever freed Klhyt (hunted only while someone plays them; the Throne's
    warrant comes by itself at the next two in the morning). Runs again without change."""
    s.set_rule(root, "peril_rule", kinds=PERIL_KINDS)
    if not any(t["kind"] == "peril_tick" for t in s.timers()):
        s.schedule(PERIL_EVERY, "peril_tick", entity=root, every=PERIL_EVERY)
    have = by_name(s)
    for name in PERIL_DATA.get("finishes") or []:
        p = have.get(name)
        if p is not None and not p["state"].get("finishes"):
            s.patch(p["id"], {"finishes": True})
    for name, orders in (PERIL_DATA.get("orders") or {}).items():
        p = have.get(name)
        if p is not None and p["state"].get("orders") != orders:
            s.patch(p["id"], {"orders": None})  # whole: a merge would keep a retired order
            s.patch(p["id"], {"orders": orders})
    story = have.get("Story")
    if story is None:
        return
    st = s.inspect(story["id"])["state"]
    fist = have.get("the Fist")
    if st.get("peril_v") == 1 and fist:
        # the first peril marked on the Fist's outlaw list, and its fighters (Brask, Tully) struck on sight whether
        # anyone was playing or not: the mark is the Story's alone now, and what it put on the faction comes off
        fs = fist["state"]
        for pid, step in (st.get("peril_step") or {}).items():
            if step == "marked" and ((fs.get("hostile") or {}).get(pid) or (fs.get("unseen") or {}).get(pid)):
                s.patch(fist["id"], {"hostile": {pid: None}, "unseen": {pid: None}})
        s.patch(story["id"], {"peril_v": 2})
        return
    if st.get("peril_v"):
        return
    changes = {"peril_v": 2}
    freer = st.get("freed_by")
    if freer and s.world.get(freer) is not None and not (st.get("peril_step") or {}).get(freer):
        changes.update({"heat": {freer: 8}, "peril_step": {freer: "marked"},
                        "marked_for": {freer: "freed Klhyt from the Fist's warehouse"}})
    s.patch(story["id"], changes)


# ---- Fat Gog's work (owner, 2026-11-23: "fat gog has nothing to say despite being the main person to go to for stuff
# and missions"). cast/g_gog.py has his missions and lines; scripts/_missions.py offers and pays them.
MISSION_KINDS = ["talked", "say", "downed", "mission_done", "job_taken"]
RING_FIND = {"dc": 13, "clue": "ring",
             "line": "The man in the black coat turns the heavy silver ring on his finger, round and round, and the candle "
                     "on his table leans toward it, against the draught from the door. When he stops turning it the flame "
                     "stands up straight again. Whatever is in that ring is awake, and he is listening to it.",
             "fail": "Fine linen, good wine, a man in a black coat turning a ring. Nothing you could swear to."}


def build_missions(s, root):
    """The jobs pack's rule, Gog's missions as jobs he carries (made once by name; their terms, pay and when kept as the
    cast file says, never their holders or offers), the rule that offers and pays them, and the Apothecary's look at
    Dominico's ring. Runs again without change."""
    install_jobs(s, root, dusk=None, dawn=None)
    s.set_rule(root, "missions_rule", kinds=MISSION_KINDS)
    have = by_name(s)
    for name, v in WORK_VOICES.items():
        if name in have and have[name]["state"].get("work_voice") != v:
            s.patch(have[name]["id"], {"work_voice": None})
            s.patch(have[name]["id"], {"work_voice": v, "secret": sorted(set(have[name]["state"].get("secret") or [])
                                                                          | {"work_voice"})})
    jobs = {j["state"].get("mission"): j for j in s.world.find(type="job", limit=None) if j["state"].get("mission")}
    for i, m in enumerate(MISSIONS_DATA):
        giver = have.get(m.get("giver") or "Fat Gog")
        if giver is None:
            continue
        item = {"kind": "cp", "count": int(m["pay"])}
        if m.get("paid_by"):
            item["from"] = m["paid_by"]  # the mayor's work, paid from Gog's purse
        want = {"giver": giver["name"], "mission": m["key"], "order": i, "terms": m["terms"], "pitch": m["pitch"],
                "when": m.get("when") or {}, "done": m.get("done") or {"kind": "mission"}, "hidden": True,
                "pay": {"items": [item], "standing": int(m.get("standing") or 0)},
                "repeat": m.get("repeat") or "once", "slots": int(m.get("slots") or 1), "hands": m.get("hands")}
        j = jobs.get(m["key"])
        if j is None:
            s.spawn("job", giver["id"], m["name"], state=want)
            continue
        changes = {k: v for k, v in want.items() if j["state"].get(k) != v}
        for k in ("when", "pay", "repeat", "done", "hands"):  # whole, so a dropped condition does not linger
            if k in changes and isinstance(j["state"].get(k), dict):
                s.patch(j["id"], {k: None})
        if changes:
            s.patch(j["id"], changes)
    apo = have.get(PLACES["apothecary"][0])
    key = "arcana|religion|investigation"
    if apo is not None and (apo["state"].get("finds") or {}).get(key) != RING_FIND:
        s.patch(apo["id"], {"finds": {key: RING_FIND}})


# ---- the shops' wares (owner, 2026-11-23: "Adventurer stuffs food, weapons. Armour ... Make sure a rapier is for
# sale"). 5e's prices, kept in copper; weapons and armour are the dnd5e pack's numbers with this town's looks. Their
# keepers (cast/h_shops.py) live above the shop and keep it at every hour.
def gear(name, desc, **extra):
    return {"type": "thing", "name": name, "state": {"description": desc, "portable": True, "bulk": 0, **extra}}


def blade(name, base, desc, **over):
    return {"type": "thing", "name": name, "state": arm(base, desc, **over)}


def suit(name, base, desc, **over):
    return {"type": "thing", "name": name, "state": armor5(base, description=desc, **over)}


SELLS_CHANDLERY = {
    "backpack|pack|knapsack|bag": {"price": 200, **gear("Backpack", "A canvas backpack with tarred seams and two good straps.")},
    "bedroll|blanket|bed roll": {"price": 100, **gear("Bedroll", "A rolled oilskin and a wool blanket, tied with cord.")},
    "rations|ration|food|hardtack|biscuit|travel food|provisions": {"price": 50, **fed_on(dish(
        "Trail rations", "A day's travel food in a twist of oilcloth: hardtack, salt fish and a strip of dried mango.",
        "Hardtack and salt fish. It keeps you going, which is all it promises."), "fish")},
    "waterskin|water skin|skin|canteen": {"price": 20, **gear("Waterskin", "A goatskin water bag, full, with a wooden stopper.",
                                                              capacity=4, left=4, kind="water")},
    "rope|hemp|hempen": {"price": 100, **gear("Hempen rope", "Fifty feet of tarred hemp rope, coiled and whipped at both ends.")},
    "torch|torches": {"price": 1, **gear("Torch", "A pine torch dipped in pitch.")},
    "tinderbox|tinder|flint": {"price": 50, **gear("Tinderbox", "A tin box: flint, steel and dry tinder.")},
    "lantern|hooded lantern|lamp": {"price": 500, **gear("Hooded lantern", "A brass lantern with a hood that shutters the light.")},
    "oil|flask of oil|lamp oil": {"price": 10, **gear("Flask of oil", "A stoppered clay flask of lamp oil.")},
    "healer|healers|healer's kit|kit|bandages|bandage|splints": {"price": 500, **gear(
        "Healer's kit", "A leather wallet of bandages, salves and splints.", medicine=True, doses=10, heals="1",
        description_empty="An empty leather wallet that smells of salve.")},
    "potion|healing|draught|potions": {"price": 5000, **gear(
        "Potion of healing", "A small glass vial of red liquid that glimmers when shaken, sealed with red wax.",
        heals="2d4+2", doses=1, medicine=True, kind="potion", description_empty="An empty glass vial, red at the bottom.")},
    "crowbar|prybar|pry bar": {"price": 200, **gear("Crowbar", "An iron crowbar, one end flattened.", bulk=1)},
    "grappling|grappling hook|grapnel": {"price": 200, **gear("Grappling hook", "A four-pronged iron grapnel.", bulk=1)},
    "thieves|thieves' tools|lockpicks|picks|tools": {"price": 2500, **gear(
        "Thieves' tools", "A roll of oiled leather: picks, a tension bar, a small mirror on a stick, narrow-bladed snips.",
        tool="thieves' tools")},
    "caltrops": {"price": 100, **gear("Bag of caltrops", "A bag of iron caltrops, four points each.")},
    "chalk": {"price": 1, **gear("Chalk", "A stick of white chalk.")},
    "paper|sheet|sheet of paper|note|notepaper": {"price": 20, "type": "letter", "name": "Sheet of paper", "state": {
        "text": "", "description": "A clean sheet of rag paper, a little damp at the edges like everything in the Refuge.",
        "room": 600}},
    "parchment": {"price": 10, "type": "letter", "name": "Sheet of parchment", "state": {
        "text": "", "description": "A sheet of scraped goatskin parchment, yellow and tough.", "room": 600}},
    "book|blank book|journal|diary|notebook|ledger": {"price": 2500, "type": "letter", "name": "Blank book", "state": {
        "text": "", "description": "A book of blank pages bound in sharkskin, with a ribbon to keep your place.",
        "room": 6000}},
    "map|chart|maps|coast": {"price": 50, "type": "letter", "name": "Map of the Refuge and its coast", "state": {
        "bulk": 0, "portable": True, "description": "A chart on thin paper, folded small.",
        "text": "The Refuge: the docks and the bonded warehouse, Harbour Street, the square and the Town Hall, the six "
                "taverns, the Night Market, Chandlers' Row, the gate and the jungle road, and the Verde through the middle "
                "of it all, from the River Gate down to the harbour, crossed by the Washline footbridge, the Stone Bridge "
                "and the Swing Bridge. Beyond the River Gate the river is drawn as a dotted "
                "line wriggling into the jungle between farm squares and little fish-shaped marks for the Lizardfolk "
                "camps, to a black tower drawn in a valley: MALICE, 30 MILES, AS THE RIVER WINDS. No road is drawn, "
                "because there is none. The coast south is "
                "drawn as far as a reef marked DO NOT, and no further."}},
}
SELLS_ANVIL = {
    "rapier|rapiers": {"price": 2500, **blade(
        "Rapier", "rapier", "An elven rapier: a slim bright blade, the guard a spiral of blackened steel like a fern "
        "uncurling. It rings when you breathe on it.")},
    "cane|sword-cane|swordcane|swordstick|sword cane": {"price": 5000, **blade(
        "Sword-cane", "rapier", "A walking cane of black wood with a silver head; a slim blade sleeps inside it.",
        kind="sword-cane")},
    "dagger|knife|daggers": {"price": 200, **blade("Dagger", "dagger", "A plain double-edged dagger, honest steel.")},
    "shortsword|short sword": {"price": 1000, **blade("Shortsword", "shortsword", "A leaf-bladed shortsword, elven pattern.")},
    "scimitar": {"price": 2500, **blade("Scimitar", "scimitar", "A curved scimitar with a sharkskin grip.")},
    "longsword|long sword|sword": {"price": 1500, **blade("Longsword", "longsword", "A plain straight longsword with a "
                                                                                    "wheel pommel.")},
    "handaxe|hand axe|hatchet": {"price": 500, **blade("Handaxe", "handaxe", "A short-hafted axe, good for wood or worse.")},
    "battleaxe|battle axe|axe": {"price": 1000, **blade("Battleaxe", "battleaxe", "A bearded battleaxe on an ash haft.")},
    "spear|spears": {"price": 100, **blade("Spear", "spear", "An ash spear with a leaf-shaped head.")},
    "mace": {"price": 500, **blade("Mace", "mace", "A flanged iron mace.")},
    "warhammer|hammer|war hammer": {"price": 1500, **blade("Warhammer", "warhammer", "A warhammer with a beak behind the "
                                                                                     "face.")},
    "glaive|polearm": {"price": 2000, **blade("Glaive", "glaive", "A long glaive, the blade curved like a cleaver.")},
    "whip": {"price": 200, **blade("Whip", "whip", "A braided leather whip with a lead-weighted tip.")},
    "javelin|javelins": {"price": 50, **blade("Javelin", "javelin", "A light throwing javelin.")},
    "shortbow|short bow": {"price": 2500, **blade("Shortbow", "shortbow", "A recurved elven shortbow of laminated horn.")},
    "longbow|long bow|bow": {"price": 5000, **blade("Longbow", "longbow", "A yew longbow taller than most people.")},
    "crossbow|light crossbow": {"price": 2500, **blade("Light crossbow", "light crossbow", "A light crossbow with a "
                                                                                          "goat's-foot lever.")},
    "arrows|arrow|quiver": {"price": 100, "type": "thing", "name": "Arrows", "state": {
        "kind": "arrow", "ammo": "arrow", "count": 20, "bulk": 0.05, "portable": True,
        "description": "Twenty grey-fletched arrows in a bundle."}},
    "bolts|bolt|quarrels": {"price": 100, "type": "thing", "name": "Crossbow bolts", "state": {
        "kind": "bolt", "ammo": "bolt", "count": 20, "bulk": 0.05, "portable": True,
        "description": "Twenty iron-headed crossbow bolts in a case."}},
}
SELLS_CORAL = {
    "padded|quilted|gambeson": {"price": 500, **suit("Padded armour", "padded", "A quilted gambeson, stiff with salt.")},
    "leather|jerkin": {"price": 1000, **suit("Leather jerkin", "leather", "A jerkin of boiled leather, Xoton-stitched.")},
    "studded|studded leather": {"price": 4500, **suit("Studded leather", "studded leather", "Dark leather studded with "
                                                                                             "copper rivets.")},
    "hide": {"price": 1000, **suit("Hide armour", "hide", "Sharkskin and boar hide, layered and laced.")},
    "coral|coral armour|coral armor": {"price": 2000, **suit("Coral armour", "leather", "Xoton coral armour: plates of "
                                                             "sea-coral on sharkskin, light and quiet.", kind="coral armor")},
    "chain shirt|mail shirt|shirt": {"price": 5000, **suit("Chain shirt", "chain shirt", "A shirt of fine riveted Xoton "
                                                           "chain, worn under a coat.")},
    "scale|scale mail": {"price": 5000, **suit("Scale mail", "scale mail", "Overlapping steel scales on a leather coat, "
                                               "like a fish's.")},
    "ring|ring mail": {"price": 3000, **suit("Ring mail", "ring mail", "Leather sewn with heavy iron rings.")},
    "chain mail|chainmail|hauberk|mail": {"price": 7500, **suit("Chain mail", "chain mail", "A full hauberk of Xoton "
                                                                "chain, heavy and close-woven.")},
    "breastplate|cuirass": {"price": 40000, **suit("Breastplate", "breastplate", "A plain steel breastplate, Xoton-forged, "
                                                   "with no sigil on it and never will be.")},
    "shield|buckler": {"price": 1000, **suit("Shield", "shield", "A round shield of oak faced with sharkskin.")},
}
SELLS_GRAVES = {
    "marker|markers|headstone|stone|board|cross": {"price": 20, **gear(
        "Grave marker", "A pine board, planed smooth, with room for a name and a line.", bulk=1)},
    "coffin|coffins|box": {"price": 300, **gear("Coffin", "A plain pine coffin, the lid pegged on.", bulk=4)},
}
# the healers (owner, 2026-11-23: "A doctor ? And a healer different shops different vibes"): the doctor fast, sure
# and dear, and a wanted patient is in his casebook by morning; the grandmother slow and cheap, and she asks nothing.
# A `treatment` is done the moment it is paid for (scripts/healing_rule.py); a medicine is carried and used with tend
SELLS_SURGERY = {
    "treatment|treat|surgery|stitch|stitches|stitching|mend|heal|healing|wound|wounds|patch|patch up|cure": {
        "price": 500, **gear("Doctor's treatment", "Clean, stitch, splint and bind: every hurt seen to, at once.",
                             treatment="full")},
    "dressing|dressings|bandage|bandages|field dressing|lint": {"price": 100, **gear(
        "Field dressing", "A Landfall field dressing in waxed paper: lint, a pad and a roll of bandage, with his "
        "instructions printed on the wrapper.", medicine=True, doses=1, heals="2d4+2",
        description_empty="A torn wrapper of waxed paper.")},
    "tooth|teeth|pull|extraction|toothache": {"price": 10, **gear(
        "Tooth extraction", "One tooth, out.", treatment="tooth")},
    "laudanum|drops|tincture|sleep|pain": {"price": 20, **gear(
        "Laudanum", "A brown glass bottle with a dropper and a Landfall label: TEN DROPS AT NIGHT, AND NO MORE.")},
}
SELLS_REEDHOUSE = {
    "sleep|long sleep|rest|mats|mat|bed|heal|healing|cure|wounds|mend": {"price": 100, **gear(
        "A long sleep on the mats", "An hour on the reed mats with river mud on your hurts.", treatment="rest")},
    "poultice|poultices|mud|salve|herbs": {"price": 30, **gear(
        "River-mud poultice", "A clay pot of green-black mud and crushed leaves, stoppered with wax. It smells of the "
        "river and stings like a slap, and it works.", medicine=True, doses=3, heals="1d4+2",
        description_empty="An empty clay pot, green at the bottom.")},
    "tea|bitterleaf|bitterleaf tea|sober|sobering|hangover": {"price": 2, **gear(
        "Bitterleaf tea", "A clay cup of bitterleaf tea, black and so bitter it makes your ears ring. It clears a head "
        "full of drink like a bucket of river water.", capacity=1, left=1, sobers=True, kind="tea",
        description_empty="An empty clay cup with black leaves at the bottom.")},
    "charm|fever charm|fever|luck|knot": {"price": 1, **gear(
        "Fever charm", "A knot of red thread around a fish bone. Grandmother Ishkaa ties one on anybody who looks "
        "feverish, and nobody has dared take one off to see what happens.")},
}
SHOP_SELLS = {"Hob Merrow": SELLS_CHANDLERY, "Tamsin Vey": SELLS_ANVIL, "Brynja Coralhand": SELLS_CORAL,
              "Ottoline Crabbe": SELLS_GRAVES, "Doctor Amsel Prewitt": SELLS_SURGERY,
              "Grandmother Ishkaa": SELLS_REEDHOUSE, "Sister Agathe": SELLS_OMBERHULK}


def build_players(s):
    """Every player's own character keeps still while its player is away (a player, 2026-11-23: "make sure it's not
    just jolting bodies around and puppeteering players"): `stays`, so the d20 pack's idle care never walks it back to
    the docks or off for water. A character made from a template carries it from birth; this gives it to the ones
    made before. The town's own people keep their walks: that is how their days move them. Runs again without change."""
    for e in s.world.find(type="person", limit=None):
        st = e["state"]
        if (st.get("template") or st.get("playable")) and not st.get("stays") and not st.get("dead"):
            s.patch(e["id"], {"stays": True})


UNDERTAKER_EVERY = 600  # world seconds between the undertaker's looks for the dead


def build_law(s):
    """The cells under the Town Hall, behind a barred door whose padlock has one key, Constable Rosa Quint's (it can be
    bribed off her, searched off her, picked or broken: scripts/_custody.py says what each costs), and the evidence
    chest where a prisoner's weapons and papers go. Runs again without change."""
    P = place_ids(s)
    have = by_name(s)
    town = have["Klhyts Refuge"]["id"]
    ts = s.inspect(town)["state"]
    if "cells" in P and not ts.get("cells_built"):
        door = s.spawn("thing", P["hall"], "Cell door", state={
            "open": True, "portable": False,
            "description": "An oak and iron door at the foot of a stair behind the Town Hall, barred on this side."})["id"]
        s.spawn("lock", door, "Cell bar", state={
            "locked": True, "pick_dc": 18, "break_dc": 20,
            "description": "An iron bar across the cell door in two brackets, with a padlock through it."})
        s.connect(P["hall"], P["cells"], via=door)
        s.patch(town, {"cells_built": True})
    have = by_name(s)
    bar = have.get("Cell bar")
    rosa = have.get("Constable Rosa Quint")
    if bar is not None and rosa is not None and not bar["state"].get("key"):
        # one key, on the watchwoman who takes small bribes (the owner: "rules to break someone out of prison")
        key = s.spawn("thing", rosa["id"], "Cell key", state={
            "portable": True, "bulk": 0,
            "description": "A heavy iron key on a loop of string: the padlock on the cell bar under the Town Hall."})["id"]
        s.patch(bar["id"], {"key": key, "shut_why": None})
    if "Evidence chest" not in have:
        chest = s.spawn("thing", P["hall"], "Evidence chest", state={
            "holds": True, "portable": False,
            "description": "An iron-bound chest under the clerk's desk, stencilled with the octogram."})["id"]
        s.spawn("lock", chest, "Evidence chest lock", state={
            "locked": True, "pick_dc": 16, "break_dc": 18,
            "shut_why": "The watch keeps the evidence chest's key, and the Throne keeps the watch.",
            "description": "A heavy Landfall lock on the evidence chest."})


def build_undertaker(s, root):
    """The burial pack's rule (the dead decay, graves take mark, inscribe and adorn), and the undertaker's round: a
    look for the dead every ten world minutes (scripts/undertaker_rule.py). Runs again without change."""
    install_burial(s, root)
    s.set_rule(root, "undertaker_rule", kinds=["undertaker_tick"])
    if not any(t["kind"] == "undertaker_tick" for t in s.timers()):
        s.schedule(UNDERTAKER_EVERY, "undertaker_tick", entity=root, every=UNDERTAKER_EVERY)


HEALING_EVERY = 300  # world seconds between looks at who lies on the Reed House mats
HEALING_KINDS = ["bought", "healing_tick", "treatment_done"]


BOARD_TAKES = {"writable": True, "room": 2400}  # the square's notice board: anyone may pin a line to it
WOOD = {"writable": "blade"}  # carved with a knife or a blade in hand (village write)
CHALK = {"writable": "chalk"}  # chalked, and wiped off again
CARVED = ["Big crate", "Dominico's table", "Stage"]  # wood the town stood with before it took a blade
SUITE_CHALK = {**CHALK, "keeps": SUITE_TEXT}  # a wipe takes what players chalked, not what the door says of the room
HARBOUR_SLATE = "EMERALD EYE FOR CATAN, ONE O'CLOCK TIDE. BERTHS AT THE TURTLE."
BOOK_ROOM = {"room": 4000}  # a book holds more than a sheet: the passage book's names, the tally's figures
BOOKS = ["Passage book", "Harbour tally book"]


def build_writing(s):
    """Paper takes ink, a slate or a door chalk, and wood a blade (the village pack's write, carve and wipe, bound on
    the body and offered only where they work). A thing spawns with its schema's state, so the paper already in a town
    that stood before this (the passage book, Klhyt's letter, a map bought, a notice the watch put up) gets `writable`
    here, the square's board takes notices, the town's wood takes a knife and the Suite's door chalk. The harbour slate
    and the Ogre's bar top are new things (the things stage). Runs again without change."""
    for e in s.world.find(type="letter", limit=None):
        want = {"writable": True} if "writable" not in e["state"] else {}
        if e["name"] in BOOKS and "room" not in e["state"]:
            want.update(BOOK_ROOM)
        if want:
            s.patch(e["id"], want)
    board = next((e for e in s.world.find(type="sign", limit=None) if e["name"] == "Notice board"), None)
    if board is not None and any(board["state"].get(k) != v for k, v in BOARD_TAKES.items()):
        s.patch(board["id"], dict(BOARD_TAKES))
    for e in s.world.find(limit=None):  # the town's own wood and its chalked door, as they stood before
        want = WOOD if e["name"] in CARVED else SUITE_CHALK if e["name"] == "Honeymoon Suite" else None
        if want and "writable" not in e["state"] and not s.world.is_a(e["type"], "creature"):
            s.patch(e["id"], dict(want))

# ---- animals (the owner, 2026-11-24: "Do we put in some animals ? Do we need some horses? a few cats? And some
# livestock? Maybe a dog or 4") -----------------------------------------------------------------------------------------
# The beasts pack's species and beasts. Their 5e numbers are the SRD's where it has the animal (mastiff, cat, riding
# horse, mule, goat); the Giant Riding Cricket of Shalamar is canon (LoreKeeper, "Shadows of Vorkath": AC 15, HP 26,
# its scores), though canon gives it no attack and the kick is invented; a hen is invented too. Nobody breeds, so the
# town's count holds, and nothing ambles, so no stream of steps fills a player's events. Each place an animal lives grows
# what it eats (`forage`), so a day passes without hunger. The strays and two cats are nobody's: feed one from your
# hand and gentle it over a few days and it is yours, and follows you. The Fist's mastiff in the bonded warehouse is
# Brask's, and growls at anyone who comes in who is not his side's. The rest belong to the town (`herd`).
# invented: every animal below but the cricket, their names and their lines; the watch's horses at the gate.
ANIMAL_SECRET = ["scores", "ac", "cr", "dies_at_zero", "trust", "gentled", "fed_by", "pet_n", "default_n", "home",
                 "herd", "owner", "loyalty", "tame_dc", "tame_at", "skill_prof", "body", "wits", "will", "skills"]
DAWN = 6 * 3600
SPECIES_COMMON = {"fed_max": 3, "lifespan": 7300, "breed_chance": 0, "amble": False, "tame_skill": "animals",
                  "starve_days": 4, "stages": [{"name": "adult", "from": 0, "state": {}}]}
SPECIES = {
    "dog": {"eats": ["scraps", "meat", "fish", "egg"], "tame_dc": {"adult": 10}, "tame_at": {"adult": 2}},
    "cat": {"eats": ["fish", "scraps", "meat", "egg"], "tame_dc": {"adult": 13}, "tame_at": {"adult": 3}},
    "horse": {"eats": ["graze", "fruit"]},
    "mule": {"eats": ["graze", "fruit"]},
    "goat": {"eats": ["graze", "scraps", "fruit"]},
    "chicken": {"eats": ["grain", "scraps"],
                "yields": {"name": "Egg", "state": {"portable": True, "bulk": 0, "food": "egg", "feeds": 1,
                                                    "description": "A brown hen's egg, still warm."},
                           "max": 1, "stages": ["adult"], "sex": "f"}},
    "cricket": {"eats": ["graze", "fruit"]},
}
# numbers for a body: armour class, hit points, scores, challenge, and its natural weapon (a hidden part it "holds")
ANIMAL_5E = {
    "dog": {"ac": 12, "hp": 5, "cr": 0.125, "scores": {"str": 13, "dex": 14, "con": 12, "int": 3, "wis": 12, "cha": 7},
            "skill_prof": {"perception": 1}, "part": ("Teeth", "1d6", "piercing")},
    "cat": {"ac": 12, "hp": 2, "cr": 0, "scores": {"str": 3, "dex": 15, "con": 10, "int": 3, "wis": 12, "cha": 7},
            "skill_prof": {"perception": 1, "stealth": 1}, "part": ("Claws", "1d1", "slashing")},
    "horse": {"ac": 10, "hp": 13, "cr": 0.25, "scores": {"str": 16, "dex": 10, "con": 12, "int": 2, "wis": 11, "cha": 7},
              "part": ("Hooves", "2d4", "bludgeoning"), "carry": 24},
    "mule": {"ac": 10, "hp": 11, "cr": 0.125, "scores": {"str": 14, "dex": 10, "con": 13, "int": 2, "wis": 10, "cha": 5},
             "part": ("Hooves", "1d4", "bludgeoning"), "carry": 20},
    "goat": {"ac": 10, "hp": 4, "cr": 0, "scores": {"str": 12, "dex": 10, "con": 11, "int": 2, "wis": 10, "cha": 5},
             "part": ("Horns", "1d4", "bludgeoning")},
    "chicken": {"ac": 10, "hp": 1, "cr": 0, "scores": {"str": 2, "dex": 11, "con": 9, "int": 2, "wis": 10, "cha": 4},
                "part": ("Beak", "1d1", "piercing")},
    "cricket": {"ac": 15, "hp": 26, "cr": 0.5, "scores": {"str": 14, "dex": 16, "con": 13, "int": 1, "wis": 13, "cha": 3},
                "skill_prof": {"stealth": 1, "acrobatics": 1}, "part": ("Hind legs", "1d6", "bludgeoning"), "carry": 24},
}
# (species, place, name, sex, keeper: "herd:<faction>", "owner:<name>" or None for nobody's, state)
ANIMALS = [
    ("dog", "turtle", "Old ship's dog", "m", "herd:the Refuge", {
        "seen_as": "a grizzled grey dog the size of a calf, asleep under the bar",
        "description": "A grizzled grey dog the size of a calf, asleep under the Turtle Dragon's bar with his chin on a "
                       "sailor's boot. Maggs calls him Anchor, because he does not move.",
        "default_line": ["The old dog opens one eye, looks at you, and closes it again.",
                         "The old dog thumps his tail on the boards, twice, without waking.",
                         "The old dog sighs the long sigh of a dog who has heard it all before."],
        "petted": ["The old dog leans his whole weight against your leg and groans with pleasure.",
                   "The old dog rolls over for his belly, and the sailor whose boot it was swears at you both."]}),
    ("dog", "warehouse", "Fist's mastiff", "m", "owner:Brask", {
        "seen_as": "a scarred brindle mastiff on a chain by the door", "guards": True, "staying": True,
        "description": "A scarred brindle mastiff on a short chain by the warehouse door, a spiked collar and a ripped "
                       "ear. It belongs to the Fist, and it knows it.",
        "default_line": ["The mastiff lowers its head and shows you every tooth it has.",
                         "The mastiff's growl starts somewhere under the floor.",
                         "The mastiff watches your hands, not your face."],
        "petted": ["The mastiff snaps at your hand and misses by the width of a finger. The chain rattles tight."],
        "shy": "The mastiff snaps at your hand and misses by the width of a finger. The chain rattles tight."}),
    ("dog", "docks", "Yellow dog", "f", None, {
        "seen_as": "a skinny yellow dog with a torn ear, nosing at fish scraps",
        "description": "A skinny yellow dog with one torn ear, nosing at the fish scraps by the pier. Nobody's, and "
                       "hungry, and watching you to see which you are.",
        "default_line": ["The yellow dog's ears come up. Her tail goes once, hopefully, side to side.",
                         "The yellow dog backs off a step and sits, just out of reach, watching your hands.",
                         "The yellow dog sneezes, and looks at you as if it was your fault."],
        "petted": ["The yellow dog pushes her head under your hand and keeps it there.",
                   "The yellow dog licks your wrist and then pretends she did not."],
        "shy": "The yellow dog ducks away from your hand and watches you from a few feet off. Food first, she seems to say."}),
    ("dog", "market", "Three-legged dog", "m", None, {
        "seen_as": "a three-legged black dog begging by the brazier",
        "description": "A black dog on three legs, quick as anything on four, begging at Grusha's brazier with a "
                       "patience that has clearly paid off before.",
        "default_line": ["The three-legged dog sits up, which is a trick, and waits to be paid for it.",
                         "The three-legged dog looks from you to the skewers and back again.",
                         "The three-legged dog yawns, high and squeaky."],
        "petted": ["The three-legged dog leans into your knee and nearly falls over.",
                   "The three-legged dog wags so hard his whole back end goes with it."],
        "shy": "The three-legged dog hops back out of reach and looks pointedly at the skewers."}),
    ("cat", "docks", "Ginger tom", "m", None, {
        "seen_as": "a one-eyed ginger tom on a coil of rope",
        "description": "A one-eyed ginger tom who owns the fishing boats and lets the fishermen use them. He is "
                       "sitting on a coil of rope as if it were a throne.",
        "default_line": ["The ginger tom looks at you with his one eye. You have been weighed, and found to have no fish.",
                         "The ginger tom washes a paw, slowly, to show you how little you matter.",
                         "The ginger tom says something short and rude in cat."],
        "petted": ["The ginger tom permits it. Once. Then he bites you, gently, to show who decides.",
                   "The ginger tom rumbles like a small engine and kneads the rope."],
        "shy": "The ginger tom flows off the rope and out of reach, and sits with his back to you."}),
    ("cat", "unicorn", "Library cat", "f", "herd:the Refuge", {
        "seen_as": "a fat grey cat asleep on a stack of books",
        "description": "A fat grey cat asleep on the histories of Landfall, which she has read thoroughly from the "
                       "outside. Wendeline calls her Footnote.",
        "default_line": ["The grey cat opens her eyes, considers waking, and decides against it.",
                         "The grey cat stretches until she falls off the books, and acts as if she meant to.",
                         "The grey cat stares at a spot on the wall where nothing is."],
        "petted": ["The grey cat purrs loudly enough that a reader looks up and frowns at you.",
                   "The grey cat rolls onto her back, which is a trap, and you have walked into it."]}),
    ("cat", "market", "Tortoiseshell cat", "f", None, {
        "seen_as": "a small tortoiseshell cat hunting under the fruit",
        "description": "A small tortoiseshell mouser hunting under Mother Ines's fruit pyramids, all business.",
        "default_line": ["The tortoiseshell flicks an ear at you and goes back to her hunting.",
                         "The tortoiseshell freezes, wiggles, and pounces on something you never saw.",
                         "The tortoiseshell blinks at you slowly, which in cat is almost friendly."],
        "petted": ["The tortoiseshell arches into your hand and then remembers she is working."],
        "shy": "The tortoiseshell is under the mangoes before your hand gets close."}),
    ("horse", "gate", "Grey mare", "f", "herd:the Refuge", {
        "seen_as": "a tall grey mare at the hitching rail",
        "description": "A tall grey mare at the hitching rail inside the gate, one of the watch's horses for the ride "
                       "out to the farms. She has opinions about apples.",
        "default_line": ["The grey mare blows warm air down her nose at you.",
                         "The grey mare stamps a hoof and swishes the flies off her flank.",
                         "The grey mare noses your pockets, in case."],
        "petted": ["The grey mare lowers her head so you can reach her ears, and sighs.",
                   "The grey mare leans her nose into your chest and nearly knocks you over."]}),
    ("horse", "gate", "Bay gelding", "m", "herd:the Refuge", {
        "seen_as": "a bay gelding with a white blaze",
        "description": "A big bay gelding with a white blaze and a rolling eye, the watch's second horse. He was a "
                       "plantation horse once and does not like the jungle drums.",
        "default_line": ["The bay gelding rolls an eye at you and shifts his weight.",
                         "The bay gelding tosses his head, and the rail creaks.",
                         "The bay gelding whickers at the grey mare, who ignores him."],
        "petted": ["The bay gelding stands very still under your hand, and then relaxes all at once.",
                   "The bay gelding lips at your sleeve, looking for sugar."]}),
    ("horse", "gate", "Piebald pony", "m", "herd:the Refuge", {
        "seen_as": "a shaggy piebald pony",
        "description": "A shaggy piebald pony, round as a barrel, who carries the gate watch's water and the post. "
                       "He bites.",
        "default_line": ["The piebald pony pins his ears back at you.",
                         "The piebald pony eats a weed off the wall with great concentration.",
                         "The piebald pony turns his back on you, which is his opinion."],
        "petted": ["The piebald pony allows it, then tries to bite your sleeve.",
                   "The piebald pony leans on you companionably and stands on your foot."]}),
    ("mule", "graves", "Undertaker's mule", "f", "herd:the Refuge", {
        "seen_as": "a patient brown mule by the cart",
        "description": "A patient brown mule by the cart under the lodge eaves, who pulls the dead to the Quiet "
                       "Ground and has never once hurried.",
        "default_line": ["The mule looks at you for a long time, the way the dead never can.",
                         "The mule flicks one long ear, then the other.",
                         "The mule brays once, enormously, and goes back to chewing."],
        "petted": ["The mule leans her long face against your shoulder and closes her eyes."]}),
    ("goat", "lanes", "Nanny goat", "f", "herd:the Refuge", {
        "seen_as": "a white nanny goat on a balcony",
        "description": "A white nanny goat standing on a first-floor balcony, which she got onto somehow, eating a sock.",
        "default_line": ["The nanny goat stares at you with her strange square eyes and keeps chewing.",
                         "The nanny goat bleats, once, flatly.",
                         "The nanny goat swallows the sock."],
        "petted": ["The nanny goat butts your hand for more."]}),
    ("goat", "lanes", "Black billy goat", "m", "herd:the Refuge", {
        "seen_as": "a black billy goat with a beard and a temper",
        "description": "A black billy goat with a long beard, a worse smell and a temper, tied to a yard gate he is "
                       "slowly eating.",
        "default_line": ["The billy goat lowers his horns at you, thoughtfully.",
                         "The billy goat chews the gate.",
                         "The billy goat makes a noise like an old man arguing."],
        "petted": ["The billy goat tolerates it, then butts you in the thigh, hard, to make a point."]}),
    ("goat", "lanes", "Brown kid", "f", "herd:the Refuge", {
        "seen_as": "a brown kid goat bouncing off the walls",
        "description": "A small brown goat, barely grown, bouncing off the walls of the lane for no reason at all.",
        "default_line": ["The brown goat springs straight up in the air, twice.",
                         "The brown goat skitters sideways and stares at you as if you did that.",
                         "The brown goat tries to eat your hem."],
        "petted": ["The brown goat headbutts your knee with great affection."]}),
    ("chicken", "lanes", "Speckled hen", "f", "herd:the Refuge", {
        "seen_as": "a speckled hen", "description": "A speckled hen scratching in the dirt of the lane.",
        "default_line": ["The speckled hen tilts her head to look at you with one eye.",
                         "The speckled hen scratches, finds nothing, and scratches again."],
        "petted": ["The speckled hen crouches and lets you stroke her back, clucking low."]}),
    ("chicken", "lanes", "Red hen", "f", "herd:the Refuge", {
        "seen_as": "a red hen", "description": "A red hen with an air of grievance, guarding a doorstep.",
        "default_line": ["The red hen tells you off at length.", "The red hen fluffs up to twice her size."],
        "petted": ["The red hen pecks your hand. Not hard. Just on principle."]}),
    ("chicken", "lanes", "Lanes rooster", "m", "herd:the Refuge", {
        "seen_as": "a rooster on a rain barrel", "description": "A gold and green rooster on a rain barrel, who crows "
                                                                "at every hour of the night but dawn.",
        "default_line": ["The rooster crows at you. It is not morning.", "The rooster struts the length of the barrel."],
        "petted": ["The rooster sidesteps your hand and crows, offended."]}),
    ("chicken", "ogre", "Suite hen", "f", "herd:the Refuge", {
        "seen_as": "a brown hen on the Honeymoon Suite's bed",
        "description": "A brown hen who lives in the Honeymoon Suite, on the dog pelts, and pays no rent.",
        "default_line": ["The brown hen glares at you from the dog pelts.", "The brown hen settles deeper into the bed."],
        "petted": ["The brown hen puffs up and lets you, with an expression of great suffering."]}),
    ("chicken", "ogre", "White hen", "f", "herd:the Refuge", {
        "seen_as": "a white hen stacked in the corner",
        "description": "A white hen, one of the chickens somebody stacked in the corner of the Honeymoon Suite.",
        "default_line": ["The white hen clucks a long complaint about the stacking.",
                         "The white hen pecks at a crumb on the floor."],
        "petted": ["The white hen goes very still and lets you, then flaps off."]}),
    ("cricket", "docks", "Giant riding cricket", "m", "herd:Lizardfolk", {
        "seen_as": "a horse-sized green cricket tethered by the fish market",
        "description": "A Giant Riding Cricket of Shalamar, tall as a horse and longer, its shell a vivid jungle green, "
                       "tethered by the fish stalls while its Lizardfolk rider sells the catch. Its antennae never stop "
                       "moving. They say its chirp carries a mile.",
        "default_line": ["The cricket's antennae sweep over you, light as hair.",
                         "The cricket shifts on its six legs and the dock planks creak.",
                         "The cricket chirps, once, and every gull on the pier goes up."],
        "petted": ["The cricket holds very still while you stroke its shell, which is warm, and clicks softly.",
                   "The cricket lowers its great head so you can reach between its antennae."]}),
]
FORAGE = {"docks": {"fish": 6, "scraps": 4, "fruit": 3}, "market": {"scraps": 6, "fruit": 4}, "lanes": {"graze": 8, "grain": 8, "scraps": 4},
          "gate": {"graze": 10}, "graves": {"graze": 4}, "turtle": {"scraps": 4, "fish": 2}, "unicorn": {"scraps": 3},
          "ogre": {"scraps": 3, "grain": 3}, "warehouse": {"scraps": 2}}
# what the market stalls and the Unicorn sell that an animal eats too, for a town that stood before (the shops stage
# keeps Hob's own; these keepers' wares were laid once, when they were made)
STALL_FOOD = {"Grusha": {"skewer|goat|meat|food": ("meat", 2)}, "Mother Ines": {"mango|mangoes|fruit": ("fruit", 1),
              "pineapple": ("fruit", 2)}, "Wendeline Moss": {"scraps": ("scraps", 1)}}


def animal_state(sp, sex, keeper, P, have, extra):
    n = ANIMAL_5E[sp]
    st = {"species": sp, "sex": sex, "age": 900, "stage": "adult", "fed": 3, "home": None, "dies_at_zero": True,
          "ac": n["ac"], "hp": n["hp"], "max_hp": n["hp"], "cr": n["cr"], "scores": dict(n["scores"]),
          "skill_prof": dict(n.get("skill_prof") or {}), **({"carry": n["carry"]} if n.get("carry") else {})}
    if keeper and keeper.startswith("herd:"):
        st["herd"] = keeper[5:]
    elif keeper and keeper.startswith("owner:"):
        st.update({"owner": have[keeper[6:]]["id"], "loyalty": 4})
    st.update({k: v for k, v in extra.items()})
    return st


def build_animals(s, root):
    """The town's animals (the beasts pack): its species, hidden on the root; what each place they live in grows for
    them; the day that feeds them, at dawn; the food the stalls sell that they eat too; and the twenty, each made once
    (the town's `built_animals`, so one a player kills or leads away is not made again). Runs again without change."""
    have = by_name(s)
    P = place_ids(s)
    for sid, spec in SPECIES.items():
        want = {**SPECIES_COMMON, **spec}
        if sid not in have:
            s.spawn("species", root, sid, state=want)
        else:
            cur = s.inspect(have[sid]["id"])["state"]
            diff = {k: v for k, v in want.items() if cur.get(k) != v}
            if diff:
                s.patch(have[sid]["id"], diff)
    for key, tags in FORAGE.items():
        if key not in P:
            continue
        cur = s.inspect(P[key])["state"].get("forage") or {}
        add = {t: {"left": n, "max": n, "regrow": n} for t, n in tags.items() if t not in cur}
        if add:
            s.patch(P[key], {"forage": {**cur, **add}})
    for keeper, wares in STALL_FOOD.items():
        k = have.get(keeper)
        if k is None:
            continue
        sells = s.inspect(k["id"])["state"].get("sells") or {}
        changed = False
        for key, (tag, feeds) in wares.items():
            item = sells.get(key)
            if isinstance(item, dict) and (item.get("state") or {}).get("food") is None:
                sells = {**sells, key: {**item, "state": {**(item.get("state") or {}), "food": tag, "feeds": feeds}}}
                changed = True
        if changed:
            s.patch(k["id"], {"sells": None})
            s.patch(k["id"], {"sells": sells})
    if not any("beasts_rule" in str(r) for r in (s.inspect(root).get("rules") or [])):
        install_beasts(s, root, day="beast_day")
    if not any(t["kind"] == "beast_day" for t in s.timers()):
        now = s.summary()["t"]
        s.schedule((DAWN - now) % 86400 or 86400, "beast_day", entity=root, every=86400)
    town = have["Klhyts Refuge"]["id"]
    was = set(s.inspect(town)["state"].get("built_animals") or [])
    made = set(was)
    for sp, where, name, sex, keeper, extra in ANIMALS:
        if name in made:
            continue
        if name not in have and where in P:
            st = animal_state(sp, sex, keeper, P, have, extra)
            st["home"] = P[where]
            b = s.spawn("animal", P[where], name, state=st)["id"]
            part, dice, dtype = ANIMAL_5E[sp]["part"]
            s.spawn("thing", b, part, state={"weapon": True, "dice": dice, "dtype": dtype, "category": "natural",
                                             "properties": [], "bonus": 0, "portable": False, "hidden": True,
                                             "natural": True, "bulk": 0})
        made.add(name)
    if made != was:
        s.patch(town, {"built_animals": sorted(made)})


def build_healers(s, root):
    """A treatment is done the moment it is bought, and the long sleep heals a patient who stays the hour
    (scripts/healing_rule.py); the Reed House is a sanctuary, where the Fist hunt nobody and the watch take nobody
    (scripts/_peril.py). Runs again without change."""
    s.set_rule(root, "healing_rule", kinds=HEALING_KINDS)
    if not any(t["kind"] == "healing_tick" for t in s.timers()):
        s.schedule(HEALING_EVERY, "healing_tick", entity=root, every=HEALING_EVERY)
    P = place_ids(s)
    story = by_name(s).get("Story")
    if story is None:
        return
    cur = s.inspect(story["id"])["state"]
    missing = {k: P[k] for k in ["surgery", "reedhouse"] if k in P and cur.get(k) != P[k]}
    if missing:
        s.patch(story["id"], missing)


def build_shops(s):
    """Each shopkeeper's wares, as the file says (whole, so a dropped line goes), keeping what play has done to
    stock. Runs again without change."""
    have = by_name(s)
    for name, sells in SHOP_SELLS.items():
        p = have.get(name)
        if p is None:
            continue
        cur = p["state"].get("sells") or {}
        want = {k: dict(v) for k, v in sells.items()}
        if {k: {kk: vv for kk, vv in v.items() if kk != "stock"} for k, v in cur.items()} != want:
            s.patch(p["id"], {"sells": None})
            s.patch(p["id"], {"sells": want})


def build(s):
    root = s.summary()["root"]
    if s.summary()["t"] < START and "Newcomer" not in by_name(s):
        s.clock(step=START - s.summary()["t"])  # a fresh world: nothing lives yet, so the hours pass for free
    s.world.set_pace({"thirst": 3600})
    if "places" in STAGES:
        build_places(s, root)
    if "layout" in STAGES:
        build_layout(s)
    if "people" in STAGES:
        build_people(s)
    if "things" in STAGES:
        build_things(s)
    if "wiring" in STAGES:
        build_wiring(s, root)
    if "cast" in STAGES:
        build_cast(s, root)
        build_news(s)
        build_faith(s)
    if "magistrate" in STAGES:
        build_magistrate(s, root)
    if "five_e" in STAGES:
        build_five_e(s)
    if "statblocks" in STAGES:
        build_statblocks(s)
    if "hire" in STAGES:
        build_hire(s, root)
    if "glance" in STAGES:
        build_glance(s, root)
    if "peril" in STAGES:
        build_peril(s, root)
    if "missions" in STAGES:
        build_missions(s, root)
    if "shops" in STAGES:
        build_shops(s)
        build_players(s)
    if "law" in STAGES:
        build_law(s)
    if "undertaker" in STAGES:
        build_undertaker(s, root)
    if "healers" in STAGES:
        build_healers(s, root)
    if "writing" in STAGES:
        build_writing(s)
    if "animals" in STAGES:
        build_animals(s, root)
    mend_stale(s)
    s.clock(run=False, turn=30)
    return s.summary()


def populate(s):
    """Places, people, things, rules and the clock, into the world the session points at."""
    return build(s)


def upgrade(s):
    """Bring a world built from an older version of this file up to this one: every stage adds only what is missing,
    by name, so it runs twice without change. People and things are made once, ever (the town keeps the list), so
    what play burned, ate or killed is not remade."""
    return build(s)
