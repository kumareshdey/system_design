from models.buildings import Building
from models.floor import Floor
from models.conferenceRoom import ConfRoom
from models.central import Controller
from service.slotHandler import checkSlotAvailibility
# while(True):  
#     inp = input('Provide details like building name/floor/room. type exit when done. \n')
#     if inp =='exit':
#         break
#     building,floor,room = inp.split('/')
#     b = Building()
#     f = Floor()
#     r = ConfRoom()
#     b.setBuildingDetails(building, building)
#     f.setFloor(floor, b)
#     r.setConfRoom(room, f)

def display():
    for buildings in c.buildings:
        for floors in buildings.floors:
            for rooms in floors.confRooms:
                print(f"building: {buildings.name}, floor: {floors.floorNo}, room: {rooms.roomNo}, slot: {rooms.getSlots()}")

c = Controller()
def inputs():
    # i = input('Enter building name\n')
    # f = input('Enter Floor\n')
    # r = input('Enter room\n')
    # s = input('Enter slot\n')
    i, f, r, s = input('give inputs in this manner building/floor/room/slot(eg:start-end): \n').split('/')
    #building
    if c.getBuilding(i):
        print('Building found')
        building = c.getBuilding(i)
    else:
        print('Adding new building')
        building = Building()
        building.setName(i)
        c.setController(building)
    #floor
    if building.getFLoor(f):
        print('Floor found')
        floor = building.getFLoor(f)
    else:
        print('Adding new floor')
        floor = Floor()
        floor.setFloorNo(f)
        building.addFloor(floor)
    #room
    if floor.getRoom(r):
        print('Room found')
        room = floor.getRoom(r)
    else:
        print('Adding new room')
        room = ConfRoom()
        room.setRoomNo(r)
        floor.addConfRoom(room)
    #slot
    occupied_slots = room.getSlots()
    if checkSlotAvailibility(occupied_slots, s):
        room.setSlot(s)
        print(f'Your slot has been set {s}')
    else:
        print(f'Slot is occupied please choose another slots except {occupied_slots}')

    decission = input('1. delete slot, 2. Give another input, 3. exit, 4. view db\n')
    if decission == '3':
        return
    if decission == '1':
        can = input(f'which slot to cancel between {occupied_slots}')
        room.cancelSlot(can)
        print(f'SLot cancelled, available slots are {room.getSlots()}')
    if decission =='2':
        inputs()
    if decission =='4':
        display()
        inputs()
inputs()
# Building().setBuildingDetails(i,None)
# c.setController(b)

