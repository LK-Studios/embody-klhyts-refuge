# Hiring (owner, 2026-11-22): the one way a player brings a second agent into the Refuge. A person the world marks
# `for_hire` names their price, and each names their own: coin by the day (a few coppers or a fortune), a thing they
# want handed over, or a favour the world has marked done for you. A hire offers the hirer a seat for that person
# (ctx.offer_seat), which claim_seat turns into a sub-agent's paste; unplayed, the hireling follows the hirer. A
# character keeps 1 + their Charisma modifier hirelings at once (at least one), and a hireling hires nobody. The days
# run out, the hirer dismisses them, or they die: the hire ends and the seat goes back to the world.
#
# for_hire: {"wage": copper a day, paid up front | "wants": a thing's name or kind | "favour": what they want done,
#            "days": what a thing or a favour buys (default 1), "max_days": the longest ahead they sign on for
#            (default 7), "line": said when hired, "ask": said when the terms are asked or not met}
# favoured: {body id: true}, on the hireling: favours done, set by the narrator or a story rule, spent by a hire.
# hired: {"by", "until", "since"}, on the hireling; hirelings: {id: until}, on the hirer.

use("five")

def coin_kind(ctx):
    return ctx.root().state.coin_kind or "coin"

def money(n):
    # copper counted out as gold, silver and copper: 100 cp to the gold piece, 10 to the silver
    n = int(n)
    if n <= 0:
        return "nothing"
    parts = []
    if n // 100:
        parts.append(str(n // 100) + "gp")
    if (n % 100) // 10:
        parts.append(str((n % 100) // 10) + "sp")
    if n % 10:
        parts.append(str(n % 10) + "cp")
    return " ".join(parts)

def pay_coin(ctx, payer, to, price):
    # the coin moves hand to hand, from whatever stacks of it the payer carries (not five's `pay`, the turn's economy)
    kind = coin_kind(ctx)
    owed = price
    for it in payer.children():
        if owed <= 0:
            break
        if it.state.kind != kind and (it.name or "").lower() != kind:
            continue
        n = min(owed, ctx.count(it))
        ctx.transfer(it, to, count=n)
        owed = owed - n

def day(ctx):
    return ctx.day_seconds()

def days_text(n):
    n = int(n)
    return "a day" if n == 1 else str(n) + " days"

def max_days(offer):
    return int(offer.get("max_days") or 7)

def price_text(offer):
    first = ("a favour first (" + str(offer.get("favour")) + "), then ") if offer.get("favour") else ""
    if offer.get("wage"):
        return first + money(offer.get("wage")) + " a day, paid up front"
    if offer.get("wants"):
        return first + str(offer.get("wants")) + ", for " + days_text(offer.get("days") or 1)
    if offer.get("favour"):
        return "a favour (" + str(offer.get("favour")) + "), for " + days_text(offer.get("days") or 1)
    return "nothing anyone has named"

def keeps(ctx, who):
    # how many hirelings a character keeps at once: 1 + their Charisma modifier, at least one
    return max(1, 1 + amod(who, "cha"))

def mine(ctx, who):
    # the hirelings whose days are still running for this body
    out = []
    for hid, until in (who.state.hirelings or {}).items():
        h = ctx.get(hid)
        if h is not None and (h.state.hired or {}).get("by") == who.id and float(until or 0) > ctx.t:
            out.append(h)
    return out

def held_thing(ctx, who, want):
    # a thing the hirer carries that answers to the name or kind the hireling wants
    w = str(want or "").lower()
    for it in who.children():
        if (it.name or "").lower() == w or str(it.state.kind or "").lower() == w:
            return it
    for it in who.children():
        if w and w in (it.name or "").lower():
            return it
    return None

def end_hire(ctx, who, why):
    # the days are done, the hirer let them go, or they died: the seat goes back and they stop following
    h = who.state.hired or {}
    boss = ctx.get(h.get("by")) if h.get("by") else None
    ctx.withdraw_seat(who, why=why)
    st = {"hired": None}
    if h.get("post"):
        st["post"] = h.get("post")  # back to where they kept before the hire; their idle routine walks them home
    if boss is not None and who.state.follows == boss.id:
        st["follows"] = None
    ctx.patch(who, st)
    if boss is not None:
        ctx.patch(boss, {"hirelings": {who.id: None}})
        ctx.emit("hire_ended", target=boss, reach=0, who=who.id, name=who.name, why=why,
                 text=who.name + " is no longer in your hire: " + why + ".")
    if not who.state.dead:
        ctx.remember(who, "My hire " + ("with " + boss.name + " " if boss is not None else "") + "is over: " + why + ".")
