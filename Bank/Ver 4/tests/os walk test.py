import os

users_path = os.path.sep.join(__file__.split(os.path.sep)[:-2]) + os.path.sep + 'users' + os.path.sep

walk_iter = os.walk(users_path)

next(walk_iter)
j = next(walk_iter)
for i in walk_iter:
    #print(i)
    for j in i[-1]:
        print(i[0]+os.path.sep+j)


