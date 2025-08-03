import sys
from bank_account import BankAccount

def __init__(self, account_owner= "User", initial_balance= 0):
    self.account_owner = account_owner # Example account number
    self.balance = initial_balance 
    deposited: 67 
    # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command> : <amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

        command, *params = sys.argv[1].split(':')
        amount = float(params[0]) if params else None

        if command == "deposit" and amount is not None:

            account.deposit(amount)
            print(f"Deposited: ${amount} ")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds. ")
        elif command == "display":
         account.display_balance()
    else:
            print("Invalid command. ")
            if __name__ == "__main__":
                account = BankAccount("Calvin", 250)
                account.display_balance()