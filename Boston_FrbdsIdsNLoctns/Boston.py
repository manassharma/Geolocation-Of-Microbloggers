__author__ = 'ddnyanmo'
import twitter
import tweepy
from tweepy import OAuthHandler
import tweepy
import re
import time
import logging

consumer_key = 'rh8GZgdV0ZoXbYg8rnppDqUWV'
consumer_secret = 'lkSF6LRFdDYSeuTC8p4wNSz5XopFaanGjtHy8QBi4Ry1GAreHu'
access_token = '3599330359-ygWHc9JIp0mCbaUv0Lgp0SlIx6ev6CljLC7nj5J'
access_secret = '24b4rhtJ2t8Zt8JAVNMcgR4NfM9sigRF5KUl3qRsS9PEX'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
file = open("BostonIds.txt","r")

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
         ff = open("BostonFriendsList.txt","a")
         user1 = api.get_user(friend.id)
         ff.write(str(user_ids)+"\t"+user.screen_name+"\t"+str(user.location)+"\t"+str(friend.id)+"\t"+user1.screen_name+"\t"+str(user1.location))
         ff.write("\n")
 except(tweepy.error.TweepError, UnicodeEncodeError) as e:
    pass