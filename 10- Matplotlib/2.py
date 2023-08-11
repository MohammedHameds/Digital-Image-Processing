import cv2
import matplotlib.pyplot as plt

image = cv2.imread('lena.jpeg',0)

ret,th1 = cv2.threshold(image,150,255,cv2.THRESH_BINARY)
ret,th2 = cv2.threshold(image,150,255,cv2.THRESH_BINARY_INV)
ret,th3 = cv2.threshold(image,150,255,cv2.THRESH_TRUNC)
ret,th4 = cv2.threshold(image,150,255,cv2.THRESH_TOZERO)
ret,th5 = cv2.threshold(image,150,255,cv2.THRESH_TOZERO_INV)

names = ['ORIGINAL','THRESH_BINARY','THRESH_BINARY_INV',
         'THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
filters  = [image,th1,th2,th3,th4,th5]

plt.figure(figsize=(10, 7))
for i in range (len(names)) :
    plt.subplot(2,3,i+1)
    plt.imshow(filters[i])
    plt.title(names[i])
    plt.xticks([])
    plt.yticks([])
plt.show()