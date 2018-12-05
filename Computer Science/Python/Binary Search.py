string = input("Enter String: ")
search = int(input("Enter a number to search for: "))
start = 0
end = len(string)
while start <= end:
    middle = (end + start) // 2
    if middle == search:
        print("Letter found as",string[search-1])
        exit()
    elif middle < search:
        start = middle + 1
    else:
        end = middle - 1
if end > start:
    print("Letter not present")