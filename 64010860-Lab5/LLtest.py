class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Linklist:
    def __init__(self):
        self.head = None
    
    def insertFirst(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insertLast(self,data):

        if self.head is None:
            self.head = Node(data,None)
            return 

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data,None)

    def print(self):
        current = self.head
        liststr = ''

        while current:
            if current.next is None:
                liststr += str(current.data)
            else:
                liststr += str(current.data) + ' -> '
            current = current.next
        
        print(liststr)

    def insertAt(self,data,index):
        count = 0
        current = self.head

        while current:
            if count==index-1:
                node = Node(data,current.next)
                current.next = node
            count+=1
            current = current.next

    def removeAt(self,index):
        count = 0
        current = self.head
        while current:
            if count==index-1:
                current.next = current.next.next

            count+=1
            current = current.next

inputlist = [e for e in input('enter numbers : ').split()]

LL = Linklist()
for x in inputlist:
    LL.insertLast(x)

LL.print()
LL.insertAt(6,2)
LL.print()
LL.removeAt(2)
LL.print()
