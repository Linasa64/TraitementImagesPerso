# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 09:43:15 2021

@author: linab
"""

from skimage import io
from random import randint, random

img = io.imread("image2_reference.png")


# ALGO SALT AND PEPPER
for line in range(len(img)):
    for col in range(len(img)):
        if (randint(1, 10) == 1):
            if (random() <0.5):
                img[line, col] = 0
            else:
                img[line, col] = 255

#Affichage
io.imshow(img)
io.show