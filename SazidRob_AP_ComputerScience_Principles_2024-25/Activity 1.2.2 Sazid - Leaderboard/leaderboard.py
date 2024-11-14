import random
import turtle as trtl

# leaderboard.py
# The leaderboard module to be used in Activity 1.2.2

# Set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 25

# Return names in the leaderboard file
def get_names(file_name):
    # Open file to read leader names
    leaderboard_file = open(file_name, "r")
    names = []
    
    for line in leaderboard_file:
        leader_name = ""
        index = 0

        # TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")
        while line[index] != ",":
            leader_name += line[index]
            index += 1
        print("Leader name is:", leader_name)
        # TODO 2: add the player name to the names list
        names.append(leader_name)
    
    leaderboard_file.close()
    return names
# Return scores from the leaderboard file
def get_scores(file_name):
    # Open file to read leader scores
    leaderboard_file = open(file_name, "r")
    scores = []

    for line in leaderboard_file:
        leader_score = ""
        index = line.index(",") + 1

        # TODO 4: use a while loop to get the score
        while index < len(line) and line[index] != "\n":
            leader_score += line[index]
            index += 1
        # TODO 5: add the player score to the scores list
        scores.append(int(leader_score))
    
    leaderboard_file.close()
    return scores

# Update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):
    index = 0

    # TODO 8: loop through all the scores in the existing leaderboard list
    for score in leader_scores:
        # TODO 9: check if this is the position to insert new score at
        if player_score > score:
            break
        index += 1
    
    # TODO 10: insert new player and score
    leader_names.insert(index, player_name)
    leader_scores.insert(index, player_score)

    # TODO 11: keep both lists at 5 elements only (top 5 players)
    if len(leader_names) > 5:
        leader_names.pop()
        leader_scores.pop()
    
    # TODO 12: store the latest leaderboard back in the file
    leaderboard_file = open(file_name, "w")
    
    # TODO 13: loop through all the leaderboard elements and write them to the file
    for i in range(len(leader_names)):
        leaderboard_file.write(leader_names[i] + "," + str(leader_scores[i]) + "\n")

    leaderboard_file.close()

# Draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-160, 100)
    turtle_object.hideturtle()
    turtle_object.down()

    # Loop through the lists and use the same index to display the corresponding name and score
    for index in range(len(leader_names)):
        turtle_object.write(f"{index + 1}\t{leader_names[index]}\t{leader_scores[index]}", font=font_setup)
        turtle_object.goto(turtle_object.xcor(), turtle_object.ycor() - 30)
    
    # Display message to the high scorer
    if player_score >= gold_score:
        turtle_object.write("Congratulations! You've earned the Gold score!", font=font_setup)
    elif player_score >= silver_score:
        turtle_object.write("Great job! You've earned the Silver score!", font=font_setup)
    elif player_score >= bronze_score:
        turtle_object.write("Good effort! You've earned the Bronze score!", font=font_setup)
    else:
        turtle_object.write("Keep trying to improve your score!", font=font_setup)

import random
import turtle as trtl

# leaderboard.py
# The leaderboard module to be used in Activity 1.2.2

# Set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 25

# Return names in the leaderboard file
def get_names(file_name):
    leaderboard_file = open(file_name, "r")
    names = []
    
    for line in leaderboard_file:
        leader_name = ""
        index = 0

        # TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")
        while line[index] != ",":
            leader_name += line[index]
            index += 1
        print("Leader name is:", leader_name)
        # TODO 2: add the player name to the names list
        names.append(leader_name)
    
    leaderboard_file.close()
    return names 

# Return scores from the leaderboard file
def get_scores(file_name):
    leaderboard_file = open(file_name, "r")
    scores = []

    for line in leaderboard_file:
        leader_score = ""
        index = line.index(",") + 1

        # TODO 4: use a while loop to get the score
        while index < len(line) and line[index] != "\n":
            leader_score += line[index]
            index += 1
        # TODO 5: add the player score to the scores list
        scores.append(int(leader_score))
    
    leaderboard_file.close()
    return scores 

# Update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):
    index = 0

    # TODO 8: loop through all the scores in the existing leaderboard list
    for score in leader_scores:
        # TODO 9: check if this is the position to insert new score at
        if player_score > score:
            break
        index += 1
    
    # TODO 10: insert new player and score
    leader_names.insert(index, player_name)
    leader_scores.insert(index, player_score)

    # TODO 11: keep both lists at 5 elements only (top 5 players)
    if len(leader_names) > 5:
        leader_names.pop()
        leader_scores.pop()
    
    # TODO 12: store the latest leaderboard back in the file
    leaderboard_file = open(file_name, "w")
    
    # TODO 13: loop through all the leaderboard elements and write them to the file
    for i in range(len(leader_names)):
        leaderboard_file.write(leader_names[i] + "," + str(leader_scores[i]) + "\n")

    leaderboard_file.close()

# Draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-160, 100)
    turtle_object.hideturtle()
    turtle_object.down()

    # Loop through the lists and use the same index to display the corresponding name and score
    for index in range(len(leader_names)):
        turtle_object.write(f"{index + 1}\t{leader_names[index]}\t{leader_scores[index]}", font=font_setup)
        turtle_object.goto(turtle_object.xcor(), turtle_object.ycor() - 30)

    # TODO 14: Display a message if the player made or didn't make the leaderboard
    if high_scorer:
        turtle_object.write("Congratulations!\nYou made the leaderboard!", font=font_setup)
    else:
        turtle_object.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=font_setup)
    
    # Move turtle to a new line after leaderboard message
    turtle_object.penup()
    turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
    turtle_object.pendown()

    # TODO 15: Display a medal message if player earned a gold/silver/bronze medal
    if player_score >= gold_score:
        turtle_object.write("You earned a gold medal!", font=font_setup)
    elif player_score >= silver_score:
        turtle_object.write("You earned a silver medal!", font=font_setup)
    elif player_score >= bronze_score:
        turtle_object.write("You earned a bronze medal!", font=font_setup)
