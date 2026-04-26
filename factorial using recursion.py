def fact(n):
    f=1
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter No:"))
if n>=0:
    r=fact(n)
    print("Result=",r)
else:
    print("Wrong Input")