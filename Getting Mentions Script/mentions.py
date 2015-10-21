''' Finding the mentions program'''


tweetInfo = open("testData.txt", "r")
mentionsFile = open("mentions.txt", "w")



initialUserId = 0

#making a dictionary to to store all the mentions and their count 
dictionary = {}

startFlag = 0

for tweet in tweetInfo:
    # To get the user id
    splitSentence = tweet.split('\t')
    userId = str(splitSentence[0])

    #Segregating mentions based on users
    if (userId != initialUserId) & (startFlag == 0):
        userId = userId[3:]
        initialUserId = userId
        print "1st if: " + str(userId + "<--->" + initialUserId)
        startFlag = 1
        print userId != initialUserId

    if (userId != initialUserId) & (startFlag == 1):
        print "2nd if:" + str((userId != initialUserId) & (startFlag == 1))
        print userId + "<--->" + initialUserId
        mentionsFile.write(str(userId) + "\t\t")
        
        # For getting the number of mentions in sorted order
        for w in sorted(dictionary, key=dictionary.get, reverse=True):
            mentionsFile.write(str(w) + " " + str(dictionary[w]) + "\t")
            #print w,dictionary[w]
        #Building a new Dictionary for every user 
        dictionary.clear()
        initialUserId = userId

        #Printing newline after every user
        mentionsFile.write("\n")

    splitline = tweet.split('@')
    i = 1
    while i < len(splitline):
        splitBySymbol = str(splitline[i].split(' ')[0]).lower()
        #print splitBySymbol
        if dictionary.has_key(splitBySymbol):
            dictionary[splitBySymbol] = dictionary[splitBySymbol] + 1;
        else:
            dictionary[splitBySymbol] = 1
        i += 1



#For Printing dictionary of last user
mentionsFile.write(str(userId) + "\t\t")
for w in sorted(dictionary, key=dictionary.get, reverse=True):
    mentionsFile.write(str(w) + " " + str(dictionary[w]) + "\t")
    print w,dictionary[w] 

#Closing the files    
tweetInfo.close()
mentionsFile.close()
    
    
