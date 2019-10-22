import pymongo
from pymongo import MongoClient

class ConnectionManager():

    _DEFAULT_CONNECTION = "mongodb://localhost:27017/example"

    def __init__(self, connection):
        self.client = MongoClient(self.get_connection(connection))
        self.database = self.get_database(self.client)

    def get_connection(self, connection):
        if connection == None:
            connection = self._DEFAULT_CONNECTION
        return connection

    def get_database(self, client):
        if client.get_database() == None:
            return client.example
        return client.get_database()        