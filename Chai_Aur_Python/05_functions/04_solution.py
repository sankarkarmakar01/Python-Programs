# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def calculate(r):
    area = math.pi * r * r
    cir = 2 * math.pi * r
    print("Area:",area)
    print("Circumference:",cir)
    
calculate(1.5)