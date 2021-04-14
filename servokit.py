from servo import Servo

class ServoKit:
	""" the combination of our PCA9685 16 channel servo driver
		smart car has two servos has of right now on the I2C

	"""
	
	def __init__(self, pca):
		self.pca = pca #the pca9685 object

		#the two servo motors
		self.servo0 = Servo(self.pca, 8)
		self.servo1 = Servo(self.pca, 9)


	def movetoObject(self, location):
		""" move the servo "face" to where the object is"""
		pass
