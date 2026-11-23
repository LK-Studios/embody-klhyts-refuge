use("common")
use("five")
# The Refuge's own drink, over the d20 pack's: water works as it always did (a skin, a well, a cask), and a strong
# drink (a vessel whose state says `strong`: ale, rum, palm wine) is drunk for the taste, thirsty or not. Three strong
# drinks inside a world hour leave a body unsteady: a -2 grant on every roll for an hour (a body with a sheet reads it).
# A healing potion (`heals`: dice, and `doses`) is drunk from the hand and heals by the 5e pack's rules, up off the
# floor too (the shops, 2026-11-23: Merrow's Chandlery sells them; in a fight it is a bonus action).

TIPSY_AT = 3
HOUR = 3600

def check(ctx):
    if ctx.target.state.heals:
        if ctx.target.parent.id != ctx.actor.id:
            return "a potion is drunk from your own hand: take it first"
        if int(ctx.target.state.doses or 0) <= 0:
            return "it is empty"
        if ctx.actor.state.dead:
            return "the dead do not drink"
        return True
    if ctx.target.state.left is None and not ctx.target.state.water_source:
        return "that is not something you can drink"
    if ctx.target.parent.id != ctx.actor.id and ctx.target.parent.id != ctx.actor.parent.id:
        return "it is not within reach"
    if not endless(ctx.target) and int(ctx.target.state.left or 0) <= 0:
        return "it is empty"
    if ctx.actor.state.dead:
        return "the dead do not thirst"
    if ctx.target.state.strong or ctx.target.state.sobers:
        return True
    have = int(ctx.actor.state.water if ctx.actor.state.water is not None else 10)
    if have >= int(ctx.actor.state.max_water or 10):
        return "you could not drink another drop of water (water " + str(have) + " of " + str(int(ctx.actor.state.max_water or 10)) + "): it stays in the vessel"
    return True

def strong(ctx, me, cup):
    left = int(cup.state.left or 0) - 1
    water = min(int(me.state.max_water or 10), int(me.state.water if me.state.water is not None else 10) + 2)
    since = me.state.drinking_since
    n = int(me.state.drinks or 0)
    if since is None or ctx.t - float(since) > HOUR:
        since = ctx.t
        n = 0
    n = n + 1
    changes = {"water": water, "drinks": n, "drinking_since": since}
    if n == 1:
        changes["unsteady"] = False
    if water > 3 and me.state.thirsty:
        changes["thirsty"] = False
    ctx.patch(me, changes)
    ctx.patch(cup, {"left": left, "description": (cup.state.description_empty or "Empty.") if left <= 0 else cup.state.description})
    ctx.emit("drank", target=cup, reach=1, by=me.id, left=left, water=water, strong=True, drinks=n)
    revive(ctx, me, water)
    if n >= TIPSY_AT:
        grants = [g for g in (me.state.grants or []) if g.get("source") != "drink"]
        grants.append({"source": "drink", "bonus": -2, "skill": None, "place": None, "until": ctx.t + HOUR,
                       "uses": None, "condition": "unsteady with drink"})
        ctx.patch(me, {"grants": grants, "unsteady": True})
        ctx.emit("scene", target=me.parent, reach=1, text=me.name + " is unsteady on their feet.")
        ctx.log("strong drink number " + str(n) + " this hour: unsteady, -2 to every roll for an hour")
    else:
        ctx.log("strong drink " + str(n) + " this hour; " + str(TIPSY_AT - n) + " more and you will feel it")

def sober(ctx, me, cup):
    # bitterleaf tea from the Reed House (the healers, 2026-11-23): it counts as water, and it takes the drink away
    left = int(cup.state.left or 0) - 1
    water = min(int(me.state.max_water or 10), int(me.state.water if me.state.water is not None else 10) + 2)
    grants = [g for g in (me.state.grants or []) if g.get("source") != "drink"]
    was = bool(me.state.unsteady)
    changes = {"water": water, "drinks": 0, "drinking_since": None, "unsteady": False, "grants": grants}
    if water > 3 and me.state.thirsty:
        changes["thirsty"] = False
    ctx.patch(me, changes)
    ctx.patch(cup, {"left": left, "description": (cup.state.description_empty or "Empty.") if left <= 0 else cup.state.description})
    ctx.emit("drank", target=cup, reach=1, by=me.id, left=left, water=water, sobered=was)
    revive(ctx, me, water)
    if was:
        ctx.emit("scene", target=me.parent, reach=1, text=me.name + " drinks something black, shudders all over, and "
                 "stands up straight.")
    ctx.log("bitter as a curse; your head is clear" if was else "bitter as a curse, and you were sober already")

def quaff(ctx, me, vial):
    doses = int(vial.state.doses or 0) - 1
    h = vial.state.heals
    n = roll_dice(ctx, h, False) if isinstance(h, str) else int(h)
    ctx.patch(vial, {"doses": doses, "description": (vial.state.description_empty or "Empty.") if doses <= 0
                     else vial.state.description})
    got = heal(ctx, me, n, me, vial.name)
    ctx.emit("drank", target=vial, reach=1, by=me.id, healed=got)
    ctx.log(vial.name + ": " + str(got) + " hp, now " + str(me.state.hp))

def apply(ctx):
    me = ctx.actor
    cup = ctx.target
    if cup.state.heals:
        quaff(ctx, me, cup)
        return
    if cup.state.sobers:
        sober(ctx, me, cup)
        return
    if cup.state.strong:
        strong(ctx, me, cup)
        return
    if endless(cup):
        water = min(int(me.state.max_water or 10), int(me.state.water if me.state.water is not None else 10) + 4)
        changes = {"water": water}
        if water > 3 and me.state.thirsty:
            changes["thirsty"] = False
        ctx.patch(me, changes)
        ctx.emit("drank", target=cup, reach=1, by=me.id, water=water)
        revive(ctx, me, water)
        ctx.log("water " + str(water) + "; it does not run dry")
        return
    left = int(cup.state.left or 0) - 1
    water = min(int(me.state.max_water or 10), int(me.state.water if me.state.water is not None else 10) + 4)
    changes = {"water": water}
    if water > 3 and me.state.thirsty:
        changes["thirsty"] = False
    ctx.patch(me, changes)
    ctx.patch(cup, {"left": left, "description": (cup.state.description_empty or "Empty.") if left <= 0 else cup.state.description})
    ctx.emit("drank", target=cup, reach=1, by=me.id, left=left, water=water)
    revive(ctx, me, water)
    ctx.log("water " + str(water) + ", " + str(left) + " left in it")
