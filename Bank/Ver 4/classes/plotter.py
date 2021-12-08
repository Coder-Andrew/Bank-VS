from matplotlib import pyplot as plt

class Plotter:
    def __init__(self):
        self.plot = None


    def plot_account(self, account):
        y_axis = []

        for i in account.transactions:
            y_axis.append(i.final)

        plt.ylabel('Balance in $')
        plt.xlabel('Transaction Number')
        plt.xticks(range(len(y_axis)))
        plt.plot(y_axis)
        plt.title(f'{account.first_name}\'s {account.account_type} account.')
        plt.show()


    def plot_accounts(self, list_accounts):
        legend_list = []
        for i in list_accounts:
            x_axis = []

            legend_list.append(f'{i.first_name}\'s {i.account_type}')

            for j in i.transactions:
                x_axis.append(j.final)

            plt.plot(x_axis, marker = 'o')

        plt.legend(legend_list)
        plt.ylabel('Balance in $')
        plt.xlabel('Transaction Number')

        if len(list_accounts) == 2:
            plt.title(f'{i.first_name}\'s accounts.')
        else:
            plt.title('Accounts')

        plt.show()