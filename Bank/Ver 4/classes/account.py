import os

class Account:
    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.transactions = []

        self.path = os.path.sep.join(__file__.split(os.path.sep)[:-2]) + os.path.sep + 'users' + os.path.sep + self.first_name + self.last_name + os.path.sep #sets path equal to the location in the users folder that corresponds to a user's first and last name
        print(__file__)
        self.make_folder_if_one_doesnt_exist()

    @staticmethod
    def join(lst, sep = '/') -> list:
        '''Converts a list into a string separated by sep'''
        temp_str = ''
        for i in lst:
            temp_str += str(i) + sep
            
        return temp_str

    def make_folder_if_one_doesnt_exist(self):
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

    def make_file_if_one_doesnt_exist(self, account_type, file_name_path):
        if not os.path.isfile(file_name_path):
            with open(file_name_path, 'w') as file:
                file.write('First Name,Last Name,Account Type,Balance\n')
                file.write('{},{},{},{}\n\nInitial Balance,Amount,Final Balance,Checked\n'.format(self.first_name, self.last_name, account_type, self.balance))
                file.write(f'0,{self.balance},{self.balance}\n')


if __name__ == '__main__':
    test = Account('Andrew', 'South', 500)

    print(test.path)
