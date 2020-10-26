"""
@author Zach Stoebner
@date 10-25-2020
@details generate a cute resume icon for github and linked in URLs
@ref https://automatetheboringstuff.com/chapter17/
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_bw(im,thresh=200):
    data = im.load()
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            if data[x,y] < (thresh,thresh,thresh,thresh):
                data[x, y] = (0, 0, 0, 255)

# load icons and generate icons of different sizes to try out
ghub_im = Image.open('github.png').convert("RGBA")
lin_im = Image.open('linkedin.png').convert("RGBA")
icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256,256)]
for sz in icon_sizes:
    ghub = ghub_im.resize(sz)
    lin = lin_im.resize(sz)
    ghub.save("github%d.png" % (sz[0]))
    lin.save("linkedin%d.png" % (sz[0]))

# generate the final icon
im = Image.new('RGBA',(700,250),'white')
draw = ImageDraw.Draw(im)
fontsFolder = '/Library/Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((25, 50), 'github.com/zstoebs', fill='black', font=arialFont)
draw.text((25, 125), 'linkedin.com/in/zstoebs', fill='black', font=arialFont)
ghub_im = Image.open('github64.png')
lin_im = Image.open('linkedin64.png')
im.paste(ghub_im,(400,30),ghub_im)
im.paste(lin_im,(400,105),lin_im)
im.save('icon.png')
