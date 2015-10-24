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
file = open("Texas_Frnd_Foll_Rel.txt","r")
for line in file:
 #try:

    user_ids = int(line)
    user = api.get_user(user_ids)
    print user.screen_name
    print user.followers_count
    for follower in tweepy.Cursor(api.followers,user_id = user_ids).items():
     if(user.followers_count > 100000):
        pass
     else:
         time.sleep(10)
         ff = open("TexasTarunFollowersList.txt","a")
         user1 =  api.get_user(follower.id)
         ff.write(str(user_ids)+"    "+str(follower.id)+"   "+str(user1.location)+"     "+user1.screen_name)
         ff.write("\n")

 #except(tweepy.error.TweepError,UnicodeEncodeError) as e:
    #pass