import numpy as np
import cv2


apple = cv2.imread('apple.png')
orange = cv2.imread('orange.png')

apple_orange = np.hstack((apple[:,:256],orange[:,256:]))
# cv2.imshow('apple_orange',apple_orange)


#gaussian pyramids for applle 
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range (6) :
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)


#gaussian pyramids for orange 
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range (6) :
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)
    
#laplacian pyramids for apple
apple_copy = gp_apple[5]
la_apple= [apple_copy]
for i in range (5,0,-1) :
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1],gaussian_extended)
    la_apple.append(laplacian)
    
#laplacian pyramids for orange
orange_copy = gp_orange[5]
la_orange= [orange_copy]
for i in range (5,0,-1) :
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1],gaussian_extended)
    la_orange.append(laplacian)    
    
    
# add left and right haves of images
apple_orange_pyramids = []
for apple_lap , orange_lap in zip(la_apple,la_orange):
    cols,rows,_ = apple_lap.shape
    laplacian = np.hstack((apple_lap[:,:int(cols/2)],orange_lap[:,int(cols/2):]))
    apple_orange_pyramids.append(laplacian)
    
#reconstruct 
apple_orange_reconstruct = apple_orange_pyramids[0]
for i in range (1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramids[i],apple_orange_reconstruct)


cv2.imshow('apple',apple)    
cv2.imshow('orange',orange)    
cv2.imshow('apple_orange',apple_orange)    
cv2.imshow('apple orange reconstruct',apple_orange_reconstruct)    

cv2.waitKey(0)
cv2.destroyAllWindows()


