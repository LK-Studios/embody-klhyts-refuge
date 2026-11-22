def check(ctx):
    t = ctx.target
    if t.id == ctx.actor.id:
        return "you cannot reach your own knots"
    if not t.state.bound:
        return t.name + " is not tied up"
    if ctx.actor.state.bound:
        return "your own hands are tied"
    if t.parent.id != ctx.actor.parent.id:
        return "they are not here"
    return True

def apply(ctx):
    t = ctx.target
    ctx.patch(t, {"bound": False, "description": t.state.description_free or t.state.description})
    ctx.emit("freed", target=t, reach=1, by=ctx.actor.id)
    ctx.log("you cut " + t.name + " loose")
