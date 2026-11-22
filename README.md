# Shalamar: Klhyts Refuge

A custom game built on [embody](https://github.com/newsbubbles/embody), the open-source world engine by Nathaniel
Gibson (MIT). This repository is the world, not the engine: the places, people, rules and story of one evening in
Klhyts Refuge, which embody loads, runs and serves.

## What embody is, and what we build on it

embody keeps persistent, deterministic worlds that people and AI agents share. The engine holds the truth (entities,
actions, events, who perceives what, the clock) and has no LLM inside: every player, narrator and resident NPC brings
their own agent, which connects over MCP and plays a body in the world. See the engine's
[README](https://github.com/newsbubbles/embody#readme) and [DESIGN.md](https://github.com/newsbubbles/embody/blob/main/DESIGN.md).

The game here is everything on top of that:

- **The setting.** Shalamar, before the war, from the LoreKeeper campaign world "Shalamar Est: 1988": its canon is
  imported, and what the canon leaves open is filled in and marked as a host default.
- **The place.** Klhyts Refuge, the nicest town on the continent: six taverns, the inns, the docks and the ships in
  harbour, laid out as a map, with prices, rooms, baths and passage for sale.
- **The people.** Fat Gog's guild, under threat from Dominico; the Custodian, running the town while its founder Klhyt
  is missing; refugees from Landfall, Lizardfolk who are tolerated, elves in exile, Xoton sailors. Each has what they
  know, what they will say, and what they want.
- **The rules.** The world's own verbs (buy, drink, eat, bathe, throw, free, and mingle or hail in a crowd), guards who
  answer what they are given or shown when nobody plays them, an elf ship that takes only elves and those an elf
  vouches for, and finds that answer a good check, all on top of the engine's d20 rules pack. Fights run by D&D 5e
  (the dnd5e pack): initiative and turns, armour class, damage dice, death saves, conditions and spell slots.
- **The story.** One evening, from half past ten until a ship sails on the one o'clock tide. The clock is turn-based:
  each act moves the world 30 seconds, so the evening waits for its players.

## Playing

Everyone starts at the docks, just off a boat. Seats: the Newcomer, Deloris, Kael Ironjaw, or a new character from a
template: refugee, sellsword, lizardfolk, elf, Xoton sailor or Jonulvicha.

On the hosted server, the host sends you an invite link: give it to your agent and it joins as your character. There
is no public sign-up.

To run it yourself, put this repository in an embody checkout as `worlds/klhyts-refuge`:

    git clone https://github.com/newsbubbles/embody
    cd embody
    git clone https://github.com/LK-Studios/embody-klhyts-refuge worlds/klhyts-refuge
    uv run embody --as gm --author load klhyts-refuge
    uv run embody --as you join klhyts-refuge Newcomer
    uv run embody --as you perceive

## What is in here

- `build.py` builds the world: the canon, the taverns' prices, the places and map, the people, the things, the wiring.
- `scripts/` holds the world's own verbs and rules: `buy`, `drink`, `eat`, `bathe`, `throw`, `free`, the guard's
  `guard_on`, `bound_guard`, the `gangplank`, the crowd's `crowd_hail` and `crowd_mingle`, the `finds` that answer a
  passed check, and the `story`.
- `notes/bible.md` is the canon digest, the owner's words verbatim, and every host default that was invented.
  **It holds the story's secrets: players should not read it.** `notes/` also keeps the playtest notes and the text
  to carry back into LoreKeeper.
- `tests/` run with the engine's suite, from the engine's folder:
  `timeout 300 uv run pytest -q worlds/klhyts-refuge/tests`.

## Hosting

The live world runs on Railway in the engine's own container: one service, the database on a volume at `/data`,
`EMBODY_WORLD=klhyts-refuge`. From the engine's folder, `uv run python tools/stage_deploy.py --world klhyts-refuge`
stages the engine's HEAD with this repository's HEAD, and prints the `railway up` line that ships it. Only committed
work ships. The engine's [docs/HOSTING.md](https://github.com/newsbubbles/embody/blob/main/docs/HOSTING.md) has the
whole path: invites, seats, owner grants.
