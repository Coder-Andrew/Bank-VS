class Transaction:
    def __init__(self, amount, initial_bal, final_bal):
        self.amount = amount
        self.initial = initial_bal
        self.final = final_bal


    def write_format(self):
        return f'{self.initial},{self.amount},{self.final}'


    def __str__(self):
        return f'Transaction amount:{self.amount}\nBalance before transaction: {self.initial}\nBalance after transaction: {self.final}\n'