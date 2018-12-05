import random
import sys
def flip():
    #input(random.choice(["Heads","Tails"]))
    print("How many times do you want to flip the coin?")
    flipc = input()
    try:
        int(flipc)
    except ValueError:
        print("Not an integer.")
        flip()
    flipc = int(flipc)
    tosses = []
    for x in range(flipc):
        toss = random.choice(["Heads","Tails"])
        tosses.append(toss)
    headsc = 0
    tailsc = 0
    #Counts the result of each flip and adds it to a variable
    for tossed in tosses:
        if tossed == "Heads":
            headsc = headsc+1
        elif tossed == "Tails":
            tailsc = tailsc+1
        else:
            print("Oh Crap")
    print("Tails =",tailsc)
    print("Heads =",headsc)
def dice():
    input(random.randint(1,6))
def menu():
    print("--------------------------------")
    print("1 - Flip Coin ------------------")
    print("2 - Roll Dice ------------------")
    print("Q - Exit      ------------------")
    print("--------------------------------")
    cmd = input("Select: ")
    if cmd.lower() == "1":
        flip()
    elif cmd.lower() == "q":
        print("Are you sure you want to exit? (Y/N)")
        confquit = input()
        if confquit.lower() == "yes"or"y":
            print("Quitting...")
            sys.exit()
        else:
            print("Not quitting.")
            menu()
    elif cmd.lower() == "2":
        dice()
    else:
        print("Invalid.")
        menu()
menu()
