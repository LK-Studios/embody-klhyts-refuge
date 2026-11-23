"""The healers (owner, 2026-11-23: "do we need a healer shop ? A doctor ? And a healer different shops different
vibes"). Doctor Prewitt mends you whole the moment you pay, dearly, and tells the Throne about a wanted patient; Grandmother
Ishkaa's long sleep is cheap and slow and heals only if you stay the hour, under a roof nobody is taken from; Sister
Agathe stitches you for a copper and prays over you for five silver; bitterleaf tea sobers."""

from pathlib import Path

from embody.cli import load_world
from embody.ops import AUTHOR, Engine

REPO = next(p for p in Path(__file__).resolve().parents if (p / "pyproject.toml").exists())
WORLD = Path(__file__).resolve().parents[1]


def town():
    eng = Engine(":memory:", workspace=REPO, record=False)
    gm = eng.session("gm", capabilities=[AUTHOR])
    load_world(gm, WORLD)
    gm.patch(gm.world.root_id, {"dnd5e": {"player_rolls": False}})
    g = gm.invite("player", entity="Newcomer", label="p")
    you = eng.session_for_token(g["token"])
    you.join()
    return eng, gm, you


def eid(gm, name):
    return next(e["id"] for e in gm.world.find(limit=None) if e["name"] == name)


def where(gm, name):
    return gm.world.get(gm.world.get(eid(gm, name))["parent_id"])["name"]


def put(gm, name, place, hold=False):
    gm.move(eid(gm, name), eid(gm, place))
    gm.patch(eid(gm, name), {"post": eid(gm, place), **({"routine_hold_until": 10 ** 9} if hold else {})})


def held(gm, who):
    return {c["name"] for c in gm.world.children(eid(gm, who))}


def hurt(gm, hp=2, mx=30):
    me = eid(gm, "Newcomer")
    gm.patch(me, {"hp": hp, "max_hp": mx})
    gm.spawn("thing", me, "Purse", state={"kind": "cp", "count": 2000, "portable": True, "bulk": 0})
    return me


def hp(gm):
    return gm.inspect("Newcomer")["state"]["hp"]


def run(gm, seconds):
    for _ in range(int(seconds // 60)):
        gm.clock(step=60)


def test_the_doctor_mends_you_whole_at_once_and_the_treatment_is_not_carried_off():
    eng, gm, you = town()
    hurt(gm)
    put(gm, "Doctor Amsel Prewitt", "Prewitt's Surgery", hold=True)
    put(gm, "Newcomer", "Prewitt's Surgery")
    you.act("buy", "Doctor Amsel Prewitt", {"item": "treatment"})
    assert hp(gm) == 30 and "Doctor's treatment" not in held(gm, "Newcomer")
    you.act("buy", "Doctor Amsel Prewitt", {"item": "dressing"})
    assert "Field dressing" in held(gm, "Newcomer")  # a medicine: carried, and used with tend


def test_the_doctor_writes_down_a_wanted_patient_and_the_throne_comes_to_his_door():
    eng, gm, you = town()
    me = hurt(gm, hp=200, mx=200)
    gm.act_as("The Custodian", "warrant", params={"who": "Newcomer"})
    put(gm, "Doctor Amsel Prewitt", "Prewitt's Surgery", hold=True)
    put(gm, "Newcomer", "Prewitt's Surgery")
    you.act("buy", "Doctor Amsel Prewitt", {"item": "tooth"})
    run(gm, 540)
    assert where(gm, "Lieutenant Voss") != "Prewitt's Surgery"
    run(gm, 120)
    assert where(gm, "Lieutenant Voss") == "Prewitt's Surgery"
    assert gm.inspect("Lieutenant Voss")["state"].get("fight")
    assert me in gm.inspect("Story")["state"]["wanted"]


def test_the_long_sleep_heals_only_if_you_stay_the_hour():
    eng, gm, you = town()
    hurt(gm)
    put(gm, "Grandmother Ishkaa", "The Reed House", hold=True)
    put(gm, "Newcomer", "The Reed House")
    you.act("buy", "Grandmother Ishkaa", {"item": "sleep"})
    run(gm, 1800)
    assert hp(gm) == 2  # not yet
    run(gm, 2100)
    assert hp(gm) == 30
    gm.patch(eid(gm, "Newcomer"), {"hp": 2})
    you.act("buy", "Grandmother Ishkaa", {"item": "sleep"})
    put(gm, "Newcomer", "The Verde")  # up before the hour: it was only mud
    run(gm, 3900)
    assert hp(gm) == 2 and not gm.inspect("Newcomer")["state"].get("mending")


def test_the_reed_house_is_a_sanctuary_and_its_wares_are_cheap():
    eng, gm, you = town()
    st = gm.inspect("Story")["state"]
    assert st["reedhouse"] == eid(gm, "The Reed House")
    hurt(gm)
    put(gm, "Grandmother Ishkaa", "The Reed House", hold=True)
    put(gm, "Newcomer", "The Reed House")
    you.act("buy", "Grandmother Ishkaa", {"item": "poultice"})
    you.act("tend", "Newcomer")
    assert hp(gm) > 2


def test_agathe_prays_over_you_and_bitterleaf_tea_sobers():
    eng, gm, you = town()
    me = hurt(gm)
    put(gm, "Sister Agathe", "The Omberhulk & Nun", hold=True)
    put(gm, "Newcomer", "The Omberhulk & Nun")
    you.act("buy", "Sister Agathe", {"item": "blessing"})
    assert 2 + 4 <= hp(gm) <= 2 + 11
    gm.patch(me, {"unsteady": True, "drinks": 3, "grants": [{"source": "drink", "bonus": -2, "skill": None,
                                                              "place": None, "until": 10 ** 9, "uses": None,
                                                              "condition": "unsteady with drink"}]})
    put(gm, "Grandmother Ishkaa", "The Reed House", hold=True)
    put(gm, "Newcomer", "The Reed House")
    you.act("buy", "Grandmother Ishkaa", {"item": "tea"})
    you.act("drink", "Bitterleaf tea")
    st = gm.inspect("Newcomer")["state"]
    assert not st.get("unsteady") and not [g for g in (st.get("grants") or []) if g.get("source") == "drink"]
