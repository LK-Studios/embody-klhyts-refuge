"""Shops, keepers who keep their houses, and work from more than Gog (owner, 2026-11-23: "we need some shops. Adventurer
stuffs food, weapons. Armour ... Make sure a rapier is for sale"; "The touchy unicorn seems to have lost its owner bar
keep"; "Key NPCs need power and agency")."""

from pathlib import Path

from embody.cli import load_world
from embody.ops import AUTHOR, Engine

REPO = next(p for p in Path(__file__).resolve().parents if (p / "pyproject.toml").exists())
WORLD = Path(__file__).resolve().parents[1]
DAY = 86400
SHOPS = {"Hob Merrow": "Merrow's Chandlery", "Tamsin Vey": "The Crooked Anvil", "Zuri Coralhand": "Coral and Chain"}
TAVERNS = {"Wendeline Moss": "The Touchy Unicorn", "Bosun Maggs": "The Turtle Dragon", "Big Ludo": "Rampant Ogre & Curved Cleaver",
           "Sister Agathe": "The Omberhulk & Nun", "Master Quillon": "The High Apothecary"}


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


def put(gm, name, place, hold=False):
    gm.move(eid(gm, name), eid(gm, place))
    gm.patch(eid(gm, name), {"post": eid(gm, place), **({"routine_hold_until": 10 ** 9} if hold else {})})


def story(gm):
    return gm.inspect("Story")["state"]


