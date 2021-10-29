from skimage import io
from random import randint, random

img = io.imread("image2_reference.png")


# ALGO BRUIT ADDITIF
for line in range(len(img)):
    for col in range(len(img)):
        if (randint(1, 100) == 1):
            img[line, col] = img[line, col] + 20
            if (img[line, col]>255):
              img[line, col] = 255


#Affichage
# io.imshow(img)
imgRefBruit = io.imread("image1_bruitee_snr_10.8656.png")
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 300))
axes[0].imshow(imgRefBruit, cmap=cm.gray)
axes[0].set_title('Bruitée')
axes[1].imshow(img, cmap=cm.gray)
axes[1].set_title('Débruitée')
axes[2].imshow(imgRef, cmap=cm.gray)
axes[2].set_title('Originale')

io.show