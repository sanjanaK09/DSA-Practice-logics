import sys
class Queue:
    
    def __init__(self,size):
        self.myQueue=[]
        self.queueSize = size
    def isFull(self):
        if len(self.myQueue) == size:
            return True
        else:
            return False
#-------------------------------------------------------------#      
    def Enque(self,value):
        if self.isFull():
            print("Queue is Full")
        else:
           self.myQueue.append(value)
        print("Element push") 


    def display(self):
        print(self.myQueue) 


    def isEmpty(self):
        if self.myQueue == []:
            return True
        else:
            return False
        

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.myQueue.pop(0))


    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.myQueue[0])   


    def deleteQueue(self):
        self.myQueue =None  

#--------------------------------------------------------------------------------------#


size = int(input("Enter the size of Queue:"))               
print("Queue has created:")
obj = Queue(size)
while True:
     
     
    print("1. Enque Operation :")
    print("2. Display Queue :")
    print("3. DeQueue Operation :")
    print("4. Peek Operation :")
    print("5. Delete Queue")
    print("6. Queue Full")
    print("7. Exit")

 #--------------------------------------------------------------------------#

    choice =int(input("Enter your choice:"))
    if choice == 1:
        value = int(input("Enter value in Queue :"))
        obj.Enque(value)
    elif choice ==2:
        obj.display()
    elif choice ==3:
        obj.deQueue() 
    elif choice ==4:
        obj.peek() 
    elif choice ==5:
        obj.deleteQueue() 
    elif choice ==6:
        obj.isFull()      
    else:
        sys.exit()

