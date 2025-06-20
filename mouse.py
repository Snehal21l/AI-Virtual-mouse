import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui

############################
wCam, hCam = 640,480
############################

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0
while True:
    success, img = cap.read()
    lmList, bbox = detector.findPosdition(img)
    cTime= time.time()
    fps = 1/(cTime-pTime)
    pTime= cTime
    cv2.putText(img,str(int(fps)),(20,40),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
    cv2.imshow('Image',img)
    cv2.waitKey(1)