def summary():
        #time.sleep(1)
        print("You have",lives," tries left.")
        print("You have",score," points")
        #time.sleep(1)
    print("------------------------------------------------------")
    print("Welcome to rock paper scissors, press RETURN to begin.")
    print("Or type RULES for rules!")
    print("------------------------------------------------------")
    wantRules = input("")
    if wantRules.lower() == "rules":
        print("Paper beats rock")
        #time.sleep(1)
        print("Rock beats scissors")
        #time.sleep(1)
        print("Scissors beats paper")
        #time.sleep(1)
        print("If they're the same, it's a tie!")
        repeat()
    else:
        print("Okay, lets begin.")
        #time.sleep(1)
def guess():
  global userguess
  global cpuguess
  userguess = input("'rock', 'paper' or 'scissors'? \n Input: ")
  if userguess.lower() == "rock":
    userguess = 1
  elif userguess.lower() == "paper":
    userguess = 2
  elif userguess.lower() == "scissors":
    userguess = 3
  else:
      print("Rock, paper, or scissors?")
      #time.sleep(1)
      guess()
def repeat():
    lives = 3
    score = 0
    import random
    import time
   

def main():
  global lives
  global score
  print("Make your guess!")
  #time.sleep(1)
  guess()
  '''
  1 = rock
  2 = paper
  3 = scissors
  '''
  cpuguess = random.randint(1, 3)
  if userguess == 1 and cpuguess == 2:
      #time.sleep(1)
      print("Paper beats rock, so I win!")
      lives = lives - 1
      if lives > 0:
        summary()
        main()
  elif userguess == 1 and cpuguess == 3:
      #time.sleep(1)
      print("Rock blunts my scissors, you win.")
      score = score + 5
      if lives > 0:
        summary()
        main()
  elif userguess == 1 and cpuguess == 1:
      #time.sleep(1)
      print("It's a tie, lets repeat.")
      if lives > 0:
        summary()
        main()
  elif userguess == 2 and cpuguess == 1:
      #time.sleep(1)
      print("Paper covers rock, you win.")
      score = score + 5
      if lives > 0:
        summary()
        main()
  elif userguess == 2 and cpuguess == 2:
      #time.sleep(1)
      print("It's a tie.")
      if lives > 0:
        summary()
        main()
  elif userguess == 2 and cpuguess == 3:
      #time.sleep(1)
      print("Scissors win.")
      lives = lives - 1
      if lives > 0:
        summary()
        main()
  elif userguess == 3 and cpuguess == 1:
      #time.sleep(1)
      print("Rock wins and so do I")
      lives = lives - 1
      if lives > 0:
        summary()
        main()
  elif userguess == 3 and cpuguess == 2:
      #time.sleep(1)
      print("Scissors win, so do you.")
      score = score + 5
      if lives > 0:
        summary()
        main()
  else:
      print("It's a tie.")
      if lives > 0:
        summary()
        main()
if lives > 0:
    main()
print("The game has ended.")
summary()
print("Starting again, automatically.")
repeat()
repeat()
