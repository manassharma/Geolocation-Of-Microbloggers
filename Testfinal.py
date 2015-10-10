from tweepy import OAuthHandler
import tweepy
import re
from string import punctuation
from nltk.corpus import stopwords
import string
import time

consumer_key = 'q0FPYbzctolJ3tCwHc5PBd0IF'
consumer_secret = 'c1zshTpZ0YnoafJueyIpo6StrOTybcKLSqQsRlLbzVrjF0a83j'
access_token = '604340177-SH2zgSFwY3hT9NeTxGBgkBeE1fealGTHwVhb4EAN'
access_secret = 'nq00oY0Bxwv6LhvOdUxf2HUMYL0VTwanPakuVt4sjPduy'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
stop = stopwords.words('english')

for status in tweepy.Cursor(api.home_timeline).items():
    #Converting tweets to lowercase
    status.text = status.text.lower()
    #removing http links in tweets
    status.text = re.sub(r"http\S+", "", status.text)
    #removing usernameids in tweets
    status.text = re.sub(r"@\S+", "", status.text)
    #removing citations
    status.text = re.sub(r'@[a-zA-Z0-9]*', '', status.text)
    # Puncuation contains !"#$%&'()*+,-./:;<=>?@[]^_`{|}~
    #Removing numbers
    status.text = re.sub(r'[0-9]*','',status.text)
    time.sleep(10)
    for tweet in list(punctuation):
        status.text = status.text.replace(tweet,'')

    #Remove Emojis
    try:
    # UCS-4
      highpoints = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
    # UCS-2
      highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
# mytext = u'<some string containing 4-byte chars>'
    status.text = highpoints.sub(u'\\u25FD', status.text)

    #removing stop words using nltk.corpus
    status.text = ' '.join([word for word in status.text.split() if word not in (stopwords.words('english'))])
    print(stopwords.words)
    #Tempfile =str(status.text)
    #Testfile = open("TestFile11243.csv", 'a')
    #Testfile.write(Tempfile)
    #Testfile.write('\n')
#    Testfile.close()