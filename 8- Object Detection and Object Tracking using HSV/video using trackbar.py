import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow('trackbar')

def nothing(x) :
    print(x)
   
cv2.createTrackbar('LH','trackbar',0,255,nothing)
cv2.createTrackbar('LS','trackbar',0,255,nothing)
cv2.createTrackbar('LV','trackbar',0,255,nothing)
cv2.createTrackbar('UH','trackbar',0,255,nothing)
cv2.createTrackbar('US','trackbar',0,255,nothing)
cv2.createTrackbar('UV','trackbar',0,255,nothing)
    
while True : 
    ret,frame = cap.read()
    if ret == True :
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('LH','trackbar')
    ls = cv2.getTrackbarPos('LS','trackbar')
    lv = cv2.getTrackbarPos('LV','trackbar')
    uh = cv2.getTrackbarPos('UH','trackbar')
    us = cv2.getTrackbarPos('US','trackbar')
    uv = cv2.getTrackbarPos('UV','trackbar')

    lower_b = np.array([lh,ls,lv] )
    upper_b = np.array([uh,us,uv])
    mask = cv2.inRange(hsv,lower_b, upper_b)
    result = cv2.bitwise_and(hsv,hsv,mask = mask)
    
    cv2.imshow("image",frame)
    cv2.imshow("Mask" , mask)
    cv2.imshow("Result",result)
    
    if cv2.waitKey(27) == ord('q') :
        break    

cap.release()
cv2.destroyAllWindows()