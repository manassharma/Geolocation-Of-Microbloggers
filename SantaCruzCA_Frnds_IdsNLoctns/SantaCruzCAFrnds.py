__author__ = 'ddnyanmo'
import twitter
import tweepy
from tweepy import OAuthHandler
import tweepy
import re
import time
import logging

consumer_key = 'x3Qf9Lf1htNSKAaTS9oN6wcIO'
consumer_secret = 'vB1srpMswQpzZdEO3uni1Mer0AMG1l14bU5KoJvxuAgtfvVJhh'
access_token = '3977139434-N5yWPkH20aGOSCTuo95vCDQjgN1aQMDypnBq5YL'
access_secret = 'gkrfQRteRCh6dJTh9IC6UTGjUO9RUXgSVdCZKR4O8lbxb'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
file = open("Santacruzids.txt","r")

for line in file:
 try:
    line = line.split("	")[0]
    print line
    user_ids = int(line)
    user = api.get_user(user_ids)
    print user.screen_name
    print user.location
    for friend in tweepy.Cursor(api.friends,user_id = user_ids).items():
         time.sleep(10)
         ff = open("SantaCruzFrndsFriendsList.txt","a")
         user1 = api.get_user(friend.id)
         ff.write(str(user_ids)+"\t"+user.screen_name+"\t"+str(user.location)+"\t"+str(friend.id)+"\t"+user1.screen_name+"\t"+str(user1.location))
         ff.write("\n")
 except(tweepy.error.TweepError, UnicodeEncodeError) as e:
    pass