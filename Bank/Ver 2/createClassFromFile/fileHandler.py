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

    def user_list(self):
        return os.listdir(self.directory)
