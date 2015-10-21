import re
from string import punctuation
from nltk.corpus import stopwords
import string

tweetInfo = open("haggu.txt", "r")
mentionsFile = open("hagguWithoutStopWords.txt", "w")

stop = stopwords.words('english')
for status in tweetInfo:
    #Converting tweets to lowercase
    status = status.lower()
    #removing http links in tweets
    status = re.sub(r"http\S+", "", status)
    #removing citations
    status = re.sub(r'@[a-zA-Z0-9]*', '', status)
    # Puncuation contains !"#$%&'()*+,-./:;<=>?@[]^_`{|}~
    #time.sleep(10)
    for tweet in list(punctuation):
        status = status.replace(tweet,'')

    #Remove Emojis
    print status
    try:
    # UCS-4
      highpoints = re.compile(u'[\U00010000-\U0010ffff]')
    # UCS-2
      highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
# mytext = u'<some string containing 4-byte chars>'
      status = highpoints.sub(u'\\u25FD', status)
       
    #removing stop words using nltk.corpus
      status = ' '.join([word for word in status.split() if word not in (stopwords.words('english'))])
      mentionsFile.write(status)
    except Exception:
        print Exception
