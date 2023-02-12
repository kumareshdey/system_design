from services.addUser import userService
from services.bill_service import BillService
from services.addgroup import groupService


user = userService()
group = groupService()
bill = BillService()

user1 = user.addUser(id=1, name='kumaresh')
user2 = user.addUser(id=2, name='sangita')

group1 = group.addGroup(id='group1',name='group1', members=[user1,user2])

paidBy = {1: 100}
contribution = {1:50, 2: 50}

billing = bill.addBill('billing1', 'group1', contribution, paidBy )
billing = bill.addBill('billing2', 'group1', contribution, paidBy )

print(bill.getUserBalance(1))
print(bill.getUserBalance(2))