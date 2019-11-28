import tweepy
import numpy

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = '963718534982459392-4y4zXIZVfVdGa3Xv3df9wo1XIfcqeKN'
ACCESS_SECRET = 'HF3ppnRfe95c3bzKKGN3Wpg9bMHNJck8smmUcyK6s3VQX'
CONSUMER_KEY = 'pNtfyCs4o7DIIWJoXjJjKfWWb'
CONSUMER_SECRET = 'LkO70LvTkL8cVgqhA8bFz9q3oTjtkvwgWViP4xgOb12k4C93Vn'


# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api


# Create API object
api = connect_to_twitter_OAuth()

# tweets from my stream
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)