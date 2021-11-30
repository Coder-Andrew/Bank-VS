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
                if j == 'savings.txt' or j == 'checking.txt':
                    hold_list.append(os.path.join(self.users_path,i,j))
        return hold_list

    def import_existing_users(self):
        hold_list = []

        for i in self.list_account_file_directories():
            #print('\t\t',i)
 
            with open(i) as file:
                file.readline()                                         #skips header
                info = file.readline().strip().split(',')               #saves user info as info 
                #print('\t\t',info)
                if info[2] == 'savings':                                #recreates saving or checking objects
                    user = Savings(info[0],info[1],int(info[3]))
                    #user.transactions = []
                elif info[2] == 'checking':
                    user = Checking(info[0],info[1],int(info[3]))
                    #user.transactions = []
                #print(user)
                file.readline()                                         #skips newline and transaction header
                file.readline()

                while True:                                             #entering loop that inputs user's transactions
                    info = file.readline().strip()
                    #print(info)

                    if info == '':
                        #print(info)
                        break

                    info = info.strip().split(',')


                    #print(info)
                    user.transactions.append(Transaction(int(info[1]),int(info[0]),int(info[2])))
                #print()
                #print(user.print_transactions())

            #print(user.first_name)       
            #user.print_transactions()
            #print()
                user.set_initial_balance()
                hold_list.append(user)
                
        return hold_list

