import cv2
import keras_ocr
import matplotlib.pyplot as plt

pipeline = keras_ocr.pipeline.Pipeline()

image = cv2.imread('image.jpg')

predictions = pipeline.recognize([image])

for image, prediction in zip([image], predictions):
    keras_ocr.tools.drawAnnotations(image=image, predictions=prediction)
    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
