from LED import LED
import board
import neopixel

led = LED(board.D18,8, neopixel.GRB)
#xfor i in range(10):
	#led.random(1)
led.rainbow(10,2)
led.stop()
