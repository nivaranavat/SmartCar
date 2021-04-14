from adafruit_motor import motor
import adafruit_pca9685
import board
import busio
import time


class Motor:

	"""Motor class to control our 4 Adafruit DC Motors in our I2C Setup"""
	
	def __init__(self,pca, channels):
		self.pca = pca #the 16 channel pca9685

		#the motors
		self.motor  = motor.DCMotor(self.pca.channels[channels[0]], self.pca.channels[channels[1]])
		self.motor.decay_mode = (motor.SLOW_DECAY)

	def moveForward(self,  wait):
		""" move the specific motor forward at full speed"""
		self.motor.throttle = 1
		time.sleep(wait)

	def moveBackward(self, wait):
		"""move the motor backwards at full speed"""
		self.motor.throttle = -1
		time.sleep(wait)

	def stop(self):	
		"""stop the motor"""
		self.motor.throttle = 0
	
	def spinFreely(self):
		"""motor will spin any direction it wants"""
		self.motor.throttle = None
	
	def moveForwardwithSpeed(self, speed, wait):
		""" move the motor forward with a given speed
			speed needs to be between 0 and 1
		"""

		self.motor.throttle = speed
		time.sleep(wait)

	def moveBackwardwithSpeed(self,speed, wait):
		""" move the motor backward with a given speed
			speed needs to be between 0 and 1"""
		self.motor.throttle = -1 * speed
		time.sleep(wait)



	 
