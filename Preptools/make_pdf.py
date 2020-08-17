import os
from PIL import Image

path = os.getcwd()
im_lst = []
for filename in os.listdir(path):
	if ".png" in filename:
		img = Image.open(filename)
		im_lst += [img]
dataset_name = path.split('/')[-1]
pdf_name = path + '/' + dataset_name + "_report.pdf"
img0 = im_lst.pop(0)
img0.save(pdf_name,"PDF",resolution=100.0,save_all=True,append_images=im_lst)
