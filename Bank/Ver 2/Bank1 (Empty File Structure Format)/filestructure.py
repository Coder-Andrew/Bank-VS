import os

path = '\\Bank1'

cwd = os.getcwd()

tree = cwd + path

folders = {'Users':['user1','user2','user3'], 'Classes' : ['account', 'file handling', 'bank']}

print(cwd)

os.mkdir(tree+'\\Test')

for i, j in folders.items():
    print(i)
    os.mkdir(tree+ '\\' +i)
    for k in j:
        os.mkdir(tree + '\\' + i + '\\' +k)