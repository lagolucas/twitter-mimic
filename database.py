import re
import database_auth


def insere_um(tweet, db):
    cursor = db.cursor()

    try:
        line = re.sub('"', '', tweet.full_text)

        sql = "INSERT INTO `tweets`.`mimic_tweets` (`idTweets`, `plain text`, `timestamp_tw`, `handle`, `retweets`, `favs`) VALUES (" \
              ""+tweet.id_str+", \""+ line +"\",\""+str(tweet.created_at)+"\" , \""+tweet.user.screen_name+"\", "+str(tweet.retweet_count)+", "+str(tweet.favorite_count)+");"
        try:
            cursor.execute(sql)
            return 1
        except Exception as E:
            print(E)
            return -1
    except Exception as E:
        print(E)


def insere_lista(tweets):
    db = database_auth.conecta_banco()
    for tweet in tweets:
        insere_um(tweet, db)
    db.commit()
    db.close()


def get_last_id():
    db = database_auth.conecta_banco()
    sql = "select max(idTweets) from mimic_tweets;"
    cursor = db.cursor()
    value = ""
    try:
        cursor.execute(sql)
        value = cursor.fetchone()
    except Exception as E:
        print(E)
    db.close()
    return value[0]


def recupera_ids(conta):
    sql = "select idTweets from mimic_tweets where handle = \""+conta+"\";"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        value = cursor.fetchall()
    except Exception as E:
        print(E)
    db.close()
    return value

