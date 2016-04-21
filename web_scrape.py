import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint
import pandas as pd
import html5lib

# url = 'http://www.boxofficemojo.com/yearly/chart/?yr=2015&p=.htm'
#response = requests.get(url)
# page_html = response.text
# page_string = str(page_html) #string to enable regex search


movie_f = open('moviebudgetcopy.html',encoding='UTF-8')

soup = BeautifulSoup(movie_f, 'lxml')

tags = soup.find_all('b')
movies_wtags = tags[7:5126]

movie_list = []

for movie in movies_wtags:
	
	tmp = str(movie).split('>')
	first = tmp[1]
	second = first.split("<")
	final = second[0]
	movie_list.append(final)

temp = soup.find_all('table')

plist = []
for table in temp:
	tmp = table.find_all('p', attrs={'class':'p4'})
	# tmp2 = tmp.text()
	plist.append(tmp[1].text)

budget_list = plist




import numpy as np
import pandas as pd


movie_array = np.array(movie_list[1:-1])
budget_array = np.array(budget_list)
df = pd.DataFrame({'budget': budget_array, 'movie': movie_array})

import numpy as np
a = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
b = array([0, 0, 0, 1, 0, 0, 0, 1, 1, 0])
# view which should match up
print zip(a,b)
​
# use np.where to index a
values_of_a_where_b_is_greater_than_zero = a[np.where(b>0)]
print values_of_a_where_b_is_greater_than_zero





