import cv2 
import numpy as np

image  = cv2.imread('home.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp,des = sift.detectAndCompute(gray,None)
result = cv2.drawKeypoints(image,kp,None,(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
