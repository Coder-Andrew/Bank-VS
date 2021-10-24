class Account:
    total_money_in_bank = 0
    def __init__(self, user, balance, transactions = []):
        self.user = user
        self.balance = int(balance)
        self.transactions = transactions

        Account.update_total_money(self)

    def __str__(self):
        return ('{},{}'.format(self.user, self.balance))

    def update_total_money(self):
        Account.total_money_in_bank += self.balance

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
            Account.total_money_in_bank += i.get_amount()
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
