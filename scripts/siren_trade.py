# Pelagie's trade (cast/q_siren.py), a rule on her: hand her a weapon or a piece of armour and she pays for it from
# her pouches, a pearl for a weapon or plain armour, a nugget of raw gold for coral armour (sea-coral does not rot).
# Anything else she thanks you for and keeps, puzzled. With three in hand she goes home: down the pier and under the
# harbour, for good. While someone plays her, the player decides and this keeps out of it. Her `armed` counts what she
# has been given; `armed_by` who gave it.

NEED = 3
UNDER = "Under the Harbour"
DOCKS = "The Docks"

def pouch(ctx, me, name):
    for c in ctx.children(me):
        if c.name == name and int(ctx.count(c)) > 0:
            return c
    return None

def place_named(ctx, name):
    for p in ctx.find(type="place", name=name, limit=3):
        if p.name == name:
            return p
    return None

def on(ctx, event):
    me = ctx.self
    if event.kind != "given" or event.target != me.id or ctx.embodied(me) or me.state.dead or me.state.gone_home:
        return
    item = ctx.get(event.payload.get("item"))
    giver = ctx.get(event.payload.get("by"))
    if item is None or giver is None or item.parent is None or item.parent.id != me.id:
        return
    st = item.state
    if not st.weapon and not st.armor:
        ctx.gesture("She turns the " + str(item.name).lower() + " over in her hands, puzzled, and holds it to her chest.",
                    to=giver.id)
        ctx.say("Thank you. I do not know what it is for. I wanted something sharp, or coral.", to=giver.id)
        return
    coral = "coral" in str(st.kind or "").lower() or "coral" in str(item.name).lower()
    pay = pouch(ctx, me, "Raw gold") if coral else None
    if pay is None:
        pay = pouch(ctx, me, "Pearls")
    if pay is None:
        pay = pouch(ctx, me, "Raw gold")
    n = int(me.state.armed or 0) + 1
    by = list(me.state.armed_by or [])
    by.append(giver.id)
    ctx.patch(me, {"armed": n, "armed_by": by})
    if pay is None:
        ctx.gesture("She feels in both pouches, finds them empty, and goes red to the ears.", to=giver.id)
        ctx.say("I have nothing left. I am so sorry. Nacre will remember you.", to=giver.id)
    else:
        what = "a nugget of raw gold" if pay.name == "Raw gold" else "a pearl"
        ctx.transfer(pay, giver, 1)
        ctx.gesture("She holds the " + str(item.name).lower() + " as if it might break, and presses " + what +
                    " into your hand.", to=giver.id)
        if coral:
            ctx.say("Coral. It will not rot. You do not know what you have done for us.", to=giver.id)
        else:
            ctx.say("Thank you. That is " + str(n) + ". I need " + str(NEED) + ".", to=giver.id)
    if n < NEED:
        return
    # three: she goes home, for good
    ctx.patch(me, {"gone_home": True, "routine_off": True})
    ctx.say("That is enough. I can go home now. Thank you. Thank you all.", to=giver.id)
    ctx.emit("scene", target=me.parent, reach=1,
             text="The barefoot woman gathers what she has been given into her arms, shawl and all, and goes down "
                  "toward the water without looking back.")
    under = place_named(ctx, UNDER)
    docks = place_named(ctx, DOCKS)
    if docks is not None:
        ctx.emit("scene", target=docks, reach=1,
                 text="A woman walks off the end of the pier into the black water, arms full of steel, and the swirls on "
                      "her skin shine blue under the surface all the way down.")
    if under is not None:
        ctx.move(me, under)
        ctx.patch(me, {"post": under.id})
