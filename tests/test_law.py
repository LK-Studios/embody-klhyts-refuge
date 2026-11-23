"""Surrender and the dead (owner, 2026-11-23: "Surrender should mean surrender. And you are taken to prison."; "we will
need an undertaker to go and sort out bodies etc."). A player who yields to the Fist, the Throne's people or the
watch while they press them goes to the cells under the Town Hall, weapons and papers in the evidence chest, and
comes out after six world hours or on five gold bail; or is broken out (the key bribed off Rosa, the bar picked or
broken), wanted for it, and whoever is seen at the door is wanted too; the undertaker brings the dead to the Quiet
Ground and buries them there."""

from pathlib import Path

from embody.cli import load_world
from embody.ops import AUTHOR, Engine, Rejected

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


def story(gm):
    return gm.inspect("Story")["state"]


def run(gm, seconds):
    for _ in range(int(seconds // 60)):
        gm.clock(step=60)


def held(gm, who):
    return {c["name"] for c in gm.world.children(eid(gm, who))}


def test_a_surrender_to_the_fist_is_the_cells_not_a_grave():
    eng, gm, you = town()
    me = eid(gm, "Newcomer")
    gm.patch(me, {"hp": 200, "max_hp": 200})
    put(gm, "Newcomer", "Harbour Street")
    put(gm, "Ott Fennick", "Harbour Street", hold=True)
    gm.act_as("Dominico", "set_on", params={"who": "Newcomer"})
    for _ in range(6):  # the hunters find them, show themselves, and strike
        gm.clock(step=31)
        if gm.inspect("Newcomer")["state"].get("fight"):
            break
    you.act("yield", "Ott Fennick")
    assert where(gm, "Newcomer") == "The Cells"
    st = story(gm)
    assert st["peril_step"][me] == "jailed" and me in st["jailed"]
    assert not [h for h, r in (st.get("hunts") or {}).items() if r and r.get("target") == me]
    assert "Knife" not in held(gm, "Newcomer") and "Knife" in held(gm, "Evidence chest")
    try:  # the door is barred on the Hall side: going out is refused
        you.act("go", "The Town Hall")
        left = True
    except Rejected:
        left = False
    assert not left and where(gm, "Newcomer") == "The Cells"
    gm.clock(step=6 * 3600 + 60)
    run(gm, 60)
    assert where(gm, "Newcomer") == "The Town Hall" and "Knife" in held(gm, "Newcomer")
    assert me not in [k for k, v in (story(gm).get("jailed") or {}).items() if v]


def test_bail_and_a_yield_nobody_presses():
    eng, gm, you = town()
    me = eid(gm, "Newcomer")
    put(gm, "Newcomer", "Harbour Street")
    put(gm, "Ott Fennick", "Harbour Street", hold=True)
    you.act("yield", "Ott Fennick")  # nobody is pressing them: manners, not a surrender
    assert where(gm, "Newcomer") == "Harbour Street"
    gm.act_as("The Custodian", "warrant", params={"who": "Newcomer"})
    put(gm, "Lieutenant Voss", "Harbour Street", hold=True)
    you.act("yield", "Lieutenant Voss")
    assert where(gm, "Newcomer") == "The Cells" and me not in (story(gm).get("wanted") or [])
    put(gm, "Sergeant Pell Harrow", "The Town Hall", hold=True)
    gm.spawn("person", eid(gm, "The Town Hall"), "Friend", state={"hp": 10, "max_hp": 10})
    gm.spawn("thing", eid(gm, "Friend"), "Purse", state={"kind": "cp", "count": 600, "portable": True, "bulk": 0})
    gm.act_as("Friend", "give", "Sergeant Pell Harrow", params={"item": "Purse", "count": 500})
    assert where(gm, "Newcomer") == "The Town Hall"


def jailed(gm, you):
    """The Newcomer, warranted and yielded to Voss: in the cells. Voss is sent out of the Hall after."""
    gm.act_as("The Custodian", "warrant", params={"who": "Newcomer"})
    put(gm, "Newcomer", "Harbour Street")
    put(gm, "Lieutenant Voss", "Harbour Street", hold=True)
    you.act("yield", "Lieutenant Voss")
    assert where(gm, "Newcomer") == "The Cells"
    put(gm, "Lieutenant Voss", "Harbour Street", hold=True)
    for n in ["Sergeant Pell Harrow", "Constable Abel Fitch", "Constable Rosa Quint"]:
        put(gm, n, "Market Square", hold=True)
    gm.spawn("person", eid(gm, "The Town Hall"), "Friend", state={"hp": 10, "max_hp": 10})
    gm.spawn("thing", eid(gm, "Friend"), "Purse", state={"kind": "cp", "count": 600, "portable": True, "bulk": 0})


def test_two_gold_to_rosa_is_the_key_and_the_prisoner_walks_out_wanted():
    """The owner, 2026-11-23: "We gonna need rules to break someone out of prison." Rosa carries the cell key and
    takes bribes: two gold, and the key is in your hand while she is at the market."""
    eng, gm, you = town()
    me = eid(gm, "Newcomer")
    jailed(gm, you)
    rosa_key = next(c for c in gm.world.children(eid(gm, "Constable Rosa Quint")) if c["name"] == "Cell key")
    put(gm, "Constable Rosa Quint", "The Town Hall", hold=True)
    gm.act_as("Friend", "give", "Constable Rosa Quint", params={"item": "Purse", "count": 100})
    assert "Cell key" not in held(gm, "Friend")  # one gold is a mango
    gm.act_as("Friend", "give", "Constable Rosa Quint", params={"item": "Purse", "count": 100})
    assert "Cell key" in held(gm, "Friend") and where(gm, "Constable Rosa Quint") == "The Night Market"
    gm.act_as("Friend", "unlock", "Cell bar")
    gm.clock(step=5)
    you.act("go", "The Town Hall")
    run(gm, 60)
    st = story(gm)
    assert where(gm, "Newcomer") == "The Town Hall" and me in st["wanted"]
    assert eid(gm, "Friend") not in (st.get("wanted") or [])  # nobody saw who opened it
    bar = gm.inspect("Cell bar")["state"]
    assert bar["locked"] and bar["key"] != rosa_key["id"]  # the watch changed the padlock: her old key fits nothing
    assert "Cell key" in held(gm, "Constable Rosa Quint")


def test_working_the_cell_door_in_front_of_the_watch_is_a_crime():
    eng, gm, you = town()
    jailed(gm, you)
    put(gm, "Lieutenant Voss", "The Town Hall", hold=True)
    gm.patch(eid(gm, "Friend"), {"hp": 200, "max_hp": 200})
    gm.act_as("Friend", "break", "Cell bar")
    gm.clock(step=130)
    st = story(gm)
    assert eid(gm, "Friend") in st["wanted"]
    assert gm.inspect("Friend")["state"].get("attacked_by") == eid(gm, "Lieutenant Voss")  # fought on the spot


def test_a_prisoner_heard_at_the_door_gets_another_hour():
    eng, gm, you = town()
    me = eid(gm, "Newcomer")
    jailed(gm, you)
    before = story(gm)["jailed"][me]
    put(gm, "Sergeant Pell Harrow", "The Town Hall", hold=True)
    you.act("break", "Cell bar")
    gm.clock(step=130)
    assert story(gm)["jailed"][me] == before + 3600
    assert gm.inspect("Cell bar")["state"]["locked"] and where(gm, "Newcomer") == "The Cells"


def test_the_undertaker_brings_the_dead_to_the_quiet_ground():
    eng, gm, you = town()
    put(gm, "Husok Sourfist", "Market Square", hold=True)
    gm.patch(eid(gm, "Husok Sourfist"), {"dead": True, "down": True, "hp": 0})
    run(gm, 60)
    assert where(gm, "Husok Sourfist") == "Market Square"  # half an hour to lie, for anyone who would sit with them
    gm.patch(eid(gm, "Husok Sourfist"), {"died_at": gm.summary()["t"] - 3600})
    run(gm, 660)
    graves = [e for e in gm.world.find(type="grave", limit=10) if e["state"].get("lies") == "Husok Sourfist"]
    assert graves and gm.world.get(graves[0]["parent_id"])["name"] == "The Quiet Ground"
    assert graves[0]["state"]["buried_by"] == "Ottoline Crabbe"
    assert gm.inspect("Husok Sourfist")["state"].get("buried_in") == graves[0]["id"]
    put(gm, "Newcomer", "The Quiet Ground")
    gm.spawn("thing", eid(gm, "Newcomer"), "Purse", state={"kind": "cp", "count": 100, "portable": True, "bulk": 0})
    you.act("buy", "Ottoline Crabbe", {"item": "marker"})
    assert "Grave marker" in held(gm, "Newcomer")


def test_a_dead_seat_still_held_is_not_carried_off():
    eng, gm, you = town()
    put(gm, "Newcomer", "Market Square")
    gm.patch(eid(gm, "Newcomer"), {"dead": True, "down": True, "hp": 0, "died_at": gm.summary()["t"] - 3600})
    run(gm, 660)
    assert where(gm, "Newcomer") == "Market Square"  # its player still sits in it
