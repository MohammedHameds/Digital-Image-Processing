import cv2


image = cv2.imread('noise.jpg',0)

ret1,threth1 = cv2.threshold(image,150,255,cv2.THRESH_BINARY)

ret2,threth2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(image,(5,5),0)

ret3,threth3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow("ORiginal Image",image)
cv2.imshow("THRESH_BINARY Image",threth1)
cv2.imshow("THRESH_OTSU1 Image",threth2)
cv2.imshow("GaussianBlur Image",blur)
cv2.imshow("THRESH_OTSU2 Image",threth3)

cv2.waitKey(0)
cv2.destroyAllWindows()
