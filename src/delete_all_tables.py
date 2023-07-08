import sqlite3

dbname = "./tweet_bot.db"

conn = sqlite3.connect(dbname)

cur = conn.cursor()

sqls = [
    "drop table Episodes",
    "drop table Characters;",
    "drop table Quotes;"
]

for sql in sqls:
    conn.execute(sql)

conn.commit()

cur.close()
conn.close()