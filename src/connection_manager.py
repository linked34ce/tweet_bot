import sqlite3
from sqlite3 import Connection

class ConnectionManager:

    DB_NAME = "./tweet_bot.db"

    @staticmethod
    def getConnection() -> Connection:

        conn: Connection = None

        try:
            conn = sqlite3.connect(ConnectionManager.DB_NAME)     

        except sqlite3.Error:
            print("database error occurred")

        return conn
