import pickle
import pandas as pd
import numpy as np
from collections import defaultdict

with open('COVIDdata2.pkl', 'rb') as f:
	df = pickle.load(f).sort_index(axis = 0)
	f.close()

dfTime = pd.DataFrame(index=list(df.index))

for label, series in df.T.iteritems():
	idx = []
	#hMap = defaultdict(bool)
	s = series.to_numpy()

	for i in range(len(series)):
		#print(series[i])

		matches = np.where(series == series[i])
		idx.append(matches)
		print(idx)
		break
	break
		#print(idx)
		#if hMap[series[i]] != 0:
			#idx.append(hMap[series[i]])
		#else:
			#hMap[series[i]] = i
	print(idx)

#print(df[3520])
