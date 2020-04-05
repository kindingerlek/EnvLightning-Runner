import board
from  envlight.animator_controller import AnimatorController
import time
import neopixel
import argparse
from envlight.tools import cmath

# LED strip configuration:
LED_COUNT = 288             # Number of LED pixels.
LED_PIN = board.D18         # GPIO pin connected to the pixels (18 uses PWM!).
LED_BRIGHTNESS = .35        # Set to 0.0 for darkest and 1.0 for brightest


def colorWipe(pixels, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(0, len(pixels)):
        pixels[i] = color
        pixels.show()
        time.sleep(wait_ms / 1000.0)


# Main program logic follows:
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--animation', help='Define the start animation')
    parser.add_argument('--brightness', type=float, help = 'Define the brightness of pixels')
    parser.add_argument('--count', type=int, help = 'Define the lenght of pixels')

    args = parser.parse_args()

    LED_BRIGHTNESS = args.brightness if args.brightness else LED_BRIGHTNESS
    LED_COUNT = cmath.clamp_int(args.count, 0,288) if args.count else LED_COUNT

    # Create NeoPixel object with appropriate configuration.
    pixels = neopixel.NeoPixel(
        LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False)

    print('Press Ctrl-C to quit.')

    try:
        if(args.animation):
            anim_controller = AnimatorController(pixels, animation=args.animation)
        else:
            anim_controller = AnimatorController(pixels)

        anim_controller.run()

    except KeyboardInterrupt:
        print("\r\nStopping... Please Wait...")

        for i in range(0, len(pixels)):
            pixels[i] = (0, 0, 0)
            pixels.show()
            time.sleep(0 / 1000.0)
        
        print("Done!")
