# Hail someone out of a crowd: a passer-by is made from the crowd's mix of peoples when spoken to, and is real from
# then on (a body with a name, a trade, a few things to say). A crowd gives up only so many faces a night.

NAMES = {
    "human": ["Inés Calvo", "Tomas Brack", "Marguerite Lune", "Benedikt Sorle", "Rosa Medal", "Jem Harrow", "Aldo Ferro",
              "Yvette Marchal", "Corin Tate", "Lucia Varga", "Piet Ostrand", "Nell Coppard"],
    "xoton": ["Kofi Stormbringer", "Nia Tidesinger", "Obi Tidehunter", "Sade Wavewhisper", "Chike Driftwood", "Ayana Starfinder",
              "Juma Seastrider", "Mirembe Oceanseer", "Femi Stormwarden", "Zola Tideshaper", "Taye Deepwave", "Adia Moonrider"],
    "elf": ["Ilyrien", "Saelwyn", "Thandril", "Aelora", "Merethil", "Caerwyn", "Lirael", "Eldrin"],
    "jonulvicha": ["Hratka", "Borgu", "Krenna", "Galmuk", "Ushra", "Torgan", "Vekka", "Druum"],
    "lizardfolk": ["Hrass", "Tssiv", "Kssa", "Ssorrek", "Ixil"],
}
LOOKS = {
    "human": ["A sunburnt colonist in a sweat-dark shirt", "A Landfall woman with a basket on her hip", "A thin clerk with ink to the elbow",
              "A fisherman with a net over one shoulder", "A grandmother selling nothing in particular", "A young man in a borrowed coat"],
    # Xotons (owner, 2026-11-24): dark-skinned, nearly as wide as they are tall, each ship its own tribe; rarely a pirate
    "xoton": ["A barrel-chested Xoton deckhand, black skin shining with sweat, in a tarred sailcloth wrap and nothing else",
              "A Xoton woman nearly as wide as she is tall, deep brown and tattooed to the jaw, a coil of rope and a glow kelp lamp on her hip",
              "A Xoton boatman off the envoy's launch in a sea-green sash and gold earrings, bare-chested and very pleased with himself",
              "A grey-bearded Xoton, dark as tarred oak, chest-high and as wide as a door, with tattooed knuckles and a shark-tooth necklace",
              "A Xoton marine off the Navy frigate, oiled and bare-chested under a sharkskin harness, a fleet knot tattooed at each wrist",
              "A Xoton with no House mark and no fleet knot, gold in both ears and a cutlass worn too comfortably: a pirate, if anyone asked"],
    "elf": ["A hooded elf with a Landfall accent and careful eyes", "A tall elf in a fisherman's coat that doesn't fit him",
            "An elf woman with silver rings and no luggage", "A young elf who flinches at uniforms"],
    "jonulvicha": ["A big Jonulvicha stevedore, tusks capped in brass", "A Jonulvicha woman with a cleaver in her belt",
                   "A scarred Jonulvicha with a Vorkathian frontier tattoo", "A Jonulvicha porter with a crate on each shoulder"],
    "lizardfolk": ["A green Lizardfolk of the Meters with a string of fish", "A Lizardfolk boatman, salt on his scales"],
}
TRADES = {
    "human": [["a fisher", "\"Up before the sun, back after it. The fish don't care.\""],
              ["a clerk at the chandlers'", "\"I count rope. Someone has to.\""],
              ["a cook", "\"Fried fish, fried yams, fried anything. It's too hot to eat and everyone eats.\""],
              ["a runaway from Landfall", "\"I did something in Landfall. Here, nobody asks. That's all I'll say.\""]],
    "xoton": [["a deckhand", "\"Haul, splice, climb, drink. In that order, mostly.\""],
              ["a timber buyer", "\"Straight trunks, tall ones. The Crows Nest always needs more.\""],
              ["a ship's cook", "\"Kelp stew. You'd love it. Nobody loves it.\""],
              ["a sailmaker", "\"Every patch on every sail in this harbour, I can tell you which ship sewed it. And which ship stole it.\""]],
    "elf": [["an exile", "\"I was a scholar. Now I am an exile. The work is less rewarding.\""],
            ["a scribe for hire", "\"I write letters home for people who can't. I don't write any of my own.\""],
            ["a healer", "\"Herbs, needles, a steady hand. Vorkath's priests called it witchcraft. Here it's a living.\""]],
    "jonulvicha": [["a stevedore", "\"Crates off, crates on. Some of them are heavier than they should be.\""],
                   ["a butcher", "\"Goat, mostly. Sometimes something with more legs.\""],
                   ["a sellsword between jobs", "\"I came from the frontier camps. Same fighting, better weather.\""]],
    "lizardfolk": [["a fisher of the Meters", "\"We fish. They buy. Lately they look at us while they buy.\""]],
}
ON_KLHYT = {
    "human": ["\"The mayor? Upriver, they say. I never saw him go.\"", "\"Klhyt'd never leave in the middle of the dues. Never.\""],
    "xoton": ["\"Klhyt? Drank with our captain a month back. Good man. Haven't seen him since.\""],
    "elf": ["\"The mayor let us stay when nobody else would. If he is gone, we should be gone soon too.\""],
    "jonulvicha": ["\"Mayor's not been down the docks in days. He always comes down the docks.\""],
    "lizardfolk": ["\"The castaway is kind to the Meters. If he is gone, it is not kind news.\""],
}

