import sqlite3
from sqlite3 import Connection, Row, Error

class ConnectionManager:

    DB_NAME = "./tweet_bot.db"

    @staticmethod
    def getConnection() -> Connection:

        conn: Connection = None

        try:
            conn = sqlite3.connect(ConnectionManager.DB_NAME)
            conn.row_factory = Row   

        except Error:
            print("database error occurred")

        return conn
