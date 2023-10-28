class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0) :
        self. __account_number=account_number
        self. __account_holder_name=account_holder_name
        self. __account_balance=initial_balance
    def Deposit(self, amount):
       if amount>0:
           self. __account_balance+=amount
           print("Deposited ₹",amount,"New Balance ₹",self.__account_balance)
       else:
           print("Invalid Deposit")
    def withdraw (self, amount):
        if amount>0 and amount<=self.__account_balance :
            self. __account_balance-=amount
            print ("Withdraw ₹",amount,"Ac.Balance ₹",self.__account_balance)
        else:
            print ("Invalid Withdraw")
    def display_balance (self):
        print ("Account Balance For",self.__account_holder_name,"(Account No:",self.__account_number,")₹",self. __account_balance)
account=BankAccount(account_number=20040111,account_holder_name="Tamil",initial_balance=10000.00)
account. display_balance ()
account. Deposit (4000)
account. withdraw (5000)
account. display_balance ()