import cv2  
import numpy as np
import time

cam = cv2.VideoCapture(0)
#green (hMin = 44 , sMin = 61, vMin = 0), (hMax = 89 , sMax = 255, vMax = 255)

def FindArea(contours):
    for cnt in contours:
        area = cv2.contourArea(cnt)
        x,y,w,h = cv2.boundingRect(cnt)
        if area>5000:
            print("Area = ",area,"x :",x,"y",y)
while True:
    check,frame = cam.read()
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowergreen = np.array([44,61,0])
    uppergreen = np.array([79,140,224])
    greendetect = cv2.inRange(hsv,lowergreen,uppergreen)
    contours, hierarchy = cv2.findContours(greendetect,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame,contours,-1,(0,0,255),3)
    FindArea(contours)

    cv2.imshow('video',frame)
    key = cv2.waitKey(1)
    if key == 27:
        break



cam.release()
cv2.destroyAllWindows() 