import math
#from . import cmath

def hsv_to_rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)    
    return r, g, b
    
def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v

def temperature_to_rgb(k: float):
    """
        Start with a temperature, in Kelvin, somewhere between 1000 and 40000.
        (Other values may work, but I can't make any promises about the quality
        of the algorithm's estimates above 40000 K.) Note also that the
        temperature and color variables need to be declared as floating-point.

        Source: https://tannerhelland.com/2012/09/18/convert-temperature-rgb-algorithm-code.html
    """

    k = k / 100.0
    r = 0.0
    g = 0.0
    b = 0.0


    #Calculate Red:
    if (k <= 66.):
        r = 255.0
    else:
        r = k - 60
        r = 329.698727446 * (math.pow(r , -0.1332047592))
        if (r < 0): r = 0
        if (r > 255) : r = 255
    
    #Calculate Green:
    if (k <= 66.):
        g = k
        g = 99.4708025861 * math.log(g) - 161.1195681661
        if (g < 0): g = 0
        if (g > 255): g = 255
    else:
        g = k - 60.
        g = 288.1221695283 * (math.pow(g , -0.0755148492))
        if (g < 0): g = 0
        if (g > 255): g = 255
    
    #Calculate Blue:
    if (k >= 66.):
        b = 255
    else:
        if (k <= 19.):
            b = 0
        else:
            b = k - 10.
            b = 138.5177312231 * math.log(b) - 305.0447927307
            if (b < 0): b = 0
            if (b > 255): b = 255

    return int(r), int(g), int(b)


def rgb_to_temperature(r, g, b):
    k = 0

    if(r == 255):
        k = math.pow(math.e,((g + 161.1195681661)/99.4708025861))        
    else:
        k = (g/288.1221695283)**(1.0/-0.0755148492)
        k += 60

    return k * 100

# def lerp( t:float, fromColor:tuple, toColor:tuple ):

#     r1,g1,b1 = fromColor
#     r2,g2,b2 = toColor

#     r = cmath.lerp_int(t,r1,r2)
#     g = cmath.lerp_int(t,g1,g2)
#     b = cmath.lerp_int(t,b1,b2)

#     return r,g,b