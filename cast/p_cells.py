# The cells under the Town Hall, as the watch talk about them (the owner, 2026-11-23: "Surrender should mean surrender.
# And you are taken to prison."; "We gonna need rules to break someone out of prison"). The mechanics are in
# scripts/_custody.py: six world hours, or five gold bail to Sergeant Harrow; Rosa Quint carries the one key to the
# bar's padlock and takes small bribes, and two gold buys it and a quarter of an hour of her not looking.
#
# Merged over the earlier files by build.load_cast: each topic here JOINS the person's table. No new topic shares an
# alias with any topic the person already has (Rosa and Harrow already answer "bribe"; Harrow already answers "keys").

CAST = {
    "Constable Rosa Quint": {"dialog": {
        "cell|cells|jail|gaol|prison|prisoner|prisoners|lockup|key|padlock|bar|spring|break":
            "She pats a pocket, where something heavy and iron hangs on a string. \"Only key to the cells, love, and the "
            "sergeant trusts me with it, bless him.\" She takes a slow bite of mango. \"Between you and me, if a body "
            "had a friend down there, and that friend had a friend with two gold, I might fancy a walk to the market. "
            "Quarter of an hour. Lot can happen in a quarter of an hour that I never saw.\"",
        "bail|fine|sentence":
            "\"Six hours, or five gold bail. Bail goes to the sergeant, all proper, written in his book.\" She shrugs. "
            "\"I'm the other kind of arrangement.\"",
    }},
    "Sergeant Pell Harrow": {"dialog": {
        "cell|cells|jail|gaol|prison|prisoner|prisoners|lockup|bail|fine|sentence":
            "\"Two cells under the Hall, and they're for the Throne's lot mostly, these days.\" He licks his pencil. "
            "\"Six hours, and out you go with your knife back. Or five gold bail, to me, in the book, and out you go "
            "sooner. I'll not have it said this watch can't be paid honestly.\"",
        "escape|escaped|break|spring|padlock|bar":
            "\"Somebody's always got a crowbar and an idea.\" He does not look up from his book. \"Break my bar and you're "
            "on the Throne's paper by morning, son, and so's whoever you let out. And I fit a new bar. I've a cellar full "
            "of bars.\"",
    }},
    "Constable Abel Fitch": {"dialog": {
        "cell|cells|jail|gaol|prison|prisoner|prisoners|lockup|bail|escape|break|key|padlock|bar":
            "\"The cells are for keeping people until they're let out, sir!\" He considers this. \"Six hours, unless "
            "somebody pays the sergeant five gold, which is called bail, which is legal. Breaking them out is not legal. "
            "I'd stop you.\" He grips his spear. \"Rosa has the key,\" he adds helpfully, \"so it would be very hard.\"",
    }},
    "Lieutenant Voss": {"dialog": {
        "cell|cells|jail|gaol|prison|prisoner|prisoners|lockup|surrender|yield|bail|escape":
            "\"Surrender is accepted, in the Throne's name, by me or by the watch. The cells, six hours, the papers to "
            "the Throne.\" He folds his gloves. \"Those who leave by another door are posted on the square by dawn. I "
            "have never yet found the town short of people who can read a notice and use a sword.\"",
    }},
}
