# Pet an animal here (the beasts pack's beast): it answers in its own way, its `petted` lines in turn. One that is
# nobody's and does not trust you yet answers with its `shy` line instead (feed it, gentle it); a dog on guard snaps.
# The room sees it, as a scene.

def check(ctx):
    b = ctx.target
    if not b.state.beast:
        return "you can only pet an animal"
    if b.parent is None or ctx.actor.parent is None or b.parent.id != ctx.actor.parent.id:
        return "it is not here"
    if b.state.dead:
        return "it is dead"
    if b.state.down:
        return "it is down and hurt: tend it, do not pet it"
    return True

def apply(ctx):
    b = ctx.target
    me = ctx.actor
    trusts = int((b.state.trust or {}).get(me.id) or 0) > 0 or b.state.owner == me.id
    wary = b.state.shy and not trusts and (b.state.owner is not None or b.state.herd is None)
    lines = list(b.state.petted or [])
    if wary:
        line = str(b.state.shy)
    elif lines:
        n = int(b.state.pet_n or 0)
        line = str(lines[n % len(lines)])
        ctx.patch(b, {"pet_n": n + 1})
    else:
        line = "The " + str(b.name).lower() + " leans into your hand."
    ctx.emit("scene", target=me.parent, reach=1, text=me.name + " reaches out to the " + str(b.name).lower() + ". " + line)
    ctx.log(line)
    return {"line": line, "wary": bool(wary)}
