class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)
        return self.root
    
    def _insert(self,data,currentNode):
        if data<currentNode.data:
            if currentNode.left==None:
                currentNode.left = Node(data)
            else:
                self._insert(data,currentNode.left)
        elif data>currentNode.data:
            if currentNode.right==None:
                currentNode.right = Node(data)
            else:
                self._insert(data,currentNode.right)
           
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def checkpos(self,num):
        
        if self.root.data == num:
            print('Root')
            return
        else:
            self.findpos(self.root,int(num))
    
    def findpos(self,currentNode,data):

        if currentNode is None:
            print('Not exist')
            return
        elif data < currentNode.data:
            currentNode.left = self.findpos(currentNode.left,data)
        elif data > currentNode.data:
            currentNode.right = self.findpos(currentNode.right,data)
        elif data==currentNode.data:
            if currentNode.left is None and currentNode.right is None:
                print('Leaf')
                return
            else:
                print('Inner')
                return




    
            


             

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(int(inp[0]))