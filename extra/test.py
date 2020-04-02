import time
import argparse
import neopixel
import board
from colour import Color
from noise import pnoise2

# LED strip configuration:
LED_COUNT = 144  # Number of LED pixels.
LED_PIN = board.D18  # GPIO pin connected to the pixels (18 uses PWM!).
LED_BRIGHTNESS = 1.0  # Set to 0 for darkest and 255 for brightest


# Define functions which animate LEDs in various ways.
def colorWipe(pixels, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(0, len(pixels)):
        pixels[i] = color
        pixels.show()
        time.sleep(wait_ms / 1000.0)


def playground(pixels):

    while True:
        for i in range(0, len(pixels)):
            c = Color(rgb = (1.0, 1.0, 1.0))
            pixels[i] = tuple(int(1*x) for x in c.rgb)
        pixels.show()
        time.sleep(1000.0 / 1000.0)


def mapFromTo(x, a, b, c=0.0, d=1.0):
    y = (x - a) / (b - a) * (d - c) + c
    return y


def clamp(x, minimum=0.0, maximum=1.0):
    return max(minimum, min(x, maximum))


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()

    # Create NeoPixel object with appropriate configuration.
    pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness = LED_BRIGHTNESS, auto_write = False)

    print('Press Ctrl-C to quit.')

    try:
        playground(pixels)

    except KeyboardInterrupt:
        colorWipe(pixels, (0, 0, 0), 0)
