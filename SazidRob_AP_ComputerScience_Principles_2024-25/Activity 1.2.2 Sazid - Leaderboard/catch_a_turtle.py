import turtle as trtl
import random
import leaderboard as lb

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input ("Please enter your name: ")

# Setup screen and customize
wn = trtl.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.addshape("space_bg_resized.gif")
wn.bgpic("space_bg_resized.gif") 

# initialize variables
score = 0 
#timer = 5 #30 is to be the real timer, but for testing sake, temporarily reducing to 5
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
        manage_leaderboard()
        # scoret.speed(0)
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)

# Add this function to your game code

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)

spot.onclick(update_score)
moving_turtle() 
countdown() 
wn.mainloop()
