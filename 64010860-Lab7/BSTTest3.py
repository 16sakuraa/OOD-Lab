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
        if currentNode.data < data:
            if currentNode.right is None:
                currentNode.right = Node(data)
            else:
                self._insert(data,currentNode.right)
        elif currentNode.data > data:
            if currentNode.left is None:
                currentNode.left = Node(data)
            else:
                self._insert(data,currentNode.left)
    
    def delete(self,data,currentNode):
        if currentNode is None:
            print('not found')
        elif currentNode.data < data:
            currentNode.right = self.delete(data,currentNode.right)
        elif currentNode.data > data:
            currentNode.left = self.delete(data,currentNode.left)
        elif currentNode.data == data:
            
            if currentNode.left is None:
                temp = currentNode.right
                currentNode = None
                return temp
            elif currentNode.right is None:
                temp = currentNode.left
                currentNode = None
                return temp

            temp = minValueNode(currentNode.right)
            currentNode.data = temp.data
            currentNode.right = self.delete(temp.data,currentNode.right)
        
        return currentNode


            
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

def minValueNode(node):
    current = node
    if current is None:
        return
    
    while current.left is not None:
        current = current.left

    return current


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
T.delete(3,root)
T.printTree(root)