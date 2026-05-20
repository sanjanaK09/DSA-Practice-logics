# 
class Tree:
    def __init__(self,data):
        self.data = data
        self.child =[]
    
    def __str__(self,level =0):
        ret =" "* level + str(self.data)+ "\n"
        for ch in self.child:
            ret += ch.__str__(level+1)
        return ret 
    def addChild(self,object):
        self.child.append(object)
        print("Tree node added")
        
rootNode= Tree("N1")
N2      = Tree("N2")
N3      = Tree("N3")
N4      = Tree("N4")
N5      = Tree("N5")
N6      = Tree("N6")
N7      = Tree("N7")
N8      = Tree("N8")
rootNode.addChild(N2)
rootNode.addChild(N3)
N2.addChild(N4)
N2.addChild(N5)
N3.addChild(N6)
N4.addChild(N7)
N4.addChild(N8)

print(rootNode)

