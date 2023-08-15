import cv2

image = cv2.imread('noise.jpg',0)
_,th1 = cv2.threshold(image,150,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(image,(5,5),0)
_,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("original Image",image)
cv2.imshow("THRESH_BINARY Image",th1)
cv2.imshow("THRESH_OTSU1 Image",th2)
cv2.imshow("GaussianBlur Image",blur)
cv2.imshow("THRESH_OTSU2 Image",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
