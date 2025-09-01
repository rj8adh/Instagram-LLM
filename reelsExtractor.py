from bs4 import BeautifulSoup
import json

HtmlFile = open('message_1.html', 'r', encoding='utf-8')

soup = BeautifulSoup(HtmlFile.read())

divs = soup.find_all('div', attrs={'class':'pam _3-95 _2ph- _a6-g uiBoxWhite noborder'})

allReels = []

for div in divs:
    anchors = div.find_all('a')
    sender = div.find('h2', attrs={'class':'_3-95 _2pim _a6-h _a6-i'})
    print(sender)
        
    # print(currPerson.text)

    if not anchors:
        continue
    
    for anchor in anchors:
        url = anchor.get('href')
        if 'https://www.instagram.com/reel/' in url:
            allReels.append({'Reel':str(url), 'Sender':sender.text})
    # break

with open('allReels.json', 'w') as f:
    json.dump(allReels, f, indent=4)