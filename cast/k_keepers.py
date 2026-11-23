"""The tavern keepers' days (owner, 2026-11-23: "The touchy unicorn seems to have lost its owner bar keep").
Each keeper is behind their own bar from evening to closing; their errands (the pond, the Town Hall, the
catch, the pump, the limes) moved to the early morning, when the taverns are shut. Written by a script from
the earlier days; the slots that stay home are as they were."""

# invented: host: the keepers' morning errands and the new morning and evening slots

CAST = {
    "Wendeline Moss": {
        "routine": [
            {
                "at": 0.0,
                "place": "unicorn",
                "doing": "She walks the library's shelves with a shaded candle, straightening spines and checking who is asleep in which chair."
            },
            {
                "at": 2.0,
                "place": "unicorn",
                "doing": "She sits up at the front desk with a lamp and a book she is not reading, facing the door, the register shut under her hand.",
                "beats": [
                    "When the man in the pressed uniform comes in, the woman with spectacles says \"Shh\" before he can speak, and keeps saying it until he sits down.",
                    "The woman with spectacles on a chain tears a page from the register without a sound, folds it small and holds it over the lamp until it is gone."
                ]
            },
            {
                "at": 3.5,
                "place": "unicorn",
                "doing": "She sleeps in a little room behind the desk with the door ajar and her spectacles folded on the register."
            },
            {
                "at": 6.0,
                "place": "square",
                "doing": "She buys ink and candles off the morning carts in the square and reads the notice board with visible disapproval of its spelling."
            },
            {
                "at": 6.5,
                "place": "hall",
                "doing": "She hands a folded letter to the Town Hall's clerk, the twelfth about the pond, and waits to see it put on the pile.",
                "go": "The woman with spectacles takes a folded letter from her sleeve, checks the address, and walks into town."
            },
            {
                "at": 7.0,
                "place": "treeline",
                "doing": "She stands by the pond off the Treeline Road with a jar, counting the bugs that fly into it and writing the number down."
            },
            {
                "at": 8.0,
                "place": "unicorn",
                "doing": "She opens the shutters of the Touchy Unicorn's library and dusts the spines, one shelf a morning, in an order only she understands."
            },
            {
                "at": 12.0,
                "place": "unicorn",
                "doing": "She sleeps through the heat behind the desk, a book open face down on her chest."
            },
            {
                "at": 17.0,
                "place": "unicorn",
                "doing": "She lights the reading lamps one by one, sets out the evening's quiet like a table, and takes her place at the front desk."
            },
            {
                "at": 18.5,
                "place": "unicorn",
                "doing": "She lights the reading lamps one by one and unlocks the study rooms, saying shh to the first guest of the evening on principle."
            },
            {
                "at": 21.0,
                "place": "unicorn",
                "doing": "She keeps the front desk of the Touchy Unicorn, spectacles on their chain, saying shh to anyone who breathes too loudly."
            }
        ]
    },
    "Bosun Maggs": {
        "routine": [
            {
                "at": 0.5,
                "place": "turtle",
                "doing": "She keeps the passage book open on the bar, taking names and coin for berths on anything that floats out on the tide, and pours with her other hand."
            },
            {
                "at": 1.25,
                "place": "turtle",
                "doing": "She calls the last hard hour behind the bar, throwing out the drunk and the sorry with equal care.",
                "go": "The one-eyed woman snaps the passage book shut, nods to the harbourmaster and walks back up to the Turtle Dragon."
            },
            {
                "at": 3.0,
                "place": "turtle",
                "doing": "She sleeps in the back room behind the bar, the door open and a bung-starter in reach."
            },
            {
                "at": 6.0,
                "place": "docks",
                "doing": "She haggles with the fishermen on the pier for the morning's catch, prodding every fish with one finger.",
                "pay": {
                    "to": "Ssark",
                    "cp": 6,
                    "for": "the morning's catch"
                }
            },
            {
                "at": 7.0,
                "place": "turtle",
                "doing": "She hangs the morning's catch on the hooks behind the bar and shucks oysters into a bucket faster than you can count them."
            },
            {
                "at": 8.0,
                "place": "turtle",
                "doing": "She scrubs the Turtle Dragon's floor in the morning cool, singing a whaling song very badly."
            },
            {
                "at": 12.5,
                "place": "turtle",
                "doing": "She sleeps out the heat in the back room, shutters closed."
            },
            {
                "at": 17.0,
                "place": "turtle",
                "doing": "She opens up the Turtle Dragon, lighting lanterns among the nets and floats, and scaring the pot-boy awake."
            },
            {
                "at": 21.0,
                "place": "turtle",
                "doing": "She runs the bar like a deck in weather, a mug in each hand, one eye on the whole room."
            },
            {
                "at": 23.5,
                "place": "turtle",
                "doing": "She counts twenty copper into a grey-coated woman's palm with her jaw set, then chalks something on the underside of the bar.",
                "pay": {
                    "to": "Sabeth Crane",
                    "cp": 20,
                    "for": "peace money"
                }
            }
        ]
    },
    "Big Ludo": {
        "routine": [
            {
                "at": 0.5,
                "place": "ogre",
                "doing": "He leans on the bar over a table of Dominico's off-duty men, pouring their rum slow and weak, listening with his eyes half shut.",
                "pay": {
                    "to": "Wick",
                    "cp": 1,
                    "for": "carrying a word to the Stripperwitch"
                },
                "beats": [
                    "The barman with the broken tusk pours a round for Dominico's men from a bottle he keeps under the bar, a little water in each, and laughs at their joke a moment late.",
                    "The huge barman bends and murmurs something to a ragged child at the back door, presses a copper into the small hand, and the child is gone."
                ]
            },
            {
                "at": 2.5,
                "place": "ogre",
                "doing": "He sweeps sawdust and spilled rum into the gutter, then throws the last drinker out after it, gently."
            },
            {
                "at": 3.5,
                "place": "ogre",
                "doing": "He sleeps on a pallet behind the bar, one hand on his cudgel, snoring like a stuck door."
            },
            {
                "at": 6.0,
                "place": "docks",
                "doing": "He rolls rum barrels up off a Xoton boat two at a time, one under each arm, saying nothing to anyone."
            },
            {
                "at": 7.0,
                "place": "ogre",
                "doing": "He rakes the night's sawdust out of the door in one long heap and throws down fresh, slowly, as if it were a sacrament."
            },
            {
                "at": 11.5,
                "place": "ogre",
                "doing": "He sleeps out the heat behind the bar, the shutters down."
            },
            {
                "at": 18.0,
                "place": "ogre",
                "doing": "He opens the Ogre's door, kicks fresh sawdust over yesterday's, and sets the dice cup on the corner table."
            },
            {
                "at": 21.0,
                "place": "ogre",
                "doing": "He stands behind a bar made of a ship's door, pouring, watching the dice game, saying almost nothing."
            },
            {
                "at": 23.0,
                "place": "ogre",
                "doing": "He counts twenty copper onto the bar for a grey-coated woman without a word, then wipes the bar where the coins were.",
                "pay": {
                    "to": "Sabeth Crane",
                    "cp": 20,
                    "for": "peace money"
                }
            }
        ]
    },
    "Sister Agathe": {
        "routine": [
            {
                "at": 0.0,
                "place": "omberhulk",
                "doing": "She stands at the bar with her arms folded while the midnight bell rings, counting coins into a grey-coated woman's palm as if each one were a tooth.",
                "pay": {
                    "to": "Sabeth Crane",
                    "cp": 20,
                    "for": "peace money, with bad grace"
                },
                "beats": [
                    "The big woman in the wimple counts twenty copper into a stranger's palm, then says a prayer over the hand, very quietly, that makes the stranger snatch it away.",
                    "The woman in the wimple says something loud by the stairs about Fat Gog hiring thirty Xotons for midnight. One of the two men by the stairs writes it down. She winks at the kitchen."
                ]
            },
            {
                "at": 0.5,
                "place": "omberhulk",
                "doing": "She works the room with a jug in one hand and the bung-starter in the other, stitching a sailor's eyebrow between pours."
            },
            {
                "at": 2.5,
                "place": "omberhulk",
                "doing": "She throws the last drinkers out into the square one by one, blessing each of them on the way out the door."
            },
            {
                "at": 3.5,
                "place": "omberhulk",
                "doing": "She sleeps in a chair by the kitchen door, the bung-starter across her knees, the back room's door open a crack."
            },
            {
                "at": 6.0,
                "place": "square",
                "doing": "She fills two buckets at the town pump and carries them back without spilling, nodding to everyone and stopping for no one."
            },
            {
                "at": 6.5,
                "place": "omberhulk",
                "doing": "She sets a cauldron of porridge on the fire and stirs it with an oar, counting the night's casualties on the benches."
            },
            {
                "at": 8.0,
                "place": "omberhulk",
                "doing": "She scrubs tables and peels a mountain of spuds, telling Beatrice from Susan by touch."
            },
            {
                "at": 12.5,
                "place": "omberhulk",
                "doing": "She sleeps through the heat upstairs, shutters closed, a wet cloth over her eyes."
            },
            {
                "at": 18.5,
                "place": "omberhulk",
                "doing": "She lights the lamps and the cookfires, and sets the spuds on to boil in a pot the size of a font."
            },
            {
                "at": 21.0,
                "place": "omberhulk",
                "doing": "She runs the Omberhulk like an infirmary in a riot, a jug in one hand and the bung-starter on her belt."
            }
        ]
    },
    "Master Quillon": {
        "routine": [
            {
                "at": 0.0,
                "place": "apothecary",
                "doing": "He stands at the door to the lemon bath with a list of names, admitting guests one at a time as the midnight bell goes.",
                "beats": [
                    "The silver-haired steward consults his list, admits a guest to the lemon bath, and adds a line to a different list in a smaller book."
                ]
            },
            {
                "at": 2.0,
                "place": "apothecary",
                "doing": "He polishes glasses at the far end of the room with his back very precisely turned to the window table, where coins are being counted out.",
                "beats": [
                    "The steward in grey gloves polishes the same glass for a long while, his back turned to the window table where a man in a black coat counts silver into rough hands."
                ]
            },
            {
                "at": 3.0,
                "place": "apothecary",
                "doing": "He sits in his pantry with the night's takings in neat stacks, writing the Custodian's account in a beautiful hand."
            },
            {
                "at": 4.0,
                "place": "apothecary",
                "doing": "He sleeps in a narrow room off the pantry, his gloves folded on the chair beside the bed."
            },
            {
                "at": 6.0,
                "place": "hall",
                "doing": "He presents the house's account to the Custodian's clerk in the Town Hall, waiting with his gloved hands folded while it is signed unread."
            },
            {
                "at": 6.5,
                "place": "market",
                "doing": "He chooses limes for the lemon bath at a fruit stall in the Night Market, one at a time, holding each to his nose.",
                "go": "The silver-haired steward collects a signed paper, folds it into his coat, and walks downhill toward the market.",
                "pay": {
                    "to": "Mother Ines",
                    "cp": 5,
                    "for": "limes and lemons for the bath"
                }
            },
            {
                "at": 7.25,
                "place": "apothecary",
                "doing": "He inspects the morning's linen sheet by sheet against the window light, and sends two back."
            },
            {
                "at": 10.0,
                "place": "apothecary",
                "doing": "He inspects the linen sheet by sheet, holding each to the window light and finding fault with most of them."
            },
            {
                "at": 13.0,
                "place": "apothecary",
                "doing": "He rests through the heat in his narrow room, shutters drawn, a cold cloth folded exactly over his eyes."
            },
            {
                "at": 17.5,
                "place": "apothecary",
                "doing": "He stands at the foot of the grand staircase receiving the evening's guests, gloves white, voice low, every name already known to him."
            },
            {
                "at": 21.0,
                "place": "apothecary",
                "doing": "He stands at the top of the grand staircase in grey gloves, receiving guests with a look that weighs their purses."
            }
        ]
    }
}
