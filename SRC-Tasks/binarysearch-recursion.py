def binarySearch(array, itemSought, first, last):

    if last >= first:

        mid = first + (last - first)//2

        # If found at mid, then return it
        if array[mid] == itemSought:
            return mid

        # Search the left half
        elif array[mid] > itemSought:
            return binarySearch(array, itemSought, first, mid-1)

        # Search the right half
        else:
            return binarySearch(array, itemSought, mid + 1, last)

    else:
        return -1
