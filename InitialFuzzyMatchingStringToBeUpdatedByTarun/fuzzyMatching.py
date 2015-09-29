import enchant
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

myDict = enchant.Dict("en_US")
sentence = raw_input("Enter the string---->")
myWord = sentence.split(" ")

def assessor(analyseString):
    truth = myDict.check(analyseString)
    return truth

for i in range(0, len(myWord)):
  
    check = assessor(myword[i])

    if(check == True):
        print "Perfect match for entered word"

    if(check == False):
        myArray = myDict.suggest(myword[i])
        print myArray
        
        tokenSetRatioArray = []
        maxProb = 0
        index = 0
        for j in range(0,len(myArray)):
            tokenSetRatioArray.append(fuzz.token_sort_ratio(myWord[i],myArray[j]))
            if (maxProb < tokenSetRatioArray[j]):
                maxProb = tokenSetRatioArray[j]
                index = j;

        print "Index:" + str(index) + "maxProb:" + str(maxProb)
          
