class User(object):
    def __init__(self):
        self.__id = None
        self.__name = None

    def setId(self, id):
        self.__id = id
    
    def getId(self):
        return self.__id

    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name