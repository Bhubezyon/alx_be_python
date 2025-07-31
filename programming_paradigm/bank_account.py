# BankAccount class
class BankAccount:
    def __init__(self, account_number, account_owner, balance=0):
        self.account_number = account_number
        self.account_holder = account_owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Withdrawal amount exceeds available balance.")
        return False

    def get_balance(self):
        return self.balance

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")


