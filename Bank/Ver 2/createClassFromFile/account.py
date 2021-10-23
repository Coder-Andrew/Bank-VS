class Account:
    def __init__(self, user, balance, transactions = []):
        self.user = user
        self.balance = int(balance)
        self.transactions = transactions

    def __str__(self):
        return ('{},{},{}'.format(self.user, self.balance, self.transactions))

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance_after_transactions(self):
        temp_balance = self.balance

        for i in self.transactions:
            temp_balance += i.get_amount()

        return temp_balance

    def print_transactions(self):
        for i in self.transactions:
            print('{},{},{}\n'.format(self.balance, i.get_amount(), self.balance + i.get_amount()))
            self.balance += i.get_amount()


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

