import turtle
import random
import time
drawing_board=turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Turtle Game")
a=turtle.Turtle()
a.shape("turtle")
a.color("red")
ttime=31
b=turtle.Turtle()

def spawn_turtle():
    xrandom_int = random.randint(-250, 250)
    yrandom_int = random.randint(-250, 250)
    a.hideturtle()           #make the turtle invisible
    a.penup()                #don't draw when turtle moves
    a.goto(xrandom_int,yrandom_int)       #move the turtle to a location
    a.showturtle()           #make the turtle visible
    a.pendown()              #draw when the turtle moves


def remaining_time():
    b.hideturtle()
    b.penup()
    b.goto(10,270)
    inreal_time=30
    while 0 < inreal_time:
        b.write(font=("Arial", 15, "normal"),arg=inreal_time,align="center")
        inreal_time -=1
        time.sleep(0.3)
        b.clear()
        spawn_turtle()
remaining_time()



'''while int(ttime)>0:
    ttime -=1
    remaining_time()'''


turtle.mainloop()
