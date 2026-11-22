FREE_VERBS = ["talk", "check", "sleep", "wake", "yield", "drink"]

def on(ctx, event):
    # a body tied up does nothing with its hands or feet until someone frees it
    me = ctx.get(event.actor) if event.actor else None
    if me is None or not me.state.bound:
        return
    verb = event.payload.get("verb")
    if verb in FREE_VERBS:
        return
    ctx.reject("your hands and feet are tied", "talk, or wait for someone to free you")
