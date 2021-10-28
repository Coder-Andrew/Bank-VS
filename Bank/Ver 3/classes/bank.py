from .file_handler import Account_Handler

class Bank:
    def __init__(self,name, *args):
        self.name = name
        self.users = []

    def add_user(self, user):
        self.user.append(user)

    def add_users(self, list_users):
        self.users += list_users

    def print_users(self):
        for i in self.users:
            print('First Name: {}, Last Name: {}, Account Type: {}, Balance: {}'.format(i.first_name, i.last_name, i.account_type, i.balance))