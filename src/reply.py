from random import randint
import os
import time
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
conn = sqlite3.connect(dbname)
cur = conn.cursor()

words = {
    "高咲": 1, "たかさき": 1, "タカサキ": 1, "takasaki": 1,
    "侑": 1, "ゆう": 1, "yu": 1, "ユウ": 1,
    
    "上原": 2, "うえはら": 2, "ウエハラ": 2, "uehara": 2,
    "歩夢": 2, "あゆ": 2, "アユ": 2, "ayu": 2,  
    "ぽむ": 2, "ポム": 2, "pomu": 2,
    
    "中須": 3, "なかす": 3, "ナカス": 3, "nakasu": 3,
    "かす": 3, "カス": 3, "kasu": 3,
    
    "桜坂": 4, "おうさか": 4, "オウサカ": 4, "osaka": 4,
    "しず": 4, "シズ": 4, "shizu": 4,
    
    "朝香": 5, "あさか": 5, "アサカ": 5, "asaka": 5,
    "果林": 5, "かり": 5, "カリ": 5, "kari": 5,
    
    "宮下": 6, "みやした": 6, "ミヤシタ": 6, "miyashita": 6,
    "愛": 6, "あい": 6, "アイ": 6, "ai": 6,
    
    "近江": 7,  "このえ": 7, "コノエ": 7, "konoe": 7,
    "彼方": 7, "かな": 7, "カナ": 7, "kana": 7,
    
    "優木": 8, "ゆうき": 8, "ユウキ": 8, "yuki": 8,
    "せつ": 8, "セツ": 8, "setsu": 8,
    
    "えま": 9, "エマ": 9,  "emma": 9,
    "ゔぇるで": 9, "ヴェルデ": 9, "verde": 9,
    
    "天王寺": 10, "てんのうじ": 10, "テンノウジ": 10, "tennoji": 10,
    "璃奈": 10, "りな": 10, "リナ": 10, "rina": 10,
    
    "三船": 11, "みふね": 11, "ミフネ": 11, "mifune": 11,
    "栞子": 11, "しお": 11, "シオ": 11, "shio": 11,
    
    "みあ": 12, "ミア": 12, "mia": 12,
    "ていらー": 12, "テイラー": 12, "taylor": 12,
    
    "鐘": 13, "しょう": 13, "ショウ": 13, "zhong": 13,
    "嵐珠": 13, "らん": 13, "ラン": 13, "lanzhu": 13,
    
    "中川": 14, "なかがわ": 14, "ナカガワ": 14, "nakagawa": 14,
    "菜々": 14, "なな": 14, "ナナ": 14, "nana": 14,
    
    "黒しずく": 15, "dark shizuku": 15,
    
    "演劇部部長": 16, "drama club president": 16,
    
    "はんぺん": 17, "hanpen": 17,
    
    "色葉": 18, "いろは": 18, "イロハ": 18, "iroha": 18,
    
    "今日子": 19, "きょうこ": 19, "キョウコ": 19, "kyoko": 19,
    
    "浅希": 20, "あさぎ": 20, "アサギ": 20, "asagi": 20,
    
    "遥": 21, "はるか": 21, "ハルカ": 21, "haruka": 21,
    
    "くりすてぃーな": 22, "クリスティーナ": 22, "christina": 22,
    
    "支倉": 23, "はせくら": 23, "ハセクラ": 23, "hasekura": 23,
    "かさね": 23, "カサネ": 23, "kasane": 23,
    
    "綾小路": 24, "あやのこうじ": 24, "アヤノコウジ": 24, "ayanokoji": 24,
    "姫乃": 24, "ひめの": 24, "ヒメノ": 24, "himeno": 24,
    
    "紫藤": 25, "しどう": 25, "シドウ": 25, "shido": 25,
    "美咲": 25, "みさき": 25, "ミサキ": 25, "misaki": 25,
    
    "副会長": 26, "vice president": 26,
    
    "書記": 27, "secretary": 27,
    
    "女子高生": 28, "high school girl": 28,
    
    "そうめん": 29, "somen": 29,
}

word_dupulicates = [
    ("ayumu", "yu"), ("黒しずく", "しず"), ("dark shizuku", "shizuku"),
    ("遥", "近江"), ("はるか", "このえ"), ("ハルカ", "コノエ"),
    ("haruka", "konoe"),
]

