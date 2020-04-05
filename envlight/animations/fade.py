from . import Animation
from ..tools import cmath
from ..tools import color
from noise import pnoise1


class FadeAnimation(Animation):

    def __init__(self, pixels):
        super().__init__(pixels)
        self.t = 0.0

        self.scale = 250.0
        self.octaves = 2
        self.speed = 1.0

    def update(self, deltaTime):
        x = pnoise1(self.t / self.scale,octaves=self.octaves)
        
        x = cmath.map(x , -0.75, 0.75, -1, 1)
        x = cmath.clamp(x, -1.0, 1.0)
        
        h = (180  * x)
        s = 1.0
        v = 1.0
        
        r, g, b = color.hsv2rgb(h,s,v)

        self._pixels.fill((int(r),int(g),int(b)))
        
        self.t += deltaTime * self.speed 
        pass
