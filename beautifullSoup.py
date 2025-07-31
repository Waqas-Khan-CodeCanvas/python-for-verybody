import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

# Input values
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: ")) - 1  # Convert to zero-based index

for i in range(count):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Get all anchor tags
    tags = soup('a')

    # Select the tag at the desired position
    url = tags[position].get('href', None)

# Final fetch to extract the name from the last page
print("Retrieving:", url)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Extract the name from the anchor tag text or page title
# (Depending on the page format — often it’s in the <title>)
name = soup.title.string.strip()
print("Last name found:", name)
