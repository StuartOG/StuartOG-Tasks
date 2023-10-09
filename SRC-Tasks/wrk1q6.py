x = "empty"
y = "taken"
car_park_array = [
    [x,x,x,x,x,x,x,x,x,x],
    [x,x,x,x,x,x,x,x,x,x],
    [x,x,x,x,x,x,x,x,x,x],
    [x,x,x,x,x,x,x,x,x,x],
    [x,x,x,x,x,x,x,x,x,x],
    [x,x,x,x,x,x,x,x,x,x],
]
for col in car_park_array:
    print(col)
parking_row = input("Input row you parked: ")
parking_col = input("Input column you parked: ")
car_park_array[parking_col][parking_row] = y
for i in car_park_array:
    if parking_row and parking_col == x:
        print("Valid parking spot")
        car_park_array[parking_col][parking_row] = y
    elif parking_row and parking_row == y:
        print("Invalid spot")
for col in car_park_array:
    print(col)

