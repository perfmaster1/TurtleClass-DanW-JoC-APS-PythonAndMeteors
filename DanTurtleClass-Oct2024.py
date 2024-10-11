

import turtle
#import os

#
#  Set up screen - screen object
#
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
#
#  startx and starty are for where turtle window is anchored.
#  0,0 is upper left corner. Turtle window grows down and to the right
#  My laptop will allow 695 x 695 without spilling off the bottom of screen.
#  My max width is 1350.
#  Your values may vary.
#
wn.setup(1350, 695, startx = 0, starty = 0)
#
#  Create a border
#

#
#delay = raw_input("Press ENTER to finish")
#
delay=input("Press ENTER to finish")
#
#   Keeps turtle window open
#
#turtle.done()