# A passed check always answers. A place's `finds` table, {"perception|investigation": {"dc": 12, "line": ...,
# "fail": ..., "clue": ...}}, is read against the roll's total (the world's difficulty, never the caller's). A skill
# the place has nothing for gets an honest "nothing here for that". Only the one who rolled hears the answer.

def matches(key, skill):
    s = str(skill or "").lower()
    for alias in key.split("|"):
        if alias.strip() and alias.strip() in s:
            return True
    return False

def on(ctx, event):
    p = event.payload or {}
    who = ctx.get(p.get("by"))
    place = ctx.get(p.get("place")) if p.get("place") else (who.parent if who else None)
    if who is None or place is None:
        return
    finds = place.state.finds
    if not finds:
        return
    total = int(p.get("total") or 0)
    for key, entry in finds.items():
        if not matches(key, p.get("skill")):
            continue
        if total >= int(entry.get("dc", 12)):
            ctx.emit("scene", target=who, reach=0, text=entry.get("line"))
            if entry.get("clue"):
                st = ctx.find(type="story", limit=1)
                if st:
                    have = list(st[0].state.clues or [])
                    if entry.get("clue") not in have:
                        have.append(entry.get("clue"))
                        ctx.patch(st[0], {"clues": have})
        else:
            ctx.emit("scene", target=who, reach=0, text=entry.get("fail") or "You look, and come up with nothing you can use.")
        return
    ctx.emit("scene", target=who, reach=0, text="Nothing here answers to " + str(p.get("skill") or "that") + ". " +
             (place.state.finds_hint or "Try your eyes or your wits on it instead."))
