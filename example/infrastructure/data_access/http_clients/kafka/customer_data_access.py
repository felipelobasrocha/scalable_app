from kafka import KafkaConsumer
from kafka import KafkaProducer

from example.infrastructure.data_access.contracts.icustomer_data_access import ICustomerDataAccess

class CustomerDataAccess(ICustomerDataAccess):

    _DEFAULT_CONNECTION = "hnodevh002.hlg.bigdata.dc.nova:6667"
    _DEFAULT_TOPIC = "customer"

    _producer = None
    _consumer = None

    def __init__(self, connection=None):
        _producer = KafkaProducer(bootstrap_server=self._get_connection(connection))
        _consumer = KafkaConsumer(bootstrap_server=self._get_connection(connection))

    def get(self, customer_id):
        pass

    def set(self, customer):
        self._producer.send(self._DEFAULT_TOPIC, customer)

    def _get_connection(self, connection):
        if connection == None:
            connection = self._DEFAULT_CONNECTION
        return connection        