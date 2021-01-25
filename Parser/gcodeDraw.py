import turtle

# Initialize pen and variables
pen = turtle.Turtle()
pen.color('black')
pen.pensize('5')
pen.shape("circle")
pen.speed("")

#Parameter definitions: 
#   X:      x-coordinate or distance
#   Y:      y-coordinate or distance
#   fr:     Feed rate 
#   unit:   current units (default = inches)
#   mode:   current mode (default = relative)

# Draw function for g0 and g1 is shared as g1. g0 will call g1 with max feedrate.
def line(x, y, fr, mode):
    # 360 in/min = 10 pen, figure out later
    if unit == "inch":
        pen.speed(fr*25.4)
        x *= 25.4
        y *= 25.4
    else:
        pen.speed(fr)

    if mode == "abs":   #abs
        pen.goto(x,y)   # go to (x,y)
    else:               #rel
        pen.goto(x+pen.xcor(),y+pen.ycor()) 
 
def arc(x, y, i, j, mode, dir): #CW if dir == 1, CCW if dir == -1
     if unit == "inch":
        pen.speed(fr*25.4)
        x *= 25.4
        y *= 25.4
        i *= 25.4
        j *= 25.4
    else:
        pen.speed(fr)
    
    ax = pen.xcor()
    ay = pen.ycor()
    
    if mode == "abs":
        x -= ax
        y -= ay
        i -= ax
        j -= ay
    #center
    center = [ax+i, ay+j]
    #radius
    rad = math.sqrt(i**2 + j**2)
    #d
    d = math.sqrt((ax-x)**2 + (ay-y)**2)
    #arclength
    theta = math.acos(1 - d**2 / 2 / r**2)
    length = rad * theta
    degree = theta * 180 / math.pi

    th_a = math.atan(y/x)
    if ax < 0:                         # ax+ ay+     th_a
        if ay < 0:
            th_a = th_a + 180          # ax- ay-     180 + th_a
        else:
            th_a = 180 - th_a          # ax- ay+     180 - th_a
    elif ay < 0:                      
        th_a = 360 - th_a              # ax+ ay-     360 - th_a

    if x < 0:                          # x+ y+       th_b
        if y < 0:
            th_b = th_b + 180          # x- y-       180 + th_b
        else:
            th_b = 180 - th_b          # x- y+       180 - th_b
    elif y < 0:                      
        th_b = 360 - th_b              # x+ y-       360 - th_b

    if th_b > th_a and th_b < (th_a + 180):
        theta = 360 - theta
        
    pen.circle(dir*rad, theta)

def m6(num):
    tools = ["black", "red", "green", "blue"]
    pen.color(tools[num]) # selecting a pen color


