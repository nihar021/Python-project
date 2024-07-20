from bank_accounts import *

Dave=BankAccount(1000,"Dave")
Sara=BankAccount(2000,"Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(600)
Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(500,Sara)
Dave.transfer(100000,Sara)