"""Fat Gog's work (owner, 2026-11-23: "fat gog has nothing to say despite being the main person to go to for stuff and
missions"). Asked for work he offers what the night calls for, as jobs (the engine's jobs pack); the world checks the
work and he pays it from his own purse. His table answers work, pay and guarding before it answers the Custodian."""

from pathlib import Path

from embody.cli import load_world
from embody.ops import AUTHOR, Engine, Rejected

REPO = next(p for p in Path(__file__).resolve().parents if (p / "pyproject.toml").exists())
WORLD = Path(__file__).resolve().parents[1]
DAY = 86400


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


def put(gm, name, place):
    gm.move(eid(gm, name), eid(gm, place))
    gm.patch(eid(gm, name), {"post": eid(gm, place)})


def story(gm):
    return gm.inspect("Story")["state"]


def run(gm, seconds):
    for _ in range(int(seconds // 60)):
        gm.clock(step=60)


def coin(gm, name):
    return sum(int(c["state"].get("count") or 0) for c in gm.world.children(eid(gm, name)) if c["state"].get("kind") == "cp")


def texts(r, kinds=("say", "gestured", "scene")):
    return " ".join(str((e.get("payload") or {}).get("text")) for e in r["events"] if e["kind"] in kinds)


def offered(r):
    return [gm_job for gm_job in [(e.get("payload") or {}).get("job") for e in r["events"] if e["kind"] == "job_offered"]]


def job_names(gm, ids):
    return sorted(gm.world.get(i)["name"] for i in ids)


def paper(gm, clue):
    gm.spawn("letter", eid(gm, "Newcomer"), "Paper (" + clue + ")",
             state={"clue": clue, "portable": True, "bulk": 0, "text": clue})
    return "Paper (" + clue + ")"


def expose(gm, you):
    put(gm, "Newcomer", "The Bonded Warehouse")
    you.act("free", "Klhyt")
    run(gm, 240)
    assert story(gm)["custodian_exposed"]


def test_on_the_first_night_gog_offers_work_and_pays_for_a_lead():
    eng, gm, you = town()
    put(gm, "Newcomer", "The Stripperwitch")
    r = you.act("talk", "Fat Gog", {"about": "got any work for me?"})
    names = job_names(gm, offered(r))
    assert "Where my mayor went" in names and "Keep my books" in names and "Bring him breathing" not in names
    assert "Bring me something I can hold" in texts(r)
    you.act("take_job", params={"job": "Where my mayor went"})
    before = coin(gm, "Newcomer")
    r = you.act("show", "Fat Gog", {"item": paper(gm, "letter")})
    assert story(gm)["gog_knows"]
    assert coin(gm, "Newcomer") == before + 50
    assert any(e["kind"] == "job_paid" for e in gm.history(newest=True, limit=80))
    r = you.act("talk", "Fat Gog", {"about": "any more work?"})
    assert "Bring him breathing" in job_names(gm, offered(r))


def test_bring_him_breathing_pays_whoever_cuts_klhyt_loose():
    eng, gm, you = town()
    put(gm, "Newcomer", "The Stripperwitch")
    gm.patch(gm.inspect("Story")["id"], {"gog_knows": True})
    you.act("talk", "Fat Gog", {"about": "what's the job?"})
    you.act("take_job", params={"job": "Bring him breathing"})
    before = coin(gm, "Newcomer")
    put(gm, "Newcomer", "The Bonded Warehouse")
    you.act("free", "Klhyt")
    run(gm, 60)
    assert coin(gm, "Newcomer") == before + 500


def test_asked_about_pay_and_guarding_gog_answers_that_not_the_custodian():
    eng, gm, you = town()
    expose(gm, you)
    put(gm, "Newcomer", "The Stripperwitch")  # the Fist has marked them: Gog's house is the one door they won't use
    r = you.act("talk", "Fat Gog", {"about": "Are you guarding the mayor tomorrow when he exposes the Custodian? Or is "
                                              "that down to us?"})
    assert "conversation. A long one" not in texts(r) and "small hours" in texts(r)
    r = you.act("talk", "Fat Gog", {"about": "Work, then. If we're protecting Klhyt tomorrow when he names the Custodian, "
                                              "are we getting paid for it? Or is it just out of the kindness of our "
                                              "hearts? Why are we doing this?"})
    assert "conversation. A long one" not in texts(r)
    names = job_names(gm, offered(r))
    assert "Sit up with a witness" in names and "The Fist's dogs" in names
    assert "Where my mayor went" not in names and "Bring him breathing" not in names and "Keep my books" not in names


def test_the_dogs_bounty_pays_for_one_of_the_fist_put_down():
    eng, gm, you = town()
    put(gm, "Newcomer", "The Stripperwitch")
    gm.act_as("Dominico", "set_on", params={"who": "Newcomer"})
    you.act("talk", "Fat Gog", {"about": "any bounty going?"})
    you.act("take_job", params={"job": "The Fist's dogs"})
    before = coin(gm, "Newcomer")
    put(gm, "Ott Fennick", "Harbour Street")
    gm.patch(eid(gm, "Ott Fennick"), {"hp": 1, "ac": 1, "routine_hold_until": 10 ** 9})
    gm.patch(eid(gm, "Newcomer"), {"init_bonus": 50, "scores": {"str": 50, "dex": 50}, "hp": 200, "max_hp": 200})
    put(gm, "Newcomer", "Harbour Street")
    for _ in range(8):  # swing on each of our turns until he drops (a natural 1 misses anything)
        if gm.inspect("Ott Fennick")["state"].get("down"):
            break
        try:
            you.act("attack", "Ott Fennick")
        except Rejected:
            gm.clock(step=6)
    assert gm.inspect("Ott Fennick")["state"].get("down")
    assert coin(gm, "Newcomer") >= before + 200


def test_what_moves_dominico_seen_at_the_apothecary_and_told_to_gog():
    eng, gm, you = town()
    put(gm, "Newcomer", "The Stripperwitch")
    you.act("talk", "Fat Gog", {"about": "is there work?"})
    you.act("take_job", params={"job": "Who pays for Dominico's nerve"})
    gm.patch(eid(gm, "Newcomer"), {"scores": {"int": 50, "wis": 50}})
    put(gm, "Newcomer", "The High Apothecary")
    you.act("check", params={"skill": "arcana"})
    assert me_in(gm, story(gm)["clue_by"]["ring"])
    put(gm, "Newcomer", "The Stripperwitch")
    before = coin(gm, "Newcomer")
    r = you.act("talk", "Fat Gog", {"about": "his candle leans toward the ring he keeps turning"})
    assert story(gm)["iron_known"] and coin(gm, "Newcomer") == before + 500
    assert "think like a heron" in texts(r)


def me_in(gm, ids):
    return eid(gm, "Newcomer") in ids


def test_friends_in_gogs_house_at_the_bell_turn_the_fist_away():
    eng, gm, you = town()
    put(gm, "Newcomer", "The Stripperwitch")
    you.act("talk", "Fat Gog", {"about": "I could use the money"})
    you.act("take_job", params={"job": "Keep my books"})
    before = coin(gm, "Newcomer")
    now = gm.summary()["t"]
    gm.clock(step=(now // DAY + 1) * DAY - now - 30)
    you.say("Quiet in here.")
    run(gm, 120)
    st = story(gm)
    assert st["dominico_backed"] and st["dominico_why"] == "Gog's friends were waiting" and not st.get("guild_hit")
    assert coin(gm, "Newcomer") == before + 300


def test_sitting_up_with_a_witness_pays_and_keeps_them_talking():
    eng, gm, you = town()
    expose(gm, you)
    put(gm, "Newcomer", "The Stripperwitch")
    gm.patch(gm.inspect("Story")["id"], {"clues": list(story(gm)["clues"]) + ["teague"]})
    you.act("talk", "Fat Gog", {"about": "what work have you got"})
    you.act("take_job", params={"job": "Sit up with a witness"})
    before = coin(gm, "Newcomer")
    now = gm.summary()["t"]
    two = (now // DAY + 1) * DAY + 2 * 3600
    gm.clock(step=two - now - 60)
    run(gm, 180)  # the first night: the warrant
    assert eid(gm, "Newcomer") in story(gm)["wanted"]
    gm.clock(step=DAY - 300)
    put(gm, "Harbourmaster Teague", "Harbour Street")  # sitting up with him: his own day would walk him off
    gm.patch(eid(gm, "Harbourmaster Teague"), {"routine_hold_until": 10 ** 9})
    put(gm, "Newcomer", "Harbour Street")
    run(gm, 240)
    st = story(gm)
    assert "teague" not in (st.get("silenced") or []) and coin(gm, "Newcomer") >= before + 30
