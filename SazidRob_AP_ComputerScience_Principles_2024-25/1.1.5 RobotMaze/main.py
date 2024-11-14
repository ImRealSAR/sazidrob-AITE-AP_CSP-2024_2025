import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze3.png") # other file names should be maze2.png, maze3.png

#maze 2
for new_step in range(5):
  move()
if(new_step == 2):
  robot.right(90)
  robot.goto(startx,starty)
for new_steps in range(7):
  move()
if(new_steps == 2):
  turn_left()
if (new_steps == 5):
  turn_left()

#maze 3
move()
robot.rt(90)
for i in range(2):
  move()
robot.lt(90)
for i in range (2):
  move()
robot.rt(90)
for i in range(2):
  move()
robot.lt(90)
move()




#---- end robot movement 

wn.mainloop()