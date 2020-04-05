from . import Animation
from ..tools import cmath


class TurnCollapseCenterAnimation(Animation):

    def __init__(self, pixels):
        super().__init__(pixels)
        self.i = 0

    def start(self):
        pass

    def update(self, deltaTime):
        if self.i > (self._num_pixels / 2):
            return

        self._pixels[self.i] = (0, 0, 0)
        self._pixels[self._num_pixels-1-self.i] = (0, 0, 0)
        
        self.i += 1
