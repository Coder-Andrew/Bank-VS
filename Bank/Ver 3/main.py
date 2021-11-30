from classes.checking import Checking
from classes.savings import Savings 
from classes.file_handler import Account_Handler
from classes.bank import Bank
from classes.transaction import Transaction
from classes.plotter import Plotter


act_handler = Account_Handler()

usbank = Bank('US Bank')
usbank.add_users(act_handler.import_existing_users())

#usbank.print_users()

Plot = Plotter(usbank.users[0])

#Plot.plot()

Plot.plot()
