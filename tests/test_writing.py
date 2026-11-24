"""Writing on things (owner, 2026-11-23: "A few time we encounter paper or books and no ability to write on things",
then "Chalkboards etc messages, scratching into wood"): the passage book takes a name, Hob Merrow sells paper and a
blank book, a note passes hand to hand, the square's notice board takes a line where a price board takes none, the
harbour slate keeps its own chalk and wipes clean, and the Ogre's bar top takes a knife."""

from pathlib import Path

import pytest

from embody.cli import load_world
from embody.ops import AUTHOR, Engine, Rejected

REPO = next(p for p in Path(__file__).resolve().parents if (p / "pyproject.toml").exists())
WORLD = Path(__file__).resolve().parents[1]


def town():
    eng = Engine(":memory:", workspace=REPO, record=False)
    gm = eng.session("gm", capabilities=[AUTHOR])
    load_world(gm, WORLD)
    g = gm.invite("player", entity="Newcomer", label="p")
    you = eng.session_for_token(g["token"])
    you.join()
    return eng, gm, you


def eid(gm, name):
    return next(e["id"] for e in gm.world.find(limit=None) if e["name"] == name)


def put(gm, name, place):
    gm.move(eid(gm, name), eid(gm, place))
    gm.patch(eid(gm, name), {"post": eid(gm, place), "routine_hold_until": 10 ** 9})


def test_the_passage_book_takes_a_name_and_keeps_what_it_said():
    eng, gm, you = town()
    put(gm, "Newcomer", "The Turtle Dragon")
    before = gm.inspect("Passage book")["state"]["text"]
    you.act("write", "Passage book", {"text": "Mira Tallow, one berth for Catan."})
    after = gm.inspect("Passage book")["state"]
    assert after["text"] == before + "\nMira Tallow, one berth for Catan."
    assert after["clue"] == "passage" and after["hands"][-1]["by"] == eid(gm, "Newcomer")


def test_hob_sells_paper_and_a_note_passes_hand_to_hand():
    eng, gm, you = town()
    gm.spawn("thing", eid(gm, "Newcomer"), "Purse", state={"kind": "cp", "count": 3000, "portable": True, "bulk": 0})
    put(gm, "Newcomer", "Merrow's Chandlery")
    you.act("buy", "Hob Merrow", {"item": "paper"})
    you.act("buy", "Hob Merrow", {"item": "blank book"})
    held = {c["name"]: c for c in gm.world.children(eid(gm, "Newcomer"))}
    assert held["Sheet of paper"]["state"]["writable"] and held["Blank book"]["state"]["room"] == 6000
    you.act("write", "Sheet of paper", {"text": "The crate on the pier breathes. Tell Gog."})
    you.act("give", "Hob Merrow", {"item": "Sheet of paper"})
    note = next(c for c in gm.world.children(eid(gm, "Hob Merrow")) if c["name"] == "Sheet of paper")
    assert note["state"]["text"] == "The crate on the pier breathes. Tell Gog." and note["state"]["penned"]
    said = you.act("talk", "Hob Merrow", {"about": "do you sell paper?"})
    assert any("two silver the sheet" in str(e["payload"]) for e in said["events"])


def test_the_notice_board_takes_a_line_and_a_price_board_does_not():
    eng, gm, you = town()
    put(gm, "Newcomer", "Market Square")
    you.act("write", "Notice board", {"text": "WANTED: news of the Mayor. Ask at the Turtle."})
    assert gm.inspect("Notice board")["state"]["text"].endswith("WANTED: news of the Mayor. Ask at the Turtle.")
    put(gm, "Newcomer", "The Turtle Dragon")
    board = next(e["id"] for e in gm.world.children(eid(gm, "The Turtle Dragon")) if e["name"] == "Price board")
    with pytest.raises(Rejected) as r:
        you.act("write", board, {"text": "Ale free tonight."})
    assert "nowhere on that to write" in r.value.reason
    offered = {a["target_name"] for a in gm.world.affordances(eid(gm, "Newcomer")) if a["verb"] == "write"}
    assert "Passage book" in offered and "Price board" not in offered


