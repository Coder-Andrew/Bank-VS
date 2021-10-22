class PrintMe:
    def __init__(self, string = 'Hello World!'):
        self.string = string

    def __str__(self):
        return self.string

def main():
    print(PrintMe('This is my test case.'))

if __name__ == '__main__':
    main()