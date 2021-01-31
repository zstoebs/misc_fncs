import os
import nibabel as nb
import numpy as np
import math

def compute_pad(data,axis):
	div = (256 - data.shape[axis]) / 2
	return (math.floor(div), math.ceil(div))

def generate_average(dataset: str):
	sm = np.zeros((256,256,256))
	count = 0
	for fname in os.listdir():
		if '.nii' and dataset in fname:
			nii = nb.load(fname)
			data = nii.get_fdata()
			
			padded = np.pad(data,[compute_pad(data,0),compute_pad(data,1),compute_pad(data,2)])
			sm += padded
			count += 1

	avg = sm / count
	avg_img = nb.Nifti1Image(avg,np.eye(4))
	nb.save(avg_img,"%s_average" % (dataset))

