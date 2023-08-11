import cv2
import matplotlib.pyplot as plt

image = cv2.imread('lena.jpeg',1)
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

plt.imshow(image)
cv2.imshow('image',image)

cv2.waitKey(0)
cv2.destroyAllWindows()