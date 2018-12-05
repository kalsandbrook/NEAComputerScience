import random
import sys
def gencode():
    #Generates the code
    a = random.randint(1,9);b = random.randint(1,9);c = random.randint(1,9);d = random.randint(1,9)
    #Makes sure the code has no duplicate integers
    if a == b:
        gencode()
    if b == c:
        gencode()
    if c == d:
        gencode()
    if a == d:
        gencode()
    if b == d:
        gencode()
    if c == a:
        gencode()
    global codelist
    global code
    codelist = (a,b,c,d)
    #Compiles the list of the numbers into one integer
    code = int(''.join(map(str,codelist)))
def choice():
    print("--------------------------------------------")
    print("Enter your guess to the number or type exit.")
    print("--------------------------------------------")
    print("Cows =","Bulls =")
    print(code)
    global cmd
    cmd = input()
    if cmd.lower() == "exit":
        conf = input("Are you sure?")
        if conf == "yes":
            sys.exit()
        else:
            choice()
    elif len(cmd) != 4:
        print("--------------------------------------------")
        print("Length Error")
        choice()
    elif len(cmd) == 4:
        try:
            cmd = int(cmd)
        except ValueError:
                print("This is not a whole number.")
                choice()
        check()
    else:
        print("Error")
        choice()


def check():
    global cmdlist
    cmdstr = str(cmd)
    cmdlist=list(cmdstr);
    print(cmdlist)
    enumerate(cmdlist)
    print(cmdlist)
gencode()
choice()
