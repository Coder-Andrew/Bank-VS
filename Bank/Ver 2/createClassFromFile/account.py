class Account:
    def __init__(self, user, balance, transactions = []):
        self.user = user
        self.balance = int(balance)
        self.transactions = transactions

    def __str__(self):
        return ('{},{},{}'.format(self.user, self.balance, self.transactions))


class Checking(Account):
    def __init__(self, user, balance, transactions = []):
        Account.__init__(self, user, balance, transactions)
        self.account_type = 'checking'
        
    def __str__(self):
        return Account.__str__(self) + ',' + self.account_type


class Savings(Account):
    def __init__(self, user, balance, transactions = []):
        Account.__init__(self, user, balance, transactions)
        self.account_type = 'saving'

    def __str__(self):
        return Account.__str__(self) + ',' + self.account_type

hank = Checking('Hank', 200)

