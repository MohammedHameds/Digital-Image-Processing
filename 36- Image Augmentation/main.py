import imgaug.augmenters as iaa
import cv2
import glob
import matplotlib.pyplot as plt


img = cv2.imread('dog.jfif')

images = [img]

    
seq = iaa.Sequential([
    iaa.Fliplr(0.5),
    iaa.Crop(percent=(0, 0.1)), 
    iaa.Sometimes(0.5,iaa.GaussianBlur(sigma=(0, 0.5))),
    iaa.LinearContrast((0.75, 1.5)),
    iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
    iaa.Multiply((0.8, 1.2), per_channel=0.2),
    iaa.Affine(
        scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
        translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
        rotate=(-25, 25),
        shear=(-8, 8))], random_order=True) 


images_aug = seq(images=images)

for i in images_aug :
    plt.imshow(i)   
    plt.show
    
    
    
    
    
    
    
    
    
   