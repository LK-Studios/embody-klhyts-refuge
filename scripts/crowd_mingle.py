# A crowd is place state, not a hundred bodies: mingling in it, you overhear one of its rumours, one you have not
# heard from this crowd before. Only you hear it.

def check(ctx):
    c = ctx.target
    if c.parent.id != ctx.actor.parent.id:
        return "you are not in that crowd"
    if not c.state.rumours:
        return "nobody here is talking about anything you would want to hear"
    return True

def apply(ctx):
    c = ctx.target
    me = ctx.actor
    rumours = c.state.rumours
    heard = dict(c.state.heard or {})
    mine = list(heard.get(me.id) or [])
    fresh = [i for i in range(len(rumours)) if i not in mine]
    if not fresh:
        ctx.emit("scene", target=me, reach=0, text=c.state.heard_all or "You have heard everything this crowd is saying tonight, twice.")
        ctx.log("nothing new in this crowd tonight")
        return
    i = ctx.rand.choice(fresh)
    mine.append(i)
    heard[me.id] = mine
    ctx.patch(c, {"heard": heard})
    ctx.emit("scene", target=me, reach=0, text=rumours[i])
    ctx.log("overheard: " + rumours[i])
