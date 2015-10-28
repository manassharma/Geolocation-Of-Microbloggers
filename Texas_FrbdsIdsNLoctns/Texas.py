__author__ = 'ddnyanmo'
import twitter
import tweepy
from tweepy import OAuthHandler
import tweepy
import re
import time
import logging

consumer_key = 'xCoBy6T0aXnJe9Jn6oNIDlpmH'
consumer_secret = '8rJTXj4qYdjO3HtiUb90YDDeYWkvMrdCHxJVtTo9TgIsGNMxqU'
access_token = '91728131-2NzvkCWqr5wMYab6eHpUJSsHeh3REGCmS3Wqzst3S'
access_secret = 'GGau71GdBZEMMO26uaLWuvA42KNTTEE9nCuhvsf3NsoIM'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
file = open("TexasIds.txt","r")

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
         ff = open("TexasFriendsList.txt","a")
         user1 = api.get_user(friend.id)
         ff.write(str(user_ids)+"\t"+user.screen_name+"\t"+str(user.location)+"\t"+str(friend.id)+"\t"+user1.screen_name+"\t"+str(user1.location))
         ff.write("\n")
 except(tweepy.error.TweepError, UnicodeEncodeError) as e:
    pass