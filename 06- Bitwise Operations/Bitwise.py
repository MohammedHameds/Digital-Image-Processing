import cv2
import numpy as np

image1 = np.zeros((250,500,3),np.uint8)
image1 = cv2.rectangle(image1, (200,0),(300,100),(255,255,255),-1)

image2 = np.full((250,500,3),0,np.uint8)
image2 = cv2.rectangle(image2, (0,0),(250,250),(255,255,255),-1)

btw_And = cv2.bitwise_and(image2,image1)
btw_Not = cv2.bitwise_not(image1)
btw_Or = cv2.bitwise_or(image1,image2)
btw_Xor = cv2.bitwise_xor(image1,image2)


cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.imshow("btw_And", btw_And)
cv2.imshow("btw_Not", btw_Not)
cv2.imshow("btw_Or", btw_Or)
cv2.imshow("btw_Or", btw_Xor)

cv2.waitKey(0)
cv2.destroyAllWindows()



