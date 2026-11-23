"""Micro quests played through the way a player and a narrator would, each to what the world records (owner's
playtest, 2026-11-22: walking Ithriel's household to the Moonmoth left them at the Unicorn and carried the player
aboard)."""

from pathlib import Path

import pytest

from embody.cli import load_world
from embody.ops import AUTHOR, Engine, Rejected

REPO = next(p for p in Path(__file__).resolve().parents if (p / "pyproject.toml").exists())
WORLD = Path(__file__).resolve().parents[1]
HOUSE = ["Ithriel", "Faelan", "Ysolde", "Corwen", "Miravel"]


def town():
    eng = Engine(":memory:", workspace=REPO, record=False)  # the test's author moves stay out of changes.jsonl
    gm = eng.session("gm", capabilities=[AUTHOR])
    load_world(gm, WORLD)
    you = eng.session("you")
    you.join("klhyts-refuge", "Newcomer")
    return eng, gm, you


def eid(gm, name):
    return next(e["id"] for e in gm.world.find(limit=None) if e["name"] == name)


def at(gm, name):
    p = gm.inspect(eid(gm, name))["parent"]
    return gm.inspect(p.get("id") if isinstance(p, dict) else p)["name"]


def scenes(r):
    return [e["payload"].get("text") or "" for e in r.get("events", []) if e["kind"] == "scene"]


def test_ithriel_and_her_household_walk_with_you_and_board_the_moonmoth():
    eng, gm, you = town()
    gm.move(eid(gm, "Newcomer"), eid(gm, "The Touchy Unicorn"))
    r = you.act("talk", "Ithriel", {"about": "passage on the Moonmoth"})
    assert any("fall in behind you" in t for t in scenes(r))
    assert all(gm.inspect(n)["state"]["follows"] == eid(gm, "Newcomer") for n in HOUSE)
    for step in ["The Treeline Road", "Market Square", "Harbour Street"]:
        you.act("go", step)
        assert {at(gm, n) for n in HOUSE} == {step}, step  # they keep up, step after step
    gm.clock(step=300)  # five quiet minutes on Harbour Street, and nobody drifts home
    assert {at(gm, n) for n in HOUSE} == {"Harbour Street"}
    r = you.act("go", "The Docks")
    assert {at(gm, n) for n in HOUSE} == {"The Moonmoth"} and at(gm, "Newcomer") == "The Docks"
    assert gm.inspect("Story")["state"]["elves_aboard"]
    assert any("is the last up the gangplank" in t for t in scenes(r))  # described, not named
    gm.clock(step=600)
    assert {at(gm, n) for n in HOUSE} == {"The Moonmoth"}  # aboard is their place now
    you.act("go", "The Moonmoth")  # the leaf she gave opens the ship to you
    assert at(gm, "Newcomer") == "The Moonmoth"


def test_following_never_carries_anyone_aboard():
    eng, gm, you = town()
    docks = eid(gm, "The Docks")
    for n in ("Ithriel", "Tully"):
        gm.move(eid(gm, n), docks)
        gm.patch(eid(gm, n), {"post": docks, "routine_hold_until": 10 ** 9})
    you.act("follow", "Ithriel")
    gm.act_as("Tully", "follow", "Ithriel")
    gm.act_as("Ithriel", "go", "The Moonmoth")
    assert at(gm, "Ithriel") == "The Moonmoth"
    assert at(gm, "Newcomer") == "The Docks" and not gm.inspect("Newcomer")["state"].get("follows")  # your own step
    assert at(gm, "Tully") == "The Docks"  # no elf, no leaf: the gangplank turns him back


