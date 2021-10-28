class Person:
    def __init__(self, age, lst = []):
        self.age = 5
        self.lst = lst

    def print_list(self):
        for i in self.lst:
            print(i)

class Dollar:
    def __init__(self, amount=0):
        self.amount = amount

    def __str__(self):
        return '{}'.format(self.amount)
    
hank = Person(5,[Dollar(50),Dollar(100)])
sally = Person(50,[Dollar(500),Dollar(600)])

user = hank

user.lst.append(Dollar(-100))

user = sally

user.lst.append(Dollar(0))

print('H',hank.print_list())
print('S',sally.print_list())
