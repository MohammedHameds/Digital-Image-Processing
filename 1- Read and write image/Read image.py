import cv2
import matplotlib.pyplot as plt

# print(cv2.__version__)

imageGray = cv2.imread("image.jpeg",0)
imageColors = cv2.imread("image.jpeg",1)

# cv2.imshow("Gray frame",imageGray)
# cv2.waitKey(0)

# cv2.imshow("Colored frame",imageColors)
# cv2.waitKey(0)


# plt.imshow(imageColors)
# plt.show()
# plt.imshow(imageGray)
# plt.show()

cv2.imwrite("Gray image.png",imageGray)