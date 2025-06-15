import cv2
import mediapipe as mp
import pyautogui

#initialize the webcam capture
cap = cv2.VideoCapture(0)

#initialize the mediapipe hands module for hand detection
hand_detector = mp.solutions.hands.Hands()

#import drawing utilities for ladnmark visualization
drawing_utils = mp.solutions.drawing_utils

#get the screen resolution for mouse control
screen_width, screen_height = pyautogui.size()

#initialize index finger
index_y=0
while True:
    #capture frame-by-frame
    ret, frame = cap.read()
    frame=cv2.resize(frame, (1920,1080))
    frame=cv2.flip(frame,1)
    frame_height, frame_width,_=frame.shape
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #process the frame to detetct hands
    output = hand_detector.process(rgb_frame)
    #get detected hands
    hands= output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            #get landmarks of the hand
            landmarks= hand.landmark
            for id, landmark in enumerate(landmarks):
                #get coordinates of the landmark
                x= int(landmark.x*frame_width)
                y= int(landmark.y*frame_height)

                #if index finger landmark  (id==8) is detected
                if id==8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    #convert finger coordinates to screen coordinates
                    index_x= screen_width/frame_width*x
                    index_y= screen_height/frame_height*y
                    #move the cursor to the index finger position
                    pyautogui.moveTo(index_x,index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) <50:
                        pyautogui.click()
                    elif abs(index_y - thumb_y) <90:
                        pyautogui.doubleClick()
                        pyautogui.sleep(1)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)