class Bank:
    def __init__(self):
        self.amount = 0.0

    def main(self):
        print("DeskBank app")
        print(self.amount)

    def deposit(self):
        print("Enter a deposit amount")
        deposit = float(input())
        self.amount = self.amount + deposit
        print(f"Amount deposited is: {deposit}" )
        print(f"Current balance is: {self.amount}")

    def withdraw(self):
        print("Enter amount to withdraw")
        withdraw = float(input())
        if (self.amount>=withdraw):
            self.amount = self.amount - withdraw
        else:
            print("You dont have enough balance to withdraw")
        print(f"Current balance is: {self.amount}")



bank = Bank()
bank.main()
bank.deposit()
bank.withdraw()