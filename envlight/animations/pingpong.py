from . import Animation
from ..tools import cmath
from ..tools import color
from noise import pnoise2
import math


class PingPongAnimation(Animation):

    def __init__(self, pixels):
        super().__init__(pixels)
        self._angle = 0
        self._speed = 60


        x = math.cos(math.radians(self._angle))
        x = math.floor(cmath.map(x,-1.0,1.0,0.0,self._num_pixels))

        self._lastUpdatedPixel = x

    def update(self, deltaTime):
        #self.clear()

        # Trailling Effect
        for i in range(0, self._num_pixels):
            self._pixels[i] = cmath.multiply_tuple_by_scalar_int(self._pixels[i],.7)
            

        self._angle += self._speed * deltaTime
        self._angle = cmath.repeat(self._angle, 360)

        x = math.cos(math.radians(self._angle))
        x = math.floor(cmath.map(x,-1.0,1.0,0.0,self._num_pixels))

        for i in range(min(x,self._lastUpdatedPixel), max(self._lastUpdatedPixel,x)):
            self._pixels[i] = (255,255,255)        
        
        self._lastUpdatedPixel = x
