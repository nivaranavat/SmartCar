import time


class PID:
	""" Proportional Integral Derivative controller  is a common feedback control loop 
		it is a way to to automate feedback quickly and accurately by calculating error terms
		Proportional is keeing track of the current error
		Integral is keeping track of the historical values in  the past and seeing if error is reducing
		Derivative is making a prediction about the past to make sure that we don't overshoot

	"""

	def __init__(self, kP = 1, kI =  0 , kD = 0):
		self.kP = kP
		self.kI = kI
		self.kD = kD

	def initialize(self):
		""" initialize some values, a separate function if reinitialization is needed"""
		
		#the current and previous time
		self.currTime = time.time()
		self.prevTime = self.currTime

		#previous error
		self.prevError = 0

		# the term result variables
		self.cP = 0
		self.cI = 0
		self.cD = 0

	def update(self, error, sleep = 0.2):
		time.sleep(sleep)
		
		self.currTime = time.time()
		#find the change in time
		deltaTime = self.currTime - self.prevTime
		

		#find the difference in error
		deltaError = error - self.prevError

		self.cP = error
		self.cI += error * deltaTime 
		self.cD = (deltaError/deltaTime) if deltaTime>0 else 0
		
		self.prevTime = self.currTime
		self.prevError = error

		#formula given by website
		return sum([self.kP *self.cP, self.kI*self.cI, self.kD*self.cD])

	
