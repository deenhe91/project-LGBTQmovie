from __future__ import unicode_literals

import csv
import re
import pandas as pd


character_df = pd.read_csv('character_list5.csv', encoding="ISO-8859-1")

movie_df = pd.read_csv('meta_data7.csv', encoding="ISO-8859-1") 

with open('meta_data7.csv', encoding="ISO-8859-1") as f:
	meta_reader = csv.reader(f)

	#print(type(meta_reader))
	#for row in meta_reader:
		#print(row)
		# for cell in row:
		# 	print(cell)
		# if re.search('((^|, )(tt0103644|tt0211915|tt0110413))+$', row) 
	rows = [[cell.strip() for cell in row] for row in meta_reader]
	
	#rows = [[unicode(cell, 'utf-8') for cell in row] for row in meta_reader]

movie_titles = []

for row in rows:
 	movie_titles.append(row[2])

# movie_dict ={}

# movie_dict = {year : }


# var lineInfo = data.lines_data.match(/.{1,2}/g);

# for (line in lineInfo){
#     var minuteTotal = +lineInfo[line].slice(0,1) + +lineInfo[line].slice(1,2);
#     var row = [minuteTotal,14-minuteTotal];
#     lineData.push(row);
#     }
