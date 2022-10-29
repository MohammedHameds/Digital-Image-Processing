import cv2

img = cv2.imread('opencv.png' , 1)
img = cv2.resize(img,(512,512))
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


_, thresh = cv2.threshold(gray_img,20,255,cv2.THRESH_BINARY)

contours,hiraarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Num of contours :" , str(len(contours)))
cv2.drawContours(img,contours,-1,(0,255,255) , 2)


cv2.imshow('Original image',img)
cv2.imshow('Gray image',gray_img)
cv2.imshow('Binary Threshold',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()