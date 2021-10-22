class Bank:
    def __init__(self, *args):
        self.users = [*args]
        self.login_index = None


    def add_user(self, user):
        self.users.append(user)

    def print_users(self):
        for i in self.users:
            print(i)

    def print_user(self, username):
        for i in self.users:
            
            if i.username == username:
                return str(i)

        return 'Username {} not found.'.format(username)

    def check_user_balance(self, username):
        for i in self.users:
            if i.username == username:
                return ('{}\'s balance: ${}'.format(i.username,i.balance))
        else:
            return ('Username {} not found.'.format(username))

    def find_user_index(self, username):
        if self.user_exists(username):
            for i in range(len(self.users)):
                if self.users[i].username == username:
                    return i

    def user_exists(self, user):
        for i in self.users:
            if i.username == user:
                return True
        else:
            print('User {} not found.'.format(user))
            return False

    def login(self, username, password):
        if self.user_exists(username):
            user_index = self.find_user_index(username)
            
            if self.users[user_index].password == password:
                self.login_index = user_index
                return 'Login successful welcome {}'.format(username)
            else:
                return 'Incorrect login information'

    def logout(self):
        self.login_index = None

    def add_charge(self, charge):
        if self.user_exists(charge.to):
            self.users[self.find_user_index(charge.to)].charges.append(charge)


class Account:
    def __init__(self, username, password, balance = 0):
        self.username = username
        self.password = password
        self.balance = balance

    def check_balance(self):
        return 'Balance: ${:,.2f}'.format(self.balance)

    def __str__(self):
        return 'Username: {:<10}Password: {:<10}Balance: ${:<12,.2f}'.format(self.username, self.password, self.balance)


class User(Account):
    def __init__(self, username, password, balance = 0):
        Account.__init__(self, username, password, balance)
        self.charges = []

    def __str__(self):
        self.del_charges()
        output_str = ''
        output_str += Account.__str__(self) + '\nCharges:\n'
        for i in self.charges:
            output_str += str(i)

        return output_str

    def add_charge(self, charge):
        self.charges.append(charge)

    def charge_exists(self, charge_name):
        for i in self.charges:
            if i.charge_name == charge_name:
                return True
        print('Charge name: \'{}\' not found.'.format(charge_name))
        return False


    def pay_charge(self, charge_name, amount):
        if self.charge_exists(charge_name):
            if amount > self.balance:
                return 'Can\'t pay more than you have in your account'
            
            for i in self.charges:
                if i.charge_name == charge_name:
                    if i.amount - amount < 0:
                        self.balance -= i.amount
                        i.amount = 0
                    else:
                        self.balance -= amount
                        i.amount -= amount


    def del_charges(self):
        i = 0
        length = len(self.charges)

        while i < length:
            if self.charges[i].amount <= 0:
                del(self.charges[i])
                length = len(self.charges)
                i = -1
            i += 1


class Admin(Account):
    def __init__(self, bank, username = 'Admin', password = 'Admin', balance = 9999999, authority = 1,):
        Account.__init__(self, username, password, balance)
        self.bank = bank
        self.authority = authority

    def test(self):
        self.bank.print_users()

    def test_authority(self, required):
        if self.authority < required:
            print('Access Denied: Authority level {} is required. Your\'s is: {}'.format(required, self.authority))
            return False
        else:
            return True

    def add_user(self, user):
        if self.test_authority(1):
            self.bank.add_user(user)


    def check_user_balance(self, user):
        if self.test_authority(1):
            print(self.bank.check_user_balance(user))

    def print_user(self, user):
        if self.test_authority(2):
            self.bank.print_user(user)


    def print_users(self):
        '''Only allows access to bank's methods if admin meets a certain authority level'''

        if self.test_authority(3):
            self.bank.print_users()

class Charge:
    def __init__(self, to, from_user, amount, charge_name):
        self.to = to
        self.from_user = from_user
        self.amount = amount
        self.charge_name = charge_name

    def __str__(self):
        return '\n\tCharge Name: {}\n\tFrom: {}\n\tAmount: ${:,.2f}\n'.format(self.charge_name, self.from_user, self.amount)
        
    def del_charge(self):
        del()

frank = User('Frank1', 'Rank1',1000)
sally = User('Sally1', 'Sloth', 1000)
hank = User('HankHill', 'Propane', 50000)

usbank = Bank(frank, sally, hank)

admin = Admin(usbank, authority = 5)
usbank.add_user(admin)

frank.add_charge(Charge('Frank1', 'Sally1', 10000, 'Groceries and Dinner'))
frank.add_charge(Charge('Frank1', 'HankHill', 20, 'Propane'))
frank.add_charge(Charge('Frank1', 'Andrew', 5000, 'Taxes'))
    #left off making sure to check the admin's authority before allowing an access to usbank's methods
    #work on charge class, more admin methods, sending charges etc...
