__author__ = 'ddnyanmo'
import twitter
import tweepy
from tweepy import OAuthHandler
import tweepy
import re
import time
import logging

consumer_key = 'y2AklbQgjxgUL6tLczXKsb1gP'
consumer_secret = 'TRox57fTR5OJqVO03rcPsUdxnF4kSEPk9zNfoiMrN4tDfE0QdD'
access_token = '3977062212-svlA5fLYadx785RX7fweQVpyqNSs9jtrH4maKkC'
access_secret = 'glky6Tp0B07BlxhOG0rnuAYCOeuEajmXFARkgqvg0dNnX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
file = open("SacramentoIds.txt","r")

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
         ff = open("SacramentoFriendsList.txt","a")
         user1 = api.get_user(friend.id)
         ff.write(str(user_ids)+"\t"+user.screen_name+"\t"+str(user.location)+"\t"+str(friend.id)+"\t"+user1.screen_name+"\t"+str(user1.location))
         ff.write("\n")
 except(tweepy.error.TweepError, UnicodeEncodeError) as e:
    pass