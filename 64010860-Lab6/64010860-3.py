
def gcd(a,b):
    r = a%b
    if r==0:
        if b<0:
            return -b
        else:
            return b
    else:
        return gcd(int(b),int(r))

a,b = input('Enter Input : ').split()

if int(a)==0 and int(b)==0:
    print('Error! must be not all zero.')
elif int(a)>=int(b):
    print('The gcd of '+str(a)+' and '+str(b)+' is : '+str(gcd(int(a),int(b))))
elif int(a)<int(b):
    print('The gcd of '+str(b)+' and '+str(a)+' is : '+str(gcd(int(a),int(b))))