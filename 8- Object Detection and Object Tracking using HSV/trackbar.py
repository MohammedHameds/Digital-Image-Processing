import cv2
import numpy as np

cv2.namedWindow('image')

def nothing(x) :
    print(x)
   
cv2.createTrackbar('LH','image',0,255,nothing)
cv2.createTrackbar('LS','image',0,255,nothing)
cv2.createTrackbar('LV','image',0,255,nothing)
cv2.createTrackbar('UH','image',0,255,nothing)
cv2.createTrackbar('US','image',0,255,nothing)
cv2.createTrackbar('UV','image',0,255,nothing)
    
while True : 
    img = cv2.imread("ball.png",1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('LH','image')
    ls = cv2.getTrackbarPos('LS','image')
    lv = cv2.getTrackbarPos('LV','image')
    uh = cv2.getTrackbarPos('UH','image')
    us = cv2.getTrackbarPos('US','image')
    uv = cv2.getTrackbarPos('UV','image')

    lower_b = np.array([lh,ls,lv] )
    upper_b = np.array([uh,us,uv])
    mask = cv2.inRange(hsv,lower_b, upper_b)
    result = cv2.bitwise_and(hsv,hsv,mask = mask)
    cv2.imshow("image",img)
    cv2.imshow("Mask" , mask)
    cv2.imshow("Result",result)
    
    if cv2.waitKey(27) == ord('q') :
        break    


cv2.destroyAllWindows()