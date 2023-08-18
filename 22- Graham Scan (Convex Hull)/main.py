import cv2

img = cv2.imread('car.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

hull = [cv2.convexHull(contour) for contour in contours]
cv2.drawContours(img,hull,-1,(0,255,255),3)
    
cv2.imshow('image',img)
cv2.imshow('gray',gray)
cv2.imshow('thresh',thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()