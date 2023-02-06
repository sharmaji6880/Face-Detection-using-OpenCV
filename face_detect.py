import cv2 as cv
import numpy as np
def resizeImage(frame,scale):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions)

img=cv.imread("C:/Users/HP/Pictures/Camera Roll/WIN_20230206_17_11_37_Pro.jpg")
img=resizeImage(img,0.5)
#cv.imshow("image",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("gray",gray)


haar_cascade=cv.CascadeClassifier('haar_face.xml')
faces_rect=haar_cascade.detectMultiScale(gray,1.1,4)

print(f"No. of faces detected {len(faces_rect)}")

for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


cv.imshow("Faces detected",img)

cv.waitKey(0)
