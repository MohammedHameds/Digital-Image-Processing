import cv2
import numpy as np

img = np.zeros([512,512,3],np.uint8)


# img = cv2.line(img, (0,0), (255,255), (255,0,0), 10)
# img = cv2.arrowedLine(img , (0,0) , (255,255) , (255,0,0) , 10)
# img = cv2.rectangle(img , (0,0) , (255,255) , (255,0,0) , 10)
# img = cv2.circle(img , (255,255) , 80 , (0,0,255) , 10)
# img = cv2.circle(img , (255,255) , 80 , (0,0,255) , -1)
# font = cv2.FONT_HERSHEY_SIMPLEX
# img = cv2.putText(img,"OpenCV", (100,255), font , 2 ,(0,0,255), 10)
# pts = np.array([[20,20],[150,150],[150,30]],np.int32)
# img = cv2.polylines(img,[pts],True,(255,0,255,10))
pts = np.array([[200,200],[300,200],[250,100]],np.int32)
img = cv2.fillPoly(img,[pts],(255,0,255))


cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()