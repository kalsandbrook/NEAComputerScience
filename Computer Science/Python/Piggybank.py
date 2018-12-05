#Asks the user for input and assigns it to penniesin
def pennies():
    #declares the amount of pennies in as a global variable so it can be used elsewhere
    ###
    global penniesin
    print("How many pennies are you putting into the bank?")
    penniesin = input()
    #This makes sure the user has entered a valid number, and not a string.### Why not int the input?
    try:
        int(penniesin)
    except ValueError:
        #This is the error returned. Then the subroutine is called again & looped
        print("This is not a valid integer")
        pennies()
    #This actually defines the input as an integer
    penniesin = int(penniesin)



#The Process is used again for two and five pennies.

def twopennies():
    global twopenniesin
    print("How many two pences are you putting into the bank?")
    twopenniesin = input()
    try:
        int(twopenniesin)
    except ValueError:
        print("This is not a valid integer")
        twopennies()
    twopenniesin = int(twopenniesin)
    
def fivepennies():
    global fivepenniesin
    print("How many five pences are you putting into the bank?")
    fivepenniesin = input()
    try:
        int(fivepenniesin)
    except ValueError:
        print("This is not a valid integer")
        fivepennies()
    fivepenniesin = int(fivepenniesin)
    
def accumulator():
    #This accumulates the amount of pennies and defines it as an integer
    totalpennies = penniesin + (fivepenniesin * 5) + (twopenniesin * 2)
    #This converts the integer into a string so it can be printed easier
    totalpennies = str(totalpennies)
    print(totalpennies+"p is currently in the bank")

#This calls the subroutines.
pennies()
twopennies()
fivepennies()
accumulator()
    
        
