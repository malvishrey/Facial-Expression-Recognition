import cv2
import numpy as np
img=cv2.imread('3.png')
height=56
width=56
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
scaled = cv2.resize(gray, (height, width))
y,x=scaled.shape
gx=np.zeros((x,y))
scaled = np.lib.pad(scaled, 1, 'constant', constant_values=0)
gy = np.zeros((x, y))
for i in range(y):
    a = np.convolve(scaled[i - 1, :], [1, 0, -1], 'valid')
    b = np.convolve(scaled[i, :], [2, 0, -2], 'valid')
    c = np.convolve(scaled[i + 1, :], [1, 0, -1], 'valid')
    gx[i, :] = np.sum([a, b, c], axis=0)
for j in range(x):
    a = np.convolve(scaled[:, j - 1], [1, 0, -1], 'valid')
    b = np.convolve(scaled[:, j], [2, 0, -2], 'valid')
    c = np.convolve(scaled[:, j + 1], [1, 0, -1], 'valid')
    gy[:, j] = np.sum([a, b, c], axis=0)
cv2.imshow('x',gx)
cv2.imshow('y',gy)
cv2.waitKey()
magnitude=np.sqrt(gx**2+gy**2)
mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)
print(angle)



'''
a=np.array([[1,2,3,4],[4,3,2,1],[5,6,7,8],[8,7,6,5]])
y1,x1=a.shape
a = np.lib.pad(a, 1, 'constant', constant_values=0)

print(a)
g1x=np.zeros((y1,x1))
'''
'''
for i in range(1,y+1):
    x1=np.convolve(scaled[i,:],[-1,0,1],'valid')
    gx[i-1,:]=x1
cv2.imshow('x',gx)
cv2.waitKey()
'''
