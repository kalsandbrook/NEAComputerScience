from random import *
import sys
from time import *
def main():
    print("------------------------------------------")
    print("Press ENTER to shake the Magic 8 Ball")
    print("------------------------------------------")
    sleep(1)
    print("What is your question?")
    input(">> ")
    n = randint(1,6)
    if n == 1:
        sleep(0.5)
        print("It is completely certain.")
    elif n == 2:
        sleep(0.5)
        print("It's a yes from me")
    elif n == 3:
        sleep(0.5)
        print("The sights are unclear")
    elif n == 4:
        sleep(0.5)
        print("It's unforeseeable at this point.")
    elif n == 5:
        sleep(0.5)
        print("Not happening.")
    else:
        sleep(0.5)
        print("That is a no.")
main()
for x in range(500):
    sleep(0.5)
    print("Would you like to roll again? [yes OR no]")
    repeat = input(">> ")
    if repeat == "yes":
        sleep(0.5)
        print("A new game will begin.")
        main()
    elif repeat == "no":
        sleep(0.5)
        print("The game will now exit.")
        sys.exit()
    else:
        sleep(0.5)
        print("Invalid response. Game will exit")
        sys.exit()
        
