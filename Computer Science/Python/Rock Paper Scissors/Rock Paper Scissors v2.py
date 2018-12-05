import sys
import random
roundc = 0
playerchoice = ""
compchoice = ""


def begin(): #This is where the user chooses rounds
    print("How many rounds would you like to play?")
    global totalrounds
    try:
        totalrounds = int(input())
    except ValueError:
        print("This is not a valid number.")
        begin()
    totalrounds = totalrounds + 1
    choice()

    
def choice(): #This is where the user discovers
    global roundc
    roundc = roundc + 1
    if roundc >= totalrounds:
        end()
    print("!!! Round",roundc)
    def subchoice():
        print("Choose 'rock', 'paper' or 'scissors'")
        playerchoice = input()
        if playerchoice.lower() == "paper":
            comparechoices()
        elif playerchoice.lower() == "scissors":
            comparechoices()
        elif playerchoice.lower() == "rock":
            comparechoices()
        else:
            print("Invalid!")
            subchoice()
    subchoice()

        
def comparechoices():
    possibilities = ["paper","rock","scissors"]
    compchoice = random.choice(possibilities)
    global score
    if compchoice == "paper" and playerchoice == "scissors":
        print("Player wins")
        print("Score +1")
        score = +1
        choice()
    elif compchoice == "rock" and playerchoice == "paper":
        print("Player wins")
        print("Score +1")
        score = +1
        choice()
    elif compchoice == "scissors" and playerchoice == "rock":
        print("Player wins")
        print("Score +1")
        score = +1
        choice()
    elif compchoice == playerchoice:
        print("It's a draw")
        print("Nobody wins.")
        choice()
    else:
        print("The Computer Wins!")
        score = -1
        choice()

def end():
    print("Not Implemeneted properly")
    if score < 0:
        print("You win!")
    elif score > 0:
        print("You lose!")
    else:
        print("It's a draw!")
    sys.exit()
    
begin()

        
