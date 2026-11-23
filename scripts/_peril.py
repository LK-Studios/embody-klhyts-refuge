# Peril, shared by the peril rule (scripts/peril_rule.py), the story, the warehouse guard and the orders verb. The
# owner, 2026-11-23: "I don't feel like the antagonists are really antangoist enough. I have not ecounttered them being
# anything but passive. And it has made every mission too easy. We need more peril!" Asked, the owner picked "Full 5e,
# to the death" (the Fist and the Throne fight to kill: `finishes` on their people) and "World first, minds after"
# (the villains act with nobody running them; minds may run Dominico and the Custodian later, with the orders verb).
#
# Heat is what Dominico's people have heard about someone a player holds, kept on the Story (`heat`). At 3 one of the
# Fennicks tails them; at 5 Sabeth Crane finds them and warns them; at 8 the Fist marks them (on the Story, never the
# faction's outlaw list, whose fighters strike on sight whether anyone is playing or not) and two of Dominico's men
# (three past 12) hunt them to the death, a hop a tick, with a fight on sight. Five gold in coin to any of the Fist buys
# the word back. Hunters move only while someone plays their mark and is at it (a body
# left alone, or held by a human who has gone quiet, is never murdered in its sleep), and never set foot in the
# Stripperwitch (Fat Gog's house) or aboard the Moonmoth: they wait outside. The Throne's warrant is the Custodian's: Vorkathia outlaws someone, and the officer and the constable
# he pays attack them on sight (they do not chase).

use("common")
use("five")

FIST = "the Fist"
THRONE = "Vorkathia"
HOT_WORDS = ["klhyt", "crate", "warehouse", "custodian", "dominico", "mayor", "skim", "skimming", "dues", "brask",
             "tally", "ledger", "books"]
TAIL_AT = 3
WARN_AT = 5
MARK_AT = 8
MARK_DEPTH = -8
TRIBUTE = 500  # copper, in coin, to any of the Fist: the word is taken back
TALK_GAP = 300
TAIL_FOR = 1800
WARN_FOR = 3600
HOLD = 600
WAVE_GAP = 21600
ACTIVE = 1800
TAILS = ["Ott Fennick", "Jory Fennick"]
WARNER = "Sabeth Crane"
FIST_MEN = ["Ott Fennick", "Jory Fennick", "Tully", "Brask", "Sabeth Crane"]
THRONE_MEN = ["Lieutenant Voss", "Constable Rosa Quint"]

def the_story(ctx):
    found = ctx.find(type="story", limit=1)
    return found[0] if found else None

def cap1(t):
    t = str(t)
    return t[:1].upper() + t[1:]

def look_of(e, fallback):
    # how a stranger would point them out: never a name
    return (e.state.seen_as if e is not None else None) or fallback

def faction_called(ctx, name):
    for f in ctx.find(type="faction", limit=20):
        if f.name == name:
            return f
    return None

def body_named(ctx, name):
    for p in ctx.find(type="person", name=name, limit=5):
        if p.name == name:
            return p
    return None

def free_hand(ctx, p):
    # a body the story may send: standing, nobody playing it, in nobody's hire, not tied, following no one, not in irons
    if p is None or p.parent is None:
        return False
    st = p.state
    if st.dead or st.down or st.bound or st.in_irons or st.hired or st.follows or st.asleep:
        return False
    return not ctx.embodied(p)

def playing(ctx, who):
    # someone plays them and is at it: their seat did something within the last ACTIVE world seconds. A seat whose
    # human has gone (held, but quiet) is not hunted, or the Fist would murder sleepers
    q = ctx.quiet(who)
    return q is not None and q < ACTIVE

def sanctuary(st, place_id):
    return place_id is not None and place_id in [st.stripperwitch, st.moonmoth]

def ears_at(ctx, st, place):
    # Dominico's informants drink at the Omberhulk, his muscle at the Ogre, and he sits at the Apothecary; anywhere
    # else the walls have ears only when one of the Fist stands in the room
    if place is None:
        return False
    if place.id in [st.omberhulk, st.ogre, st.apothecary]:
        return True
    for p in ctx.children(place, "person"):
        if p.state.faction == FIST and not p.state.dead and not ctx.embodied(p):
            return True
    return False

def hot(text):
    t = " " + str(text).lower() + " "
    for ch in [",", ".", "?", "!", ";", ":", "'", "\"", "(", ")"]:
        t = t.replace(ch, " ")
    for w in HOT_WORDS:
        if " " + w + " " in t or " " + w + "s " in t:
            return True
    return False

def heat_of(st, who):
    return int((st.heat or {}).get(who.id) or 0)

def add_heat(ctx, who, n, why, played=True):
    # the Fist hears something about someone; the steps follow from where it lands. `played`: only while someone
    # plays them (a deed seen); a word that reaches Dominico later (Brask talks) counts either way
    s = the_story(ctx)
    if s is None or who is None or who.state.dead or (played and not ctx.embodied(who)):
        return 0
    h = heat_of(s.state, who) + int(n)
    ctx.patch(s, {"heat": {who.id: h}})
    climb(ctx, who, h, why)
    return h

