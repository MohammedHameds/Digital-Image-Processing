import cv2


img = cv2.imread('shapes.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
contours , _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# draws = cv2.drawContours(gray,contours,-1,(0,255,255),1)


for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01 * cv2.arcLength(contour, True),True)
    cv2.drawContours(img,[approx],0,(0,100,255),5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    print(len(approx))
    
    if len(approx) == 3 :
        cv2.putText(img,'Triangle',(x+35,y-100),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

    elif len(approx) == 4 :   
        x1,y1,w,h = cv2.boundingRect(approx)
        print(x1,y1,w,h)
        aspect_ratio = float(w)/h
        print(aspect_ratio)
        if aspect_ratio > 0.95 and aspect_ratio < 1.05 :
            cv2.putText(img,'Square',(x+35,y-100),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
        else :
            cv2.putText(img,'Rectangle',(x+35,y-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

    elif len(approx) == 5 :   
        cv2.putText(img,'Pentagon',(x+35,y-53),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

    elif len(approx) == 6 :   
        cv2.putText(img,'Hexagon',(x+35,y-53),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

    elif len(approx) == 10 :   
        cv2.putText(img,'Star',(x+35,y-53),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
            
    elif len(approx) == 12 :   
        cv2.putText(img,'Oval',(x+75,y-45),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
           
    else :
        cv2.putText(img,'Circle',(x-5,y-5),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
                   
    
cv2.imshow('Original image' , img)
cv2.imshow('THreshold' , thresh)
# cv2.imshow('Contours' , draws)

cv2.waitKey(0)
cv2.destroyAllWindows()
