class Slot:
    def __init__(self):
        self.slots = []
    
    def setSlot(self, slot):
        slot = slot.split(":")
        start,end = int(slot[0]), int(slot[1])
        self.slots.append([start,end])

    def cancelSlot(self, slot):
        slot = slot.split(":")
        start,end = int(slot[0]), int(slot[1])
        self.slots.remove([start, end])