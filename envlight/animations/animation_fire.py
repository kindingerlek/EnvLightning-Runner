from noise import pnoise2
from .animation import Animation
from ..tools import cmath
from ..tools import color


class FireAnimation(Animation):

    def __init__(self, pixels):
        super().__init__(pixels)
        self.t = 0.0

        self.scale = 25.0
        self.octaves = 6
        self.speed = 15.0

    def update(self, deltaTime):
        for i in range(0, self._num_pixels-1):
            x = pnoise2(
                i / self.scale,
                self.t / self.scale,
                octaves=self.octaves)
            
            h, s, v = color.rgb2hsv(255, 70, 0)

            x = cmath.map(x, -0.75, 0.75, 0, 1)
            x = x * x * x * x
            x = cmath.clamp(x, 0.0, 1.0)
            
            v = x
            
            r, g, b = color.hsv2rgb(h,s,v)

            self._pixels[i] = (int(r),int(g),int(b))
        self.t += deltaTime * self.speed 
        pass