def test_a_follower_keeps_up_and_goes_home_when_told_to_stay():
    eng, gm, you = town()
    unicorn = eid(gm, "The Touchy Unicorn")
    gm.move(eid(gm, "Newcomer"), unicorn)
    gm.act_as("Faelan", "follow", "Newcomer")
    you.act("go", "The Treeline Road")
    you.act("go", "Market Square")
    gm.clock(step=300)
    assert at(gm, "Faelan") == "Market Square"
    gm.act_as("Faelan", "stay")
    assert gm.inspect("Faelan")["state"]["post"] == unicorn  # his place, kept while he followed
    gm.clock(step=900)
    assert at(gm, "Faelan") in ("The Treeline Road", "The Touchy Unicorn")  # on his way, at the idle walk's pace
    gm.clock(step=1800)
    assert at(gm, "Faelan") == "The Touchy Unicorn"


def coin(gm, who="Newcomer"):
    return sum(c["state"].get("count", 1) for c in gm.world.children(eid(gm, who)) if c["name"] == "Coin")


def test_the_custodian_pays_once_for_your_silence():
    eng, gm, you = town()
    for p in ["Harbour Street", "The Turtle Dragon"]:
        you.act("go", p)
    you.act("take", "Passage book")
    for p in ["Harbour Street", "Market Square", "The Town Hall"]:
        you.act("go", p)
    before = coin(gm)
    r = you.act("show", "The Custodian", {"item": "Passage book"})
    assert coin(gm) == before + 500 and any("Five gold for your trouble" in t for t in scenes(r))
    you.act("show", "The Custodian", {"item": "Passage book"})
    assert coin(gm) == before + 500  # once: the second showing buys nothing


def test_a_lemon_bath_for_a_gold_piece():
    eng, gm, you = town()
    for p in ["Harbour Street", "The High Apothecary"]:
        you.act("go", p)
    gm.patch(next(c["id"] for c in gm.world.children(eid(gm, "Newcomer")) if c["name"] == "Coin"), {"count": 500})
    you.act("buy", "Master Quillon", {"item": "a lemon bath"})
    you.act("bathe", eid(gm, "Lemon bath"))
    grants = gm.inspect("Newcomer")["state"]["grants"]
    assert {g["skill"] for g in grants if g["source"] == "lemon bath"} == {"persuasion", "parley"}


def test_ithriels_leaf_opens_the_moonmoth_to_whoever_holds_it():
    eng, gm, you = town()
    bo = eng.session("bo")
    bo.join("klhyts-refuge", template="sellsword", name="Bo")
    gm.move(eid(gm, "Newcomer"), eid(gm, "The Touchy Unicorn"))
    you.act("talk", "Ithriel", {"about": "help"})
    for p in ["The Treeline Road", "Market Square", "Harbour Street", "The Docks"]:
        you.act("go", p)
    # by id: a short name like "Bo" is lost among the names that contain it (an engine bug in name lookup)
    you.act("give", eid(gm, "Bo"), {"item": "Silverleaf token"})
    bo.act("go", "The Moonmoth")
    assert at(gm, "Bo") == "The Moonmoth"
    with pytest.raises(Rejected) as e:  # given away, it opens nothing for you
        you.act("go", "The Moonmoth")
    assert "gangplank" in e.value.reason


# fixed in the engine on engine/playtest-fixes (2026-11-22); an engine from before that still adds raw wits and skills
OLD_PICK = "def hand(" not in (REPO / "packs" / "locks" / "scripts" / "locks_pick.py").read_text(encoding="utf-8")


@pytest.mark.xfail(OLD_PICK, strict=True, reason="this engine's pick roll reads raw `skills` and `wits`, so a sheet "
                   "character's lockpick rank never counts (fixed on engine/playtest-fixes)")
def test_a_rogue_picks_the_warehouse_lock_with_her_own_rank():
    eng, gm, you = town()
    gm.patch(eid(gm, "Newcomer"), {"sheet": {"skills": {"lockpick": 5}}})
    you.act("pick", "Warehouse lock")
    gm.clock(step=600)
    log = gm.history(limit=400, newest=True)
    rolls = [e for e in (log["events"] if isinstance(log, dict) else log) if e["kind"] in ("lock_picked", "pick_failed")]
    assert rolls and rolls[-1]["payload"]["mod"] >= 5
