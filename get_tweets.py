import twitter, database


def get_all(arrobas):
    last_tweet = database.get_last_id()
    for arroba in arrobas:
        print(arroba)
        twitter.lista_tweets(arroba, last_tweet)
