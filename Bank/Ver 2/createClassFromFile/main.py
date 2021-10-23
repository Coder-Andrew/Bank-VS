from account import Account, Checking, Savings
from fileHandler import Account_Handler

file_name = 'Checking.txt'

hank = Account_Handler()
hank.directory += 'user1'
info = hank.input_from_file('checking.txt')

print(info)


try:
    hank_act = Checking(info[0],info[1])

except ValueError as excpt:
    print(excpt, 'attempted to create class with wrong type')


print(hank.user_list())