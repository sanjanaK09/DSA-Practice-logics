##--FULL BINARY TREE
#Each node has either 0 or 2 children
#No node has a single child

##--COMPLETE BINARY TREE
#All levels excepts possibly the last are completely filled
#Nodes in the last level are filled from left to right 
 
 ##--PERFECT BINARY TREE
 #All internal nodes have exactly two nodes
 #All leaf nodes are ot the same level
 
 
##--OPERATIONS PERFORMED
#1. creation of tree
#2. insertion of a node
#3. deletion of node
#4. search for a value
#5. traverse all nodes
#6. deletion of tree



class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftchild= None
        self.rightchild=None

def insertNode(rootNode,nodeValue):
    if rootNode.data==None:
        rootNode.data = nodeValue
            
    elif nodeValue <=rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild= BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftchild,nodeValue)
    else :
        if rootNode.rightchild is None:
            rootNode.rightchild= BSTNode(nodeValue)  
        else:
            insertNode(rootNode.rightchild,nodeValue)  

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data,end=" ")
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)
    
    
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data,end=" ")
    inOrderTraversal(rootNode.rightchild) 
    
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data,end=" ")

def searchNode(rootNode,nodeValue):
    if rootNode.data==nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftchild == None:
            print("The value not found")
        elif rootNode.leftchild == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftchild,nodeValue)
    elif nodeValue> rootNode.data:
        if rootNode.rightchild == None:
            print("Value not found ")
        elif rootNode.rightchild == nodeValue:
            print("Value is found ")
        else:
            searchNode(rootNode.rightchild,nodeValue)
    else:
        print("Value not found")
      
        
           

newBST = BSTNode(None)
insertNode(newBST,70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
preOrderTraversal(newBST)
print()
inOrderTraversal(newBST)
print()
postOrderTraversal(newBST)
print()
searchNode(newBST,22)
print()
searchNode(newBST,20)
print()