def talk_heat(ctx, who, text, place):
    # a hot word where the Fist has ears: at most one a TALK_GAP
    s = the_story(ctx)
    if s is None or who is None or not ctx.embodied(who) or not hot(text) or not ears_at(ctx, s.state, place):
        return 0
    last = float((s.state.heat_t or {}).get(who.id) or -1000000)
    if ctx.t - last < TALK_GAP:
        return 0
    ctx.patch(s, {"heat_t": {who.id: ctx.t}})
    return add_heat(ctx, who, 1, "asking about the crate where the Fist could hear")

def step_of(st, who):
    return (st.peril_step or {}).get(who.id)

def set_step(ctx, who, step):
    ctx.patch(the_story(ctx), {"peril_step": {who.id: step}})

def climb(ctx, who, h, why):
    st = the_story(ctx).state
    at = step_of(st, who)
    if h >= MARK_AT:
        if at != "marked":
            mark(ctx, who, why)
        return
    if h >= WARN_AT and at in [None, "tailed"]:
        send_warning(ctx, who)
        set_step(ctx, who, "warned")
    elif h >= TAIL_AT and at is None:
        send_tail(ctx, who)
        set_step(ctx, who, "tailed")

def outlaw(ctx, faction, who):
    # the faction wants them, quietly and deep: kept in its own secret count, so no event names it
    cur = standing(ctx, who, faction)
    if cur > MARK_DEPTH:
        unseen = dict(faction.state.unseen or {})
        unseen[who.id] = int(unseen.get(who.id) or 0) + (MARK_DEPTH - cur)
        keep_secret(ctx, faction, {"unseen": unseen})
    if not (faction.state.hostile or {}).get(who.id):
        ctx.patch(faction, {"hostile": {who.id: True}})

def pardon_of(ctx, faction, who):
    # back to just short of outlawed (a gift or two from friends), no longer hunted
    cur = standing(ctx, who, faction)
    if cur < -3:
        unseen = dict(faction.state.unseen or {})
        unseen[who.id] = int(unseen.get(who.id) or 0) + (-3 - cur)
        keep_secret(ctx, faction, {"unseen": unseen})
    if (faction.state.hostile or {}).get(who.id):
        ctx.patch(faction, {"hostile": {who.id: None}})

def fist_gone(ctx, st):
    dom = ctx.get(st.dominico) if st.dominico else None
    return dom is None or dom.state.dead or dom.state.in_irons

def mark(ctx, who, why):
    # the Fist marks them: no new marks once Dominico is dead or in irons, there being nobody to give the word
    s = the_story(ctx)
    st = s.state
    fist = faction_called(ctx, FIST)
    if fist is None or who is None or who.state.dead or fist_gone(ctx, st):
        return False
    set_step(ctx, who, "marked")
    ctx.patch(s, {"marked_for": {who.id: why}})
    dom = ctx.get(st.dominico)
    ctx.remember(dom, who.name + " has crossed the Fist (" + why + "). Sabeth has the word out: they are to be found.")
    # one of the Fist in their hire is found out, and is finished with Dominico
    for p in ctx.find(type="person", limit=500):
        if p.state.faction == FIST and (p.state.hired or {}).get("by") == who.id and not p.state.dead:
            ctx.patch(p, {"faction": None, "left_the_fist": True})
            ctx.emit("scene", target=who.id, reach=0, text=cap1(look_of(p, "the man you hired")) + " has gone grey under "
                     "the colour. \"Word's out on you,\" he says quietly. \"Which means it's out on me. That's me finished "
                     "with Mister Dominico, then. Or him with me.\"")
    return True

def is_hunting(st, hid):
    return bool((st.hunts or {}).get(hid))

def hunt_for(ctx, h, target, mode, until):
    ctx.patch(the_story(ctx), {"hunts": {h.id: {"target": target.id, "mode": mode, "until": until, "seen": [],
                                                 "sprung": False}}})
    ctx.patch(h, {"routine_hold_until": ctx.t + HOLD})

def end_hunt(ctx, hid):
    ctx.patch(the_story(ctx), {"hunts": {hid: None}})
    h = ctx.get(hid)
    if h is not None and not h.state.dead:
        ctx.patch(h, {"routine_hold_until": None, "routine_key": None})

def send_tail(ctx, who):
    for name in TAILS:
        p = body_named(ctx, name)
        if free_hand(ctx, p) and not is_hunting(the_story(ctx).state, p.id):
            hunt_for(ctx, p, who, "tail", ctx.t + TAIL_FOR)
            return p
    return None

def send_warning(ctx, who):
    st = the_story(ctx).state
    names = [WARNER] + TAILS
    for name in names:
        p = body_named(ctx, name)
        if p is None or not free_hand(ctx, p):
            continue
        rec = (st.hunts or {}).get(p.id)
        if rec and rec.get("target") != who.id:
            continue
        hunt_for(ctx, p, who, "warn", ctx.t + WARN_FOR)
        return p
    return None

