from mysql.connector import (connection)
from mysql.connector.types import ParamsSequenceOrDictType
from app.core.config import Config


class ORM:
    def __init__(self):
        self.cnx = connection.MySQLConnection(host=Config.DB_HOST,
                                              user=Config.DB_USER,
                                              password=Config.DB_PASSWORD,
                                              database=Config.DB_DATABASE,
                                              port=Config.DB_PORT)

    def __del__(self):
        self.cnx.close()

    def commit(self):
        self.cnx.commit()

    def rollback(self):
        self.cnx.rollback()

    def close(self):
        self.cnx.close()

    def insert(self, values: str, tables: str, params: ParamsSequenceOrDictType | None = None):
        cursor = self.cnx.cursor()
        query = f"INSERT INTO {tables} VALUES ({values})"
        cursor.execute(query, params)
        self.commit()
        return cursor.lastrowid

    def update(self, values: str, tables: str, where: str, params: ParamsSequenceOrDictType | None = None):
        cursor = self.cnx.cursor()
        query = f"UPDATE {tables} SET {values} WHERE {where}"
        cursor.execute(query, params)
        self.commit()
        return cursor.rowcount

    def delete(self, tables: str, where: str, params: ParamsSequenceOrDictType | None = None):
        cursor = self.cnx.cursor()
        query = f"DELETE FROM {tables} WHERE {where}"
        cursor.execute(query, params)
        self.commit()
        return cursor.rowcount

    def select(self, columns: str, tables: str, where: str | None = None, params: ParamsSequenceOrDictType | None = None):
        cursor = self.cnx.cursor()
        query = f"SELECT {columns} FROM {tables}"
        if where:
            query += f" WHERE {where}"
        cursor.execute(query, params)
        return cursor.fetchall()

    def execute(self, query: str, params: ParamsSequenceOrDictType | None = None):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        return cursor
