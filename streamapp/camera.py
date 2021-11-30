import cv2,os,urllib.request
import numpy as np
from django.conf import settings
import datetime
import math
from django.shortcuts import render
import pandas as pd
import os

class VideoCamera(object):

	kernel = np.ones((5,5),np.uint8)
	qrcode_detectoin=cv2.QRCodeDetector()
	dic={'qr_code':[]}

	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def getAngle(self, a, b, c):
		ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
		return ang if ang < 0 else ang


	def get_frame(self):
		#success, image = self.video.read()
		img=cv2.imread('1.jpg')
		
		hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		lower_blue = np.array([0,0,168])
		upper_blue = np.array([172,111,255])
		mask = cv2.inRange(hsv, lower_blue, upper_blue)
		res = cv2.bitwise_and(img, img, mask= mask)

		erosion = cv2.erode(res,self.kernel,iterations =1)

		gray= cv2.cvtColor(erosion, cv2.COLOR_BGR2GRAY)

		opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))

		contours0, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnumber = 0

		for sl, cnt in enumerate(contours0):
			x, y, w, h = cv2.boundingRect(cnt)
			crop_img=img[y:y+h, x:x+w]

			edges = cv2.Canny(crop_img, 40, 300)
			circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 1000,
			param1=60, param2=30, minRadius=0, maxRadius=0)

			try:
				for i in circles[0, :]:
					cnumber +=1
					cx = int(i[0])
					cy = int(i[1])
					r = int(i[2])
					angle = int(self.getAngle((x, y), (x + w, y + h), (x+h, x)))
					if (angle >= 40 and angle <= 50) or (angle >= 220 and angle <= 230):
						ret, thresh1 = cv2.threshold(crop_img, 170, 255, cv2.THRESH_BINARY)
						decodedText, points, _ = self.qrcode_detectoin.detectAndDecode(thresh1)
						#here is final output as string
						img[y:y + h, x:x + w][:, :, 2] = 255
						#file.writelines(f"{decodedText} \n")
						self.dic['qr_code'].append(decodedText)
						
			except:
				pass

		df=pd.DataFrame(self.dic)
		df.to_csv("output.csv")
		cv2.imwrite('output.jpg', img)
		os.remove('1.jpg')
		ret, jpeg = cv2.imencode('.jpg', img)
		return jpeg.tobytes()

