

def perket(arr,sour,bits):
    if len(arr) == 0:
        return abs(sour-bits)
    else:
        a,b = arr[0].split()
        sour*=int(a)
        bits+=int(b)
        arr.remove(arr[0])
        return perket(arr,sour,bits)

inputString = [e for e in input('Enter Input : ').split(',')]

print(perket(inputString,1,0))



