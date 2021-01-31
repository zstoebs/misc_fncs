"""
Normalize all MRI between 0 and 1. Handles negative intensities. 
"""

import os
import nibabel as nb
import numpy as np

for fname in os.listdir():
    if '.nii' in fname:
    
        nii_img = nb.load(fname)
        affine = nii_img.affine
        img_data = nii_img.get_fdata()
        
        img_data[img_data < 0] = 0
        norm_img = (img_data - np.min(img_data))/(np.max(img_data) - np.min(img_data))
        
        norm_nii_img = nb.Nifti1Image(norm_img,affine)
        nb.save(norm_nii_img,fname)
        
