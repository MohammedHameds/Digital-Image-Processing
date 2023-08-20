import cv2 


image = cv2.imread('image.jpg')

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

(boxes,weights) = hog.detectMultiScale(image,winStride = (4,4),
                                                padding = (8,8),
                                                scale = 1.05)

for (x,y,w,h) in boxes :
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),3)


cv2.imshow('image',image)

cv2.waitKey(0)
cv2.destroyAllWindows()