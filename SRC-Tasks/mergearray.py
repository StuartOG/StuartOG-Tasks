alist = [1, 3, 4, 6, 8, 9]
blist = [2, 5, 12, 14, 17]
clist = [0 for _ in range(len(alist)+len(blist))]

def merge(alist, blist, clist):
    pointer_a = 0
    pointer_b = 0
    pointer_c = 0
    while pointer_a <= len(alist) or pointer_b <= len(blist):
        if alist[pointer_a] < blist[pointer_b]:
            clist[pointer_c] = alist[pointer_a]
            pointer_c += 1
            pointer_a += 1
        else:
            clist[pointer_c] = blist[pointer_b]
            pointer_c += 1
            pointer_b += 1
    if pointer_a > len(alist):
        while pointer_b <= len(blist):
            clist[pointer_c] = blist[pointer_b]
            pointer_c += 1
            pointer_b += 1
    else:
        while pointer_a <= len(alist):
            clist[pointer_c] = alist[pointer_a]
            pointer_c += 1
            pointer_a += 1

merge(alist, blist, clist)