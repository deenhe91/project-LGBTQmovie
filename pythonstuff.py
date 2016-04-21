
import requests
from bs4 import BeautifulSoup
import re


url = 'http://www.boxofficemojo.com/intl/china/yearly/?yr=2015&p=.html'
response = requests.get(url)
page = response.text
data_page = BeautifulSoup(page,'html5lib')


for td in table.find_all('td'):
	if re.search()
