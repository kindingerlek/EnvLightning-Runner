from . import Animation
from ..tools import cmath
from ..tools import color
from noise import pnoise2


class FireAnimation(Animation):

    def __init__(
            self,
            pixels,
            speed : float = 25,
            scale : float = 80):

        super().__init__(pixels)
        self._t = 0.0

        self._octaves = 6
        self._speed = speed
        self._scale = scale

    def update(self, deltaTime):
        for i in range(0, self.get_pixels_count()-1):
            # Get a heat from a perlinnoise map
            heat = pnoise2(
                i / self._scale,
                self._t / self._scale,
                octaves=self._octaves)
            
            # Take the values from range -.5 to .75, and map to 0 to 1            
            heat = cmath.map( heat, -0.5, .75, 0, 1)

            # convert the linear space to exponential space, and bump up the values
            heat = (heat * heat * heat * heat) * 4
            
            # Limit the values to range [ 0, 1]
            heat = cmath.clamp(heat, 0.0, 1.0)
            
            # Get map the heat value between some celsius temperature range
            k = cmath.inv_lerp(heat, 500, 2000)
            
            # Get color from temperature
            h, s, v = color.rgb_to_hsv(*color.temperature_to_rgb(k))

            # Make the brightness of pixel proportional to heat
            v = heat
            r,g,b = color.hsv_to_rgb(h, s, v)

            # Write Pixel
            self._pixels[i] = (int(r),int(g),int(b))
        self._t += deltaTime * self._speed 
        pass
