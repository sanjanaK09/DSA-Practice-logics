
import sys
class Stack:
    # def __init__(self):
    def __init__(self,size):
        self.myStack =[] #creating stack
        self.stackSize= size
        
    def isFull(self):
        if len(self.myStack)==self.stackSize:
            return True
            # print("Stack is full:")
        else:
            return False
            
    def push(self,value):
        self.myStack.append(value)
        print("----------Element push----------")
        
    def display(self):
        print(self.myStack) 
    
    def isEmpty(self):
        if self.myStack ==[]:
            return True
        else:
            return False  
    
    def pop(self):
        if self.isEmpty():
            print("------------Stack iss empty-----------")
        else:
            print(self.myStack.pop())
    
    def peek(self):
        if self.isEmpty():
            print("---Stack is empty---")
        else:
            print(self.myStack[-1])
    
    def deleteStack(self):
        self.myStack = None
# stack=[]
# max_size=5  
size = int(input("Enter the size of stack :")) 
obj = Stack(size)   
print("stack has created:")    
while True:
   
    print("-->1.Push Operation :")
    print("-->2.Display stack  :")
    print("-->3.Pop operation  :")
    print("-->4.Peek operation :")
    print("-->5.Delete stack.  :")
    print("-->6.stack full")
    print("-->7.Exit")
    choice = int(input("-*-Enter your choice:"))
    if choice == 1:
        value = int(input("-*-Enter value to push in stack:"))
        obj.push(value)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.pop()
    elif choice == 4:
        obj.peek()
    elif choice == 5:
        obj.deleteStack()
    elif choice == 6:
        obj.isfull()
    else:
        sys.exit()
        