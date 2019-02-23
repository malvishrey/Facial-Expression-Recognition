import cv2
import sys
face_cascade = cv2.CascadeClassifier('C:\\Users\\Shrey Malvi\\Downloads\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
img1 = cv2.imread('download.jpg')
img = cv2.imread('download.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
index=0
for (x,y,w,h) in faces:
    img2 = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    s =str(index) + '.png'
    cropped = img1[y :y +  h , x : x + w]
    cv2.imwrite(s , cropped)
    index=index+1
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
