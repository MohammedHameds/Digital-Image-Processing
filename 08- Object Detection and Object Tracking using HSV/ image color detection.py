import cv2
import numpy as np

while True:
    img  = cv2.imread("ball.png",1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    l_b = np.array([50,30,30])
    u_b = np.array([130,255,255])
    
    mask = cv2.inRange(hsv,l_b,u_b)
    result = cv2.bitwise_and(img,img,mask = mask)
    
    cv2.imshow("Image",img)
    cv2.imshow("Mask" , mask)
    cv2.imshow("Result",result)
    
    if cv2.waitKey(27) == ord('q') :
        break
    
cv2.destroyAllWindows()    