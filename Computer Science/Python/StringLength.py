from string import *
import sys
found = 0
I = 0
string = input("String: ")
stringlen = int(len(string))
print("Length =",stringlen)
searchcrit = int(input("Criterium: "))
def lengthtest():
    if I == stringlen:
        if found == "true":
            print("Item found.")
        elif found != "true":
            print("Item not found.")
    elif I != stringlen:
        if I == searchcrit:
            found = "true"
        elif I != searchcrit:
            I = I+1
            lengthtest()
lengthtest()
