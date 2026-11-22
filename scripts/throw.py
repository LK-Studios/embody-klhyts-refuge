def check(ctx):
    d = ctx.target
    if d.parent.id != ctx.actor.id and d.parent.id != ctx.actor.parent.id:
        return "they are not within reach"
    return True

def apply(ctx):
    d = ctx.target
    dice = d.state.dice or "2d6"
    total = ctx.rand.roll(dice)
    ctx.emit("thrown", target=d, reach=1, by=ctx.actor.id, dice=dice, total=total)
    ctx.emit("scene", target=ctx.actor.parent, reach=1,
             text=ctx.actor.name + " throws the " + str(d.name).lower() + ": " + str(total) + ".")
    ctx.log("you throw " + dice + ": " + str(total))
    return {"dice": dice, "total": total}
