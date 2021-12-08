from bank import Bank
from checking import Checking
from savings import Savings 
from plotter import Plotter

def invalid_choice(choice):
    print(f'{choice} is not a valid choice. Please try again.\n')

westernBank = Bank()
plotter = Plotter()

while True:
    choice = input('\nWELCOME TO WESTERN BANKING SOLUTIONS\n\nMenu:\n\n(0) Customer Menu\n(1) Teller Menu\n(2) Quit\n\nChoice: ')   #Main menu

    if choice == '0':
        while True:
            choice = input('\nCUSTOMER MENU\n(0) Login\n(1) Create New Account\n(2) Quit\n\nChoice: ')  #Customer menu

            if choice == '0':   #Login menu
                while True:
                    first_name = input('Please enter your first name. Enter q to quit: ')

                    if first_name == 'q':
                        break

                    last_name = input('Please enter your last name. Enter q to quit: ')

                    if first_name == 'q':
                        break

                    try:
                        user = westernBank.login_search(first_name, last_name)
                        break

                    except ValueError as excpt:
                        print(excpt, 'Please try again.\n')
                        continue

                if (first_name == 'q') or (last_name == 'q'):
                        break
                
                while True: #Successful login
                    print(f'\nWelcome {user.first_name} {user.last_name}.\n')
                    print(f'Balance {user.account_type} account: ${user.balance:.2f}')

                    if user.account_link != None:   #Checks if the user has both a checking and savings account
                        print(f'Balance {user.account_link.account_type} account: ${user.account_link.balance:.2f}\n')
                        
                        while True: #Menu for account choice. Defaults to whatever account the user has if they only have one account type. 
                            account_choice = input('Which account would you like to perform transactions on?\n(0) Checkings\n(1) Savings\n(2) Show Plots For Both Accounts\n(3) Quit\n\nChoice: ')

                            if account_choice == '0':   #Switches user's account to account_link account if the account isn't checking
                                if user.account_type != 'checking':
                                    user = user.account_link
                                break
                            
                            elif account_choice == '1': #Switches user's account to account_link account if the account isn't savings
                                if user.account_type != 'savings':
                                    user = user.account_link
                                break

                            elif account_choice == '2': 
                                plotter.plot_accounts([user,user.account_link])

                            elif account_choice == '3':
                                break

                            else:
                                invalid_choice(account_choice)
                                continue  
                        
                        if account_choice == '3':
                            break
                        
                    else:
                        print('.\n\n')

                    while True: #User account operations menu
                        print(f'What would you like to do with your {user.account_type} account?\n\nBalance: {user.balance:.2f}\n')

                        choice = input('(0) Withdraw\n(1) Deposit\n(2) View Balance\n(3) View Account Graphs\n(4) Close Account\n(5) Quit\n\nChoice: ')

                        if (choice == '0') or (choice == '1'):
                            #print(f'\n\n{user.print(user.account_type)}\n\n')
                            if choice == '0':
                                transaction_sign = -1   #Indicates a withdrawal
                                if user.balance == 0:
                                    print('Cannot withdraw with a balance of zero.')
                                    continue
                            else:
                                transaction_sign = 1


                            while True:
                                transaction_amount = float(input('Enter the transaction amount: '))

                                if transaction_amount <= 0:
                                    print('Transaction amount cannot be less-than or equal-to 0, please try again.')
                                    continue

                                try:
                                    user.add_transaction(user.file_path, user.account_type, transaction_amount * transaction_sign)

                                except ValueError as excpt:
                                    print(excpt,'please try again.\n')

                                else:
                                    break

                        elif choice == '2':
                            print(f'\nBalance in {user.account_type}: ${user.balance:.2f}\n')

                        elif choice == '3':
                            plotter.plot_account(user)

                        elif choice == '4':
                            user.close_account(user.file_path)

                            if user.account_link != None:
                                user.account_link.account_link = None   #Delinks account from account_link's link.
                            
                            westernBank.delete_user(user)

                            break

                        elif choice == '5':
                            break

                        else:
                            invalid_choice(choice)

                    if (choice == '5') or (choice == '4'):
                        break

            elif choice == '1': #Create new account
                first_name = input('Enter your first name: ')
                last_name = input('Enter your last name: ')

                while True:
                    try:
                        account_type = input('\nWhat kind of account would you like?\n(0) Checking\n(1) Savings\n\nChoice: ')

                        if (account_type != '0') and (account_type != '1'):
                            raise ValueError(f'{account_type} is not a value option. Please try again')

                        initial_balance = float(input('Enter the initial balance for the account: '))

                        if initial_balance <= 0:
                            raise ValueError(f'Initial balance cannot be less-than or equal-to 0, please try again.')

                        break

                    except ValueError as excpt:
                        print(excpt)

                while True: #Adjusts last name until a last name that doesn't exist is found

                    if account_type == '0':
                        user = Checking(first_name, last_name, initial_balance)

                    elif account_type == '1':
                        user = Savings(first_name, last_name, initial_balance)

                    if user.exists:
                        last_name += '1'
                        continue
                    else:
                        break

                westernBank.add_user(user)

                print(f'\nAccount creation success, {user.account_type} with first name {user.first_name} and last name {user.last_name} created! Please proceed to login.')

            elif choice == '2':
                break

            else:
                invalid_choice(choice)

    elif choice == '1':
        while True:
            teller_choice = input('\nWelcome Teller\n\nMenu Options:\n(0) Search for account\n(1) Print out all accounts\n(2) Plot all accounts\n(3) Quit\n\nChoice: ')

            if teller_choice == '0':
                first_name = input('Enter the first name of the person\'s account that you wish to search for: ')
                last_name = input('Enter the last name of the person\'s account that you wish to search for: ')

                try:
                    user = westernBank.login_search(first_name, last_name)
                    print()
                    print(user.print(user.account_type))
                    if user.account_link != None:
                        print(user.account_link.print(user.account_link.account_type))

                except ValueError as excpt:
                    print(excpt)

            elif teller_choice == '1':
                print('\nUsers:')
                westernBank.print_users()

            elif teller_choice == '2':
                plotter.plot_accounts(westernBank.users)

            elif teller_choice == '3':
                break

            else:
                invalid_choice(teller_choice)
                

    elif choice == '2':
        break

    else:
        invalid_choice(choice)