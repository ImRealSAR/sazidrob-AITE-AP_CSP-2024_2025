#   a115_robot_maze.py
import turtle as trtl
# ----- maze and turtle config variables
screen_h = 700
screen_w = 720
startx = 280
starty = -280
turtle_scale = 1.5

# ----- robot commands
def again(action, times):
    for _ in range(times):
        action()
def move():
    robot.dot(10)
    robot.fd(50)

def turn_left():
    robot.speed(0)
    robot.lt(90)
    robot.speed(2)

def turn_right():
    robot.speed(0)
    robot.rt(90)
    robot.speed(2)

# ----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

# ----- init robot
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

# ---- TODO: change maze here
wn.bgpic("maze4.png")  # other file names should be maze2.png, maze3.png

# ---- TODO: begin robot movement here
# Using again to make code shorter and more readable
for i in range(1): # I usd the for loop, and it works, and I shortened it from the other possiblity! 
    again(move, 1)
    turn_left()
    again(move, 1)
    turn_right()
    again(move, 2)
    turn_left()
    again(move, 1)
    turn_right()
    again(move, 1)
    turn_left()
    again(move, 1)
    turn_right()
    again(move, 1)
    turn_left()
    again(move, 1)
    turn_right()
    again(move, 1)
    turn_left()
    again(move, 1)
    turn_right()
    again(move, 3)
    turn_left()
    again(move, 4)
    turn_right()
    again(move, 2)
    turn_left()
    again(move, 2)

# ---- end robot movement 

wn.mainloop()
