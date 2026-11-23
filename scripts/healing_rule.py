# Healing as a service (the owner, 2026-11-23: "do we need a healer shop ? A doctor ? And a healer different shops
# different vibes"). A treatment bought from a healer (a thing whose state has `treatment`) is done at once and the
# thing is gone: the doctor's full treatment (every hit point back, now; and a wanted patient is reported to the
# Throne, which sends its officer to his door in ten world minutes), Sister Agathe's blessing (1d8 + 3) and stitches
# (1d4), a tooth pulled. Grandmother Ishkaa's long sleep (`rest`) heals only if the patient stays on her mats a world hour
# (`healing_tick` checks every five world minutes). Medicines (dressings, poultices) are the dnd5e pack's: `tend`.
use("common")
use("five")

DOCTOR = "Doctor Amsel Prewitt"
REST_FOR = 3600

def on(ctx, event):
    if event.kind == "healing_tick":
        mend_tick(ctx)
        return
    if event.kind == "treatment_done":
        # the bought treatment's token, cleared away a beat later: the buy verb still reads it when "bought" is heard
        t = ctx.get((event.payload or {}).get("item"))
        if t is not None and t.state.treatment:
            ctx.destroy(t)
        return
    if event.kind != "bought":
        return
    p = event.payload or {}
    item = ctx.get(p.get("item")) if p.get("item") else None
    buyer = ctx.get(p.get("by")) if p.get("by") else None
    seller = ctx.get(event.target) if event.target else None
    if item is None or buyer is None or seller is None:
        return
    here = seller.parent.id if seller.parent is not None else None
    if seller.name == DOCTOR and reported(ctx, buyer):
        # whatever a wanted patient buys of him, he writes it down, and the Throne reads his book (scripts/peril_rule.py)
        ctx.schedule(600, "doctor_tells", target=ctx.root().id, payload={"who": buyer.id, "at": here})
        ctx.emit("scene", target=buyer.id, reach=0, text="He writes something in a casebook, blots it, and closes it "
                 "before you can see.")
    if not item.state.treatment:
        return
    kind = item.state.treatment
    who = seller.state.seen_as or "the healer"
    who = who[:1].upper() + who[1:]
    if kind == "full":
        got = heal(ctx, buyer, int(buyer.state.max_hp or 1), seller, "treatment")
        ctx.emit("scene", target=buyer.id, reach=0, text=who + " works fast and without a wasted word: clean, stitch, "
                 "splint, bind. It hurts more than the wound did, and then it does not hurt at all. (" + str(got)
                 + " hit points back.)")
    elif kind == "blessing":
        n = roll_dice(ctx, item.state.heals or "1d8+3", False)
        got = heal(ctx, buyer, n, seller, "blessing")
        ctx.emit("scene", target=buyer.id, reach=0, text=who + " lays a hand on your head and prays, short and fierce, "
                 "like someone telling off a child. Warmth runs down into your hurts. (" + str(got) + " hit points back.)")
    elif kind == "stitches":
        n = roll_dice(ctx, item.state.heals or "1d4", False)
        got = heal(ctx, buyer, n, seller, "stitches")
        ctx.emit("scene", target=buyer.id, reach=0, text=who + " sits you on a barrel and puts a needle through you "
                 "with no ceremony at all, talking about spuds the whole time. (" + str(got) + " hit points back.)")
    elif kind == "rest":
        ctx.patch(buyer, {"mending": {"at": here, "until": ctx.t + REST_FOR}})
        ctx.emit("scene", target=buyer.id, reach=0, text=who + " lays you down on the reed mats, packs river mud on "
                 "your hurts and sings, low, under her breath. Stay the hour, and wake whole. Get up before, and it is "
                 "only mud.")
    elif kind == "tooth":
        ctx.emit("scene", target=buyer.id, reach=0, text=who + " has the tooth out before you have finished saying "
                 "which one.")
    ctx.move(item, seller)  # done: out of your hands now, and gone at the next beat
    ctx.schedule(1, "treatment_done", target=ctx.root().id, payload={"item": item.id})

def reported(ctx, who):
    found = ctx.find(type="story", limit=1)
    if not found:
        return False
    st = found[0].state
    return who.id in (st.wanted or [])

def mend_tick(ctx):
    for p in ctx.find(type="person", limit=1000):
        m = p.state.mending
        if not m:
            continue
        if p.state.dead:
            ctx.patch(p, {"mending": None})
            continue
        if p.parent is None or p.parent.id != m.get("at"):
            ctx.patch(p, {"mending": None})
            ctx.emit("scene", target=p.id, reach=0, text="You got up before the hour was out. The mud cracks and "
                     "falls away, and it was only mud.")
            continue
        if ctx.t >= float(m.get("until") or 0):
            got = heal(ctx, p, int(p.state.max_hp or 1), None, "the long sleep")
            ctx.patch(p, {"mending": None})
            ctx.emit("scene", target=p.id, reach=0, text="You wake on the reed mats with the river going by "
                     "underneath, and you are whole. (" + str(got) + " hit points back.)")
