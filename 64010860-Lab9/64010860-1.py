num = [int(e) for e in input('Enter Input : ').split()]

if (num[0] <= num[1]):

    for i in range(1,len(num)-1):
        if num[i] >= num[i+1]:
            print('No')
            exit()
    print('Yes')

elif (num[0] > num[1]):

    for i in range(1,len(num)-1):
        if num[i] < num[i+1]:
            print('No')
            exit()
    print('Yes')