
output = []
def sortNum(n,arr):
    if n==1:
        output.append(arr[0])
        return str(output)
    else:
        output.append(max(arr))
        arr.remove(max(arr))
        return sortNum(n-1,arr)


inputNumber = [int(e) for e in input('Enter your List : ').split(',')]
n = len(inputNumber)
outputstr = sortNum(n,inputNumber)
print('List after Sorted : '+str(outputstr))
