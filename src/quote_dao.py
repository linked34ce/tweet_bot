from random import randint
from sqlite3 import Connection, Cursor, Error
from connection_manager import ConnectionManager
from quote import Quote


class QuoteDAO:

    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def find_quote_by_quote_id(self, quote_id: int) -> Quote:
        sql: str = "SELECT * FROM (Quotes INNER JOIN Episodes ON Quotes.episode = Episodes.id) " \
                   "INNER JOIN Characters ON Quotes.character = Characters.id WHERE Quotes.id = ?;"
        cur: Cursor = None
        params: tuple = (quote_id, )
        res: tuple = ()
        quote: Quote = None

        try:
            self.conn = ConnectionManager.getConnection()
            cur = self.conn.cursor()

            cur.execute(sql, params)
            res = cur.fetchone()
            
            quote = Quote(res["episode"], res["title"], res["name"], res["quote"])

        except Error:
            print("database error occurred")

        finally:
            if cur != None:
                cur.close()

        return quote

    def find_quote_by_character_id(self, character_id: int) -> Quote:
        sql: str = "SELECT * FROM (Quotes INNER JOIN Episodes ON Quotes.episode = Episodes.id) " \
                   "INNER JOIN Characters ON Quotes.character = Characters.id WHERE Characters.id = ?;"
        cur: Cursor = None
        params: tuple = (character_id, )
        sum_of_quotes: int = 0
        random_index: int = 0
        res: tuple = ()
        quote: Quote = None

        try:
            self.conn = ConnectionManager.getConnection()
            cur = self.conn.cursor()

            sum_of_quotes = self.get_sum_of_quotes_by_character_id(character_id)
            random_index = randint(0, sum_of_quotes - 1)

            cur.execute(sql, params)
            res = cur.fetchall()[random_index]
            
            quote = Quote(res["episode"], res["title"], res["name"], res["quote"])

        except Error:
            print("database error occurred")

        finally:
            if cur != None:
                cur.close()

        return quote

    def find_quote_by_episode(self, episode: int):
        pass

    def find_quote_by_character_id_and_episode(self, character_id: int, episode: int):
        pass

    def get_sum_of_all_quotes(self) -> int:
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
    
    def get_sum_of_quotes_by_character_id(self, character_id: int) -> int:
        sql: str = "SELECT COUNT(*) AS count FROM Quotes WHERE character = ?;"
        cur: Cursor = None
        params: tuple = (character_id, )
        res: tuple = ()
        sum_of_quotes: int = 0

        try:
            self.conn = ConnectionManager.getConnection()
            cur = self.conn.cursor()

            cur.execute(sql, params)
            res = cur.fetchone()

            sum_of_quotes = res["count"]

        except Error:
            print("database error occurred")

        finally:
            if cur != None:
                cur.close()

        return sum_of_quotes
    
    def get_sum_of_quotes_by_episode(self, episode: int) -> int:
        pass

    def get_sum_of_quotes_by_character_id_and_episode(self, character_id: int, episode: int) -> int:
        pass
    
    def getConn(self) -> Connection:
        return self.conn

    def setConn(self, conn: Connection) -> None:
        self.conn = conn