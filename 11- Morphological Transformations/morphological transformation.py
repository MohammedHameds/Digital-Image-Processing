import cv2
import numpy as np

img = cv2.imread('ball.png',0)
ret,mask = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
kernal = np.ones((5,5),np.uint8)

dilation = cv2.dilate(mask,kernal,iterations = 2)
erosion = cv2.erode(mask,kernal,iterations = 2)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal,iterations = 2)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal,iterations = 2)

cv2.imshow('Original image',img)
cv2.imshow('Thrshold',mask)
cv2.imshow('Dilation',dilation)
cv2.imshow('Erosion',erosion)
cv2.imshow('Opening',opening)
cv2.imshow('Opening',opening)

cv2.waitKey(0)
cv2.destroyAllWindows()