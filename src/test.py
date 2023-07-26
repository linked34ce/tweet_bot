from sqlite3 import Connection, Error
from connection_manager import ConnectionManager
from quote_dao import QuoteDAO
from quote import Quote

try: 
    conn: Connection = ConnectionManager.getConnection()
    quote_dao = QuoteDAO(conn)
    quote: Quote = None
    status: str = ""
    sum_of_quotes: int = 0
    character_id: int = 0
    quote_id: int = 0

    sum_of_quotes = quote_dao.get_sum_of_all_quotes()
    print("get_sum_of_all_quotes() -> " + str(sum_of_quotes))
    print()

    character_id = 1  # Yu
    sum_of_quotes = quote_dao.get_sum_of_quotes_by_character_id(character_id)
    print("get_sum_of_quotes_by_character_id() -> " + str(sum_of_quotes))
    print()

    quote_id = 1
    quote = quote_dao.find_quote_by_quote_id(quote_id)
    status = "{}\n───────────────\n{}\n第{}話「{}」".format(
                quote.quote, quote.character, quote.episode, quote.title
            )
    print(status)
    print()

    character_id = 2  # Ayumu
    quote = quote_dao.find_quote_by_character_id(character_id)

    status = "{}\n───────────────\n{}\n第{}話「{}」".format(
                quote.quote, quote.character, quote.episode, quote.title
            )
    print(status)

except Error:
    print("database error occurred")

finally:
    if conn != None:
        conn.close()