#Asks the user for input and assigns it to coinsin
def insertcoins():
    print("How many pennies are you putting into the bank?")
    coinsin = input()
    try:
        int(coinsin)
    except ValueError:
        print("This is not a valid integer")
        insertcoins()
    coinsin = int(coinsin)
    
        
