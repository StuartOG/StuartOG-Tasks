school = ["AAAA", "BBBB", "CCCC", "DDDD"]
medal = [4,7,1,3]
system = True
while system == True:
    Medal_input = int(input("Enter a school number"))
    if Medal_input < 4 and Medal_input > 0:
        medal[Medal_input-1] += 1
        continuing = input("Would you like to continue?y/n")
        if continuing == "y":
            system = True
        else:
            system = False
    elif Medal_input == -1:
        for i in range(4):
            print(i+1)
            print(school[i])
            print(medal[i])
        continuing = input("Would you like to continue?y/n")
        if continuing == "y":
            system = True
        else:
            system = False



