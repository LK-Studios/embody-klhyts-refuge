# The undertaker (the owner, 2026-11-23: "we will need an undertaker to go and sort out bodies etc."). Every ten world
# minutes (`undertaker_tick`) she looks for the town's dead: anyone dead half a world hour or more, lying in a place a
# townsperson would know (not a hidden one), whose seat nobody holds (a dead player's seat lets go when they take up
# another), and not already in a grave. She takes one at a time on her mule cart to the Quiet Ground, and buries them
# there in the burial pack's own grave (who lies there, who buried them, the words, with what they carried). The pack's
# graves take mark, inscribe and adorn from anyone after; she sells markers.
use("burial")

UNDERTAKER = "Ottoline Crabbe"
GROUND = "The Quiet Ground"
LIE_FOR = 1800

def on(ctx, event):
    if event.kind != "undertaker_tick":
        return
    me = None
    for p in ctx.find(type="person", name=UNDERTAKER, limit=3):
        if p.name == UNDERTAKER:
            me = p
    if me is None or me.state.dead or me.state.down or me.state.hired or ctx.embodied(me):
        return
    ground = None
    for g in ctx.find(type="place", name=GROUND, limit=3):
        if g.name == GROUND:
            ground = g
    if ground is None:
        return
    body = next_dead(ctx)
    if body is not None:
        lay_to_rest(ctx, me, body, ground)

def next_dead(ctx):
    best = None
    best_t = None
    for b in ctx.find(type="creature", limit=1000):
        st = b.state
        if not st.dead or st.buried_in or b.parent is None or not b.parent.is_a("place") or b.parent.state.hidden:
            continue
        if ctx.embodied(b):
            continue  # a dead seat still held: it lets go when its player takes up another (or gives leave)
        died = float(st.died_at) if st.died_at is not None else 0.0  # dead before she came: long enough
        if ctx.t - died < LIE_FOR:
            continue
        if best is None or died < best_t:
            best = b
            best_t = died
    return best

def lay_to_rest(ctx, me, b, ground):
    here = b.parent
    seen = b.state.seen_as or (("a dead " + str(b.state.people)) if b.state.people else "the dead")
    if here.id != ground.id:
        ctx.emit("scene", target=here.id, reach=1, text="A high-wheeled mule cart creaks in under a tarpaulin, led by "
                 "a stooped woman in a black stovepipe hat. She looks at the body of " + str(seen) + " for a while, "
                 "takes her hat off, and lifts it onto the cart with a strength you would not expect. She covers the face, "
                 "puts her hat back on, and leads the mule away toward the Treeline Road.")
        ctx.move(me, ground)
        ctx.move(b, ground)
        ctx.emit("arrived", target=ground.id, reach=-1, who=me.id, place=ground.id)
    words = "Here lies " + b.name + ". Nobody here asked where they came from."
    g = ctx.spawn("grave", ground, name="Grave of " + b.name,
                  state={"lies": b.name, "buried_by": me.name, "buried_at": ctx.t, "words": words, "remains": b.id})
    ctx.move(b, g)
    ctx.patch(b, {"hidden": True, "buried_in": g.id})
    look(ctx, g)
    ctx.emit("buried", target=g, reach=1, by=me.id, grave=g.id, place=ground.id, body=b.id, words=words)
    ctx.emit("scene", target=ground.id, reach=1, text="The stooped woman in the stovepipe hat digs, steady as a clock, "
             "and fills the grave in, and says the words over it in a voice nobody else is meant to hear.")
    ctx.patch(me, {"post": ground.id, "routine_hold_until": ctx.t + 1800})
    ctx.remember(me, "Buried " + b.name + ", brought in from " + here.name + ".")
