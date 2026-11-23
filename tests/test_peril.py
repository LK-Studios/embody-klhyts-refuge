"""Peril (owner, 2026-11-23: "I don't feel like the antagonists are really antangoist enough. I have not ecounttered
them being anything but passive. And it has made every mission too easy. We need more peril!"; asked, "Full 5e, to the
death" and "World first, minds after"). Heat brings a tail, a warning and then the Fist's men, who fight to kill; every
way off Brask's door has a price and a clock; Dominico wants the paper he is shown; the Custodian posts the Throne's
warrant and works on the witnesses; Klhyt can die before he reaches the square."""

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
    gm.patch(gm.world.root_id, {"dnd5e": {"player_rolls": False}})  # the world rolls the player's initiative too
    g = gm.invite("player", entity="Newcomer", label="p")
    you = eng.session_for_token(g["token"])
    you.join()
    return eng, gm, you, g["token"]


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


def scenes(gm, since=0):
    return [str((e.get("payload") or {}).get("text")) for e in gm.history(since=since, kinds=["scene"], limit=2000)]


def last_seq(gm):
    return gm.history(newest=True, limit=1)[-1]["seq"]


def hunts(gm, mode, target):
    return [h for h, r in (story(gm).get("hunts") or {}).items() if r and r["mode"] == mode and r["target"] == target]


def test_asking_about_the_crate_where_the_fist_drinks_brings_a_tail_then_a_warning():
    eng, gm, you, _ = town()
    me = eid(gm, "Newcomer")
    put(gm, "Newcomer", "The Omberhulk & Nun")
    since = last_seq(gm)
    for i in range(3):
        you.say("Has anyone seen Klhyt? They say there's a crate in the warehouse.")
        gm.clock(step=301)
    st = story(gm)
    assert st["heat"][me] == 3 and st["peril_step"][me] == "tailed"
    tail = hunts(gm, "tail", me)
    assert tail
    run(gm, 600)
    assert gm.world.get(tail[0])["parent_id"] == gm.world.get(me)["parent_id"]
    assert any("does not look your way" in t for t in scenes(gm, since))
    for i in range(2):
        you.say("And the Custodian's dues: who skims them?")
        gm.clock(step=301)
    assert story(gm)["peril_step"][me] == "warned"
    run(gm, 1800)
    assert any("bad for your health" in t or "heard your name" in t for t in scenes(gm, since))


def test_the_fists_word_sends_men_who_fight_to_kill():
    eng, gm, you, _ = town()
    me = eid(gm, "Newcomer")
    put(gm, "Newcomer", "Harbour Street")
    gm.patch(me, {"hp": 4, "max_hp": 4, "ac": 5})
    since = last_seq(gm)
    gm.act_as("Dominico", "set_on", params={"who": "Newcomer"})
    assert story(gm)["peril_step"][me] == "marked"
    gm.clock(step=31)  # one tick: the wave goes out
    assert len(hunts(gm, "kill", me)) >= 2
    for _ in range(40):
        if gm.inspect("Newcomer")["state"].get("dead"):
            break
        gm.clock(step=60)
    assert gm.inspect("Newcomer")["state"].get("dead")
    assert any("come in out of the dark" in t or "walks straight at you" in t for t in scenes(gm, since))
    killers = [e["payload"].get("by") for e in gm.history(since=since, kinds=["killed"], limit=50)]
    assert any(gm.world.get(k) and gm.world.get(k)["state"].get("faction") == "the Fist" for k in killers if k)


def test_the_hunters_wait_outside_gogs_house_and_while_nobody_plays():
    eng, gm, you, token = town()
    me = eid(gm, "Newcomer")
    put(gm, "Newcomer", "The Stripperwitch")
    gm.act_as("Dominico", "set_on", params={"who": "Newcomer"})
    run(gm, 900)
    sent = hunts(gm, "kill", me)
    assert sent and all(where(gm, gm.world.get(h)["name"]) != "The Stripperwitch" for h in sent)
    assert not [f for f in gm.world.find(type="fight", limit=10) if gm.world.get(f["parent_id"])["name"] == "The Stripperwitch"]
    you.leave()
    run(gm, 120)
    for h in sent:
        assert gm.world.get(h)["state"].get("routine_hold_until") is None  # back to their own day
    assert hunts(gm, "kill", me) == sent  # and the hunt waits for them


def test_cowing_brask_brings_the_fist_to_the_door_in_five_minutes():
    eng, gm, you, _ = town()
    me = eid(gm, "Newcomer")
    gm.patch(me, {"scores": {"wis": 50, "cha": 50}})
    gm.patch(eid(gm, "Brask"), {"scores": {"wis": 1, "cha": 1}})
    r = you.act("threaten", "Brask")
    brask = gm.inspect("Brask")
    assert brask["state"]["left_post"] == "cowed"
    assert any(c["name"] == "Warehouse key" for c in gm.world.children(brask["id"]))  # he ran with it
    assert story(gm)["heat"][me] == 3
    run(gm, 360)
    assert story(gm)["fist_answered"] == "cowed"
    assert gm.inspect("Brask")["state"].get("left_post") is None and where(gm, "Brask") == "The Docks"
    fist_here = [p for p in gm.world.children(eid(gm, "The Docks")) if p["state"].get("faction") == "the Fist"
                 and not p["state"].get("dead")]
    assert len(fist_here) >= 2
    assert story(gm)["heat"][me] >= 6 and story(gm)["peril_step"][me] in ("warned", "marked")


