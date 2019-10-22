import sys
import decimal

import example
from example.infrastructure.di.container_register import ContainerRegister
from example.interface.console.cmd.container_resolver import ContainerResolver
from example.application.dto.withdrawmoney_dto import WithDrawMoneyDto

_config = None
ContainerRegister.initialize(_config)

def withdraw_money(account_type, customer_id, money):
    try:
        app_service = _start_account_service()
        response = app_service.withdraw_money(_create_withdraw_dto(account_type, customer_id, money))
        return response
    except Exception as e:
        return str(e)

def _create_withdraw_dto(account_type, customer_id, money):
    return WithDrawMoneyDto(account_type, int(customer_id), decimal.Decimal(money))

def _start_account_service():
    return ContainerResolver.instance().get_account_service()