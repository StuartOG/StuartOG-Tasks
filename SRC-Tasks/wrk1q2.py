MAX = 10
name_array = ["" for _ in range(MAX)]
for i in range(MAX):
    name_array[i] = input("Input a name: ")
#end for
search_name = input("Enter a name to find: ")
index = 0
found = False
while not found and index < MAX:
    if name_array[index] == search_name:
        found = True
    #end if
    index = index + 1
#end while
if found:
    print("index number is", index)
else:
    print("Not found")
#end if
print(name_array)
