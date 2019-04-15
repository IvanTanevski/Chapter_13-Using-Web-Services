# Extracting Data from XML
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract 
# the comment counts from the XML data, compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)                          # Creating XML object (tree).
commentList = tree.findall('comments/comment')     # Creating list of nodes with 'comment' tag
total = 0
for comment in commentList:                        # For each value in the 'comment' nodes,
    total += int(comment.find('count').text)       # adding that value to total variable to sum the numbers

print('Sum:', total)
print('Count:', len(commentList))