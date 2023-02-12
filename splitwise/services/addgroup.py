from models.group import Group

class groupService:
    groupDetails = {}
    def addGroup(self, id, name, members):
        group = Group()
        group.setId(id)
        group.setName(name)
        group.setMembers(members)
        self.__class__.groupDetails[id] = group
        return group