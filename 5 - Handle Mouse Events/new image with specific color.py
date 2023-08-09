import cv2
import numpy as np

def click_event(event,x,y,flags,param) :
    if event == cv2.EVENT_LBUTTONDOWN :
        blue = image[y, x, 0]
        green = image[y, x, 1]
        red = image[y, x, 2]     

        new_img = np.zeros([image.shape[0],image.shape[1],3], dtype=np.uint8)
        new_img[::] = [blue,green,red]
        cv2.imshow("New image",new_img)

        
image = cv2.imread('cat.jpg')
cv2.imshow("image",image)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()        
        