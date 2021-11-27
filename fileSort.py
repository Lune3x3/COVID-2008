import os, time, pickle
import pandas as pd
import numpy as np

def formatData(loc, sizeTreshold):
	files = os.listdir(loc)
	data = {}
	i = 0
	for filename in files:
		i += 1
		print(i)
		filename = loc + f'\\{filename}'
		if os.path.getsize(filename) > sizeTreshold:
			with open(filename, 'r') as f:
				f = f.read().strip().split('\n')
				for fi in f:
					uid, date, lat, lon = fi.split(',')
					uid, date, lat, lon = int(uid), time.strftime(date[:-3]), float(lon), float(lat)

					lon = round(lon, 4)
					lat = round(lat, 4)

					if date not in data:
						data[date] = [(lon, lat)]
					else:
						data[date].append((lon, lat))
	data = pd.DataFrame.from_dict(data, orient = 'index')
	data.ffill(inplace = True)
	return data

data = formatData(os.getcwd() + '\\taxi_log_2008_by_id', 10000)

#interactions dataframe

#flip dataset
dfTime = data.transpose()
for index, row in dfTime.iterrows():
	#compare each value in a column to eachother and
	for i in dfTime[index]:
	#if they match replace the match values with the macher, else replace with 0
		if dfTime.iloc[index][i] ==
	#do for each column
	#unfilp the dataframe and return it

def slowFunc(df):
	for column in df:
		a

with open('COVIDdata2.pkl', 'wb') as f:
	pickle.dump(data, f)
	f.close()

