#A program to display the number which is picked
runs = True
while runs: 
    option = int(input("What number do you want between 1 and 3?: "))
    if option >= 1 and option <= 3:
        print("You have chosen ", option)
        runs = False
    else:
        print("Please pick anlother number")


