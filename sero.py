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
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,GPIO.HIGH)
time.sleep(5)
GPIO.output(17,GPIO.LOW)
GPIO.cleanup()
