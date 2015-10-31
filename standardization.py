import os
from geopy.geocoders import Nominatim

states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

def get_state(location):
	geocode = myGeocoordinates.geocode(location) 
	if(str(geocode) == 'None'):
		return ""
	else:
        	locationSplit = geocode.address.split(',')
        	state = str(locationSplit[len(locationSplit)-2]).rstrip()
        	state = state.lstrip()
		if state in states:
			statecode = states[state]
		else:
			statecode = ""
		return statecode
	
print "Enter the input file path"
getInput = raw_input()
myInput = open(getInput, "r")
state = input("Enter the user's state\n")
user_location = states[state]
outputPointer = open("standardizedoutputfromscript.txt","w")
myGeocoordinates = Nominatim()

for currentFeature in myInput:
    myArray = currentFeature.split("\t")
    try:
        friend_location = get_state(myArray[5])	
        outputPointer.write(myArray[0] + '\t' + user_location + '\t' + myArray[3] + '\t' + friend_location + '\n')
        
    except Exception:
	print currentFeature + "ERROR"
        pass
