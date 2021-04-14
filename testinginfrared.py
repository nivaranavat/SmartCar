
import RPi.GPIO as IO
from infrared import Infrared
infrared=Infrared()

from LED import LED
led = LED()

from pca import PCA
from motorkit import MotorKit
import time

pca = PCA(0x40).getPCA()
mkit = MotorKit(pca)
mkit.changeSpeed(0.5)
while 1:
	try:
		led.random(0)
		left,middle, right = infrared.detect()
		mkit.changeSpeed(0.25)
		if middle: mkit.forward()
		elif left: 
			#mkit.changeSpeed(0.20)
			mkit.forwardLeft()
		elif right:
			#mkit.changeSpeed(0.20) 
			mkit.forwardRight()
		else: mkit.forward()
		#if middle and left: 
		#	mkit.forwardLeft()
		#	mkit.backward()	
		mkit.stop()
		#led.stop()
		#time.sleep(1)
		

	except KeyboardInterrupt:
		break
#while 1:
	#infrared.detect() 
led.stop()
infrared.stop()
mkit.stop()

