from sqlite3 import Connection, Cursor, Error
import sqlite3
from connection_manager import ConnectionManager


class QuoteDAO:

    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def findQuoteById(self, id: int):
        pass

    def findQuoteByCharacter(character: str):
        pass

    def findQuoteByEpisode(episode: int):
        pass

    def findQuoteByCharacterAndEpisode(episode: int):
        pass

    def getSumOfQuotes(self):
        sql: str = "SELECT COUNT(*) AS count FROM Quotes;"
        cur: Cursor = None
        result: tuple = ()

        try:
            self.conn = ConnectionManager.getConnection()
            cur = self.conn.cursor()
            cur.execute(sql)
            result = cur.fetchone()
            sum_of_quotes = result["count"]

        except Error:
            print("database error occurred")

        finally:
            if cur != None:
                cur.close()

        return sum_of_quotes
    
    def getConn(self) -> Connection:
        return self.conn

    def setConn(self, conn: Connection) -> None:
        self.conn = conn