# Twitter Retweet Bot using Python & Tweepy
A Python-built Twitter retweet bot using Tweepy. Searches and retweets based on hashtag or keyword. Can do multiple keywords, or hashtags.

What You Need && Need to Know
----------

* [Tweepy](http://www.tweepy.org/) - An easy-to-use Python library for accessing the Twitter API.

* Make sure you fully understand [Twitter's Rules on Automation](https://support.twitter.com/articles/76915). Play nice. Don't spam!

Instructions
----------

1. Create a New Twitter Account For Your Retweet Bot and Apply For [Twitter’s developer platform](https://developer.twitter.com/en)
2. Your application will take some time to be reviewed so wait for it. They might ask you some more questions in details so answer them neatly in points in as details as possible. Hopefully your application will be accepted within a day.
3. Once accepted, go to the [Twitter’s developer platform](https://developer.twitter.com/en) and login with the account you want to use for the bot purpose. Its best to create a profile for this purpose.
4. Once you log in to the developer portal, create a new project and generate the key, secret, access_token and access_token_secrets. Also change the app permission from read only to read + write. Its best that after changing the app permissions, regenerate the keys and tokens.
5. Start virtualenv and run the command "pip install -r requirements.txt".
6. Now create a file called keymain.py and include it in .gitignore so that if you push your code to git repository, it will not contain the keymain file.
7. I have created a keydemo.py file. Edit your keymain.py file according to this keydemo.py file. While editing, use your keys and tokens in the variables.
8. Then code your bot and test.
9. Run your script with the command "python retweet.py".