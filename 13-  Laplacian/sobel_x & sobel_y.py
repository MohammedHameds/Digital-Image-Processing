import numpy as np
import cv2

img = cv2.imread('sudocu.png',0)
sobel_x = cv2.Sobel(img,cv2.CV_64F,1,0)
sobel_y = cv2.Sobel(img,cv2.CV_64F,0,1)

sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))

compine = cv2.bitwise_or(sobel_x,sobel_y)

cv2.imshow('image',img)
cv2.imshow('sobel_x',sobel_x)
cv2.imshow('sobel_y',sobel_y)
cv2.imshow('compine',compine)

cv2.waitKey(0)
cv2.destroyAllWindows()