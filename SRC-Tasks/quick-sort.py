list = ["A", "F", "G", "B", "E", "C", "H", "D"]


def arrSwap(a, b, arr):
    temp = arr[b]
    arr[b] = arr[a]
    arr[a] = temp


def quickPass(list):
    pivot = len(list)
    ptr = 0
    direction = 1
    while ptr != pivot:
        if ((direction ==  1 and list[ptr] > list[pivot]) or 
            (direction == -1 and list[ptr] < list[pivot])):
            arrSwap(ptr, pivot, list)
            pivot, ptr = ptr, pivot
            direction = direction *-1
        #end if
        ptr += direction
    #end while
    return pivot
#end function

quickPass(list)