
tweetInfo = open("testData.txt", "r")
mentionsFile = open("trialMnetions.txt", "a")


dict = {}
#line = tweetInfo.readline()


for tweet in tweetInfo:
    splitline = tweet.split('@')
    print splitline

    i = 1
    while i < len(splitline):
        splitBySymbol = str(splitline[i].split(' ')[0]).lower()
        print splitBySymbol
        if dict.has_key(splitBySymbol):
            dict[splitBySymbol] = dict[splitBySymbol] + 1;
        else:
            dict[splitBySymbol] = 1
        i += 1



# For getting the number of mentions in sorted order
for w in sorted(dict, key=dict.get, reverse=True):
    mentionsFile.write(str(w) + " " + str(dict[w]) + "\t")

tweetInfo.close()
mentionsFile.close()
    
