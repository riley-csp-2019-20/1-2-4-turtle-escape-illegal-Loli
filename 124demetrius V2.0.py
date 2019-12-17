import turtle as trtl
import random
drawer = trtl.Turtle()
drawer.ht()
drawer.speed(0)

#code-name variables

distance = 15
gap_size = 5
wall_width = 10
door_width = 15
drawer.pensize(4)
drawer.pencolor("red")


def draw_door():

    drawer.penup()
    drawer.forward(door_width)
    drawer.pendown()


def draw_barrier():
    drawer.left(90)
    drawer.forward(wall_width+10)
    drawer.backward(wall_width+10)
    drawer.right(90)



#the maze creation/doors 
for i in range(75):
    if i > 4:
        door = random.randint(door_width, distance-2*door_width)
        barrier = random.randint(2*wall_width, distance-2*door_width)
        if door < barrier:
            drawer.forward(door)
            draw_door() #fix this
            drawer.forward(barrier-door-door_width)
            #draw barrier
            draw_barrier()
            drawer.forward(distance - barrier)


        else:
            drawer.forward(barrier)
            draw_barrier()
            drawer.forward(door-barrier)
            draw_door()
            drawer.forward(distance-door-door_width)


        drawer.left(90)

    distance += wall_width
wn = trtl.Screen()
Joemama =  trtl.Turtle()
shape = "turtle"
size = 2

def up():
   Joemama.forward(10)

def left():
   Joemama.left(90)

def right():
   Joemama.right(90)

def down():
   Joemama.back(10)

wn.onkeypress(up,"w")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.onkeypress(down,"s")




Joemama.pencolor("blue")
Joemama.pensize(2)

wn.listen()
wn.mainloop()