import sqlite3

dbname = "./tweet_bot.db"

try:
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    sqls = [
        "create table Episodes (id integer primary key autoincrement, title text not null);",
        "create table Characters (id integer primary key autoincrement, name text not null);",
        "create table Quotes (id integer primary key autoincrement, episode integer not null, character integer not null, quote integer not null);"
    ]

    for sql in sqls:
        cur.execute(sql)
        
    conn.commit()

except sqlite3.OperationalError:
    print("database already exists")
    exit(1)

except sqlite3.Error:
    print("database error occurred")
    exit(1)

finally:
    cur.close()
    conn.close()