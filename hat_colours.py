#!/usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()

red = (153, 0, 0)
green = (0, 76, 0)

speed = 0.05

message = "Fourscore and seven years ago, our fathers brought fourth on this continent a new nation convcieved in liberty and dedicated to the proposition that all men are created equal."

sense.show_message(message, speed, text_colour=red,
