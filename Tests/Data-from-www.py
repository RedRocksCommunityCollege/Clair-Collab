import urllib.request
import urllib.parse
import re

'''This code explores using the urllib and re modules for webscraping data.

In this case, pulling the paragraph data from pythonprogramming.net using the POST method

This utility could find use in this project in the future'''

# URL that we are scraping for data
url = 'http://pythonprogramming.net'

# Navigate to specific area within pythonprogramming.net
values = {'s':'basic','submit':'Search'}
# This is a POST. A POST is a more specific search,
# in this case: http://pythonprgramming.net/?s=basic&submit=Search
# We also could have used a GET request
# by making line 12 "url = 'http://pythonprogramming.net/?s=basic&submit=Search'"
# and eliminating line 15, but this would be a less "correct" method.

# Encode the values to complete the URL
data = urllib.parse.urlencode(values)
# in other words:
# original URL + encoded values = http://pythonprgramming.net/?s=basic&submit=Search

# Specify type of encoding
data = data.encode('utf-8')

# Request URL and data we want to pass
req = urllib.request.Request(url, data)

# Visits URL
resp = urllib.request.urlopen(req)

# Read data from URL
respData = resp.read()

# Find the paragraph data in the HTML
paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))
# <p>paragraphs in HTML live here</p>

#Print everything between the <p>'s and </p>'s
for eachP in paragraphs:
    print(eachP)
