import RPi.GPIO as IO
class Infrared:
	def __init__(self):
		''' define and sets up the pin '''

		IO.setmode(IO.BCM)
		IO.setup(14,IO.IN)
		IO.setup(15,IO.IN)
		IO.setup(23,IO.IN)
		self.left=IO.input(14)
		self.middle=IO.input(15)
		self.right=IO.input(23)
		
	def detect(self):
		self.left=IO.input(14)
		self.middle=IO.input(15)
		self.right=IO.input(23)
		if self.left==True:
			#motor move left
			print("move left")
		if self.middle==True:
			if self.left==True:
				self.middle=False
				print("last was left")
			if self.right==True:
				self.middle=False
				print("last was right")
			else:
				#motor move forward
				print("move forward")
		if self.right==True:
			#motor move to the right
			print("move right")
		return self.left, self.middle, self.right
	def stop(self):
		IO.cleanup()
