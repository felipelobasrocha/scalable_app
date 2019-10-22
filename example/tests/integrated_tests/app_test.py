import sys
import decimal
import unittest

from example.tests.integrated_tests.container_register import ContainerRegister
from example.interface.console.cmd.container_resolver import ContainerResolver
from example.application.dto.withdrawmoney_dto import WithDrawMoneyDto


class AppTest(unittest.TestCase):

    def setup(self):
        pass
    def tearDown(self):
        pass        

    def test_account_service_withdraw(self):

        account_type = "checking"
        customer_id = 1
        money = decimal.Decimal(10.0)

        self.setup()

        ContainerRegister.initialize()
        app_service = ContainerResolver.instance().get_account_service()    

        response = app_service.withdraw_money(self._create_withdraw_dto(account_type, customer_id, money))
        self.assertEqual("You withdraw $" in str(response), True)

    def test_account_service_deposit(self):

        account_type = "savings"
        customer_id = 1
        money = decimal.Decimal(10.0)

        self.setup()

        ContainerRegister.initialize()
        app_service = ContainerResolver.instance().get_account_service()    

        response = app_service.deposit_money(self._create_withdraw_dto(account_type, customer_id, money))
        self.assertEqual("You deposit $" in str(response), True)

    def _create_withdraw_dto(self, account_type, customer_id, money):
        return WithDrawMoneyDto(account_type, int(customer_id), decimal.Decimal(money))