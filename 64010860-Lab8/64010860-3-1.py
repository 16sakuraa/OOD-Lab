class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.freq = 0
    
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


def inOrder(root):
    global numlist
    if (root):
        inOrder(root.left)
        numlist.append(int(root.data))
        inOrder(root.right)

def rank(data):
    global numlist
    i=0
    rank=1
    if data > max(numlist):
        return len(numlist)
    elif data < min(numlist):
        return 0

    while (data>=numlist[i+1]):
        rank+=1
        i+=1


    return rank




    
    


T = BST()
inp,num = [i for i in input('Enter Input : ').split('/')]
data = [int(i) for i in inp.split()]
for i in data:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
numlist = []
inOrder(root)
print('Rank of '+str(num)+' : '+str(rank(int(num))))