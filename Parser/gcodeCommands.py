#G code commands
import sys

mode = 'inc'        # default incremental, set to 'abs' for absolute
unit = 'inch'       # default unit, set to 'mm' for millimeters

#Parameter definitions: 
#   X:      x-coordinate or distance
#   Y:      y-coordinate or distance
#   fr:     Feed rate 
#   unit:   current units (default = inches)
#   mode:   current mode (default = relative)

# G0:
def g0(para):
    if len(para) != 2:
        return -1
    else: 
        #print (" move to %s", para)
        pass

# G1:
def g1(para):
    
    pass

# G2:
def g2(para):
    
    pass

# G3:
def g3(para):
    
    pass

# G20: 
def g20(para):
    
    pass

# G21:
def g21(para):
    
    pass

# G90:
def g90(para):
    
    pass

# G91:
def g91(para):
    
    pass
    
# M2:
def m2(para):
    print("EXIT")
    sys.exit()

# M6:
def m6(para):

    gdraw.m6()
    pass
    
# M72:
def m72(para):
    
    pass