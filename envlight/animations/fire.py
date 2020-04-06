from . import Animation
from ..tools import cmath
from ..tools import color
from noise import pnoise2


class FireAnimation(Animation):

    def __init__(
            self,
            pixels,
            speed : float = 25,
            scale : float = 35):

        super().__init__(pixels)
        self._t = 0.0

        self._scale = scale
        self._octaves = 6
        self._speed = speed

    def update(self, deltaTime):
        for i in range(0, self._num_pixels-1):
            x = pnoise2(
                i / self._scale,
                self._t / self._scale,
                octaves=self._octaves)
            
            h, s, v = color.rgb2hsv(255, 70, 0)

            x = cmath.map( x, -0.5, 0.75, 0, 1)
            x = (x * x * x * x)
            x = cmath.clamp(x, 0.0, 1.0)
            
            v = x
            
            r, g, b = color.hsv2rgb(h,s,v)

            self._pixels[i] = (int(r),int(g),int(b))
        self._t += deltaTime * self._speed 
        pass
