import urllib.request
import urllib.parse
import json

# Base API URL
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Prompt for location
address = "University of Delaware"

# Encode the parameters
params = {'q': address}
url = serviceurl + urllib.parse.urlencode(params)

print(f'Retrieving {url}')
uh = urllib.request.urlopen(url)
data = uh.read().decode()

print(f'Retrieved {len(data)} characters')

# Load and parse the JSON data
try:
    js = json.loads(data)
except:
    js = None

if not js or 'plus_code' not in js:
    print('==== Failure To Retrieve ====')
else:
    print('Plus code:', js['plus_code'])
