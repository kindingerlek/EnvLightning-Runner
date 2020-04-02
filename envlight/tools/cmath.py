import math

def map(x: float, from_min: float, from_max: float, to_min: float = 0.0, to_max: float = 1.0):
    y = (x - from_min) / (from_max - from_min) * (to_max - to_min) + to_min
    return y

def clamp(x: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    return minimum if x < minimum else maximum if x > maximum else x

def clamp_int(x: float, minimum: float = 0.0, maximum: float = 1.0) -> int:
    return int(clamp(x,minimum, maximum))

def lerp(t: float, fromValue: float, toValue: float) -> float:
    return map(t, 0.0, 1.0, fromValue, toValue)

def lerp_int(t: float, fromValue: float, toValue: float) -> int:
    return int(lerp(t,fromValue, toValue))

def inv_lerp(value: float, minimum: float, maximum: float):
    return map(value, minimum, maximum)

def inv_lerp_int(value: float, minimum: float, maximum: float):
    return int(inv_lerp(value, minimum, maximum))

def multiply_tuple_by_scalar(vtuple, scalar):
    return tuple(x * scalar for x in vtuple)

def multiply_tuple_by_scalar_int(tuple_value, scalar):
    return tuple(int(x * scalar) for x in tuple_value)

def repeat(t, length):
    return t - math.floor(t/length) * length