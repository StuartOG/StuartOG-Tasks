name = ["r", "o", "b", "e", "r", "t"]
stack = []
outName = []
for c in name:
    stack.append(c)

for i in range(0, len(stack)):
    outName.append(stack.pop())
    print(len(stack)-1)

print(outName)