#!/usr/bin/env/ python

from sense_hat import SenseHat
sense = SenseHat()
import time
import random 

r= random.randint(0,255)
g= random.randint(0,255)
b= random.randint(0,255)
print("the random number is"), r, ("this time")

sense.show_letter("H", (r, g, b))
time.sleep(1)
sense.show_letter("i", (b, r, g))
time.sleep(1)
sense.show_letter("!", (g, b, r))
time.sleep(1)
sense.clear()
