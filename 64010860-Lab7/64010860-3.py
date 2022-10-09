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

    def findUp(self,node,num):
        global list
        if node:
            if int(node.data) > int(num):
                node.data = node.data*3
                self.findUp(node.right,num)
                self.findUp(node.left,num)
            else:
                self.findUp(node.right,num)
                self.findUp(node.left,num)
               
        return list


list = []
T = BST()
inp,num = [i for i in input('Enter Input : ').split('/')]
inpdata = [int(i) for i in inp.split()]
for i in inpdata:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
T.findUp(root,num)
T.printTree(root)


