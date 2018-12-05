def examgrade():
    print("Enter an exam grade")
    grade = int(input())
    if grade >= 50:
        status = "pass"
    else:
        status = "fail"
    print(grade,"is a",status)
examgrade()
