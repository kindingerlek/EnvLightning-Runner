from noise import pnoise1
from .animation import Animation
from ..tools import cmath
from ..tools import color
import time


class TestColorsAnimation(Animation):

    def __init__(self, pixels):
        super().__init__(pixels)
        self._time_to_change = 5.0

        self._colors = {
            "white"     : ( 255, 255, 255),
            "red"       : ( 255,   0,   0),
            "yellow"    : ( 255, 255,   0),
            "green"     : (   0, 255,   0),
            "cian"      : (   0, 255, 255),
            "blue"      : (   0,   0, 255),
            "magenta"   : ( 255,   0, 255)
        }

    def update(self, deltaTime):
        for colorItem in self._colors.items():
            self._pixels.fill(colorItem[1])
            self._pixels.show()
            time.sleep(self._time_to_change)