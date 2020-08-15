from xml.etree.ElementTree import parse
doc = parse('rt22_2.xml')
print(type(doc))
print(doc)

for bus in doc.findall("bus"):
    lat = bus.findtext("lat")
    direction = bus.findtext("d")
    busid = bus.findtext("id")
    print("Bus ID: {}, Direction: {}, Lat: {}".format(busid, direction, lat))

