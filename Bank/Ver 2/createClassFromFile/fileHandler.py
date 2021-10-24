import os

class Account_Handler:
    def __init__(self, directory = os.getcwd()):
        self.directory = directory

        if os.path.split(self.directory)[1] == 'Bank VS':
            self.directory += '\\Bank\\Ver 2\\createClassFromFile\\users\\'

    def input_from_file(self, filename):
        # = self.directory + '\\' + filename
        try:
            with open(filename) as read:
                read.readline()
                output_list = read.readline()[:-1].split(',')
        except:
            return 'Error in inputting file.'
        return output_list

    def dir_of_account(self, account): #returns a directory name for an account object in the users folder
        if self.is_account(account):
            dir_of_account = self.directory + account.user
            return dir_of_account
        return None

    def is_account(self, object):   #returns True if object is of type account and returns False otherwise
        if 'account' in str(type(object)):
            return True
        return False

    def dir_exists(self, dir_name): #checks if input is account object and checks if accounts username is in user list, otherwise checks if dir_name is in user_list
        if self.is_account(dir_name):
            if dir_name.user in self.user_list():
                return True
            return False
        if dir_name in user_list():
            return True
        return False

    def make_dir(self, dir_name):   #makes directory for account object if dir_name is account, otherwise makes a directory named dir_name. Returns directory of newly created dir
        if not self.dir_exists(dir_name):
            if self.is_account(dir_name):
                dir_name = self.dir_of_account(dir_name)
                os.mkdir(dir_name)
                return dir_name
            else:
                dir_name = self.directory + dir_name
                os.mkdir(dir_name)
                return dir_name
        else:
            print('Directory already exists.')

    def get_account_dir(self, account):
        account_dir = self.directory + account.user
        return account_dir

    def make_account_text(self, account):
        account_file = self.get_account_dir(account) + '\\' + account.account_type + '.txt'
        with open(account_file, 'w') as file:
            file.write('Account Name,Balance,Account Type\n')
            file.write(str(account) + '\n\n')
            file.write('Starting Balance,Transactions,End Balance')

    def user_list(self):
        return os.listdir(self.directory)
