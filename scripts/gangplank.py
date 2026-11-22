# The Moonmoth takes elves aboard, and anyone an elf has vouched for with a silverleaf token. Everyone else finds the
# gangplank lifting itself an inch out of reach. Going aboard is always a step taken yourself (owner's playtest,
# 2026-11-22: following an elf up the pier carried a player aboard): a played body that follows someone up the pier
# stops at the foot of the gangplank, and nobody is carried aboard behind a leader past the token.

def welcome(me):
    if me.state.people == "elf":
        return True
    for it in me.children():
        if it.state.elf_token:
            return True
    return False

def pier(ctx):
    for e in ctx.edges(ctx.self, "connects_to", "out"):
        return ctx.get(e["target"])
    return None

def on(ctx, event):
    p = event.payload or {}
    if event.kind == "arrived":
        if not p.get("following") or p.get("place") != ctx.self.id:
            return
        me = ctx.get(p.get("who"))
        back = pier(ctx)
        if me is None or back is None:
            return
        if ctx.embodied(me):
            ctx.move(me, back)
            ctx.patch(me, {"follows": None})
            ctx.emit("scene", target=me, reach=0, text="You stop at the foot of the Moonmoth's gangplank: going aboard "
                     "is a step you take yourself, if she will have you.")
        elif not welcome(me):
            ctx.move(me, back)
            ctx.patch(me, {"follows": None})
            ctx.emit("scene", target=back, reach=1, text=me.name + " starts up the Moonmoth's gangplank behind the others, "
                     "and it lifts itself an inch out of reach. " + me.name + " stays on the pier.")
        return
    if p.get("verb") not in ("go", "crawl") or event.target != ctx.self.id:  # crawling up it is still going aboard
        return
    me = ctx.get(event.actor) if event.actor else None
    if me is None or welcome(me):
        return
    ctx.reject("the Moonmoth's gangplank lifts itself an inch out of reach as you step onto it: she does not take your kind aboard",
               "an elf in exile can vouch for you: they give a silverleaf token to those they trust")
