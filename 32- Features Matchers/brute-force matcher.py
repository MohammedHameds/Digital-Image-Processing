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
result = cv2.drawMatches(img1,kp1,img2,kp2,matches,None,flags = 2)
cv2.imshow('result 1',result)

matcher = cv2.BFMatcher()
matches = matcher.knnMatch(des1,des2,k=2)
best_matches = [[m] for m , n in matches if m.distance < 0.75 * n.distance]
result = cv2.drawMatchesKnn(img1,kp1,img2,kp2,best_matches,None,flags=2)
cv2.imshow('result 2',result)

cv2.waitKey(0)
cv2.destroyAllWindows()
