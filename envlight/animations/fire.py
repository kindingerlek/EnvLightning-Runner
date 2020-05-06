from . import Animation
from ..tools import cmath
from ..tools import color
from noise import pnoise2


class FireAnimation(Animation):

    def __init__(
            self,
            pixels,
            speed : float = 25,
            scale : float = 80,
            basecolor : tuple = (255, 70, 0)):

        super().__init__(pixels)
        self._t = 0.0

        self._octaves = 6
        self._speed = speed
        self._scale = scale
        self._basecolor = basecolor


    def update(self, deltaTime):
        for i in range(0, self.get_pixels_count()-1):
            x = pnoise2(
                i / self._scale,
                self._t / self._scale,
                octaves=self._octaves)
            

            x = cmath.map( x, -0.5, .75, 0, 1)
            x = (x * x * x * x) * 4
            x = cmath.clamp(x, 0.0, 1.0)
            
            k = cmath.inv_lerp(x, 500, 2000)
            
            h, s, v = color.rgb_to_hsv(*color.temperature_to_rgb(k))
            v = x

            r,g,b = color.hsv_to_rgb( h, s, v)

            self._pixels[i] = (int(r),int(g),int(b))
        self._t += deltaTime * self._speed 
        pass
