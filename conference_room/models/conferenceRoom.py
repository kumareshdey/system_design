class ConfRoom:
    def __init__(self):
        self.roomNo = None
        self.slots = []

    def setRoomNo(self, roomNo):
        self.roomNo = roomNo

    def setSlot(self, slot):
        slot = slot.split("-")
        start,end = int(slot[0]), int(slot[1])
        self.slots.append([start,end])

    def cancelSlot(self, slot):
        slot = slot.split("-")
        start,end = int(slot[0]), int(slot[1])
        self.slots.remove([start, end])

    def getSlots(self):
        return self.slots

        