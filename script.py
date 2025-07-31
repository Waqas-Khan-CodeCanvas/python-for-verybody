import re

# Open the file
with open("text.txt") as file:
    contents = file.read()

# Find all numbers
numbers = re.findall(r'[0-9]+', contents)

# Convert to integers and sum
total = sum(int(num) for num in numbers)

print(total)
