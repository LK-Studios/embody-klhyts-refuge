"""The Xotons as canon has them (owner, 2026-11-24: dark-skinned, almost as wide as they are tall, barrel-chested
warriors of the sea, Merchant Navy, Military Navy or rarely pirates, each ship its own tribe): every Xoton in town looks
it, carries a name from LoreKeeper's Xoton naming doc, and has the canon's speed and tongues; the Navy's frigate is at
the pier with her captain and two marines; a town built before all this is renamed in place, once."""

import hashlib
import json
from pathlib import Path

from embody.cli import load_world
from embody.ops import AUTHOR, Engine

REPO = next(p for p in Path(__file__).resolve().parents if (p / "pyproject.toml").exists())
WORLD = Path(__file__).resolve().parents[1]
OLD = {"Dayo Oceanheart": "Torvald Brineknot", "Imani Wavebreaker": "Ragna Seaward", "Kwasi Foamtooth": "Bjarke Foamtooth",
       "Little Jabali": "Little Olaf", "Amara Ironwake": "Hulda Ironwake", "Khamisi Saltbeard": "Hallvard Saltbeard",
       "Zuri Coralhand": "Brynja Coralhand"}
NAVY = ["Captain Zuberi Seawarden", "Kesi Reefstrider", "Obasi Tidewalker"]


def town():
    eng = Engine(":memory:", workspace=REPO, record=False)
    gm = eng.session("gm", capabilities=[AUTHOR])
    load_world(gm, WORLD)
    g = gm.invite("player", entity="Newcomer", label="p")
    you = eng.session_for_token(g["token"])
    you.join()
    return eng, gm, you


def by_name(gm):
    out = {}
    for e in gm.world.find(limit=None):
        out.setdefault(e["name"], []).append(e)
    return out


def eid(gm, name):
    return by_name(gm)[name][0]["id"]


def place(gm, name):
    return gm.world.get(gm.world.get(eid(gm, name))["parent_id"])["name"]


def words(r):
    return " ".join(str(e["payload"].get("text") or "") for e in r["events"] if e["kind"] in ("say", "gestured", "scene"))


def meet(gm, who, where):
    gm.patch(eid(gm, who), {"routine_hold_until": 10 ** 9})
    gm.move(eid(gm, who), eid(gm, where))
    gm.move(eid(gm, "Newcomer"), eid(gm, where))


def digest(world):
    rows = sorted((e["id"], e["type"], e["name"], json.dumps(e["state"], sort_keys=True, default=str))
                  for e in world.find(limit=None))
    return hashlib.sha256(json.dumps(rows).encode()).hexdigest()[:12]


def test_every_xoton_is_dark_broad_and_named_as_canon_names_them():
    eng, gm, you = town()
    have = by_name(gm)
    xotons = [e for e in gm.world.find(limit=None) if e["state"].get("people") == "xoton" and e["type"] == "person"]
    assert {e["name"] for e in xotons} >= set(OLD) | set(NAVY) | {"Captain Eirik", "Marlo"}
    assert not set(OLD.values()) & set(have)
    for e in xotons:
        look = e["state"]["description"].lower()
        assert any(w in look for w in ("black", "brown", "dark")), e["name"]
        assert any(w in look for w in ("wide", "broad", "barrel")), e["name"]
        sb = e["state"]["statblock"]
        assert sb["speed"] == "25 ft., swim 25 ft." and sb["languages"][:3] == ["Common", "Dwarvish", "Siren"], e["name"]
    # the Navy's frigate at the pier, her captain and marines on the docks, armed as canon arms them
    assert place(gm, "Keepers of the Storm") == "The Docks" and "Timber Acquisition" in gm.inspect("Keepers of the Storm")["state"]["description"]
    for name in NAVY:
        assert len(have[name]) == 1 and place(gm, name) == "The Docks"
    kit = {c["name"]: c["state"] for c in gm.world.children(eid(gm, "Kesi Reefstrider"))}
    assert kit["Harpoon crossbow"]["dice"] == "1d10" and kit["Harpoon bolts"]["ammo"] == "bolt"
    assert "Ironwake" in gm.inspect("Whispers of the Deep")["state"]["description"]
    assert any("no House mark" in r for r in gm.inspect("Dockside crowd")["state"]["rumours"])
    # each ship its own word on the other
    meet(gm, "Captain Eirik", "The Turtle Dragon")
    assert "Keepers of the Storm" in words(you.act("talk", "Captain Eirik", {"about": "the navy"}))
    meet(gm, "Captain Zuberi Seawarden", "The Turtle Dragon")
    assert "no House mark" in words(you.act("talk", "Captain Zuberi Seawarden", {"about": "pirates"}))
    # a passer-by hailed out of the docks' crowd is a Xoton with a canon name
    gm.patch(eid(gm, "Dockside crowd"), {"mix": None})
    gm.patch(eid(gm, "Dockside crowd"), {"mix": {"xoton": 1}})
    gm.move(eid(gm, "Newcomer"), eid(gm, "The Docks"))
    face = you.act("hail", "Dockside crowd")["result"]
    assert face["people"] == "xoton" and face["name"] in {"Kofi Stormbringer", "Nia Tidesinger", "Obi Tidehunter", "Sade Wavewhisper",
                                        "Chike Driftwood", "Ayana Starfinder", "Juma Seastrider", "Mirembe Oceanseer",
                                        "Femi Stormwarden", "Zola Tideshaper", "Taye Deepwave", "Adia Moonrider"}


