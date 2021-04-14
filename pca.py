import board
import busio
import adafruit_pca9685

class PCA:
	""" Adafruit PCA9685 16 Channel Servo Driver Class""" 

	def __init__(self,address = 0x40):
		self.i2c = busio.I2C(board.SCL, board.SDA)

		#the PCA9685 object	
		self.pca = adafruit_pca9685.PCA9685(self.i2c, address = address)
		
		self.pca.frequency =50 #default 50, can change if needed

	def setFreq(self, freq):
		""" set the PWM(pulse width movement) frequency"""
		self.pca.frequency = freq
	def getPCA(self):
		return self.pca

