class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
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


    def delete(self,r, data):

        if r is None:
            print('Error! Not Found DATA')
            return r
        else:
            if data < r.data:
                r.left = self.delete(r.left,data)
                return r
        
            elif data > r.data:
                r.right =self.delete(r.right,data)
                return r

            elif data == r.data:
                
                # if r.left is None and r.right is None:
                #     print('hello1')
                #     r = None
                #     return r
                if r.left is None:
                    #print('hello')
                    temp = r.right
                    r = None
                    return temp
                elif r.right is None:
                    temp = r.left
                    r = None
                    return temp

                    
        

                temp = minValueNode(r.right)

                r.data = temp.data
                r.right = self.delete(r.right,temp.data)

                return r

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def minValueNode(node):
    current = node
  
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
  
    return current


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")

for x in data:
    action,num = x.split()
    if action[0] == 'i':
        print('insert '+num)
        tree.insert(num)
        printTree90(tree.root)
    elif action[0] == 'd':
        print('delete '+num)
        tree.delete(tree.root,num)
        printTree90(tree.root)
