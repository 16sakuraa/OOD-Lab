class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur = self.tail
        s = str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        newnode = Node(value=item)
        last = self.head
        newnode.next = None

        if self.head is None:
          #  self.head.previous = None
            self.head = newnode
            self.tail = newnode
            return
        
        while (last.next is not None):
            last = last.next
        
        last.next = newnode
        newnode.previous = last
        self.tail = newnode
            

    def addHead(self, item):
        
        newnode = Node(value=item)
        newnode.next = self.head
        newnode.previous = None

        if self.head is not None:
            self.head.previous = newnode
        
        if self.head is None:
            self.tail = newnode

        self.head = newnode

    def insert(self, pos, item):
        if pos==0:
            self.addHead(item)
            return
        elif pos<0:
            pos = self.size()+pos
            if pos<0:
                self.addHead(item)
                return
        elif pos==self.size():
            self.append(item)
            return

        count=0

        newnode = Node(value=item)

        itr = self.head
        while itr:
            if count == pos-1:
                newnode.next = itr.next
                newnode.previous = itr
                itr.next = newnode
                break

            itr = itr.next
            count +=1

    def search(self, item):
        itr = self.head
        while itr:
            if itr.value == item:
                #print('Found')
                return 'Found'
            itr = itr.next
        #print('Not Found')
        return 'Not Found'



    def index(self, item):
        itr = self.head
        count = 0
        while itr:
            if itr.value == item:
                return count
            itr = itr.next
            count+=1
        return -1

    def size(self):
        size = 0
        itr = self.head
        while itr:
            itr = itr.next
            size+=1
        #print(size)
        return size

    def pop(self, pos):
        if pos<0 or self.size()<=pos:
            #print('Out of range')
            return 'Out of range'

        # elif pos==0 and self.size()!=0:
        #     self.head = self.head.next
        #     print('Out of range')
        
        count=0
        itr = self.head
        while itr:
            if pos==0:
                self.head = self.head.next
                return 'Success'
            elif count == pos-1:
                itr.next = itr.next.next
                return 'Success'
            itr = itr.next
            count+=1
    
    def print(self):
        if self.head is None:
            print('This linked list is empty')
            return
        
        itr = self.head
        liststr = ''

        while itr:
            #print(itr)
            if itr.next is None:
                liststr += str(itr.value)
            else:
                liststr += str(itr.value) + ' <- '
            itr = itr.next
            
        print(liststr)

L = LinkedList()
# L.addHead('1')
# L.addHead('3')
# L.print()
# L.append('4')
# L.print()
# L.insert(2,'5')
# L.print()
# L.append('6')
# L.print()
# L.search('2')
# L.size()


inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())

