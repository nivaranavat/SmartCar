import neopixel
import board
import time
import random
from collections import deque

class LED:
	"""
	class for the led lights functions
	the lights provided on the smart car are adafruit neopixel lights
	"""

	def __init__(self, pixel_pin = board.D18, num_pixels = 8, pixel_order = neopixel.GRB):
		self.pixel_pin = pixel_pin # the gpio pin number according to the board
		self.num_pixels = num_pixels #number of led lights 
		self.pixel_order = pixel_order #color order for the led lights

		#create the pixels object to represent the led lights
		self.pixels =  neopixel.NeoPixel(self.pixel_pin, self.num_pixels, 
				brightness = 0.2, auto_write = False, pixel_order = self.pixel_order)

	def fillAll(self,color, sleep_time = 0):
		"""
		fill all the pixels with one color
		param: color a length of 3 pixels represented in the pixel order
		"""
		self.pixels.fill(color)
		self.pixels.show()
		time.sleep(sleep_time)

	def random(self, wait = 0):
		"""
		random coloring for each of the lights
		param: wait : the number of time of seconds to keep the lights on
		""" 
		for i in range(0,self.num_pixels,1):
			R=random.randint(0,255)
			G=random.randint(0,255)
			B=random.randint(0,255)
			self.pixels[i]=(R,G,B)
			self.pixels.show()
		time.sleep(wait)

	def rainbow(self,iterations = 1,wait = 0):
		"""
		cycle around rainbow colors
		param: iterations number of time you want to cycle through
		param: wait is the number of seconds between each cycle
		"""
		rainbow_colors = deque([(255,0,0), (255,127,0),(255,255,0), (0,255,0), (0,0,255), (75,0,130), (148,0,211),(255,0,196)])
		
		for i in range(iterations):
			for p in range(self.num_pixels):
				self.pixels[p] = rainbow_colors[p]
				self.pixels.show()
				#time.sleep(1)
			rainbow_colors.rotate(1)
			self.pixels.show()
			time.sleep(wait)

			
	def stop(self):
		"""
		turn off all the pixels by setting all pixels to black 0
		"""
		self.fillAll((0,0,0), 0)







