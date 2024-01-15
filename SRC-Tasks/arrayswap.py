arr = ['Sophie', 'Lily', 'Jessica', 'Isabella', 'Ava', 'Poppy', 'Emily', 'Isla', 'Olivia', 'Amelia']
def arrSwap(a, b, arr):
    temp = arr[b]
    arr[b] = arr[a]
    arr[a] = temp


def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arrSwap(j,j+1, arr)
            #end if
        #next j
    #next i
#end procedure
            
print(arr)
bubble_sort(arr)
print(arr)