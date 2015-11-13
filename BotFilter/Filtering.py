__author__ = 'gatluri'
import twitter
import tweepy
from tweepy import OAuthHandler
import tweepy
import re
import time
consumer_key = 'q0FPYbzctolJ3tCwHc5PBd0IF'
consumer_secret = 'c1zshTpZ0YnoafJueyIpo6StrOTybcKLSqQsRlLbzVrjF0a83j'
access_token = '604340177-SH2zgSFwY3hT9NeTxGBgkBeE1fealGTHwVhb4EAN'
access_secret = 'nq00oY0Bxwv6LhvOdUxf2HUMYL0VTwanPakuVt4sjPduy'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

arr = []


idd = 91728131 #input valid Twitter id's here
try :
 User = api.get_user(idd)
 botScore = 0
 botScore1 = 0
 botScore2 = 0
 botScore3 = 0
 botScore4 = 0
 botScore5 = 0
 follower_ratio = User.followers_count/(User.friends_count+1)
 spamWords = ["follow", "rt and follow", "follow and rt"]
 matchExact = re.compile(r'%s' % '|'.join(spamWords), flags=re.IGNORECASE)
 if(follower_ratio <0.001):
   botScore1= botScore1+50;
 if(follower_ratio <0.01):
   botScore1 = botScore1+20;
 if(follower_ratio <0.1):
   botScore1 = botScore1+10;

 if(User.statuses_count < 50):
   botScore2 = botScore2+20;
 if(User.statuses_count < 100):
   botScore2 = botScore2+10;
 timeline = api.user_timeline(idd,count=20)

 for tweet in timeline:

  len1 = len(re.findall(r"#\S+",tweet.text))
  if(len1>3):  botScore3 = botScore3+10;
  len2 = len(re.findall(r"http\S+",tweet.text))
  if(len2>=1): botScore4 = botScore4+30;
  len3 = len(matchExact.findall(tweet.text))
  if(len3 >=1):
     botScore5 = botScore5+25;

 botScore= botScore1+botScore2+botScore3+botScore4+botScore5;
 print("Bot Score for Follower Ratio : "+str(botScore1))
 print("Bot Score for Status Count : "+str(botScore2))
 print("Bot Score for HashTags : "+str(botScore3))
 print("Bot Score for Http Links : "+str(botScore4))
 print("Bot Score for Tweet Content : "+str(botScore5))

 if(botScore <300):
  print("Total Bot Score: "+str(botScore))
  print("Valid User")
 else:
     print("Total Bot Score: "+str(botScore))
     print("Bot Detected")
except tweepy.error.TweepError:
 pass









