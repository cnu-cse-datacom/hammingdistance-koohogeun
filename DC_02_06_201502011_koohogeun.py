import random
import numpy as np
import pandas as pd
from hamming_parctice import hamming

df = pd.read_csv('sample.csv',names=['word','bin'])

leng = df.shape
count = 1
for i in range(0, leng[0]):
	for j in range(i + 1, leng[0]):
		hd = hamming(df.iloc[i,1],df.iloc[j,1])
		print(count,"(",df.iloc[i,0],df.iloc[j,0],")hamming_distance:",hd)
		if count == 1:
			min_ = hd
		if hd < min_:
			min_ = hd
		count = count + 1

print("min hamming distance", min_)
