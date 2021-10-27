import os
from .checking import Checking
from .savings import Savings
from .transaction import Transaction 

class Account_Handler:
    def __init__(self, users_path = os.path.split(os.path.split(__file__)[0])[0]+ '\\users\\'):
        self.users_path = users_path

    def list_users(self):
        return os.listdir(self.users_path)

    def list_account_file_directories(self):
        hold_list = []
        for i in self.list_users():
            for j in os.listdir(self.users_path + i):
                hold_list.append(os.path.join(self.users_path,i,j))
        return hold_list

    def import_transaction(self, amount):   #might need to modify to include the checked variable. 
        return Transaction(amount)

    def import_existing_users(self):
        hold_list = []
        for i in self.list_account_file_directories():
            with open(i) as file:
                file.readline()                                         #skips header
                info = file.readline().strip().split(',')               #saves user info as info 
            
                if info[2] == 'savings':                                #recreates saving or checking objects
                    user = Savings(info[0],info[1],info[3])
                if info[2] == 'checking':
                    user = Checking(info[0],info[1],info[3])

                file.readline()                                         #skips newline and transaction header
                file.readline()

                while True:                                             #entering loop that inputs user's transactions
                    info = file.readline().strip()

                    if info == '':
                        break

                    info = info.strip().split(',')

                    user.transactions.append(Transaction(info[1],info[0],info[2],info[3]))

            hold_list.append(user)
        return hold_list

