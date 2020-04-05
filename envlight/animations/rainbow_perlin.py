from . import Animation
from ..tools import cmath
from ..tools import color
from noise import pnoise2


class RainbowPerlinAnimation(Animation):

    def __init__(self, pixels):
        super().__init__(pixels)
        self.t = 0.0

        self.scale = 100.0
        self.octaves = 2
        self.speed = 15.0
        self.hue_time = 180

    def update(self, deltaTime):
        for i in range(0, self._num_pixels-1):
            x = pnoise2(
                i / self.scale,
                self.t / self.scale,
                octaves=self.octaves)
            
            x = cmath.map(x , -0.75, 0.75, -1, 1)
            x = cmath.clamp(x, -1.0, 1.0)
            
            self.hue_time = cmath.repeat(self.hue_time, 360)

            h = self.hue_time + (180  * x)
            s = 1.0
            v = 1.0
            
            r, g, b = color.hsv2rgb(h,s,v)

            self._pixels[i] = (int(r),int(g),int(b))
        
        self.hue_time += 1
        self.t += deltaTime * self.speed 
        pass
