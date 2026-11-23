"""Hired help: the one way a player brings a second agent into the Refuge. A person marked for hire names their price
(coin by the day, a thing, a favour), the hire offers the hirer their seat, a character keeps 1 + Charisma of them,
and the seat goes back when the days run out or the hirer lets them go."""

import re
from pathlib import Path

import pytest

from embody.cli import load_world
from embody.ops import AUTHOR, Engine, Rejected

REPO = next(p for p in Path(__file__).resolve().parents if (p / "pyproject.toml").exists())
WORLD = Path(__file__).resolve().parents[1]


def town():
    eng = Engine(":memory:", workspace=REPO, record=False)  # the test's author moves stay out of changes.jsonl
    gm = eng.session("gm", capabilities=[AUTHOR])
    load_world(gm, WORLD)
    g = gm.invite("player", entity="Newcomer", label="p")
    you = eng.session_for_token(g["token"])
    you.join()
    return eng, gm, you


def eid(gm, name):
    return next(e["id"] for e in gm.world.find(limit=None) if e["name"] == name)


def here(gm, *names):
    """Bring these people to where the Newcomer stands."""
    at = gm.inspect("Newcomer")["parent"]
    at = at["id"] if isinstance(at, dict) else at
    for n in names:
        gm.move(eid(gm, n), at)
        # or their idle walk takes them back to their own post, and their day to the next place in it
        gm.patch(eid(gm, n), {"post": at, "routine_hold_until": 10 ** 9})


def purse(gm, you, cp=None, cha=None):
    me = eid(gm, "Newcomer")
    coin = next(c for c in gm.world.children(me) if c["name"] == "Coin")
    if cp is not None:
        gm.patch(coin["id"], {"count": cp})
    if cha is not None:
        gm.patch(me, {"sheet": {"attributes": {"projection": cha}}})
    return gm.inspect(coin["id"])["state"].get("count", 1)


def token_in(paste):
    return re.search(r"Bearer ([A-Za-z0-9_-]{20,})", paste).group(1)


def test_coin_hires_for_days_offers_the_seat_and_the_days_run_out():
    eng, gm, you = town()
    here(gm, "Kael Ironjaw", "Tully")
    purse(gm, you, cp=500, cha=8)
    r = you.act("hire", "Kael Ironjaw")  # asked bare: the price, and nothing changes hands
    assert r["result"] == {"hired": False} and purse(gm, you) == 500
    r = you.act("hire", "Kael Ironjaw", params={"days": 1})
    assert r["result"]["hired"] and purse(gm, you) == 450
    kael = gm.inspect("Kael Ironjaw")["state"]
    assert kael["hired"]["by"] == eid(gm, "Newcomer") and kael["follows"] == eid(gm, "Newcomer")
    post = kael["hired"]["post"]
    assert post and not kael.get("post")  # his post waits while he follows you
    offer = you.seats()["offers"][0]
    assert offer["name"] == "Kael Ironjaw"
    paste = you.claim_seat(offer["offer"])["paste"]
    sub = eng.session_for_token(token_in(paste))
    assert sub.join()["you"]["name"] == "Kael Ironjaw"
    with pytest.raises(Rejected) as e:  # the hired one's agent hires nobody: no chain of agents
        sub.act("hire", "Tully", params={"days": 1})
    assert "a hireling hires nobody" in e.value.reason
    gm.clock(step=86400 + 120)
    assert gm.world.embodied(eid(gm, "Kael Ironjaw")) is None  # the days ran out: the seat went back
    assert eng.session_for_token(token_in(paste)) is None
    assert not gm.inspect("Kael Ironjaw")["state"].get("hired")
    assert gm.inspect("Kael Ironjaw")["state"]["post"] == post and not gm.inspect("Kael Ironjaw")["state"].get("follows")
    assert not gm.inspect("Newcomer")["state"].get("hirelings")


