class Node:
    def __init__(self,name,pointer) -> None:
        self.name = name
        self.pointer = pointer
    #end constructor
    def __repr__(self) -> str:
        return "Data:"+self.name+",Ptr:"+str(self.pointer)
#end Node record
# Create array of blank Nodes (records)
myList = [Node("",-1) for _ in range(50) ]
for index in range(49):
    myList[index].pointer = index + 1
#next index
myList[49].pointer = -1
start = 1
nextfree = -1
print(myList)

def AddItem(newItem):
    #check if list is full and if so, print error message
    if nextfree == None:
        print("Error")
    else:
        newName = myList[nextfree].name
        if start == None:
            temp = myList[nextfree].pointer       #save pointer
            myList[nextfree].pointer = None
            start = nextfree
            nextfree = temp
        else:
            p = start
            if newName < myList[p].name:  
                start  = myList[nextfree].pointer
                start = nextfree
            else:   
                placeFound = False    #general case
                while myList[p].pointer != None and placeFound == False:
                    #peek ahead
                    if newName >= myList[myList[p].pointer].name:
                        p = myList[p].pointer
                    else:
                        placefound = True
                    
                
                temp = nextfree
                nextfree = Node[nextfree].pointer
                Node[temp].pointer = Node[p].pointer
                Node[p].pointer = temp
