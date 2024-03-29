import cv2
import numpy as np


img = np.full((300,600,3),0,np.uint8)
cv2.namedWindow('image')

def nothing(x):
    print(x)
    
cv2.createTrackbar("B","image",0,255,nothing)
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("R","image",0,255,nothing)
switch = "0:On | 1:Off"
cv2.createTrackbar(switch,'image',0,1,nothing)

while True :
    cv2.imshow("image",img)
    if cv2.waitKey(27) == ord('q'):
        break
    
    b = cv2.getTrackbarPos("B","image")
    g = cv2.getTrackbarPos("G","image")
    r = cv2.getTrackbarPos("R","image")
    s = cv2.getTrackbarPos(switch,"image")

    
    if s == 0 :
        img [:] = 0
    else:
        img[:] = [b,g,r] 
    

cv2.destroyAllWindows()