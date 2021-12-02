
class BankAccount:
    #don't forget to add some default values to thesr parameters!
    def __init__(self, int_rate=0, balance=0):
        self.interest=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if amount > self.balance:
            print("Insuffucient funds: Charginga $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        self.balance
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:    
            self.balance = self.balance + self.balance * self.interest
        return self

Account1=BankAccount(.01, 0)
Account2=BankAccount(.01, 0)
Account1.deposit(300).deposit(300).deposit(50).withdraw(100).yield_interest().display_account_info()
Account2.deposit(500).deposit(2500).withdraw(300).withdraw(750).withdraw(200).withdraw(600).yield_interest().display_account_info()