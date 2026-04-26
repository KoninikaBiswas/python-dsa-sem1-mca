
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
x=int(input("Enter a number:"))
y=int(input("Enter another number:"))
x=abs(x)
y=abs(y)
lcm=(x*y)//gcd(x,y)
print("The lcm is:",lcm)