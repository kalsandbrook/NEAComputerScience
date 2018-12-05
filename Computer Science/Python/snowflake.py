import random
from turtle import *
setup( width = 800, height = 800, startx = None, starty = None)
#fd(100)
speed(0)

for i in range(9):
    for i in range(18):
        for i in range(6):
            fd(50)
            lt(360/5)
            fd(50)
        lt(5)
        
    for i in range(18):
        for i in range(6):
            fd(50)
            rt(360/5)
            fd(50)
        rt(5)
    if i == 5:
        for i in range(6):
            fd(75)
            rt(360/5)
            fd(75)
        rt(5)
