class Transaction:
    def __init__(self, amount = 0, transaction_type = 'deposit'):
        self.transaction_type = transaction_type
        self.amount = amount

        if (transaction_type == 'withdrawal') or (transaction_type == 'w'):
            self.amount = self.amount * -1

    def get_amount(self):
        return self.amount

