import math

def sin(x):
    """Oblicza wartość funkcji sinus dla kąta x w radianach"""
    return math.sin(x)

def sin_deg(deg):
    """Oblicza wartość funkcji sinus dla kąta deg w stopniach"""
    rad = math.radians(deg)
    return math.sin(rad)