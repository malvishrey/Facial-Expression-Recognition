import cv2
import numpy as np
img=cv2.imread('download.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h=np.array(([-1,-1,-1],[2,2,2],[-1,-1,-1]),np.float32)
v=np.array(([-1,2,-1],[-1,2,-1],[-1,2,-1]),np.float32)

img2 = np.float32(img) / 255.0
gx = cv2.Sobel(img2, cv2.CV_32F, 1, 0, ksize=1)
gy = cv2.Sobel(img2, cv2.CV_32F, 0, 1, ksize=1)
hedge=cv2.filter2D(img,-1,h)
vedge=cv2.filter2D(img,-1,v)
print(gx.shape)
print(img2.shape)
cv2.imshow('Main', hedge)
cv2.imshow('Numpy Vertical', vedge)
cv2.waitKey()
