import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_pixel(image, center, x, y):
    new_value = 0
    try:
        if image[x][y]>center:
            new_value = 1
    except:
        pass
    return new_value

def lbp(image):
    height = image.shape[0]
    width = image.shape[1]
    pat = np.zeros((height, width), np.uint8)
    for i in range(height):
        for j in range(width):
            center = image[i, j]
            val_ar = []
            val_ar.append(get_pixel(image, center, i-1, j-1))
            val_ar.append(get_pixel(image, center, i - 1, j))
            val_ar.append(get_pixel(image, center, i - 1, j + 1))
            val_ar.append(get_pixel(image, center, i, j + 1))
            val_ar.append(get_pixel(image, center, i + 1, j + 1))
            val_ar.append(get_pixel(image, center, i + 1, j))
            val_ar.append(get_pixel(image, center, i + 1, j - 1))
            val_ar.append(get_pixel(image, center, i, j - 1))
            val = 0
            for m in range(8):
                val += val_ar[m]*(2**m)
            pat[i,j] = val

    return pat

img = cv2.imread("schrodinger.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
result = lbp(gray)

cv2.imshow("image", img)    
cv2.imshow("result",result)
cv2.imwrite('result.png',result)  
  
cv2.waitKey(0)
cv2.destroyAllWindows()
    
    
    