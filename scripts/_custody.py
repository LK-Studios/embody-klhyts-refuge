# Custody (the owner, 2026-11-23: "Surrender should mean surrender. And you are taken to prison."). A player's
# character yielded to two of the Fist and was beaten to death anyway (flaw-26b070): a yield the engine accepted
# stopped only the one yielded to, and only until the next yield. Used by scripts/peril_rule.py after use("peril").
#
# A yield to someone who takes prisoners (the Fist, the Throne's people, the watch) while they are pressing you (you
# are marked or wanted, or you are in their fight) is a surrender. The fight is over for you; your weapons and any
# paper against the Custodian go into the evidence chest in the Town Hall; the Fist's word on you is satisfied and the
# Throne's warrant served; and you are put in the cells under the Hall. Six world hours later the watch lets you out
# with your weapons (papers stay with the Throne). Five gold bail, paid to Sergeant Harrow, lets you out sooner.
#
# Breaking someone out (the owner, 2026-11-23: "We gonna need rules to break someone out of prison"). The cell door is
# barred, and the bar's padlock has one key, which Constable Rosa Quint carries. The ways through it:
# - the key: two gold to Rosa while someone is held, and she presses it into your hand and goes off to the market for
#   a quarter of an hour (she takes small bribes: the cast says so); or take it off her by `search` when she is down
#   or asleep;
# - pick the padlock (DC 18, ten quiet minutes) or break the bar (DC 20, two loud ones), from the Hall or the cell.
# Whoever works the door where the watch or the Throne's officers can see it is wanted for it and fought on the spot;
# a break is heard next door, and they come. A prisoner caught at it from inside gets another hour. A prisoner out of
# the cells by any of these is wanted for the escape. With nobody held, the watch fit a new bar if it was broken, and
# change the padlock if the key has left their hands.

SENTENCE = 21600
BAIL = 500
WATCH = ["Sergeant Pell Harrow", "Constable Abel Fitch", "Constable Rosa Quint"]
BAILERS = ["Sergeant Pell Harrow"]
CELLS = "The Cells"
CHEST = "Evidence chest"
PAPERS = ["letter", "passage", "tally"]
DOOR = "Cell door"
BAR = "Cell bar"
KEY = "Cell key"
KEEPER = "Constable Rosa Quint"
LOOK_AWAY = 200
LOOK_FOR = 900
BREAK_KINDS = ["unlocked", "lock_picked", "pick_failed", "lock_broken", "break_failed"]
LOUD = ["lock_broken", "break_failed"]
EXTRA = 3600

def place_called(ctx, name):
    for p in ctx.find(type="place", name=name, limit=3):
        if p.name == name:
            return p
    return None

def chest_in(ctx, hall):
    for c in ctx.children(hall):
        if c.name == CHEST:
            return c
    return None

def takes_prisoners(ctx, st, p):
    if p is None or p.state.dead or p.state.down or ctx.embodied(p):
        return False
    return (p.state.faction in [FIST, THRONE] or p.name in THRONE_MEN or p.name in WATCH
            or p.id in (st.magistrate_guards or []))

def pressing(ctx, st, who, captor):
    if step_of(st, who) == "marked" or who.id in (st.wanted or []):
        return True
    return who.state.fight is not None and who.state.fight == captor.state.fight

