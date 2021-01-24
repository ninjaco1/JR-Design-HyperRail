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

# library
import sys
import gcodeCommands as gcom
import gcodeDraw as gdraw

# Reading individual G Code commands
# Params: string
# Return: 
def read_Gcode(params):
    # if statement hell
    # G0 X0 Y0
    # convert params [string -> list]
    temp = []
    temp.append(params)
    temp = [i for item in temp for i in item.split()]
    params = temp
    command = params[0]

    if command == 'G0':  
        if gcom.g0(params[1:]) == -1:
            print("ERROR: break in G0")
            return -1
                    
    elif command == 'G1': 
        if gcom.g1(params[1:]) == -1:
            print("ERROR: break in G1")
            return -1
                    
    elif command == 'G2': 
        if gcom.g2(params[1:]) == -1:
            print("ERROR: break in G2")
            return -1
        else:
                gdraw.g2()
            
    elif command == 'G3': 
        if gcom.g3(params[1:]) == -1:
            print("ERROR: break in G3")
            return -1            
                     
    elif command == 'G20': 
        if gcom.g20(params) == -1:
            print("ERROR: break in G20")
            return -1
        
            
    elif command == 'G21': 
        if gcom.g21(params) == -1:
            print("ERROR: break in G21")
            return -1
        
    elif command == 'G90': 
        if gcom.g90(params) == -1:
            print("ERROR: break in G90")
            return -1
                
    elif command == 'G91': 
        if gcom.g91(params) == -1:
            print("ERROR: break in G91")
            return -1
                
    elif command == 'M2': 
        if gcom.m2(params) == -1:
            print("ERROR: break in M2")
            return -1
        else:
            return False #Exit
                    
    elif command == 'M6': 
        if gcom.m6(command) == -1:
            print("ERROR: break in M6")
            return -1
                
    elif command == 'M72': 
        if gcom.m72(command) == -1:
            print("ERROR: break in M72")
            return -1
                    
    else:
        print("ERROR: Command %s not found" % command)
        return -1


# File reader - goes through file line by line, calls read_Gcode()
# Params: string (file path/name)
def read_File(f):
    # open file, reading every command from line
    f_len = open(f).readlines()  # read all the lines in the file
    for line in f_len:                # loop through file and parse gcode
        # user_in string -> list 
        condition = read_Gcode(line)
        if condition == -1 or condition == False:
            return condition
    return f_len                      # returns length of file once complete
    

# main 
if __name__ == "__main__": 
    # gcom.g0()
    
    # GUI
    while True:
        val = input("Manual or Auto: ")
        if val.lower() == "manual":
            # Manual mode: loops and reads user input as gcode
            while True:
                user_in = input("Input: ")
                # exit case, user can back out of auto mode
                if user_in.lower() == "exit":
                    break
                else:
                    # print("user_in: " + str(temp))
                    condition = read_Gcode(user_in)
                    if condition == -1 or condition == False:
                        print("Program terminating.")
                        sys.exit()
                    
        # Auto mode: read from a TXT or GCO file    
        elif val.lower() == "auto":
            file_name = input("File name/path: ")
            condition = read_File(file_name)
            if condition == -1 or condition == False:
                print("Program terminating.")
                sys.exit()
            


