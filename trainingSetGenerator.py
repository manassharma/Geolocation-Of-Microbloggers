import os
from itertools import izip

userInfo = open("training_set_users.txt", "r")
tweetInfo = open("training_set_tweets.txt", "r")
trainingSet = open("training_combined.txt", "w")

def setGenerator():

    myDict = {}
    for userData in userInfo:
        userBuffer = str(userData)
        userArray = userBuffer.split("\t")
        try:
            myDict[userArray[0]] = userArray[1]
        except Exception:
            pass

        
    for currentTweetInfo in tweetInfo:
        tweetBuffer = str(currentTweetInfo)
        myTweetArray = tweetBuffer.split("\t")
        try:
            if (myTweetArray[0] in myDict):
                getString = str(myDict.get(myTweetArray[0]))
                getString = getString.lstrip()
                getString = getString.rstrip()

                trainingSet.write(currentTweetInfo.rstrip() + "\t" + getString + "\n")
        except Exception:
            pass
        
    print "Data collator finished execution"
    
if __name__ == '__main__':

    print "Bootstrapping training data creation script **************"
    
    setGenerator()

    
    
    
    
