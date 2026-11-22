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

def scene(ctx, place, text):
    if place:
        ctx.emit("scene", target=place, reach=1, text=text)

def walk(ctx, who, dest):
    # an NPC crossing town on the story's word: the room they leave and the room they reach both see it
    p = ctx.get(who)
    if p is None or p.state.down or p.state.dead or p.parent.id == dest or ctx.embodied(p):
        return False
    ctx.move(p, dest)
    ctx.patch(p, {"post": dest})  # their post moves with them, or their idle routine walks them straight back
    ctx.emit("arrived", target=dest, reach=-1, who=p.id, place=dest)
    return True

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
    scene(ctx, gog.parent.id, "Fat Gog goes very still. Then he laughs, low and long, and it is not a happy sound. "
          "\"I carried that man up the sand with his tongue black from thirst. And the Custodian puts him in a crate.\" "
          "He slides a carved bone marker across the table. "
          "\"Show that to whoever is minding the warehouse. Bring Klhyt to me breathing.\"")
    ctx.spawn("thing", by, name="Fat Gog's marker", state={
        "marker": "gog", "portable": True, "bulk": 0,
        "description": "A carved bone marker, a fat lizard grinning on one side. Everyone at the docks knows whose it is."})
    ctx.patch(gog, {"dialog": {
        "klhyt|mayor|founder|warehouse": "\"You have my marker. Use it. The warehouse, before the tide.\"",
        "custodian": "\"The Custodian and I will have a conversation. A long one. After.\"",
        "dominico": "\"Dominico runs errands for a thief. When he hears whose errand, we will see if he still wants my books.\""}})

def dominico_backs_off(ctx, st, why):
    if st.dominico_backed:
        return
    ctx.patch(story(ctx), {"dominico_backed": True, "dominico_why": why})
    dom = ctx.get(st.dominico)
    ctx.patch(dom, {"dialog": {
        "gog|guild|books|stripperwitch|midnight": "\"The books can stay where they are. For now. I don't fight other men's wars on a lie.\"",
        "custodian": "\"He told me a crate. A crate. Not the man who built this town.\""}})
    scene(ctx, dom.parent.id, "Dominico closes his hand slowly, the way a man puts away a knife. \"Tell Gog,\" he says, "
          "\"the midnight business is off.\"")
    brask = ctx.get(st.brask)
    if brask is not None and not brask.state.left_post and not brask.state.down and not ctx.embodied(brask):
        ctx.patch(brask, {"left_post": "called off"})
        scene(ctx, brask.parent.id, "A runner in Dominico's colours trots down the pier and says something in Brask's ear. "
              "Brask spits, shrugs, hangs the warehouse key on a nail by the door and leaves his post.")
        for it in brask.children():
            if it.name == "Warehouse key":
                ctx.move(it, brask.parent)
        walk(ctx, st.brask, st.ogre)

def klhyt_free(ctx, st, by):
    if st.klhyt_freed:
        return
    ctx.patch(story(ctx), {"klhyt_freed": True, "freed_by": by})
    klhyt = ctx.get(st.klhyt)
    ctx.patch(klhyt, {"dialog": {
        "custodian|dues|harbour": "\"Three seasons of harbour dues, skimmed before they reach the strongbox. He signs every tally. Tomorrow the whole town hears it.\"",
        "thanks|thank|grateful": "\"I came here with nothing but the salt in my beard. Ask me for something when this is done. I'll remember.\"",
        "gog|guild": "\"Gog runs the shadows and I let him, because he keeps them honest. Dominico runs the fist. The Custodian was meant to keep the books.\""}})
    scene(ctx, klhyt.parent.id, "Klhyt rubs his wrists and stands, unsteady, a big man gone thin. \"Four nights,\" he says. "
          "\"Four nights I've listened to the tide. Walk me to the square.\"")
    ctx.schedule(120, "klhyt_returns", target=ctx.root().id, payload={"by": by})

def klhyt_returns(ctx, st):
    klhyt = ctx.get(st.klhyt)
    if klhyt is None or klhyt.state.dead or st.custodian_exposed:
        return
    walk(ctx, st.klhyt, st.square)
    ctx.patch(story(ctx), {"custodian_exposed": True, "outcome": "Klhyt is home, and the Custodian's skimming is out in the square"})
    scene(ctx, st.square, "Klhyt climbs the Town Hall steps with the lamps behind him. People come out of all six taverns "
          "to see if it's really him. It is. He tells them where the harbour dues went, and whose name is on every tally.")
    cust = ctx.get(st.custodian)
    if cust is not None:
        ctx.patch(cust, {"disgraced": True,
                         "description": "The Custodian, in a good coat gone suddenly too warm, with nobody standing near him.",
                         "dialog": {"klhyt|mayor|dues|tally|harbour": "\"A misunderstanding. Accounts are complicated things. You wouldn't understand them.\""}})
    if not st.dominico_backed:
        dominico_backs_off(ctx, story(ctx).state, "his patron fell")
    ctx.patch(ctx.root(), {"story": "complete"})

