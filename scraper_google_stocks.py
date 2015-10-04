from bs4 import BeautifulSoup
import urllib3

# Note that urllib3 is not backwards compatible with urllib2 
# opening the socket is done completely differently in urllib2

# original url shown below but the sourceid and espv variables can be stripped out
# want to keep the UTF-8 encoding in the GET request though for correct char handling
# url = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=aapl+stock+prices"

url = "https://www.google.com/webhp?ie=UTF-8#q=aapl+stock+prices"
manager = urllib3.PoolManager()
req = manager.request('GET', url)

print req.status

soup = BeautifulSoup(req)

print soup.prettify()


