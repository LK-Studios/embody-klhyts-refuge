# dismiss: let someone in your hire go before their days are up. Nothing is paid back, and their seat goes back to
# the world with the hire.
use("hired")

def check(ctx):
    who = ctx.target
    if (who.state.hired or {}).get("by") != ctx.actor.id:
        return who.name + " is not in your hire"
    return True

def apply(ctx):
    who = ctx.target
    end_hire(ctx, who, ctx.actor.name + " let them go")
    ctx.log(who.name + " is out of your hire; what you paid stays paid")
