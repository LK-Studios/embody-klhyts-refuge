# The Refuge's storyline, on the world root. The Story entity keeps the facts; every branch checks a fact, never a
# stage, so play off the rails still finds an end. What happened (invented for this build, see notes/invented.md):
# four nights ago Klhyt had it out with the Custodian at the Stripperwitch over skimmed harbour dues. Dominico's men
# walked him out, and he has been tied up in the bonded warehouse at the docks ever since, crated for Catan aboard the
# Emerald Eye (Danny DeVito's ship; he likes gold) on the one o'clock tide. Meanwhile Dominico squeezes Fat Gog: the Stripperwitch's books by midnight, or else.

CLUE_ITEMS = ["letter", "passage", "ring", "tally"]
DOCKS_ARRIVAL = ("Klhyts Refuge comes at you all at once: tar and fish and frying onions, six kinds of music from six "
                 "taverns, and lamplight on wet planks. Out past the harbour mouth a Xoton trader rides at anchor, too many "
                 "masts for one ship. Nobody asks where you came from. That is the point of the place.")

def story(ctx):
    return ctx.find(type="story", limit=1)[0]

def seen(ctx, who, fallback):
    # someone as a stranger sees them (their `seen_as`), capitalised for the start of a line: the story tells what the
    # room sees, and a name comes only when someone says it (owner, 2026-11-23)
    e = ctx.get(who) if who else None
    t = (e.state.seen_as if e is not None else None) or fallback
    return t[:1].upper() + t[1:]

def scene(ctx, place, text):
    if place:
        ctx.emit("scene", target=place, reach=1, text=text)

def walk(ctx, who, dest):
    # an NPC crossing town on the story's word: the room they leave and the room they reach both see it
    p = ctx.get(who)
    if p is None or p.state.down or p.state.dead or p.parent.id == dest or ctx.embodied(p):
        return False
    ctx.move(p, dest)
    # their post moves with them, or their idle walk takes them straight back; their day waits half an hour
    ctx.patch(p, {"post": dest, "routine_hold_until": ctx.t + 1800})
    ctx.emit("arrived", target=dest, reach=-1, who=p.id, place=dest)
    return True

def come_ashore(ctx, st, who):
    # each one who comes to play gets the town coming at them once, told to them alone: the pier has watched boats come
    # in all evening, and the line is written to the one stepping off
    have = list(st.ashore or [])
    if who.id in have:
        return
    have.append(who.id)
    ctx.patch(story(ctx), {"ashore": have, "seen_docks": True})
    ctx.emit("scene", target=who.id, reach=0, text=DOCKS_ARRIVAL)

def tell_town(ctx, flag):
    # the town hears: every person carries the news as a flag their own lines answer to (cast lines use if_state)
    for p in ctx.find(type="person", limit=500):
        if not p.state.get(flag):
            ctx.patch(p, {flag: True})

def add_clue(ctx, st, name):
    have = list(st.clues or [])
    if name in have:
        return
    have.append(name)
    ctx.patch(story(ctx), {"clues": have})

def gog_learns(ctx, st, by, what):
    if st.gog_knows:
        return
    ctx.patch(story(ctx), {"gog_knows": True, "gog_told_by": by})
    gog = ctx.get(st.gog)
    scene(ctx, gog.parent.id, seen(ctx, st.gog, "the huge old lizardman") + " goes very still. Then he laughs, low and long, and it is not a happy sound. "
          "\"I carried that man up the sand with his tongue black from thirst. And the Custodian puts him in a crate.\" "
          "He slides a carved bone marker across the table. "
          "\"Show that to whoever is minding the warehouse. Bring Klhyt to me breathing.\"")
    ctx.spawn("thing", by, name="Fat Gog's marker", state={
        "marker": "gog", "portable": True, "bulk": 0,
        "description": "A carved bone marker, a fat lizard grinning on one side. Everyone at the docks knows whose it is."})
    ctx.patch(gog, {"gog_knows": True})

