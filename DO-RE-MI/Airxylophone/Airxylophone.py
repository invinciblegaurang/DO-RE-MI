import cv2
import numpy as np
import imutils
import mediapipe as mp
from playsound import playsound
import time
import pygame

pygame.init()
HIGH_VALUE = 10000
WIDTH = HIGH_VALUE
HEIGHT = HIGH_VALUE

mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils

pTime=0
cTime=0

cap = cv2.VideoCapture(0);
while True:
	_, frame = cap.read()
	frame = cv2.flip(frame,1)
	frame = imutils.resize(frame,height=700, width=900)
	imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	cv2.rectangle(frame, (50,250), (148,450), (128,0,128),-1)
	cv2.putText(frame, 'c', (90,350), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (152,240), (248, 460), (139,0,0),-1)
	cv2.putText(frame, 'd', (190,350), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (252,230), (348, 470), (235,206,135),-1)
	cv2.putText(frame, 'e', (290,350), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (352,220), (448, 480), (0,100,0),-1)
	cv2.putText(frame, 'f', (390,350), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (452,210), (548, 490), (144,238,144),-1)
	cv2.putText(frame, 'g', (490,350), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (552,200), (648, 500), (0,255,255),-1)
	cv2.putText(frame, 'A', (590,350), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (652,190), (748,510), (0,165,255),-1)
	cv2.putText(frame, 'B', (690,350), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (752,180), (848,520), (59,70,227),-1)
	cv2.putText(frame, 'C', (790,350), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	results=hands.process(imgRGB)


	if results.multi_hand_landmarks:
		for handLms in results.multi_hand_landmarks:
			for id,lm in enumerate(handLms.landmark):
				h,w,c=frame.shape
				cx,cy=int(lm.x*w),int(lm.y*h)
				if id in[4,8]:
					if cx > 50 and cy > 250 and cx < 148 and cy < 450:
						pygame.mixer.Sound('c1.wav').play()
						time.sleep(0.10)
						pygame.mixer.Sound('c1.wav').stop()
					if cx > 152 and cy > 240 and cx < 248 and cy < 460:
						pygame.mixer.Sound('d1.wav').play()
						time.sleep(0.10)
						pygame.mixer.Sound('d1.wav').stop()
					if cx > 252 and cy > 230 and cx < 348 and cy < 470:
						pygame.mixer.Sound('e1.wav').play()
						time.sleep(0.10)
						pygame.mixer.Sound('e1.wav').stop()
					if cx > 352 and cy > 220 and cx < 448 and cy < 480:
						pygame.mixer.Sound('f.wav').play()
						time.sleep(0.10)
						pygame.mixer.Sound('f.wav').stop()
					if cx > 452 and cy > 210 and cx < 548 and cy < 490:
						pygame.mixer.Sound('g.wav').play()
						time.sleep(0.10)
						pygame.mixer.Sound('g.wav').stop()
					if cx > 552 and cy > 200 and cx < 648 and cy < 500:
						pygame.mixer.Sound('a.wav').play()
						time.sleep(0.10)
						pygame.mixer.Sound('a.wav').stop()
					if cx > 652 and cy > 190 and cx < 748 and cy < 510:
						pygame.mixer.Sound('b.wav').play()
						time.sleep(0.10)
						pygame.mixer.Sound('b.wav').stop()
					if cx > 752 and cy > 180 and cx < 848 and cy < 520:
						pygame.mixer.Sound('c2.wav').play()
						time.sleep(0.10)
						pygame.mixer.Sound('c2.wav').stop()
		mpDraw.draw_landmarks(frame,handLms,mpHands.HAND_CONNECTIONS)

		cTime=time.time()
		fps=1/(cTime-pTime)
		pTime = cTime

		cv2.putText(frame, str(int(fps)), (800, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)

	
	cv2.imshow("frame", frame)

	key = cv2.waitKey(1)
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()