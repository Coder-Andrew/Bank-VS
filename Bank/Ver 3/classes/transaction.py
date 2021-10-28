class Transaction:
    def __init__(self, amount, balance_initial = 0, balance_final = 0, checked = False):
        self.amount = amount
        self.checked = checked

        self.balance_initial = balance_initial
        self.balance_final = balance_final

    def export_if_not_checked(self):
        if self.checked == False:
            self.checked = True
            return self.amount
        return 'Already checked'

    def format_for_write(self):
        return '{},{},{}\n'.format(self.balance_initial, self.amount, self.balance_final)

    def __str__(self):
        return '{},{},{}'.format(self.balance_initial, self.amount, self.balance_final)