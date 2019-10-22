import decimal
from example.infrastructure.data_access.contracts.iaccount_data_access import IAccountDataAccess
from example.infrastructure.data_access.mongodb_data_access.connection.connection_manager import ConnectionManager

class AccountDataAccess(IAccountDataAccess):

    def __init__(self, config=None):
        connection = self._get_connection(config.connection if config != None else None)
        self._bankingAccount = connection.database.bankingAccount

    def get_balance(self, banking_account):
        return self._mapper(self._bankingAccount.find_one({"CustomerId": banking_account.customer.id}))

    def update_balance(self, banking_account, money):
        # withdraw implementation here
        # withdraw implementation here
        # withdraw implementation here
        print str(money) + "$ update has been done in MongoDB. Customer: " + str(banking_account.customer.id)
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
        return decimal.Decimal(row["Balance"])

    def _get_connection(self, connection):
        return ConnectionManager(connection)