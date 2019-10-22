import sys
import decimal

from example.infrastructure.di.container_register import ContainerRegister
from example.interface.console.cmd.container_resolver import ContainerResolver
from example.application.dto.withdrawmoney_dto import WithDrawMoneyDto

_config = None
ContainerRegister.initialize(_config)

def main():
    service_type = sys.argv[1]
    account_type = sys.argv[2]
    customer_id = sys.argv[3]
    money = sys.argv[4]

    if service_type == "WITHDRAW":
        app_service = _start_account_service()
        print app_service.withdraw_money(_create_withdraw_dto(account_type, customer_id, money))
    else:
        print "No service has been chosen"

def _create_withdraw_dto(account_type, customer_id, money):
    return WithDrawMoneyDto(account_type, int(customer_id), decimal.Decimal(money))

def _start_account_service():
    return ContainerResolver.instance().get_account_service()