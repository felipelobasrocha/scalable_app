from example.infrastructure.events.event_manager import EventManager
from example.domain.model.banking_account.checking_account import CheckingAccount
from example.domain.model.banking_account.investment_account import InvestmentAccount
from example.domain.model.banking_account.savings_account import SavingsAccount

class ApplicationFactory:

    _components = dict()

    def __init__(self):
        self._components["investment"] = InvestmentAccount
        self._components["savings"] = SavingsAccount
        self._components["checking"] = CheckingAccount

    def create_banking_account(self, account_type, account_number, customer):
        return self._components[account_type](account_number, customer, account_type)

    def create_banking_account_by_customer(self, account_type, customer):
        return self._components[account_type](0, customer, account_type)

    def create_event_manager(self):
        return EventManager.instance()        

    _instance = None

    @staticmethod
    def instance():
        if ApplicationFactory._instance is None:
            _instance = ApplicationFactory()
        
        return _instance            