import sys
#Exercise 1
#Print your name 100 times
def name100():
    name = input("Enter your name: ")
    for x in range(100):
        print(name)
    print("Done.")
#Exercise 2
#Print your name 100 times horizontally too.
def name100Horiz():
    name = input("Enter your name: ")
    for x in range(100):
        print(name,end='')
    print("Done.")
#Exercise 3
#Name 100 times with numbered lines
def name100numbered():
    name = input("Enter your name: ")
    line = int(0)
    for x in range(100):
        line = line + 1
        print(line, name)
    print("Done.")
#Exercise 4
#All integers from 1 to 20 and their squares
def squaredintegers():
    input()
    for x in range(1,21):
        basenum = x
        squarenumber = basenum * basenum
        print(basenum,"---",squarenumber)
def increment3():
    input("Begin")
    n = 8
    for x in range(27):
        n = n + 3
        print(n)
def reduction():
    input("Start")
    n = 100
    for x in range(49):
        n = n - 2
        print(n)
def lettersequence():
    print("Not done")
def namespecific():
    name = input("What is your name? ")
    amount = int(input("How many times? "))
    x = 0
    while x != amount:
        print(name)
        amount = amount - 1
def fibonacci(amt):
    print("Unfinished and probably broken.")
    print("EXPECTED --- 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610")
    exe = 0
    amt = int(input())
    a = 0
    b = 1
    while exe >= amt:
        c = a+b
        print(a,b,c)
        a = b+c
        b = c+a
def name():
    print("Good day")
    print("Your name?")
    name = input()
    #makes sure the name has a full stop on the end of it
    name = name + "."
    str(name)
    print("Nice to see you,", name)
    mockmenu()


def lovelace():
    fname= input("Your first name?")
    lname= input("Your last name?")
    funame = fname + " " + lname
    print("Hello",funame.title()".")
    mockmenu()

def whtspc():
    print("Telford Priory")
    print("\tTelford Priory")
    print("Telford\nPriory")
    print("Telford\n\tPriory")

def whitestrip():
    lang = "     Python    "
    print(lang.rstrip())
    print(lang.lstrip())
    print(lang.strip())
#------------------------------------#
#Select an exercise
def menu():
    choice = eval(input("Enter a defined name: "))
    choice()
#menu()
