from tkinter import *
import time




root = Tk()
root.geometry("1200x1000")
red = IntVar()
green = IntVar()
blue = IntVar()


def get_hex(red,green,blue):
   r = hex(red.get())
   r = r[2:]
   g = hex(green.get())
   g = g[2:]
   b = hex(blue.get())
   b = b[2:]
   hexvalue = "#" + str(r) + str(g) + str(b)
   canvas.itemconfig(circle,fill=hexvalue)


sliders = []
for i in range(1,4,1):
   slider = Scale(root,label="Red",from_=0,to=255,variable=red,command=get_hex)
   slider.grid(row=0,column=i)
   sliders.append(slider)


sliders[1].configure(label="Green",variable=green)
sliders[2].configure(label="Blue",variable=blue)


button = Button(root,text="Change Color",command=get_hex)
button.grid(row=2,column=1)


canvasf = Frame(root,width=1000,height=600)
canvasf.grid(row=1,column=i)
canvas = Canvas(canvasf,width=1000,height=600,bg="LightBlue")
canvas.grid(row=0,column=0)






x1 = 50
x2 = 50
y1 = 100
y2 = 100
circle = canvas.create_oval(x1,x2,y1,y2,fill="#000000")
movex = 2
movey = 3
while True:
   a,b,c,d = canvas.coords(circle)
   if c > 1000:
       movex *= -1
   if a < 0:
       movex *= -1
   if d > 600:
       movey *= -1
   if b < 0:
       movey *= -1
   canvas.move(circle,movex,movey)
   time.sleep(.01)
   canvas.update()












root.mainloop()
