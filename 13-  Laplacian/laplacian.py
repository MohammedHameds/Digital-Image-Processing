import numpy as np
import cv2

img = cv2.imread('sudocu.png',0)
lap = cv2.Laplacian(img,cv2.CV_64F,ksize = 3)
lap = np.uint8(np.absolute(lap))

cv2.imshow('image',img)
cv2.imshow('laplacian',lap)
cv2.waitKey(0)
cv2.destroyAllWindows()