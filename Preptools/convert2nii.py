import os
import nibabel as nb

path = os.getcwd()
for fname in os.listdir(path):
    if '.nii' in fname:
        img = nb.load(fname)
        splits = fname.split('.')
        filename = "".join(splits[:-1]) + '.' + splits[-1]
        nb.save(img,filename.replace('.nii','.nii.gz'))
