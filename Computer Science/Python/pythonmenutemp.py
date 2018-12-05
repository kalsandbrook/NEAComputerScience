from random import *
import sys
def menu():
    print("----------------------")
    print("Menu:")
    print("A - Choice1")
    print("B - Choice2")
    print("C - Choice3")
    print("Q - Quit")
    print("----------------------")
    choice = input("Enter the letter: ")
    if choice == "A":
        print("----------------------")
        print("A Chosen.")
        menu()
    elif choice == "B":
        print("----------------------")
        print("B Chosen.")
        menu()
    elif choice == "C":
        print("----------------------")
        print("C Chosen.")
        menu()
    elif choice == "Q":
        print("----------------------")
        print("Quitting....")
        input("Press ENTER to quit.")
        print("----------------------")
        sys.exit()
    else:
        print("----------------------")
        print("INVALID RESPONSE")
        print("RESTARTING")
        menu()
menu()
        
        
    
