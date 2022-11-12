class BankAccount:
    def __init__(self, accountnumber, name, balance):
        self.accountnumber = accountnumber
        self.name = name
        self.balance = balance

    def Deposit(self):
        amount = float(input("Enter amout to be deposited: "))
        self.balance+=amount
        return(f"Your deposit of {amount} has been processed, your balance is : {self.balance}")

    def Withdrawal(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >=amount:
            self.balance-=amount
            return(f"Withrawal of {amount}is being processed, kindly take your cash")
        else:
            return("Your account balance is not sufficient for this transaction")
    def Bankfee(self):
        fee = self.balance * 0.05
        self.balance-=fee
        return(f"A fee of {fee} has been deducted from your account, Your balance is {self.balance}")

    def Display(self):
        return(f"Your account details is displayed below: \n Account number: {self.accountnumber} \n Account name: {self.name} \n Account balance: {self.balance}")
    
Account = BankAccount('0794801278', 'TOLULOPE ALADE', 20000.54)
# print(Account.Deposit())
# print(Account.Withdrawal())
# print(Account.Bankfee())
print(Account.Display())


