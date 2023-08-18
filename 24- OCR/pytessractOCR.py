import cv2
import pytesseract 

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image =cv2.imread('image.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
adaptiveThreshold = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                         cv2.THRESH_BINARY,201,11)


text = pytesseract.image_to_string(adaptiveThreshold,lang = ('eng'),config="3")


boxes = pytesseract.image_to_boxes(adaptiveThreshold,lang = ('eng'))
for b in boxes.splitlines():
    b = b.split(" ")
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(image,(x,image.shape[0]-y),(w,image.shape[0]-h),(0,255,0),3)
    cv2.putText(image, b[0], (x,image.shape[0]-y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),3)

    
data = pytesseract.image_to_data(adaptiveThreshold,lang = ('eng'))
for x,t in enumerate(data.splitlines()):
    if x != 0:
        t = t.split()
        if len(t) == 12 :
            x,y,w,h = int(t[6]),int(t[7]),int(t[8]),int(t[9])
            cv2.rectangle(image,(x,y),(w+x,h+y),(255,0,0),3)
            cv2.putText(image, t[-1], (x,y-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0),3)
        

cv2.imshow('Original',image)
cv2.imshow('Gray',gray)
cv2.imshow('AdaptiveThreshold',adaptiveThreshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