def test_the_stage_makes_old_paper_writable_and_runs_again_without_change():
    eng, gm, you = town()
    book = eid(gm, "Passage book")
    assert gm.world.get(book)["state"]["room"] == 4000  # a book holds more than a sheet
    gm.world.patch(book, {"writable": None, "room": None})
    gm.world.patch(eid(gm, "Notice board"), {"writable": None, "room": None})
    gm.world.patch(eid(gm, "Big crate"), {"writable": None})
    gm.world.patch(eid(gm, "Honeymoon Suite"), {"writable": None})
    assert "writable" not in gm.world.get(book)["state"]
    from importlib import util
    spec = util.spec_from_file_location("refuge_build", WORLD / "build.py")
    b = util.module_from_spec(spec)
    spec.loader.exec_module(b)
    b.build_writing(gm)
    assert gm.world.get(book)["state"]["writable"] is True and gm.world.get(book)["state"]["room"] == 4000
    assert gm.world.get(eid(gm, "Notice board"))["state"]["room"] == 2400
    assert gm.world.get(eid(gm, "Big crate"))["state"]["writable"] == "blade"
    assert gm.world.get(eid(gm, "Honeymoon Suite"))["state"]["writable"] == "chalk"
    seq = gm.world.store.next_seq(gm.world.id)
    b.build_writing(gm)
    assert gm.world.store.next_seq(gm.world.id) == seq  # nothing left to do: no patch, no event


def test_the_harbour_slate_keeps_its_own_chalk_and_wipes_clean():
    eng, gm, you = town()
    put(gm, "Newcomer", "The Docks")
    you.act("write", "Harbour slate", {"text": "CREW WANTED FOR THE MOONMOTH. ASK FOR NOBODY."})
    st = gm.inspect("Harbour slate")["state"]
    assert st["text"].endswith("ASK FOR NOBODY.") and st["writable"] == "chalk"
    you.act("wipe", "Harbour slate")
    assert gm.inspect("Harbour slate")["state"]["text"] == ""
    with pytest.raises(Rejected) as r:
        you.act("wipe", "Harbour slate")
    assert "nothing on it to wipe" in r.value.reason


def test_the_suite_door_takes_chalk_in_hand_and_the_ogre_bar_takes_a_knife():
    eng, gm, you = town()
    me = eid(gm, "Newcomer")
    for c in gm.world.children(me):  # whatever kit the newcomer lands with, nothing to write with
        if c["state"].get("weapon") or "chalk" in c["name"].lower():
            gm.world.destroy(c["id"])
    put(gm, "Newcomer", "Rampant Ogre & Curved Cleaver")
    with pytest.raises(Rejected) as r:
        you.act("write", "Honeymoon Suite", {"text": "OCCUPIED"})
    assert "chalk in your hand" in r.value.reason
    with pytest.raises(Rejected) as r:
        you.act("carve", "Bar top", {"text": "M + T"})
    assert "a blade in your hand" in r.value.reason
    gm.spawn("thing", me, "Chalk", state={"portable": True, "bulk": 0, "description": "A stick of white chalk."})
    gm.spawn("thing", me, "Dagger", state={"portable": True, "weapon": True, "dtype": "piercing", "kind": "dagger"})
    you.act("write", "Honeymoon Suite", {"text": "OCCUPIED"})
    assert gm.inspect("Honeymoon Suite")["state"]["text"].endswith("\nOCCUPIED")
    r = you.act("carve", "Bar top", {"text": "M + T"})
    assert r["result"]["how"] == "blade" and gm.inspect("Bar top")["state"]["text"] == "M + T"
    assert "M + T" in you.act("read", "Bar top")["result"]
    offered = {(a["verb"], a["target_name"]) for a in gm.world.affordances(me) if a["ok"]}
    assert ("carve", "Bar top") in offered and ("wipe", "Honeymoon Suite") in offered
    assert ("carve", "Honeymoon Suite") not in offered and ("wipe", "Bar top") not in offered
    you.act("wipe", "Honeymoon Suite")  # the chalk goes; what the door says of the room stays
    st = gm.inspect("Honeymoon Suite")["state"]
    assert st["text"] == st["keeps"] and "OCCUPIED" not in st["text"] and "dog pelts" in st["text"]
