# Following someone means keeping to them (owner's playtest, 2026-11-22: elves told to follow walked straight home).
# The idle routine walks a body that is not thirsty back to its `post` a step at a time, so a follower would undo every
# step; whoever follows has their usual place kept for them in `post_kept`, and gets it back when they stay. A hire
# keeps a hireling's place its own way.

def on(ctx, event):
    p = event.payload or {}
    if event.kind == "following":
        me = ctx.get(p.get("by"))
        if me is None or (me.state.hired or {}).get("by") or not me.state.post:
            return
        ctx.patch(me, {"post": None, "post_kept": me.state.post})
    elif event.kind == "stayed":
        me = ctx.get(event.target)
        if me is not None and me.state.post_kept:
            ctx.patch(me, {"post": me.state.post_kept, "post_kept": None})
