from bank import Bank


def invalid_choice(choice):
    print(f'{choice} is not a valid choice. Please try again.\n')

westernBank = Bank()

while True:
    choice = input('\nWELCOME TO WESTERN BANKING SOLUTIONS\n\nMenu:\n\n(0) Customer Menu\n(1) Teller Menu\n(2) Quit\n\nChoice: ')

    if choice == '0':
        while True:
            choice = input('\nCUSTOMER MENU\n(0) Login\n(1) Create New Account\n(2) Quit\n\nChoice: ')

            if choice == '0':
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
                
                while True:
                    print(f'\nWelcome {user.first_name} {user.last_name}.')
                    print(f'You have ${user.balance:.2f} in your {user.account_type} account', end = '')
                    if user.account_link != None:
                        print(f' and ${user.account_link.balance:.2f} in your {user.account_link.account_type} account.\n\n')
                        
                        while True:
                            account_choice = input('Which account would you like to perform transactions on?\n(0) Checkings\n(1) Savings\n(2) Quit\n\nChoice: ')

                            if account_choice == '0':
                                if user.account_type != 'checking':
                                    user = user.account_link
                            
                            elif account_choice == '1':
                                if user.account_type != 'savings':
                                    user = user.account_link

                            elif account_choice == '2':
                                break

                            else:
                                print(f'{account_choice} is not a valid option, please try again.')
                                continue          
                        
                    else:
                        print('.\n\n')

                    while True:
                        print(f'What would you like to do with your {user.account_type} account?\n\nBalance: {user.balance:.2f}\n\n')

                        choice = input('(0) Withdraw\n(1) Deposit\n(2) View Balance\n(3) View Account Graphs\n(4) Quit\n\nChoice: ')

                        if (choice == '0') or (choice == '1'):
                            if choice == '0':
                                transaction_sign = -1   #Indicates a withdrawal
                            else:
                                transaction_sign = 1

                            while True:
                                transaction_amount = float(input('Enter the transaction amount: '))

                                if transaction_amount <= 0:
                                    print('Transaction amount cannot be less-than or equal-to 0, please try again.')
                                    continue

                                else:
                                    break

                            try:
                                user.add_transaction(user.file_path, user.account_type, transaction_amount * transaction_sign)

                            except ValueError as excpt:
                                print(excpt,'please try again.\n')

                        else:
                            invalid_choice(choice) ################################LEFT OFF HERE. WAS WORKING ON IMPLEMENTING QUIT, VIEW BALANCE, AND PYPLOT. NEED ACCOUNT CLOSING OPTION.



                #print(f'\n{user}\n\n')
                #user.balance = 99999
                #westernBank.print_users()


            elif choice == '1':     ###################################NEED TO IMPLEMENT ACCOUNT CREATION. NEED BANK METHOD TO ADD ACCOUNTS. 
                pass

            elif choice == '2':
                break

            else:
                invalid_choice(choice)

    elif choice == '1':     #################################NEED TO IMPLEMENT TELLER MENU AND TELLER OPERATIONS.
        pass 


    elif choice == '2':
        break

    else:
        invalid_choice(choice)