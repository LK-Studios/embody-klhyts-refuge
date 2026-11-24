"""A second siren (owner, 2026-11-24: a shy, frightened siren in dark blue swirls, ashore to find weapons for her city
deep beneath the water, with pearls and raw gold): Pelagie stands in the town by her look, carries no coin, answers in
her own voice, pays a pearl for a weapon and raw gold for coral armour, and goes home under the harbour with three.
Ondrine, Brynja and Wendeline each point to her."""

from importlib import util
from pathlib import Path

from embody.cli import load_world
from embody.ops import AUTHOR, Engine

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


def held(gm, who):
    return {c["name"]: int(c["state"].get("count") or 1) for c in gm.world.children(eid(gm, who))}


def place(gm, name):
    return gm.world.get(gm.world.get(eid(gm, name))["parent_id"])["name"]


def words(r):
    return " ".join(str(e["payload"].get("text") or "") for e in r["events"] if e["kind"] in ("say", "gestured", "scene"))


def meet(gm, you):
    gm.move(eid(gm, "Pelagie"), eid(gm, "The Touchy Unicorn"))
    gm.patch(eid(gm, "Pelagie"), {"routine_hold_until": 10 ** 9})
    gm.move(eid(gm, "Newcomer"), eid(gm, "The Touchy Unicorn"))


def test_she_stands_in_town_by_her_look_with_pearls_and_gold_and_no_coin():
    eng, gm, you = town()
    st = gm.inspect("Pelagie")["state"]
    assert st["people"] == "siren" and st["seen_as"].startswith("the barefoot woman in the borrowed shawl")
    assert len(st["routine"]) == 5
    mine = held(gm, "Pelagie")
    assert mine["Pearls"] == 6 and mine["Raw gold"] == 3 and "Coin" not in mine
    meet(gm, you)
    looks = {p["name"]: p["looks"] for p in you.perceive()["people"]}
    assert looks["Pelagie"].startswith("the barefoot woman")


def test_she_answers_in_her_own_voice_and_others_point_to_her():
    eng, gm, you = town()
    meet(gm, you)
    assert "steel rots in the sea" in words(you.act("talk", "Pelagie", {"about": "what weapons do you need"}))
    assert "No ears" in words(you.act("talk", "Pelagie", {"about": "the brood in the trench"}))
    assert "Please don't bring him here" in words(you.act("talk", "Pelagie", {"about": "the officer in blue"}))
    assert "washbasin" in words(you.act("talk", "Wendeline Moss", {"about": "your barefoot lodger"}))
    gm.move(eid(gm, "Newcomer"), eid(gm, "Coral and Chain"))
    assert "door doesn't bite" in words(you.act("talk", "Brynja Coralhand", {"about": "the girl at your window"}))


def test_a_pearl_for_a_weapon_gold_for_coral_and_home_with_three():
    eng, gm, you = town()
    meet(gm, you)
    me = eid(gm, "Newcomer")
    gm.spawn("thing", me, "Old boot", state={"portable": True, "description": "A boot."})
    r = you.act("give", "Pelagie", {"item": "Old boot"})
    assert "do not know what it is for" in words(r) and "Pearls" not in held(gm, "Newcomer")
    r = you.act("give", "Pelagie", {"item": "Knife"})
    assert held(gm, "Newcomer").get("Pearls") == 1 and "That is 1" in words(r)
    gm.spawn("thing", me, "Coral armour", state={"portable": True, "kind": "coral armor", "armor": {"ac": 11},
                                                 "description": "Coral on sharkskin."})
    r = you.act("give", "Pelagie", {"item": "Coral armour"})
    assert held(gm, "Newcomer").get("Raw gold") == 1 and "It will not rot" in words(r)
    assert place(gm, "Pelagie") == "The Touchy Unicorn"
    gm.spawn("thing", me, "Hooked knife", state={"portable": True, "weapon": True, "dice": "1d4", "dtype": "slashing"})
    r = you.act("give", "Pelagie", {"item": "Hooked knife"})
    st = gm.inspect("Pelagie")["state"]
    assert st["gone_home"] and st["armed"] == 3 and st["routine_off"]
    assert place(gm, "Pelagie") == "Under the Harbour"
    assert "go home now" in words(r) and held(gm, "Newcomer").get("Pearls") == 2
    assert held(gm, "Pelagie")["Pearls"] == 4 and held(gm, "Pelagie")["Raw gold"] == 2


def test_the_stage_runs_again_without_change():
    eng, gm, you = town()
    spec = util.spec_from_file_location("refuge_build", WORLD / "build.py")
    b = util.module_from_spec(spec)
    spec.loader.exec_module(b)
    seq = gm.world.store.next_seq(gm.world.id)
    b.build_siren(gm)
    assert gm.world.store.next_seq(gm.world.id) == seq
    b.spawn_new(gm)  # the people new to the town are made once ever
    assert len([e for e in gm.world.find(limit=None) if e["name"] == "Pelagie"]) == 1
