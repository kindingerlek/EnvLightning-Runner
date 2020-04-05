from . import Animation
from ..tools import cmath
from ..tools import color
from noise import pnoise1
import time


class TestColorsAnimation(Animation):

    def __init__(self, pixels):
        super().__init__(pixels)
        self._time_to_change = 5.0

        self._colors = {
            "white"     : ( 255, 255, 255),
            "red"       : ( 255,   0,   0),
            "orange"    : ( 255, 128,   0),
            "yellow"    : ( 255, 255,   0),
            "ambar"     : ( 128, 255,   0),
            "green"     : (   0, 255,   0),
            "anil"      : (   0, 255, 128),
            "cian"      : (   0, 255, 255),
            "lightblue" : (   0, 128, 255),
            "blue"      : (   0,   0, 255),
            "puple"     : ( 128,   0, 255),
            "magenta"   : ( 255,   0, 255),
            "magenta1"  : ( 255,   0, 128)
        }

    def update(self, deltaTime):
        for colorItem in self._colors.items():
            self._pixels.fill(colorItem[1])
            self._pixels.show()
            time.sleep(self._time_to_change)