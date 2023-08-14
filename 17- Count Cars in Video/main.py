import cv2
import numpy as np
from tracker import *

cap = cv2.VideoCapture('train.mp4')
forcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',forcc, 30,(1048,720))

tracker = EuclideanDistTracker()
object_detector = cv2.createBackgroundSubtractorMOG2(history = 100,varThreshold = 40)

while cap.isOpened() :

    _,frame = cap.read()
    height,width,_ = frame.shape
    roi = frame[340: 720,500: 800]  # Region of interest
    
    mask = object_detector.apply(roi)
    _,thresh = cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    detetctions = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 150 :
            x,y,h,w = cv2.boundingRect(contour)
            detetctions.append([x,y,h,w])
    boxes_ids = tracker.update(detetctions)
    for box_id in boxes_ids:
        x,y,h,w,id = box_id
        cv2.putText(roi,str(id),(x,y),0,1,(0,0,255),3)
        cv2.rectangle(roi,(x,y),(x+w,h+y),(0,255,255),3)
        

    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)
    cv2.imshow("thresh",thresh)
    
    image = cv2.resize(frame,(1048,720))  
    out.write(image)
    if cv2.waitKey(27) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
out.release()    
    
        
    
        
     
