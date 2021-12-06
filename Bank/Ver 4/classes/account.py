import os
from transaction import Transaction

class Account:
    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.account_link = None
        self.transactions = []

        self.path = os.path.sep.join(__file__.split(os.path.sep)[:-2]) + os.path.sep + 'users' + os.path.sep + self.first_name + self.last_name + os.path.sep #sets path equal to the location in the users folder that corresponds to a user's first and last name

        self.make_folder_if_one_doesnt_exist()


    def make_folder_if_one_doesnt_exist(self):
        if not os.path.isdir(self.path):
            os.mkdir(self.path)


    def make_file_if_one_doesnt_exist(self, account_type):
        self.file_path = self.path + os.path.sep + account_type + '.txt'

        if not os.path.isfile(self.file_path):
            with open(self.file_path, 'w') as file:
                file.write('First Name,Last Name,Account Type,Balance\n')
                file.write('{},{},{},{}\n\nInitial Balance,Amount,Final Balance\n'.format(self.first_name, self.last_name, account_type, self.balance))
                file.write(f'0,{self.balance},{self.balance}\n')
            
            self.transactions.append(Transaction(self.balance,0,self.balance))


    def append_transaction_to_transaction_list(self, transaction):
        self.transactions.append(transaction)


    def rewrite_file_to_update_balance_in_file(self, account_file_path, account_type):
        with open(account_file_path, 'w') as file:
            file.write('First Name,Last Name,Account Type,Balance\n')
            file.write('{},{},{},{}\n\nInitial Balance,Amount,Final Balance\n'.format(self.first_name, self.last_name, account_type, self.balance))

            for i in self.transactions:
                file.write(i.write_format())


    def add_transaction(self, account_file_path, account_type, amount):
        if (self.balance + amount) < 0:
            raise ValueError('Cannot takeout more money than what\'s in your account')

        transaction = Transaction(amount, self.balance, self.balance + amount)
        
        self.balance = transaction.final
        self.transactions.append(transaction)

        self.rewrite_file_to_update_balance_in_file(account_file_path, account_type)

if __name__ == '__main__':
    test = Account('John', 'South', 500)

    print(test.transactions)
