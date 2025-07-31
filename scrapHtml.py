import urllib.request
from bs4 import BeautifulSoup

# Prompt for URL
url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all span tags
tags = soup('span')

# Compute the sum
total = 0
for tag in tags:
    total += int(tag.contents[0])

# Print the results
print('Count', len(tags))
print('Sum', total)
