import cv2
import numpy as np

cap = cv2.VideoCapture('test.mp4')
forcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',forcc, 30,(1048,720))



_,frame1 = cap.read()
_,frame2 = cap.read()

while(True):
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations = 10)
    contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('dilated',dilated)
    
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 1500 :
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,255),3)
            cv2.putText(frame1,'Status: {}'.format('Movement'),(10,20)
                    ,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
            
    image = cv2.resize(frame1,(1048,720))  
    out.write(image)       
    cv2.imshow("Frame",frame1) 
    cv2.imshow("Thresh",thresh)
    cv2.imshow("Dilation",dilated)
    
    frame1 = frame2
    _,frame2 = cap.read()
    if cv2.waitKey(27) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
