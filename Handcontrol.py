import cv2
import mediapipe as mp

cap=cv2.VideoCapture(0)
mphand=mp.solutions.hands
hands=mphand.Hands()
mpdraw=mp.solutions.drawing_utils

while True:
    ret,img=cap.read()
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=hands.process(imgrgb)
    # print(result.multi_hand_landmarks)

    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            mpdraw.draw_landmarks(img,handlms)





    cv2.imshow("img",img)
    key=cv2.waitKey(1)
    if key==27:
        break