# The Moonmoth takes elves aboard, and anyone an elf has vouched for with a silverleaf token. Everyone else finds the
# gangplank lifting itself an inch out of reach.

def on(ctx, event):
    if event.payload.get("verb") != "go" or event.target != ctx.self.id:
        return
    me = ctx.get(event.actor) if event.actor else None
    if me is None or me.state.people == "elf":
        return
    for it in me.children():
        if it.state.elf_token:
            return
    ctx.reject("the Moonmoth's gangplank lifts itself an inch out of reach as you step onto it: she does not take your kind aboard",
               "an elf in exile can vouch for you: they give a silverleaf token to those they trust")
