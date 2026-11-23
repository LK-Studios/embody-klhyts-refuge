# The town's day (owner, 2026-11-23: "Give them routines, jobs, their own money, their plans or schemes"). A repeating
# `routine_tick` on the root walks everyone through their day: each person's `routine` is a list of slots,
# {"at": hour, "place": place id, "doing": sentence, "go": what the room they leave sees, "pay": {"to": id, "cp": n,
# "for": why}, "beats": [...]}, the last whose hour has come is theirs (the last of the list wraps round past
# midnight). A new slot moves their `post` (d20's idle walk then takes them there, a step a minute), sets what they
# are doing into their description (`look` + `doing`), hands over its pay, and tells the room they leave, if anyone
# is in it. While a player is in a room, the people at work there show it now and then (`beats`), one a tick.
#
# A routine waits for: a body someone holds, a hireling, a follower, someone tied, down or dead, one the story walked
# (`routine_hold_until`), one the story has done with (`routine_off`), and one whose `routine_when` names facts (the
# story's, or a flag of their own) none of which is true yet (Klhyt starts his day once he is free, Brask once he is
# off the warehouse door). `routine_if` ([[flag, slots], ...]) is a day the news brings: the first whose flag is true
# (the person's own, or the story's) is kept instead of `routine` (the watch split once Klhyt is home).

def story(ctx):
    found = ctx.find(type="story", limit=1)
    return found[0] if found else None

def hour_now(ctx):
    d = ctx.day_seconds()
    return ((ctx.t % d) / d) * 24.0, int(ctx.t // d)

def slot_of(routine, h):
    # the last slot whose hour has come; before the first, the day's last slot still runs (it wrapped past midnight)
    idx = len(routine) - 1
    wrapped = True
    for i in range(len(routine)):
        if float(routine[i].get("at", 0)) <= h:
            idx = i
            wrapped = False
    return idx, wrapped

def waits(ctx, p, st, facts):
    if st.dead or st.down or st.bound or st.routine_off or st.hired or st.follows:
        return True
    if ctx.embodied(p):
        return True
    if st.routine_hold_until is not None and ctx.t < float(st.routine_hold_until):
        return True
    when = st.routine_when
    if when:
        for k in when:
            if facts.get(k) or st.get(k):
                return False
        return True
    return False

def pay(ctx, payer, slot):
    deal = slot.get("pay")
    if not deal:
        return
    to = ctx.get(deal.get("to"))
    owed = int(deal.get("cp") or 0)
    if to is None or owed <= 0 or to.state.dead:
        return
    kind = ctx.root().state.coin_kind or "coin"
    paid = 0
    for it in payer.children():
        if owed <= 0:
            break
        if it.state.kind != kind and (it.name or "").lower() != kind:
            continue
        n = min(owed, ctx.count(it))
        if n > 0:
            ctx.transfer(it, to, count=n)
            owed = owed - n
            paid = paid + n
    if paid:
        ctx.emit("paid", target=to, reach=0, by=payer.id, cp=paid, why=deal.get("for") or "")

def told(here, people_here):
    # someone a player holds is in this room: only then is a leaving or a beat worth a line
    return here is not None and people_here.get(here.id)

def daylight(ctx, h):
    # the hour as the town feels it, for anyone who looks at the sky; the night's story says midnight and the small
    # hours itself, and this only speaks when the band changes
    bands = [[0.0, "midnight", None], [0.5, "the small hours", None], [5.0, "dawn", "grey light coming up out of the sea"],
             [7.0, "morning", "sunlight, already hot"], [11.0, "the heat of the day", "hard white sunlight; every shutter shut"],
             [16.0, "afternoon", "long gold light"], [18.5, "evening", "lamplight coming on along the harbour"],
             [21.0, "night", "lamplight, torchlight and the harbour lanterns"]]
    band = bands[len(bands) - 1]
    for b in bands:
        if b[0] <= h:
            band = b
    root = ctx.root()
    if root.state.daylight_band == band[1]:
        return
    amb = dict(root.state.ambient or {})
    amb["time_of_day"] = band[1]
    if band[2]:
        amb["light"] = band[2]
    ctx.patch(root, {"daylight_band": band[1], "ambient": amb})

def on(ctx, event):
    if event.kind != "routine_tick":
        return
    h, day = hour_now(ctx)
    if day > 0 or h < 22.0:  # night one's hours are the story's to tell
        daylight(ctx, h)
    s = story(ctx)
    facts = s.state if s is not None else {}
    people = ctx.find(type="person", limit=500)
    played = {}
    for p in people:
        if ctx.embodied(p) and p.parent is not None:
            played[p.parent.id] = True
    beat_at = {}
    for p in people:
        st = p.state
        r = st.routine
        which = ""
        for alt in (st.routine_if or []):
            if st.get(alt[0]) or facts.get(alt[0]):
                r = alt[1]
                which = alt[0] + "/"
                break
        if not r:
            continue
        here = p.parent
        if waits(ctx, p, st, facts):
            continue
        idx, wrapped = slot_of(r, h)
        slot = r[idx]
        key = which + str(day - 1 if wrapped else day) + ":" + str(idx)
        fresh = st.routine_key != key
        changes = {}
        if fresh:
            changes["routine_key"] = key
            changes["doing"] = slot.get("doing") or ""
            if st.look:
                changes["description"] = (str(st.look) + " " + str(slot.get("doing") or "")).strip()
        if st.post != slot.get("place"):
            changes["post"] = slot.get("place")
        if changes:
            ctx.patch(p, changes)
        if fresh:
            pay(ctx, p, slot)
            if slot.get("go") and here is not None and here.id != slot.get("place") and told(here, played):
                ctx.emit("scene", target=here, reach=1, text=slot.get("go"))
            continue
        # settled in: maybe the room sees them at it
        if here is None or here.id != slot.get("place") or not told(here, played):
            continue
        lines = slot.get("beats") or st.beats
        if lines and here.id not in beat_at:
            beat_at[here.id] = [p, lines]
        elif lines:
            mine = beat_at[here.id]
            if int(p.state.beat_n or 0) < int(mine[0].state.beat_n or 0):
                beat_at[here.id] = [p, lines]
    for pid in beat_at:
        who = beat_at[pid][0]
        lines = beat_at[pid][1]
        n = int(who.state.beat_n or 0)
        ctx.patch(who, {"beat_n": n + 1})
        ctx.emit("scene", target=pid, reach=1, text=lines[n % len(lines)])
