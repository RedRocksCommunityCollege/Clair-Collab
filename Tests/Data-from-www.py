#Used for pulling paragraph data from the web using POST

import urllib.request
import urllib.parse
import re
import numpy as np

'''
url = 'http://pythonprogramming.net'
#URL that we are scraping for data
values = {'s':'basic','submit':'Search'}
#this is a POST. A POST is a more specific search,
#in this case: http://pythonprgramming.net/?s=basic&submit=Search
#We also could have used a GET request
#by making line 7 "url = 'http://pythonprogramming.net/?s=basic&submit=Search'"
#and eliminating line 9. This would be less "correct."
data = urllib.parse.urlencode(values)
#This encodes the values to complete the GET format url
#in other words:
#URL + encoded values = http://pythonprgramming.net/?s=basic&submit=Search
data = data.encode('utf-8')
#a type of encoding (puts data in bytes)
req = urllib.request.Request(url, data)
#request URL and data we want to pass
resp = urllib.request.urlopen(req)
#visiting URL
respData = resp.read()
#reads data from URL

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))
#finds the paragraph data in the HTML
#<p>paragraphs in HTML live here</p>

for eachP in paragraphs:
    print(eachP)
#prints everything between the <p>'s and </p>'s

'''
#Used for pulling paragraph data from the web using GET

url = urllib.request.urlopen('http://www.rrcc.edu/idea-institute')

#print(x)

HTML = url.read()
#print(HTML)

#x = urllib.parse.encode('utf-8')

#req = urllib.request.Request(url, x)
#request URL and data we want to pass
#resp = urllib.request.urlopen(req)
#visiting URL
#respData = resp.read()
#reads data from URL
paragraphs = re.findall(r'<p>(.*?)</p>',str(HTML))
Non = re.findall(r'<a href=(.*?)</a>',str(HTML))

#finds the paragraph data in the HTML
#<p>paragraphs in HTML live here</p>
print(Non)
np.shape(Non)
print(paragraphs)
np.shape(paragraphs)
paragraphs[0]


for eachP in paragraphs:
    print(eachP)
#prints everything between the <p>'s and </p>'s
