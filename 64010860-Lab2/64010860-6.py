def Rshift(num,shift):
    newnum = num >> shift
    return  newnum



n,s = input("Enter number and shiftcount : ").split()
print(Rshift(int(n),int(s)))