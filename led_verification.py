import time
import adafruit_dotstar
import board
import busio as io

num_pixels = 12
pixels = adafruit_dotstar.DotStar(board.A0, board.A3, num_pixels, brightness=0.1, auto_write=False)


def clear_pixels():
    pixels[::] = [(0, 0, 0) for _ in range(12)]
    pixels.show()

def verify_color(wait, color):
    time.sleep(wait)

    for x in range(num_pixels):
        pixels[x] = color
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
    verify_color(0.25, RED)
    clear_pixels()

    verify_color(0.25, GREEN)
    clear_pixels()

    verify_color(0.25, BLUE)
    clear_pixels()

    verify_color(0.25, PURPLE)
    clear_pixels()
