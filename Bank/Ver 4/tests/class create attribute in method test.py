class test:
    def __init__(self):
        self.data_test = 50

    def add_attribute(self, more_data):
        self.new_data = more_data

test = test()
try:
    print(test.new_data)

except:
    print('test.new_data doesnt exist')

test.add_attribute(1000)

print(test.new_data)
