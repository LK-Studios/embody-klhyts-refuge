# The missions rule, on the root (scripts/_missions.py has the why). Anyone who carries work (Fat Gog, Klhyt, River,
# the Custodian), asked for it (talk, or a line said to them), offers what the night calls for; a job taken that comes
# with something to carry hands it over; the story's and the peril rule's `mission_done` pays whoever did it; one of
# the Fist put on the ground pays the dogs' bounty; and whoever saw what moves Dominico, telling Gog, is paid for it.
use("missions")

FIST_NAME = "the Fist"

def on(ctx, event):
    k = event.kind
    p = event.payload or {}
    if k == "mission_done":
        finish(ctx, p.get("key"), p.get("who") or [], p.get("why"))
        return
    if k == "downed":
        t = ctx.get(event.target) if event.target else None
        by = ctx.get(p.get("by")) if p.get("by") else None
        if t is not None and by is not None and t.state.faction == FIST_NAME and by.state.faction != FIST_NAME:
            finish(ctx, "dogs", [by.id], None)
        return
    if k == "job_taken":
        handed(ctx, event, p)
        return
    if k != "talked" and k != "say":
        return
    tid = event.target if k == "talked" else (p.get("to") or event.target)
    giver = ctx.get(tid) if tid else None
    if giver is None or not giver.is_a("person") or ctx.embodied(giver):
        return  # a mind playing a giver offers the work itself (offer_job)
    who = ctx.get(event.actor) if event.actor else None
    if who is None or not ctx.embodied(who) or who.parent is None or giver.parent is None or who.parent.id != giver.parent.id:
        return
    said = said_words(p.get("about") if k == "talked" else p.get("text"))
    s = story_now(ctx)
    if giver.name == "Dominico" and s is not None and [w for w in said if w in RING_WORDS]:
        # asked about his ring, he closes his hand on it and the candle leans toward it (his lines): seen, as at the
        # Apothecary's look, so the one who saw it can tell Gog (his "Who pays for Dominico's nerve")
        by = list((s.state.clue_by or {}).get("ring") or [])
        if who.id not in by:
            ctx.patch(s, {"clue_by": {"ring": by + [who.id]}})
        return
    if giver.name == GOG and s is not None and not s.state.iron_known \
            and who.id in ((s.state.clue_by or {}).get("ring") or []) and [w for w in said if w in RING_WORDS]:
        iron_told(ctx, s, giver, who)
        return
    if [w for w in said if w in WORK_WORDS] and carried_jobs(ctx, giver):
        offer_work(ctx, giver, who)

def handed(ctx, event, p):
    # a job that comes with something to carry (`hands`: a letter or thing) gives it to the one who took it
    j = ctx.get(p.get("job")) if p.get("job") else None
    taker = ctx.get(event.target) if event.target else None
    if j is None or taker is None or not j.state.hands:
        return
    h = j.state.hands
    ctx.spawn(h.get("type") or "thing", taker, name=h["name"], state=dict(h.get("state") or {}))
    g = giver_of(ctx, j)
    if g is not None and h.get("line"):
        ctx.emit("scene", target=taker.id, reach=0, text=h["line"])

def iron_told(ctx, s, gog, who):
    ctx.patch(s, {"iron_known": True, "iron_told_by": who.id})
    ctx.emit("scene", target=gog.parent.id, reach=1, text="The huge old lizardman listens without blinking, all the "
             "way to the end. Then he sits back, and the chair complains. \"A candle that leans toward a ring.\" He is "
             "quiet a long time. \"Old things don't stay buried in this country, friend. Something under the ground has "
             "found a man who wants what I have, and it is whispering him the price.\" He looks at you properly. \"Tell "
             "nobody else. I need to think like a heron.\"")
    ctx.remember(gog, who.name + " told me what moves Dominico: a candle that leans toward the ring he turns. Something "
                 "old is whispering to him.")
    finish(ctx, "iron", [who.id], None)
