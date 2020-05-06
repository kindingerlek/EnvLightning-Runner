from . import Animation
from ..tools import cmath
from ..tools import color
import math


class SunriseAnimation(Animation):

    def __init__(
            self,
            pixels,
            duration = 60):

        super().__init__(pixels)

        self._duration = duration

    
    def start(self):
        self._leftTime = self._duration


    def update(self, deltaTime):
        
        self._leftTime = (self._leftTime - deltaTime)
        if (self._leftTime <= 0):
            return

        t = 1 - (self._leftTime/self._duration)

        k = cmath.inv_lerp(t, 0, 6500)
        
        

        light_on = False
        start= 0
        end = self.get_pixels_count()

        rk, gk, bk = color.temperature_to_rgb(k)

        for i in range(0, self.get_pixels_count()):
            r, g, b = (rk,gk,bk)
            angle = cmath.map(i, 0, self.get_pixels_count(),0,180)
            sin = 1-math.sin(math.radians(angle))

            #r,g,b = cmath.multiply_tuple_by_scalar((r,g,b), diff)

            if(t > sin):
                if(not light_on):
                    start = i
                    end = self.get_pixels_count() - i
                    light_on = True

                angle = cmath.map(i, start, end, 0, 180)
                smooth = math.sin(math.radians(angle))

                # get the color
                r, g, b = color.temperature_to_rgb(cmath.inv_lerp(smooth*t, 500, 3500))
                
                # smooth the brightness from center to edges
                r, g, b = cmath.multiply_tuple_by_scalar_int((r,g,b), smooth*smooth*t*t)

                self._pixels[i] = (int(r),int(g),int(b))
            else:
                self._pixels[i] = (0, 0, 0)

        pass
