import pyodbc
from example.infrastructure.data_access.contracts.iregulation_data_access import IRegulationDataAccess
from example.infrastructure.data_access.sql_server_data_access.connection.connection_manager import ConnectionManager

class RegulationDataAccess(IRegulationDataAccess):
  
    _GET_QUERY = "{CALL [example].[dbo].[GetMinimumAge]}"

    def __init__(self, config=None):
        self._config = config

    def get_minimum_age(self):
        with self._get_connection_factory(self._config.connection if self._config != None else None) as connection:
            connection.cursor.execute(self._GET_QUERY)
            return int(connection.cursor.fetchone().MinimumAge)

    def _get_connection_factory(self, connection):
        return ConnectionManager(connection)            