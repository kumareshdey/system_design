class Bill(object):
    def __init__(self):
        self.__id = None
        self.__groupId = None
        self.__amount = None
        self.__contribution = {}
        self.__paidBy = {}

    def setId(self, id):
        self.__id = id
    
    def getId(self):
        return self.__id

    def setGroupId(self, groupId):
        self.__groupId = groupId
    
    def getGroupId(self):
        return self.__groupId

    def setAmount(self, amount):
        self.__amount = amount
    
    def getAmount(self):
        return self.__amount

    def setContribution(self, contribution):
        self.__contribution = contribution
    
    def getContribution(self):
        return self.__contribution

    def setPaidBy(self, paidBy):
        self.__paidBy = paidBy
    
    def getPaidBy(self):
        return self.__paidBy

