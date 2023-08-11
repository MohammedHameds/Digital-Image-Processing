import cv2

image = cv2.imread('pic1.jpg',0)

avarage = cv2.blur(image,(5,5))
gblur = cv2.GaussianBlur(image,(5,5),0)
median = cv2.medianBlur(image,5)
bilateralFilter = cv2.bilateralFilter(image,5,75,75)

cv2.imshow("original",image)
cv2.imshow("avarage",avarage)
cv2.imshow("gblur",gblur)
cv2.imshow("median",median)
cv2.imshow("bilateralFilter",bilateralFilter)

cv2.waitKey(0)
cv2.destroyAllWindows()