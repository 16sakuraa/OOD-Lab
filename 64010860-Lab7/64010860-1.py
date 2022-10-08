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
            return
        elif self.root.left is None:
            self.root.left = Node(data)
            return
        elif self.root.right is None:
            self.root.right = Node(data)
            return
        else:
            if self.root.data == data:
                return 
            elif self.root.data < data:
                self.root.left = self.insert(data)
                return
            elif self.root.data > data:
                self.root.right = self.insert(data)
                return
        return
           
         
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)