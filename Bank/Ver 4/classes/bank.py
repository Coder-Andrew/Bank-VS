import os
import csv
from account import Account
from checking import Checking
from savings import Savings
from transaction import Transaction
from plotter import Plotter

class Bank:
    def __init__(self):
        self.users = []
        self.users_path = os.path.sep.join(__file__.split(os.path.sep)[:-2]) + os.path.sep + 'users' + os.path.sep

        self.import_existing_users()

    def import_existing_users(self):
        failed_imports = []

        walk_iter = os.walk(self.users_path)
        next(walk_iter)

        for i in walk_iter:
            for j in i[-1]:
                account_path = i[0] + os.path.sep + j

                if not (j != 'savings.txt' or j != 'checking.txt'):     #Simple check to if file names are correct, skips import if not.
                    #print(f'File at path: \'{account_path}\' is not a valid file name/path.')
                    failed_imports.append(account_path)
                    continue

                with open(account_path) as read_file:
                    csv_reader = csv.reader(read_file)

                    if next(csv_reader) != ['First Name','Last Name','Account Type','Balance']:     #Checks if file headers are correct
                        #print(f'File at path: \'{account_path}\' does not have a valid header format. Skipping.')
                        failed_imports.append(account_path)
                        continue

                    info = next(csv_reader)

                    if info[2] == 'checking':   #Reconstructs checking or savings account classes based on the second line in text file
                        account = Checking(info[0],info[1],float(info[3]))
                    elif info[2] == 'savings':
                        account = Savings(info[0],info[1],float(info[3]))
                    else:
                        raise ValueError(f'{info[2]} is not a valid account type.')

                    next(csv_reader)

                    if next(csv_reader) != ['Initial Balance','Amount','Final Balance']:    #Another format check
                        #print(f'File at path: \'{account_path}\' does not have a valid transaction header format. Skipping.')
                        failed_imports.append(account_path)
                        continue

                    for row in csv_reader:
                        account.append_transaction_to_transaction_list(Transaction(float(row[0]),float(row[1]),float(row[2])))

                    self.users.append(account)

        self.link_accounts()
        self.sort_users_by_last_name()
        
        return failed_imports


    def link_accounts(self):    #Links users savings and checking accounts for easier pyplot operations
        account_dict = {}
        for i in self.users:
            account_key = i.first_name + i.last_name

            if account_key in account_dict.keys():
                account_value = account_dict[account_key]
                account_value.append(i)
                
                if len(account_dict[account_key]) > 1:
                    account_value[0].account_link = account_value[1]
                    account_value[1].account_link = account_value[0]

            else:
                account_dict[account_key] = [i]

        return account_dict


    def login_search(self, first_name, last_name):
        for i in self.users:
            if (first_name == i.first_name) and (last_name == i.last_name):
                return i
        
        raise ValueError('Account not found.')

    
    def delete_user(self, user):
        for i in range(len(self.users)):
            if self.users[i] == user:
                del(self.users[i])
                break


    def add_user(self, user):
        self.users.append(user)
        self.link_accounts()


    def print_users(self):
        for i in self.users:
            print(i.print(i.account_type))


    def sort_users_by_last_name(self):  #Insertion sort
        for i in range(1,len(self.users)):
            j = i

            while (j > 0) and (self.users[j].last_name < self.users[j-1].last_name):
                temp = self.users[j]
                self.users[j] = self.users[j-1]
                self.users[j-1] = temp
                j -= 1



if __name__ == '__main__':
    testbank = Bank()
    #testbank.import_existing_users()
    #print(testbank.users[1].account_link, '\n', testbank.users[1])
    testbank.print_users()
    testbank.sort_users_by_last_name()
    print()
    testbank.print_users()

    plter = Plotter()

    print('\n',testbank.users[0].print(testbank.users[0].account_type))
    #plter.plot_accounts([testbank.users[0],testbank.users[2]])
    plter.plot_accounts(testbank.users)