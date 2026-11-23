# order: a villain's own verbs, one each by the `order` action's `named_by` (cast/f_peril.py, PERIL["orders"]):
# set_on and call_off for Dominico and Sabeth Crane, warrant and pardon for the Custodian. A mind playing them uses
# these ("Bodies without minds do not follow speech": an order said aloud moves nobody, this does). Nobody else holds
# them, so no player sees them.
use("peril")

def whom(ctx):
    name = str((ctx.params or {}).get("who") or "").strip().lower()
    if not name:
        return None
    near = None
    for p in ctx.find(type="creature", limit=500):
        n = str(p.name or "").lower()
        if n == name:
            return p
        if near is None and (n.startswith(name) or name in n.split(" ")):
            near = p
    return near

def check(ctx):
    if ctx.named_entry(ctx.actor, "orders", ctx.verb) is None:
        return "that is not an order you can give"
    who = whom(ctx)
    if who is None:
        return "say who it is about: who=<their name>"
    if who.id == ctx.actor.id:
        return "not on yourself"
    if who.state.dead:
        return who.name + " is dead already"
    return True

def apply(ctx):
    who = whom(ctx)
    v = ctx.verb
    s = the_story(ctx)
    if v == "set_on":
        ctx.patch(s, {"heat": {who.id: max(heat_of(s.state, who), MARK_AT)}})
        if mark(ctx, who, ctx.actor.name + "'s word"):
            ctx.log("the word is out on " + who.name + ": the men will find them, while someone plays them")
        else:
            ctx.log("nobody is left to carry the word")
    elif v == "call_off":
        fist = faction_called(ctx, FIST)
        if fist is not None:
            pardon_of(ctx, fist, who)
        for hid in list((s.state.hunts or {}).keys()):
            rec = (the_story(ctx).state.hunts or {}).get(hid)
            if rec and rec.get("target") == who.id:
                end_hunt(ctx, hid)
        ctx.patch(the_story(ctx), {"peril_step": {who.id: "called off"}, "heat": {who.id: WARN_AT - 1}})
        ctx.log("the word on " + who.name + " is taken back")
    elif v == "warrant":
        warrant(ctx, who, "crimes against the Throne")
        ctx.log("the Throne's warrant on " + who.name + " is on the square")
    elif v == "pardon":
        throne = faction_called(ctx, THRONE)
        if throne is not None:
            pardon_of(ctx, throne, who)
        ctx.patch(s, {"wanted": [x for x in (s.state.wanted or []) if x != who.id]})
        ctx.log("the Throne's warrant on " + who.name + " is lifted")
