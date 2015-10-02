import enchant
import csv 
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

myDict = enchant.Dict("en_US")

def wordCheck(word):
    '''Description:Function to check if a word exists in US english dictionary
        Return Value: Boolean
    '''
    
    truth = myDict.check(word)
    return truth

def sentenceCorrector(sentence):
    '''Fucntion to correct the english text using fuzzy logic
        Return Value = String (Corrected sentence)
    '''
    sentence = "".join(sentence)
    #print "SENTENCE: %s" % type(sentence)
    myWord = sentence.split(",")
    #print myWord
    
    for i in range(0, len(myWord)):
      
        check = wordCheck(myWord[i])

        if check == True:
            pass
        else :
            myArray = myDict.suggest(myWord[i])
            #print myArray
            
            tokenSetRatioArray = []
            maxProb = 0
            index = 0
            for j in range(0,len(myArray)):
                tokenSetRatioArray.append(fuzz.token_sort_ratio(myWord[i],myArray[j]))
                if (maxProb < tokenSetRatioArray[j]):
                    maxProb = tokenSetRatioArray[j]
                    index = j;

            #print "Index:" + str(index) + "maxProb:" + str(maxProb) + "index:" + str(index) + "i:" + str(i)
            if tokenSetRatioArray:
                myWord[i] = myArray[index];

    #print myWord
    #print " ".join(myWord)
    return " ".join(myWord)        


'''Opening the csv file and storing the modified data in new .csv file'''
try:
    with open("testf.csv", 'rb') as orgFile:
        reader = csv.reader(orgFile)

        with open("new.csv", 'wb') as newFile:
            writer = csv.writer(newFile)
            writer.writerow("TWITTER")
    
            for row in reader:
                print row
                newSentence = sentenceCorrector(row)
                writer.writerow("%s" % (newSentence))
        
    print open("new.csv", 'rb').read() 
    #print "csvvvvvvvvvvvvvvvvvv"
finally:
    orgFile.close()
    newFile.close()

