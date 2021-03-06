import os

def classifier(dataPath, stateInfo):
    inPath = open(dataPath, "r")
    outPath = open(stateInfo+"outputbyclassifier.txt", "w")

    for tempBuffer in inPath:
        stringBuffer = str(tempBuffer)
        try:
            processedArray = stringBuffer.split('\t\t\t\t')
            checkArray = processedArray[1].split(',')

            if(str(checkArray[1]).rstrip().lstrip() == stateInfo or str(checkArray[0]).rstrip().lstrip() == stateInfo or str(processedArray[1]).rstrip().lstrip() == stateInfo):
                outPath.write(stringBuffer)
        except Exception:
            pass
    return
    

if __name__ == '__main__':

    print "Enter the input file path"
    dataPath = raw_input()

    print "Enter the U.S state you wish the classifier to run upon"
    stateInfo = raw_input()
    
    classifier(dataPath, stateInfo)

    print "Classfier finished execution, classifier's output can be seen in the same directory you ran the script from"
