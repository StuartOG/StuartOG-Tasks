class Stack:
    def __init__(self, size) -> None:
        self.maxSize = size
        self.data = ["" for _ in range(size)]
        self.sp = -1
    #end constructor

    def size(self):
        return self.sp + 1

    def isFull(self):
        return self.size() == self.maxSize

    def isEmpty(self):
        return self.sp == -1

    def push(self, item):
        if self.isFull():
            print("Already full")
        else:
            self.sp += 1
            self.data[self.sp] = item


    def pop(self):
        if self.isEmpty():
            print("Already empty")
        else:
            temp = self.sp
            self.sp -= 1
            return self.data[temp]

#end class
myString = input("Enter word or phrase: ")
numChars = len(myString)
s = Stack(numChars)
for c in myString:
    s.push(c)

palList = []
while not s.isEmpty():
    palList.append(s.pop())


print(s.data)
print("".join(palList))

if myString == "".join(palList):
    print("Is palindrome")
else:
    print("Is not palindrome")