import sys
import decimal
import unittest
from mock import MagicMock

from example.tests.unit_tests.container_register import ContainerRegister
from example.interface.console.cmd.container_resolver import ContainerResolver

from example.domain.model.customer import Customer

class CustomerTest(unittest.TestCase):

    _customer = None

    def setup(self):
        self._customer = Customer(1, "Teste de Souza", "1980-12-12T00:01:00.000Z")
        self._minimum_age = 18

    def tearDown(self):
        pass

    def test_check_mininum_age_up(self):
        self.setup()
        self._customer._calculate_age = MagicMock(return_value=20)
        is_age_ok = self._customer.check_mininum_age(self._minimum_age)

        self.assertEqual(is_age_ok, True)

    def test_check_mininum_age_under(self):
        self.setup()
        self._customer._calculate_age = MagicMock(return_value=17)
        is_age_ok = self._customer.check_mininum_age(self._minimum_age)

        self.assertEqual(is_age_ok, False)