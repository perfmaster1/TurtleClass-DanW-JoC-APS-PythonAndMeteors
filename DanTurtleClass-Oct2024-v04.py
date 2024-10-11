# @@==================================================================================================@@
#  DanTurtleClass-Oct2024: Dan W multiple turtles program for Advanced Problem Solving
#                          Turtle assignment.
#
#  Parameters:
#    None at present
#
#  Author: Daniel Wroblewski
#    Date: 10/17/2024  version 0.04
#   Status: Complete as planned
# @@==================================================================================================@@

import turtle
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
#
#  Import/use a background GIF - we could do this as an enhancement:
#    Unfortunately it gets taken out every time wn.update runs.
turtle.bgpic("StarfieldWithBlackBackground.gif")

# -none- for blank background
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
# original x 1350
#
wn.setup(1200, 600, startx = 0, starty = 220)
wn.addshape("giferDotComBouncingPythons200x130.gif")
wn.addshape("meteor45pct-horiz.gif")
wn.addshape("RocketShipSilverRedHoriz-long.gif")

wn.tracer(0)
#
#  psuedo-animation of GIFs
#
#

i=0

rs1=turtle.Turtle()
rs1.speed(12)
rs1.shape("RocketShipSilverRedHoriz-long.gif")
rs1.penup()
rs1.goto(-540,+105)
#
tr1=turtle.Turtle()
tr1.speed(6)
tr1.shape("giferDotComBouncingPythons200x130.gif")
tr1.penup()
tr1.goto(-420,+240)
#
met1=turtle.Turtle()
met1.speed(3)
met1.shape("meteor45pct-horiz.gif")
met1.penup()
met1.goto(-200,40)
#
met2=turtle.Turtle()
met2.speed(7)
met2.shape("meteor45pct-horiz.gif")
met2.penup()
met2.goto(-50,-260)
#
met3=turtle.Turtle()
met3.speed(4)
met3.shape("meteor45pct-horiz.gif")
met3.penup()
met3.goto(300,-205)
#
met4=turtle.Turtle()
met4.speed(10)
met4.shape("meteor45pct-horiz.gif")
met4.penup()
met4.goto(-585,-140)
#
met5=turtle.Turtle()
met5.speed(3)
met5.shape("meteor45pct-horiz.gif")
met5.penup()
met5.goto(-585,-75)
#
while True:
    wn.update()
    rs1.forward(1.8)
    tr1.forward(0.05)
    met1.forward(0.45)
    met2.forward(0.85)
    met3.forward(1.3)
    met4.forward(1.9)
    met5.forward(0.3)
#
    i+=1
    if i > 16500:
        tr1.goto(-420,+240)
#
    if i > 16500:
        rs1.goto(-540,+105)
#
    if i > 14500:
        met1.goto(-485, +40)
        met5.goto(-585,-75)
#
    if i > 16500:
        met2.goto(-50,-260)
        met3.goto(300,-205)
        met4.goto(-525, -140)
        i=0
#
#  if we wanted to clear the screen....
#
#    turtle.clear()