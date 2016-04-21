#sets starting point

from bs4 import BeautifulSoup
import requests



url = 'http://www.boxofficemojo.com/movies/alphabetical.htm?letter=A&p=.htm'
response = requests.get(url)
page = response.text
soup = BeautifulSoup(page, 'lxml')
​
tds = soup.find_all('td')

links = []

for td in tds:
    links.append(td.find('a'))





all_links =[]
franchise_links=[]
​
for link in soup.find_all('a'):
    all_links.append(link.get('href'))
    
for item in all_links:
    if item[0]=='.':
        franchise_links.append(item)
        
movie_links=[]
for item in franchise_links:
    url = 'http://www.boxofficemojo.com/franchises'+item[1:]
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, 'lxml')
    table = soup.find_all('table')[2]
    for link in table.find_all('a'):
        i = link.get('href')
        if i.startswith('/movie') and i not in movie_links:
            movie_links.append(i)

