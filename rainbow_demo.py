import time
import adafruit_dotstar
import board

num_pixels = 12
pixels = adafruit_dotstar.DotStar(board.A0, board.A3, num_pixels, brightness=0.1, auto_write=False)


def clear_pixels():
    pixels[::] = [(0, 0, 0) for _ in range(12)]
    pixels.show()
 
def slice_rainbow(wait):
    clear_pixels
    pixels[::6] = [RED] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[1::6] = [ORANGE] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[2::6] = [YELLOW] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[3::6] = [GREEN] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[4::6] = [BLUE] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[5::6] = [PURPLE] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)

RED = (0, 0, 255)
YELLOW = (150, 0, 255)
ORANGE = (40, 0, 255)
GREEN = (255, 0, 0)
TEAL = (255, 120, 0)
CYAN = (255, 255, 0)
BLUE = (0, 255, 0)
PURPLE = (0, 255, 180)
MAGENTA = (0, 20, 255)
WHITE = (255, 255, 255)

while True:

    slice_rainbow(0.25)
    time.sleep(0.5)
    clear_pixels()
