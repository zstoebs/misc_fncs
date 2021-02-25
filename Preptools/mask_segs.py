import os
import numpy as np
import nibabel as nb
import argparse

def subcortical_mask(M):
	"""
	Masks the segmentation to subcortical structures. 
	"""	
	mask = M

	# left
	mask[np.where(M==9)] = 1 # thalamus
	mask[np.where(M==10)] = 1 # thalamus proper
	mask[np.where(M==11)] = 2 # caudate
	mask[np.where(M==12)] = 3 # putamen
	mask[np.where(M==13)] = 4 # pallidum

	# right
	mask[np.where(M==48)] = 5 # thalamus
	mask[np.where(M==49)] = 5 # thalamus proper
	mask[np.where(M==50)] = 6 # caudate
	mask[np.where(M==51)] = 7 # putamen
	mask[np.where(M==52)] = 8 # pallidum
	
	mask[np.where(M < 1)] = 0
	mask[np.where(M > 8)] = 0

	return mask

def main(inpath,outpath):
	
	for fname in os.listdir(inpath):
		if '.nii' in fname:
			seg = nb.load(fname)
			data = seg.get_fdata()
			
			sub_data = subcortical_mask(data)
			nii = nb.Nifti1Image(sub_data,affine=seg.affine)
			
			if not os.path.exists(outpath):
				os.makedirs(outpath)

			new_fname = fname.replace('seg','subcort',1)
			nb.save(nii,os.path.join(outpath,new_fname))

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Arguments required for masking segmentations.')
	parser.add_argument('--inpath','-i',type=str,default=os.getcwd(),help="path to segs")
	parser.add_argument('--outpath','-o',type=str,default=os.getcwd(),help="path of output segs")
	
	args = parser.parse_args()
	main(args.inpath,args.outpath)		
