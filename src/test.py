import sqlite3
from sqlite3 import Connection, Error
from connection_manager import ConnectionManager
from quote_dao import QuoteDAO

try: 
    conn: Connection = ConnectionManager.getConnection()
    quote_dao = QuoteDAO(conn)
    sum_of_quotes: int = quote_dao.getSumOfQuotes()
    print(sum_of_quotes)

except Error:
    print("database error occurred")

finally:
    if conn != None:
        conn.close()