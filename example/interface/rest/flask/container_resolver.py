from example.infrastructure.di.factory import Factory
from example.application.service.account_service import AccountService
from example.infrastructure.data_access.contracts.iaccount_data_access import IAccountDataAccess
from example.infrastructure.data_access.contracts.icustomer_data_access import ICustomerDataAccess
from example.infrastructure.data_access.contracts.iregulation_data_access import IRegulationDataAccess

class ContainerResolver:

    _factory = Factory()

    def __init__(self):
        pass

    def get_account_service(self):
        return AccountService(self._factory.create(IAccountDataAccess), \
                                self._factory.create(ICustomerDataAccess), self._factory.create(IRegulationDataAccess))

    _instance = None

    @staticmethod
    def instance():
        if ContainerResolver._instance is None:
            _instance = ContainerResolver()
        return _instance
