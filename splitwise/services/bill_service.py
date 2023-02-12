from models.bill import Bill

class BillService:
    billDetails = {}
    def addBill(self, id, groupId, contribution, paidBy):
        if sum(contribution.values()) == sum(paidBy.values()):
            amount = sum(contribution.values())  
        else:
            raise ValueError("contribution and paidby sum does not match")
        bill = Bill()
        bill.setId(id)
        bill.setGroupId(groupId)
        bill.setAmount(amount)
        bill.setContribution(contribution)
        bill.setPaidBy(paidBy)
        self.__class__.billDetails[id] = bill
        return bill

    def getUserBalance(self, userId):
        balance = 0
        for billId in self.__class__.billDetails:
            bil = self.__class__.billDetails.get(billId)
            if userId in bil.getContribution():
                balance = balance - bil.getContribution().get(userId)
            if userId in bil.getPaidBy():
                balance = balance + bil.getPaidBy().get(userId)
        return balance