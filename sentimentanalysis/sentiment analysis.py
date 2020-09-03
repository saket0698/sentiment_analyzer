import tweepy
from textblob import TextBlob





consumer_key = ""
consumer_key_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

def percentage(part,whole):
    return 100 * float(part)/float(whole)

x = str(input("Enter Keyword"))
n = int(input("Enter number of tweets to be analyzed"))


tweets = tweepy.cursor(api.search,q=x).items(n)

positive,negative,neutral,polarity = 0


for tweet in tweets:
    
    print(tweet.text)
    
    analysis = TextBlob(tweet.text)
    pol = analysis.sentiment.polarity
    
    polarity + = pol

    
    if(pol>0):
        positive += 1
    elif(pol<0):
        negative += 1
    else:
        neutral += 1


positive = percentage(positive,n)
negative = percentage(negative,n)
neutral  = percentage(neutral,n)


print("people's reaction on" + x +" by analyzing" + n + " Tweets.")
if(polarity>0):
    print("Positive")
elif(polarity<0):
    print("Negative")
else:
    print("Neutral")

