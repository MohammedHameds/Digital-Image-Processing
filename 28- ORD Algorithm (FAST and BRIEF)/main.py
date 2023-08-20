import cv2 
import numpy as np

img1  = cv2.imread('cats.jpg')
img2  = cv2.imread('target.jpg')

gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

sift = cv2.ORB_create()
kp1,des1 = sift.detectAndCompute(gray1,None)
kp2,des2 = sift.detectAndCompute(gray2,None)

matcher = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck = True)
matches = matcher.match(des1,des2)
matches = sorted(matches,key = lambda x : x.distance)
result = cv2.drawMatches(img1,kp1,img2,kp2,matches[:150],None,flags = 2)

cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
