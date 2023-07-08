from random import randint
import os
import sqlite3
import tweepy

CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

dbname = "./tweet_bot.db"

try:
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    cur.execute("select count(*) from Quotes;")
    sum_of_quotes = cur.fetchall()[0][0]

    def tweet():
        random_id = randint(1, sum_of_quotes)
        
        sql = "select * from (Quotes inner join Episodes on Quotes.episode = Episodes.id)"
        sql += "inner join Characters on Quotes.character = Characters.id where Quotes.id = "
        sql += str(random_id) + ";"
        
        cur.execute(sql)
        records = cur.fetchall()
        
        episode = records[0][4]
        title = records[0][5]
        character = records[0][7]
        quote = records[0][3]
        status = "{}\n───────────────\n{}\n第{}話「{}」".format(
            quote, character, episode, title
        )
        
        api.update_status(status)
        print(status)
        
    count = 0

    while count < 50:
        try:
            tweet()
        except tweepy.error.TweepError:
            count += 1
        else:
            break

except sqlite3.Error:
    print("database error occurred")
    exit(1)

finally:
    cur.close()
    conn.close()