class Parent:
    def __init__(self, name, data = []):
        self.name = name
        self.data = data

    def input_data(self):
        with open(self.name) as file:
            while True:
                info = file.readline().strip()

                if info == '':
                    break
                self.data.append(info)

    def print_data(self):
        for i in self.data:
            print('\t',i)


class Child(Parent):
    def __init__(self, name, balance = 0):   
        super().__init__(name)  #add empty list in parent init, thought process was that parent was already going to be initialized with an empty list for the data attribute
        self.balance = balance


child1 = Child('info.txt',0)
child2 = Child('info1.txt',999)

#print(child1.name)

child1.input_data()
child2.input_data()

print('Child1')
child1.print_data()
print('Child2')
child2.print_data()


'''
Is it okay to make a parent class with an attribute/method that only the child classes use?
I know I can, but is it bad practice to?

I.E.
class Parent:
    init: self.name, self.data

    def print_data_with_balance(self):
        print('{} with balance: {}'.format(self.data, self.balance))


class Child(Parent):
    init: self.name, self.data, self.balance


child1 = Child('test',0,1000)
child.print_data_with_balance()

'''