def paper(gm, clue):
    gm.spawn("letter", eid(gm, "Newcomer"), "Paper (" + clue + ")",
             state={"clue": clue, "portable": True, "bulk": 0, "text": clue})
    return "Paper (" + clue + ")"


def test_dominico_holds_out_his_hand_for_the_paper():
    eng, gm, you, _ = town()
    me = eid(gm, "Newcomer")
    put(gm, "Newcomer", "The High Apothecary")
    put(gm, "Dominico", "The High Apothecary", hold=True)
    item = paper(gm, "letter")
    you.act("show", "Dominico", params={"item": item})
    st = story(gm)
    assert st["dominico_backed"] and st["dominico_wants"]["by"] == me
    you.act("give", "Dominico", params={"item": item})
    assert not [e for e in gm.world.find(limit=None) if e["name"] == item]  # burned
    assert not story(gm).get("dominico_wants") and int(story(gm)["heat"].get(me) or 0) == 0
    # shown again (another copy) and kept: marked
    item = paper(gm, "passage")
    gm.patch(gm.inspect("Story")["id"], {"dominico_backed": False})
    you.act("show", "Dominico", params={"item": item})
    run(gm, 180)
    assert story(gm)["peril_step"][me] == "marked"


def test_the_fist_fights_for_klhyt_on_the_waterfront_and_he_can_die():
    eng, gm, you, _ = town()
    me = eid(gm, "Newcomer")
    put(gm, "Newcomer", "The Bonded Warehouse")
    you.act("free", "Klhyt")
    assert story(gm)["freed_by"] == me and story(gm)["heat"][me] == 4
    put(gm, "Newcomer", "The Night Market")
    you.leave()
    gm.patch(eid(gm, "Klhyt"), {"hp": 1, "ac": 1, "max_hp": 1})
    gm.schedule(5, "fist_answers", entity=gm.world.root_id, payload={"why": "test"})
    for _ in range(30):
        if story(gm).get("klhyt_dead"):
            break
        gm.clock(step=60)
    st = story(gm)
    assert st["klhyt_dead"] and "Klhyt died" in st["outcome"]
    assert gm.inspect(gm.world.root_id)["state"]["story"] == "lost"
    assert not st.get("custodian_exposed")  # he never reached the square
    assert st["peril_step"][me] == "marked"


def test_the_custodian_posts_a_warrant_then_silences_a_witness():
    eng, gm, you, _ = town()
    me = eid(gm, "Newcomer")
    put(gm, "Newcomer", "The Bonded Warehouse")
    you.act("free", "Klhyt")
    run(gm, 240)
    assert story(gm)["custodian_exposed"]
    assert story(gm)["peril_step"][me] == "marked"  # Dominico lets Gog be, not the one who freed Klhyt
    you.leave()  # nobody plays them: nobody hunts them
    now = gm.summary()["t"]
    two = (now // DAY + 1) * DAY + 2 * 3600
    gm.clock(step=two - now - 60)  # a repeating timer fires once a step, at its start: land just short of two
    run(gm, 180)
    st = story(gm)
    assert me in st["wanted"]
    notice = [e for e in gm.world.find(limit=None) if e["name"] == "A WANTED notice"]
    assert notice and "WANTED" in notice[0]["state"]["text"] and "Newcomer" not in notice[0]["state"]["text"]
    assert gm.inspect("Vorkathia")["state"]["hostile"][me]
    gm.patch(gm.inspect("Story")["id"], {"clues": list(st["clues"]) + ["teague"]})
    gm.clock(step=DAY - 240)
    run(gm, 180)
    st = story(gm)
    assert "teague" in st["silenced"] and gm.inspect("Harbourmaster Teague")["state"]["silenced"]


def test_the_throne_attacks_the_wanted_on_sight():
    eng, gm, you, _ = town()
    me = eid(gm, "Newcomer")
    gm.act_as("The Custodian", "warrant", params={"who": "Newcomer"})
    assert me in story(gm)["wanted"]
    put(gm, "Lieutenant Voss", "Harbour Street", hold=True)
    since = last_seq(gm)
    put(gm, "Newcomer", "Harbour Street")
    run(gm, 60)
    fights = [f for f in gm.world.find(type="fight", limit=10) if gm.world.get(f["parent_id"])["name"] == "Harbour Street"]
    assert fights and gm.inspect("Lieutenant Voss")["state"].get("fight") == fights[0]["id"]
    assert any("By commission of the Throne" in t for t in scenes(gm, since))
    gm.act_as("The Custodian", "pardon", params={"who": "Newcomer"})
    assert me not in story(gm)["wanted"] and not (gm.inspect("Vorkathia")["state"].get("hostile") or {}).get(me)


def test_a_world_that_played_its_night_marks_whoever_freed_klhyt_on_the_upgrade():
    eng, gm, you, _ = town()
    me = eid(gm, "Newcomer")
    sid = gm.inspect("Story")["id"]
    gm.patch(sid, {"freed_by": me, "klhyt_freed": True, "peril_v": None})
    load_world(gm, WORLD, upgrade=True)
    st = story(gm)
    assert st["peril_v"] == 1 and st["peril_step"][me] == "marked" and st["heat"][me] == 8
    assert gm.inspect("the Fist")["state"]["hostile"][me]
    load_world(gm, WORLD, upgrade=True)  # again, without change
    assert story(gm)["heat"][me] == 8
