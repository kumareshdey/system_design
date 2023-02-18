class Building:
    def __init__(self):
        self.name = None
        self.floors = []

    def setName(self, name):
        self.name = name
        
    def addFloor(self,floor):
        self.floors.append(floor)

    def getFLoor(self,floor):
        for flr in self.floors:
            if floor == flr.floorNo:
                return flr
        return None