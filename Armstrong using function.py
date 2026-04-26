def digits(num):
    count=0
    while(num>0):
        num=num//10
        count=count+1
    return count
def calArmstrong(num):
    arm=0
    power=digits(num)
    while(num>0):
        rem=num%10
        arm=arm+(rem**power)
        num=num//10
    return arm
def isArmstrong(num):
    if(calArmstrong(num)==num):
        print("The given no. is Armstrong")
    else:
        print("The given no. is not Armstrong")
num=int(input("Enter a number:"))
isArmstrong(num)