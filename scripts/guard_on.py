# The warehouse guard: coin enough, Fat Gog's marker, or a hard look moves him off his door. Every way off it has a
# price and a clock (owner, 2026-11-23: "We need more peril!"): cowed, he runs for help with the key still on his belt
# and the Fist is at the warehouse in five minutes, knowing who; bribed, he hangs the key on the nail, and in half an
# hour he has told Sabeth Crane who paid him, with the Fist at the door in fifteen; shown Gog's marker, he hangs the key
# and goes, and Dominico hears Gog is moving: the Fist comes in ten. What they do when they come is
# scripts/peril_rule.py's fist_answers.
use("peril")

def walk_off(ctx, me, why, line, keep_key):
    dest = ctx.get(me.state.walks_to) if me.state.walks_to else None
    if dest is None or me.parent.id == dest.id or me.state.down or me.state.dead:
        return False
    here = me.parent
    ctx.emit("scene", target=here, reach=1, text=line)
    if not keep_key:
        # whatever he was minding the key for, he is not minding it now: it goes on the nail by the door
        for it in me.children():
            if it.name == me.state.leaves_behind:
                ctx.move(it, here)
                ctx.emit("scene", target=here, reach=1, text="He hangs the " + str(it.name).lower() + " on a nail by the door as he goes.")
    ctx.move(me, dest)
    ctx.patch(me, {"left_post": why, "off_post": True, "post": dest.id})
    ctx.emit("arrived", target=dest, reach=-1, who=me.id, place=dest.id)
    ctx.emit("left_post", target=me, reach=-1, why=why, post=here.id)
    return True

def answer_in(ctx, secs, why, by):
    ctx.schedule(secs, "fist_answers", target=ctx.root().id, payload={"why": why, "by": by})

def on(ctx, event):
    me = ctx.self
    if event.target != me.id or me.state.left_post or me.state.down or me.state.dead or me.state.asleep:
        return
    k = event.kind
    by = event.payload.get("by")
    if k == "given":
        item = ctx.get(event.payload.get("item"))
        kind = ctx.root().state.coin_kind or "coin"
        if item is None or item.state.kind != kind:
            return
        if ctx.count(me, kind) - int(me.state.purse_before or 0) >= int(me.state.bribe or 999999):
            if walk_off(ctx, me, "bribed", me.state.bribe_line or "He pockets the coin and finds somewhere else to be.", False):
                ctx.schedule(1800, "brask_talks", target=ctx.root().id, payload={"by": by})
                answer_in(ctx, 900, "bribed", by)
    elif k == "shown":
        item = ctx.get(event.payload.get("item"))
        if item is not None and item.state.marker == "gog":
            if walk_off(ctx, me, "marker", me.state.marker_line or "He looks at the marker, then at you, and walks.", False):
                answer_in(ctx, 600, "marker", by)
    elif k == "cowed":
        if walk_off(ctx, me, "cowed", me.state.cowed_line or "He backs off, then runs, shouting for help.", True):
            who = ctx.get(by) if by else None
            add_heat(ctx, who, 3, "cowed Brask off the warehouse door")
            answer_in(ctx, 300, "cowed", by)
