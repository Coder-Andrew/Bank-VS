from account import Account, Checking, Savings
from fileHandler import Account_Handler
from transaction import Transaction
import randTest 

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

'''
#Testing transactions
hank = Savings('HankHill',50000)

hank.add_transaction(Transaction(500))
hank.add_transaction(Transaction(50,'w'))
print(hank.get_balance_after_transactions())

hank.print_transactions()

act_hndlr = Account_Handler()

act_hndlr.make_dir(hank)
act_hndlr.make_account_text(hank)

print(hank.balance)

print(Account.total_money_in_bank)
'''

act_handler = Account_Handler()
for i in range(10):
    rand_choice = randTest.rand_account(randTest.list_user_names)
    if rand_choice[2] == 'checking':
        temp_act = Checking(rand_choice[0],rand_choice[1])
    if rand_choice[2] == 'savings':
        temp_act = Savings(rand_choice[0],rand_choice[1])

    act_handler.make_dir(temp_act)
    act_handler.make_account_text(temp_act)