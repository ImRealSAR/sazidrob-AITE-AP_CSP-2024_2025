#   a116_buggleg_length_image.pleg_length
import turtle as trtl
spider = trtl.Turtle()
spider.pensize(40)
spider.speed(25)
spider.circle(20) # this represents the preschool quality drawn spider's body I guess?

# create spider head

# Config spider legs
number_legs = 8
leg_length = 70
angle = 376 / number_legs
spider.pensize(5)

# Draw the spider's legs 
counting_legs = 0
while counting_legs < number_legs:
    spider.goto(0, 0)
    spider.setheading(angle * counting_legs)
    spider.forward(leg_length)
    counting_legs += 1

# Draw the spider's eyes
spider.color("white")
spider.penup()
spider.goto(-20, -2)
spider.pendown()
spider.circle(8)
spider.penup()
spider.goto(20, -2)
spider.pendown()
spider.circle(8)

spider.hideturtle() #Hide the turtle drawer so we don't get annoyed by that
wn = trtl.Screen()
wn.mainloop()