import cv2
import numpy as np
import os

img = cv2.imread('ms.jpg',1)
# Using cv2 to display images
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('msgrey.jpg', img)

# Using matplotlib to plot images
    # from matplotlib import pyplot as plt
    # plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    # plt.show()
# for some reason the Atom Runner utility doesn't wait for
# for the keypress before use matplotlib
px = img[100,100]
print px
blue = img[100,100,0]
print blue
print(img.size)
