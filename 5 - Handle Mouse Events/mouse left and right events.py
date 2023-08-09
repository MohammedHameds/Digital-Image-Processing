import cv2

events = [i for i in dir(cv2) if "EVENT" in i]
# print(events)


def click_event(event,x,y,flags,param) :
    if event == cv2.EVENT_LBUTTONDOWN :
        text = str(x) + "," + str(y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (x,y) ,font , .5, (0,255,255),2)
        cv2.imshow("Frame",img)        

    if event == cv2.EVENT_RBUTTONDOWN :
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        
        text = str(blue) + "," + str(green) + "," + str(red) 
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (x,y) ,font , .5, (255,0,255),2)
        cv2.imshow("Frame",img)               



img = cv2.imread("cat.jpg",1)
cv2.imshow("Frame",img)        
cv2.setMouseCallback('Frame' , click_event)        


cv2.waitKey(0)
cv2.destroyAllWindows()