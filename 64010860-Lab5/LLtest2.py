class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insertFirst(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        node.prev = None
        self.head = node
    
    def insertLast(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        # current = self.tail
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def print(self):
        liststr = ''
        current = self.head
        while current:
            if current.next is None:
                liststr += str(current.data)
            else:
                liststr += str(current.data) + ' -> '
            current = current.next
        print(liststr)



inputstring = [e for e in input('enter number : ').split()]

LL = LinkedList()

for x in inputstring:
    LL.insertLast(x)

LL.print()
LL.insertFirst(5)
LL.insertFirst(9)
LL.print()

        