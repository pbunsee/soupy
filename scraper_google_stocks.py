from bs4 import BeautifulSoup
import urllib3
import certifi

# Note that urllib3 is not backwards compatible with urllib2 
# opening the socket is done completely differently in urllib2

# original url shown below but the sourceid and espv variables can be stripped out
# want to keep the UTF-8 encoding in the GET request though for correct char handling
# url = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=aapl+stock+prices"

url = "https://www.google.com/webhp?ie=UTF-8#q=aapl+stock+prices"
manager = urllib3.PoolManager(
  cert_reqs='CERT_REQUIRED', # Force certificate check.
  ca_certs=certifi.where(),  # Path to the Certifi bundle.
)

try:
  req = manager.request('GET', url)
  print req.status
  soup = BeautifulSoup(req, "html.parser")
  print soup.prettify()
  #getdivs = soup.findAll("div", { "class" : "finance_answer_card__price" } )
  getdivs = soup.findAll("div")
  print getdivs
except urllib3.exceptions.SSLError as e:
  # Handle incorrect certificate error.
  print "error"

