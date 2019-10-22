import decimal
from ibanking_account import IBankingAccount

class InvestmentAccount(IBankingAccount):

    def __init__(self, account_number, customer, type):
        self.customer = customer
        self.account_number = account_number
        self.type = type

    def withdraw(self, balance, money):
        balance = balance - (money - (money * decimal.Decimal(0.10)))

        if balance < 0:
            raise ValueError("Not enough cash.")
        return balance        

    def deposit(self, balance, money):
        return balance + money