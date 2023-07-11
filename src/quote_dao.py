import sqlite3
from sqlite3 import Connection

class QuoteDAO:

    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def findQuoteByCharacter(character: str):
        pass

    def findQuoteByEpisode(episode: int):
        pass

    def findQuoteByCharacterAndEpisode(episode: int):
        pass
    
    def getConn(self) -> Connection:
        return self.conn

    def setConn(self, conn: Connection) -> None:
        self.conn = conn