import os
from account import Account

class Checking(Account):
    def __init__(self, first_name, last_name, balance):
        super().__init__(first_name, last_name, balance)
        self.account_type = 'checking'

        self.make_file_if_one_doesnt_exist(self.account_type)

if __name__ == '__main__':
    test = Checking('Fred','Jennings',500)
    test.add_transaction(test.file_path, test.account_type, 1000)
    test.add_transaction(test.file_path, test.account_type, -500)