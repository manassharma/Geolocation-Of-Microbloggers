from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

from geopy.geocoders import Nominatim
geolocator = Nominatim()
# Define the latitude and longitude array
lats, lons = [], []
#reading the input file
file = open("user_locations.txt",'r')
for input in file:
  try:
      read = input.split("	")[1]
      location = geolocator.geocode(read)
      lats.append(location.latitude)
      lons.append(location.longitude)
  except AttributeError:
      pass
#plotting the map
try:
 eq_map = Basemap(projection='ortho', resolution = '', area_thresh = 1000000.0,
              lat_0=66, lon_0=124)
 eq_map.drawcoastlines()
 eq_map.drawcountries()
 eq_map.fillcontinents(color = 'gray')
 eq_map.drawmapboundary()
 eq_map.drawmeridians(np.arange(0, 360, 30))
 eq_map.drawparallels(np.arange(-90, 90, 30))
 

 x,y = eq_map(lons, lats)
 eq_map.plot(x, y, 'ro', markersize=10)
 
 plt.show()
 
except AttributeError, GeocoderTimedOut :
    pass