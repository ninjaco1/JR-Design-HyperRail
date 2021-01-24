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

MAXSPEED = 10

def g0(x, y, mode):
    pen.speed() == MAXSPEED
    if mode == "abs":   #abs
        pen.goto(x,y)   # go to (x,y)
    else:               #rel
        pen.goto(x+pen.xcor(),y+pen.ycor()) # go to next coordinate 
    # theta = math.atan(y/x)
    # mag = math.sqrt(y ** 2 + x ** 2)
    # pen.seth(theta)
    # pen.forward(mag)
    
def g1(x, y, fr, mode):
    # 360 in/min = 10 pen, figure out later
    pen.speed(fr)
    if mode == "abs":   #abs
        pen.goto(x,y)   # go to (x,y)
    else:               #rel
        pen.goto(x+pen.xcor(),y+pen.ycor()) 
 
def g2(x, y, i, j, mode): #cw
    if mode == "abs"
        x -= pen.xcor()
        y -= pen.ycor()
    #center
    center = [pen.xcor()+i, pen.ycor()+j]
    #radius
    rad = math.sqrt((pen.xcor()-center[0])**2 + (pen.ycor()-center[1]))
    #d
    d = math.sqrt((pen.xcor()-x)**2 + (pen.ycor()-y)**2)
    #arclength
    theta = math.acos(1 - d**2 / 2 / r**2)
    length = rad * theta
    
    degree = theta * 180 / math.pi
    pen.circle()
    

def g3(x, y, i, j, mode): #ccw
    if mode == "abs"
        x -= pen.xcor()
        y -= pen.ycor()
    #center
    center = [pen.xcor()+i, pen.ycor()+j]
    #radius
    rad = math.sqrt((pen.xcor()-center[0])**2 + (pen.ycor()-center[1]))
    #d
    d = math.sqrt((pen.xcor()-x)**2 + (pen.ycor()-y)**2)
    #arclength
    theta = math.acos(1 - d**2 / 2 / r**2)
    length = rad * theta
    
    degree = theta * 180 / math.pi
    pen.circle()

def m6(num):
    tools = ["black", "red", "green", "blue"]
    pen.color(tools[num]) # selecting a pen color


