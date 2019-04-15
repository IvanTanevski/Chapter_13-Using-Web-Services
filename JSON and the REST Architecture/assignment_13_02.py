# Extracting Data from JSON
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract 
# the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below.

import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter URL - ')
urlHandle = urllib.request.urlopen(url)
data = urlHandle.read().decode()

js = json.loads(data)               # Creating JSON format
count = 0
total = 0
for comment in js['comments']:      # Iterating through all 'comments' keys in js['comments'] list, counting them
    count += 1                      
    num = int(comment['count'])     # and extracting and summing all "comment['count']" values in the total variable
    total += num
print('Count:', count)
print('Total:', total)
