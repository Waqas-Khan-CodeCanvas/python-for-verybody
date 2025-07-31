import urllib.request
import xml.etree.ElementTree as ET

url = "https://py4e-data.dr-chuck.net/comments_2250433.xml"
print('Retrieving', url)
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

# Use XPath to find all <count> elements
counts = tree.findall('.//count')
total = sum(int(c.text) for c in counts)

print('Count:', len(counts))
print('Sum:', total)
