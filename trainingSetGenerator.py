import os
from itertools import izip

userInfo = open("training_set_users.txt", "r")
tweetInfo = open("training_set_tweets.txt", "r")
trainingSet = open("training_combined.txt", "w")
    
def setGenerator():
    for iteratorTweets in tweetInfo:
        tweetBuffer = str(iteratorTweets)
        myTweetArray = tweetBuffer.split("\t")
        for iteratorUid in userInfo:
            userBuffer = str(iteratorUid)
            myUserArray = userBuffer.split("\t")
            print myUserArray[1]
            try:
                if (myTweetArray[0] == myUserArray[0]):
                    trainingSet.write(tweetBuffer+"\t"+myUserArray[1]+"\n")
            except Exception:
                pass
        
        
    
if __name__ == '__main__':

    print "Bootstrapping training data creation script **************"
    
    setGenerator()

    
    
    
    
