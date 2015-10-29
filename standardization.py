import os
from geopy.geocoders import Nominatim

print "Enter the input file path"

getInput = raw_input()
outputPointer = open("standardizedoutputfromscript.txt","w")
myGeocoordinates = Nominatim()
myInput = open(getInput, "r")

for currentFeature in myInput:
    myArray = currentFeature.split("\t")
    try:
        cityName = myArray[5]
        location = myGeocoordinates.geocode(myArray[5]) 

        latitude = location.latitude
        longitude = location.longitude

        locationSplit = location.address.split(',')
        printLocation = str(locationSplit[2]).rstrip()
        printLocation = printLocation.lstrip()

        outputPointer.write(myArray[1] + '\t' + myArray[2] + '\t' + myArray[3] + '\t' + myArray[4] + '\t' + printLocation + '\n')
        
    except Exception:
        pass
    
