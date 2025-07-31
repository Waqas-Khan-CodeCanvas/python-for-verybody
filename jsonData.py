import urllib.request
import json

# Prompt for URL
url = "http://py4e-data.dr-chuck.net/comments_2250434.json"
print("Retrieving", url)

# Read and decode JSON data
uh = urllib.request.urlopen(url)
data = uh.read().decode()

print("Retrieved", len(data), "characters")

# Parse JSON
info = json.loads(data)

# Extract the list under 'comments'
comments = info["comments"]

# Sum the 'count' fields
count = 0
for item in comments:
    count += int(item["count"])

print("Count:", len(comments))
print("Sum:", count)
