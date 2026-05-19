
class BankAccount:

    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"₹{amount} deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"₹{amount} withdrawn successfully")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Current Account Balance:", self.balance)

    def account_details(self):

        print("\n       Account Details       ")
        print("Account Holder :", self.account_holder)
        print("Account Number :", self.account_number)
        print("Current Balance:", self.balance)

acc1 = BankAccount("Shimna", 123456789, 5000)

acc1.account_details()
acc1.deposit(2000)
acc1.withdraw(3000)
acc1.display_balance()
acc1.withdraw(10000)

