import tweepy
from time import sleep
from opener import *

#Gain authentication
auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api= tweepy.API(auth)

#Retweet
for tweet in tweepy.Cursor(api.search, q='#ikokazike').items(5):
	try:
		print('\nTweet by @' + tweet.user.screen_name)
		tweet.retweet()
		print('Retweet done')

		if not tweet.user.following:
			tweet.user.follow()
			print('Follow user')

		sleep(600)

	except tweepy.TweepError as e:
		print(e.reason)

	except StopIteration:
		break

