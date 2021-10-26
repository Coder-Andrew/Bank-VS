import os

class Account:
    def __init__(self, first_name, last_name, balance, transactions = []):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.transactions = transactions 

        self.path = os.path.split(__file__)[0]  #strips the file name from the directory
        self.path = os.path.split(self.path)[0] + '\\users\\' + self.first_name + self.last_name + '\\' #directs to the ver3 directory, then goes to the users directory 

        self.make_folder_if_one_doesnt_exist()

    def make_folder_if_one_doesnt_exist(self):
        if os.path.isdir(self.path) == True:
            pass
        else:
            os.mkdir(self.path)

    def make_file_if_one_doesnt_exist(self, account_type, balance):
        file_dir = self.path + account_type + '.txt'
        if os.path.isfile(self.path) == True:
            pass
        else:
            with open(self.path,'w') as file:
                file.write('Account Name,Account Type,Balance\n')
                file.write('{},{},{}\n\nInitial Balance,Amount,Final Balance\n'.format(self.first_name + self.last_name, account_type, balance))
