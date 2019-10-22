import os
import sys

from example.infrastructure.di.factory import Factory
from example.infrastructure.events.event_manager import EventManager
from example.domain.events.account_deposit import AccountDeposit

from example.infrastructure.data_access.contracts.iaccount_data_access import IAccountDataAccess
from example.infrastructure.data_access.sql_server_data_access.account_data_access import AccountDataAcces as AccountSqlDataAccess
from example.infrastructure.data_access.mongodb_data_access.account_data_access import AccountDataAccess as AccountMongoDataAccess

from example.infrastructure.data_access.contracts.icustomer_data_access import ICustomerDataAccess
from example.infrastructure.data_access.sql_server_data_access.customer_data_access import CustomerDataAccess as CustomerSqlDataAccess
from example.infrastructure.data_access.mongodb_data_access.customer_data_access import CustomerDataAccess as CustomerMongoDataAccess

from example.infrastructure.data_access.contracts.iregulation_data_access import IRegulationDataAccess
from example.infrastructure.data_access.sql_server_data_access.regulation_data_access import RegulationDataAccess as RegulationSqlDataAccess
from example.infrastructure.data_access.mongodb_data_access.regulation_data_access import RegulationDataAccess as RegulationMongoDataAccess

class ContainerRegister:

    def __init__(self, config):
        self._config = config
        self._factory = Factory.instance()
        self._event_manager =  EventManager.instance()

    def _register(self):
        self._register_infrastructure()
        self._register_events()

    def _register_infrastructure(self):
        self._factory.register(IAccountDataAccess, AccountMongoDataAccess())
        self._factory.register(ICustomerDataAccess, CustomerSqlDataAccess(self._config))
        self._factory.register(IRegulationDataAccess, RegulationSqlDataAccess())

    def _register_events(self):
        self._event_manager.register(AccountDeposit, AccountSqlDataAccess())

    @staticmethod
    def initialize(config=None):
        ContainerRegister(config=None)._register()