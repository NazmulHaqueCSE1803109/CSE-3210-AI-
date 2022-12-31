nterm=int(input("how many item do you need ?"))
n1=0
n2=1
for i in range (0,nterm):
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
