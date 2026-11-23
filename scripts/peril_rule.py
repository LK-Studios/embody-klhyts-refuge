# The peril rule, on the root (scripts/_peril.py has the why). It hears talk where the Fist has ears, blows on the
# Fist, the Fist coming to the warehouse after Brask leaves it, and Brask talking; and every 30 world seconds
# (`peril_tick`) it moves the hunts on: a tail shows itself, a warning is delivered, a hunter takes one hop toward their
# mark and fights on sight. It also keeps the Custodian's nights until the magistrate's verdict: at two in the morning,
# once a world day, the Throne's warrant on whoever freed Klhyt, then Lieutenant Voss and Constable Rosa Quint calling
# on the witnesses the town has found, one a night.

use("peril")
use("custody")

WITNESS_KEYS = ["teague", "tully"]  # River is under Fat Gog's roof, where the Throne does not go
NIGHT_FROM = 2.0
NIGHT_TO = 5.0
BEAT = 20  # world seconds between hunters showing themselves and striking: the next tick

def hour_of(ctx):
    d = ctx.day_seconds()
    return ((ctx.t % d) / d) * 24.0, int(ctx.t // d)

def on(ctx, event):
    k = event.kind
    p = event.payload or {}
    s = the_story(ctx)
    if s is None:
        return
    if k == "peril_tick":
        tick(ctx, s)
    elif k == "talked":
        who = ctx.get(event.actor) if event.actor else None
        if who is not None and who.parent is not None:
            talk_heat(ctx, who, p.get("about", ""), who.parent)
    elif k == "say":
        who = ctx.get(event.actor) if event.actor else None
        if who is not None and who.parent is not None:
            talk_heat(ctx, who, p.get("text", ""), who.parent)
    elif k == "hit":
        t = ctx.get(event.target) if event.target else None
        by = ctx.get(p.get("by")) if p.get("by") else None
        if t is not None and by is not None and t.state.faction == FIST and by.state.faction != FIST:
            add_heat(ctx, by, 3, "struck one of the Fist")
    elif k == "given":
        if not bail(ctx, s, event, p) and not look_away(ctx, s, event, p):
            tribute(ctx, s, event, p)
    elif k in BREAK_KINDS:
        at_the_door(ctx, s, event, p)
    elif k == "yielded":
        # a surrender to someone who takes prisoners, while they press you: the cells (scripts/_custody.py)
        who = ctx.get(event.target) if event.target else None
        captor = ctx.get(p.get("to")) if p.get("to") else None
        surrender(ctx, s, who, captor)
    elif k == "fist_answers":
        fist_answers(ctx, s, p)
    elif k == "brask_talks":
        who = ctx.get(p.get("by")) if p.get("by") else None
        add_heat(ctx, who, 3, "paid Brask off his door", False)
    elif k == "doctor_tells":
        doctor_tells(ctx, s, p)

def doctor_tells(ctx, s, p):
    # Doctor Prewitt mends anyone, and writes it all down: a patient the Throne wants is in the watch's hands ten world
    # minutes after he has paid (scripts/healing_rule.py). The officers come to the surgery door; whoever is still
    # there is seen, and the warrant does the rest
    who = ctx.get(p.get("who")) if p.get("who") else None
    place = ctx.get(p.get("at")) if p.get("at") else None
    if who is None or place is None or who.state.dead or who.id not in (s.state.wanted or []):
        return
    men = [m for m in [body_named(ctx, n) for n in THRONE_MEN] if free_hand(ctx, m)]
    if not men:
        return
    for m in men:
        if m.parent is None or m.parent.id != place.id:
            go_one(ctx, m, place)
        ctx.patch(m, {"routine_hold_until": ctx.t + 1800})
    looks = [look_of(m, "an officer of the Throne") for m in men]
    ctx.emit("scene", target=place.id, reach=1, text=cap1(looks[0] if len(looks) == 1 else " and ".join(looks))
             + (" comes" if len(men) == 1 else " come") + " to the surgery door with a paper. The doctor does not look "
             "up from his basin. He only lifts a wet hand and points.")
    throne_sight(ctx, the_story(ctx))

def tribute(ctx, s, event, p):
    # five gold in coin, to any of the Fist, from someone they have marked: the word is taken back
    t = ctx.get(event.target) if event.target else None
    by = ctx.get(p.get("by")) if p.get("by") else None
    item = ctx.get(p.get("item")) if p.get("item") else None
    if t is None or by is None or item is None or t.state.faction != FIST or step_of(s.state, by) != "marked":
        return
    kind = ctx.root().state.coin_kind or "coin"
    if item.state.kind != kind:
        return
    paid = int((s.state.tribute or {}).get(by.id) or 0) + ctx.count(item)
    ctx.patch(s, {"tribute": {by.id: paid}})
    if paid < TRIBUTE:
        ctx.emit("scene", target=t.parent.id, reach=1, text=cap1(look_of(t, "the man in the black armband")) + " weighs "
                 "it, and pockets it, and does not say thank you. \"It's a start.\"")
        return
    set_step(ctx, by, "paid")
    ctx.patch(s, {"heat": {by.id: WARN_AT - 1}})
    for hid in list((s.state.hunts or {}).keys()):
        rec = (the_story(ctx).state.hunts or {}).get(hid)
        if rec and rec.get("target") == by.id:
            end_hunt(ctx, hid)
    ctx.emit("scene", target=t.parent.id, reach=1, text=cap1(look_of(t, "the man in the black armband")) + " counts it, "
             "twice. \"I'll tell Sabeth you've paid,\" comes the answer at last. \"Don't make her write your name "
             "down again.\"")
    dom = ctx.get(s.state.dominico) if s.state.dominico else None
    if dom is not None:
        ctx.remember(dom, by.name + " paid the Fist five gold. The word on them is taken back.")

def tick(ctx, s):
    st = s.state
    if st.jailed:
        check_jail(ctx, s)
    mind_the_cells(ctx, the_story(ctx))
    h, day = hour_of(ctx)
    if st.custodian_exposed and not st.verdict and NIGHT_FROM <= h < NIGHT_TO and st.throne_day != day:
        throne_night(ctx, s, day)
    if st.custodian_exposed and not st.verdict and 10.0 <= h < 10.5 and st.steps_day != day:
        on_the_steps(ctx, s, day)
    want = st.dominico_wants
    if want and ctx.t > float(want.get("until") or 0):
        ctx.patch(s, {"dominico_wants": None})
        who = ctx.get(want.get("by"))
        if who is not None and not who.state.dead:
            ctx.patch(s, {"heat": {who.id: max(heat_of(the_story(ctx).state, who), MARK_AT)}})
            mark(ctx, who, "kept a paper Dominico asked for")
    for pid in list((st.peril_step or {}).keys()):
        if (the_story(ctx).state.peril_step or {}).get(pid) != "marked":
            continue
        tgt = ctx.get(pid)
        if tgt is not None and not tgt.state.dead and playing(ctx, tgt):
            dispatch(ctx, tgt)
    hunts = the_story(ctx).state.hunts or {}
    for hid in list(hunts.keys()):
        rec = (the_story(ctx).state.hunts or {}).get(hid)
        if rec:
            run_hunt(ctx, hid, rec)
    throne_sight(ctx, the_story(ctx))

def on_the_steps(ctx, s, day):
    # ten in the morning: the Custodian reads the Throne's proclamation from the Town Hall steps, and whoever stands in
    # the square with Klhyt is seen to (Klhyt's "The steps at ten")
    st = s.state
    ctx.patch(s, {"steps_day": day})
    there = [x for x in ctx.children(st.square, "person") if ctx.embodied(x)]
    if not there:
        return
    ctx.emit("scene", target=st.square, reach=1, text="At ten the Town Hall door opens, and the thin man in the grey "
             "coat reads the Throne's proclamation from the top step in a voice that carries. This morning he reads it "
             "to faces that do not look away, and he reads it faster than he meant to.")
    tell_mission(ctx, "steps", [x.id for x in there])

def run_hunt(ctx, hid, rec):
    st = the_story(ctx).state
    h = ctx.get(hid)
    tgt = ctx.get(rec.get("target"))
    if (h is None or h.state.dead or h.state.down or h.state.in_irons or h.state.hired or ctx.embodied(h)
            or tgt is None or tgt.state.dead or h.parent is None):
        end_hunt(ctx, hid)
        return
    until = rec.get("until")
    if until is not None and ctx.t > float(until):
        end_hunt(ctx, hid)
        return
    mode = rec.get("mode")
    if mode == "kill" and step_of(st, tgt) != "marked":
        end_hunt(ctx, hid)  # paid off, or called off
        return
    if not playing(ctx, tgt) or tgt.parent is None:
        # nobody plays them now (or their human has gone quiet): the hunter goes back to his day, and the hunt waits for them
        if h.state.routine_hold_until is not None:
            ctx.patch(h, {"routine_hold_until": None, "routine_key": None})
        return
    if h.state.routine_hold_until is None or float(h.state.routine_hold_until) < ctx.t + HOLD / 2:
        ctx.patch(h, {"routine_hold_until": ctx.t + HOLD})
    if h.parent.id == tgt.parent.id:
        if mode == "kill":
            spring(ctx, hid, rec, h, tgt)
        elif mode == "tail":
            tail_seen(ctx, hid, rec, h, tgt)
        elif mode == "warn":
            warn_now(ctx, hid, h, tgt)
        return
    if my_fight(ctx, h) is not None:
        return  # in a fight where they stand: the fight runs them
    step_toward(ctx, st, h, tgt.parent)

def spring(ctx, hid, rec, h, tgt):
    st = the_story(ctx).state
    place = h.parent
    if sanctuary(st, place.id):
        return
    if not rec.get("sprung"):
        # they show themselves first, and strike on the next tick: one beat (about one deed) to run, shout or draw.
        # A rehearsal of the live world saw two of them kill a fresh character inside one round with no beat at all.
        here = []
        for oid in (st.hunts or {}):
            o = (st.hunts or {}).get(oid)
            b = ctx.get(oid)
            if o and o.get("target") == tgt.id and o.get("mode") == "kill" and b is not None and b.parent is not None \
                    and b.parent.id == place.id:
                here.append(b)
                ctx.patch(the_story(ctx), {"hunts": {oid: {"sprung": ctx.t}}})
        ambush_scene(ctx, place, here)
        return
    if ctx.t - float(rec.get("sprung") or 0) < BEAT:
        return  # the beat is not over: this tick is the one they showed themselves on
    strike_first(ctx, h, tgt)

def ambush_scene(ctx, place, men):
    if not men:
        return
    if len(men) == 1:
        text = (cap1(look_of(men[0], "a hard-faced man")) + " comes in out of the dark and walks straight at you, with "
                "something already in hand.")
    else:
        names = [look_of(m, "a hard-faced man") for m in men]
        text = (cap1(", ".join(names[:-1]) + " and " + names[-1]) + " come in out of the dark, from more than one side "
                "at once. They are not here to drink, and they are not here to talk.")
    ctx.emit("scene", target=place.id, reach=1, text=text)

def tail_seen(ctx, hid, rec, h, tgt):
    seen = list(rec.get("seen") or [])
    if h.parent.id in seen:
        return
    seen.append(h.parent.id)
    ctx.patch(the_story(ctx), {"hunts": {hid: {"seen": seen}}})
    who = cap1(look_of(h, "a man in a black armband"))
    if len(seen) == 1:
        text = who + " is here too, and does not look your way."
    elif len(seen) == 2:
        text = who + " comes in a little after you and finds a wall to lean on, and does not look your way. That is twice tonight."
    else:
        text = who + " again. A wall, a drink nobody is drinking, and eyes that are always somewhere else when you look."
    ctx.emit("scene", target=tgt.id, reach=0, text=text)

def warn_now(ctx, hid, h, tgt):
    if h.name == WARNER:
        text = (cap1(look_of(h, "a neat woman with a little black book")) + " stops at your elbow, opens a small black "
                "book and reads from it without looking up: where you have been tonight, who you asked, and what about. She "
                "closes it. \"Mister Dominico says the docks are bad for your health,\" she says pleasantly. \"Drink "
                "somewhere else. Tonight, and every night.\" Then she is gone, and the room starts breathing again.")
    else:
        text = (cap1(look_of(h, "a man in a black armband")) + " steps in close enough that you can smell the rum on him. "
                "\"Mister Dominico's heard your name,\" he says. \"He doesn't like hearing it. Drink somewhere else.\" He "
                "pats your shoulder, twice, and goes.")
    ctx.emit("scene", target=h.parent.id, reach=1, text=text)
    end_hunt(ctx, hid)

# ---- the Fist comes to the warehouse (Brask cowed, bribed or shown Gog's marker: scripts/guard_on.py) --------------

def fist_answers(ctx, s, p):
    st = s.state
    if st.fist_answered or fist_gone(ctx, st):
        return
    ctx.patch(s, {"fist_answered": p.get("why") or True})
    by = ctx.get(p.get("by")) if p.get("by") else None
    men = []
    brask = ctx.get(st.brask) if st.brask else None
    if free_hand(ctx, brask) and not is_hunting(st, brask.id):
        men.append(brask)
    for name in ["Tully", "Ott Fennick", "Jory Fennick"]:
        if len(men) >= 3:
            break
        m = body_named(ctx, name)
        if free_hand(ctx, m) and not is_hunting(the_story(ctx).state, m.id) and m.id not in [x.id for x in men]:
            men.append(m)
    if not men:
        return
    klhyt = ctx.get(st.klhyt) if st.klhyt else None
    looks = [look_of(m, "a man in a black armband") for m in men]
    who = cap1(looks[0] if len(looks) == 1 else ", ".join(looks[:-1]) + " and " + looks[-1])
    come = " comes" if len(men) == 1 else " come"
    if not st.klhyt_freed and not st.shipped and klhyt is not None and klhyt.parent is not None and klhyt.parent.id == st.warehouse:
        for m in men:
            if m.parent is None or m.parent.id != st.docks:
                go_one(ctx, m, ctx.get(st.docks))
            ctx.patch(m, {"post": st.docks, "routine_hold_until": ctx.t + 3 * 3600})
        if brask is not None and brask.id in [x.id for x in men]:
            ctx.patch(brask, {"left_post": None, "off_post": None})
        ctx.emit("scene", target=st.docks, reach=1, text=who + come + " down the pier at a run and settle round "
                 "the warehouse door, meaning to stay. Nobody is getting in there quietly now.")
        if by is not None:
            add_heat(ctx, by, 3, "the Fist knows who moved Brask", False)
        return
    if st.klhyt_freed and klhyt is not None and klhyt.parent is not None and not klhyt.state.dead and \
            klhyt.parent.id in [st.docks, st.warehouse, st.harbour]:
        place = klhyt.parent
        freer = ctx.get(st.freed_by) if st.freed_by else None
        if freer is not None:
            ctx.patch(s, {"heat": {freer.id: max(heat_of(the_story(ctx).state, freer), MARK_AT)}})
            mark(ctx, freer, "freed Klhyt from the Fist's warehouse")
        for m in men:
            if m.parent is None or m.parent.id != place.id:
                go_one(ctx, m, place)
            ctx.patch(m, {"post": place.id, "routine_hold_until": ctx.t + HOLD})
            if freer is not None:
                hunt_for(ctx, m, freer, "kill", None)
                ctx.patch(the_story(ctx), {"hunts": {m.id: {"sprung": True}}})
        ctx.emit("scene", target=place.id, reach=1, text=who + come + " down the pier at a run, see the grey-bearded man "
                 "standing loose, and stop. Then they spread out, slowly, the way men do who have been told what happens "
                 "to them if the crate goes out empty.")
        strike_first(ctx, men[0], klhyt)
        for m in men:
            mark_foes(ctx, m, klhyt)  # each of them is there for him
        return
    freer = ctx.get(st.freed_by) if st.freed_by else None
    if freer is not None:
        ctx.patch(s, {"heat": {freer.id: max(heat_of(the_story(ctx).state, freer), MARK_AT)}})
        mark(ctx, freer, "freed Klhyt from the Fist's warehouse")

# ---- the Throne: the warrant, on sight, and the witnesses ----------------------------------------------------------

def throne_sight(ctx, s):
    st = s.state
    if not st.wanted:
        return
    throne = faction_called(ctx, THRONE)
    if throne is None:
        return
    for pid in st.wanted:
        tgt = ctx.get(pid)
        if tgt is None or tgt.state.dead or not playing(ctx, tgt) or tgt.parent is None or sanctuary(st, tgt.parent.id):
            continue
        if not outlaw_of(ctx, throne, tgt):
            continue
        for p in ctx.children(tgt.parent, "person"):
            if p.id == tgt.id or not free_hand(ctx, p) or my_fight(ctx, p) is not None:
                continue
            if p.name not in THRONE_MEN and p.id not in (st.magistrate_guards or []):
                continue
            seen = the_story(ctx).state.sighted or {}
            if seen.get(pid) != tgt.parent.id:
                ctx.patch(the_story(ctx), {"sighted": {pid: tgt.parent.id}})
                ctx.emit("scene", target=tgt.parent.id, reach=1, text=cap1(look_of(p, "an officer of the Throne"))
                         + " looks at you, and then at the paper in one hand, and then at you again. \"By commission of "
                         "the Throne of Vorkath,\" comes the voice, quite calm, \"you will come with me.\" Nobody waits "
                         "for an answer.")
            strike_first(ctx, p, tgt)

def throne_night(ctx, s, day):
    st = s.state
    ctx.patch(s, {"throne_day": day})
    cust = ctx.get(st.custodian) if st.custodian else None
    if cust is None or cust.state.dead or cust.state.in_irons:
        return
    freer = ctx.get(st.freed_by) if st.freed_by else None
    if freer is not None and not freer.state.dead and freer.id not in (st.wanted or []):
        warrant(ctx, freer, "the theft of a prisoner of the Throne from the bonded warehouse")
        return
    men = [m for m in [body_named(ctx, n) for n in THRONE_MEN] if free_hand(ctx, m)]
    if not men:
        return
    for key in WITNESS_KEYS:
        if key not in (st.clues or []) or key in (st.silenced or []):
            continue
        w = ctx.get(st.get(key)) if st.get(key) else None
        if w is None or w.state.dead or w.parent is None or sanctuary(st, w.parent.id):
            continue
        place = w.parent
        for m in men:
            if m.parent is None or m.parent.id != place.id:
                go_one(ctx, m, place)
            ctx.patch(m, {"routine_hold_until": ctx.t + 1800})
        looks = [look_of(m, "an officer of the Throne") for m in men]
        who = cap1(looks[0] if len(looks) == 1 else " and ".join(looks))
        come = " comes" if len(men) == 1 else " come"
        wl = look_of(w, "the witness")
        guarded = [x for x in ctx.children(place, "person") if ctx.embodied(x)]
        if guarded:
            tell_mission(ctx, "witnesses", [x.id for x in guarded])
            ctx.emit("scene", target=place.id, reach=1, text=who + come + " to the door in the small hours, look at who is "
                     "sitting up with " + wl + ", and stand there a while. Then they go away again. Too many eyes.")
            ctx.patch(s, {"spared": {key: day}})
            return
        ctx.patch(w, {"silenced": True})
        ctx.patch(s, {"silenced": list(st.silenced or []) + [key]})
        ctx.emit("scene", target=place.id, reach=1, text=who + come + " in out of the small hours and sit down either side "
                 "of " + wl + " and talk, quietly, for a long time. When they go, " + wl + " sits very still and does "
                 "not finish the drink.")
        ctx.remember(cust, "Voss has spoken to the witness the town calls " + key + ". They will not speak to the magistrate.")
        return
