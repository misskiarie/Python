class BankAccount:
    def __init__(self,account_number, holder_name, balance=0):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >=amount:
           self.balance -=amount
        else:
            print("insufficient funds")
    def display_balance(self):
        print(f"Account number : {self.account_number}")
        print(f"Holder : {self.holder_name}")
        print(f"Balance : {self.balance}")
myaccount=BankAccount("1234567","Joy", 10000000000)
myaccount.display_balance()
myaccount.deposit(2000000000)
myaccount.display_balance()
myaccount.withdraw(500000)
myaccount.display_balance()