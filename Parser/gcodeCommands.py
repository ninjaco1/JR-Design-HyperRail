#G code commands
import sys

#Parameter definitions: 
#   X:      x-coordinate or distance
#   Y:      y-coordinate or distance
#   fr:     Feed rate 
#   unit:   current units (default = inches)
#   mode:   current mode (default = incremental)

MAXSPEED = 10

# G0:
def g0(tool):
    tempfr = tool.fr            # store previous feed rate in temp var
    tool.fr = MAXSPEED          # set current feed rate to max feed rate
    gdraw.line(tool.x, tool.y, tool.fr, tool.mode)
    # other function stuff in here

    tool.fr = tempfr            # restore value of tool.fr

# G1:
def g1(tool):
    gdraw.line(tool.x, tool.y, tool.fr, tool.mode)
        
# G2:
def g2(tool, i, j):
    gdraw.arc(tool.x, tool.y, i,j, -1)
    
# G3:
def g3(tool, i, j):
    gdraw.arc(tool.x, tool.y, i,j, 1)
    
# G20: 
def g20(tool):
    tool.unit = 'mm' 
    pass

# G21:
def g21(tool):
    tool.unit = 'inch'
    pass

# G90:
def g90(tool):
    tool.mode = 'abs'
    pass

# G91:
def g91(tool):
    tool.mode = 'inc'
    pass
    
# M2:
def m2(tool):
    print("EXIT")
    sys.exit()

# M6:
def m6(tool):
    tool.currTool =  tool.nextTool
    gdraw.m6(tool.currTool)
    # call the hardware stuff
    pass
    
# M72:
def m72(tool):
    
    pass