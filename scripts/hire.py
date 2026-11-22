# hire: take someone here into your service, on their terms (see _hired). Asked bare, they name their price; with
# {"days": n}, coin buys n days; someone who wants a thing takes it from what you carry, and a favour (alone, or
# before a price) counts once the world has marked it done. Hiring again before the days run out adds days.
use("hired")

def deal(ctx, me, who):
    # {"go": False, "why": ...}: say the terms and what is missing; {"go": True, ...}: the hire; a string: refused
    offer = who.state.for_hire or {}
    p = ctx.params or {}
    h = who.state.hired or {}
    ours = h.get("by") == me.id and float(h.get("until") or 0) > ctx.t
    start = float(h.get("until")) if ours else ctx.t
    # a favour comes before any price: once to sign them on, and again for more days when the favour is all they take
    alone = not offer.get("wage") and not offer.get("wants")
    if offer.get("favour") and (not ours or alone) and not (who.state.favoured or {}).get(me.id):
        return {"go": False, "why": "The favour comes first (" + str(offer.get("favour")) + "), and it is not done yet"}
    if offer.get("wage"):
        if p.get("days") is None:
            return {"go": False, "why": "Hire them with params {\"days\": n}"}
        d = str(p.get("days"))
        if not d.isdigit() or int(d) < 1:
            return "days is a whole number of days, 1 or more"
        n = int(d)
        cost = int(offer.get("wage")) * n
        have = ctx.count(me, coin_kind(ctx))
        if have < cost:
            return (days_text(n) + " of " + who.name + " is " + money(cost) + ", and you have " +
                    (money(have) if have else "no coin"))
    elif offer.get("wants"):
        n = int(offer.get("days") or 1)
        cost = 0
        thing = held_thing(ctx, me, offer.get("wants"))
        if thing is None:
            return {"go": False, "why": "You carry no " + str(offer.get("wants")) + "; bring one and hire them again"}
    elif offer.get("favour"):
        n = int(offer.get("days") or 1)
        cost = 0
    else:
        return who.name + " has named no price"
    if start + n * day(ctx) - ctx.t > max_days(offer) * day(ctx) + 1:
        return who.name + " signs on for at most " + days_text(max_days(offer)) + " ahead"
    if not ours and len(mine(ctx, me)) >= keeps(ctx, me):
        names = ", ".join([x.name for x in mine(ctx, me)])
        return ("you keep " + str(keeps(ctx, me)) + " in your hire at once (1 + your Charisma modifier), and have: " +
                names + ". Let one go (dismiss) or wait for their days to end")
    out = {"go": True, "days": n, "cost": cost, "ours": ours, "start": start}
    if offer.get("wants"):
        out["thing"] = thing
    return out

def check(ctx):
    who = ctx.target
    me = ctx.actor
    if who.id == me.id:
        return "you cannot hire yourself"
    if not who.state.for_hire:
        return who.name + " is not for hire"
    if who.state.dead or who.state.down:
        return who.name + " is in no state to work for anyone"
    if who.state.asleep:
        return who.name + " is asleep: wake them first"
    if (me.state.hired or {}).get("by"):
        return "you are in someone's hire yourself, and a hireling hires nobody"
    h = who.state.hired or {}
    ours = h.get("by") == me.id and float(h.get("until") or 0) > ctx.t
    if h.get("by") and not ours and float(h.get("until") or 0) > ctx.t:
        return who.name + " is in someone else's hire already"
    if ctx.embodied(who) and not ours:
        return who.name + " has a mind of their own: talk terms with them"
    d = deal(ctx, me, who)
    if isinstance(d, str):
        return d
    return True

def apply(ctx):
    who = ctx.target
    me = ctx.actor
    offer = who.state.for_hire
    ask = offer.get("ask")
    terms = who.name + " asks " + price_text(offer) + (". " + who.name + ": \"" + ask + "\"" if ask else "")
    d = deal(ctx, me, who)
    if not d["go"]:
        ctx.log(terms + ". " + d["why"])
        return {"hired": False}
    n = d["days"]
    until = d["start"] + n * day(ctx)
    if d["cost"]:
        pay_coin(ctx, me, who, d["cost"])
    paid = money(d["cost"]) if d["cost"] else ""
    if d.get("thing") is not None:
        t = d["thing"]
        paid = t.name
        ctx.transfer(t, who, count=1 if ctx.count(t) > 1 else None)
    if offer.get("favour") and (who.state.favoured or {}).get(me.id):
        ctx.patch(who, {"favoured": {me.id: None}})  # spent
        paid = (paid + " and the favour") if paid else "the favour"
    if d["ours"]:
        ctx.patch(who, {"hired": {"until": until}})
    else:
        # their post waits for them: an idle body walks back to its post, and a hireling's place is beside the hirer
        ctx.patch(who, {"hired": {"by": me.id, "until": until, "since": ctx.t, "post": who.state.post}, "post": None})
    ctx.patch(me, {"hirelings": {who.id: until}})
    ctx.schedule(until - ctx.t, "hire_ends", target=who, payload={"by": me.id, "until": until})
    ctx.emit("hired_on", target=who, reach=1, by=me.id, who=who.id, name=who.name, days=n, until=until, paid=paid)
    if d["ours"]:
        ctx.remember(who, me.name + " paid for " + days_text(n) + " more of my time.")
        ctx.log(who.name + " stays in your hire " + days_text(n) + " longer, for " + paid)
        return {"hired": True, "until": until}
    if offer.get("line"):
        ctx.emit("scene", target=who.parent, reach=1, text=who.name + ": \"" + offer.get("line") + "\"")
    ctx.remember(who, me.name + " hired me for " + days_text(n) + ", for " + paid + ". I go where " + me.name +
                 " leads and do what they ask, within reason; I am still myself, and the hire ends when the days do.")
    seat = ""
    if not ctx.embodied(who):
        ctx.patch(who, {"follows": me.id})
        if offer.get("seat") is False or not who.state.seatable:
            # someone whose seat is kept for one player (Deloris, Ed's) joins as herself: no seat comes with the hire
            seat = ". They follow you, as themself: no seat comes with this hire"
        else:
            oid = ctx.offer_seat(who, me, why="in your hire for " + days_text(n) + ": they follow your lead, and stay themself")
            seat = (". They follow you. Their seat is offered to you (" + oid + "): claim_seat(\"" + oid + "\") gives "
                    "them an agent of their own, for as long as the hire lasts")
    ctx.log(who.name + " is in your hire for " + days_text(n) + ", for " + paid + seat)
    return {"hired": True, "until": until}
