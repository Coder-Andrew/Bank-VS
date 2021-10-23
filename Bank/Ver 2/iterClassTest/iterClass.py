class MyList:
    def __init__(self, items):
        self.items = items

        self.index = 0

    def __iter__(self):
        return TestIter()

    def __next__(self):
        if self.index < len(self.items):
            result = self.items[self.index]

            self.index += 1
            return result

        raise StopIteration


mylist = MyList(['Bob','Hank','Phill','Stacy','Rob'])


for i in mylist:
    print(i)