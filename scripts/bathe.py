HOUR = 3600

def token_of(ctx, me):
    for it in me.children():
        if it.state.bath_token:
            return it
    return None

def check(ctx):
    if token_of(ctx, ctx.actor) is None:
        return "a lemon bath is a gold piece: buy a bath token from the steward first"
    return True

def apply(ctx):
    me = ctx.actor
    ctx.destroy(token_of(ctx, me))
    grants = [g for g in (me.state.grants or []) if g.get("source") != "lemon bath"]
    for skill in ["persuasion", "parley"]:
        grants.append({"source": "lemon bath", "bonus": 1, "skill": skill, "place": None, "until": ctx.t + HOUR,
                       "uses": None, "condition": "scrubbed clean and smelling of lemons"})
    ctx.patch(me, {"grants": grants})
    ctx.emit("bathed", target=me, reach=1, by=me.id)
    ctx.emit("scene", target=me.parent, reach=1,
             text="Lime stings the skin clean, and then a woman with a large fishbone sees to the rest. " + me.name +
                  " comes out pink, raw and smelling of lemons.")
    ctx.log("clean as a new coin: +1 to persuasion and parley for an hour")
