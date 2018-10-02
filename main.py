import requests
import populartimes
from populartimes import get

response = requests.get('https://httpbin.org/ip')

apiKey = "AIzaSyCscTwcpOOEBQSANv0n3ctflHiVAhSN-oo"

def hello_world():

    lat1 = 51.45527
    long1 = -0.01907

    lat2 = 51.46753
    long2 = -0.00407

    data = populartimes.get(apiKey,["bar"], (lat1, long1), (lat2, long2))
    print(data)
    for location in data:
        if('current_popularity' in location):
            print("Location name: " + location['name'] + " is has current popularity of: " +
  str(location['current_popularity']))

hello_world()

mprint('Your IP is {0}'.format(response.json()['origin']))
