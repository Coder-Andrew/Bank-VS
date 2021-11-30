import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, *args):
        self.user_accounts = [*args]
        self.user = self.user_accounts[0]
        self.colors = ['blue','orange','green','red','black']


    def print_user_accounts(self):
        for i in self.user_accounts:
            print(i)

    def first_point(self):
        return self.user.initial_balance

    def plot_range(self):
        hold = [self.first_point()]
        for i in self.user.transactions:
            hold.append(i.balance_final)
        return hold

    def plot_domain(self):
        hold = ['Balance at Account Creation']
        transaction_num = 1
        for i in range(len(self.user.transactions)):
            hold.append('Transaction #{}'.format(transaction_num))
            transaction_num += 1
        return hold

    def plot(self):
        plt.title(self.user.first_name + ' ' + self.user.last_name + '\'s ' + 'accounts.')
        
        for i in range(len(self.user_accounts)):
            plt.plot(self.plot_domain(), self.plot_range(), marker = '*')
            plt.show()

    def show_plot(self):
        plt.show()


    def show_plot(self):
        pass