def run(gm, seconds):
    for _ in range(int(seconds // 60)):
        gm.clock(step=60)


def purse(gm, amount):
    gm.spawn("thing", eid(gm, "Newcomer"), "Purse", state={"kind": "cp", "count": amount, "portable": True, "bulk": 0})


def coin(gm, name):
    return sum(int(c["state"].get("count") or 0) for c in gm.world.children(eid(gm, name)) if c["state"].get("kind") == "cp")


def held(gm, name):
    return {c["name"]: c["state"] for c in gm.world.children(eid(gm, "Newcomer"))}.get(name)


def offered(gm, r):
    return sorted(gm.world.get(e["payload"]["job"])["name"] for e in r["events"] if e["kind"] == "job_offered")


def test_chandlers_row_and_its_three_shops_and_their_keepers():
    eng, gm, you = town()
    ways = {e["target"] for e in gm.world.edges(eid(gm, "Chandlers' Row"), "connects_to", "out")}
    for p in ["Harbour Street", "The Night Market"] + list(SHOPS.values()):
        assert eid(gm, p) in ways
    for keeper, shop in SHOPS.items():
        assert where(gm, keeper) == shop
        st = gm.inspect(keeper)["state"]
        assert st.get("sells") and st.get("look") and len(st.get("dialog") or {}) >= 20
        assert {gm.world.get(sl["place"])["name"] for sl in st["routine"]} == {shop}  # they keep the shop, every hour


def test_a_rapier_for_sale_and_it_fights_as_a_rapier():
    eng, gm, you = town()
    purse(gm, 3000)
    put(gm, "Newcomer", "The Crooked Anvil")
    before, till = coin(gm, "Newcomer"), coin(gm, "Tamsin Vey")
    you.act("buy", "Tamsin Vey", {"item": "rapier"})
    r = held(gm, "Rapier")
    assert r and r["weapon"] and r["dice"] == "1d8" and "finesse" in r["properties"]
    assert coin(gm, "Newcomer") == before - 2500 and coin(gm, "Tamsin Vey") == till + 2500


def test_armour_and_a_healing_potion():
    eng, gm, you = town()
    purse(gm, 12000)
    put(gm, "Newcomer", "Coral and Chain")
    you.act("buy", "Zuri Coralhand", {"item": "chain shirt"})
    assert held(gm, "Chain shirt")["armor"]["ac"] == 13
    put(gm, "Newcomer", "Merrow's Chandlery")
    you.act("buy", "Hob Merrow", {"item": "potion of healing"})
    you.act("buy", "Hob Merrow", {"item": "rations"})
    you.act("buy", "Hob Merrow", {"item": "waterskin"})
    assert held(gm, "Potion of healing")["heals"] and held(gm, "Trail rations") and held(gm, "Waterskin")["capacity"]
    me = eid(gm, "Newcomer")
    gm.patch(me, {"hp": 1})
    you.act("drink", "Potion of healing")
    assert gm.inspect("Newcomer")["state"]["hp"] > 1


def test_the_tavern_keepers_keep_their_houses_from_evening_to_closing():
    eng, gm, you = town()
    for keeper, tavern in TAVERNS.items():
        for sl in gm.inspect(keeper)["state"]["routine"]:
            h = float(sl["at"])
            if not 5.0 <= h < 8.0:
                assert gm.world.get(sl["place"])["name"] == tavern, (keeper, h)


def test_river_gives_a_note_for_the_lamplighter():
    eng, gm, you = town()
    put(gm, "Newcomer", "The Stripperwitch")
    r = you.act("talk", "River", {"about": "got any errand for me, love?"})
    assert "A note for the lamplighter" in offered(gm, r)
    you.act("take_job", params={"job": "A note for the lamplighter"})
    assert held(gm, "River's note")
    put(gm, "Ned Tallow", "The Stripperwitch", hold=True)
    before = coin(gm, "Newcomer")
    you.act("give", "Ned Tallow", {"item": "River's note"})
    assert coin(gm, "Newcomer") == before + 20


def test_klhyt_asks_for_paper_and_the_custodian_buys_it():
    eng, gm, you = town()
    put(gm, "Newcomer", "The Bonded Warehouse")
    you.act("free", "Klhyt")
    run(gm, 240)
    assert story(gm)["custodian_exposed"]
    put(gm, "Klhyt", "The Stripperwitch", hold=True)
    put(gm, "Newcomer", "The Stripperwitch")
    r = you.act("talk", "Klhyt", {"about": "how can I help you? is there work?"})
    assert "Paper for the mayor" in offered(gm, r) and "The steps at ten" in offered(gm, r)
    you.act("take_job", params={"job": "Paper for the mayor"})
    gm.spawn("letter", eid(gm, "Newcomer"), "Paper (letter)", state={"clue": "letter", "portable": True, "bulk": 0,
                                                                     "text": "letter"})
    before = coin(gm, "Newcomer")
    you.act("show", "Klhyt", {"item": "Paper (letter)"})
    assert coin(gm, "Newcomer") == before + 200
    put(gm, "The Custodian", "The Town Hall", hold=True)
    put(gm, "Newcomer", "The Town Hall")
    r = you.act("talk", "The Custodian", {"about": "perhaps we could make a deal"})
    assert "The Custodian's bargain" in offered(gm, r)
    you.act("take_job", params={"job": "The Custodian's bargain"})
    before = coin(gm, "Newcomer")
    you.act("give", "The Custodian", {"item": "Paper (letter)"})
    assert coin(gm, "Newcomer") == before + 1000
    assert not [e for e in gm.world.find(limit=None) if e["name"] == "Paper (letter)"]  # burned


def test_a_players_body_stays_where_they_left_it():
    # a player, 2026-11-23: their character was walked back to the pier while they were away ("make sure it's not
    # just jolting bodies around and puppeteering players"); the d20 pack's idle care walked a held seat to its post
    eng, gm, you = town()
    gm.world.set_meta({"idle_after": 50})
    assert gm.inspect("Newcomer")["state"].get("stays")
    assert all(t["state"].get("stays") for t in (gm.inspect(gm.world.root_id)["state"].get("templates") or {}).values())
    put(gm, "Newcomer", "Market Square")
    gm.patch(eid(gm, "Newcomer"), {"post": eid(gm, "The Docks")})
    run(gm, 600)
    assert where(gm, "Newcomer") == "Market Square"
