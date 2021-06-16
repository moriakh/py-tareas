class BankAccount:
    def __init__(self, yld_rate, balance):
        self.yld_rate = yld_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance<amount:
            print("You got not enough money!")
        else:
            self.balance -= amount
        return self

    def display_account_info(self, user):
        print(f'Hi {user.name} You got ${self.balance}')
        return self

    def yield_interest(self):
        self.balance += self.balance * self.yld_rate
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {1: BankAccount(0.02, 0)}

    def make_deposit(self, account, amount):
        self.accounts[account].deposit(amount)
        return self
    
    def make_withdraw(self, account, amount):
        self.accounts[account].withdraw(amount)
        return self
    
    def display_user_balance(self, account=0):
        if account!=0:
            print(f"Account # {account}: ")
            self.accounts[account].display_account_info(self)
        else:
            for account in self.accounts:
                print(f"Account # {account}: ")
                self.accounts[account].display_account_info(self)
        return self

    def new_account(self, cod, int_rate=0.02, amount=0):
        if cod in self.accounts:
            print(f"The account # {cod} already exists")
        else:
            self.accounts[cod] = BankAccount(int_rate, amount)
        return self

    def delete_account(self, account):
        if self.accounts[account].balance > 0:
            print("If you want to delete the account # {account} you have to transfer the current balance (${self.accounts[account].balance}) to other account")
            print("Do you want to transfer to another account [y/n]?")
            # incorporar input, lectura de y/n, cuenta de destino, eliminación de la cuenta y elminación directa en else
        return self

    def rename_account(self):
        return self

    def transfer_money(self, origin_account, destiny_user, destiny_account, amount):
        if self.accounts[origin_account].balance < amount:
            print('You got not enough money')
        else:
            self.accounts[origin_account].withdraw(amount)
            destiny_user.accounts[destiny_account].deposit(amount)
            print(f"You have transferred ${amount} to {destiny_user.name}")
            print(f"The current balance of Account # {origin_account} is ${self.accounts[origin_account].balance}\n")
        return self



moriak = User('Moriak', 'moriak@growthzilla.tk')
tamara = User('Tamara', 'tamara@oldschoolgirl.uk')

moriak.accounts[1].deposit(304030).deposit(34001).deposit(203133).withdraw(50330).yield_interest()
tamara.accounts[1].deposit(304030).deposit(34001).deposit(203133).withdraw(50330).yield_interest()

moriak.new_account(2)
tamara.new_account(2)

moriak.make_deposit(2, 300)
tamara.make_deposit(2, 600)

moriak.transfer_money(2, tamara, 2, 300)
tamara.transfer_money(1, moriak, 2, 5000)

moriak.new_account(2)