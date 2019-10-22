from example.infrastructure.data_access.contracts.icustomer_data_access import ICustomerDataAccess
from example.infrastructure.data_access.sql_server_data_access.connection.connection_manager import ConnectionManager
from example.domain.model.customer import Customer

class CustomerDataAccess(ICustomerDataAccess):
   
    _GET_QUERY = "{CALL [example].[dbo].[GetCustomer](@customer_id=?)}"

    def __init__(self, config=None):
        self._config = config

    def get_customer(self, customer_id):
        with self._get_connection(self._config.connection if self._config != None else None) as connection:
            connection.cursor.execute(self._GET_QUERY, (customer_id))
            return self._mapper(connection.cursor.fetchone())

    def _mapper(self, row):
        return self._get_customer_factory(row.CustomerId, row.Name, row.BirthDate)

    def _get_customer_factory(self, id, name, birth_date):
        return Customer(id, name, birth_date)

    def _get_connection(self, connection):
        return ConnectionManager(connection)

