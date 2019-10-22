from example.infrastructure.data_access.contracts.icustomer_data_access import ICustomerDataAccess
from example.infrastructure.data_access.mongodb_data_access.connection.connection_manager import ConnectionManager
from example.domain.model.customer import Customer

class CustomerDataAccess(ICustomerDataAccess):

    def __init__(self, config=None):
        connection = self._get_connection(config.connection if config != None else None)
        self._customer = connection.database.customer

    def get_customer(self, customer_id):
        return self._mapper(self._customer.find_one({"CustomerId": customer_id}))

    def _mapper(self, document):
        return self._get_customer_factory(document["CustomerId"], document["Name"], document["BirthDate"])

    def _get_customer_factory(self, id, name, birth_date):
        return Customer(id, name, birth_date)

    def _get_connection(self, connection):
        return ConnectionManager(connection)