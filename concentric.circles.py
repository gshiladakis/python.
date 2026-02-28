import turtle

def draw_concentric_circles(num_circles, initial_radius, radius_increment):
  """
  Draws a series of concentric circles.
  :param num_circles: Number of circles to draw
  :param initial_radius: Radius of the smallest circle
  :param radius_increment: Increment in radius for each subsequent circle
  """
  turtle.speed(0) # Set drawing speed to the fastest
  turtle.penup() # Lift the pen to avoid drawing while moving 
  turtle.hideturtle() # Hide the turtle cursor 

  for i in range(num_circles):
    radius = initial_radius + i * radius_increment
    turtle.goto(0, -radius) # Move to the starting position of the circle
    turtle.pendown() # Lower the pen to draw the circle
    turtle.circle(radius) # Draw the circle
    turtle.penup() # Lift the pen to move for the next circle

def main():
  # Setup the turtle environment
  screen = turtle.Screen()
  screen.title("Concentric Circles")
  screen.bgcolor("blue")

  # Draw concentric circles 
  draw_concentric_circles(num_circles=10, initial_radius=10, radius_increment=15)

  # Finish up
  screen.mainloop()

if _name_ == "__main__":
  main() 
