import cv2

img = cv2.imread('cars.jpg',1)
image = cv2.imread('cars.jpg',1)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)




for contour in contours:
    hull = cv2.convexHull(contour)    
    cv2.drawContours(img,[hull],-1,(0,255,255),2)
    cv2.drawContours(image,[contour],0,(0,255,255),2)
    
    
cv2.imshow('Hull',img)
cv2.imshow('Contour',image)

# cv2.imshow('Gray image',gray)
# cv2.imshow('Threshhold',thresh)    
cv2.waitKey(0)
cv2.destroyAllWindows()