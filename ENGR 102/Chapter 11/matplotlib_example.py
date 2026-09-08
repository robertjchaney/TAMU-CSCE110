from turtle import *
from time import *
from random import *

def starrySky():
    penup()
    # Original color tuple in range [0, 255]
    color_rgb = (18, 0, 48)

    # Convert to range [0, 1] for turtle
    normalized_color = (color_rgb[0] / 255, color_rgb[1] / 255, color_rgb[2] / 255)

    # Use the normalized color with bgcolor
    bgcolor(normalized_color)

    for num in range(200):
        goto(randint(-400, 400), randint(-400, 400))
        dot(4, "white")


speed(0)
starrySky()
exitonclick()