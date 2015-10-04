from bs4 import BeautifulSoup
import urllib3

url = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=aapl+stock+prices"
manager = urllib3.PoolManager()
req = manager.request('GET', url)

print req.status

soup = BeautifulSoup(req)

print soup.prettify()


