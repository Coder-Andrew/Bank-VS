class Parent:
    def __init__(self, name):
        self.name = name

    def print_name_and_amount(self):
        print('{} has balance {}'.format(self.name, self.balance))


class Child(Parent):
    def __init__(self, name, balance):
        super().__init__(name)
        self.balance = balance


child1 = Child('Frank', 5000)

child1.print_name_and_amount()
