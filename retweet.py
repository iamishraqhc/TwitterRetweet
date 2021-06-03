# import dependencies
import tweepy
from streamlistener import StreamListener

from keysmain import *

API_KEY = twitter_api_key
API_SECRET = twitter_api_secret
ACCESS_TOKEN = twitter_access_token
ACCESS_TOKEN_SECRET = twitter_access_token_secret

# print("API KEY: " + API_KEY)
# print("API SECRET: " + API_SECRET)
# print("ACCESS TOKEN: " + ACCESS_TOKEN)
# print("ACCESS TOKEN SECRET: " + ACCESS_TOKEN_SECRET)

twitter_auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

twitter_api = tweepy.API(twitter_auth)

try:
    print(twitter_api.verify_credentials())
    print("Successfully logged in")

except tweepy.TweepError as e:
    print(e)

except Exception as e:
    print(e)

# instantiate a StreamListener object
tweets_listener = StreamListener(twitter_api)

# instantiate a tweepy.Stream object
tweet_stream = tweepy.Stream(twitter_api.auth, tweets_listener)

# use the filter method
tweet_stream.filter(track=["#100DaysofCode", "#ProgrammingLife", "#javascript", "#nodejs", "#pythondeveloper", "#javaprogramming"],
languages=["en"])
