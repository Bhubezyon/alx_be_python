# BankAccount class
class BankAccount:
    def __init__(self, account_number, account_owner, balance):
        self.account_owner = account_owner
        self.balance = balance

    def deposit(self, amount):
            self.balance += amount
            print(f"Deposited ${amount}")
            return True

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
        print(f"Current Balance: ${self.account_balance:.2f}")


