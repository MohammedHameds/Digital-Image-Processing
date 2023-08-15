import cv2
import matplotlib.pyplot as plt

image = cv2.imread('lena.png')
b,g,r = cv2.split(image)

plt.hist(image.ravel(),255,[0,255])
plt.hist(b.ravel(),255,[0,255])
plt.hist(g.ravel(),255,[0,255])
plt.hist(r.ravel(),255,[0,255])
plt.show()

cv2.imshow('Image',image)
cv2.imshow('Blue',b)
cv2.imshow('Green',g)
cv2.imshow('Red',r)

colors = ['b','g','r']
for i,color in enumerate(colors):
    hist = cv2.calcHist(image,[i],None,[256],[0,256])
    plt.plot(hist)    

cv2.waitKey(0)
cv2.destroyAllWindows()