def test_a_town_from_before_renames_its_xotons_in_place_once():
    eng, gm, you = town()
    w = gm.world
    # the town as it was: the old names, an old passer-by, the old Whispers, no Navy, the old tongue
    ids = {}
    for new, old in OLD.items():
        ids[old] = eid(gm, new)
        gm.rename(ids[old], old)
    face = gm.spawn("person", eid(gm, "The Docks"), "Hallgrim Ropewise", state={
        "people": "xoton", "passer_by": True, "description": "A broad Xoton deckhand, black skin shining with sweat, a ship's cook.",
        "dialog": {"name|who|you": "\"Hallgrim Ropewise. A ship's cook.\""},
        "default_line": "\"Hallgrim Ropewise. A ship's cook. Ask me about my work, the mayor, or the news.\""})["id"]
    # a player's own Xoton, made from the template with their own look (the owner's Kalypso)
    b = __import__("importlib").util.spec_from_file_location("refuge_build", WORLD / "build.py")
    build = __import__("importlib").util.module_from_spec(b)
    b.loader.exec_module(build)
    was, now = build.PLAYER_XOTONS["Kalypso"]
    kalypso = gm.spawn("person", eid(gm, "Market Square"), "Kalypso", state={
        "people": "xoton", "description": was, "stays": True,
        "statblock": {"kind": "humanoid (xoton)", "languages": ["Common", "Xoton"], "senses": [], "size": "Medium",
                      "speed": "30 ft."}})["id"]
    for name in NAVY + ["Keepers of the Storm"]:
        gm.destroy(eid(gm, name))
    town_id = eid(gm, "Klhyts Refuge")
    st = gm.inspect(town_id)["state"]
    gm.patch(town_id, {"built_people": sorted({OLD.get(n, n) for n in st["built_people"]} - set(NAVY)),
                       "built_things": sorted(t for t in st["built_things"] if "Keepers of the Storm" not in t)})
    gm.patch(eid(gm, "Whispers of the Deep"), {"description": "A deep-keeled Xoton cog unloading by lantern-light."})
    amara = ids["Hulda Ironwake"]
    gm.patch(amara, {"statblock": {**gm.inspect("Hulda Ironwake")["state"]["statblock"], "speed": "30 ft.",
                                   "languages": ["Common", "Xoton"]}})

    load_world(gm, WORLD, upgrade=True)
    have = by_name(gm)
    for new, old in OLD.items():
        assert old not in have and [e["id"] for e in have[new]] == [ids[old]], new
    assert w.get(face)["name"] == "Kofi Stormbringer"
    assert w.get(face)["state"]["dialog"]["name|who|you"].startswith("\"Kofi Stormbringer.")
    assert set(OLD) <= set(gm.inspect(town_id)["state"]["built_people"])
    assert all(len(have[n]) == 1 for n in NAVY) and len(have["Keepers of the Storm"]) == 1
    assert "Ironwake" in gm.inspect("Whispers of the Deep")["state"]["description"]
    sb = w.get(amara)["state"]["statblock"]
    assert sb["speed"] == "25 ft., swim 25 ft." and sb["languages"] == ["Common", "Dwarvish", "Siren"]
    assert "black-skinned" in w.get(amara)["state"]["description"]
    k = w.get(kalypso)["state"]
    assert k["description"] == now and "deep brown" in now and "bare chin" in now
    assert k["statblock"]["speed"] == "25 ft., swim 25 ft." and k["statblock"]["languages"] == ["Common", "Dwarvish", "Siren"]
    gm.patch(kalypso, {"description": "Kalypso, as the player has since written them."})
    before = digest(w)
    load_world(gm, WORLD, upgrade=True)
    assert digest(w) == before
    assert w.get(kalypso)["state"]["description"] == "Kalypso, as the player has since written them."
