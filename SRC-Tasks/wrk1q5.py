x ="X"
o = "O"
grid_array = [[o, x, x, x], 
              [x, x, x, x],
              [x, x, x, x],
              [x, x, x, x],
              [x, x, x, x],
              [x, x, x, x],
              ]
grid_array[0][0] = o
for col in grid_array:
    print(col)
movement = input("Input a movement: ")
for x in grid_array:
    if movement == "right":
        grid_array[0][0+1] = o
        grid_array[0][0] = grid_array[0][2]
    elif movement == "down":
        grid_array[0+1][0] = o
        grid_array[0][0] = grid_array[2][0]
    elif movement == "left":
        grid_array[0][3] = o
        grid_array[0][0] = grid_array[2][0]
    elif movement == "up":
        grid_array[5][0] = o
        grid_array[0][0] = grid_array[2][0]
for col in grid_array:
    print(col)