def dominico_backs_off(ctx, st, why):
    if st.dominico_backed:
        return
    ctx.patch(story(ctx), {"dominico_backed": True, "dominico_why": why})
    dom = ctx.get(st.dominico)
    ctx.patch(dom, {"backed_off": True})
    scene(ctx, dom.parent.id, seen(ctx, st.dominico, "the man in the black coat") + " closes his hand slowly, the way a man puts away a knife. \"Tell Gog,\" he says, "
          "\"the midnight business is off.\"")
    brask = ctx.get(st.brask)
    if brask is not None and not brask.state.left_post and not brask.state.down and not ctx.embodied(brask):
        ctx.patch(brask, {"left_post": "called off", "off_post": True})
        scene(ctx, brask.parent.id, "A runner in black trots down the pier and says something in the ear of " + seen(ctx, st.brask, "the big man on the bollard").lower() + ". "
              "He spits, shrugs, hangs the warehouse key on a nail by the door and leaves his post.")
        for it in brask.children():
            if it.name == "Warehouse key":
                ctx.move(it, brask.parent)
        walk(ctx, st.brask, st.ogre)

def klhyt_free(ctx, st, by):
    if st.klhyt_freed:
        return
    ctx.patch(story(ctx), {"klhyt_freed": True, "freed_by": by})
    klhyt = ctx.get(st.klhyt)
    if klhyt.state.look_free:
        ctx.patch(klhyt, {"look": klhyt.state.look_free})
    scene(ctx, klhyt.parent.id, "The grey-bearded man rubs his wrists and stands, unsteady, a big man gone thin. \"Four nights,\" he says. "
          "\"Four nights I've listened to the tide. Walk me to the square.\"")
    ctx.schedule(120, "klhyt_returns", target=ctx.root().id, payload={"by": by})

def klhyt_returns(ctx, st):
    klhyt = ctx.get(st.klhyt)
    if klhyt is None or klhyt.state.dead or st.custodian_exposed:
        return
    walk(ctx, st.klhyt, st.square)
    ctx.patch(story(ctx), {"custodian_exposed": True, "outcome": "Klhyt is home, and the Custodian's skimming is out in the square"})
    scene(ctx, st.square, "The big grey-bearded man from the warehouse climbs the Town Hall steps with the lamps behind "
          "him. People come out of all six taverns shouting his name, Klhyt, Klhyt, to see if it's really him. It is. He tells them where the harbour dues went, and whose name is on every tally.")
    tell_town(ctx, "klhyt_home")
    disgrace(ctx, st)
    if not st.dominico_backed:
        dominico_backs_off(ctx, story(ctx).state, "his patron fell")
    ctx.patch(ctx.root(), {"story": "complete"})

def disgrace(ctx, st):
    # the Custodian, found out: the coat, the empty space round him, and a smaller day (his `routine_disgraced`)
    cust = ctx.get(st.custodian)
    if cust is None or cust.state.disgraced:
        return
    look = cust.state.look_disgraced or "A thin, neat man in a good grey coat gone suddenly too warm, with nobody standing near him."
    changes = {"disgraced": True, "look": look, "description": look}
    if cust.state.routine_disgraced:
        changes["routine"] = cust.state.routine_disgraced
        changes["routine_key"] = None
    ctx.patch(cust, changes)

# Ithriel's household, the five the Moonmoth waits for. Asked about passage, Ithriel and her four fall in behind the
# one who asked, their usual places kept for them (or the idle walk would take them straight home); at the docks each
# goes up the gangplank on their own, and the story keeps that they got away.
# Whole words, so "go" is never found in "good": a player saying it is time to leave counts too (2026-11-23).
ESCORT_TOPICS = ["passage", "ship", "ships", "moonmoth", "boat", "boats", "pier", "walk", "escort", "catan", "help",
                 "follow", "lead", "gather", "ready"]

def words(text):
    t = str(text).lower()
    for ch in [",", ".", "?", "!", ";", ":", "'", "\"", "(", ")"]:
        t = t.replace(ch, " ")
    return t.split()

def household(ctx, st):
    out = []
    for x in (st.household or []):
        e = ctx.get(x)
        if e is not None:
            out.append(e)
    return out

