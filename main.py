import board
from  envlight.animator_controller import AnimatorController
import time
import neopixel
import argparse
import signal
from envlight.tools import cmath

# LED strip configuration:
LED_COUNT = 228             # Number of LED pixels.
LED_PIN = board.D18         # GPIO pin connected to the pixels (18 uses PWM!).
LED_BRIGHTNESS = .35        # Set to 0.0 for darkest and 1.0 for brightest

def keyboardInterruptHandler(signal, frame):
    anim_controller.stop()
    pixels.fill((0,0,0))
    pixels.show()
    print("")


# Main program logic follows:
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--animation', help='Define the start animation')
    parser.add_argument('--brightness', type=float, help = 'Define the brightness of pixels')
    parser.add_argument('--count', type=int, help = 'Define the lenght of pixels')

    args = parser.parse_args()

    LED_BRIGHTNESS = args.brightness if args.brightness else LED_BRIGHTNESS
    LED_COUNT = cmath.clamp_int(args.count, 0,228) if args.count else LED_COUNT

    # Create NeoPixel object with appropriate configuration.
    pixels = neopixel.NeoPixel(
        LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False)

    signal.signal(signal.SIGINT, keyboardInterruptHandler)
    
    print('Press Ctrl-C to quit.')

    if(args.animation):
        anim_controller = AnimatorController(pixels, animation=args.animation)
    else:
        anim_controller = AnimatorController(pixels)

    anim_controller.run()
