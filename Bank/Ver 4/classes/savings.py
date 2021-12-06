import os
from account import Account

class Savings(Account):
    def __init__(self, first_name, last_name, balance):
        super().__init__(first_name, last_name, balance)
        self.account_type = 'savings'

        self.make_file_if_one_doesnt_exist(self.account_type)

if __name__ == '__main__':
    hank = Savings('Hank', 'Hill', 1000)
    print(hank.transactions)