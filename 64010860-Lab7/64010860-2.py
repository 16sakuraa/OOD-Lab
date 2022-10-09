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

    def findBelow(self,node,num):
        global list
        if node:
            if int(node.data) < int(num):
                list.append(node.data)
                self.findBelow(node.right,num)
                self.findBelow(node.left,num)
            else:
                self.findBelow(node.right,num)
                self.findBelow(node.left,num)
               
        return list

def listSorting(l):
        toStr = ''
        for i in range(len(l)):
            for j in range(i + 1, len(l)):

                if l[i] > l[j]:
                    l[i], l[j] = l[j], l[i]
        
        if len(l)==0:
            print('Not have')
        else:
            for i in l:
                toStr += str(i)+' '
        print(toStr)


list = []
T = BST()
inp,num = [i for i in input('Enter Input : ').split('|')]
inpdata = [int(i) for i in inp.split()]
for i in inpdata:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print('Below '+num+' : ',end='')
res = T.findBelow(root,num)
listSorting(res)