def surrender(ctx, s, who, captor):
    st = s.state
    if who is None or who.state.dead or who.state.jailed or not ctx.embodied(who):
        return False
    if not takes_prisoners(ctx, st, captor) or not pressing(ctx, st, who, captor):
        return False
    cells = place_called(ctx, CELLS)
    hall = ctx.get(st.hall) if st.hall else None
    if cells is None or hall is None or who.parent is None:
        return False
    here = who.parent
    for hid in list((st.hunts or {}).keys()):
        rec = (the_story(ctx).state.hunts or {}).get(hid)
        if rec and rec.get("target") == who.id:
            end_hunt(ctx, hid)
    set_step(ctx, who, "jailed")
    ctx.patch(the_story(ctx), {"heat": {who.id: WARN_AT - 1}})
    if who.id in (st.wanted or []):
        throne = faction_called(ctx, THRONE)
        if throne is not None:
            pardon_of(ctx, throne, who)
        ctx.patch(the_story(ctx), {"wanted": [x for x in (st.wanted or []) if x != who.id]})
    chest = chest_in(ctx, hall)
    taken = []
    for it in ctx.children(who):
        if it.state.weapon or it.state.clue in PAPERS:
            ctx.move(it, chest if chest is not None else hall)
            ctx.patch(it, {"taken_from": who.id})
            taken.append(it.name)
    took = (" " + cap1(look_of(captor, "the one you yielded to")) + " takes your " + ", ".join(taken).lower() + ".") if taken else ""
    ctx.emit("scene", target=here.id, reach=1, text=cap1(look_of(captor, "the one you yielded to")) + " takes the "
             "surrender. Your hands are tied behind you with your own belt." + took + " Then you are marched out, up "
             "the hill to the Town Hall and down a stair behind it, and nobody in the street meets your eye.")
    ctx.move(who, cells)
    ctx.patch(who, {"jailed": {"by": captor.id, "since": ctx.t, "until": ctx.t + SENTENCE}, "yielded": None})
    ctx.patch(the_story(ctx), {"jailed": {who.id: ctx.t + SENTENCE}})
    ctx.emit("arrived", target=cells.id, reach=-1, who=who.id, place=cells.id)
    ctx.emit("scene", target=who.id, reach=0, text="The cell door shuts behind you and a bar drops across it on the far "
             "side. Stone, straw, a bucket of water, and a slit of a window at street height. The watch keeps the key. "
             "Six hours, the constable says through the grille, or five gold bail to the sergeant from a friend.")
    if captor.parent is not None and captor.parent.id != hall.id:
        go_one(ctx, captor, hall)
    ctx.patch(captor, {"routine_hold_until": ctx.t + 1800})
    return True

def release(ctx, s, who, why):
    st = s.state
    hall = ctx.get(st.hall) if st.hall else None
    ctx.patch(the_story(ctx), {"jailed": {who.id: None}, "bail_paid": {who.id: None}})
    ctx.patch(who, {"jailed": None})
    set_step(ctx, who, "served")
    if hall is None or who.state.dead:
        return
    chest = chest_in(ctx, hall)
    back = []
    for it in (ctx.children(chest) if chest is not None else []):
        if it.state.taken_from == who.id and it.state.weapon:
            ctx.move(it, who)
            ctx.patch(it, {"taken_from": None})
            back.append(it.name)
    ctx.move(who, hall)
    ctx.emit("arrived", target=hall.id, reach=-1, who=who.id, place=hall.id)
    line = ("The bar lifts. A constable who leans on things swings the cell door open. \"Out you get, love. " + why + "\"")
    if back:
        line = line + " Your " + ", ".join(back).lower() + " are handed back across the desk. The papers stay with the Throne."
    ctx.emit("scene", target=who.id, reach=0, text=line)

def check_jail(ctx, s):
    cells = place_called(ctx, CELLS)
    st = s.state
    for pid in list((st.jailed or {}).keys()):
        until = (the_story(ctx).state.jailed or {}).get(pid)
        if until is None:
            continue
        who = ctx.get(pid)
        if who is None or who.state.dead:
            ctx.patch(the_story(ctx), {"jailed": {pid: None}})
            continue
        if cells is not None and (who.parent is None or who.parent.id != cells.id):
            # out by their own hand (a picked or broken door): the Throne wants them for it
            ctx.patch(the_story(ctx), {"jailed": {pid: None}})
            ctx.patch(who, {"jailed": None})
            set_step(ctx, who, "escaped")
            warrant(ctx, who, "escape from the Throne's cells")
            for bar in ctx.find(type="lock", name="Cell bar", limit=2):  # the watch drops the bar again, if it holds
                if not bar.state.broken and not bar.state.locked:
                    ctx.patch(bar, {"locked": True})
            continue
        if ctx.t >= float(until):
            release(ctx, s, who, "Your time's served. Don't come back.")

