 
import board
import busio
import adafruit_pca9685
import time
from adafruit_motor import servo

class Servo:
	def __init__(self, pca, channel ):
		self.pca=pca
		self.servo=servo.Servo(self.pca.channels[channel])
	

	def move(self,angle):
		'''
		move servo depending on the angle that you are given and the
			servo that you are given
		'''
		self.servo.angle = angle

	def reset(self):
		'''
		reset the the servos to 90

		'''
		self.servo.angle = 90

	def moveToLocation(self,x,y):
		'''
			moves the servos to the location
			needs to be fixed
		'''
		#if (180*y)/1024<90:
			#self.servo1.angle=90
		#else:
			#print("got here")
			#self.servo1.angle=(180*y)/1024
		self.servo.angle=(180*x)/1024
