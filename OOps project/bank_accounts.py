class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,initialAmount,acctName):
        self.balance=initialAmount
        self.name=acctName
        print(f"\n Account '{self.name}' created. \nBalance= ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance=$'{self.balance:.2f}'")
        
    def deposit(self,amount):
        self.balance+=amount
        print("\nDeposit complete")
        self.getBalance()

    def viabletransaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"\n Sorry ! ,Account '{self.name}' only has a balance of $'{self.balance:.2f}'")
    def withdraw(self,amount):
        try:
            self.viabletransaction(amount)
            self.balance-=amount
            print(f"\nWithdraw Complete.")
            self.getBalance()
        except BalanceException as error:    
            print(f"Withdraw interrupted: {error}")

    def transfer(self,amount,account):
        try:
            print('\n********\n\nBegining Transfer..')
            self.viabletransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n Transfer Complete ! \n\n*********")
        except BalanceException as error:
            print(f'\nTransfer interrupted.{error}')