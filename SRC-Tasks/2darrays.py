rows, cols = (6, 4)
arr = [['x' for i in range(cols)] for j in range(rows)]
arr[0][0]='O'
for row in arr:
    for x in row:
        print(x, end=' ')
    print()
my_row = int(input("Enter a row to move to: "))
my_row = my_row - 1
my_col = int(input("Enter a col to move to: "))
my_col = my_col - 1

arr[0][0] = 'X'
arr[my_row][my_col] = 'O'
for row in arr:
    for x in row:
        print(x, end=' ')
    print()