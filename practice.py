# import urllib.request
# import urllib.parse
# import urllib.error
# from bs4 import BeautifulSoup

# # Start values from the assignment
# url = 'http://py4e-data.dr-chuck.net/known_by_Ismaeel.html'
# count = 7
# position = 18 - 1  # convert to 0-based index

# for i in range(count):
#     print("Retrieving:", url)
#     html = urllib.request.urlopen(url).read()
#     soup = BeautifulSoup(html, 'html.parser')

#     # Get all the anchor tags
#     tags = soup('a')

#     # Follow the link at the specified position
#     url = tags[position].get('href', None)

# # Final retrieval
# print("Retrieving:", url)
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

# # Extract the name from the last link (the anchor text)
# tags = soup('a')
# final_name = tags[position].text if len(tags) > position else 'Unknown'

# print("Last name found:", final_name)


import urllib.request
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Ismaeel.html'
count = 7
position = 18 -1 # zero-based index

for i in range(count):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    url = tags[position].get('href', None)

# Final page fetch
print("Retrieving:", url)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# We expect the last page's name in either the page title or anchor tag
final_names = [a.text for a in soup('a')]
if final_names:
    final_name = final_names[position] if len(final_names) > position else final_names[-1]
else:
    final_name = soup.title.string.strip()

print("Last name found:", final_name)
