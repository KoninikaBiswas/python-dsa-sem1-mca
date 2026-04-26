n=int(input("Enter a number: "))
print(f"The reverse of {n} is: ")
while(n>0):
    r=n%10
    print(r,end="")
    n=n//10
