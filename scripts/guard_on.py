def walk_off(ctx, me, why, line):
    # the guard leaves his post: for the coin, for Fat Gog's marker, or because he was cowed
    dest = ctx.get(me.state.walks_to) if me.state.walks_to else None
    if dest is None or me.parent.id == dest.id or me.state.down or me.state.dead:
        return
    here = me.parent
    ctx.emit("scene", target=here, reach=1, text=line)
    # whatever he was minding the key for, he is not minding it now: it goes on the nail by the door
    for it in me.children():
        if it.name == me.state.leaves_behind:
            ctx.move(it, here)
            ctx.emit("scene", target=here, reach=1, text=me.name + " hangs the " + str(it.name).lower() + " on a nail by the door as he goes.")
    ctx.move(me, dest)
    ctx.patch(me, {"left_post": why, "post": dest.id})
    ctx.emit("arrived", target=dest, reach=-1, who=me.id, place=dest.id)
    ctx.emit("left_post", target=me, reach=-1, why=why, post=here.id)

def on(ctx, event):
    me = ctx.self
    if event.target != me.id or me.state.left_post or me.state.down or me.state.dead or me.state.asleep:
        return
    k = event.kind
    if k == "given":
        item = ctx.get(event.payload.get("item"))
        kind = ctx.root().state.coin_kind or "coin"
        if item is None or item.state.kind != kind:
            return
        if ctx.count(me, kind) - int(me.state.purse_before or 0) >= int(me.state.bribe or 999999):
            walk_off(ctx, me, "bribed", me.state.bribe_line or (me.name + " pockets the coin and finds somewhere else to be."))
    elif k == "shown":
        item = ctx.get(event.payload.get("item"))
        if item is not None and item.state.marker == "gog":
            walk_off(ctx, me, "marker", me.state.marker_line or (me.name + " looks at the marker, then at you, and walks."))
    elif k == "cowed":
        walk_off(ctx, me, "cowed", me.state.cowed_line or (me.name + " decides this is not worth his teeth and goes."))
