"""The town's people: crowds that talk and give up faces, the Moonmoth's gangplank, the siren's night, the Emerald Eye."""

from pathlib import Path

import pytest

from embody.cli import load_world
from embody.ops import AUTHOR, Engine, Rejected

REPO = next(p for p in Path(__file__).resolve().parents if (p / "pyproject.toml").exists())
WORLD = Path(__file__).resolve().parents[1]


def town():
    eng = Engine(":memory:", workspace=REPO)
    gm = eng.session("gm", capabilities=[AUTHOR])
    load_world(gm, WORLD)
    you = eng.session("you")
    you.join("klhyts-refuge", "Newcomer")
    return eng, gm, you


def eid(gm, name):
    return next(e["id"] for e in gm.world.find(limit=None) if e["name"] == name)


def where(gm, name):
    return gm.world.get(eid(gm, name))["parent_id"]


def scenes(r):
    return [e["payload"].get("text") or "" for e in r.get("events", []) if e["kind"] == "scene"]


def test_the_night_market_crowd_talks_and_gives_up_faces():
    eng, gm, you = town()
    for p in ["Harbour Street", "The Night Market"]:
        you.act("go", p)
    r = you.act("mingle", "Market crowd")
    assert any(t.startswith("\"") for t in scenes(r)), "mingling overhears a rumour"
    made = []
    for _ in range(8):
        r = you.act("hail", "Market crowd")
        made.append(r["result"]["name"])
    assert len(set(made)) == 8
    peoples = {gm.inspect(n)["state"]["people"] for n in made}
    assert peoples <= {"human", "xoton", "elf", "jonulvicha", "lizardfolk"}
    with pytest.raises(Rejected):
        you.act("hail", "Market crowd")  # a crowd gives up only so many faces a night
    r = you.act("talk", made[0], {"about": "what do you do for work?"})
    assert [e for e in r["events"] if e["kind"] in ("say", "gestured")]


def test_vendors_sell_at_the_night_market():
    eng, gm, you = town()
    for p in ["Harbour Street", "The Night Market"]:
        you.act("go", p)
    you.act("buy", "Grusha", {"item": "goat skewer"})
    you.act("buy", "Saelwyn", {"item": "a map of the coast"})
    held = {c["name"] for c in you.perceive(brief=False)["holding"]}
    assert {"Goat skewer", "Map of the southern coast"} <= held


def test_the_moonmoth_takes_elves_and_those_an_elf_vouches_for():
    eng, gm, you = town()
    with pytest.raises(Rejected):
        you.act("go", "The Moonmoth")
    for p in ["Harbour Street", "Market Square", "The Treeline Road", "The Touchy Unicorn"]:
        you.act("go", p)
    you.act("talk", "Ithriel", {"about": "passage on the moonmoth"})
    assert "Silverleaf token" in {c["name"] for c in you.perceive(brief=False)["holding"]}
    for p in ["The Treeline Road", "Market Square", "Harbour Street", "The Docks", "The Moonmoth"]:
        you.act("go", p)
    assert where(gm, "Newcomer") == eid(gm, "The Moonmoth")


def test_the_siren_rises_sings_and_goes_back_to_the_sea():
    eng, gm, you = town()
    assert where(gm, "Ondrine") == eid(gm, "Under the Harbour")
    gm.clock(step=3650)
    assert where(gm, "Ondrine") == eid(gm, "The Docks")
    gm.clock(step=300)
    assert where(gm, "Ondrine") == eid(gm, "The Stripperwitch")
    gm.clock(step=4000)
    assert where(gm, "Ondrine") == eid(gm, "Under the Harbour")


def test_the_emerald_eye_sails_on_the_tide():
    eng, gm, you = town()
    assert where(gm, "The Emerald Eye") == eid(gm, "The Docks")
    gm.clock(step=9100)
    assert where(gm, "The Emerald Eye") == eid(gm, "The Emerald Eye, outward bound")
    assert where(gm, "Klhyt") == eid(gm, "The Emerald Eye, outward bound")
