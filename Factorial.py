n=int(input("Enter the value of n : "))
fact=1
if n<0:
    print("\nit's imposible\n")
elif n==0:
    print("\nFactorial of n is : 1\n")
else:
    for i in range(1,n+1):
        fact *=i
    print("\nFactorial of ",n, " is : ",fact)
    print("\n")