class User:
    def __init__(self, username, email_address):
        self.name = username			
        self.email = email_address		
        self.account_balance = 0

    def make_deposit(self, amount):	
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.account_balance < amount:
            print('Insufficient balance')
        else:
            self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f'{self.name} has {self.account_balance} dollars')
        return self

    def transfer_money(self, other_user, amount):
        if self.account_balance < amount:
            print('Insufficient balance')
        else:
            self.make_withdrawal(amount)
            other_user.make_deposit(amount)
        return self

class BankAccount:
    def __init__(self, yld_rate, balance):
        self.yld_rate = yld_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance-amount)<0:
            print("You got not enough money!")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        # introducir nombre usuario
        print(f'Hi nombre! You got {self.balance} dollars')
        return self

    def yield_interest(self):
        self.balance += self.balance * self.yld_rate
        return self

account01 = BankAccount(0.05, 15000)
account02 = BankAccount(0.01, 35000)

account01.deposit(30400).deposit(340011).deposit(2031).withdraw(7500).yield_interest().display_account_info()
account02.deposit(25000).deposit(30000).withdraw(2000).withdraw(3040).withdraw(2000).withdraw(3040).yield_interest().display_account_info()


# alfonso = User('Alfonso Gómez', 'agomez@yahoo.es')
# felipe = User('Felipe Avello', 'favello@yahoo.es')
# george = User('George Carlin', 'gcarlin@spyder.de')

# alfonso.make_deposit(300).make_deposit(1050).make_deposit(321301).make_withdrawal(15000).display_user_balance()

# felipe.make_deposit(50000).make_deposit(50000).make_withdrawal(50000).make_withdrawal(60000).display_user_balance()

# george.make_deposit(1000000).make_withdrawal(10000).make_withdrawal(10000).display_user_balance()

# alfonso.transfer_money(george, 20000)
# alfonso.display_user_balance()
# george.display_user_balance()
