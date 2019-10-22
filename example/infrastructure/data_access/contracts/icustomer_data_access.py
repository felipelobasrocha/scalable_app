from abc import ABCMeta, abstractmethod

class ICustomerDataAccess():

    @abstractmethod
    def get_customer(self, customer_id): pass