from classes.checking import Checking
from classes.savings import Savings 
from classes.file_handler import Account_Handler
from classes.bank import Bank
from classes.transaction import Transaction

act_handler = Account_Handler()

usbank = Bank('US Bank')
usbank.add_users(act_handler.import_existing_users())


#test = usbank.users[1]
#test.print_transactions()
#print(act_handler.list_account_file_directories())
#test.print_transactions()
#for i in test.transactions:
    #print(i)

#usbank.print_users()