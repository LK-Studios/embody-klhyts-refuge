# The hire's clock, on the root: when the days paid for run out (`hire_ends`, scheduled by hire) or the hireling is
# killed, the hire ends and the seat goes back to the world. A timer from before more days were paid finds the
# hire still running and lets it be.
use("hired")

def on(ctx, event):
    who = ctx.get(event.target)  # the hireling: a hire_ends timer's entity, a killed event's victim
    if who is None or not (who.state.hired or {}).get("by"):
        return
    if event.kind == "hire_ends":
        if float((who.state.hired or {}).get("until") or 0) > ctx.t + 1:
            return
        end_hire(ctx, who, "the days paid for are done")
    elif event.kind == "killed":
        end_hire(ctx, who, "killed")
