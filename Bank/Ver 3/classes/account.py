import os

class Account:
    def __init__(self, first_name, last_name, balance, transactions = []):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.transactions = transactions
        self.accounts = []

        #strips the file name from the directory, directs to the Ver 3 directory, then goes to the user's directory
        self.path = os.path.split(os.path.split(__file__)[0])[0] + '\\users\\' + self.first_name + self.last_name + '\\'
        self.file_path = None
                                                                                                                           

        self.make_folder_if_one_doesnt_exist()

    def make_folder_if_one_doesnt_exist(self):
        if os.path.isdir(self.path) == True:
            pass
        else:
            os.mkdir(self.path)

    def make_file_if_one_doesnt_exist(self, account_type, file_path):
        if os.path.isfile(file_path) == True:
            pass
        else:
            with open(file_path,'w') as file:
                file.write('First Name,Last Name,Account Type,Balance\n')
                file.write('{},{},{},{}\n\nInitial Balance,Amount,Final Balance,Checked\n'.format(self.first_name, self.last_name, account_type, self.balance))

    def write_un_checked_transactions(self):
        with open(self.file_path,'a') as file:
            for i in self.transactions:
                if i.checked == False:
                    i.checked = True
                    file.write('{},{},{},{}\n'.format(self.balance, i.amount, self.balance + i.amount, i.checked))
                    self.balance += i.amount

    def add_transaction(self, transaction):
        transaction.balance_initial = self.balance
        self.balance += transaction.amount
        transaction.balance_final = self.balance
        #transaction.checked = True
        self.transactions.append(transaction)
        self.append_transaction_to_file(transaction) #left off here, still need to test,
        self.write_to_file()

    def write_to_file(self):
        with open(self.file_path, 'w') as file:
                file.write('First Name,Last Name,Account Type,Balance\n')
                file.write('{},{},{},{}\n\nInitial Balance,Amount,Final Balance\n'.format(self.first_name, self.last_name, self.account_type, self.balance))
                for i in self.transactions:
                    file.write(i.format_for_write())

    def append_transaction_to_file(self, transaction):
        with open(self.file_path,'a') as file:
            file.write(transaction.format_for_write())

    #def import_transactions(self):

    def update_balance_after_transactions(self):
        initial_balance = self.balance
        print(initial_balance)
        for i in self.transactions:
            if i.checked == False:
                i.checked = True
                i.balance_initial = self.balance
                self.balance += i.amount
                i.balance_final = self.balance

                with open(self.file_path,'a') as file:
                    file.write(i.format_for_write())

        with open(self.file_path,'a+') as file: #FIX ME!!! Should update balance at the top of the text file.
            data = file.read()
            data[1].replace(str(initial_balance)+'\n', str(self.balance)+'\n')
            file.write(data)

    def print_transactions(self):
        for i in self.transactions:
            print(i)

    def __str__(self):
        return 'Please Work: {},{},{},{}'.format(self.first_name, self.last_name, self.account_type, self.balance)