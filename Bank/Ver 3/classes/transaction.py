class Transaction:
    def __init__(self, amount, checked = False):
        self.amount = amount
        self.checked = checked

    def export_if_not_checked(self):
        if self.checked == False:
            self.checked = True
            return self.amount
        return 'Already checked'