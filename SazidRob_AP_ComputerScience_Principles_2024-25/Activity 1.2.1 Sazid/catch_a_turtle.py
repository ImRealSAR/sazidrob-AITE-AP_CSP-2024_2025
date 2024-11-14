import turtle as trtl
import random

# Setup screen and customize
wn = trtl.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.addshape("Activity 1.2.1 Sazid\space_bg_resized.gif")
wn.bgpic("Activity 1.2.1 Sazid\space_bg_resized.gif")

# initialize variables
score = 0 
timer = 30
timer_up = False
font_setup = ("Arial", 18)
counter_interval = 1000
move_interval = 100  # Interval for random movement of the turtle

# Create turtle objects
customizer = trtl.Turtle()

spot = trtl.Turtle()
spot.shape("turtle")
spot.color("red")
spot.penup()

scoret = trtl.Turtle()
scoret.color("Yellow")
scoret.penup()
scoret.goto(-600, 300)
scoret.write("Score: " + str(score), font=font_setup)
scoret.hideturtle()

counter = trtl.Turtle()
counter.color("#FFFDD0")
counter.penup()
counter.goto(575, 300)
counter.hideturtle()


# Functions for the program
def update_score(x, y):
    global score
    if not timer_up:
        score += 1
        scoret.clear()
        scoret.write("Score: " + str(score), font=font_setup)
    if timer_up == True:
        spot.goto(0,0)
    # while counter == 0
        move_turtle()

def move_turtle():
    colors = ["orange", "blue", "yellow", "pink", "green", "purple", "seashell"]
    spot.color(random.choice(colors))
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    spot.goto(x, y)

# def moving_turtle():
#     if not timer_up:
#         angle = random.randint(0, 360)
#         distance = random.randint(10, 90)
#         distance -= 1
#         angle -= 1
#         spot.setheading(angle)
#         spot.forward(distance)
#         wn.ontimer(moving_turtle, move_interval) 

def moving_turtle():
    if not timer_up:
        angle = random.randint(0, 360)
        distance = random.randint(10, 90)
        spot.setheading(angle)
        spot.forward(distance)
        x, y = spot.position()
        if x < -400:
            x = -400
        elif x > 400:
            x = 400
        if y < -300:
            y = -300
        elif y > 300:
            y = 300
        spot.setpos(x, y)
        wn.ontimer(moving_turtle, move_interval)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
        # scoret.speed(0)
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)


spot.onclick(update_score)
moving_turtle() 
countdown() 
wn.mainloop()
