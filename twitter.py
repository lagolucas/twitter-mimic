import tweepy
import twitter_auth
import database
import comparador


def lista_tweets(conta, last_tweet):
    api = twitter_auth.autentica()

    tweets = []

    for status in tweepy.Cursor(api.user_timeline, id=conta,  tweet_mode='extended', since_id=last_tweet).items():
        tweets.append(status)

    database.insere_lista(tweets)


def get_all(conta):
    api = twitter_auth.autentica()

    tweets = []

    for status in tweepy.Cursor(api.user_timeline, id=conta,  tweet_mode='extended').items():
        tweets.append(status)

    return tweets


def tweet(text):
    api = twitter_auth.autentica()
    api.update_status(text)
