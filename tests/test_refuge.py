"""Shalamar - Klhyts Refuge: the town builds, the taverns sell, the clues answer, and every road to the end works."""

from pathlib import Path

import pytest

from embody.cli import load_world
from embody.ops import AUTHOR, Engine

REPO = next(p for p in Path(__file__).resolve().parents if (p / "pyproject.toml").exists())
WORLD = Path(__file__).resolve().parents[1]


def town(tmp_path):
    eng = Engine(":memory:", workspace=REPO)
    gm = eng.session("gm", capabilities=[AUTHOR])
    load_world(gm, WORLD)
    you = eng.session("you")
    you.join("klhyts-refuge", "Newcomer")
    return eng, gm, you


def scenes(r):
    return [e["payload"].get("text") or "" for e in r.get("events", []) if e["kind"] == "scene"]


def eid(gm, name):
    return next(e["id"] for e in gm.world.find(limit=None) if e["name"] == name)


def story(gm):
    return gm.inspect("Story")["state"]


def holding(you):
    return {c["name"]: c for c in you.perceive()["holding"]}


def coin(you):
    h = holding(you)
    return h["Coin"].get("count", 1) if "Coin" in h else 0


def test_the_town_stands_and_the_newcomer_lands_at_the_docks(tmp_path):
    eng, gm, you = town(tmp_path)
    p = you.perceive()
    assert p["here"]["name"] == "The Docks"
    here = {e["name"] for e in p["present"]}
    assert {"Brask", "Harbourmaster Teague", "Klhyt's signet ring"} <= here
    # the card offers no nonsense: nobody is offered a drink of their own coin
    assert not any(a["verb"] == "drink" and a.get("target_name") == "Coin" for a in p["affordances"])
    r = you.act("talk", "Harbourmaster Teague", {"about": "hello"})
    assert any("Fat Gog" in str(e["payload"]) for e in r["events"] if e["kind"] in ("say", "gestured"))
    assert story(gm)["seen_docks"] is True  # the first deed at the docks is the arrival


def test_buying_and_drinking_at_the_turtle_dragon(tmp_path):
    eng, gm, you = town(tmp_path)
    you.act("go", "Harbour Street")
    you.act("go", "The Turtle Dragon")
    before = coin(you)
    r = you.act("buy", "Bosun Maggs")  # asked bare: the menu, nothing changes hands
    assert "Massive beer" not in holding(you) and coin(you) == before
    you.act("buy", "Bosun Maggs", {"item": "a beer"})
    assert "Massive beer" in holding(you) and coin(you) == before - 1
    beer = holding(you)["Massive beer"]["id"]
    you.act("drink", beer)  # full of water, and it still goes down: ale is for the taste
    for _ in range(2):
        you.act("buy", "Bosun Maggs", {"item": "mead"})
        you.act("drink", holding(you)["Cup of mead"]["id"])
    me = gm.inspect("Newcomer")["state"]
    assert me["drinks"] == 3 and me["unsteady"] is True
    assert any(g["source"] == "drink" and g["bonus"] == -2 for g in me["grants"])
    with pytest.raises(Exception):
        you.act("buy", "Bosun Maggs", {"item": "a bottle of the vintage"})


def test_river_tells_what_she_saw_and_a_passed_check_always_answers(tmp_path):
    eng, gm, you = town(tmp_path)
    for p in ["Harbour Street", "Market Square", "The Stripperwitch"]:
        you.act("go", p)
    r = you.act("talk", "River", {"about": "where is Klhyt, the mayor?"})
    assert any("red booth" in str(e["payload"]) or "booth" in str(e["payload"]) for e in r["events"])
    assert "river" in story(gm)["clues"]
    r = you.act("check", "Newcomer", {"skill": "insight"})
    assert scenes(r), "a check in a place with finds always answers"
    r = you.act("check", "Newcomer", {"skill": "basket weaving"})
    assert any("Nothing here answers" in t or "nothing" in t.lower() for t in scenes(r))


