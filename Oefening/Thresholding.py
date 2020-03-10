
import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.close()

img = cv2.imread('hc.jpg',0)
tH = input("Please provide a threshold value: ")
ret,thresh1 = cv2.threshold(img,tH,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,tH,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,tH,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,tH,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,tH,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

# ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#             cv2.THRESH_BINARY,11,2)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv2.THRESH_BINARY,11,2)
#
# titles = ['Original Image', 'Global Thresholding (v = 127)',
#             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]
#
# for i in xrange(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
