import json , StringIO, urllib2, pygame
from PIL import Image
screen = pygame.display.set_mode([600,400])
import urllib2
api = "https://publicdata-transit.firebaseio.com/sf-muni.json"
def get_data(api):
  get = urllib2.urlopen(api).read()
  data = json.loads(get)

  return data
data = get_data(api)

def find_bus(bus_name, data):
  for bus_id, bus_info in data['vehicles'].iteritems():
    if bus_info['routeTag']:
      return bus_info



# for routes that are just numbers the input parameter 
# should be int instead of string
number = 'F'
location = find_bus(number, data)

latitude = location['lat']
longitude = location['lon']

print latitude
print longitude

def get_map(latitude, longitude):
  size = '600x450'
  zoom = '16'
  url = "http://maps.google.com/maps/api/staticmap?size=%s&maptype=roadmap&markers=size:mid|color:red|%s,%s&sensor=false&zoom=%s"

  return url % (size, latitude, longitude, zoom)


map_url = get_map(latitude, longitude)  
img_buffer = StringIO.StringIO(urllib2.urlopen(map_url).read())
image = Image.open(img_buffer)
image2 = pygame.image.fromstring(str(img_buffer), (600,450), 'RGB')
screen.blit(image2, 0, 0)
pygame.display.update
