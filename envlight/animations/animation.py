import time
from ..tools import cmath


class Animation(object):
    def __init__(self, pixels):
        self._pixels = pixels
        self._num_pixels = len(pixels)
        pass

    def clear(self):
        self._pixels.fill((0,0,0))

    def start(self):
        pass

    def update(self, deltaTime):
        raise NotImplementedError
