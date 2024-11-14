import turtle as trtl
import random

trtl_shapes = ["arrow", "turtle", "classic", "square", "circle", "triangle"]
trtl_colors = ["red", "blue", "green", "yellow", "purple", "orange"]
trtl_objects = [] 


for shape in trtl_shapes:
    t = trtl.Turtle(shape=shape)
    color = random.choice(trtl_colors)
    t.color(color)
    trtl_colors.remove(color) 
    trtl_objects.append(t)

for i in range(len(trtl_objects)):
    x = (i % 2) * 200 - 100 
    y = (i // 2) * -100 + 100 
    trtl_objects[i].penup()
    trtl_objects[i].goto(x, y)

for i in range(len(trtl_objects)):
    if i % 2 == 0: 
        trtl_objects[i].setheading(135) # I put 135 because I think that would be 45 degrees northwest  
        trtl_objects[i].forward(100)
    else: 
        trtl_objects[i].setheading(-45)
        trtl_objects[i].forward(100)

wn = trtl.Screen()
wn.mainloop()
print("IDK IF THIS IS WHAT IT IS SUPPOSED TO BE")