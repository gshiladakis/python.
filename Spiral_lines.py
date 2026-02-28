#This program draws a design using repeated lines.
import turtle

#Named constants
START_X = -200       #Staring X coordinate 
START_Y = 0          #Starting Y coordinate 
NUM_LINES = 36       #Number of lines to draw 
LINE_LENGTH = 400    #Length of each line
ANGLE = 170          #Angle to turn 
ANIMATION_SPEED = 0  #Animation speed

#Move the turle to its initial position.
turtle.hideturtle()
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()

#Set the animation speed.
turtle.speed(ANIMATION_SPEED)

#Draw 36 Lines, with the turtle titled by 170 degrees after each line is drawn. 
for x in range(NUM_LINES):
  turtle.forward(LINE_LENGTH)
  turtle.left(ANGLE)
