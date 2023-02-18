from models.buildings import Building
from models.central import Controller

def buildingSet(c, i):
    if c.getBuilding(i):
        print('Building found')
        building = c.getBuilding(i)
    else:
        print('Adding new building')
        building = Building()
        building.setName(i)
        c.setController(building)
    return i