def test_the_bribe_road_brask_goes_drinking_and_klhyt_comes_home(tmp_path):
    eng, gm, you = town(tmp_path)
    you.act("take", "Klhyt's signet ring")
    assert "ring" in story(gm)["clues"]
    r = you.act("give", "Brask", {"item": "Coin", "count": 200})
    assert gm.inspect("Brask")["state"]["left_post"] == "bribed"
    assert gm.world.get(eid(gm, "Brask"))["parent_id"] == eid(gm, "Rampant Ogre & Curved Cleaver")
    you.act("take", "Warehouse key")
    you.act("unlock", "Warehouse lock")
    r = you.act("go", "The Bonded Warehouse")
    assert story(gm)["klhyt_found"] is True
    r = you.act("free", "Klhyt")
    assert story(gm)["klhyt_freed"] is True
    gm.clock(step=300)
    st = story(gm)
    assert st["custodian_exposed"] is True
    assert gm.inspect(gm.summary()["root"])["state"]["story"] == "complete"
    assert gm.world.get(eid(gm, "Klhyt"))["parent_id"] == eid(gm, "Market Square")


def test_the_proof_road_the_passage_book_turns_dominico(tmp_path):
    eng, gm, you = town(tmp_path)
    for p in ["Harbour Street", "The Turtle Dragon"]:
        you.act("go", p)
    you.act("take", "Passage book")
    you.act("read", "Passage book")
    assert "passage" in story(gm)["clues"]
    for p in ["Harbour Street", "The High Apothecary"]:
        you.act("go", p)
    you.act("show", "Dominico", {"item": "Passage book"})
    st = story(gm)
    assert st["dominico_backed"] is True
    assert gm.inspect("Brask")["state"]["left_post"] == "called off"
    docks = eid(gm, "The Docks")
    assert any(c["name"] == "Warehouse key" for c in gm.inspect(docks)["contents"])


def test_the_gog_road_his_marker_moves_the_guard(tmp_path):
    eng, gm, you = town(tmp_path)
    you.act("take", "Klhyt's signet ring")
    for p in ["Harbour Street", "Market Square", "The Stripperwitch"]:
        you.act("go", p)
    you.act("show", "Fat Gog", {"item": "Klhyt's signet ring"})
    assert story(gm)["gog_knows"] is True
    assert "Fat Gog's marker" in holding(you)
    for p in ["Market Square", "Harbour Street", "The Docks"]:
        you.act("go", p)
    you.act("show", "Brask", {"item": "Fat Gog's marker"})
    assert gm.inspect("Brask")["state"]["left_post"] == "marker"


def test_the_clock_ultimatum_midnight_and_the_tide(tmp_path):
    eng, gm, you = town(tmp_path)
    gm.clock(step=620)
    assert story(gm)["ultimatum_given"] is True
    assert gm.world.get(eid(gm, "Dominico"))["parent_id"] == eid(gm, "The Stripperwitch")
    gm.clock(step=400)
    assert gm.world.get(eid(gm, "Dominico"))["parent_id"] == eid(gm, "The High Apothecary")
    gm.clock(step=600)
    assert gm.world.get(eid(gm, "The Custodian"))["parent_id"] == eid(gm, "The Stripperwitch")
    gm.clock(step=4000)
    assert story(gm)["guild_hit"] is True
    gm.clock(step=3700)
    st = story(gm)
    assert st["shipped"] is True
    assert gm.world.get(eid(gm, "Klhyt"))["parent_id"] == eid(gm, "The Emerald Eye, outward bound")
    assert gm.inspect(gm.summary()["root"])["state"]["story"] == "lost"


def test_a_day_with_nobody_playing_kills_nobody(tmp_path):
    eng, gm, you = town(tmp_path)
    you.leave()
    for _ in range(24):
        gm.clock(step=3600)
    people = [e for e in gm.world.find(limit=None) if e["type"] in ("person", "fighter", "guard")]
    assert people
    assert not [p["name"] for p in people if p["state"].get("dead") or p["state"].get("down")]
