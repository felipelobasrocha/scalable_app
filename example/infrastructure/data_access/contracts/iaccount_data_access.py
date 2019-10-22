from abc import ABCMeta, abstractmethod

class IAccountDataAccess:

    @abstractmethod
    def get_balance(self, banking_account): pass

    @abstractmethod
    def update_balance(self, banking_account, money): pass
