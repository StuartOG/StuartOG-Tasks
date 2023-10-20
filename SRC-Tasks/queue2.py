class Queue_data:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = [0 for _ in range(max_size)]
        self.size = 0
        self.fp = 0
        self.rp = 0
    #end constructor

    def __repr__(self) -> str:
        return_str = ""
        ptr = self.fp
        while ptr != self.rp:
            return_str += str(self.data[ptr]) + ""
            ptr = (ptr + 1) % self.mac_size
        #end while
        return return_str
#end record

new_q1 = Queue_data(5)
new_q2 = Queue_data(7)

def isEmpty(q):
    return q.size == 0
#end function

def isFull(q):
    return q.max_size == q.size
#end function

def enqueue(item, q):
    if not isFull(q):
        q.rp = (q.rp + 1) % q.max_size
        q.size += 1
        q.data[q.rp] = item
    else:
        print("Error")
    #end if
#end function

def dequeue(q):
    if isEmpty():
        return 0
    else:
        
        q.front = (q.front + 1) % q.maxsize
        q.size = q.size - 1
    return q[q.front - 1] 

print(new_q1.data)
for num in range(11,15):
    enqueue(num, new_q1)
#endfor
print(new_q1.data)

print(new_q2.data)
for num in range(16, 21):
    enqueue(num, new_q2)
#next num
print(new_q2.data)
        
