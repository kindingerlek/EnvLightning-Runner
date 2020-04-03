import time
import sys

from neopixel import NeoPixel
from .tools import cmath

from .animations.animation import Animation
from .animations.animation_fire import FireAnimation
from .animations.animation_ping_pong import PingPongAnimation
from .animations.animation_rainbow_perlin import RainbowPerlinAnimation
from .animations.animation_collapsecenter import TurnCollapseCenterAnimation
from .animations.animation_fade import FadeAnimation
from .animations.animation_test_colors import TestColorsAnimation


class AnimatorController(object):
    def __init__(self,
                pixels: NeoPixel,
                animation: str = "fire",
                update_rate: int = 60):
        self._pixels = pixels

        animations = {
            "fire" : FireAnimation(pixels),
            "rainbow" : RainbowPerlinAnimation(pixels),
            "pingpong" : PingPongAnimation(pixels),
            "fade": FadeAnimation(pixels),
            "test": TestColorsAnimation(pixels)
        }


        self._animation = animations[str.lower(animation)]

        self._update_time = (1.0/update_rate)
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
            start_cycle_time = time.process_time()

            delta_time = 1.0 / self.FPS
            self._animation.update(delta_time)
            self._pixels.show()

            end_cycle_time = time.process_time()
            
            cycle_time = (end_cycle_time - start_cycle_time)

            
            self.__calc_and_print_FPS(cycle_time + self.__wait_next_update(cycle_time))

    def __wait_next_update(self, cycle_time):
        waitTime = cmath.clamp(self._update_time - cycle_time)    
        
        if(waitTime > 0):
            time.sleep(waitTime)

        return waitTime

    def __calc_and_print_FPS(self, cycle_time):        
        self.FPS = int(1.0/cycle_time)

        sys.stdout.write(f"\rFPS: {self.FPS}")
        sys.stdout.flush()