import json
import urllib2


cities = {'San Francisco' :'sanfrancisco',
          'Houston': 'houston',
           'New York' : 'newyork', 'Baltimore' : 'baltimore', 'Austin' : 'austin'
          
          }

         

# This is the API URL
for city, value in cities.iteritems():
    api = "https://publicdata-weather.firebaseio.com/"+value+"/currently.json"

    get = urllib2.urlopen(api).read()
    data = json.loads(get)

    summary = data['summary']
    if summary == 'Rain':
        summary = 'Rainy'
    temperature = data['temperature']
    if temperature < 60:
        temp = 'Cold temperature'
    elif temperature > 80:
        temp = 'Hot temperature'
    else:
        temp = 'Mild temperature'
    windspeed = data['windSpeed']
    if windspeed > 25:
        wind = 'Windy'
    elif windspeed < 5:
        wind = 'Still wind'
    else:
        wind = 'Moderate wind'
    print city
    print summary
    print temp
    print wind
    print
