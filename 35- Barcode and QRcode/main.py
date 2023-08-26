import pyzbar.pyzbar as pyzbar
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
data = list( dict.fromkeys([]) )

while True:
    ret,frame = cap.read()
    decodeobject = pyzbar.decode(frame)
    for obj in decodeobject:
            cv2.putText(frame,str(obj.data),(30,30),font,2,(255,0,0),2)
            data.append(obj.data)
            
    cv2.imshow("QR code",frame)
    if cv2.waitKey(27) == ord('q') :
        break

data = list( dict.fromkeys(data) )
for i in data : print (i) 
cap.release()
cv2.destroyAllWindows()        