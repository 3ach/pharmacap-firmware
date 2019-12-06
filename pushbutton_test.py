import time
import board
from digitalio import DigitalInOut, Direction, Pull
import busio as io
import adafruit_ht16k33.segments

i2c = io.I2C(board.SCL, board.SDA)
display = adafruit_ht16k33.segments.Seg7x4(i2c)

 
switch = DigitalInOut(board.D4)
switch.direction = Direction.INPUT
switch.pull = Pull.DOWN

value = 0

while True:
    if switch.value:
    	value += 1

    display.print("{:04}".format(value))
    display.show()
 
    time.sleep(0.05)  # debounce delay