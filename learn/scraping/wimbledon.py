import urllib.request,urllib.parse
from bs4 import BeautifulSoup as BS

url = 'http://www.wimbledon.com/en_GB/draws/index.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
urlOpen = urllib.request.urlopen(req)
html = urlOpen.read()

data = BS(html,'html.parser')

tags = data('a')

crawled = []
for anchor in tags:
    newUrl = anchor.get('href',None)

    if (newUrl == None or newUrl.startswith('#')
        or newUrl.startswith('javascript:')) :
        continue
    if newUrl not in crawled:
        crawled.append(newUrl)

for i in crawled:
    print(i)

print(len(crawled),' new urls found')
