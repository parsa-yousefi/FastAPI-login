from databases import Database
from typing import Optional


class DatabaseConnectionManager:
    def __init__(self):
        self._database: Optional[Database] = None

    async def get_impala_connection(self):
        if self._database is None:
            self._database = Database('jdbc:hive2://host.example.com:21050/;auth=noSasl')

    def mysql_connection(self):
        if self._database is None:
            self._database = Database("mysql+pymysql://root:D@rkdawnte1376@localhost/fastapi")

    async def db_start(self):
        if self._database:
            await self._database.connect()

    async def db_stop(self):
        if self._database:
            await self._database.disconnect()

    def get_db(self):
        return self._database


db_manager = DatabaseConnectionManager()

