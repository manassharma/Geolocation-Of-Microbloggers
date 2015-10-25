''' Finding the mentions program'''
import tweepy
import time

tweetInfo = open("Test_user_set.txt", "r")
mentionsFile = open("TestOutput.txt", "w")
friendsFile = open("Test_friend_list.txt", "r")

consumer_key = 'y2AklbQgjxgUL6tLczXKsb1gP'
consumer_secret = 'TRox57fTR5OJqVO03rcPsUdxnF4kSEPk9zNfoiMrN4tDfE0QdD'
access_token = '3977062212-svlA5fLYadx785RX7fweQVpyqNSs9jtrH4maKkC'
access_secret = 'glky6Tp0B07BlxhOG0rnuAYCOeuEajmXFARkgqvg0dNnX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#To store initial UserId and compare it with consecutive ones
initialUserId = 0

#making a dictionary to to store all the mentions and their count
dictionary = {}

startFlag = 0
friendFlag = 0          #to keep a track whether user is a friend or not

for tweet in tweetInfo:
    # To get the user id
    splitSentence = tweet.split('\t')
    userId = str(splitSentence[0])

    #Segregating mentions based on users
    if (userId != initialUserId) & (startFlag == 0):
        initialUserId = userId
        userLocation = str(tweet.split(' \t\t\t')[1]).rstrip(' \t\n\r')
        #print "1st if:" + str(userId) + "<--->" + str(initialUserId) + "-->"
        startFlag = 1

    if (userId != initialUserId) & (startFlag == 1):

        # For getting mentions in ascending order
        for w in sorted(dictionary, key=dictionary.get, reverse=True):
            if((str(w) != " ") & (str(w) != "")):

                #Check for any friends of the user in friends file and assign a weight 2
                friendsFile.seek(0)
                for friend in friendsFile:
                    friendName = str(friend.split('\t')[3]).rstrip(' \t\r\n')
                    #print friend.split('\t')[3]

                    friendId = str(friend.split('\t')[0]).strip(' \t\r\n')
                    #print initialUserId + friendId + str(w) + friendName

                    if((str(initialUserId) == str(friendId)) & (str(w) == str(friendName))):
                        mentionsFile.write(str(initialUserId) + "-" + str(userLocation) + "|" + friend.split('\t')[1] + "-" + friend.split('\t')[2] + "|" + str(len(dictionary)))
                        friendFlag = 2

                if(friendFlag != 2):
                    try:
                        Id = api.get_user(str(w))
                        location = str(Id.location)
                        if (location == ''):
                            location = "Error"
                        mentionsFile.write(str(initialUserId) + "-" + str(userLocation) + "|" + str(Id.id) + "-" + location +"|" + str(len(dictionary)))
                    except(tweepy.error.TweepError, UnicodeEncodeError) as e:
                        mentionsFile.write(str(initialUserId) + "-" + str(userLocation) + "|" + str(0) + "-" + "Error" +"|" + str(len(dictionary)))

                mentionsFile.write("|" + str(friendFlag + 2) +"\n")
                friendFlag = 0

        #Building a new Dictionary for every user
        dictionary.clear()
        initialUserId = userId

        #To get user location from valid user file
        userLocation = str(tweet.split(' \t\t\t')[1]).rstrip(' \t\n\r')


    splitline = tweet.split('@')
    i = 1
    while i < len(splitline):
        splitBySymbol = str(splitline[i].split(' ')[0]).lower()

        if dictionary.has_key(splitBySymbol):
            dictionary[splitBySymbol] = dictionary[splitBySymbol] + 1;
        else:
            dictionary[splitBySymbol] = 1
        i += 1


#For Printing dictionary of last user
for w in sorted(dictionary, key=dictionary.get, reverse=True):
    if((str(w) != " ") & (str(w) != "")):

        friendsFile.seek(0) #Setting offset to 0 to reading file everytime from starting

        #Check for any friends of the user in friends file and assign a weight 2
        for friend in friendsFile:
            friendName = str(friend.split('\t')[3]).rstrip(' \t\r\n')
            #print friend.split('\t')[3])
            friendId = str(friend.split('\t')[0]).strip(' \t\r\n')
            #print initialUserId + friendId + str(w) + friendName
            #print str(len(dictionary))
            if((str(initialUserId) == str(friendId)) & (str(w) == str(friendName))):
                mentionsFile.write(str(initialUserId) + "-" + str(userLocation) + "|" + str(friend.split('\t')[1]) + "-" + str(friend.split('\t')[2]) + "|" + str(len(dictionary.keys())))
                friendFlag = 2

        if(friendFlag != 2):
            try:
                Id = api.get_user(str(w))
                location = str(Id.location)
                if (location == ''):
                    location = "Error"
                mentionsFile.write(str(initialUserId) + "-" + str(userLocation) + "|" + str(Id.id) + "-" + location +"|" + str(len(dictionary)))
            except(tweepy.error.TweepError, UnicodeEncodeError) as e:
                mentionsFile.write(str(initialUserId) + "-" + str(userLocation) + "|" + str(0) + "-" + "Error" +"|" + str(len(dictionary)))

        mentionsFile.write("|" + str(friendFlag + 2) +"\n")
        friendFlag = 0
    #print w,dictionary[w]


#Building a new Dictionary for every user
dictionary.clear()

#Closing the files
tweetInfo.close()
mentionsFile.close()

'''
Output format:
UserId-Userlocation|friend/mentionID-location|TotalMentions|Weight
'''