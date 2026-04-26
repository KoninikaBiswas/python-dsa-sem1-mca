marks1=int(input("Enter the marks in Maths: "))
marks2=int(input("Enter the marks in Physics: "))
marks3=int(input("Enter the marks in Computer: "))
marks4=int(input("Enter the marks in Chemistry: "))
total=marks1+marks2+marks3+marks4
avg=float(total/4)
print("Total marks:",total)
print("Average marks:",avg)
if(avg<0 or avg>100):
    print("The given input is invalid")
elif(avg>=60 and avg<=100):
    print("1st Division")
elif(avg>=45 and avg<=59.99):
    print("2nd Division")
elif(avg>=30 and avg<=44.99):
    print("3rd Division")
else:
    print("Fail")