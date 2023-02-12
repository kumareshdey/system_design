class Group(object):
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__members = []

    def setId(self, id):
        self.__id = id
    
    def getId(self):
        return self.__id

    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name

    def setMembers(self, members):
        self.__members = members
    
    def getMembers(self):
        return self.__members