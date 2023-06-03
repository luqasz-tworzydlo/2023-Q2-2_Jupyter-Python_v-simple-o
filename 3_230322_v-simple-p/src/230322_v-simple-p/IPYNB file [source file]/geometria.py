"""Łukasz Tworzydło, Paweł Wójcik"""

import math

# figura nr 1 [kwadrat]
def pole_kwadratu(a):
    return a*a
def obwod_kwadratu(a):
    return 4*a

# figura nr 2 [prostokąt]
def pole_prostokata(a, b):
    return a*b
def obwod_prostokata(a, b):
    return 2*a + 2*b

# figura nr 3 [trójkąt]
def pole_trojkata(a, h):
    return 0.5*a*h
def obwod_trojkata(a, b, c):
    return a + b + c

# figura nr 4 [równoległobok]
def pole_rownolegloboku(a, h):
    return a*h
def obwod_rownolegloboku(a, b):
    return 2*a + 2*b

# figura nr 5 [trapez]
def pole_trapezu(a, b, h):
    return (a+b)*h/2
def obwod_trapezu(a, b, c, d):
    return a + b + c + d

# figura nr 6 [koło]
def pole_kola(r):
    return math.pi * r**2
def obwod_kola(r):
    return 2 * math.pi * r
