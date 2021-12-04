import os
from account import Account

class Checking(Account):
    def __init__(self, first_name, last_name, balance):
        super().__init__(first_name, last_name, balance)
        self.account_type = 'checking'
        self.account_link = None

        self.file_path = self.path + os.path.sep + self.account_type + '.txt'

        self.make_file_if_one_doesnt_exist(self.account_type, self.file_path)


test = Checking('Andrew','Test',500)