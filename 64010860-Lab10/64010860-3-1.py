class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    def __init__(self,item,table,maxCollision):
        self.table = table
        self.maxCollision = maxCollision
        self.item = item
    
    
    def tableFull(self):
        for i in self.item:
            if i is None:
                return False
        return True

    def QuadraticProb(self,number):
        index = number%self.table
        colCount = 1
        while self.item[index] != None:
            # collision number 1 at 0
            print('collision number '+str(colCount)+' at '+str(index))
            if colCount >= self.maxCollision:
                print('Max of collisionChain')
                return
            index = (number+pow(colCount,2))%self.table
            colCount+=1
        return index
    
    def printTable(self):
        for i in range(len(self.item)):
            print('#'+str(i+1)+"	"+str(self.item[i]))
        print("---------------------------")

def getAsciiSum(string):
    index = 0
    stringAscii = [ord(c) for c in string]
    for i in stringAscii:
        index += int(i)
    return index

print(' ***** Fun with hashing *****')
tableMax,dataN = input('Enter Input : ').split('/')
sizeTable,maxColli = [int(e) for e in tableMax.split()]

Table = [None]*sizeTable

Hash = hash(Table,sizeTable,maxColli)
dataList = dataN.split(',')
# print(dataN)
for i in dataList:
    if Hash.tableFull():
        print('This table is full !!!!!!')
        break
    key,value = i.split()
    insertAt = Hash.QuadraticProb(getAsciiSum(key))
    if insertAt != None:
        Table[insertAt] = Data(key,value)
    Hash.printTable()
    
