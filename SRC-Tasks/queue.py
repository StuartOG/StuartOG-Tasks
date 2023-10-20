# Intitalise Queue variable
MAX_SIZE = 5
q1 = [0 for _ in range(MAX_SIZE)]
q1_size = 0
q1_fp = 0
q1_rp = -1
def isEmpty():
    global q1_size
    return q1_size == 0
def isFull():
    global MAX_SIZE
    global q1_size
    return MAX_SIZE == q1_size
#end function
def enqueue(item):
    global q1_rp
    global q1_size
    if not isFull():
        q1_rp = (q1_rp + 1) % MAX_SIZE
        q1_size += 1
        q1[q1_rp] = item
    #end if
#end procedure
def dequeue():
    global q1_fp
    global q1_size
    if not isEmpty():
        item_p = q1_fp
        q1_fp = (q1_fp + 1) % MAX_SIZE
        q1_size -= 1
        return q1[item_p]
    #end if
#end function
    
for num in range(11,16):
    enqueue(num)
#next num
print(q1)
enqueue(16)
print(q1)
for _ in range(6):
    print(dequeue())
#next _
print(q1)
enqueue(20)
print(q1)