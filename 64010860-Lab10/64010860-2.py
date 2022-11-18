
def firstGreaterValue(data,num):
    value = None
    dif = 1000000
    for i in data:
        if i-num < dif and i-num >0:
            dif = i-num
            value = i
    if value is None:
        return 'No First Greater Value'
    return value


inp,num = input('Enter Input : ').split('/')

data = [int(e) for e in inp.split()]
searchNum = [int(e) for e in num.split()]

for i in searchNum:
    print(firstGreaterValue(data,i))