def brask_on_door(ctx, st, p):
    # Brask is minding the warehouse while Klhyt is still in it: the door is his whole job
    if p is None or p.id != st.brask or p.state.left_post or p.state.off_post:
        return False
    return not st.klhyt_freed and not st.shipped

def dispatch(ctx, tgt):
    # a wave of hunters for someone marked, while someone plays them: two of the Fist (three past heat 12)
    s = the_story(ctx)
    st = s.state
    for hid in (st.hunts or {}):
        rec = (st.hunts or {}).get(hid)
        if rec and rec.get("target") == tgt.id and rec.get("mode") == "kill":
            return []
    if ctx.t < float((st.next_wave or {}).get(tgt.id) or 0):
        return []
    n = 3 if heat_of(st, tgt) >= 12 else 2
    sent = []
    for name in FIST_MEN:
        if len(sent) >= n:
            break
        p = body_named(ctx, name)
        if not free_hand(ctx, p) or is_hunting(the_story(ctx).state, p.id) or brask_on_door(ctx, st, p):
            continue
        hunt_for(ctx, p, tgt, "kill", None)
        sent.append(p)
    if sent:
        ctx.patch(s, {"next_wave": {tgt.id: ctx.t + WAVE_GAP}})
    return sent

def go_one(ctx, h, place):
    ctx.move(h, place)
    ctx.patch(h, {"post": place.id})
    ctx.emit("arrived", target=place.id, reach=-1, who=h.id, place=place.id)

def step_toward(ctx, st, h, dest):
    # one hop nearer, never into a sanctuary, never down a path they do not know
    here = h.parent
    if here is None or dest is None:
        return False
    far = ctx.ways(here, dest, 12)
    best = None
    bd = None
    for e in ctx.edges(here, "connects_to", "out"):
        nb = ctx.get(e["target"])
        if nb is None or sanctuary(st, nb.id):
            continue
        if nb.state.hidden and not ctx.knows_way(h, nb):
            continue
        if nb.id == dest.id:
            best = nb
            bd = 0
            break
        d = ctx.ways(nb, dest, 12)
        if d is None:
            continue
        if bd is None or d < bd:
            best = nb
            bd = d
    if best is None or (far is not None and bd is not None and bd >= far):
        return False
    go_one(ctx, h, best)
    return True

def strike_first(ctx, h, tgt):
    # what d20's fighters do on sight: the first hostile deed here starts the fight, and their turn is taken at once
    place = h.parent
    if my_fight(ctx, h) is not None:
        mark_foes(ctx, h, tgt)  # in the fight already: this one is its foe too
        return None
    f = start_fight(ctx, place, h, tgt)
    if f is not None and f.state.turn_of == h.id:
        npc_turn(ctx, f, h)
        schedule_next(ctx, f, "done")
    return f

def tell_mission(ctx, key, ids):
    # one of Fat Gog's missions is done by these: scripts/missions_rule.py pays it (this file and the scripts that use
    # it never include the jobs pack, whose `pay` would shadow the 5e pack's)
    ids = [i for i in (ids or []) if i]
    if ids:
        ctx.emit("mission_done", target=ctx.root().id, reach=0, key=key, who=ids)

def mission_holders(ctx, key):
    for j in ctx.find(type="job", limit=200):
        if j.state.mission == key:
            hs = j.state.holders or {}
            return [h for h in hs if hs.get(h) is not None]
    return []

def warrant(ctx, who, crime):
    # the Throne's warrant: Vorkathia outlaws them, a notice goes up on the square, describing them as a stranger would
    s = the_story(ctx)
    st = s.state
    throne = faction_called(ctx, THRONE)
    if throne is None or who is None or who.state.dead:
        return False
    outlaw(ctx, throne, who)
    if who.id not in (st.wanted or []):
        ctx.patch(s, {"wanted": list(st.wanted or []) + [who.id]})
    looks = str(who.state.look or who.state.description or "a stranger off the boats").strip()
    if len(looks) > 240:
        looks = looks[:240].rsplit(" ", 1)[0] + "..."
    people = who.state.people or "stranger"
    text = ("WANTED, by commission of the Throne of Vorkath, for " + crime + ": one " + str(people) + ". " + looks
            + " Ten gold to whoever brings them to the Town Hall. The Throne does not ask in what condition.")
    ctx.spawn("letter", st.square, name="A WANTED notice", state={
        "portable": False, "bulk": 0, "text": text, "wanted": who.id,
        "description": "A fresh notice nailed over the notice board, the octogram at its head and a red seal at its foot. "
                       "Under the seal, in a clerk's hand: WANTED."})
    ctx.emit("scene", target=st.square, reach=1, text="Before dawn a constable comes down the Town Hall steps with a "
             "hammer and a paper, and nails it over the notice board. The octogram is at its head.")
    cust = ctx.get(st.custodian) if st.custodian else None
    if cust is not None:
        ctx.remember(cust, "Posted the Throne's warrant on " + who.name + " for " + crime + ".")
    return True
