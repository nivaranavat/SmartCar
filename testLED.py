from LED import LED
import board
import neopixel

led = LED(board.D18,8, neopixel.GRB)
for i in range(3):
	led.random(1)
#led.rainbow(10,2)
led.stop()
