import math

def pole_kwadratu(a):
    """Oblicza pole powierzchni kwadratu o boku a."""
    return a**2

def pole_prostopadloscianu(a, b, c):
    """Oblicza pole powierzchni prostopadłościanu o bokach a, b, c."""
    return 2*(a*b + b*c + c*a)

def pole_kuli(r):
    """Oblicza pole powierzchni kuli o promieniu r."""
    return 4*math.pi*r**2

def pole_walec(r, h):
    """Oblicza pole powierzchni walca o promieniu r i wysokości h."""
    return 2*math.pi*r*(r+h)

def pole_stozka(r, l):
    """Oblicza pole powierzchni stożka o promieniu podstawy r i tworzącej l."""
    return math.pi*r*(r+l)