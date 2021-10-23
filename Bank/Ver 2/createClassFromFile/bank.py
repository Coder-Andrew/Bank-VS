from fileHandler import Account_Handler
from account import Account, Checking, Savings
import os

class Bank:
    def __init__(self, *args):
        self.users = [*args]

    def add_user(self, user):
        self.users.append(user)

    def import_existing_users(self):
        handle_accounts = Account_Handler()
        #print(handle_accounts.directory)
        for i in handle_accounts.user_list():
            for j in os.listdir(handle_accounts.directory + '\\' + i):
                j = j.lower()
                users_accounts = handle_accounts.directory + i + '\\' + j

                if j == 'checking.txt':
                    account_info = handle_accounts.input_from_file(users_accounts)
                    self.add_user(Checking(account_info[0],account_info[1]))

                if j == 'savings.txt':
                    account_info = handle_accounts.input_from_file(users_accounts)
                    self.add_user(Savings(account_info[0],account_info[1]))

usbank = Bank()

usbank.import_existing_users()
for i in usbank.users:
    print(i)