import tweepy
from textblob import TextBlob
consumer_key = ""
consumer_key_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)


auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

x = str(input("Enter Keyword"))
public_tweets = api.search(x)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if(analysis.sentiment[0]>0):
        print("positive")
    elif(analysis.sentiment[0]<0):
        print("negative")
    else:
        print("neutral")
