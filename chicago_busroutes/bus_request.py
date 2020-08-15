import requests
request = requests.get("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
data = request.text
#import urllib
#u = urllib.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
#data = u.read()
f = open('rt22_2.xml', 'w')
f.write(data)
f.close()