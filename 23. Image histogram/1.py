import matplotlib.pyplot as plt
import numpy as np
import cv2



# image  = np.zeros((500,700),np.uint8)
# cv2.rectangle(image,(100,100),(600,400),(255),-1)
# cv2.rectangle(image,(50,50),(300,200),(127),-1)
image = cv2.imread('lena.png',0)



# b,g,r = cv2.split(image)
# plt.hist(image.ravel(),255,[0,255])
# plt.hist(b.ravel(),255,[0,255])
# plt.hist(g.ravel(),255,[0,255])
# plt.hist(r.ravel(),255,[0,255])



# cv2.imshow('Image',image)
# cv2.imshow('Blue',b)
# cv2.imshow('Green',g)
# cv2.imshow('Red',r)

hist = cv2.calcHist(image,[0],None,[255],[0,255])
plt.plot(hist)


cv2.waitKey(0)
cv2.destroyAllWindows()


len(image.ravel())
