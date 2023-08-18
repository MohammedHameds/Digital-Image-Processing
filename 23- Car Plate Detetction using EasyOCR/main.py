import cv2
import easyocr
import numpy as np

img= cv2.imread('car.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bfilter = cv2.bilateralFilter(gray,11,17,17)
edged = cv2.Canny(bfilter,30,200)
contours,_ = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours,key=cv2.contourArea, reverse = True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour,10,True)
    if len(approx) == 4 :
        location = approx
        break

[x1,y1] = location[0][0]
[x2,y2] = location[2][0]

cropped_image = gray[y1-3:y2+3,x1-3:x2+3]

reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_image)

plat_text = result[0][-2]
accuracy = int(round((result[0][-1]),2)*100)
print("result is",plat_text,"with accuracy :" ,str(accuracy) ,"%")

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,plat_text,(x1,y1),font,1,(0,255,255),3)

cv2.imshow('frame',img)
cv2.imshow('bfilter',bfilter)
cv2.imshow('edged',edged)
cv2.imshow('cropped_image',cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()