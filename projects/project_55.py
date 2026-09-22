import math
from typing import Callable

def square(a):
    return a * a

def circle(a):
    return math.pow(a, 2) * math.pi

def rectangle(l, w):
    return l * w

def triangle(b, h):
    return b * h / 2

def get_func(ls: list[str]) -> list[Callable]:
    funcs = []
    for func in ls:
        if func == "square":
            funcs.append(square)

        elif func == "circle":
            funcs.append(circle)

        elif func == "rectangle":
            funcs.append(rectangle)

        elif func == "triangle":
            funcs.append(triangle)

    return funcs