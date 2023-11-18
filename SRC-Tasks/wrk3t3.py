class Node:
    def __init__(self,name,pointer) -> None:
        self.name = name
        self.pointer = pointer
    #end constructor
    def __repr__(self) -> str:
        return "Data:"+self.name+",Ptr:"+str(self.pointer)
#end Node record
# Create array of blank Nodes (records)
myList = [Node("",-1) for _ in range(5) ]
for index in range(4):
    myList[index].pointer = index + 1
#next index
myList[4].pointer = -1
start = 0
nextfree = 0
print(myList)

def outputList(arr):
    global start
    current_pointer = start
    while current_pointer != -1:
        print(arr[current_pointer].name)
        current_pointer=arr[current_pointer].pointer
    #end while
#end procedure

def AddItem(newItem, myList):
    global nextfree
    global start
    #check if list is full and if so, print error message
    if nextfree == -1:
        print("Error")
    else:
        myList[nextfree].name = newItem
        if start == -1:
            temp = myList[nextfree].pointer       #save pointer
            myList[nextfree].pointer = -1
            start = nextfree
            nextfree = temp
        else:
            p = start
            if newItem < myList[p].name:
                temp = myList[nextfree].pointer  
                start = myList[nextfree].pointer
                start = nextfree
                nextfree = temp
            else:   
                placefound = False    #general case
                while myList[p].pointer != -1 and placefound == False:
                    #peek ahead
                    if newItem >= myList[myList[p].pointer].name:
                        temp = myList[nextfree].pointer
                        
                        myList[p].pointer = -1

                    else:
                        placefound = True
                    
                
                temp = nextfree
                myList[nextfree].pointer = nextfree
                myList[temp].pointer = myList[p].pointer
                myList[p].pointer = temp


AddItem("Colin",myList)
AddItem("Albert",myList)
AddItem("Barry",myList)
AddItem("Derek",myList)
AddItem("Fred",myList)
print(nextfree)
# outputList(myList)
# AddItem("Trevor",myList)
