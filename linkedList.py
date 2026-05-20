# class Node:
#     def __init__(self, data):
#         self.data= data
#         self.next= None
# class linkedlist:
#     def __init__(self):
#         self.head =None
        
# linkedlist = linkedlist()

# linkedlist.head = Node(5)
# second          = Node(10)
# third           = Node(15)
# fourth          = Node(20)

# #connecting nodes
# linkedlist.head.next= second
# second.next = third
# third.next = fourth

# #display linkedlist
# while linkedlist.head.next != None:
#     print(linkedlist.head.data,"|",linkedlist.head.next,"->",end=" ")
#     linkedlist.head = linkedlist.head.next

# ##OUTPUT:
# #5 | <__main__.Node object at 0x1043a3e80> -> 10 
# # | <__main__.Node object at 0x1043a3dc0> -> 15 
# # | <__main__.Node object at 0x1043a3d60> ->


import sys
class Node:
    def __init__(self,data):
        self.data=data # instance variable(5)
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,value):
        self.node = Node(value)
        if self.head is None:
            self.head=self.node
            self.tail=self.node
        else:
            self.tail.next=self.node
            self.tail =self.node
    
    def addNodeBeginning(self,value):
        print("Add not at beginning:")
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.node.next = self.head
            self.head = self.node
    def addNodeBetween(self,value,index):
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        elif index ==0:
            self.node.next = self.head
            self.head=self.node
        else:
            temp =self.head
            for _ in range(index-1):
                temp = temp.next
            self.node.next = temp.next
            temp.next = self.node
            
    # def addNodeEnd(self,value):
        
    #displaynode        
    def displayNode(self):
        while self.head is not None:
            print(self.head.data,"|",self.head.next,"->",end=" ")
            self.head = self.head.next
        print()
if __name__ == '__main__':
    object = linkedlist() #linkedlist object created
    #menu driven options
    while True:
        print('1.Add Node Linkedlist:')
        print('2.Add Node in begning:')
        print('3.Add Node in between:')
        print('4.Add Node in end:')
        print('5. display linked list:')
        print("6.Exit  ")
        ch = int(input("Enter your choice:"))
        if ch==1:
            value = int(input("Enter value for node:"))
            object.addNode(value)
            print('Node added succefully in single linkedlist:')
         
        elif ch==2:
            value = int(input("Enter value for node:"))
            object.addNodeBeginning(value)
            print('Node added succefully in beginning:') 
        elif ch==3:
            value = int(input("Enter value for node: "))
            index = int (input("Enter the position to insert element:"))
            object.addNodeBetween(value)
            print('Node added succefully in between:')
        elif ch==4:
             value = int(input("Enter value for node: "))
             object.addNodeEnd(value)
             print('Node added succefully at the end:')
        elif ch==5:
            object.displayNode()
            print('Node is displayed:')
        elif ch==6:
            sys.exit()




