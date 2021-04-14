import RPi.GPIO as GPIO
import time


try:
	GPIO.setmode(GPIO.BCM)

	TRIG = 27
	ECHO = 22

	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)

	GPIO.output(TRIG, False)
	time.sleep(2)
	print("sensor has settled")

	GPIO.output(TRIG, True)
	time.sleep(0.0001)
	GPIO.output(TRIG,False)

	while GPIO.input(ECHO) == 0:
		print("finding")
		start = time.time()

	while GPIO.input(ECHO) == 1:
		print("coming back")
		end = time.time()


	sig_time = end-start
	distance = sig_time *17150  #cm of distance

	print('Distance: {} cm'.format(distance))

	GPIO.cleanup()


except:
	GPIO.cleanup()



