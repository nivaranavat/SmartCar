from pca import PCA
from motor import Motor
import time

class MotorKit:

	"""  the 4 Adafruit DC motors kit"""


	def __init__(self, pca):
		self.pca = pca

		self.motor1 = Motor(self.pca, [0,1])
		self.motor2 = Motor(self.pca, [3,2])
		self.motor3 = Motor(self.pca, [4,5])
		self.motor4 = Motor(self.pca,[6,7])
		
		self.speed = 0.5 #default to 0.5 change it when needed, turns need slower

	def changeSpeed(self, speed):
		self.speed = speed

	def forward(self):
		
		""" move all motors forward for point one second """


		self.motor1.moveForwardwithSpeed(self.speed,0)
		self.motor2.moveForwardwithSpeed(self.speed,0)
		self.motor3.moveForwardwithSpeed(self.speed,0)
		self.motor4.moveForwardwithSpeed(self.speed,0)
		time.sleep(0.1)
	
	def backward(self):
		""" move all motors backward for point one second """
		self.motor1.moveBackwardwithSpeed(self.speed,0)
		self.motor2.moveBackwardwithSpeed(self.speed,0)
		self.motor3.moveBackwardwithSpeed(self.speed,0)
		self.motor4.moveBackwardwithSpeed(self.speed,0)
		time.sleep(0.1)

	def stop(self):
		"""  stop all movements"""
		self.motor1.stop()
		self.motor2.stop()
		self.motor3.stop()
		self.motor4.stop()

	def forwardLeft(self):
		self.motor4.moveForwardwithSpeed(self.speed,0)
		self.motor3.moveForwardwithSpeed(self.speed,0)
		time.sleep(0.1)

	def forwardRight(self):
		self.motor1.moveForwardwithSpeed(self.speed,0)
		self.motor2.moveForwardwithSpeed(self.speed,0)
		time.sleep(0.1)
	
	def backwardLeft(self):
		self.motor1.moveBackwardwithSpeed(self.speed,0)
		self.motor2.moveBackwardwithSpeed(self.speed,0)
		time.sleep(0.1)

	def backwardRight(self):
		self.motor3.moveBackwardwithSpeed(self.speed,0)
		self.motor4.moveBackwardwithSpeed(self.speed,0)
		time.sleep(0.1)
