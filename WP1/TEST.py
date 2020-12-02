import requests
from bs4 import BeautifulSoup

def clearFromTags(whatClear):
    whatClear = whatClear[whatClear.find('>')+1:]
    whatClear = whatClear[:whatClear.find('<')]
    return whatClear

r = requests.get('https://www.imdb.com/title/tt0367594/?ref_=nv_sr_srsg_0')
soup = BeautifulSoup(r.text, 'html.parser')
title = soup.find('h1')
title = str(title)
title = title[title.find('Ч'):title.rfind('а') + 1]
print(title)
desc = soup.find('div', {'class': 'summary_text'})
desc = str(desc)
desc = desc[desc.find('A'):desc.rfind('.') + 1]
print(desc)
about = soup.find_all('div', {'class':'credit_summary_item'})
#about = str(about)
#about = clearFromTags(about)
director, writer, star = [i.find_all('a')for i in about]
print('Director: ' + clearFromTags(str(director)))
writers = []
for i in writer:
     test = clearFromTags(str(i))
     writers.append(test)
writers = str(writers)
print('writers: ' + writers)
stars = []
for i in star:
     test = clearFromTags(str(i))
     stars.append(test)
stars[3] = ''
stars = str(stars)
print('stars: ' + stars)