def pick_people(ctx, mix):
    keys = sorted(mix.keys())
    total = 0
    for k in keys:
        total = total + int(mix[k])
    r = ctx.rand.randint(1, total)
    acc = 0
    for k in keys:
        acc = acc + int(mix[k])
        if r <= acc:
            return k
    return keys[0]

def free_name(ctx, kind):
    names = list(NAMES[kind])
    ctx.rand.shuffle(names)
    for n in names:
        taken = [e for e in ctx.find(name=n, limit=5) if e.name == n]
        if not taken:
            return n
    return None

def check(ctx):
    c = ctx.target
    if c.parent.id != ctx.actor.parent.id:
        return "you are not in that crowd"
    if int(c.state.faces or 0) >= int(c.state.max_faces or 6):
        return c.state.no_more or "nobody else in this crowd wants to stop for you tonight: talk to the ones you have met"
    return True

def apply(ctx):
    c = ctx.target
    me = ctx.actor
    kind = pick_people(ctx, c.state.mix or {"human": 1})
    name = free_name(ctx, kind)
    if name is None:
        ctx.log("nobody turns: try another crowd")
        return
    look = ctx.rand.choice(LOOKS[kind])
    trade = ctx.rand.choice(TRADES[kind])
    rumours = c.state.rumours or ["\"Nothing worth repeating.\""]
    state = {
        "people": kind, "passer_by": True, "crowd": c.id,
        "description": look + ", " + trade[0] + ".",
        "dialog": {
            "name|who|you": "\"" + name + ". " + trade[0][0].upper() + trade[0][1:] + ".\"",
            "work|trade|job|do": trade[1],
            "klhyt|mayor|founder": ctx.rand.choice(ON_KLHYT[kind]),
            "news|rumour|gossip|heard": ctx.rand.choice(rumours),
        },
        "default_line": "\"" + name + ". " + trade[0][0].upper() + trade[0][1:] + ". Ask me about my work, the mayor, or the news.\"",
    }
    p = ctx.spawn("person", c.parent, name=name, state=state)
    ctx.patch(c, {"faces": int(c.state.faces or 0) + 1})
    ctx.emit("scene", target=c.parent, reach=1, text=look + " turns out of the crowd at " + me.name + "'s call: " + name + ".")
    ctx.log(name + " steps out of the crowd: " + trade[0])
    return {"name": name, "id": p.id, "people": kind}