def escort_begins(ctx, st, by):
    if st.escort_by or st.elves_aboard:
        return
    ith = ctx.get(st.ithriel)
    me = ctx.get(by)
    if ith is None or me is None or ith.parent is None or ith.state.dead or ith.state.down:
        return
    came = []
    for e in household(ctx, st):
        if e.parent is None or e.parent.id != ith.parent.id or e.state.dead or e.state.down or ctx.embodied(e):
            continue
        ctx.patch(e, {"follows": me.id, "post": None})
        came.append(e.id)
    if not came:
        return
    ctx.patch(story(ctx), {"escort_by": me.id, "escorted": came})
    scene(ctx, ith.parent.id, seen(ctx, st.ithriel, "the hooded elf with the book") + " closes her book and stands. Around the room hooded figures rise from the corners and "
          "fall in behind you, quiet as smoke: her household. \"To the pier, then,\" she says. \"And not past the "
          "Apothecary, if you can help it.\"")
    ctx.remember(ith, me.name + " is walking my household to the Moonmoth.")

def boards(ctx, st, who):
    # one of the household, at the docks behind the one walking them, goes up the gangplank on their own
    ctx.move(who, st.moonmoth)
    ctx.patch(who, {"follows": None, "post": st.moonmoth, "home": st.moonmoth, "aboard": True, "routine_off": True})
    ctx.emit("arrived", target=st.moonmoth, reach=1, who=who.id, place=st.moonmoth, boarded=True)
    left = []
    for x in (st.escorted or []):
        e = ctx.get(x)
        if e is not None and not e.state.dead and (e.parent is None or e.parent.id != st.moonmoth):
            left.append(x)
    if left or st.elves_aboard:
        return
    ctx.patch(story(ctx), {"elves_aboard": True, "elves_walked_by": st.escort_by})
    scene(ctx, st.docks, seen(ctx, st.ithriel, "the hooded elf") + " is the last up the gangplank. At the top she turns. \"You walked with us,\" she says. "
          "\"Keep the leaf. While the Moonmoth is in harbour, she will open to you.\" Then she is gone among the bundles, "
          "and the empty places on the deck are empty no longer.")
    ith = ctx.get(st.ithriel)
    walker = ctx.get(st.escort_by)
    if ith is not None:
        ctx.remember(ith, "My household is aboard the Moonmoth" + ((", walked there by " + walker.name) if walker else "") + ".")

