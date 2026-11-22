def coin_kind(ctx):
    # what money is called in this world: the root's `coin_kind`, else "coin"
    return ctx.root().state.coin_kind or "coin"

def money(n):
    # copper counted out as gold, silver and copper: 100 cp to the gold piece, 10 to the silver
    n = int(n)
    if n <= 0:
        return "free"
    parts = []
    if n // 100:
        parts.append(str(n // 100) + "gp")
    if (n % 100) // 10:
        parts.append(str((n % 100) // 10) + "sp")
    if n % 10:
        parts.append(str(n % 10) + "cp")
    return " ".join(parts)

def words(text):
    t = str(text).lower()
    for ch in [",", ".", "?", "!", ";", ":", "'", "\""]:
        t = t.replace(ch, " ")
    return t.split()

def entry_for(ctx, seller, want):
    # a `sells` key is one word or several joined with |: "ale|beer|mug". Whole words only, so "rum" is not "drum".
    asked = words(want)
    best = None
    best_score = 0
    for key, entry in (seller.state.sells or {}).items():
        s = 0
        for alias in key.split("|"):
            a = alias.strip().lower()
            if " " in a:
                if a in " ".join(asked):
                    s = s + 10 + len(a)
            elif a in asked:
                s = s + 10 + len(a)
        if s > best_score:
            best = [key, entry]
            best_score = s
    return best

def menu(ctx, seller):
    kind = coin_kind(ctx)
    parts = []
    for key, entry in (seller.state.sells or {}).items():
        stock = entry.get("stock")
        if stock is not None and int(stock) <= 0:
            continue
        parts.append(key.split("|")[0] + " (" + money(entry.get("price", 0)) + ")")
    if not parts:
        return seller.name + " has nothing to sell right now"
    return seller.name + " sells: " + ", ".join(parts)

def check(ctx):
    seller = ctx.target
    if seller.id == ctx.actor.id:
        return "you cannot buy from yourself"
    if not seller.state.sells:
        return seller.name + " is not selling anything"
    if seller.state.dead or seller.state.down:
        return seller.name + " is in no state to serve anyone"
    if seller.state.asleep:
        return seller.name + " is asleep: wake them first"
    if seller.state.closed:
        return str(seller.state.closed)
    if not ctx.params or not ctx.params.get("item"):
        return True  # asked bare: apply reads out what they sell, and nothing changes hands
    found = entry_for(ctx, seller, ctx.params.get("item"))
    if found is None:
        return seller.name + " does not sell that. " + menu(ctx, seller)
    entry = found[1]
    stock = entry.get("stock")
    if stock is not None and int(stock) <= 0:
        return "the " + found[0].split("|")[0] + " is all gone. " + menu(ctx, seller)
    kind = coin_kind(ctx)
    price = int(entry.get("price", 0))
    have = ctx.count(ctx.actor, kind)
    if have < price:
        return "it costs " + money(price) + " and you have " + (money(have) if have else "no coin")
    return True

def pay(ctx, buyer, seller, price):
    # the coin moves hand to hand, from whatever stacks of it the buyer carries
    kind = coin_kind(ctx)
    owed = price
    for it in buyer.children():
        if owed <= 0:
            break
        if it.state.kind != kind and (it.name or "").lower() != kind:
            continue
        n = min(owed, ctx.count(it))
        ctx.transfer(it, seller, count=n)
        owed = owed - n

def apply(ctx):
    seller = ctx.target
    buyer = ctx.actor
    if not ctx.params or not ctx.params.get("item"):
        have = ctx.count(buyer, coin_kind(ctx))
        ctx.log(menu(ctx, seller) + ". Buy one with params {\"item\": ...}; you have " + (money(have) if have else "no coin"))
        return
    found = entry_for(ctx, seller, ctx.params.get("item"))
    key = found[0]
    entry = found[1]
    price = int(entry.get("price", 0))
    if price > 0:
        pay(ctx, buyer, seller, price)
    state = dict(entry.get("state") or {})
    state["portable"] = state.get("portable", True)
    state["bought_from"] = seller.id
    got = ctx.spawn(entry.get("type", "thing"), buyer, name=entry.get("name", key.split("|")[0]), state=state)
    if entry.get("stock") is not None:
        ctx.patch(seller, {"sells": {key: {"stock": int(entry.get("stock")) - 1}}})
    ctx.emit("bought", target=seller, reach=1, by=buyer.id, item=got.id, name=got.name, price=price,
             coin=coin_kind(ctx))
    line = entry.get("line")
    if line:
        ctx.emit("scene", target=seller.parent, reach=1, text=line)
    ctx.log("bought " + got.name + " for " + money(price))
