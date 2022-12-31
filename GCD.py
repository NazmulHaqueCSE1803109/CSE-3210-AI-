def gcd(n1,n2):
    if n1>=n2:
        g=n1
        l=n2
    else:
        g=n2
        l=n1
    while 1:
        r=g%l
        if r==0:
            break;
        g=l
        l=r
    return l
n1=int(input("Enter the value of n1 : "))
n2=int(input("Enter the value of nw : "))
print("GCD of n1 and n2 is : ",gcd(n1,n2))