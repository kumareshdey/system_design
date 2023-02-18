class Floor:
    def __init__(self):
        self.floorNo = None
        self.confRooms = []

    def setFloorNo(self, floorNo):
        self.floorNo = floorNo

    def addConfRoom(self, confRoom):
        self.confRooms.append(confRoom)

    def getRoom(self,confRoom):
        for rm in self.confRooms:
            if confRoom == rm.roomNo:
                return rm
        return None

