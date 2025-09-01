from bs4 import BeautifulSoup
import json

HtmlFile = open('message_1.html', 'r', encoding='utf-8')

soup = BeautifulSoup(HtmlFile.read())

divs = soup.find_all('div')

allReels = []
currPerson = '' # filetype will change later to bs4 object

for div in divs:
    anchors = div.find_all('a')
    people = div.find('h2')

    if people:
        currPerson = people
        
    # print(currPerson.text)

    if not anchors:
        continue
    
    for anchor in anchors:
        url = anchor.get('href')
        if 'https://www.instagram.com/reel/' in url:
            allReels.append({'Reel':str(url), 'Sender':currPerson.text})

with open('allReels.json', 'w') as f:
    json.dump(allReels, f, indent=4)