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

alfonso = User('Alfonso Gómez', 'agomez@yahoo.es')
felipe = User('Felipe Avello', 'favello@yahoo.es')
george = User('George Carlin', 'gcarlin@spyder.de')

alfonso.make_deposit(300).make_deposit(1050).make_deposit(321301).make_withdrawal(15000).display_user_balance()

felipe.make_deposit(50000).make_deposit(50000).make_withdrawal(50000).make_withdrawal(60000).display_user_balance()

george.make_deposit(1000000).make_withdrawal(10000).make_withdrawal(10000).display_user_balance()

alfonso.transfer_money(george, 20000)
alfonso.display_user_balance()
george.display_user_balance()
