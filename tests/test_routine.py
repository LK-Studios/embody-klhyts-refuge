"""The town's day (owner, 2026-11-23): people walk their routines, carry their own money, are seen at their work, and
are met by their look before their name. And the news of the night reaches them as flags their lines answer to; River's
cove is hidden until someone finds the shore path."""

import re
from pathlib import Path

import pytest

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


def where(gm, name):
    p = gm.inspect(name)["parent"]
    return p["id"] if isinstance(p, dict) else p


def scenes(gm, since, place=None):
    w = gm.world
    return [e["payload"].get("text") for e in w.events(since=since, limit=2000)
            if e["kind"] == "scene" and (place is None or e["target_id"] == place)]


def coins(gm, name):
    c = next(x for x in gm.world.children(eid(gm, name)) if x["name"] == "Coin")
    return int(gm.inspect(c["id"])["state"].get("count") or 0)


def run(gm, seconds):
    """The clock a minute at a time, as a hosted world's runs: a repeating timer fires once a step."""
    for _ in range(int(seconds // 60)):
        gm.clock(step=60)


def day_for(gm, name, slots, **more):
    """Give someone a plain day for the test: at 22.0 the first slot, at the clock's next quarter the second."""
    gm.patch(eid(gm, name), {"routine": None})
    gm.patch(eid(gm, name), {"routine": slots, "routine_key": None, "routine_hold_until": None, **more})


def test_a_new_slot_walks_them_there_and_the_room_they_leave_sees_them_go(tmp_path):
    eng, gm, you = town()
    w = gm.world
    docks, turtle = eid(gm, "The Docks"), eid(gm, "The Turtle Dragon")
    since = w.store.next_seq(w.id)
    now_h = (gm.summary()["t"] % 86400) / 3600
    day_for(gm, "Harbourmaster Teague", [
        {"at": 20.0, "place": docks, "doing": "He counts the boats."},
        {"at": now_h + 0.05, "place": turtle, "doing": "He nurses a small beer by the window.",
         "go": "The stooped man in the salt-white coat tucks his tally board under his arm and goes up Harbour Street."}],
        look="A stooped man in a salt-white coat with a pencil behind each ear.")
    run(gm, 60 * 12)
    assert where(gm, "Harbourmaster Teague") == turtle
    st = gm.inspect("Harbourmaster Teague")["state"]
    assert st["post"] == turtle
    assert st["description"] == "A stooped man in a salt-white coat with a pencil behind each ear. He nurses a small beer by the window."
    assert any("tucks his tally board" in (t or "") for t in scenes(gm, since, docks))  # the Newcomer stands on the docks


def test_a_slot_pays_and_a_held_or_hired_or_following_body_keeps_still(tmp_path):
    eng, gm, you = town()
    ogre, turtle = eid(gm, "Rampant Ogre & Curved Cleaver"), eid(gm, "The Turtle Dragon")
    now_h = (gm.summary()["t"] % 86400) / 3600
    before = coins(gm, "Bosun Maggs")
    ludo = coins(gm, "Big Ludo")
    day_for(gm, "Big Ludo", [{"at": 20.0, "place": ogre, "doing": "He pours."},
                              {"at": now_h + 0.02, "place": ogre, "doing": "He pours, slower.",
                               "pay": {"to": eid(gm, "Bosun Maggs"), "cp": 7, "for": "a debt"}}])
    day_for(gm, "Tully", [{"at": 20.0, "place": turtle, "doing": "He sings."}])
    gm.patch(eid(gm, "Tully"), {"follows": eid(gm, "Big Ludo")})
    since = gm.world.store.next_seq(gm.world.id)
    run(gm, 60 * 8)
    paid = [e for e in gm.world.events(since=since, limit=5000) if e["kind"] == "paid"
            and e["payload"].get("by") == eid(gm, "Big Ludo") and e["target_id"] == eid(gm, "Bosun Maggs")]
    assert [e["payload"]["cp"] for e in paid] == [7]  # once, on the slot
    assert coins(gm, "Bosun Maggs") >= before + 7  # (others pay and are paid on their own slots too)
    assert where(gm, "Tully") == ogre  # following: his day waits


def test_the_story_holds_a_day_it_walked_and_klhyt_starts_his_when_free(tmp_path):
    eng, gm, you = town()
    hall, square = eid(gm, "The Town Hall"), eid(gm, "Market Square")
    now = gm.summary()["t"]
    day_for(gm, "The Custodian", [{"at": 20.0, "place": hall, "doing": "He signs papers."}],
            routine_hold_until=now + 3000)
    gm.move(eid(gm, "The Custodian"), square)
    gm.patch(eid(gm, "The Custodian"), {"post": square})
    run(gm, 60 * 10)
    assert where(gm, "The Custodian") == square  # held by the story for now
    k = gm.inspect("Klhyt")["state"]
    assert k.get("routine_when") == ["klhyt_freed"] or not k.get("routine")


def test_the_cove_is_hidden_until_someone_finds_the_shore_path(tmp_path):
    eng, gm, you = town()
    w = gm.world
    cove = eid(gm, "The Cove Behind the Reef")
    me = eid(gm, "Newcomer")
    assert w.knows_way(eid(gm, "River"), cove)
    assert not w.knows_way(me, cove)
    names = [x.get("name") for x in (you.perceive().get("exits") or [])]
    assert "The Cove Behind the Reef" not in names
    gm.patch(me, {"sheet": {"attributes": {"acuity": 20}, "skills": {"survival": 2}}})
    for _ in range(6):  # a d20 is a d20: try until it passes the DC 15, each try a fresh hour
        you.act("check", params={"skill": "survival", "dc": 15})
        if w.knows_way(me, cove):
            break
        gm.clock(step=3600)
    assert w.knows_way(me, cove)


def test_the_town_hears_klhyt_is_home(tmp_path):
    eng, gm, you = town()
    w = gm.world
    gm.move(eid(gm, "Newcomer"), eid(gm, "The Bonded Warehouse"))
    you.act("free", "Klhyt")
    run(gm, 200)
    assert gm.inspect("Story")["state"].get("custodian_exposed")
    for name in ["Fat Gog", "River", "Mother Ines", "Harbourmaster Teague"]:
        assert gm.inspect(name)["state"].get("klhyt_home") is True, name
    assert gm.inspect("The Custodian")["state"].get("disgraced") is True


# ---- the cast files: what the writers were asked for (cast/*.py) -----------------------------------------------------

import importlib.util


def cast():
    spec = importlib.util.spec_from_file_location("refuge_build_for_test", WORLD / "build.py")
    import sys
    sys.path.insert(0, str(REPO))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


COMMON = {"you", "your", "the", "a", "is", "are", "what", "do", "have", "here", "there", "this", "that", "it", "me", "my",
          "i", "and", "about", "tell", "to", "of", "in", "on", "for", "with"}


def test_the_cast_is_whole_and_tells_no_names():
    b = cast()
    if not b.CAST:
        pytest.skip("no cast files yet")
    spawned = {n for _, _, n, _, _ in b.people()} | {h[0] for h in b.HOUSEHOLD} | {s[0] for s in b.SAILORS} | set(b.NEW_PEOPLE) | {"Ondrine"}
    problems = []
    for name, c in b.CAST.items():
        if name not in spawned:
            problems.append(f"{name}: no such person")
        first = name.replace("The ", "").replace("Captain ", "").replace("Harbourmaster ", "").replace("Sister ", "") \
            .replace("Bosun ", "").replace("Master ", "").replace("Lieutenant ", "").replace("Mother ", "").replace("Big ", "") \
            .replace("Constable ", "").replace("Sergeant ", "").split()[0]
        texts = [c.get("look", ""), c.get("seen_as") or ""] + [s.get("doing", "") for s in c.get("routine") or []] + \
                [s.get("go", "") or "" for s in c.get("routine") or []] + list(c.get("beats") or [])
        for t in texts:
            if re.search(r"\b" + re.escape(first) + r"\b", t):
                problems.append(f"{name}: names them in {t[:60]!r}")
        for key in (c.get("dialog") or {}):
            for alias in key.split("|"):
                if " " in alias or alias != alias.lower() or alias in COMMON:
                    problems.append(f"{name}: alias {alias!r}")
        d = c.get("default_line")
        if not isinstance(d, list) or not 3 <= len(d) <= 5:
            problems.append(f"{name}: default_line should be 3 to 5 lines")
        for s in c.get("routine") or []:
            if s.get("place") not in b.PLACES:
                problems.append(f"{name}: no place {s.get('place')!r}")
        blob = repr(c)
        if "—" in blob or "–" in blob:
            problems.append(f"{name}: a dash")
    assert not problems, "\n".join(problems)
