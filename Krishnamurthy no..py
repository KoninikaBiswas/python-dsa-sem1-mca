num=int(input("Enter a number:"))
temp=num
sum=0
if (temp<0):
    print("Special number is not defined for negative number")
else:
    while(temp>0):
        r=temp%10
        fact=1
        for i in range(1,r+1):
            fact=fact*i
        sum=sum+fact
        temp=temp//10
    if(sum==num):
        print("The given no. is Special")
    else:
        print("The given no. is not Special")