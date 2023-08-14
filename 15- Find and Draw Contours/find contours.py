import cv2

image = cv2.imread('opencv.png')
imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,20,255,0)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image,contours,-1,(0,255,255),3) 

cv2.imshow('image',image)
cv2.imshow('thresh',thresh)
cv2.imshow('imgray',imgray)


cv2.waitKey(0)
cv2.destroyAllWindows()
