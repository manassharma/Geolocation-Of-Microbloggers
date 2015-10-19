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
f = open('OhioUsers.txt','r+')
count=0

for line in f:
        global count
        count = count+1
        if(count%25==0):
             time.sleep(60);
        idd = int(filter(str.isdigit, line))


        try :
            User = api.get_user(idd)

            botScore = 0

            follower_ratio = User.followers_count/(User.friends_count+1)
            spamWords = ["follow", "rt and follow", "follow and rt"]
            matchExact = re.compile(r'%s' % '|'.join(spamWords), flags=re.IGNORECASE)
            if(follower_ratio <0.001):
              botScore= botScore+50;
            if(follower_ratio <0.01):
              botScore = botScore+20;
            if(follower_ratio <0.1):
              botScore = botScore+10;

            if(User.statuses_count < 50):
              botScore = botScore+20;
            if(User.statuses_count < 100):
              botScore = botScore+10;
            timeline = api.user_timeline(idd,count=5)
            for tweet in timeline:

              len1 = len(re.findall(r"#\S+",tweet.text))
              if(len1>3):  botScore = botScore+10;
              len2 = len(re.findall(r"http\S+",tweet.text))
              if(len2>=1): botScore = botScore+20;
              len3 = len(matchExact.findall(tweet.text))
              if(len3 >=1):
               botScore = botScore+25;

            if(botScore <125):
               ff=open('valid_Ohio_users.txt','a')
               print(line)
               ff.write(str(line))
               ff.write('\n')
        except tweepy.error.TweepError:
            pass








