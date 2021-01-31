"""
Gets the stats of a statistical CSV file.
"""

import os
import pandas as pd
import numpy as np
import json

path = os.getcwd()

with open("stats.txt",'w') as file:
	for fname in os.listdir(path):
		if '.csv' in fname:
			name = fname.replace('.csv','')
			df = pd.read_csv(path + "/" + fname).to_dict('list')
			file.write(name + ":\n")
			for stat in df.keys():
				data = [json.loads(x) for x in df[stat] if str(x) != 'nan']
				A = []
				B = []
				for vals in data:
					
					A += [vals[0]]
					B += [vals[1]]
				A, B = np.array(A), np.array(B)
				A_mean, A_std = np.mean(A), np.std(A)
				B_mean, B_std = np.mean(B), np.std(B)
				file.write(stat + " - A = (%f, %f), B = (%f, %f)\n" % (A_mean,A_std,B_mean,B_std))
			file.write("\n\n")
