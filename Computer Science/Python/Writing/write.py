string = ""
while string.lower() != "stop":
    string = input("Enter a string: ")
    write = open("write.txt","w")
    wchar = [wr for wr in string]
    for wr in wchar:
        write.write(wr)
    write.close()
