import pickle
import pandas as pd
import numpy as np
from time import time
from collections import defaultdict

with open('COVIDdata2.pkl', 'rb') as f:
	df = pickle.load(f).sort_index(axis = 0)
	f.close()

#dfTime = pd.DataFrame(index=list(df.index))
#start = time()
#for label, series in df.T.iteritems():
#	idx = []
#	#hMap = defaultdict(bool)
#	s = series.to_numpy()
#
#	for i in range(len(series)):
#		#print(series[i])
#
#		matches = np.where(series == series[i])
#		idx.append(matches)
#		#print(idx)
#
#		#print(idx)
#		#if hMap[series[i]] != 0:
#			#idx.append(hMap[series[i]])
#		#else:
#			#hMap[series[i]] = i
#	#print(label)
#	break
#end = time()
#
#print(end-start)

dic = {}
for label, series in df.T.iteritems():
	print(label)
	hMap = defaultdict(bool)
	idx = []
	for i in range(len(series)):
		if hMap[series[i]] != 0:
			idx.append((hMap[series[i]]))
		else:
			hMap[series[i]] = i
			idx.append(False)
	dic[label] = idx
dfTime = pd.DataFrame.from_dict(dic, orient = 'index').sort_index(axis = 0)

with open('allInteractions.pkl', 'wb') as f:
	pickle.dump(dfTime, f)
	f.close()
