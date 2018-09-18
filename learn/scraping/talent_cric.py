import urllib.request,urllib.parse
from bs4 import BeautifulSoup as BS

status = 0
crawled = []
items = []
count = [0]
for i in range(1,100):
    url = 'https://www.talentcricket.co.uk/cricket_equipment_sale/c243.html?page='+str(i)
    print(url)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    urlOpen = urllib.request.urlopen(req)
    html = urlOpen.read()
    data = BS(html,'html.parser')
    tags = data('a')

    for anchor in tags:
        urlType = anchor.get('class', [None])
        if urlType[0] != "pos":
            continue
        else:
            newUrl = anchor.get('href', None)
        if newUrl not in crawled:
            crawled.append(newUrl)
            urlContents = newUrl.split('/')
            itemName = urlContents[4]
            itemType = itemName.split('_')
            if itemType[-1] == 'bat':
                if itemType[-3] != 'junior':
                    items.append(itemName)
    count.append(len(crawled))
    if count[i] == count[i-1] and count[i-1] == count[i-2]:
        break

fRead = open('talentCric.txt','r')
for item,line in zip(items,fRead):
    line = line.strip()
    if item != line:
        print('SALE REVISED!!')
        status = 1
        break
    else:
        continue
fRead.close()

if status == 1:
    fWrite = open('talentCric.txt','w')
    for item in items:
        fWrite.write(item+'\n')
    print('File updated')
    fWrite.close()
print("THE END")
