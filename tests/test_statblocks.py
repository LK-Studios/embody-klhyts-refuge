"""Classic statblocks (owner, 2026-11-22): the town's people wear SRD statblocks, Deloris and Kael their LoreKeeper
sheets, skills roll the 5e way (ability + proficiency, expertise twice it), and a player may give their own d20."""

from pathlib import Path

import pytest

from embody.cli import load_world
from embody.ops import AUTHOR, Engine

REPO = next(p for p in Path(__file__).resolve().parents if (p / "pyproject.toml").exists())
WORLD = Path(__file__).resolve().parents[1]
# the statblock and 5e skills live in the dnd5e pack from engine/5e-skills-statblocks; an engine before it has neither
pytestmark = pytest.mark.skipif(
    "def statblock(" not in (REPO / "packs" / "dnd5e" / "scripts" / "_five.py").read_text(encoding="utf-8"),
    reason="this engine's dnd5e pack has no statblock or 5e skills yet")


def town():
    eng = Engine(":memory:", workspace=REPO, record=False)
    gm = eng.session("gm", capabilities=[AUTHOR])
    load_world(gm, WORLD)
    you = eng.session("you")
    you.join("klhyts-refuge", "Newcomer")
    return eng, gm, you


def block(gm, name):
    return gm.act_as(name, "stats")["result"]["statblock"]


def has(text, *lines):
    for line in lines:
        assert line in text, line


def test_the_town_wears_classic_srd_statblocks():
    eng, gm, you = town()
    has(block(gm, "Brask"), "Armor Class 11 (leather armor)", "Hit Points 32 (5d8 + 10)", "Skills Intimidation +2",
        "Challenge 1/2 (100 XP)", "Pack Tactics.", "Multiattack. Brask makes two melee attacks.",
        "Cudgel. Melee Weapon Attack: +4 to hit")
    has(block(gm, "Lieutenant Voss"), "Armor Class 18 (plate)", "Hit Points 52 (8d10 + 8)", "Saving Throws Con +4, Wis +2",
        "Challenge 3 (700 XP)", "Brave.", "Leadership", "REACTIONS", "Parry.")
    has(block(gm, "River"), "Skills Deception +5, Insight +4, Investigation +5, Perception +6, Persuasion +5, "
                            "Sleight of Hand +4, Stealth +4", "passive Perception 16", "Sneak Attack.", "Cunning Action.")
    has(block(gm, "Ssark"), "humanoid (lizardfolk)", "Speed 30 ft., swim 30 ft.", "Skills Perception +3, Stealth +4, Survival +5",
        "Bite. Melee Weapon Attack: +4 to hit", "Languages Common, Draconic")
    has(block(gm, "Sister Agathe"), "Skills Medicine +4, Religion +2", "Spellcasting. WIS (spell save DC 12")


def test_deloris_and_kael_from_their_lorekeeper_sheets():
    eng, gm, you = town()
    has(block(gm, "Kael Ironjaw"), "Armor Class 15", "Hit Points 38", "Skills Athletics +5, Intimidation +3, Survival +2",
        "Languages Common, Orc", "Level 4 fighter", "Relentless Endurance.",
        "Glaive. Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 8 (1d10 + 3) slashing damage.")
    has(block(gm, "Deloris"), "Armor Class 16 (studded leather)", "Hit Points 58", "Saving Throws Dex +8",
        "Skills Acrobatics +8, Deception +7, Insight +5, Perception +5, Sleight of Hand +8, Stealth +8",
        "passive Perception 15", "Tools. Thieves' tools, navigator's tools.")


def test_a_newcomer_rolls_skills_the_5e_way_and_may_give_their_own_d20():
    eng, gm, you = town()
    s = you.act("stats")["result"]
    assert s["skills"]["perception"] == 4 and s["passive_perception"] == 14  # WIS 15 (+2), proficiency +2
    has(s["statblock"], "Medium humanoid (human)", "Languages Common", "Level 1 rogue")
    r = you.act("check", params={"skill": "perception", "dc": 15, "roll": 12})["result"]
    assert r["roll"] == 12 and r["total"] == 16 and r["success"]  # the player's own die, the world's modifier
