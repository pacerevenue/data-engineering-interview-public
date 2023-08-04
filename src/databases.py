import sqlite3
from typing import List


def dict_factory(cursor: sqlite3.Cursor, row: sqlite3.Row) -> dict:
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


class Database:

    DB_NAME = None
    SCHEMA_FILENAME = None

    def __init__(self) -> None:
        con = sqlite3.connect(self.DB_NAME)
        with open(self.SCHEMA_FILENAME) as stream:
            schema = stream.read()
        con.executescript(schema)
        con.close()

    def run_query(self, sql: str) -> List[dict]:
        con = sqlite3.connect(self.DB_NAME)
        con.row_factory = dict_factory
        cursor = con.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


class CustomerDatabase(Database):
    DB_NAME = "customers.db"
    SCHEMA_FILENAME = "customers.sql"
