from sqlite3 import Connection, Cursor, Error
from connection_manager import ConnectionManager
from quote import Quote


class QuoteDAO:

    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def findQuoteById(self, id: int) -> Quote:
        sql: str = "select * from (Quotes inner join Episodes on Quotes.episode = Episodes.id) " \
                   "inner join Characters on Quotes.character = Characters.id where Quotes.id = ?;"
        cur: Cursor = None
        params: tuple = (id, )
        res: tuple = ()
        quote: Quote = None

        try:
            self.conn = ConnectionManager.getConnection()
            cur = self.conn.cursor()
            cur.execute(sql, params)
            res = cur.fetchone()
            quote = Quote(res["episode"], res["title"], res["character"], res["quote"])

        except Error:
            print("database error occurred")

        finally:
            if cur != None:
                cur.close()

        return quote

    def findQuoteByCharacter(character: str):
        pass

    def findQuoteByEpisode(episode: int):
        pass

    def findQuoteByCharacterAndEpisode(episode: int):
        pass

    def getSumOfQuotes(self) -> int:
        sql: str = "SELECT COUNT(*) AS count FROM Quotes;"
        cur: Cursor = None
        res: tuple = ()
        sum_of_quotes: int = 0

        try:
            self.conn = ConnectionManager.getConnection()
            cur = self.conn.cursor()
            cur.execute(sql)
            res = cur.fetchone()
            sum_of_quotes = res["count"]

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