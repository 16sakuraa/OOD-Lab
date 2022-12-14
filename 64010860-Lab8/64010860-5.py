
class Node:

    def __init__(self, data): 

        self.data = data  

        self.left = None  

        self.right = None 

        self.level = None 



    def __str__(self):

        return str(self.data) 



class Tree:

    def __init__(self): 

        self.root = None

        self.num = 0



    def insert(self, val):  

        if self.root == None:

            self.root = Node(val)

            self.num += 1

        else:

            h = height(self.root)

            max_node = pow(2,h+1)-1

            current = self.root

            if self.num+1 > max_node:

                while(current.left != None):

                    current = current.left

                current.left = Node(val)

                self.num+=1

            elif self.num+1 == max_node:

                while(current.right != None):

                    current = current.right

                current.right = Node(val)

                self.num+=1

            else:

                print(max_node-((max_node-(pow(2,h)-1))/2))

                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):

                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val)

                else:

                    insert_subtree(current.right,self.num - pow(2,h),val)

                self.num+=1

                    

def insert_subtree(r,num,val):

    if r != None:

        h = height(r)

        max_node = pow(2,h+1)-1

        current = r

        if num+1 > max_node:

            while(current.left != None):

                current = current.left

            current.left = Node(val)

            return

        elif num+1 == max_node:

            while(current.right != None):

                current = current.right

            current.right = Node(val)

            return

        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):

            insert_subtree(current.left,num - round(pow(2,h)/2),val)

        else:

            insert_subtree(current.right,num - pow(2,h),val)

    else:

        return



def height(root):

    if root == None:

        return -1

    else:

        left = height(root.left)

        right = height(root.right)

        if left>right:

            return left + 1

        else:

            return right + 1

                       

def printTree90(node, level = 0):

    if node != None:

        printTree90(node.right, level + 1)

        print('     ' * level, node)

        printTree90(node.left, level + 1)


def check_binary_search_tree_(node, min, max):

    global leftNode
    global rootData
    global count
 

    if node is None:
        return True
    count+=1

    if node.data >= min or node.data <= max:
        return False

    if count <= int(leftNode) and count!=0:
        if node.data >= rootData:

            return False
    elif count > leftNode:
        if node.data <= rootData:
            return False

    return (check_binary_search_tree_(node.left, node.data, 0) and check_binary_search_tree_(node.right, 100, node.data))

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



tree = Tree()

data = input("Enter Input : ").split()

for e in data:

    tree.insert(int(e))

printTree90(tree.root)
if tree.root is not None:
    leftNode = TotalNodes(tree.root.left)
    rootData = tree.root.data
    count = -1
    print(check_binary_search_tree_(tree.root,100,0))
else:
    print('False')