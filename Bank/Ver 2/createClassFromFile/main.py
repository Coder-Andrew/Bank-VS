from account import Account, Checking, Savings
from fileHandler import Account_Handler
from transaction import Transaction

'''
#Testing file handling class
file_name = 'Checking.txt'

hank = Account_Handler()
hank.directory += 'user1'
info = hank.input_from_file('checking.txt')

print(info)


try:
    hank_act = Checking(info[0],info[1])

except ValueError as excpt:
    print(excpt, 'attempted to create class with wrong type')


print(hank.user_list())

'''


#Testing transactions
hank = Savings('HankHill',50000)

hank.add_transaction(Transaction(500))
hank.add_transaction(Transaction(50,'w'))
print(hank.get_balance_after_transactions())

hank.print_transactions()