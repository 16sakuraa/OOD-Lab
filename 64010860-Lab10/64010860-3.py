class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    def __init__(self,table,maxCollision):
        self.table = table
        self.maxCollision = maxCollision
        self.dataList = []
    
    def getIndex(self,string):
        index = 0
        stringAscii = [ord(c) for c in string]
        for i in stringAscii:
            index += int(i)
        index = index%table # modulo by max table
        return index

    def insert(self,data):
        key,value = data.split()
        node = Data(key,value)
        index = self.getIndex(key)
        if self.dataList[index] is None:
            self.dataList[index] = node
        
        for i in range(0,self.table-1):
            # #1	(1+1, I)
            print('#'+str(i+1)+'	')
            print(self.dataList[i])







print(' ***** Fun with hashing *****')
tableMax,dataN = input('Enter Input : ').split('/')
table,maxColli = [int(e) for e in tableMax.split()]
dataList = dataN.split(',')
table1 = hash(table,maxColli)
print(dataN)
for element in dataList:
    table1.insert(element)
