# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:57:09 2021

@author: linab
"""

import matplotlib.cm as cm
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import math as m


img = io.imread("image1_bruitee_snr_10.8656.png")


def debruitageMoyenne(img):
    for line in range(1, (len(img)-1)):
        for col in range(1, len(img)-1):
            img[line, col] = moyenne_pixels(line, col)
            
def debruitageMediane(img):
    for line in range(1, (len(img)-1)):
        for col in range(1, len(img)-1):
            img[line, col] = mediane_pixels(line, col)

def moyenne_pixels(x, y):
    sum = 0
    for line in range((x-1), (x+2)):
        for col in range((y-1), (y+2)):
            sum = sum + int(img[line, col])
    sum = sum - int(img[x, y])
    res = sum/8
    return res

def mediane_pixels(x, y):
    liste = []
    for line in range((x-1), (x+2)):
        for col in range((y-1), (y+2)):
            liste.append(int(img[line, col]))
    liste.sort()
    return liste[4]

def afficherCarre(x, y):
    for line in range((x-1), (x+2)):
        for col in range((y-1), (y+2)):
            print(img[line, col])            

debruitageMediane(img)


## CALCUL SNR

from math import log, log10

imgRef = io.imread("image1_reference.png")
imgBruit = img

pSignal = 0
pBruit = 0

for line in range(0, len(imgBruit)):
    for col in range(0, len(imgBruit)):
        pSignal = pSignal + int(imgRef[line, col])**2
        pBruit = pBruit + (int(imgBruit[line, col])-int(imgRef[line, col]))**2
 

print("pSignal : ", pSignal)
print("pBruit : ", pBruit)
snr = 10*log((pSignal/pBruit), 10)
print("SNR: ", snr)

#Affichage
# io.imshow(img)
img = io.imread("image1_bruitee_snr_10.8656.png")
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 300))
axes[0].imshow(img, cmap=cm.gray)
axes[0].set_title('Bruitée')
axes[1].imshow(imgBruit, cmap=cm.gray)
axes[1].set_title('Débruitée')
axes[2].imshow(imgRef, cmap=cm.gray)
axes[2].set_title('Originale')

io.show   