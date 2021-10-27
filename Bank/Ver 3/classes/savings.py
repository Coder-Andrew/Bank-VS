from .account import Account

class Savings(Account):
    def __init__(self, first_name, last_name, balance):
        super().__init__(first_name, last_name, balance)
        self.account_type = 'savings'
        self.file_path = self.path + 'savings.txt'

        self.make_file_if_one_doesnt_exist(self.account_type, self.file_path)


