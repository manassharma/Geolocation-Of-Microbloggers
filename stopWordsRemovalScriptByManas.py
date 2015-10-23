import re
from string import punctuation
from nltk.corpus import stopwords
import string

print "Enter the input file location"
inputFilePath = raw_input()

print "Enter the output path name and location"
outputFilePath = raw_input()

tweetList = open(inputFilePath, "r")
processedFile = open(outputFilePath, "w")

stopWordsMap = stopwords.words('english')

# Iterating through the tweets file and removing stop words
for currentTweet in tweetList:
    #Converting tweets to lowercase
    currentTweet = currentTweet.lower()
    #removing http links in tweets
    currentTweet = re.sub(r"http\S+", "", currentTweet)
    #removing citations
    currentTweet = re.sub(r'@[a-zA-Z0-9]*', '', currentTweet)
    # Puncuation contains !"#$%&'()*+,-./:;<=>?@[]^_`{|}~
    #time.sleep(10)
    for tweet in list(punctuation):
        currentTweet = currentTweet.replace(tweet,'')
    try:
        currentTweet = ' '.join([word for word in currentTweet.split() if word not in stopwords.words("english")])
        processedFile.write(currentTweet + "\n")
    except Exception:
        print Exception.getMessage()
