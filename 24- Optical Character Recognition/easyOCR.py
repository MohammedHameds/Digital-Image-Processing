import cv2
import easyocr

image =cv2.imread('image.jpg')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

adaptiveThreshold = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                         cv2.THRESH_BINARY,85,11)

reader = easyocr.Reader(['en']) 
result = reader.readtext(adaptiveThreshold)

text = ""
for i in range(len(result)):
    print(result[i][-2])

cv2.imshow('Original',image)
cv2.imshow('Gray',gray)
cv2.imshow('AdaptiveThreshold',adaptiveThreshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
