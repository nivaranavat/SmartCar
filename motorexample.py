from adafruit_servokit import ServoKit
import board
import busio
import adafruit_pca9685
import time
from adafruit_motor import servo, motor
from adafruit_motorkit import MotorKit



i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c, address = 0x40)
pca.frequency = 100

motor4 = motor.DCMotor(pca.channels[6], pca.channels[7])
motor4.decay_mode = ( motor.SLOW_DECAY)

motor4.throttle = 1
time.sleep(3)
motor4.throttle = 0
time.sleep(3)
motor4.throttle = -1
time.sleep(3)
motor4.throttle = 0

"""i2c = busio.I2C(board.SCL, board.SDA)

pca = adafruit_pca9685.PCA9685(i2c)

pca.frequency = 50

servo0 = servo.Servo(pca.channels[8])
servo1 = servo.Servo(pca.channels[9])
#servo0.angle=90
#for i in range(180):
	#servo0.angle = i
#for i in range(180):
	#servo0.angle = 180-i
#time.sleep(3)
servo1.angle=180
#for i in range(180):
	#servo1.angle=i
#for i in range(180):
	#servo0.angle=180-i
"""
"""
kit = ServoKit(channels = 16)
kit.servo[1].set_pulse_width_range(1000,2000)

kit.servo[1].angle = 90
time.sleep(1)
kit.servo[1].angle = 0
"""






















"""import time
import RPi.GPIO as GPIO


#set up the pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setwarnings(False)
print("starting motor sequence")


while True:
	try:
		#makes the motor spin in on direction
		GPIO.output(2,True)
		GPIO.output(3,False)
		time.sleep(3)

		#spin the other direction
		GPIO.output(2,False)
		GPIO.output(3,True)
		time.sleep(3)
		print("one loop")
	except: 
		print("finishing up")
		GPIO.output(2,False)
		GPIO.output(3,False)
		#GPIO.cleanup()
		quit()


"""
