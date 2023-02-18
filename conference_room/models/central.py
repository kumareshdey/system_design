class Controller:
    def __init__(self):
        self.buildings = []

    def setController(self, building):
        self.buildings.append(building)

    def getBuilding(self, building):
        for bld in self.buildings:
            if building == bld.name:
                return bld
        return None