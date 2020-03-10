import numpy as np
import cv2

img = cv2.imread('IMG_416gaps.jpg')
grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(grey,50,255,cv2.THRESH_BINARY)

cv2.namedWindow("window1", cv2.WINDOW_NORMAL)
cv2.imshow('window1', thresh)
cv2.resizeWindow('window1',600,600)

kernal = np.ones((4,4),np.uint8)
opening3 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN,kernal, iterations =4)

cv2.namedWindow("window2", cv2.WINDOW_NORMAL)
cv2.imshow('window2', opening3)
cv2.resizeWindow('window2',600,600)
cv2.waitKey()

kernal = np.ones((3,3),np.uint8)
opening4 = cv2.morphologyEx(opening3, cv2.MORPH_CLOSE,kernal, iterations =5)

cv2.imshow('window1', opening3)

cv2.imshow('window2', opening4)
cv2.waitKey()
cv2.destroyAllWindows()

# kernal = np.ones((4,4),np.uint8)
# opening2 = cv2.morphologyEx(opening3, cv2.MORPH_CLOSE,kernal, iterations =5)
#
# cv2.namedWindow("opening2", cv2.WINDOW_NORMAL)
# cv2.imshow('opening2', opening2)
# cv2.waitKey()
# cv2.destroyAllWindows()
#
#
imgSize = opening4.size
nonBlack = cv2.countNonZero(opening4)
black = imgSize-nonBlack

print(imgSize)
print (black)

gap = 590688/108          # size of hole in carton
hole = 56701/26           # pixel count for an open gap after image processing
holes = round(black/hole,0)
gaps_total = imgSize/gap

strHoles = "I count " + str(holes) + " holes and " + str(gaps_total) + " potential gaps."
print(strHoles)

strGaps = "I count " + str(gaps_total) + " gaps."
print(strGaps )

percentage = round((gaps_total-holes)/gaps_total,2)*100
strGrade = "\nThat's a " + str(percentage) + "-grade board."
print(strGrade)

import Tkinter as tk
import tkMessageBox
root = tk.Tk()
root.withdraw()
tkMessageBox.showwarning('CountBot says:', strHoles + "\n\n" + strGrade)
tkMessageBox.showwarning('CountBot says:', strGrade)
