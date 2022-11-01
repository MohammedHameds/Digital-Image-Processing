import cv2
import tracker


cap = cv2.VideoCapture('train.mp4')
tracker = tracker.EuclideanDistTracker()

object_detector = cv2.createBackgroundSubtractorMOG2(history = 100,
                                                     varThreshold = 50)
while(cap.isOpened()):
    ret,frame = cap.read()
    height,width,_ = frame.shape
    roi = frame[340:720,500:800]             #Region of interest  
    mask = object_detector.apply(roi)
    _,mask = cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    draw = cv2.drawContours(roi,contours,-1,(0,255,255)) 

    
    detections = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300 :
            x,y,w,h = cv2.boundingRect(contour)
            detections.append([x,y,w,h])
            # cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,255),2)
            # cv2.imshow('ROI with detections',roi)    
    
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
       x,y,w,h,id = box_id
       cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,255),2)
       cv2.putText(roi,str(id),(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,
                   1,(60,0,70),3)
       
    cv2.imshow('Frame',frame)    
    cv2.imshow('Region of interest',roi)    
    cv2.imshow('Mask',mask)
    cv2.imshow('Draw contours',draw)
             
            
    if cv2.waitKey(27) == ord('q'):
        break
    
   
cv2.destroyAllWindows()
cap.release()    
