import random
import sys

def menu():
    print("-------------------------")
    print("-1-PLAY------------------")
    print("-2-SETTINGS--------------")
    print("-Q-EXIT------------------")
    print("-------------------------")
    cmd = input()
    cmd = cmd.lower()
    try:
        str(cmd)
    except ValueError:
        print("Something went wrong!")
        print("Menu cmd variable")
        print("Invalid String")
        print(ValueError)
    if cmd == "1":
        print("Actual Game Stuff will be here")
    elif cmd == "2":
        print("There'll be a settings menu here")
        
    elif cmd == "q":
        print("Are you sure you want to quit?")
        cmd = input()
        if cmd.lower() == "yes"or"y":
            print("Quitting...")
            sys.exit()
        else:
            print("Not Quitting.")
    else:
        print("This is not a valid response")
        menu()

menu()
