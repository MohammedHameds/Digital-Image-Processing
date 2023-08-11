import cv2
import datetime

cap = cv2.VideoCapture(0)

while True :
    ret , frame = cap.read()
    if ret :
        time = str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame = cv2.putText(frame,time,(0,50),font,1,(0,0,255),2)
        cv2.imshow("Frame",frame)
        if cv2.waitKey(27) == ord("q") :
          break
    else:
        break

cap.release()
cv2.destroyAllWindows()