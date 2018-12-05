print("This will write to a file")
text = input("Enter some text: ")
f = open("thefile.txt","w")
textlist = [x for x in text]
for x in textlist:
    f.write(x)
f.close()
