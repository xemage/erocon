# Crawl a webpage and get all links
# Show time for page load and time for processing

import urllib.request
import time
from bs4 import BeautifulSoup

t0 = time.time()
req = urllib.request.urlopen('http://www.example.com')
t1 = time.time()
print("Total Time To Fetch Page: {0} Seconds".format(str(t1-t0)))

soup = BeautifulSoup(req.read(), "html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))

t2 = time.time()
print("Total Execeution Time: {0} Seconds".format(str(t2-t1)))