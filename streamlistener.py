# import dependencies
from time import sleep
import tweepy

# create new class "StreamListener" 
# takes in tweepy.StreamListener as a parameter
class StreamListener(tweepy.StreamListener):
  def __init__(self, api):
    self.api = api
    self.me = api.me()
  
  # the function containing the logic on what to do for each tweet
  def on_status(self, tweet):
    # We only want the bot to retweet original tweets, not replies.
    # We also don't want the bot to retweet itself
    if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
      return

    # If we haven't retweeted this tweet yet, retweet it   
    if not tweet.retweeted:
      try: 
        tweet.retweet()
        print("Tweet retweeted successfully")
        sleep(10)
      except Exception as e:
        print(e)

    # If we haven't favorited this tweet yet, favorite it
    if not tweet.favorited:
      try:
        tweet.favorite()
        print("Tweet favorited successfully")
      except Exception as e:
        print(e)

  # the function containing the logic in case there is an error  
  def on_error(self, status):
    print(f"Error while retweeting: {status}")
