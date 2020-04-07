import time
from ..tools import cmath


class Animation(object):
    def __init__(
            self,
            pixels,
            loop : bool = True):
        self._pixels = pixels
        self.__num_pixels = len(pixels)
        self.loop = loop
        self.done = False
        pass

    def clear(self):
        """
            Turn off all pixels
        """
        self._pixels.fill((0,0,0))

    def start(self):
        """
            Called before the first update cycle. Useful to prepare your animation
        """
        pass

    def update(self, deltaTime):
        raise NotImplementedError

    def end(self):
        """
            Call this method to finalize the animation.
            This not affect if animation is loop
        """
        self.done = True

    def get_pixels_count(self):
        return self.__num_pixels