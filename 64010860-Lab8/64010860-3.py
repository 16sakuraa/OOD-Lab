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


def getRank(node,num,rootRank):
    print(rootRank)
    while node:
        if num > node.data:
            node = node.right
            rootRank+=1
        elif num < node.data:
            node = node.left
            rootRank-=1
        else:
            break
    print(rootRank)
    return rootRank

def left_height(node):
    ht = 0
    while(node):
        ht += 1
        node = node.left
        
    return ht
  
def right_height(node):
    ht = 0
    while(node):
        ht += 1
        node = node.right

    return ht
  
def TotalNodes(root):
    
    if(root == None):
        return 0
        
    lh = left_height(root)
    rh = right_height(root)
      
    if(lh == rh):
        return (1 << lh) - 1
        
    return 1 + TotalNodes(root.left) + TotalNodes(root.right)
    # 7 4 3 1 2 6 9 12 5 11/10


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

def minValueNode(node):
    current = node
    if current is None:
        return None
  
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
  
    return current

    
    


T = BST()
inp,num = [i for i in input('Enter Input : ').split('/')]
data = [int(i) for i in inp.split()]
for i in data:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
total = TotalNodes(root.left)
getRank(root,int(num),total+1)
# inOrder(root)