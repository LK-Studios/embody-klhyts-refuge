# Shalamar - Klhyts Refuge

A world for embody, imported from the LoreKeeper world "Shalamar Est: 1988". Shalamar before the war: Klhyts Refuge,
the nicest town on the continent, with its six taverns and its docks. Fat Gog's guild is under threat from Dominico,
the founder Klhyt is missing, and the Custodian runs the town in his absence.

    uv run embody --as gm --author load klhyts-refuge
    uv run embody --as you join klhyts-refuge Newcomer
    uv run embody --as you perceive

- `build.py` builds it: the canon, the taverns' prices, the places and map, the people, the things, and the wiring.
- `scripts/` holds the world's own verbs and rules: `buy`, `drink`, `eat`, `bathe`, `throw`, `free`, the guard's
  `guard_on`, the `finds` that answer a passed check, `bound_guard`, and the `story`.
- `notes/bible.md` is the canon digest, the owner's words verbatim, and every host default that was invented.
- `tests/` run with the engine's suite: `timeout 300 uv run pytest -q worlds/klhyts-refuge/tests`.

Seats: Newcomer (at the docks), Deloris (the Touchy Unicorn), Kael Ironjaw (the Rampant Ogre), or a new character
from a template: refugee, sellsword, lizardfolk, elf (`seats()` lists them).
