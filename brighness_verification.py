import time
import board
from digitalio import DigitalInOut, Direction, Pull
import busio as io
import adafruit_dotstar

num_pixels = 12
pixels = adafruit_dotstar.DotStar(board.A0, board.A3, num_pixels, brightness=0.1, auto_write=False)

switch = DigitalInOut(board.D4)
switch.direction = Direction.INPUT
switch.pull = Pull.DOWN

one = True
color = (255, 255, 0)
pixels[::] = [color] + [(0, 0, 0) for _ in range(11)]
pixels.show()

while True:
    if switch.value and one:
    	pixels[::] = [color] + [(0, 0, 0) for _ in range(11)]
    	pixels.show()
    	one = False
    elif switch.value and not one:
    	pixels[::] = [color for _ in range(12)]
    	pixels.show()
    	one = True
 
    time.sleep(0.1)  # debounce delay