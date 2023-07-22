from sqlite3 import Connection, Error
from connection_manager import ConnectionManager
from quote_dao import QuoteDAO
from quote import Quote

try: 
    conn: Connection = ConnectionManager.getConnection()
    quote_dao = QuoteDAO(conn)

    id: int = 1
    quote: Quote = quote_dao.findQuoteById(1)
    status: str = "{}\n───────────────\n{}\n第{}話「{}」".format(
                    quote.quote, quote.character, quote.episode, quote.title
                )
    print(status)

    sum_of_quotes: int = quote_dao.getSumOfQuotes()
    print(sum_of_quotes)

except Error:
    print("database error occurred")

finally:
    if conn != None:
        conn.close()