__author__ = 'ddnyanmo'
__author__ = 'ddnyanmo'
import twitter
import tweepy
from tweepy import OAuthHandler
import tweepy
import re
import time
import logging


consumer_key = 'q0FPYbzctolJ3tCwHc5PBd0IF'
consumer_secret = 'c1zshTpZ0YnoafJueyIpo6StrOTybcKLSqQsRlLbzVrjF0a83j'
access_token = '604340177-SH2zgSFwY3hT9NeTxGBgkBeE1fealGTHwVhb4EAN'
access_secret = 'nq00oY0Bxwv6LhvOdUxf2HUMYL0VTwanPakuVt4sjPduy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
file = open("SanFranciscoIds.txt","r")

for line in file:
 try:
    line = line.split("	")[0]
    user_ids = line
    user = api.get_user(user_ids)
    print user.screen_name
    print user.location
    for friend in tweepy.Cursor(api.friends,user_id = user_ids).items():
         time.sleep(10)
         ff = open("SanFranciscoIdsFrndsFriendsList.txt","a")
         user1 = api.get_user(friend.id)
         ff.write(str(user_ids)+"\t"+user.screen_name+"\t"+str(user.location)+"\t"+str(friend.id)+"\t"+user1.screen_name+"\t"+str(user1.location))
         ff.write("\n")
 except(tweepy.error.TweepError, UnicodeEncodeError) as e:
    pass