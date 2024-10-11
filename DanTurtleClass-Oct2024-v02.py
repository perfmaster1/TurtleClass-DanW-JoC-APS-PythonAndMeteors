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
wn.title("Python And Meteors")

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
wn.addshape("meteor2.gif")

wn.tracer(0)
#
#  Create a border
#

#
#  psuedo-animation of GIFs
#
#

tr1=turtle.Turtle()
tr1.speed(6)
tr1.shape("giferDotComBouncingPythons200x130.gif")
tr1.penup()
tr1.goto(-585,+180)
i=0

met1=turtle.Turtle()
met1.speed(3)
met1.shape("meteor2.gif")
met1.penup()
met1.goto(-200,55)

met2=turtle.Turtle()
met2.speed(1)
met2.shape("meteor2.gif")
met2.penup()
met2.goto(-50,+10)

met3=turtle.Turtle()
met3.speed(0)
met3.shape("meteor2.gif")
met3.penup()
met3.goto(300,0)
#
met4=turtle.Turtle()
met4.speed(0)
met4.shape("meteor2.gif")
met4.penup()
met4.goto(-585,+30)
#
met5=turtle.Turtle()
met5.speed(2)
met5.shape("meteor2.gif")
met5.penup()
met5.goto(-585,+3)

while True:
    wn.update()
    tr1.forward(0.05)
    met1.forward(0.45)
    met2.forward(0.85)
    met3.forward(1.3)
    met4.forward(1.9)
    met5.forward(0.1)

    i+=1
    if i > 16500:
        tr1.goto(-582,+180)

    if i > 14500:
        met1.goto(-582, -55)
        met5.goto(-585,+3)

    if i > 16500:
        met2.goto(-50,-35)
        met3.goto(300,-1)
        met4.goto(-585, -12)
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