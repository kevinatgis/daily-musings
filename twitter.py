# twitter playground
# kevinatgis
# tweepy: https://github.com/tweepy/tweepy

import tweepy
import sys

# static
consumer_key = sys.argv[1]
consumer_secret = sys.argv[2]
access_token = sys.argv[3]
access_token_secret = sys.argv[4]

# oauth info
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# oauth
twitter = tweepy.API(auth)

# print all tweets
public_tweets = twitter.home_timeline()
for tweets in public_tweets:
	print(tweets)