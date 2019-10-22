import pyodbc

class ConnectionManager():

    _DEFAULT_CONNECTION = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=example;UID=SA;PWD=1qaz@WSX" 

    def __init__(self, connection):
        self._connection = pyodbc.connect(self._get_connection(connection))
        self.cursor = self._connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exct_type, exce_value, traceback):
        self.cursor.close()
        del self.cursor
        self._connection.close()

    def _get_connection(self, connection):
        if connection == None:
            connection = self._DEFAULT_CONNECTION
        return connection