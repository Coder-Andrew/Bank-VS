from classes.checking import Checking
from classes.savings import Savings 
from classes.file_handler import Account_Handler
from classes.bank import Bank
from classes.transaction import Transaction

act_handler = Account_Handler()

hank_check = Checking('Hank','Hill',500)
hank_save = Savings('Hank','Hill',1650)

sally_check = Checking('Sally','Sells',2000)
sally_save = Savings('Sally','Sells',5000)

usbank = Bank('US Bank')

usbank.add_users(act_handler.import_existing_users())
usbank.print_users()

hank_check.add_transaction(Transaction(5000))