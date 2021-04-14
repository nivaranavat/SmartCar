'''
from  gpiozero import Motor
from time import sleep
motor=Motor(forward=4,backward=14)
print(motor)
while True:
	motor.forward()
	sleep(5)
	motor.backward()
	sleep(5)
'''
import RPi.GPIO as GPIO
import time
try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarning(False)
	GPIO.setup(2,GPIO.OUT)
	GPIO.output(2,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(3,GPIO.LOW)
except:
	GPIO.cleanup()
GPIO.cleanup()
