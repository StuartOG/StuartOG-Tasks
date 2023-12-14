def linearSearch(array, end, index, itemSought):
    if array[index] == itemSought:
        return index
    
    elif array[index] == end and array[index] != itemSought:
        return -1
    
    else:
        return linearSearch(array, end, index + 1, itemSought)

array = [1, 2, 3, 36, 6, 7]

item = 36

result = linearSearch(array, len(array) - 1, 0, item)

print(str(result))