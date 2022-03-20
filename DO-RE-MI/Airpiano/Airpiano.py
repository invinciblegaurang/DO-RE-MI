import cv2
import numpy as np
import imutils
import mediapipe as mp
from playsound import playsound
import pygame
import time
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

	cv2.rectangle(frame, (50,0), (148,250), (255,255,255),-1)
	cv2.putText(frame, 'a', (90,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (152,0), (248, 250), (255,255,255),-1)
	cv2.putText(frame, 'b', (190,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (116,0), (182,150), (0,0,0),-1)
	cv2.putText(frame, 'a#', (129,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

	cv2.rectangle(frame, (252,0), (348, 250), (255,255,255),-1)
	cv2.putText(frame, 'c', (290,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (352,0), (448, 250), (255,255,255),-1)
	cv2.putText(frame, 'd', (390,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (316,0), (382,150), (0,0,0),-1)
	cv2.putText(frame, 'c#', (329,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (452,0), (548, 250), (255,255,255),-1)
	cv2.putText(frame, 'e', (490,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (416,0), (482,150), (0,0,0),-1)
	cv2.putText(frame, 'd#', (429,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (552,0), (648, 250), (255,255,255),-1)
	cv2.putText(frame, 'f', (590,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (652,0), (748,250), (255,255,255),-1)
	cv2.putText(frame, 'g', (690,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (616,0), (682,150), (0,0,0),-1)
	cv2.putText(frame, 'f#', (629,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.rectangle(frame, (752,0), (848,250), (255,255,255),-1)
	cv2.putText(frame, 'A', (790,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	results=hands.process(imgRGB)

	if results.multi_hand_landmarks:
		for handLms in results.multi_hand_landmarks:
			for id,lm in enumerate(handLms.landmark):
				h,w,c=frame.shape
				cx,cy=int(lm.x*w),int(lm.y*h)
				if id in[4,8]:	
					if cx > 50 and cy > 0 and cx < 148 and cy < 250:
						pygame.mixer.Sound('a.mp3').play()
						time.sleep(0.10)
						pygame.mixer.Sound('a.mp3').stop()
					if cx > 152 and cy > 0 and cx < 248 and cy < 250:
						pygame.mixer.Sound('b.mp3').play()
						time.sleep(0.10)
						pygame.mixer.Sound('b.mp3').stop()
					if cx > 252 and cy > 0 and cx < 348 and cy < 250:
						pygame.mixer.Sound('c.mp3').play()
						time.sleep(0.10)
						pygame.mixer.Sound('c.mp3').stop()
					if cx > 352 and cy > 0 and cx < 448 and cy < 250:
						pygame.mixer.Sound('d.mp3').play()
						time.sleep(0.10)
						pygame.mixer.Sound('d.mp3').stop()
					if cx > 452 and cy > 0 and cx < 548 and cy < 250:
						pygame.mixer.Sound('e.mp3').play()
						time.sleep(0.10)
						pygame.mixer.Sound('e.mp3').stop()
					if cx > 552 and cy > 0 and cx < 648 and cy < 250:
						pygame.mixer.Sound('f.mp3').play()
						time.sleep(0.10)
						pygame.mixer.Sound('f.mp3').stop()
					if cx > 652 and cy > 0 and cx < 748 and cy < 250:
						pygame.mixer.Sound('g.mp3').play()
						time.sleep(0.10)
						pygame.mixer.Sound('g.mp3').stop()
					if cx > 752 and cy > 0 and cx < 848 and cy < 250:
						pygame.mixer.Sound('A2.mp3').play()
						time.sleep(0.10)
						pygame.mixer.Sound('A2.mp3').stop()
					if cx > 116 and cy > 0 and cx < 182 and cy < 150:
						pygame.mixer.Sound('a#.mp3').play()
						time.sleep(0.10)
						pygame.mixer.Sound('a#.mp3').stop()
					if cx > 316 and cy > 0 and cx < 382 and cy < 150:
						pygame.mixer.Sound('c#.mp3').play()
						time.sleep(0.10)
						pygame.mixer.Sound('c#.mp3').stop()
					if cx > 416 and cy > 0 and cx < 482 and cy < 150:
						pygame.mixer.Sound('d#.mp3').play()
						time.sleep(0.10)
						pygame.mixer.Sound('d#.mp3').stop()
					if cx > 616 and cy > 0 and cx < 682 and cy < 150:
						pygame.mixer.Sound('f#.mp3').play()
						time.sleep(0.10)
						pygame.mixer.Sound('f#.mp3').stop()
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