a = 0
loopco = 0
stunames=[]
score=[]
passed=[]
minscore = 0
print("Minimum Score Boundary?")
minscore = int(input())
print("How many results do you need to input?")
amt = int(input())
while amt > loopco:
    loopco = loopco + 1
    print("Student name?")
    stunames.append(input())
    print("Result?")
    score.append(int(input()))
for a in range(amt):
    if score[a] >= minscore:
        passed.append("True")
    else:
        passed.append("False")
    print(stunames[a], score[a], passed[a])
