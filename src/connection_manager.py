import sqlite3
from sqlite3 import Connection

class ConnectionManager:

    @staticmethod
    def getConnection() -> Connection:

        dbname = "./tweet_bot.db"

        try:
            conn = sqlite3.connect(dbname)     

        except sqlite3.Error:
            print("database error occurred")

        return conn
