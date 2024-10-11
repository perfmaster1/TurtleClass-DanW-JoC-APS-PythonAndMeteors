# @@==================================================================================================@@
#  DanTurtleClass-Oct2024: Dan W multiple turtles program for Advanced Problem Solving
#                          Turtle assignment.
#
#  Parameters:
#    None at present
#
#  Author: Daniel Wroblewski
#    Date: 10/17/2024
#   Status: In Progress
# @@==================================================================================================@@

import turtle
#import os

#
#  Set up screen - screen object
#
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#
# Turtle does not allow multiple windows simultaneously. To do that effect you
#  must do as follows:  Turtle is built on top of TKinter module code but is
#    very restrictive and gives you only one window, but flipping this and use
#    TKinter itself to manage windows and using Turtle from within TKinter will
#    give you more options.
#
#  https://www.reddit.com/r/learnpython/comments/qbrfq8/how_to_display_multiple_windows_turtle_sos/
#
#wn2=turtle.Screen()
#wn2.bgcolor("blue")
#wn2.title("pylogo")
#wn2.setup(350, 190, startx = 0, starty = 0)
#
#  Import/use a background GIF:
#
# turtle.bgpic(picname=None)
#turtle.bgpic("giferDotComBouncingPythons200x130.gif")
#
#  setup parameters:
#  startx and starty are for where turtle window is anchored.
#  0,0 is upper left corner. Turtle window grows down and to the right
#  +x is the distance between left screen edge and left edge start of window going right..
#     -x is the distance between  right screen edge and start of window right border
#      going left.
#  +y is distance between top screen edge and top window going down;
#     -y is distance between bottom of screen and bottom of turtle window going up.
#  My laptop will allow 695 x 695 without spilling off the bottom of screen.
#  My max width is 1350.
#  Your values may vary.
#
wn.setup(1350, 495, startx = 0, starty = 220)
wn.addshape("giferDotComBouncingPythons200x130.gif")
wn.tracer(0)
#
#  Create a border
#

#
#  psuedo-animation of GIFs
#
#

tr1=turtle.Turtle()
tr1.speed(1)
tr1.shape("giferDotComBouncingPythons200x130.gif")
tr1.penup()
tr1.goto(-585,+180)
i=0

while True:
    wn.update()
    tr1.forward(0.1)
    i+=1
    if i > 13500:
        tr1.goto(-582,+180)
        i=0


#    turtle.clear()
#    for i in range(6):

#        tr1.penup()
#        tr1.clear()
#        offset=i * 200
#        tr1.goto(offset,0)
#        tr1.pendown()
        # turtle.bgpic(picname=None)
#        turtle.bgpic("giferDotComBouncingPythons200x130.gif")
#        tr1.circle(5,180)
#        tr1.dot(1)

#        j=0
#        for j in range(10000):
#            k = "wait for me"
#            k2 = j^4 + i^2
#        turtle.bgpic("nopic")







#
#delay = raw_input("Press ENTER to finish")
#
delay=input("Press ENTER to finish")
#
#   Keeps turtle window open after all the code runs.
#
#turtle.done()