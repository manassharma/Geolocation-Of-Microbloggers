import tweepy
import time
import logging
import re
import string

#Authentication of Twitter API
auth = tweepy.OAuthHandler('m6uBb1lC3ddz1OTt4miidpm3P','Yd6hk6XFC58mWH1gHU3oRm5Bt1viWiQgWadajzeC4O9uuEO6gj')
auth.set_access_token('3841660274-snXbr0BBPb2TTdkqgmKVY8DkcW13sibj50br5hJ',
                                      'TDbRRPecfTgbpxv6h0xOWdkizrbWaqHEEItOLYhcWvhtl')
api = tweepy.API(auth)

logging_location = 'tweet_extraction.log'
logging.basicConfig(filename=logging_location,level=logging.DEBUG)

f_in=open("userids/input.txt","r")
user_id = f_in.read()
print "Extracting tweets for user-" + user_id + "from the top 20  pages"

time.sleep(300)
logging.debug("Extracted tweets of -"+str(user_id))
	
print "Extraction complete. Tweets stored at tweets_output/5444512.txt"
f_in.close()

	





