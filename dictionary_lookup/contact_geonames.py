import requests

response = requests.get(
    "http://api.geonames.org/searchJSON?q=basil&fuzzy=0.8&username=demo")
# with geoname id
# response = requests.get(
#     "http://api.geonames.org/searchJSON?q=coimbatore&fuzzy=1.0&username=demo")

print(response.content)
