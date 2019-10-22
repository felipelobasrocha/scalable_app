from example.infrastructure.data_access.contracts.iaccount_data_access import IAccountDataAccess
from example.infrastructure.data_access.sql_server_data_access.connection.connection_manager import ConnectionManager

class AccountDataAcces(IAccountDataAccess):

    _GET_QUERY = "{CALL [example].[dbo].[GetBalance](@customer_id=?,@accountId=?,@accountType=?)}"

    def __init__(self, config=None):
        self._config = config

    def get_balance(self, banking_account):
        with self._get_connection(self._config.connection if self._config != None else None) as connection:
            connection.cursor.execute(self._GET_QUERY, \
                                (banking_account.customer.id,banking_account.account_number, banking_account.type))
            return self._mapper(connection.cursor.fetchone())

    def update_balance(self, banking_account, money):
        # withdraw implementation here
        # withdraw implementation here
        # withdraw implementation here
        print str(money) + "$ update has been done in Sql Server. Customer: " + str(banking_account.customer.id)
        # withdraw implementation here
        # withdraw implementation here        
        return self.get_balance(banking_account)

    def raise_event(self, event, domain_event, callback):
        try:
            account = event(domain_event)
            return self.update_balance(account, callback())
        except Exception as e:
            pass        

    def _mapper(self, row):
        return row.Balance

    def _get_connection(self, connection):
        return ConnectionManager(connection)        
