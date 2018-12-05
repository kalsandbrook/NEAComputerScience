import sys; import random; import os
'''
Password Checker
10/07/2018 - 16/07/2018 - Kal Sandbrook
YSH Year 10 - Computer Science
'''
genpass = []
pread = open("password.txt","r")
p = pread.read()
quiet = "no"
print("\n"*50)
#-------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------------------------------------------#
def passlength(): # This checks the length of the password to ensure it meets regulation
    global p 
    # Strips the password entry of any whitespace on the edges
    p = p.strip()
    if len(p) >= 8:
        if len(p) <= 24:
            pass
            # The two error outcomes below indicate a length error, and then restart the program from the beginning
        else:
            if quiet == "no":print("Password too long, Invalid.")
            setpass()
    else:
        if quiet == "no":print("Password too short, Invalid.")
        setpass()



#-------------------------------------------------------------------------------------------------------------------------------------------#        
def charcheck():
    plist = list(p) # Checks for any spaces in a character and returns an error in that case
    for char in plist:
        if char == " ":
            if quiet == "no":print("Spaces are not permitted in passwords.")
            setpass()



#-------------------------------------------------------------------------------------------------------------------------------------------#    
def verifypass(): # This subroutine exists to verify that the entered password is correct, in case of human error.
    verifp = input("Please enter your password again: ").strip()
    if verifp == p:
        print("Password Verified.")
        print("Exiting...")
        savepass()
        menu()
    else:
        print("Invalid Password; Try again.")
        setpass()


    
#-------------------------------------------------------------------------------------------------------------------------------------------#
def generatepass():
    allowedchars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', ')', '_', '+', '@', '$', '£', '/', '!', '?']
    global p
    gp = ''
    genpass = []
    for x in range(10):
        genpass.append(random.choice(allowedchars))
    gp = gp.join(genpass)
    print("Your generated password is:",gp)

    print("Is this acceptable? (Y/N) ")
    genconf = input()
    if genconf.lower() == "yes":
        p = gp
        savepass()
        print("This is your new password")
        menu()
    elif genconf.lower() == "y":
        p = gp
        savepass()
        print("This is your new password")
        menu()
    else:
        print("A new password will be generated.")
        generatepass()



#-------------------------------------------------------------------------------------------------------------------------------------------#
def login():
    print("---------------------------")
    loginattempt = input("Enter password to login: ")
    if loginattempt == p:
        print("Login success!")
    else:
        print("Login failed.")



#-------------------------------------------------------------------------------------------------------------------------------------------#        
def savepass():
    f = open("password.txt","w")
    pchar = [pl for pl in p]
    for pl in pchar:
        f.write(pl)
    f.close()
    print("Password Saved Successfully.")


def setpass():
    global p
    p = input("Enter a new password: ")
    passlength()
    charcheck()
    verifypass()
    savepass()
#-------------------------------------------------------------------------------------------------------------------------------------------#
def menu(): #Menu for running different subroutines
    print("-----------------------------")
    print("--- A - Login ---------------")
    print("--- B - Set Password --------")
    print("--- C - Generate Password ---")
    print("--- D - Exit Program --------")
    print("-----------------------------")
    cmd = input("Select: ")
    if cmd.lower() == "a":
        login()
    elif cmd.lower() == "b":
        setpass()
    elif cmd.lower() == "c":
        generatepass()
    elif cmd.lower() == "d":
        print("Are you sure you want to exit? (Y/N)")
        confquit = input()
        if confquit.lower() == "yes":
            print("Quitting...")
            sys.exit()
        else:
            print("Not quitting.")
            menu()
menu()
