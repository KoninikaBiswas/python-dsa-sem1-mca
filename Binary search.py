arr=[]
l=int(input("Enter the lower bound: "))
r=int(input("Enter the upper bound: "))
for i in range(r):
    element=int(input(f"Enter element{i+1}:"))
    arr.append(element)
print("The array is:",arr)
data=int(input("Enter the data to be searched: "))
while(l<r):
    mid=(l+r)//2
    if(arr[mid]==data):
        print("Element is present at index",mid+1)
        break
    elif(arr[mid]>data):
        l=mid+1
    else:
        r=mid-1
if(l>r):
    print("Element not found!")