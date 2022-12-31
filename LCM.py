def lcm(n1,n2):
    if n1>=n2:
        l=n1
    else:
        l=n2
    while 1:
        if l%n1==0 and l%n2==0:
            break;
        else:
            l=l+1
    return l
n1=int(input("Enter the value of n1 : "))
n2=int(input("Enter the value of n2 : "))
print("LCM of n1 and n2 is : ",lcm(n1,n2))