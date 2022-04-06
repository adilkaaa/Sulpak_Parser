from bs4 import BeautifulSoup
import requests
from pprint import pprint
import csv

URL = 'https://www.sulpak.kg/f/smartfoniy'

HEADERS = {
    'User-Agent':
	'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'
}

response = requests.get(URL,headers=HEADERS,verify=False)
smartphones = BeautifulSoup(response.content,'html.parser')
s = smartphones.find_all('div',class_ ="goods-tiles")
list_smartphones = []
for i in s:
    list_smartphones.append({'name':i.find('h3',class_="title").get_text(strip=True),'price': i.find('div',class_='price').get_text(strip=True)[5:],'code':i.find('span',class_ = 'code').get_text(strip=True)[12:],'rating':i.find('a',class_='rating-container').get_text(strip=True)})
print(list_smartphones[0])

field = ['name','price','code','rating']

with open('smartphones.csv','w',newline='') as file:
    writer = csv.DictWriter(file,fieldnames=field)
    writer.writeheader()
    writer.writerows(list_smartphones)
    

