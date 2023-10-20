class Queue_data:
    def __init__(self, max_size):
        self.data = [0 for _ in range(max_size)]
        self.size = 0
        self.fp = 0
        self.rp = 0
    #end constructor
#end record

new_q1 = Queue_data(5)