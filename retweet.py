# import dependencies
import tweepy

from keys import *

API_KEY = twitter_api_key
API_SECRET = twitter_api_secret
ACCESS_TOKEN = twitter_access_token
ACCESS_TOKEN_SECRET = twitter_access_token_secret

print("API KEY: " + API_KEY)
print("API SECRET: " + API_SECRET)
print("ACCESS TOKEN: " + ACCESS_TOKEN)
print("ACCESS TOKEN SECRET: " + ACCESS_TOKEN_SECRET)

twitter_auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

twitter_api = tweepy.API(twitter_auth)
