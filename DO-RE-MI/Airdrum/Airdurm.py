import cv2
import numpy as np
import imutils
from playsound import playsound
import time
import pygame

pygame.init()

cap = cv2.VideoCapture(0);
while True:
	_, frame = cap.read()
	frame = cv2.flip(frame,1)
	frame = imutils.resize(frame,height=700, width=900)

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lowred = np.array([131,90,106])
	highred = np.array([255,255,255])

	lowblue = np.array([40,150,116])
	highblue = np.array([255,255,255])

	red_mask = cv2.inRange(hsv, lowred, highred)
	blue_mask = cv2.inRange(hsv, lowblue, highblue)

	cv2.circle(frame, (450,520), 150, (255,255,0), 3)
	cv2.rectangle(frame, (340,420), (550,620), (255,0,0),1)
	cv2.putText(frame, 'Kick Base', (400,500), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.circle(frame, (135,450), 100, (255,255,0), 3)
	cv2.rectangle(frame, (65,380), (205, 520), (255,0,0),1)
	cv2.putText(frame, 'Snare', (100,450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.circle(frame, (140,200), 100, (255,255,0), 3)
	cv2.rectangle(frame, (70,140), (210, 270), (255,0,0),1)
	cv2.putText(frame, 'Hi Hat', (90,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.circle(frame, (450,260), 100, (255,255,0), 3)
	cv2.rectangle(frame, (380,190), (520, 330), (255,0,0),1)
	cv2.putText(frame, 'Tom', (400,260), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.circle(frame, (750,400), 100, (255,255,0), 3)
	cv2.rectangle(frame, (680,330), (820, 470), (255,0,0),1)
	cv2.putText(frame, 'Floor Tom', (670,400), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.circle(frame, (430,50), 100, (255,255,0), 3)
	cv2.rectangle(frame, (360,0), (500, 120), (255,0,0),1)
	cv2.putText(frame, 'Crash', (390,60), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	cv2.circle(frame, (750,50), 100, (255,255,0), 3)
	cv2.rectangle(frame, (680,0), (820, 120), (255,0,0),1)
	cv2.putText(frame, 'Ride', (700,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3, cv2.LINE_AA)

	contours,hierachy=cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

	for cnt in contours:
		(x,y,w,h) = cv2.boundingRect(cnt)
		cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
		# print((x,y))
		if x > 340 and y > 420 and x < 550 and y < 620:
			pygame.mixer.Sound('Kick Base.mp3').play()
			time.sleep(0.10)
			pygame.mixer.Sound('Kick Base.mp3').stop()
		if x > 65 and y > 380 and x < 205 and y < 520:
			pygame.mixer.Sound('Snare.mp3').play()
			time.sleep(0.10)
			pygame.mixer.Sound('Snare.mp3').stop()
		if x > 70 and y > 140 and x < 210 and y < 270:
			pygame.mixer.Sound('Hi Hat.mp3').play()
			time.sleep(0.10)
			pygame.mixer.Sound('Hi Hat.mp3').stop()
		if x > 380 and y > 190 and x < 520 and y < 330:
			pygame.mixer.Sound('Tom.mp3').play()
			time.sleep(0.10)
			pygame.mixer.Sound('Tom.mp3').stop()
		if x > 680 and y > 330 and x < 820 and y < 470:
			pygame.mixer.Sound('Floor_Tom.mp3').play()
			time.sleep(0.10)
			pygame.mixer.Sound('Floor_Tom.mp3').stop()
		if x > 360 and y > 0 and x < 550 and y < 120:
			pygame.mixer.Sound('Crash.mp3').play()
			time.sleep(0.10)
			pygame.mixer.Sound('Crash.mp3').stop()
		if x > 680 and y > 0 and x < 820 and y < 120:
			pygame.mixer.Sound('Ride.mp3').play()
			time.sleep(0.10)
			pygame.mixer.Sound('Ride.mp3').stop()
		break


	contours,hierachy=cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

	for cnt in contours:
		(x,y,w,h) = cv2.boundingRect(cnt)
		cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
		print((x,y))
		if x > 340 and y > 420 and x < 550 and y < 620:
			pygame.mixer.Sound('Kick Base.mp3').play()
			time.sleep(0.10)
			pygame.mixer.Sound('Kick Base.mp3').stop()
		if x > 65 and y > 380 and x < 205 and y < 520:
			pygame.mixer.Sound('Snare.mp3').play()
			time.sleep(0.10)
			pygame.mixer.Sound('Snare.mp3').stop()
		if x > 70 and y > 140 and x < 210 and y < 270:
			pygame.mixer.Sound('Hi Hat.mp3').play()
			time.sleep(0.10)
			pygame.mixer.Sound('Hi Hat.mp3').stop()
		if x > 380 and y > 190 and x < 520 and y < 330:
			pygame.mixer.Sound('Tom.mp3').play()
			time.sleep(0.10)
			pygame.mixer.Sound('Tom.mp3').stop()
		if x > 680 and y > 330 and x < 820 and y < 470:
			pygame.mixer.Sound('Floor_Tom.mp3').play()
			time.sleep(0.10)
			pygame.mixer.Sound('Floor_Tom.mp3').stop()
		if x > 360 and y > 0 and x < 550 and y < 120:
			pygame.mixer.Sound('Crash.mp3').play()
			time.sleep(0.10)
			pygame.mixer.Sound('Crash.mp3').stop()
		if x > 680 and y > 0 and x < 820 and y < 120:
			pygame.mixer.Sound('Ride.mp3').play()
			time.sleep(0.10)
			pygame.mixer.Sound('Ride.mp3').stop()
		break
	cv2.imshow("frame", frame)

	key = cv2.waitKey(1)
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()