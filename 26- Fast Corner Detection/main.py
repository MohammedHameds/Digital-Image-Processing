import cv2 
import numpy as np

image  = cv2.imread('house.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

fast = cv2.FastFeatureDetector_create()
# fast = cv2.FastFeatureDetector_create(0)

kp = fast.detect(image,None)
result = cv2.drawKeypoints(image,kp,None,(255,0,0))
print(f"Number of keypoints: {len(kp)}")
print(f"Threshold: {fast.getThreshold()}")
print(f"Neighborhood: {fast.getType()}")
print(f"NonMaxSuppression: {fast.getNonmaxSuppression()}")

cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
