"""
Montages axial slices in the order of epochs. The first image is the original image. 
"""

import os
import numpy as np
import nibabel as nb
import math
import matplotlib.pyplot as plt
from skimage.util import montage

# path to original dataset for the real image
orig_path = "/absolute/path/to/ground/truths"
dataset = os.listdir(orig_path)

def compute_pad(data,axis):
	div = (256 - data.shape[axis]) / 2
	return (math.floor(div), math.ceil(div))

# get the middle axial slice and convert to an image object
def get_axial(fname):
	nii = nb.load(fname)
	data = nii.get_fdata()
	axial = data[:,:,data.shape[2] // 2]
	return axial	

# find the root of the nearest perfect square above the current number
def find_root(num):
	return math.floor(math.sqrt(num)) + 1

# create a montage of subplots of grayscale images
def plt_montage(imgs,labels,title):
	assert len(imgs) == len(labels)
	
	root = find_root(len(imgs))	
	f, ax = plt.subplots(root,root)
	
	row = -1
	for i, pair in enumerate(zip(imgs,labels)):
		img, label = pair
		col = i % root
		row += 1 if col == 0 else 0

		axis = ax[row,col]
		axis.imshow(img,cmap="gray")
		axis.set_title("Epoch = %s" % (str(label)))
	
	plt.tight_layout()	
	plt.show()
	#f.savefig(title+".png",transparent=True)

# group axial slices according to subject's session
sesses = dict()
for fname in os.listdir():
	if ".nii" in fname:
		splits = fname.split('_')

		key = '_'.join(splits[:2])
		if not key in sesses.keys():
			origs = list(filter(lambda f: key in f, dataset))
			try:
				assert len(origs) == 1
			except AssertionError:
				print(key)
				print(origs)
				raise ValueError("Bad key")
			sesses[key] = [(get_axial(os.path.join(orig_path,origs[0])),0)]

		last = splits[-1]
		epoch = int(''.join(list(filter(str.isdigit,last))))
			
		sesses[key] += [(get_axial(fname),epoch)]

# compose the montage 
for key in sesses.keys():
	lst = sesses[key]
	lst.sort(key=lambda x: x[1])
	
	imgs = [np.rot90(x[0]) for x in lst]
	epochs = [x[1] for x  in lst]
	
	padded = [np.pad(img,[compute_pad(img,0),compute_pad(img,1)]) for img in imgs]
	#plt_montage(padded,epochs,key) 
	
	stack = np.transpose(np.dstack(padded),(2,0,1))
	m = montage(stack)
	x, y = m.shape
	cols = y / 256
	
	plt.figure(figsize=(12,12))
	plt.imshow(m,cmap="gray")
	
	row = -1
	for i, epoch in enumerate(epochs):
		col = i % cols
		row += 1 if col == 0 else 0
		plt.text( col*256, (row+1)*256 - 10, "Epoch = %d" % (epoch),color="white",fontsize=11) # cols correspond to the x-axis of the figure

	plt.savefig(key+".png")
	plt.close('all')
