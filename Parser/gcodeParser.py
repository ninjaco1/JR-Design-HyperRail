"""
FP - ECE 342 - HyperRail with OPEnS
Created: Jan. 19, 2021

The G CODE (in order)
G0	Move to (A, B); Speed = 6" per sec; EXAMPLE: G0 X6 Y18
G1	Control movement (linearly); EXAMPLE: G1 X6 Y-3 F10 [Feed rate of 10 (depends on G20 and G21)]
G2	Clockwise arc motion at feed rate 
G3	Counterclockwise arc motion at feedrate
G20	Mode: Millimeters
G21	Mode: Inches
G90	Absolute Mode: Absolute mode from the datum
G91	Incremental Mode: The opposite mode of G90, moves your machine the specifies number of units from its current point of the tool.
	Ex: G1 X1 will advance the machine 1 unit in the x direction, regardless of its current location
M2	Ends program. Resets origin offset, and does the following actions:
    Set origin offset to default
    Distance mode set to absolute
    Feed rate set to units per minute
    Feed and speed overrides are set to ON
    Current motion mode is set to feed (Like G1)
M6	Tool change. Stops tool and prompts user to change tool.
M72	Restore modal state. (Requires prevous M70 call)
"""

#library
import sys
import gcodeCommands as gcom



val = input("Manual or Auto: ")
if val == "Manual"
    while True
elif 

# Console reader (returns user input as a string)
# Params: 
# Return: 
def read_Console():
    #python test.py arg1 arg2 arg3
    #sys.argv <- array/list
    pass

# Console reader (returns user input as a string)
# Params: 
# Return: 
def read_Console(
    ):
    #pyt
    pass
parserreader - goes through file line by line, calls read_Gcode()
# File reader - goes through file line by line, calls read_Gcode()
def read_File(f):
    #open file
    f_len = len(open(f).readlines())
    pass
# Params: string (file path/name)
def read_File(f):
    #open file
    f_len = len(open(f).readlines())
    pass

# ma# in 
if _# _name__ == "__main__": 
    # # if sthell
    #         read_File(user_in)
# 
    # # while True:
    #     else
            
    #     user_in = read_Console()
    #     if #it's a file name or path
    #         read_File(user_in)
    #     elif #it's a gcode command
    #         read_Gcode(user_in)
    #     else
            
    pass


