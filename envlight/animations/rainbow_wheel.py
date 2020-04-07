from . import Animation
from ..tools import cmath
from ..tools import color

class RainbowWheelAnimation(Animation):

    def __init__(self, pixels):
        super().__init__(pixels)
        self.t = 0.0

        self.scale = 3
        self.speed = 20.0

    def update(self, deltaTime):
        for i in range(0, self.get_pixels_count()-1):
            self.t = cmath.repeat(self.t, 360)

            h = self.t + cmath.map(i,0,self.get_pixels_count()-1,0,360 * (1/self.scale))
            h = cmath.repeat(h, 360)
            s = 1.0
            v = 1.0
            
            r, g, b = color.hsv_to_rgb(h,s,v)

            self._pixels[i] = (int(r),int(g),int(b))
        
        self.t += deltaTime * self.speed 
        pass
