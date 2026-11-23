"""Peril (owner, 2026-11-23: "We need more peril!"; asked, "Full 5e, to the death" and "World first, minds after").
What the villains can do, and who fights to kill. The mechanics are scripts/_peril.py and scripts/peril_rule.py.

`brief_more` adds a paragraph to a brief an earlier file wrote (for a mind who may play them later). `dialog_when`
puts a person's topics behind a flag: while it holds, any topic naming one of the words says the line; otherwise what
it said before. PERIL lists who fights to kill (`finishes`, the dnd5e pack's) and the orders a villain holds (a verb of
their own each, by the `order` action: scripts/order.py).
"""

# invented: host: Sabeth Crane carries Dominico's word and delivers his warnings from her little book
# invented: host: Voss's way with a witness is a quiet talk in the small hours, never a blow

CAST = {
    "Dominico": {
        "brief_more": (
            "Your teeth (owner, 2026-11-23: more peril). You push back, always. Whoever threatens you in your own "
            "chair, keeps a paper you asked them for, or frees what you were paid to keep crated is marked: Sabeth puts "
            "the word out, and two of your men find them and kill them. When there is time, a warning from Sabeth comes "
            "first. Your own verbs: set_on (who: their name) marks someone and sends your men; call_off (who) ends it. "
            "Use them the way you would: rarely, coldly, never on a whim, and never inside the Stripperwitch, which "
            "would be war with Gog before you are ready for it. Gifts to your people buy back a little standing; a lot of "
            "them, or your word, buys it all."),
    },
    "Sabeth Crane": {
        "brief_more": (
            "You carry Dominico's word. You deliver his warnings yourself, from your little book, politely, in "
            "public. When he has given the word, set_on (who: their name) sends the men; call_off (who) when he says so. "
            "You never act on your own account, and you never set foot in the Stripperwitch on business."),
    },
    "The Custodian": {
        "brief_more": (
            "Your teeth: the Throne's warrant. warrant (who: their name) posts a notice on the square and sets "
            "Lieutenant Voss and Constable Quint on them, on sight, and they fight to kill; pardon (who) lifts it. Every "
            "night until the magistrate lands you work on the witnesses the town has found against you: Voss calls on "
            "them in the small hours, and a witness he finds alone will not speak to the magistrate. You do not go into "
            "the Stripperwitch, and you do not send anyone there."),
    },
    "Harbourmaster Teague": {
        "dialog_when": [{
            "if_state": {"silenced": True},
            "words": ["crate", "warehouse", "bonded", "log", "logged", "klhyt", "mayor", "custodian", "dues", "tally",
                      "ledger", "magistrate", "magistrates", "hearing", "brask", "dominico"],
            "line": "Teague's pencil stops. \"I count boats,\" he says, too quickly. \"I never logged any crate, and I "
                    "never saw anything, and I will say so to anybody in any coat.\" His hands will not keep still on "
                    "the tally board.",
        }],
    },
    "Tully": {
        "dialog_when": [{
            "if_state": {"silenced": True},
            "words": ["brask", "warehouse", "crate", "job", "custodian", "grey", "magistrate", "news", "heard"],
            "line": "Tully has gone white under the red. \"Never said nothing about any crate. Never. A gentleman in a "
                    "blue coat explained it to me, very kindly, in the small hours.\" He drinks, and does not offer you one.",
        }],
    },
}

PERIL = {
    # fight to kill: on their turn, with no foe standing, they finish one who is down (owner: "Full 5e, to the death")
    "finishes": ["Dominico", "Brask", "Tully", "Sabeth Crane", "Ott Fennick", "Jory Fennick", "Lieutenant Voss"],
    "orders": {
        "Dominico": {
            "set_on": {"doc": "Set the Fist on someone: they are marked, and your men find them and kill them (who: their name)"},
            "call_off": {"doc": "Call the Fist off someone you marked (who: their name)"},
        },
        "Sabeth Crane": {
            "set_on": {"doc": "Put Dominico's word out on someone: the men find them and kill them (who: their name)"},
            "call_off": {"doc": "Take Dominico's word back off someone (who: their name)"},
        },
        "The Custodian": {
            "warrant": {"doc": "Post the Throne's warrant on someone: a notice on the square, and Voss and the constable "
                               "attack them on sight (who: their name)"},
            "pardon": {"doc": "Lift the Throne's warrant from someone (who: their name)"},
        },
    },
}
