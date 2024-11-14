#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across the screen.
#   Stopping turtles when they collide.
import turtle as trtl

# Create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# Use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-350, tloc)
    ht.setheading(0)

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc, 350)
    vt.setheading(270)

    tloc += 50

# Function to detect collision
def detect_collision(t1, t2):
    x1, y1 = t1.xcor(), t1.ycor()
    x2, y2 = t2.xcor(), t2.ycor()
    if abs(x1 - x2) < 20 and abs(y1 - y2) < 20:  # Check if turtles are too close (within 20 pixels)
        return True
    return False

# Move turtles and check for collisions
for h in horiz_turtles:
    hx = h.xcor()
    hy = h.ycor()
    for v in vert_turtles:
        vx = v.xcor()
        vy = v.ycor()

        while hx < 350 and vy > -425:
            hx += 5
            vy -= 5
            h.goto(hx, hy)
            v.goto(vx, vy)

            if detect_collision(h, v): 
                h.hideturtle()  
                v.hideturtle()  
                horiz_turtles.remove(h)  
                vert_turtles.remove(v)  

wn = trtl.Screen()
wn.mainloop()
