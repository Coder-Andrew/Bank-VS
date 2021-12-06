import os
import csv
from account import Account
from checking import Checking
from savings import Savings
from transaction import Transaction

class Bank:
    def __init__(self):
        self.users = []
        self.users_path = os.path.sep.join(__file__.split(os.path.sep)[:-2]) + os.path.sep + 'users' + os.path.sep


    def import_existing_users(self):
        walk_iter = os.walk(self.users_path)

        next(walk_iter)

        for i in walk_iter:
            for j in i[-1]:
                account_path = i[0] + os.path.sep + j

                if not (j != 'savings.txt' or j != 'checking.txt'):
                    print(f'File at path: \'{account_path}\' is not a valid file name/path.')
                    continue

                with open(account_path) as read_file:
                    csv_reader = csv.reader(read_file)

                    if next(csv_reader) != ['First Name','Last Name','Account Type','Balance']:
                        print(f'File at path: \'{account_path}\' does not have a valid header format. Skipping.')
                        continue

                    info = next(csv_reader)

                    if info[2] == 'checking':
                        account = Checking(info[0],info[1],int(info[3]))
                    elif info[2] == 'savings':
                        account = Savings(info[0],info[1],int(info[3]))
                    else:
                        raise ValueError(f'{info[2]} is not a valid account type.')

                    next(csv_reader)

                    if next(csv_reader) != ['Initial Balance','Amount','Final Balance']:
                        print(f'File at path: \'{account_path}\' does not have a valid transaction header format. Skipping.')
                        continue

                    for row in csv_reader:
                        account.append_transaction_to_transaction_list(Transaction(int(row[0]),int(row[1]),int(row[2])))

                    self.users.append(account)

        self.link_accounts()


    def link_accounts(self):
        for i in self.users:
            for j in self.users:
                if (i.first_name == j.first_name) and (i.last_name == j.last_name) and (i.account_type != j.account_type):
                    i.account_link = j
                    j.account_link = i
                    continue



testbank = Bank()
testbank.import_existing_users()
print(testbank.users[1].account_link, '\n', testbank.users[1])