import time
import board
import busio as io
import adafruit_ht16k33.segments

i2c = io.I2C(board.SCL, board.SDA)
display = adafruit_ht16k33.segments.Seg7x4(i2c)

def clear_7seg():
    display.fill(0)
    
def verify_7seg(wait):
    for x in range(10):
        show = "{}{}:{}{}".format(x, x, x, x)
        display.print(show)
        display.show()
        time.sleep(wait)

    display.print("12:34")
    display.show()
    time.sleep(wait)

    display.print("")
    display.show()

while True:
    verify_7seg(0.5)
    clear_7seg()
