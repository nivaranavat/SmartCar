
import RPi.GPIO as IO
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(14,IO.OUT)
IO.setup(15,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(17,IO.IN)
while 1:

	if (IO.input(17)==True):
		print("got here")
		IO.output(14,True)
		IO.output(15,True)
	if (IO.input(17)==False):
		print("here")
		IO.output(15,True)
		IO.output(14,True)
		IO.output(23, True)
		break
IO.cleanup()
