import time
import sys

from neopixel import NeoPixel
from .tools import cmath

from .animations.animation import Animation
from .animations.animation_fire import FireAnimation
from .animations.animation_ping_pong import PingPongAnimation
from .animations.animation_rainbow_perlin import RainbowPerlinAnimation
from .animations.animation_collapsecenter import TurnCollapseCenterAnimation



class AnimatorController(object):
    def __init__(self, pixels: NeoPixel, update_rate: int = 60):
        self._pixels = pixels

        self._animation = FireAnimation(pixels)
        #self._animation = RainbowPerlinAnimation(pixels)
        #self._animation = PingPongAnimation(pixels)

        self._delta_time = (1/update_rate)
        self._running = False
        self.FPS = update_rate

    def run(self):
        self._running = True
        self.__update()

    def stop(self):
        self._animation = TurnCollapseCenterAnimation(self._pixels)
        self.run()

    def __update(self):
        while self._running:
            start_cycle_time = time.time()

            self._animation.update(1.0/self.FPS)
            self._pixels.show()

            waitTime = cmath.clamp(self._delta_time - (time.time() - start_cycle_time))    
            time.sleep(waitTime)

            self.FPS = int(1.0/(time.time() - start_cycle_time))

            sys.stdout.write(f"\rFPS: {self.FPS}")
            sys.stdout.flush()
