def check(ctx):
    me = ctx.actor
    food = ctx.target
    if food.parent.id != me.id and food.parent.id != me.parent.id:
        return "it is not within reach"
    return True

def apply(ctx):
    food = ctx.target
    me = ctx.actor
    line = food.state.eaten_line or (me.name + " eats " + str(food.name).lower() + ".")
    ctx.emit("ate", target=me, reach=1, by=me.id, name=food.name)
    ctx.emit("scene", target=me.parent, reach=1, text=line)
    ctx.destroy(food)
    ctx.log("you eat the " + str(food.name).lower())
