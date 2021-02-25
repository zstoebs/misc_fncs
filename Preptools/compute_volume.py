import os
import numpy as np
import nibabel as nb
import argparse

def compute_volume(seg):
	return np.sum(seg != 0)

def main(path):
	i = 1
	for fname in os.listdir(path):
		if '.nii' in fname:
			nii = nb.load(fname)
			data = nii.get_fdata()
			with open('volumes.txt','a') as f:
				output = fname + ': ' + str(compute_volume(data)) + ' mm^3'
				f.write(output+'\n')
				print(str(i) + ' '  + output)
			i += 1

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Args for computing segmentation volumes.")
	parser.add_argument('--path','-p',type=str,default=os.getcwd(),help="path to segs")

	args = parser.parse_args()
	main(args.path)	
