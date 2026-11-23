"""The Custodian found out doubles down, and a magistrate of the Throne is due (owner, 2026-11-23: "he should be more
militant. He is a Vorkathian empire representative"; "A magistrate is due to arrive. They would have been at sea months.
So who knows who they will decide on"; "The next week (5-9 days)"). Which Arm of Vorkath the magistrate serves is drawn
when they land, and it decides how the case is weighed; every Arm posts a decree."""

from pathlib import Path

from embody.cli import load_world
from embody.ops import AUTHOR, Engine

REPO = next(p for p in Path(__file__).resolve().parents if (p / "pyproject.toml").exists())
WORLD = Path(__file__).resolve().parents[1]
DAY = 86400


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
    p = gm.inspect(name)["parent"]
    return p["name"] if isinstance(p, dict) else gm.world.get(p)["name"]


def story(gm):
    return gm.inspect("Story")["state"]


def run(gm, seconds):
    for _ in range(int(seconds // 60)):
        gm.clock(step=60)


def said(r):
    return " ".join(str(e["payload"].get("text")) for e in r["events"] if e["kind"] in ("say", "gestured"))


def expose(gm, you):
    """Free Klhyt and let him tell the square: the Custodian is found out."""
    gm.move(eid(gm, "Newcomer"), eid(gm, "The Bonded Warehouse"))
    you.act("free", "Klhyt")
    run(gm, 240)
    assert story(gm)["custodian_exposed"]


def land(gm, arm=None):
    """Bring the ship in now, not in a week; optionally hold the magistrate to one Arm for the weighing."""
    gm.schedule(30, "magistrate_lands", entity=gm.world.root_id)
    run(gm, 60)
    st = story(gm)
    assert st["magistrate"]
    if arm:
        gm.patch(gm.inspect("Story")["id"], {"magistrate_arm": arm})
    for who in [st["magistrate"]] + list(st["magistrate_guards"]):  # the test lands them at night, not at nine:
        gm.patch(who, {"routine_hold_until": 10 ** 9})              # their day would walk them off to dinner
    return gm.inspect(st["magistrate"])


def paper(gm, you, clue):
    me = eid(gm, "Newcomer")
    gm.spawn("letter", me, "Paper (" + clue + ")", state={"clue": clue, "portable": True, "bulk": 0, "text": clue})
    return "Paper (" + clue + ")"


def test_the_magistrate_is_due_in_five_to_nine_days_at_nine(tmp_path):
    eng, gm, you = town()
    st = story(gm)
    now = gm.summary()["t"]
    days = st["magistrate_eta"] // DAY - now // DAY
    assert 5 <= days <= 9 and st["magistrate_eta"] % DAY == 9 * 3600
    kinds = {t["kind"] for t in gm.timers()}
    assert {"magistrate_sighted", "magistrate_lands"} <= kinds
    assert sorted(st["magistrate_spec"]["arms"]) == sorted(["war", "peace", "pleasure", "pain", "chaos", "destiny", "death", "life"])


def test_found_out_the_custodian_holds_the_hall_and_talks_of_the_magistrate(tmp_path):
    eng, gm, you = town()
    expose(gm, you)
    c = gm.inspect("The Custodian")["state"]
    assert c["disgraced"] and "eight-armed sigil" in c["look"]
    assert where(gm, "The Custodian") == "The Town Hall"
    gm.move(eid(gm, "Newcomer"), eid(gm, "The Town Hall"))
    you.step(to="The Custodian")
    r = you.act("talk", "The Custodian", {"about": "is a magistrate coming?"})
    assert "due within the week" in said(r)


def test_the_inquisition_upholds_him_and_the_peace_arm_does_not(tmp_path):
    for arm, want in (("pain", "upheld"), ("peace", "removed")):
        eng, gm, you = town()
        expose(gm, you)
        mag = land(gm, arm)
        assert where(gm, mag["name"]) == "The Docks"
        assert all(where(gm, g) == "The Docks" for g in ["Throne Guard Henrik Vael", "Throne Guard Oriane Sall"])
        gm.move(eid(gm, "Newcomer"), eid(gm, "The Docks"))
        you.step(to=mag["name"])
        for clue in ["tally", "letter", "passage"]:
            you.act("show", mag["name"], {"item": paper(gm, you, clue)})
        assert sorted(story(gm)["magistrate_shown"]) == ["letter", "passage", "tally"]
        gm.schedule(30, "hearing", entity=gm.world.root_id)
        run(gm, 60)
        st = story(gm)
        assert st["verdict"] == want, (arm, st["verdict_weighed"])
        assert gm.inspect("Fat Gog")["state"]["verdict"] == want and st["decree"] == arm
        assert "The Magistrate's Proclamation" in {e["name"] for e in gm.world.find(limit=None)}
        c = gm.inspect("The Custodian")["state"]
        if want == "removed":
            assert c["in_irons"] and where(gm, "The Custodian") == "The Docks"
        else:
            assert c["upheld"] and "seal" in c["look"]


def test_the_town_hears_the_magistrate_in_stages(tmp_path):
    eng, gm, you = town()
    expose(gm, you)
    gm.move(eid(gm, "Newcomer"), eid(gm, "Market Square"))
    gm.move(eid(gm, "Klhyt"), eid(gm, "Market Square"))
    gm.patch(eid(gm, "Klhyt"), {"routine_hold_until": 10 ** 9, "post": eid(gm, "Market Square")})
    you.step(to="Klhyt")
    assert "Article One" in said(you.act("talk", "Klhyt", {"about": "the magistrate"}))
    land(gm, "war")
    gm.move(eid(gm, "Newcomer"), eid(gm, "Market Square"))
    you.step(to="Klhyt")
    assert "Tomorrow at ten" in said(you.act("talk", "Klhyt", {"about": "the magistrate"}))
    gm.schedule(30, "hearing", entity=gm.world.root_id)
    run(gm, 60)
    verdict = story(gm)["verdict"]
    you.step(to="Klhyt")
    line = said(you.act("talk", "Klhyt", {"about": "the magistrate's verdict"}))
    assert ("irons" in line) if verdict == "removed" else ("Upheld" in line)
