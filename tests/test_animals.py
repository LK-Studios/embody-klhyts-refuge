"""The town's animals (owner, 2026-11-24: "Do we put in some animals ? Do we need some horses? a few cats? And some
livestock? Maybe a dog or 4"): twenty of them where the town keeps them, seen at a glance; a stray won over with food
and patience follows you home; the Fist's mastiff growls at a stranger in the warehouse; a day feeds them all and the
hens lay; a dog in a 5e fight bites back; and the stage runs again without making anything twice."""

import json
from importlib import util
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


def where(gm, name):
    return gm.world.get(gm.world.get(eid(gm, name))["parent_id"])["name"]


def day(gm):
    gm.schedule(0, "beast_day", entity=gm.world.root_id)
    gm.clock(step=1)


def build_module():
    spec = util.spec_from_file_location("refuge_build", WORLD / "build.py")
    b = util.module_from_spec(spec)
    spec.loader.exec_module(b)
    return b


def test_twenty_animals_where_the_town_keeps_them_and_seen_at_a_glance():
    eng, gm, you = town()
    beasts = gm.world.find(type="beast", limit=None)
    kinds = {}
    for e in beasts:
        kinds[e["state"]["species"]] = kinds.get(e["state"]["species"], 0) + 1
    assert kinds == {"dog": 4, "cat": 3, "horse": 3, "mule": 1, "goat": 3, "chicken": 5, "cricket": 1}
    assert where(gm, "Old ship's dog") == "The Turtle Dragon" and where(gm, "Grey mare") == "The Town Gate"
    assert where(gm, "Fist's mastiff") == "The Bonded Warehouse" and where(gm, "Nanny goat") == "The Back Lanes"
    b = you.perceive()
    looks = {p["name"]: p["looks"] for p in b["people"]}
    assert looks["Yellow dog"].startswith("a skinny yellow dog") and "Giant riding cricket" in looks
    assert not any("Teeth" in (p.get("bears") or []) for p in b["people"])  # a bite is not something a dog carries
    assert any(v.startswith("pet: ") and "Yellow dog" in v for v in b["verbs"])
    assert len(json.dumps(b)) < 4000  # still short enough to say aloud
    full = json.dumps(you.inspect("Yellow dog"))
    assert '"scores"' not in full and '"trust"' not in full  # the numbers and who it trusts are the world's


def test_a_stray_won_over_with_food_and_patience_follows_you():
    eng, gm, you = town()
    me = eid(gm, "Newcomer")
    r = you.act("pet", "Yellow dog")
    assert r["result"]["wary"] and "Food first" in r["result"]["line"]
    with pytest.raises(Rejected) as why:
        you.act("feed", "Yellow dog", {"item": "Knife"})
    assert "turns away" in why.value.reason or "feed it what" in why.value.reason
    gm.world.patch(me, {"skill_prof": {"animal handling": 2, "animals": 2}})
    for _ in range(12):
        if gm.inspect("Yellow dog")["state"].get("owner") == me:
            break
        gm.spawn("food", me, "Scraps", state={"food": "scraps", "feeds": 1, "description": "Yesterday's bread."})
        you.act("feed", "Yellow dog", {"item": "Scraps"})
        try:
            you.act("gentle", "Yellow dog")
        except Rejected:
            pass
        day(gm)
    st = gm.inspect("Yellow dog")["state"]
    assert st["owner"] == me and st["follows"] == me
    assert not you.act("pet", "Yellow dog")["result"]["wary"]
    you.act("go", "Harbour Street")
    assert where(gm, "Yellow dog") == "Harbour Street"


def test_the_fist_mastiff_growls_at_a_stranger_in_the_warehouse():
    eng, gm, you = town()
    me = eid(gm, "Newcomer")
    gm.move(eid(gm, "Warehouse key"), me)
    you.act("unlock", "Warehouse lock")
    you.act("go", "The Bonded Warehouse")
    seen = you.perceive(brief=False, cursor=0, events=300)["events"]
    assert any(e["kind"] == "growled" and e["payload"].get("at") == me for e in seen)
    r = you.act("pet", "Fist's mastiff")
    assert r["result"]["wary"] and "snaps" in r["result"]["line"]


def test_a_day_feeds_them_all_and_the_hens_lay():
    eng, gm, you = town()
    for _ in range(3):
        day(gm)
    for e in gm.world.find(type="beast", limit=None):
        st = e["state"]
        assert not st.get("hungry") and not st.get("dead"), e["name"]
        assert e["parent_id"] == st["home"], e["name"]  # nothing wandered off hungry
    eggs = [e for e in gm.world.find(limit=None) if e["name"] == "Egg"]
    assert 1 <= len(eggs) <= 4  # one at most by each hen, however many days


def test_talk_and_pet_get_an_answer_in_kind():
    eng, gm, you = town()
    gm.move(eid(gm, "Newcomer"), eid(gm, "The Turtle Dragon"))
    r = you.act("talk", "Old ship's dog", {"about": "who's a good boy"})
    said = [e["payload"].get("text") for e in r["events"] if e["kind"] == "gestured"]
    assert said and said[0].startswith("The old dog")
    r = you.act("pet", "Old ship's dog")
    assert not r["result"]["wary"] and any(e["kind"] == "scene" and "old dog" in e["payload"]["text"] for e in r["events"])


def test_a_dog_in_a_fight_bites_back_or_breaks_off():
    eng, gm, you = town()
    gm.patch(gm.world.root_id, {"dnd5e": {"player_rolls": False}})  # the world rolls initiative
    dog = eid(gm, "Yellow dog")
    for _ in range(6):
        st = gm.inspect("Yellow dog")["state"]
        if st.get("dead") or gm.world.get(dog)["parent_id"] != eid(gm, "The Docks"):
            break
        try:
            you.act("attack", "Yellow dog")
        except Rejected:
            gm.clock(step=6)
    w = gm.world
    kinds = {e["kind"] for e in w.events(since=0, limit=5000) if e["actor_id"] == dog or e["target_id"] == dog}
    assert kinds & {"hit", "missed"}  # the fight ran on the 5e rules, with no error
    st = gm.inspect("Yellow dog")["state"]
    assert st.get("dead") or st["hp"] < 5 or "missed" in kinds


def test_the_stage_runs_again_without_making_anything_twice():
    eng, gm, you = town()
    b = build_module()
    root = gm.world.root_id
    gm.world.destroy(eid(gm, "Brown kid"))  # gone in play: not made again
    seq = gm.world.store.next_seq(gm.world.id)
    b.build_animals(gm, root)
    assert gm.world.store.next_seq(gm.world.id) == seq
    assert not [e for e in gm.world.find(limit=None) if e["name"] == "Brown kid"]
    assert sum(1 for t in gm.timers() if t["kind"] == "beast_day") == 1
