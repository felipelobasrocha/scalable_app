import decimal
import json
from flask import Flask, request, jsonify

from example.interface.rest.flask.app import app
from example.interface.rest.flask.container_resolver import ContainerResolver
from example.infrastructure.di.container_register import ContainerRegister
from example.application.dto.withdrawmoney_dto import WithDrawMoneyDto

_config = None
ContainerRegister.initialize(_config)

@app.route('/withdraw', methods=['POST'])
def withdraw_money():
    try:
        if request.method == 'POST':
            request_data = json.loads(request.data)
            withdraw_dto = _create_withdraw_dto(request_data["account_type"], \
                                                request_data["customer_id"], request_data["money"])
            app_service = _start_account_service()
            response = app_service.withdraw_money(withdraw_dto)
            return jsonify(response)
    except Exception as e:
        return jsonify(str(e))

def _create_withdraw_dto(account_type, customer_id, money):
    return WithDrawMoneyDto(account_type, int(customer_id), decimal.Decimal(money))

def _start_account_service():
    return ContainerResolver.instance().get_account_service()