# -*- coding: utf-8 -*-
import numpy as np
def convolve(image, weight):
    height, width = image.shape
    h, w =weight.shape
    height_new = height -h + 1
    width_new = width - w + 1
    image_new = np.zeros((height_new,width_new),dtype = np.float)
    for i in xrange(height_new):
        for j in xrange(width_new):
            image_new[i,j] = np.sum(image[i:i+h,j:j+w] * weight)
    image_new = image_new.clip(0,255)
    image_new = np.rint(image_new).astype('uint8')
    return image_new
