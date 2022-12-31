def Fibonacci(n):
    if n<0:
        print("Invalid input\n")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
nterm=int(input("Enter the value of n fo nth fibonacci : "))
print("Fibonacci(nth term) : ",Fibonacci(nterm))