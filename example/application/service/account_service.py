from example.application.factory.application_factory import ApplicationFactory
from example.domain.events.account_deposit import AccountDeposit

class AccountService:

    _account_data_access = None
    _customer_data_access = None
    _regulation_data_access = None
    _app_factory = ApplicationFactory.instance()

    def __init__(self, account_data_access, customer_data_access, regulation_data_access):
        self._account_data_access = account_data_access
        self._customer_data_access = customer_data_access
        self._regulation_data_access = regulation_data_access
        self._event_trigger = self._app_factory.create_event_manager()

    def withdraw_money(self, request):
        try:
            customer = self._customer_data_access.get_customer(request.customer_id)
            minimum_age = self._regulation_data_access.get_minimum_age()

            if not customer.check_mininum_age(minimum_age):
                raise ValueError("The minimum required age is " + minimum_age)
                
            banking_account = self._app_factory.create_banking_account_by_customer(request.account_type, customer)

            balance = self.get_balance(banking_account)
            balance = banking_account.withdraw(balance, request.money)
            balance = self._account_data_access.update_balance(banking_account, request.money)

            response = "You withdraw $" + str(request.money) + " and now your balance is $" + str(balance)
            return response
        except Exception as e:
            return '##################Error################## ' + e.message

    def deposit_money(self, request):
        try:
            customer = self._customer_data_access.get_customer(request.customer_id)
            banking_account = self._app_factory.create_banking_account_by_customer(request.account_type, customer)

            balance = self.get_balance(banking_account)
            balance = banking_account.deposit(balance, request.money)
            self._event_trigger.raise_event(AccountDeposit, banking_account, lambda money=None : request.money)

            response = "You deposit $" + str(request.money) + " and now your balance is $" + str(balance)
            return response
        except Exception as e:
            return '##################Error################## ' + e.message        

    def get_balance(self, banking_account):
        return self._account_data_access.get_balance(banking_account)