def test_charisma_says_how_many_and_dismiss_frees_one():
    eng, gm, you = town()
    here(gm, "Kael Ironjaw", "Tully", "Hanklevode")
    purse(gm, you, cp=5000, cha=8)  # Charisma 8: -1, so one at a time
    you.act("hire", "Kael Ironjaw", params={"days": 1})
    with pytest.raises(Rejected) as e:
        you.act("hire", "Tully", params={"days": 1})
    assert "you keep 1 in your hire at once" in e.value.reason and "Kael Ironjaw" in e.value.reason
    you.act("hire", "Kael Ironjaw", params={"days": 2})  # more days for the one you have is no new hire
    assert purse(gm, you) == 5000 - 150
    with pytest.raises(Rejected) as e:
        you.act("hire", "Kael Ironjaw", params={"days": 5})  # 3 paid days ahead plus 5 is past his 7
    assert "at most 7 days" in e.value.reason
    you.act("dismiss", "Kael Ironjaw")
    assert not gm.inspect("Kael Ironjaw")["state"].get("hired") and not you.seats().get("offers")
    you.act("hire", "Tully", params={"days": 1})
    purse(gm, you, cha=14)  # Charisma 14: +2, so three
    you.act("hire", "Kael Ironjaw", params={"days": 1})
    you.act("hire", "Hanklevode", params={"days": 1})
    assert {o["name"] for o in you.seats()["offers"]} == {"Tully", "Kael Ironjaw", "Hanklevode"}


def test_not_everyone_works_for_coin_and_some_cost_a_fortune():
    eng, gm, you = town()
    here(gm, "Ssark", "Thoradin", "Deloris", "River")
    purse(gm, you, cp=900, cha=16)
    with pytest.raises(Rejected) as e:
        you.act("hire", "River")
    assert "not for hire" in e.value.reason
    # Deloris is hard to win: a favour first, then a fortune, and she joins as herself (her seat is Ed's alone)
    assert you.act("hire", "Deloris", params={"days": 1})["result"] == {"hired": False}
    gm.patch(eid(gm, "Deloris"), {"favoured": {eid(gm, "Newcomer"): True}})
    with pytest.raises(Rejected) as e:
        you.act("hire", "Deloris", params={"days": 1})
    assert "25gp, and you have 9gp" in e.value.reason
    purse(gm, you, cp=3400)
    assert you.act("hire", "Deloris", params={"days": 1})["result"]["hired"] and purse(gm, you) == 900
    assert gm.inspect("Deloris")["state"]["follows"] == eid(gm, "Newcomer") and not you.seats().get("offers")
    r = you.act("hire", "Ssark")  # wants a rum, not coin: without one, he says so
    assert r["result"] == {"hired": False}
    gm.spawn("thing", eid(gm, "Newcomer"), "Tot of rum", state={"portable": True})
    assert you.act("hire", "Ssark")["result"]["hired"]
    assert any(c["name"] == "Tot of rum" for c in gm.world.children(eid(gm, "Ssark"))) and purse(gm, you) == 900
    assert you.act("hire", "Thoradin")["result"] == {"hired": False}  # the favour comes first
    gm.patch(eid(gm, "Thoradin"), {"favoured": {eid(gm, "Newcomer"): True}})  # the narrator marks it done
    assert you.act("hire", "Thoradin")["result"]["hired"]
    assert not (gm.inspect("Thoradin")["state"].get("favoured") or {}).get(eid(gm, "Newcomer"))  # spent


def test_the_town_is_wired_for_it():
    eng, gm, you = town()
    root = gm.inspect(gm.summary()["root"])["state"]
    assert root["seat_slots"] == 6 and "Hired help:" in root["briefing"]
    assert root["briefing"].count("At this table:") == 1 and "never say \"one moment\"" in root["briefing"]
    for name in ("Tully", "Kael Ironjaw", "Hanklevode", "Thoradin", "Ssark"):
        st = gm.inspect(name)["state"]
        assert st["for_hire"] and st["seatable"], name
    assert gm.inspect("Deloris")["state"]["for_hire"]["favour"] and not gm.inspect("Deloris")["state"].get("seatable")
    assert not gm.inspect("River")["state"].get("seatable")


def test_only_ed_plays_deloris_and_nobody_picks_kael():
    eng, gm, you = town()
    ana = eng.session_for_token(gm.invite("player", label="ana")["token"])
    for name in ("Deloris", "Kael Ironjaw"):  # an open invite picks neither
        with pytest.raises(Rejected) as e:
            ana.join("klhyts-refuge", name)
        assert "not a seat you may take" in e.value.reason, name
    ed = eng.session_for_token(gm.invite("player", entity="Deloris", label="Ed")["token"])
    assert ed.join()["you"]["name"] == "Deloris"  # Ed's own invite names her
    here(gm, "Deloris")
    purse(gm, you, cp=5000)
    gm.patch(eid(gm, "Deloris"), {"favoured": {eid(gm, "Newcomer"): True}})
    with pytest.raises(Rejected) as e:  # with Ed in her, terms are Ed's to talk, not a hire to buy
        you.act("hire", "Deloris", params={"days": 1})
    assert "a mind of their own" in e.value.reason