numbers = {
    "1": 1, "１": 1, "一": 1,
    "2": 2, "２": 2, "二": 2,
    "3": 3, "３": 3, "三": 3,
    "4": 4, "４": 4, "四": 4,
    "5": 5, "５": 5, "五": 5,
    "6": 6, "６": 6, "六": 6,
    "7": 7, "７": 7, "七": 7,
    "8": 8, "８": 8, "八": 8,
    "9": 9, "９": 9, "九": 9,
    "10": 10, "１０": 10, "十": 10,
    "11": 11, "１１": 11, "十一": 11,
    "12": 12, "１２": 12, "十二": 12,
    "13": 13, "１３": 13, "十三": 13,
}

number_dupulicates = [
    ("10", "1"), ("１０", "１"), ("11", "1"), ("１１", "１"), 
    ("十一", "十"), ("十一", "一"), ("12", "1"), ("12", "2"), 
    ("１２", "１"), ("１２", "２"), ("十二", "十"), ("十二", "二"),
    ("13", "1"), ("13", "3"), ("１３", "１"), ("１３", "３"), 
    ("十三", "十"), ("十三", "三"),
]
    
def reply():
    timeline = api.mentions_timeline(count=5)
    
    for status in timeline:
        mention_time = status.created_at.timestamp()
        
        # 本番用は 60
        if time.time() - mention_time < 10000000:
            status_id = status.id
            screen_name = status.author.screen_name
        else:
            continue
        
        character_ids = []
        episode_id = 0
        
        for word in words:
            isDuplicate = False
            
            if word in status.text.casefold():
                for word_dupulicate in word_dupulicates:
                    if word_dupulicate[0] in status.text.casefold() and word == word_dupulicate[1]:
                        isDuplicate = True
                if isDuplicate:
                    continue

                print("test")
            
                character_ids.append(words[word])
        
        for number in numbers:
            isDuplicate = False
            
            if number in status.text.casefold():
                for number_dupulicate in number_dupulicates:
                    if number_dupulicate[0] in status.text.casefold() and number == number_dupulicate[1]:
                        isDuplicate = True
                if isDuplicate:
                    continue
                
                episode_id = numbers[number]
                break

        print(character_ids)
        character_id = character_ids[randint(0, len(character_ids) - 1)]
            
        if character_id > 0 and episode_id > 0:
            count_sql = "select count(*) from Quotes where character = "
            count_sql += str(character_id) + " and episode = "
            count_sql += str(episode_id) + ";"
                    
            select_sql = "select * from (Quotes inner join Episodes on Quotes.episode = Episodes.id)"
            select_sql += "inner join Characters on Quotes.character = Characters.id where Characters.id = "
            select_sql += str(character_id) + " and Episodes.id = "
            select_sql += str(episode_id) + ";"
            
        elif character_id > 0:
            count_sql = "select count(*) from Quotes where character = "
            count_sql += str(character_id) + ";"
                    
            select_sql = "select * from (Quotes inner join Episodes on Quotes.episode = Episodes.id)"
            select_sql += "inner join Characters on Quotes.character = Characters.id where Characters.id = "
            select_sql += str(character_id) + ";"
            
        elif episode_id > 0:
            count_sql = "select count(*) from Quotes where episode = "
            count_sql += str(episode_id) + ";"
                    
            select_sql = "select * from (Quotes inner join Episodes on Quotes.episode = Episodes.id)"
            select_sql += "inner join Characters on Quotes.character = Characters.id where Episodes.id = "
            select_sql += str(episode_id) + ";"
        
        else:
            continue
        
        cur.execute(count_sql)
        sum_of_quotes = cur.fetchall()[0][0]
                
        cur.execute(select_sql)
        records = cur.fetchall()
                
        random_index = randint(0, sum_of_quotes - 1)
                
        episode = records[random_index][4]
        title = records[random_index][5]
        character = records[random_index][7]
        quote = records[random_index][3]
        status = "@{} {}\n───────────────\n{}\n第{}話「{}」".format(
            screen_name, quote, character, episode, title
        )

        api.update_status(status, in_reply_to_status_id=status_id)
        print(status)
        
    cur.close()
    conn.close()

reply()