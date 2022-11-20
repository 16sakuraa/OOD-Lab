class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    def __init__(self,item,table,maxCollision,threshold):
        self.table = table
        self.maxCollision = maxCollision
        self.item = item
        self.threshold = threshold
    
    
    def tableFull(self):
        for i in self.item:
            if i is None:
                return False
        return True

    def thresholdCheck(self):
        count = 0
        for i in self.item:
            if i is not None:
                count+=1
        maxThreshold = (self.threshold*self.table)//100
        if count > maxThreshold:
            print('****** Data over threshold - Rehash !!! ******')
            nextPrime = self.getPrime()
            self.table = nextPrime
            self.item.extend([None]*(nextPrime - len(self.item)))
            return

    
    def getPrime(self):
        for Number in range (1, 101):
            count = 0
            for i in range(2, (Number//2 + 1)):
                if(Number % i == 0):
                    count = count + 1
                    break
            if (count == 0 and Number != 1):
                if Number > self.table*2:
                    nextPrime = Number
                    break
        return nextPrime

    def QuadraticProb(self,number):
        index = number%self.table
        colCount = 1
        while self.item[index] != None:
            # collision number 1 at 0
            print('collision number '+str(colCount)+' at '+str(index))
            if colCount >= self.maxCollision:
                print('****** Max collision - Rehash !!! ******')
                colCount=0
                nextPrime = self.getPrime()
                self.table = nextPrime
                self.item.extend([None]*(nextPrime - len(self.item)))
                
            index = (number+pow(colCount,2))%self.table
            colCount+=1
        return index
    
    def printTable(self):
        for i in range(len(self.item)):
            print('#'+str(i+1)+"	"+str(self.item[i]))
        print("----------------------------------------")

def getAsciiSum(string):
    index = 0
    stringAscii = [ord(c) for c in string]
    for i in stringAscii:
        index += int(i)
    return index

print(' ***** Rehashing *****')
setting,dataN = input('Enter Input : ').split('/')
sizeTable,maxColli,threshold = [int(e) for e in setting.split()]

Table = [None]*sizeTable

Hash = hash(Table,sizeTable,maxColli,threshold)
dataList = dataN.split()
print('Initial Table :')
Hash.printTable()
for i in dataList:
    print('Add : '+str(i))
    insertAt = Hash.QuadraticProb(int(i))
    if insertAt != None:
        Table[insertAt] = i
    Hash.thresholdCheck()
    Hash.printTable()
    