def held_ids(st):
    return [pid for pid, u in (st.jailed or {}).items() if u is not None]

def the_bar(ctx):
    for b in ctx.find(type="lock", name=BAR, limit=3):
        if b.name == BAR:
            return b
    return None

def is_watch(ctx, st, p):
    return p is not None and (p.name in WATCH or p.name in THRONE_MEN or p.id in (st.magistrate_guards or []))

def watchers(ctx, st, place):
    # the watch and the Throne's officers here, on their feet and nobody's puppet, and not paid to be elsewhere
    out = []
    if place is None:
        return out
    away = ctx.t < float(st.looking_away_until or 0)
    for p in ctx.children(place, "person"):
        if not is_watch(ctx, st, p) or not free_hand(ctx, p):
            continue
        if away and p.name == KEEPER:
            continue
        out.append(p)
    return out

def at_the_door(ctx, s, event, p):
    # someone works the cell door: a key, picks, or a crowbar. Seen, they answer for it
    door = ctx.get(event.target) if event.target else None
    by = ctx.get(p.get("by")) if p.get("by") else None
    st = s.state
    if door is None or door.name != DOOR or by is None or by.state.dead or is_watch(ctx, st, by):
        return
    hall = door.parent
    cells = place_called(ctx, CELLS)
    if hall is None or by.parent is None:
        return
    seen = watchers(ctx, st, hall)
    if event.kind in LOUD and not seen:
        # a bar being beaten off its brackets is heard next door: the watch come running
        for e in ctx.edges(hall, "connects_to", "out"):
            nb = ctx.get(e["target"])
            if nb is None or (cells is not None and nb.id == cells.id):
                continue
            for w in watchers(ctx, st, nb):
                go_one(ctx, w, hall)
                ctx.patch(w, {"routine_hold_until": ctx.t + 1800})
                seen.append(w)
    if not seen:
        return
    w = seen[0]
    if cells is not None and by.parent.id == cells.id:
        # the prisoner, at it from inside: the bar goes back (a new one if it broke) and the time goes up
        bar = the_bar(ctx)
        if bar is not None:
            ctx.patch(bar, {"locked": True, "broken": False})
        until = (st.jailed or {}).get(by.id)
        if until is not None:
            ctx.patch(the_story(ctx), {"jailed": {by.id: float(until) + EXTRA}})
            ctx.patch(by, {"jailed": {"until": float(until) + EXTRA}})
        ctx.emit("scene", target=cells.id, reach=1, text=cap1(look_of(w, "the watch")) + " bangs on the door with a "
                 "fist. \"I heard that. Another hour, for the noise.\" Something heavy drops across the door on the "
                 "far side.")
        return
    if by.parent.id != hall.id:
        return
    ctx.emit("scene", target=hall.id, reach=1, text=cap1(look_of(w, "the watch")) + " sees what is being done to the "
             "cell door. \"Oi! In the name of the Refuge!\"")
    warrant(ctx, by, "breaking into the Throne's cells")
    for x in seen:
        if not by.state.dead and not by.state.down:
            strike_first(ctx, x, by)

