import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

# Input values
url = "https://py4e-data.dr-chuck.net/known_by_Isimeli.html"
count = 7      # How many times to follow the link
position = 27 # Position of the link to follow (1-based)

print("Retrieving:", url)

for i in range(1,count):
    # Open and parse the page
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all anchor tags
    tags = soup('a')
    
    # Follow the link at the given position (convert 1-based to 0-based index)
    url = tags[position - 1].get('href', None)
    print("Retrieving:", url)

# Final name in URL
print("Answer:", url.split('_')[-1].replace('.html', ''))
