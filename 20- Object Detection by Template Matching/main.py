import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread('template.jpg',0)
h,w = template.shape

res = cv2.matchTemplate(gray,template,cv2.TM_CCORR_NORMED)

thresh = 0.99
loc = np.where(res>=thresh)
h_res = loc[0][0]
w_res = loc[1][0]
cv2.rectangle(img,(w_res,h_res),(w+w_res, h+h_res),(0,255,255),3)
cv2.imshow('result',res)
cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for meth in methods:
    method = eval(meth)
    res = cv2.matchTemplate(gray,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
        
    bottom_right = (top_left[0] + w, top_left[1] + h)
    plt.subplot(121)
    plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result')
    plt.xticks([])
    plt.yticks([])
    plt.subplot(122)
    plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()