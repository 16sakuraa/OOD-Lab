class LinkedList():
    class Node():

        def __init__(self,data,prev = None,next = None) :
            self.data = data
            if prev is None :
                self.prev = None
            else :
                self.prev = prev
            if next is None :
                self.next = None
            else :
                self.next = next
            
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

        def __str__(self):
            return str(self.data)
            
    def __init__(self, max):
        self.head = None
        self.tail = None
        self.max = max
        self.count = 0
        self.max_length = 1

    def push(self, value):
        node = self.Node(value)
        if int(value) > 0:
            self.max_length = max(self.max_length, len(value))
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next, node.prev = node, self.head
            self.head = node
        self.count+=1
    
    def sort(self):
        temp = []
        if not self.isEmpty():
            while not self.isEmpty():
                temp.append(int(self.pop_front()))
            for x in sorted(temp):
                self.push_front(str(x))

    def push_back(self, value):
        node = self.Node(value)
        if int(value) > 0:
            self.max_length = max(self.max_length, len(value))
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next, node.prev = node, self.head
            self.head = node
        self.count+=1

    def push_front(self, value):
        node = self.Node(value)
        if int(value) > 0:
            self.max_length = max(self.max_length, len(value))
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.prev, node.next = node, self.tail
            self.tail = node
        self.count+=1

    def pop_front(self):
        temp = self.tail.data
        try:
            self.tail = self.tail.next
            self.tail.prev = None  
            self.count-=1
        except:
            self.head = None
            self.tail = None
            self.count = 0
        return temp

    def __str__(self):
        temp = ''
        current = self.tail
        while current:
            temp += str(current.data) + ' -> '
            current = current.next
        return temp[:-3]

    def nodeAt(self,i) :          
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p

    def printLL(self):
        temp = ''
        current = self.tail
        while current:
            temp += str(current.data) + ' '
            current = current.next
        return temp
    
    def length(self):
        return self.count

    def get_max_length(self):
        return str(self.max_length-1)

    def isEmpty(self):
        return self.count == 0

    def radixsort(self):
        box = []
        for i in range(10):
            box.append(LinkedList(0))
        print("------------------------------------------------------------")
        stop = False
        counter = 0
        for i in range(self.max_length+1):
            print("Round : " + str(i+1))
            while not self.isEmpty():
                temp = self.pop_front()[::-1]
                try:
                    box[int(temp[i])].push_front(temp[::-1])   
                except:
                    box[0].push_front(temp[::-1])
            if box[0].length() == self.max:
                stop = True
            for j in range(10):
                box[j].sort()
                print(str(j) + ' : ' + box[j].printLL())
                while not box[j].isEmpty():
                    temp = box[j].pop_front()
                    self.push_back(temp)
            print("------------------------------------------------------------")
            counter += 1
            if stop:
                break
        self.max_length = counter

    


inputString = input("Enter Input : ").split()
LLsorted = LinkedList(len(inputString))
LLstring = LinkedList(len(inputString))
for x in inputString:
    LLsorted.push(x)
    LLstring.push(x)

LLsorted.radixsort()

print(LLsorted.get_max_length() + ' Time(s)')
print('Before Radix Sort : ' + str(LLstring))
print('After  Radix Sort : ' + str(LLsorted))