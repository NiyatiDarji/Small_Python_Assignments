# This program will use classes and have 4 basic banking operations
# Deposit, Withdraw, Balance and Transfer

class BankAccount:
    # Constructor
    def __init__(self):
        self.balance_amount = 0.00

    # Deposit amount in the account
    def deposit(self, amount):
        balance = self.balance()
        if amount > 0:
            balance = balance + amount
            self.balance_amount = balance
        else:
            print("The amount to deposit must be greater that zero.")

    # Withdraw amount from the account
    def withdraw(self, amount):
        balance = self.balance()
        if balance > amount:
            balance = balance - amount
            self.balance_amount = balance
        else:
            print("Cannot withdraw more than account balance.")

    # Check the balance in account
    def balance(self):
        return self.balance_amount

    # Transfer amount from account2 to account1: self is account1, account in the argument is account2
    def transfer(self, amount, account):
        self.deposit(amount)
        account.withdraw(amount)


# Unit testing
if __name__ == "__main__":
    bk1 = BankAccount()
    bk2 = BankAccount()
    print("Deposit $500 in account1 and $800 in account2:")
    bk1.deposit(500)
    bk2.deposit(800)
    print("Balance in account 1:", bk1.balance())
    print("Balance in account 2:", bk2.balance())
    print("Transfer $100 from account2 to account1:")
    bk1.transfer(100,bk2)
    print("Balance in account 1:", bk1.balance())
    print("Balance in account 2:", bk2.balance())
    print("Withdraw $50 from account1 as well as account2:")
    bk1.withdraw(50)
    bk2.withdraw(50)
    print("Balance in account 1:", bk1.balance())
    print("Balance in account 2:", bk2.balance())

