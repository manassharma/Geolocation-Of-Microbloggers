from collections import Counter
from collections import Counter
import glob
from time import sleep
import operator
import tweepy
import ast

hash_tags_collector = []

ip = "tweets_output/5444512_clean.txt"

file_io = open('tweets_output/5444512_hash_tags.txt', 'a')
print("Extracting Hash tags for 5444512")
with open(ip) as user_tweets:
    for tweet in user_tweets:
        words = tweet.split(' ')
        for i in range(0, len(words)):
            if words[i].startswith('#'):
                hash_tags_collector.append(words[i].lower())

print("Hash tags are recorded")
most_common_hashtags = Counter(hash_tags_collector).most_common()

if len(hash_tags_collector) == 0:
    print("User tweet corpus does not have any hash tags.")
file_io.close()