def on(ctx, event):
    st = story(ctx).state
    k = event.kind
    p = event.payload or {}
    if k == "act":
        # everyone who comes to play starts at the docks and never walks in: their first deed there is their arrival
        who = ctx.get(event.actor) if event.actor else None
        if who is not None and ctx.embodied(who) and who.parent is not None and who.parent.id == st.docks:
            come_ashore(ctx, st, who)
        return
    if k == "arrived":
        place = p.get("place")
        who = ctx.get(p.get("who"))
        if (who is not None and place == st.docks and st.escort_by and who.id in list(st.escorted or [])
                and who.state.follows == st.escort_by):
            boards(ctx, st, who)
            return
        if who is None or not ctx.embodied(who):
            return
        if place == st.docks:
            come_ashore(ctx, st, who)
        elif place == st.warehouse and not st.klhyt_found and not st.shipped:
            ctx.patch(story(ctx), {"klhyt_found": True})
            scene(ctx, st.warehouse, "Between the bales and the stacked crates, in the one dry corner, a big grey-bearded man "
                  "sits tied to a chair beside an open crate with air holes drilled in the lid. He lifts his head. "
                  "\"Well,\" he says. \"You're not Dominico's. Klhyt. I founded this town, for my sins.\"")
    elif k == "read":
        item = ctx.get(event.target)
        if item is not None and item.state.clue:
            add_clue(ctx, st, item.state.clue)
    elif k == "taken":
        item = ctx.get(event.target)
        if item is not None and item.state.clue:
            add_clue(ctx, st, item.state.clue)
    elif k == "talked":
        about = str(p.get("about", "")).lower()
        if event.target == st.river and ("klhyt" in about or "mayor" in about or "custodian" in about or "founder" in about):
            add_clue(ctx, st, "river")
        elif event.target == st.teague and ("crate" in about or "warehouse" in about or "klhyt" in about or "custodian" in about):
            add_clue(ctx, st, "teague")
        elif event.target == st.tully and ("brask" in about or "warehouse" in about or "crate" in about or "job" in about):
            add_clue(ctx, st, "tully")
        elif event.target == st.ithriel and p.get("by"):
            said = words(about)
            for w in ESCORT_TOPICS:
                if w in said:
                    escort_begins(ctx, st, p.get("by"))
                    break
    elif k == "shown":
        item = ctx.get(p.get("item"))
        if item is None or item.state.clue not in CLUE_ITEMS:
            return
        if event.target == st.gog and item.state.clue != "tally":
            gog_learns(ctx, st, p.get("by"), item.state.clue)
        elif event.target == st.dominico and item.state.clue in ["passage", "letter"]:
            dominico_backs_off(ctx, st, "shown the " + item.state.clue)
        elif event.target == st.custodian and not st.custodian_bribe and item.state.clue in ["letter", "passage", "tally"]:
            ctx.patch(story(ctx), {"custodian_bribe": True})
            shower = ctx.get(p.get("by"))
            scene(ctx, ctx.get(st.custodian).parent.id, "He reads it, folds it, and smiles with half his mouth. "
                  "A heavy purse appears on the table between you. \"Accounts are complicated,\" he says. "
                  "\"Five gold for your trouble, and you never learned to read.\"")
            if shower is not None:
                purse = ctx.spawn("thing", shower, name="Coin", state={
                    "kind": "cp", "count": 500, "portable": True, "bulk": 0,
                    "description": "Mixed coin, counted in copper: 100 to the gold piece, 10 to the silver."})
                ctx.merge(purse)
    elif k == "cowed" or k == "agreed":
        if event.target == st.dominico:
            dominico_backs_off(ctx, st, k)
    elif k == "freed":
        if event.target == st.klhyt:
            klhyt_free(ctx, st, p.get("by"))
    elif k in ["pick_failed", "break_failed", "lock_broken"]:
        if p.get("holder") != st.warehouse:
            return
        brask = ctx.get(st.brask)
        if brask is None or brask.state.left_post or brask.state.down or brask.state.dead or ctx.embodied(brask):
            return
        if brask.parent.id != st.docks:
            return
        ctx.patch(brask, {"attacked_by": p.get("by"), "attacked_at": ctx.t})
        scene(ctx, st.docks, seen(ctx, st.brask, "the big man on the bollard") + " hears it. He comes off the bollard with his cudgel already swinging. \"OI.\"")
    elif k == "klhyt_returns":
        klhyt_returns(ctx, st)
    elif k == "ultimatum":
        if st.dominico_backed or st.klhyt_freed:
            return
        ctx.patch(story(ctx), {"ultimatum_given": True})
        walk(ctx, st.dominico, st.stripperwitch)
        scene(ctx, st.stripperwitch, "The music falls off a note. " + seen(ctx, st.dominico, "a lean man in a black coat") + " has come in, alone, which is worse than with "
              "company. He stops at the big lizardman's table and doesn't sit. \"The books, Gog. Every ledger, every name, every cut. "
              "On my table at the Apothecary by midnight. After midnight I stop asking.\" He nods to the woman behind the bar, and leaves.")
        ctx.schedule(300, "dominico_back", target=ctx.root().id)
    elif k == "dominico_back":
        walk(ctx, st.dominico, st.apothecary)
    elif k == "custodian_out":
        if st.custodian_exposed:
            return
        if walk(ctx, st.custodian, st.stripperwitch):
            scene(ctx, st.hall, seen(ctx, st.custodian, "the thin man with the keys") + " locks the office door, checks it twice, pulls up his collar and goes out into the night.")
            scene(ctx, st.stripperwitch, seen(ctx, st.custodian, "a thin, neat man in a grey coat") + " comes in by the side door, the way a man does who is not here. "
                  "He takes the red booth. The woman behind the bar brings him wine without being asked.")
    elif k == "midnight":
        ctx.patch(ctx.root(), {"ambient": {"time_of_day": "midnight", "light": "the taverns' lamps and not much else"}})
        if st.dominico_backed or st.klhyt_freed:
            scene(ctx, st.stripperwitch, "The midnight bell goes. Nobody comes for the books.")
            return
        if st.gog_knows:
            dominico_backs_off(ctx, st, "Gog was ready for him")
            scene(ctx, st.stripperwitch, "At the midnight bell four hard men in black come to the Stripperwitch's door, look at "
                  "who is waiting inside for them, and find somewhere else to be.")
            return
        ctx.patch(story(ctx), {"guild_hit": True})
        ctx.patch(ctx.get(st.stripperwitch), {"description":
            "Red velvet, slashed. The mirror behind the bar is in pieces and the stage curtain is down. The woman who runs the bar is sweeping "
            "glass with her jaw set. The huge lizardman in the white suit sits where he always sits, bleeding into a napkin, saying nothing at all."})
        scene(ctx, st.stripperwitch, "The midnight bell, and then the door comes in. men in black go through the "
              "Stripperwitch like weather: the mirror, the bottles, the curtain, two of the house's people and the big lizardman himself. "
              "Nobody kills anybody. That is the message.")
        tell_town(ctx, "guild_hit")
    elif k == "siren_rises":
        siren = ctx.get(st.siren)
        if siren is None or siren.state.dead:
            return
        ctx.move(siren, st.docks)
        ctx.patch(siren, {"post": st.docks, "hidden": False})
        ctx.emit("arrived", target=st.docks, reach=-1, who=siren.id, place=st.docks)
        scene(ctx, st.docks, "The black water by the end of the pier goes very still. Then a woman rises out of it, climbs the "
              "ladder with water pouring off her like silk, wrings out her hair and walks up into town as if she does this "
              "every night. She doesn't. Every fisherman on the pier has stopped breathing.")
    elif k == "siren_sings":
        if walk(ctx, st.siren, st.stripperwitch):
            scene(ctx, st.stripperwitch, "The pale woman from the harbour steps onto the little stage. The fiddler stops. The woman behind the bar puts the glass down. "
                  "Then she sings, and for as long as it lasts nobody in the Stripperwitch remembers owing anybody anything.")
            for place in [st.square, st.market, st.omberhulk]:
                scene(ctx, place, "From the direction of the Stripperwitch comes a voice so beautiful that people stop in the "
                      "street with their mouths open. Somebody says it's the siren. Somebody always does, and once in a long while they're right.")
    elif k == "siren_leaves":
        siren = ctx.get(st.siren)
        if siren is None or siren.state.dead or ctx.embodied(siren):
            return
        scene(ctx, siren.parent.id, "The pale singer gathers her coins in a sealskin purse, says she has an exam in a fortnight, and "
              "goes back down toward the water.")
        ctx.move(siren, st.under)
        ctx.patch(siren, {"post": st.under})
        scene(ctx, st.docks, "Something slips off the end of the pier into the black water without a splash.")
    elif k == "small_hours":
        ctx.patch(ctx.root(), {"ambient": {"time_of_day": "the small hours", "weather": "the heat finally breaking; rain on the roofs"}})
    elif k == "tide":
        if st.klhyt_freed or st.shipped:
            return
        ctx.patch(story(ctx), {"shipped": True, "outcome": "Klhyt went out on the tide in a crate, bound for Catan"})
        tell_town(ctx, "klhyt_shipped")
        klhyt = ctx.get(st.klhyt)
        if klhyt is not None and klhyt.parent.id == st.warehouse:
            ctx.move(klhyt, st.packet)
            ctx.patch(klhyt, {"post": st.packet, "routine_off": True})
            scene(ctx, st.warehouse, "Two men in black come in with a lantern, nail the lid down on the big crate and "
                  "carry it out between them. It is heavy. It knocks, once, from the inside.")
        ship = ctx.get(st.emerald) if st.emerald else None
        if ship is not None and ship.parent.id == st.docks:
            ctx.move(ship, st.packet)
            for cap in ctx.find(type="person", name="DeVito", limit=1):  # her small captain sails with her
                if cap.parent is not None and cap.parent.id == st.docks and not ctx.embodied(cap):
                    ctx.move(cap, st.packet)
                    ctx.patch(cap, {"post": st.packet, "routine_off": True})
        scene(ctx, st.docks, "On the one o'clock tide the Emerald Eye slips her lines and slides out past the Xoton trader, "
              "low in the water, a big crate lashed on her deck and her small captain counting gold at the rail. By morning "
              "she is a light on the horizon, and then not even that.")
        ctx.patch(ctx.root(), {"story": "lost"})