def on(ctx, event):
    st = story(ctx).state
    k = event.kind
    p = event.payload or {}
    if k == "act":
        # someone who starts at the docks never walks in: their first deed there is their arrival
        who = ctx.get(event.actor) if event.actor else None
        if not st.seen_docks and who is not None and ctx.embodied(who) and who.parent is not None and who.parent.id == st.docks:
            ctx.patch(story(ctx), {"seen_docks": True})
            scene(ctx, st.docks, DOCKS_ARRIVAL)
        return
    if k == "arrived":
        place = p.get("place")
        who = ctx.get(p.get("who"))
        if who is None or not ctx.embodied(who):
            return
        if place == st.docks and not st.seen_docks:
            ctx.patch(story(ctx), {"seen_docks": True})
            scene(ctx, st.docks, DOCKS_ARRIVAL)
        elif place == st.warehouse and not st.klhyt_found and not st.shipped:
            ctx.patch(story(ctx), {"klhyt_found": True})
            scene(ctx, st.warehouse, "Between the bales and the stacked crates, in the one dry corner, a big grey-bearded man "
                  "sits tied to a chair beside an open crate with air holes drilled in the lid. He lifts his head. "
                  "\"Well,\" says Klhyt, founder of this town. \"You're not Dominico's.\"")
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
            scene(ctx, ctx.get(st.custodian).parent.id, "The Custodian reads it, folds it, and smiles with half his mouth. "
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
        scene(ctx, st.docks, "Brask hears it. He comes off the bollard with his cudgel already swinging. \"OI.\"")
    elif k == "klhyt_returns":
        klhyt_returns(ctx, st)
    elif k == "ultimatum":
        if st.dominico_backed or st.klhyt_freed:
            return
        ctx.patch(story(ctx), {"ultimatum_given": True})
        walk(ctx, st.dominico, st.stripperwitch)
        scene(ctx, st.stripperwitch, "The music falls off a note. Dominico has come in, alone, which is worse than with "
              "company. He stops at Fat Gog's table and doesn't sit. \"The books, Gog. Every ledger, every name, every cut. "
              "On my table at the Apothecary by midnight. After midnight I stop asking.\" He nods to River, and leaves.")
        ctx.schedule(300, "dominico_back", target=ctx.root().id)
    elif k == "dominico_back":
        walk(ctx, st.dominico, st.apothecary)
    elif k == "custodian_out":
        if st.custodian_exposed:
            return
        if walk(ctx, st.custodian, st.stripperwitch):
            scene(ctx, st.hall, "The Custodian locks his office door, checks it twice, pulls up his collar and goes out into the night.")
            scene(ctx, st.stripperwitch, "The Custodian comes in by the side door, the way a man does who is not here. "
                  "He takes the red booth. River brings him wine without being asked.")
    elif k == "midnight":
        ctx.patch(ctx.root(), {"ambient": {"time_of_day": "midnight", "light": "the taverns' lamps and not much else"}})
        if st.dominico_backed or st.klhyt_freed:
            scene(ctx, st.stripperwitch, "The midnight bell goes. Nobody comes for Fat Gog's books.")
            return
        if st.gog_knows:
            dominico_backs_off(ctx, st, "Gog was ready for him")
            scene(ctx, st.stripperwitch, "At the midnight bell four of Dominico's men come to the Stripperwitch's door, look at "
                  "who Gog has waiting inside, and find somewhere else to be.")
            return
        ctx.patch(story(ctx), {"guild_hit": True})
        ctx.patch(ctx.get(st.stripperwitch), {"description":
            "Red velvet, slashed. The mirror behind the bar is in pieces and the stage curtain is down. River is sweeping "
            "glass with her jaw set. Fat Gog sits where he always sits, bleeding into a napkin, saying nothing at all."})
        scene(ctx, st.stripperwitch, "The midnight bell, and then the door comes in. Dominico's men go through the "
              "Stripperwitch like weather: the mirror, the bottles, the curtain, two of Gog's people and one of Gog. "
              "Nobody kills anybody. That is the message.")
        gog = ctx.get(st.gog)
        if gog is not None:
            ctx.patch(gog, {"dialog": {"dominico|midnight|books|guild": "\"He wants a war. He doesn't know what a war is. Find me who's paying for his nerve.\""}})
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
            scene(ctx, st.stripperwitch, "The siren steps onto the little stage. The fiddler stops. River puts the glass down. "
                  "Then she sings, and for as long as it lasts nobody in the Stripperwitch remembers owing anybody anything.")
            for place in [st.square, st.market, st.omberhulk]:
                scene(ctx, place, "From the direction of the Stripperwitch comes a voice so beautiful that people stop in the "
                      "street with their mouths open. It is the siren. She only sings here once in a long while.")
    elif k == "siren_leaves":
        siren = ctx.get(st.siren)
        if siren is None or siren.state.dead or ctx.embodied(siren):
            return
        scene(ctx, siren.parent.id, "The siren gathers her coins in a sealskin purse, says she has an exam in a fortnight, and "
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
        klhyt = ctx.get(st.klhyt)
        if klhyt is not None and klhyt.parent.id == st.warehouse:
            ctx.move(klhyt, st.packet)
            ctx.patch(klhyt, {"post": st.packet})
            scene(ctx, st.warehouse, "Two of Dominico's men come in with a lantern, nail the lid down on the big crate and "
                  "carry it out between them. It is heavy. It knocks, once, from the inside.")
        ship = ctx.get(st.emerald) if st.emerald else None
        if ship is not None and ship.parent.id == st.docks:
            ctx.move(ship, st.packet)
        scene(ctx, st.docks, "On the one o'clock tide the Emerald Eye slips her lines and slides out past the Xoton trader, "
              "low in the water, a big crate lashed on her deck and her small captain counting gold at the rail. By morning "
              "she is a light on the horizon, and then not even that.")
        ctx.patch(ctx.root(), {"story": "lost"})
