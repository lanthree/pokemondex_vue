# -*- coding: utf-8 -*-
from PIL import Image

img = Image.open("./data/MSP.png")
img_width, img_height = img.size
w_size = 30
h_size = 42

for h_cnt in range(h_size):
    for w_cnt in range(w_size):
        left = w_cnt*68
        right = left+68
        upper = h_cnt*56
        lower = upper+56
        counter = h_cnt*w_size + w_cnt
        
        cropped = img.crop((left, upper, right, lower))
        cropped.save("./src/assets/icons/icons_{}.png".format(counter))