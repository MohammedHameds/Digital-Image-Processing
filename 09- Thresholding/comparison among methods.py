import cv2

img = cv2.imread('noise.jpg',0)

_,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
th6 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,111,2)
th7 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,111,2)
_,th8 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(img,(5,5),0)
_,th9 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("original Image",img)
cv2.imshow("THRESH_BINARY",th1)
cv2.imshow("THRESH_BINARY_INV",th2)
cv2.imshow("THRESH_TRUNC",th3)
cv2.imshow("THRESH_TOZERO",th4)
cv2.imshow("THRESH_TOZERO_INV",th5)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C",th6)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C",th7)
cv2.imshow("THRESH_OTSU",th8)
cv2.imshow("THRESH_OTSU with image smoothing",th9)




cv2.waitKey(0)
cv2.destroyAllWindows()