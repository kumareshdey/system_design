
def checkSlotAvailibility(slots, slotToAssign):
    slotToAssign = [int(s) for s in slotToAssign.split("-")]
    if not slots:
        return True
    for slot in slots:
        if slot[1] < slotToAssign[0] or slotToAssign[1] < slot[0]:
            return True
    return False

