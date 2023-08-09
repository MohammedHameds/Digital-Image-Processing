import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN :
        pts.append([x,y])
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.circle(img,(x,y),10,(0,255,255),-2)
        
        if len(pts) > 1 :
            cv2.line(img,pts[-1],pts[-2],(255,0,0),10)

        cv2.imshow("Frame",img)


pts = []
img = np.zeros([512,512,3],np.uint8)
cv2.imshow("Frame",img)

cv2.setMouseCallback('Frame',click_event)        
cv2.waitKey(0)
cv2.destroyAllWindows()