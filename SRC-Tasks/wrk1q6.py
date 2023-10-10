rows, cols = (10, 6)
arr = [['empty' for i in range(cols)] for j in range(rows)]
for row in arr:
    for x in row:
        print(x, end=' ')
    print()
system = True
while system is True:
    car_row = int(input("Enter the row you parked in: "))
    car_row = car_row - 1
    car_col = int(input("Enter the column you parked in: "))
    car_col = car_col - 1
    if arr[car_row][car_col] == 'taken':
        print("Enter a valid spot")
        system = True
    #end if
    
    arr[car_row][car_col] = 'taken'
    for row in arr:
        for x in row:
            print(x, end=' ')
        print()
    question = input("Do you want to continue? y or n: ")
    if question == "y":
        system = True
    else:
        system = False



