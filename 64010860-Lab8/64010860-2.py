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


def closestValue(root,value):
    current = root
    closest = root.data
    while current is not None:
        if current.data == value:
            return value

        if abs(value - closest) > abs(value - current.data):
            if current.data > 0 and closest > 0:
                closest = current.data
            elif current.data < 0 and closest < 0 and current.data>closest:
                closest = current.data
            elif current.data < 0 and closest > 0:
                closest = current.data
        
       

        if value < int(current.data):
            current = current.left
        elif value > int(current.data):
            current = current.right
        else:
            break
    
    return closest




T = BST()
inp,num = [i for i in input('Enter Input : ').split('/')]
data = [int(i) for i in inp.split()]
for i in data:
    root = T.insert(i)
    T.printTree(root)
    print('--------------------------------------------------')
print('Closest value of '+str(num)+' : '+str(closestValue(root,int(num))))