import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4,1080)

detector = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    img1 = cv2.imread('mountain.jpg')
   #cv2.imshow('mountain',img1)
    img2=img1[0:1280, 0:823]


    cv2.imshow('Image',img and 'Mountain',img1)
    cv2.waitKey(1)

