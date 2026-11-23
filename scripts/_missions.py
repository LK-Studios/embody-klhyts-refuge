# The town's work (cast/g_gog.py and cast/l_missions.py, MISSIONS), as the engine's jobs: promises their givers carry
# (Fat Gog, Klhyt, River, the Custodian), hidden on them, each with its `mission` key, the story facts it waits on
# (`when`) and what it pays. Asked for work (or pay, help, a job, a deal...), a giver offers what the night calls for,
# aloud in their own voice (`work_voice` on them) and with the jobs pack's offer, so `jobs` and `take_job` find it. The story
# and the peril rule say when a mission's work is done (a `mission_done` event to the root: they never include this
# file, whose `pay` would shadow the 5e pack's), and this pays each holder who did it from Gog's own purse.
use("jobs")

WORK_WORDS = ["work", "job", "jobs", "hire", "employ", "useful", "help", "mission", "missions", "task", "tasks", "errand",
              "errands", "favour", "favor", "pay", "paid", "payment", "reward", "rewards", "earn", "coin", "gold", "money",
              "offer", "offers", "contract", "bounty", "anything", "deal", "bargain", "errand", "something"]
RING_WORDS = ["ring", "candle", "whisper", "whispers", "voice", "leans", "flame", "spirit", "demon", "devil", "thing",
              "something", "awake", "talks", "nerve", "magic"]
GOG = "Fat Gog"

def gog_of(ctx):
    for p in ctx.find(type="person", name=GOG, limit=3):
        if p.name == GOG:
            return p
    return None

def story_now(ctx):
    found = ctx.find(type="story", limit=1)
    return found[0] if found else None

def said_words(text):
    t = " " + str(text).lower() + " "
    for ch in [",", ".", "?", "!", ";", ":", "'", "\"", "(", ")"]:
        t = t.replace(ch, " ")
    return t.split()

def mission_job(ctx, key):
    for j in ctx.find(type="job", limit=200):
        if j.state.mission == key:
            return j
    return None

def carried_jobs(ctx, giver):
    out = []
    for j in ctx.children(giver):
        if j.is_a("job") and j.state.mission:
            out.append(j)
    return order_jobs(out)

def order_jobs(jobs):
    keyed = [[int(j.state.order or 0), i] for i, j in enumerate(jobs)]
    keyed = sorted(keyed)
    return [jobs[k[1]] for k in keyed]

def wanted_now(st, job):
    w = job.state.when or {}
    for k in w.get("all") or []:
        if not st.get(k):
            return False
    for k in w.get("none") or []:
        if st.get(k):
            return False
    if w.get("any_marked"):
        steps = st.peril_step or {}
        if not [k for k in steps if steps.get(k) == "marked"]:
            return False
    return True

def voice(giver, key, default):
    return (giver.state.work_voice or {}).get(key) or default

def offer_work(ctx, gog, who):
    # what this giver would pay this person for now, offered aloud: each a job they can take (`jobs`, `take_job`)
    s = story_now(ctx)
    st = s.state if s is not None else None
    offered = []
    holding = []
    for j in carried_jobs(ctx, gog):
        if who.id in (j.state.holders or {}):
            holding.append(j)
            continue
        if st is None or not j.state.open or not wanted_now(st, j):
            continue
        if (j.state.repeat or "once") == "once" and (j.state.done_by or {}).get(who.id):
            continue
        ctx.patch(j, {"offers": {who.id: ctx.t}})
        if take_wrong(ctx, j, who):
            continue  # full, or not for them
        ctx.emit("job_offered", target=who, reach=1, job=j.id, giver=gog.id, terms=j.state.terms)
        offered.append(j)
    if offered:
        # the three that press most, said aloud (a voice client hears all of it); the rest are on `jobs`
        text = " ".join([str(j.state.pitch or j.state.terms) for j in offered[:3]])
        if len(offered) > 3:
            text = text + " " + voice(gog, "more", "\"There's more besides, if you want it. Say yes to any of it.\"")
        elif len(offered) > 1:
            text = text + " " + voice(gog, "many", "\"Any of it. Say yes, and it's yours.\"")
        else:
            text = text + " " + voice(gog, "one", "\"Say yes, and it's yours.\"")
    elif holding:
        text = voice(gog, "holding", "\"You're about my business already. Finish that, and come back.\"")
    else:
        text = voice(gog, "none", "\"Nothing tonight that I'd pay you for. Come back when the town has turned over.\"")
    ctx.emit("scene", target=gog.parent.id, reach=1, text=text)
    return offered

def finish(ctx, key, who_ids, why_others):
    # the mission's work is done: each holder among who_ids is done and paid (the jobs pack's done and pay); for a
    # once-job, whoever else holds it is told it is over
    j = mission_job(ctx, key)
    if j is None:
        return []
    paid = []
    for wid in who_ids or []:
        w = ctx.get(wid)
        if w is not None and wid in (j.state.holders or {}):
            done(ctx, j, w)
            paid.append(w)
    if (j.state.repeat or "once") == "once":
        for hid in list((j.state.holders or {}).keys()):
            if (j.state.holders or {}).get(hid) is not None:
                fail(ctx, j, hid, why_others or "it was done by someone else")
        if j.state.open:
            ctx.patch(j, {"open": False})
    giver = giver_of(ctx, j)
    for w in paid:
        if giver is not None and w.parent is not None and giver.parent is not None and giver.parent.id == w.parent.id:
            line = voice(giver, "paid_here", "It is counted out for you, coin by coin. \"Paid.\"")
        else:
            line = voice(giver, "paid_away", "A runner finds you, presses a purse into your hand, says \"Paid,\" and "
                                             "is gone.")
        ctx.emit("scene", target=w.id, reach=0, text=line)
    return paid
