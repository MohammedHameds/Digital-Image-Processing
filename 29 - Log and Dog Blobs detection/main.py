import cv2
import numpy as np

img  = cv2.imread('blood.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 50
params.maxThreshold = 255

params.filterByArea = True
params.minArea = 500
params.maxArea = 10000


params.filterByColor = False
params.blobColor = 0

params.filterByConvexity = True
params.minConvexity = 0.3
params.maxConvexity = 10

params.filterByInertia = True
params.minInertiaRatio = 0.01

detector  = cv2.SimpleBlobDetector_create(params)
keypoints =detector.detect(gray)
result = cv2.drawKeypoints(img,keypoints,None,(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
