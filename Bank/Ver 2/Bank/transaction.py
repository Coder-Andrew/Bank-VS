class Transaction:
    def __init__(self, amount, transaction_type = 'deposit'):
        self.transaction_type = transaction_type
        self.amount = amount
        self.counted_for = False

        if (transaction_type == 'withdrawal') or (transaction_type == 'w'):
            self.amount = self.amount * -1

    def get_amount(self):
        return self.amount

    def count(self):    #a method that 'counts' a transaction. This is so that a transaction isn't coninuiously* called and the balance of the user isn't overly affected
        self.counted_for = True