def look_away(ctx, s, event, p):
    # two gold to Rosa while someone is held: the key, and a quarter of an hour at the market
    t = ctx.get(event.target) if event.target else None
    item = ctx.get(p.get("item")) if p.get("item") else None
    by = ctx.get(p.get("by")) if p.get("by") else None
    st = s.state
    if t is None or item is None or by is None or t.name != KEEPER or not held_ids(st):
        return False
    kind = ctx.root().state.coin_kind or "coin"
    if item.state.kind != kind:
        return False
    paid = int((st.look_paid or {}).get(by.id) or 0) + ctx.count(item)
    ctx.patch(the_story(ctx), {"look_paid": {by.id: paid}})
    if paid < LOOK_AWAY:
        ctx.emit("scene", target=t.parent.id, reach=1, text=cap1(look_of(t, "the watchwoman")) + " pockets it. "
                 "\"Between you and me, love, that's a mango. Two gold's a long walk.\"")
        return True
    bar = the_bar(ctx)
    key = ctx.get(bar.state.key) if bar is not None and bar.state.key else None
    ctx.patch(the_story(ctx), {"look_paid": {by.id: None}, "looking_away_until": ctx.t + LOOK_FOR})
    if key is not None and key.parent is not None and key.parent.id == t.id:
        ctx.move(key, by)
        ctx.emit("scene", target=by.id, reach=0, text=cap1(look_of(t, "the watchwoman")) + " shakes your hand, and "
                 "something cold and iron is left in it. \"I didn't see nothing,\" she says, \"and I'll be not seeing "
                 "it at the market for a quarter of an hour.\"")
    else:
        ctx.emit("scene", target=by.id, reach=0, text=cap1(look_of(t, "the watchwoman")) + " pockets it. \"Key's not "
                 "on me, love, more's the pity. But I'll be at the market for a quarter of an hour, not seeing nothing.\"")
    market = ctx.get(st.market) if st.market else None
    if market is not None and t.parent is not None and t.parent.id != market.id:
        go_one(ctx, t, market)
    ctx.patch(t, {"routine_hold_until": ctx.t + LOOK_FOR})
    return True

def mind_the_cells(ctx, s):
    # with nobody held: a broken bar is replaced, and a key out of the watch's hands means a new padlock
    if held_ids(s.state):
        return
    bar = the_bar(ctx)
    if bar is None:
        return
    if bar.state.broken or not bar.state.locked:
        ctx.patch(bar, {"broken": False, "locked": True})
    key = ctx.get(bar.state.key) if bar.state.key else None
    holder = key.parent if key is not None else None
    if holder is not None and is_watch(ctx, s.state, holder) and not holder.state.dead:
        return
    keeper = None
    for n in [KEEPER] + WATCH:
        k = body_named(ctx, n)
        if k is not None and not k.state.dead:
            keeper = k
            break
    if keeper is None:
        return
    new = ctx.spawn("thing", keeper, name=KEY, state={"portable": True, "bulk": 0, "description": "A heavy iron key on "
                    "a loop of string: the padlock on the cell bar under the Town Hall."})
    ctx.patch(bar, {"key": new.id})

def bail(ctx, s, event, p):
    # five gold, given to the watch, lets out whoever has been held longest
    t = ctx.get(event.target) if event.target else None
    item = ctx.get(p.get("item")) if p.get("item") else None
    st = s.state
    if t is None or item is None or t.name not in BAILERS or not st.jailed:
        return False
    kind = ctx.root().state.coin_kind or "coin"
    if item.state.kind != kind:
        return False
    held = [pid for pid in st.jailed if (st.jailed or {}).get(pid) is not None]
    if not held:
        return False
    first = held[0]
    paid = int((st.bail_paid or {}).get(first) or 0) + ctx.count(item)
    ctx.patch(the_story(ctx), {"bail_paid": {first: paid}})
    who = ctx.get(first)
    if paid < BAIL or who is None:
        ctx.emit("scene", target=t.parent.id, reach=1, text=cap1(look_of(t, "the watch")) + " counts it. \"That's a start "
                 "on the bail, love. It's five gold.\"")
        return True
    release(ctx, s, who, "Somebody's paid your bail. Mind how you go.")
    ctx.emit("scene", target=t.parent.id, reach=1, text=cap1(look_of(t, "the watch")) + " counts it, pockets it, and "
             "goes down the stair with the key.")
    return True
