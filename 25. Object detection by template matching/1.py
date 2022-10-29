import cv2
import numpy as np


img = cv2.imread('messi.jfif',1)
gray = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)
template = cv2.imread('template.jpg',0)


w,h = template.shape[::-1]

res = cv2.matchTemplate(gray,template,cv2.TM_CCORR_NORMED)
# print(res)

threshold = 0.99
loc = np.where(res >= threshold)
print(loc)


for pt in zip(*loc[::-1]):
    print(pt)
    print(w)
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)



cv2.imshow('Original image',img)
# cv2.imshow('Template image',template)
# cv2.imshow('Res' ,res)

cv2.waitKey(0)
cv2.destroyAllWindows()